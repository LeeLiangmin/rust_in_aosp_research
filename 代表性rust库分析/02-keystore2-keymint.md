# 案例报告 02：keystore2 / KeyMint —— 把类型系统当作安全策略语言

> 代码来源：`G:\aosp-scan\platform_system_keymint`（AOSP main，2026-08）
> 规模：69 个 .rs 文件 / 23,392 行；unsafe 块仅 27 处（约 0.12%，采样库中最低档）
> 架构位置：纵贯 ③ Native（keystore2 守护进程，Rust 50,865 行）→ ④ HAL（KeyMint AIDL）→ ⑥ TEE（Trusty TA）

## 1. 问题定义：这个位置为什么难

密钥体系是全 Android 安全的根，它的工程难度是三重叠加：

- **资产最贵**：密钥材料一旦泄露/被替换，设备解锁、支付、应用签名全部沦陷；
- **输入不可信**：HAL 与 TA 之间的每条消息都可能是恶意构造的 CBOR；
- **环境最苛刻**：TEE 内存稀缺不可换页、无 OS 设施、无 GC 容忍度，还要求与用户态共享逻辑。

前身 C++ keystore/Keymaster 的失败史正是这三重压力的记录：内存类漏洞反复出现、协议解析手写 switch 对未知值静默放行、TEE 里 `malloc` 失败处理靠自觉。Google 在 Android 12 同时做了两个决定：守护进程整体用 Rust 重写（keystore2），HAL 接口换 AIDL 并把支持库做成 Rust 公共底座（KeyMint）。后者是本报告主体。

## 2. Rust 设计方案：五个机制逐层拆解

### 2.1 枚举即状态机：密码运算的生命周期建模

TEE 内的密码操作是典型状态机：begin → update(aad/data) → finish，不同算法允许的操作序列不同。C 的惯例是 `void* ctx` + 类型 tag + 手写 dispatch——tag 与指针不匹配就是类型混淆漏洞。KeyMint 的写法（`ta/src/operation.rs`）：

```rust
/// Union holder for in-progress cryptographic operations, each of which is an
/// instance of the relevant trait.
pub(crate) enum CryptoOperation {
    Aes(Box<dyn EmittingOperation>),
    AesGcm(Box<dyn AadOperation>),
    HmacSign(Box<dyn AccumulatingOperation>, usize),          // tag length
    HmacVerify(Box<dyn AccumulatingOperation>, Range<usize>), // 合法长度区间
    RsaSign(Box<dyn AccumulatingOperation>),
    ...
}

pub(crate) struct Operation {
    pub aad_allowed: bool,   // 仅 AEAD 在数据到达前允许 update_aad
    pub slot_to_delete: Option<keyblob::SecureDeletionSlot>,
    pub crypto_op: CryptoOperation,
    ...
}
```

**机制解读**：带数据的枚举让"操作类型"与"该类型所需的全部状态"绑定——`HmacVerify` 变体**自带**合法 tag 长度区间，`AesGcm` 变体的 trait 对象**只有** `AadOperation` 能力。想对 RSA 操作调 aad 更新？类型上不存在这个接口。状态标志（`aad_allowed`）是显式字段而非隐藏约定。

更进一步，`check_size` 按枚举分支施加**逐算法的输入上限**：

```rust
fn check_size(&mut self, len: usize) -> Result<(), Error> {
    self.input_size += len;
    let max_size = match &self.crypto_op {
        CryptoOperation::HmacSign(op, _) | ... => op.max_input_size(),
        ...
    };
    ...
}
```

TEE 内存稀缺，无界累积输入即是 DoS。C 里这类限制常因"每种算法上限不同"而被简化掉；这里 match 穷尽每个变体，漏一个分支就是编译错误。

### 2.2 密钥材料的两道类型级防线

**防线一：用后即焚**。`common/src/keyblob.rs` 引入 `zeroize::ZeroizeOnDrop`——敏感材料的类型挂上此 derive 后，离开作用域时内存被显式清零。C 里"密钥用完 memset"有两个经典死法：程序员忘记；编译器把"无用"的 memset 优化掉（CVE 史上反复出现）。Rust 的 `Drop` 语义保证清零必然发生且不被优化（zeroize 使用 volatile 写入）。

**防线二：格式演进建模为类型**：

```rust
pub enum EncryptedKeyBlob {
    V1(EncryptedKeyBlobV1),
    // Future versions go here...
}
pub fn new(data: &[u8]) -> Result<Self, Error> {
    Self::from_slice(data)
        .map_err(|e| km_err!(InvalidKeyBlob, "failed to parse keyblob: {:?}", e))
}
```

