# 案例报告 04：libavb-rust —— 用生命周期验证 C 的所有权契约

> 代码来源：`G:\aosp-scan\platform_external_avb\rust`（AOSP main，2026-08）
> 规模：17 个 .rs 文件 / 5,407 行；unsafe 块 95 处、unsafe fn/impl 26 处，全部带 SAFETY 论证
> 架构位置：⑥ 固件层（bootloader / pvmfw），运行在内核启动之前、普通世界之外

## 1. 问题定义：这个位置为什么难

libavb 是 Android Verified Boot 的验证库：设备上电后校验 boot/vbmeta/vendor 分区签名与完整性，把信任从硬件 root-of-trust 逐层延伸到操作系统。它的环境是 AOSP 里最苛刻的：

- **无 OS、无动态链接、无 GC 容忍度**——bootloader 与 pvmfw（受保护 VM 的第一段代码）里只有裸机设施；
- **验证逻辑本身是高危解析**：vbmeta 镜像里的描述符（descriptor）是可变长、可嵌套的 TLV 结构，镜像可被替换/构造——**验证者的解析器自己就是攻击面**；
- **回调驱动架构**：C 版 libavb 通过 `AvbOps` 回调表让平台提供 IO，回调间的数据所有权关系全在文档里。

候选语言在这里被环境压缩到只剩 C/C++/Rust。Rust 封装层的意义，`rust/src/lib.rs` 注释说得最诚实："包一层安全 API 并不提升库本身的安全性（内部仍是 C）。目的是让 Rust 成为 bootloader 等场景更有吸引力的选择。"——**它是使能件：没有它，下游所有 Rust 固件（pvmfw 等）都得先重写验证逻辑。**

## 2. Rust 设计方案：四个机制逐层拆解

### 2.1 `Ops<'a>`：把 C 回调的所有权文档编码进生命周期

全库最精妙的设计。libavb 用 C 回调让平台提供分区读取；"预加载分区"优化改变了所有权模型——验证结果**借用**平台已加载的数据而非自己拷贝。C 里"这块数据必须活得比验证结果久"是一句文档约定，违反即 UAF。Rust 侧（`ops.rs`）：

