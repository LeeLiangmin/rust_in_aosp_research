# 案例报告 03：蓝牙 GATT —— 一万行并发协议栈，零 unsafe

> 代码来源：`G:\aosp-scan\platform_packages_modules_Bluetooth`（AOSP main，2026-08）
> 规模：仓库 201 个 .rs 文件 / 74,246 行（采样中第一方 Rust 量最大）；本报告主体 `system/rust`（GATT）10,497 行，**`unsafe {}` 块为 0**
> 架构位置：③ Native 层，以 Mainline APEX `com.android.bt` 交付；④ offload HAL 亦为 Rust

## 1. 问题定义：这个位置为什么难

蓝牙栈是 Android 漏洞密度最高的子系统之一，原因是三种难度的叠加：

- **协议解析**：ATT/GATT/L2CAP 报文来自任何附近的设备，长度字段、MTU 协商全部不可信——C 解析器在这里贡献了十几年的越界读写；
- **并发状态机**：多连接 × 多事务 × 异步事件，对象生命周期（连接、数据库、回调）互相引用，UAF 与数据竞争高发；
- **长期演进**：协议版本、厂商扩展、profile 层出不穷，回归测试压力极大，而 C 协议栈的可测试性出了名的差。

前身 Fluoride（C）的历史就是这三条的病历。Gabeldorsche（gd）重写工程先以 C++ 起步，**新增组件逐步转向 Rust**；GATT server 是其中走得最远的一个——整层协议逻辑没有一个 unsafe 块。

## 2. Rust 设计方案：四个机制逐层拆解

### 2.1 解析层：类型化报文让越界"无从写起"

```rust
// gatt/server/transactions/read_request.rs（逻辑全文）
pub async fn handle_read_request<T: AttDatabase>(
    request: att::AttReadRequest,
    mtu: usize,
    db: &T,
) -> Result<att::Att, EncodeError> {
    let handle = request.attribute_handle.into();
    match db.read_attribute(handle).await {
        Ok(mut data) => {
            // as per 5.3 3F 3.4.4.4 ATT_READ_RSP, we truncate to MTU - 1
            data.truncate(mtu - 1);
            att::AttReadResponse { value: data }.try_into()
        }
        Err(error_code) => att::AttErrorResponse {
            opcode_in_error: att::AttOpcode::ReadRequest,
            handle_in_error: handle.into(),
            error_code,
        }.try_into(),
    }
}
```

**机制解读**：报文由 PDL（packet definition language）从协议定义生成——`AttReadRequest` 是结构体，字段有类型，解析期不存在手写指针运算。**漏洞不是在运行时被拦住的，而是在代码里根本写不出来**。最典型的一行是 `data.truncate(mtu - 1)`：C 里"按对端通告的 MTU 截断响应"是经典越界写（对端不可信！），`Vec::truncate` 在语义上不可能越界——它只缩长不扩容。错误路径同样类型化：`AttErrorResponse` 按规范三要素构造，编码失败是 `EncodeError`。

### 2.2 生命周期：弱引用切断循环，注释承认妥协

```rust
// gatt/server.rs
pub struct GattModule {
    connections: HashMap<TransportIndex, GattConnection>,
    databases: HashMap<ServerId, SharedBox<GattDatabase>>,
    // NOTE: this is logically owned by the GattModule. We share it behind a Mutex
    // just so we can use it as part of the Arbiter. Once the Arbiter is removed,
    // this should be owned fully by the GattModule.
    isolation_manager: Arc<Mutex<IsolationManager>>,
}

struct GattConnection {
    bearer: SharedBox<AttServerBearer<AttDatabaseImpl>>,
    database: WeakBox<GattDatabase>,   // 连接对数据库持弱引用
}
```

