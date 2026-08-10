# 案例报告 05：libprefetch —— 没有安全压力时，工程师为什么还选 Rust

> 代码来源：`G:\aosp-scan\platform_system_core\init\libprefetch`（AOSP main，2026-08）
> 规模：约 4,335 行；所在 `system/core` 全部 Rust 代码仅 24 个 unsafe 块、1 个 unsafe fn
> 架构位置：③ Native 层最底部（init 子系统，内核启动后的第一个用户态进程群）

## 1. 问题定义：这个位置为什么难

libprefetch 是开机启动路径的 I/O 预取工具：record 模式通过内核 tracepoint（`filemap/mm_filemap_add_to_page_cache`）观测启动期间的页缓存装入，replay 模式在下次开机时提前 `readahead`/`posix_fadvise`，把磁盘 I/O 移出关键路径。它的难度画像与前四个案例完全不同：

- **不解析网络输入、不持特权资产**——安全不是主要压力；
- **性能极敏感**：开机时间以毫秒计，工具自身开销必须可忽略；
- **工程复杂度不低**：tracepoint 订阅、mountinfo 解析、多线程回放、记录格式序列化——这是个正经的数据管线程序。

前身是散落在 init 与启动脚本链路中的 C++ readahead 逻辑。**正因为没有安全压力，选择 Rust 就是一次纯粹的效率投票**——这正是它对"Rust 竞争力"论证的独特价值。

## 2. Rust 设计方案：四个机制逐层拆解

### 2.1 RAII 的广谱应用：不只是内存

```rust
// replay.rs —— 作用域日志：任何路径离开（含 ? 提前返回）自动打 "end"
fn scoped_log<T: Display>(ctx: usize, msg: T) -> ScopedLog<T> { ... }
impl<T: Display> Drop for ScopedLog<T> {
    fn drop(&mut self) { debug!("{} {} end", self.thd_id, self.msg); }
}

fn readahead(id: usize, file: Arc<File>, ...) -> Result<(), Error> {
    let _dbg = scoped_log(id, "readahead");
    ...
}
```

**机制解读**：多线程 readahead 的调试日志要求 start/end 严格配对。C 里"每个 return 前补一行日志"在错误路径上几乎必然漏配；`Drop` 让配对成为对象生命周期的副产品。同一个 RAII 机制还管着 `Arc<File>` 的句柄释放——多线程共享文件不存在"一个线程关了另一个还在读"的窗口。**一种语言机制，同时覆盖内存、句柄、日志、锁四类资源的配对问题**——这是 RAII 相对"各自为战的手动管理"的结构性优势。

### 2.2 错误处理：显式转换消灭静默截断

```rust
// replay.rs —— 文件偏移的位宽转换必须显式，失败即类型化错误
let mut current_offset: off64_t = record.offset
    .try_into()
    .map_err(|_| Error::Read { error: "Failed to convert offset".to_string() })?;
```

**机制解读**：记录文件里的偏移是 u64， syscall 要 `off64_t`——C 的隐式转换在位数不匹配时静默截断，预取就会读错位置（不是安全问题，是纯正确性问题，但一样难查）。Rust 无隐式截断，`try_into` 把转换失败变成 `Result` 的一支。配合 `main.rs` 里 `match &args.nested` 的枚举子命令分发与统一错误出口，**整个程序没有一条"静默继续"的错误路径**。

### 2.3 生态杠杆：系统工具直接消费 crates.io

`tracer/mem.rs` 的 import 列表本身就是论据：

```rust
use serde::Deserialize; use serde::Serialize;   // 记录格式序列化
use walkdir::{DirEntry, WalkDir};               // 目录遍历
use regex::Regex;                               // 路径匹配
use nix::...;                                    // POSIX 类型安全封装
use lru_cache::LruCache;                        // 并发缓存
```

**机制解读**：tracepoint 解析、记录文件序列化、文件系统遍历——如果写 C，每一项都意味着数千行手写代码或引入风格各异的 C 库；Rust 侧是五行 `use`。`EXCLUDED_FILESYSTEM_TYPES`（binder/bpf/cgroup/fuse/tmpfs…）这类领域配置用静态表驱动，配合 `#[cfg(target_os)]` 的 `MajorMinorType` 处理 Android/Linux 的 `dev_t` 位宽差异——**可移植性被 cfg 系统管理，而非 #ifdef 迷宫**。

### 2.4 unsafe 的最低剂量：syscall 边界一处

整个模块唯一的 unsafe 是直接 `pread64` 系统调用，且 SAFETY 注释列出的三条不变量中有两条（buffer 有效、长度不越界）其实已由 `&mut [u8; READ_SZ]` 类型保证——unsafe 只是跨越 syscall ABI 的形式步骤。**当 unsafe 少到这种程度，"人工审计每一处"就从口号变成现实可行的流程。**

## 3. 竞争力分析

**这个案例证明了什么**：Rust 的竞争力在安全叙事之外依然成立。把安全收益全部拿掉，剩下的组合——RAII 的资源配对、`Result` 的错误完备性、crates.io 生态、零 GC 的可预测性能——仍然赢过 C（手写一切）与 C++（更高的认知与维护成本）。这解释了官方 2025 年数据里"评审耗时 -25%、返工 -20%、回滚率 4x"的来源：**编译器拦截的不只是漏洞，还有大量普通 bug**。

**对照其他候选**：Go 在这个场景其实可用（性能要求没到极限），但 init 链路对二进制体积、启动依赖敏感，Go 运行时是减分项；Python/脚本无法满足性能；C++ 能写但维护成本高。**当"写对、写快、写省心"三个目标要同时达成，Rust 在系统工具档没有对手。**

**诚实的代价**： crates.io 依赖引入供应链审计需求（AOSP 用 android-crates-io 统一 vendored 解决）；编译速度比 C 慢；对习惯 C 的 init 维护者有学习曲线。这些都是真实成本，只是被收益覆盖。

## 4. 结论

前四个案例回答"Rust 如何让 Android 更安全"，libprefetch 回答的是同样重要的另一问："**当安全不是理由时，Rust 还剩什么？**" 答案是：RAII、`Result`、生态、零成本抽象组成的日常工程效率——安全在这里甚至是副产品。一门语言只有在"非安全场景也被自发选用"时，才算真正完成了从"专项工具"到"平台默认语言"的跃迁。libprefetch 是这个跃迁的证据。