```rust
/// # Lifetimes
/// The trait lifetime `'a` indicates the lifetime of any preloaded partition data.
/// ... Because of this borrow, we need the lifetime here to ensure that the
/// underlying data outlives the verification result object.
pub trait Ops<'a> {
    fn read_from_partition(&mut self, partition: &CStr, offset: i64,
                           buffer: &mut [u8]) -> IoResult<usize>;
    fn get_preloaded_partition(&mut self, _partition: &CStr) -> IoResult<&'a [u8]> {
        Err(IoError::NotImplemented)
    }
    ...
}
```

**机制解读**：生命周期参数 `'a` 把"预加载数据 ⊇ 验证结果"这条 C 契约变成了借用检查器验证的性质——平台实现者返回的 `&'a [u8]` 若活得不够久，**编译失败**。这是"用类型系统翻译 C 所有权文档"的教科书案例：文档会被忽略，借用检查器不会。

### 2.2 描述符解析：生命周期绑定的零拷贝 + 前向兼容

验证通过后，要从 vbmeta 镜像里提取描述符（hash/hashtree/chain…）。`descriptor/mod.rs`：

```rust
pub enum Descriptor<'a> {
    Property(PropertyDescriptor<'a>),
    Hashtree(HashtreeDescriptor<'a>),
    Hash(HashDescriptor<'a>),
    KernelCommandline(KernelCommandlineDescriptor<'a>),
    ChainPartition(ChainPartitionDescriptor<'a>),
    Unknown(&'a [u8]),   // 不认识的描述符类型：原样借用，静默跳过
}

pub enum DescriptorError {
    InvalidHeader,
    InvalidValue,
    InvalidSize,      // "descriptor claimed to be larger than the available data"
    InvalidUtf8,
    InvalidContents,
}
```

**机制解读**，三个设计叠加：

1. **零拷贝借用**：所有变体带 `'a`，描述符内容直接引用已验证的镜像内存，不复制——固件里内存金贵，而生命周期保证"镜像被释放后描述符不可再用"；
2. **`Unknown` 变体 = 前向兼容**：未来新描述符类型不会打爆旧解析器——协议演进被建模为枚举的一个正常分支，而非 C 里的 default 跳过后手工指针推进（推进错了就是越界）；
3. **`InvalidSize` 单独成错误变体**："描述符自称比可用数据还大"——解析器最经典的整数/长度混淆攻击，有专属的类型化拒绝路径。

### 2.3 unsafe 的规范形态：validate 前置 + SAFETY 举证

```rust
// verify.rs
#[repr(transparent)]
pub struct VbmetaData(AvbVBMetaData);   // 零拷贝包装 C 结构体

/// Validates the internal data so the accessors can be fail-free.
fn validate(&self) -> SlotVerifyNoDataResult<()> {
    check_nonnull(self.0.partition_name)?;
    check_nonnull(self.0.vbmeta_data)?;
    Ok(())
}

pub fn data(&self) -> &[u8] {
    // SAFETY:
    // * libavb gives us a properly-allocated byte array.
    // * the returned contents remain valid and unmodified while we exist.
    unsafe { slice::from_raw_parts(self.0.vbmeta_data, self.0.vbmeta_size) }
}
```

**机制解读**：`#[repr(transparent)]` 让安全抽象零性能税；`validate()` 把所有校验集中在对象暴露给用户之前，accessor 因此 "fail-free"（注释原话）——**校验一次，处处安全**，而不是每个调用点各自防御；每个 unsafe 块上方的 SAFETY 注释列出依赖的不变量，审计者只需核对这几行论证是否成立，不必通读整个 C 库。95 块 unsafe 全是这个形态。

### 2.4 构建层的封装纪律：生成代码永不外露

`rust/Android.bp` 的注释本身就是设计文档：

```text
// The auto-generated wrappers are Rust unsafe and somewhat difficult to work
// with so are not exposed outside of this directory; instead we will provide
// a safe higher-level Rust API.
```

bindgen 生成的 `avb_bindgen` 用 flags 强制 no_std（`--raw-line=#![no_std]`、`--use-core`）并派生 zerocopy trait；`visibility` 只放行本目录与 `packages/modules/Virtualization`——**不安全层被构建系统物理隔离，安全层是唯一出口**。封装不是约定，是构建规则。

## 3. 竞争力分析

**这个案例证明了什么**：Rust 的互操作竞争力不止是"能调 C"，而是**能在不修改 C 库的前提下，把 C 的隐含契约显式化并编译期执行**。`Ops<'a>` 证明生命周期参数可以承载跨语言所有权语义；`Descriptor<'a>` 证明零拷贝解析与前向兼容可以兼得。这些是 C++ 的智能指针、Go 的 cgo 都给不出的组合：C++ 没有借用检查器，文档约定无法升级；cgo 有运行时开销且生命周期靠 GC 兜底，进不了固件。

**使能者价值**：libavb-rust 自身安全收益有限（内部仍是 C），但它解锁的下游是整条固件 Rust 线——2023 年 pvmfw 全 Rust 化（pVM 信任根）、2026 年 Pixel 基带 Rust 组件，都踩在这层外壳上。**互操作层的价值要按它解锁的下游计算。**

**诚实的代价**：安全外壳的信任根仍是 C libavb 本体——外壳挡不住内部 C 代码自身的漏洞（其价值是防止"使用方出错"）；bindgen 层与手写层之间的不变量依赖 libavb C API 的稳定性；`'a` 生命周期设计对使用者的 Rust 素养有要求。

## 4. 结论

libavb-rust 是"渐进策略"最诚实的样本：不重写成熟 C 验证逻辑，而是包一层**会编译期执法的外壳**，让固件世界里的新代码从此可以用 Rust 写。它贡献了全 AOSP 最精炼的两个教学案例——`Ops<'a>`（生命周期验证 C 回调契约）与 `Descriptor<'a>`（零拷贝 + 前向兼容的解析）——证明了在最无退路的环境（无 OS、无 GC、攻击面即自身）里，Rust 的类型系统反而发挥得最淋漓尽致。
