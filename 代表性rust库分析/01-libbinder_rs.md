# 案例报告 01：libbinder_rs —— 把 C ABI 的"君子协定"变成编译期法律

> 代码来源：`G:\aosp-scan\platform_frameworks_native\libs\binder\rust`（AOSP main，2026-08）
> 规模：30 个 .rs 文件 / 11,078 行；unsafe 块 308 处、unsafe fn/impl 47 处，几乎全部贴着 FFI 边界
> 架构位置：③ Native 层最底部（IPC 底座），触点伸进 ④ HAL 与 ⑥ TEE

## 1. 问题定义：这个位置为什么难

Binder 是 Android 全部跨进程通信的底座。它的 C/C++ 实现建立在一整套**靠文档和纪律维持的约定**之上：

- **引用计数约定**：`AIBinder_incStrong`/`AIBinder_decStrong` 必须严格配对，漏一次泄露、多一次 UAF；
- **所有权转移约定**：某些 NDK 函数"返回一个新持有的引用"，某些"只是借用"，区别只在文档里；
- **借用约束**：Parcel 的某些视图只在原对象存活期间有效，编译器不管；
- **线程安全约定**：服务实现会被 binder 线程池并发回调，"必须线程安全"写在文档里；
- **返回值约定**：每个调用返回 `status_t`，忘了检查就静默吞掉错误（历史提权漏洞 Rage Against the Cage 的根因）。

C++ 有 `sp<>`/`wp<>` 智能指针缓解其中一部分，但裸指针与智能指针可以自由混用、互转无门槛——防线是建议性的。这就是 libbinder_rs 要解决的问题：**不改动底座语义，把这套约定全部升级为编译器强制**。

## 2. Rust 设计方案：五个机制逐层拆解

### 2.1 所有权的进入与移交：`from_raw` / `Drop` / `into_raw` 的三明治

```rust
// proxy.rs —— 进入：裸指针只在入口出现一次
/// ... this method conceptually takes ownership of a strong reference ...
/// we keep a strong reference, and only decrement on drop.
pub(crate) unsafe fn from_raw(ptr: *mut sys::AIBinder) -> Option<Self> {
    ptr::NonNull::new(ptr).map(Self)
}

// native.rs —— 持有期间：析构即 decStrong，编译器保证恰好一次
impl<T: Remotable> Drop for Binder<T> {
    fn drop(&mut self) {
        unsafe { sys::AIBinder_decStrong(self.ibinder); }
    }
}

// parcel.rs —— 移交：消费 self，用 ManuallyDrop 显式抑制析构
pub(crate) fn into_raw(self) -> *mut sys::AParcel {
    let ptr = self.ptr.as_ptr();
    let _ = ManuallyDrop::new(self);   // 所有权转交 C 侧，Rust 不再负责释放
    ptr
}
```

**机制解读**：这是一套完整的所有权状态机——`from_raw`（取得）、`Drop`（自动释放）、`into_raw`（显式移交）。"所有权此刻在 Rust 侧还是 C 侧"在 C 里是脑子里的状态，在这里是类型里的状态：`into_raw` 消费 `self` 后，原变量直接不可用（编译错误），想"移交后再用一次"都写不出来。

**C++ 对照**：`sp<>` 也有析构计数，但 `sp.get()` 拿到裸指针后随处可用，移交语义靠 `release()` 之类的约定——而约定可以被违反。Rust 里 `as_raw()` 是 `unsafe` 且文档明写"仅测试用"，安全侧拿不到口子。

### 2.2 借用检查器管辖 C 资源：`BorrowedParcel<'a>`

```rust
// parcel.rs
pub fn borrowed(&mut self) -> BorrowedParcel<'_> {
    // Safety: ... the borrow checker will ensure that the `AParcel` can only be
    // accessed via the `BorrowedParcel` until it goes out of scope.
    BorrowedParcel { ptr: self.ptr, _lifetime: PhantomData }
}

pub unsafe fn from_raw(ptr: *mut sys::AParcel) -> Option<BorrowedParcel<'a>> {
    // "the lifetime ... can be chosen arbitrarily by the caller. The caller must
    // ensure it is valid to mutably borrow ... must have exclusive access"
    ...
}
```

**机制解读**：`PhantomData` + 生命周期参数把 C 对象的借用关系接进了借用检查器——`BorrowedParcel` 活着期间，原 `Parcel` 不能被移动或另行可变访问（`&mut self` 独占）。注释里明确说"the borrow checker will ensure..."——**编译器被招募来执行 C API 的访问协议**。unsafe 入口 `from_raw` 把举证责任（独占性、有效期）显式压给调用者，这正是 unsafe 的本义：机器验证不了的部分，用人可审计的契约标记出来。