**机制解读**：协议栈的对象图是网状的：模块拥有连接与数据库，连接引用数据库。C++ 里这是 UAF 的标准配方——数据库销毁后连接的回调打到悬垂指针。这里 `GattConnection` 对数据库持 `WeakBox`（弱引用）：数据库销毁后，升级操作返回 `None` 而非解引用野指针，**"对象还在不在"从运行期赌博变成类型化的 Option**。那条 NOTE 注释同样有信息量：作者明确标注了 `Arc<Mutex>` 是暂时妥协（Arbiter 移除后应回归独占所有权）——**所有权文化让技术债显式化，而不是埋成定时炸弹**。

### 2.3 并发模型：单线程 async + `?Send` 的精确表达

```rust
#[async_trait(?Send)]
pub trait AttDatabase {
    async fn read_attribute(&self, handle: AttHandle) -> Result<Vec<u8>, AttErrorCode>;
    async fn write_attribute(&self, handle: AttHandle, data: &[u8]) -> Result<(), AttErrorCode>;
    fn snapshot(&self) -> SnapshottedAttDatabase<'_> { ... }
}
```

**机制解读**：`?Send` 是一个常被忽略但信息量极大的标注：它声明这些 future **不需要**跨线程——整个 GATT 协议处理跑在单线程事件循环上，用 async/await 表达并发，用单线程消解数据竞争。**"并发安全"不是靠锁出来的，是靠架构选择让竞争条件不存在**。这与官方 DoH3 案例（"单线程内安全调度多任务，线程数更少"）同源：省下的不只是锁，还有线程本身的内存与调度开销。需要多线程的场合（如 libbinder_rs 的服务 trait）则反向使用——`Send + Sync` 强制。Rust 的并发竞争力恰在这种**双向精确**：要跨线程就编译期证明安全，不跨就把这个事实写进类型。

### 2.4 可测试性：泛型注入 + 全分支单测

`handle_read_request` 对泛型 `T: AttDatabase` 工作，于是同文件用内存 fake（`TestAttDatabase`）覆盖全部四个分支：simple / truncated / missed-handle / not-permitted。C 协议栈的测试通常需要起整套链路（控制器仿真、socketpair），反馈以分钟计；这里是毫秒级单测。**协议栈恰恰是最需要回归测试的代码，而可测试性是被泛型 + trait 设计出来的，不是补出来的。**

## 3. 竞争力分析

**这个案例证明了什么**："高危协议栈必须付出安全税"的旧等式不成立。GATT 的 10,497 行证明：类型化报文（解析安全）、弱引用（生命周期安全）、单线程 async（并发安全）、泛型注入（可测试性）四者叠加，可以让一个处理不可信输入的并发协议栈**全程不写一个 unsafe**——安全不是审计出来的，是代码结构的自然属性。

**与分发放大的化学反应**：蓝牙是 APEX 模块（`apex_available: ["com.android.bt"]`），Rust 组件随 Google Play 周级下发。**内存安全的协议栈 + 快速分发 = 攻击面收缩速度本身被改变**——漏洞少了，剩下漏洞的修复到达设备也快了一个数量级。

**渐进共存的可行性**：`libbluetooth_core_rs_bridge` + codegen 显示 Rust 组件经 cxx 桥嵌入 C++ gd 栈，同一个 APEX 里 C/C++/Rust 混布。替换不需要停机重写 74 万行——新写的先安全起来，旧的随生命周期自然退役。

**诚实的代价**：零 unsafe 仅限于 `system/rust`；全仓库 118 个 unsafe 块集中在 `gd/rust/linux`（内核 socket）与 `topshim`（JNI）——贴 OS/JNI 边界处仍需专家审计。单线程模型把吞吐上限压在单核，对 GATT 这种控制面协议足够，数据面（L2CAP 大吞吐）另当别论。

## 4. 结论

蓝牙 GATT 回答了一个被问了多年的问题：**"真实世界的复杂协议栈，能不能全程安全 Rust？"** 答案是 10,497 行、零 unsafe、带全分支测试的实证。更重要的是它展示了 Rust 竞争力的完整形态：语言内（类型 + 所有权 + async）解决安全，语言外（cxx + APEX）解决落地——前者让代码写对，后者让写对的代码到达设备。