keyblob 是落盘的长期资产，格式必然演进。版本是枚举变体而非魔法数字，未来加 V2 时编译器会强制遍历所有 `match` 点——**格式升级漏改一个分支也是编译错误**。

### 2.3 协议守门：非法输入在类型边界死亡

HAL↔TA 的 CBOR 消息里每个枚举标签先过 `TryFrom`（`wire/src/lib.rs` 的 `try_from_n!` 宏）：未知值变成 `ValueNotRecognized` 类型化错误，在反序列化阶段即被拒绝——**非法状态根本无法进入业务逻辑**。C 的 `switch + default:` 静默忽略或继续传递的写法，正是协议级漏洞（类型混淆、状态机错位）的温床。

### 2.4 trait 对象组合：厂商可插拔的安全底座

KeyMint 把全部密码原语抽象为 trait，厂商以 `Implementation` 结构体"组装"自家硬件实现（`common/src/crypto/traits.rs`）：

```rust
pub struct Implementation {
    pub rng: Box<dyn Rng>,
    pub compare: Box<dyn ConstTimeEq>,  // 文档明言：用于需要避免时序攻击的场景
    pub aes: Box<dyn Aes>,
    pub rsa: Box<dyn Rsa>,
    ...
}
pub trait ConstTimeEq: Send { fn eq(&self, left: &[u8], right: &[u8]) -> bool; ... }
```

**机制解读**：C 的对应物是函数指针表 + `void* context`——没有类型检查、没有线程安全约束、没有文档强制。这里每个 trait 都带 `Send` bound（厂商实现必须线程安全，编译期校验），`ConstTimeEq` 这种安全关键属性被单独命名成 trait——**"这里必须常数时间比较"从注释升级为类型**。Google 把 HAL 支持库做成这套 trait 组合，意味着厂商拿到的不是示例代码，而是一个"插错就编译不过"的骨架。

### 2.5 no_std + 可失败分配：TEE 的入场券

`wire`/`ta`/`boringssl` 三个 crate 都是 `#![no_std] + extern crate alloc`——同一批代码编进 std 用户态与 Trusty TEE。且分配失败被建模为类型化错误：

```rust
pub fn vec_try_fill_with_alloc_err<T: Clone, E>(...) -> Result<Vec<T>, E> {
    let mut v = alloc::vec::Vec::new();
    v.try_reserve(len).map_err(|_e| alloc_err())?;
    ...
}
```

TEE 里 OOM 必须可恢复；C 的 `malloc` NULL 检查无类型支撑，GC 语言则因运行时依赖直接出局。**"与用户态共享逻辑 + 分配失败可恢复 + 无运行时"这三件事同时成立的语言，只有 Rust。**

## 3. 竞争力分析

**这个案例证明了什么**：当安全策略足够复杂（操作状态机、格式版本、逐算法资源上限、常数时间要求、密钥擦除），它就不再能靠"写文档 + code review"维持——KeyMint 的做法是把每条策略翻译成类型。类型系统的表达力在这里不是工程美学，而是**安全策略的载体**：策略越复杂，Rust 相对 C/C++ 的优势越大。

**生态杠杆**：`system/keymint` 以 rust_library 形态成为**全体 SoC 厂商复用的底座**——厂商写自家 HAL/TA 时站在 23,392 行、unsafe 密度 0.12% 的审计过的代码上。Rust 的 trait 组合让"可复用底座 + 厂商定制"这个 C 时代的痛点（复制粘贴改 Bug 满天飞）变成了类型约束下的填空。

**交付闭环**：AIDL 接口不变、接口之下换语言——上层 App 与厂商生态零成本；同批 no_std crate 直通 TEE；4 个 fuzz target 常驻 CI（"Do we trust it? I don't think so..."）。

**诚实的代价**：`Box<dyn Trait>` 动态分发有极小性能开销（密码路径可忽略）；trait 骨架约束了厂商的自由度，遇到 trait 未覆盖的硬件能力需要向上演进接口。unsafe 虽少（27 块）但仍在 FFI 与底层处，审计不可省。

## 4. 结论

KeyMint 是"类型系统作为安全策略语言"的最完整样本：状态机、版本、资源上限、时序安全、内存擦除，五条安全策略全部编译期化。keystore2 上线至今无内存安全漏洞，不是运气——漏洞类别在类型层面就不存在。这回答了"为什么最高价值资产该第一个用 Rust 重写"：**资产越贵，越值得把保护它的规则交给不会疲倦、不会被说服、不会被绕过的检查器**。