**C++ 对照**：C++ 的 `Parcel` 引用就是个指针，原对象析构后引用即悬垂，编译器全程沉默。

### 2.3 线程安全编译化：`Send`/`Sync` trait bound

```rust
// binder.rs
pub trait Interface: Send + Sync + DowncastSync { ... }

// binder_async.rs —— 跨线程调度的每个值都带 Send 约束
pub type BoxFuture<'a, T> = Pin<Box<dyn Future<Output = T> + Send + 'a>>;
```

**机制解读**：Binder 服务被驱动线程池并发回调。`Send + Sync` 写进 trait bound 意味着：服务实现若含非线程安全字段（`Rc`、裸指针、`Cell`），**编译失败，进不了 review**。异步侧所有 future 携带 `Send`，跨线程调度的合法性同样是编译期性质。数据竞争——C/C++ 里最难查、最难复现、最常被利用的 bug 类别——在这里是编译错误。

### 2.4 错误的强制性：`Result` 收口与敏感数据标记

```rust
// error.rs —— C 错误码到类型的唯一收口
pub fn status_result(status: status_t) -> Result<()> {
    match parse_status_code(status) { StatusCode::OK => Ok(()), e => Err(e) }
}

// parcel.rs —— 敏感数据（如密码）标记后，删除/重分配前会被清零
pub fn mark_sensitive(&mut self) {
    unsafe { sys::AParcel_markSensitive(self.as_native()) }
}
```

**机制解读**：所有 FFI 调用经 `status_result` 收口后，调用方要么 `?` 传播、要么显式 `unwrap`——"忘了检查"不可表达。`mark_sensitive` 则展示了安全语义的透传：底层 C 的"敏感数据擦除"能力被包装成安全方法，Rust 侧的密钥类服务（如 keystore2）可以一行调用获得该保证。

### 2.5 RAII 不止管内存：`LazyServiceGuard`

```rust
// service.rs —— 保活状态的配对由对象生命周期承载
#[must_use]
pub struct LazyServiceGuard { _private: () }
static GUARD_COUNT: Mutex<u64> = Mutex::new(0);
// new() 时计数 0→1 调 force_lazy_services_persist(true)；
// Drop 时计数归零调 false。注释专门解释了为何必须持锁而不能用 AtomicU64（1->0->1 时序）。
```

**机制解读**：RAII 在这里管理的不是内存而是**进程级运行时状态**。C 里 `forceLazyServicesPersist(true/false)` 的配对覆盖所有退出路径（含异常、提前 return）几乎不可能靠纪律做到；guard 对象离开作用域即自动复位，编译器顺便用 `#[must_use]` 拦截"创建了却没用"。

## 3. 竞争力分析

**这个案例证明了什么**：FFI 不是 Rust 的阿喀琉斯之踵，而可以是它最强的表演场。libbinder_rs 展示了一套可复用的方法论——C ABI 的每一条约定（计数、所有权、借用、线程、错误）都有对应的 Rust 机制承接（`Drop`/`ManuallyDrop`、`PhantomData` 生命周期、`Send`/`Sync`、`Result`）。unsafe 没有消失，但被压缩成**入口处的显式举证责任**，且每块都带 SAFETY 论证。

**杠杆价值**：Binder 是"新语言接入 Android"的必经关口。这次绑定投入一次完成，之后所有 Rust 组件（keystore2、AVF、DNS……）写个 `.aidl` 文件即自动获得全套安全保证——Android.bp 里 `libbinder_rs` 与 `libbinder_rs_on_trusty_mock` 双变体意味着**同一份安全语义直通 TEE**。地基的安全性以乘数放大到每个上层组件。

**对比替代路线**：给 C++ libbinder 加 sanitizer/CFI 只能提高利用难度；换 Go 写服务则 GC 与运行时进不了 HAL/TEE。只有 Rust 能"底座不动、语义对齐、安全升级"三合一。

**诚实的代价**：308 个 unsafe 块是全库采样的最高值——绑定层天然贴 FFI，审计不能省；`sys` 层 bindgen 生成代码与手写安全层之间的不变量依赖 NDK C API 的稳定性。Rust 把审计面从 11,078 行压缩到几百处边界点，但边界点本身仍需专家 review。

## 4. 结论

libbinder_rs 的竞争力论证是：**Rust 能把一个有着 15 年历史、约定全靠文档的 C ABI，改造成编译器强制执行的类型契约，且不改动底座一行代码**。它既是受益者（拿到 NDK 稳定 ABI），更是使能者（全体 Rust 服务的地基）。Android 的 Rust 故事能不能讲下去，第一块多米诺就是它。
