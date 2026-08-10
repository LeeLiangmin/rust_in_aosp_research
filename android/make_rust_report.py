#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate RUST.md: classify Rust-related AOSP repos as internal / shared-external / third-party,
and describe the Android-system position & role of internal components."""
import os
import json
import sqlite3
from collections import Counter

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "aosp_tree.db")
OUT = os.path.join(BASE_DIR, "RUST.md")

STRONG = {"rs_file", "cargo", "rustfmt", "rust_dir"}

# repo -> (bucket, 定位/子系统, 作用)
# bucket: "internal" | "shared" | "third"
CURATED = {
    # ---------------- internal ----------------
    "platform/system/security": ("internal", "系统安全 / keystore",
        "keystore2：Android 12+ 系统密钥管理守护进程（system_server 内 AIDL 服务 android.security.keystore2），"
        "全 Rust，替代旧 C++ keystore，提供密钥生成/存储、attestation、TEE 密钥；同仓含 rkpd_client、ondevice-signing、fsverity 等 Rust 组件。"),
    "platform/packages/modules/Bluetooth": ("internal", "系统蓝牙模块（com.android.bluetooth）",
        "Gabeldorsche 新蓝牙协议栈核心（system/gd + system/rust），Rust 重写，分阶段替换 C++ Fluoride 栈，"
        "负责 HCI/host 协议与 profile 框架。"),
    "platform/packages/modules/DnsResolver": ("internal", "网络解析（com.android.resolv）",
        "DNS 解析器，含 DoH3（DNS-over-HTTP3，doh/ 目录）Rust 实现，服务于 netd 解析路径。"),
    "platform/packages/modules/Virtualization": ("internal", "Android 虚拟化框架 AVF（com.android.virt）",
        "Microdroid（受保护虚拟机最小 OS）与 libvmbase、microdroid_manager 等用 Rust；提供虚拟机与机密计算。"),
    "platform/packages/modules/Uwb": ("internal", "超宽带模块（com.android.uwb）",
        "UWB（FiRa UCI）协议栈，含 Rust 实现部分。"),
    "platform/packages/modules/SdkExtensions": ("internal", "系统 SDK 扩展模块",
        "扩展 SDK 版本判定与支持库，含 Rust 组件。"),
    "platform/system/authgraph": ("internal", "系统安全（Android 15+）",
        "认证图（attestation 认证链/设备认证），Rust 实现。"),
    "platform/system/secretkeeper": ("internal", "系统安全服务（system_server）",
        "ISecretkeeper：受保护的系统级秘密存储（AIDL + TEE），Rust 实现。"),
    "platform/system/keymint": ("internal", "密钥 HAL 参考实现",
        "KeyMint 的 Rust 参考实现，用于 TEE（Trusty/OP-TEE）集成。"),
    "platform/system/bpf": ("internal", "内核 eBPF 支撑",
        "bpfloader：开机加载 eBPF 程序（网络/性能监控），Rust 实现。"),
    "platform/system/memory/mmd": ("internal", "内存管理子系统",
        "memory metrics daemon：采集并上报系统内存指标，Rust 实现。"),
    "platform/system/libfmq": ("internal", "IPC 基础设施（HIDL/AIDL）",
        "FastMessageQueue（共享内存消息队列）的 Rust 绑定。"),
    "platform/system/librustutils": ("internal", "平台基础库",
        "Android Rust 通用工具/宏库，供各平台 Rust 组件复用。"),
    "platform/system/cros-codecs": ("internal", "编解码（Android/ChromeOS 共享）",
        "AV1/VP9 软件解码器 crate，Google 维护，Android 与 ChromeOS 共用。"),
    "platform/system/logging": ("internal", "日志子系统",
        "logd 相关工具与组件的 Rust 部分。"),
    "platform/system/apex": ("internal", "包/更新系统",
        "APEX 打包/工具链中的 Rust 部分。"),
    "platform/system/extras": ("internal", "调试/检查工具",
        "系统调试、检查工具集，含部分 Rust 工具。"),
    "platform/system/secure_element": ("internal", "硬件安全（SE）",
        "Secure Element 服务与工具，含 Rust 部分。"),
    "platform/system/see/authmgr": ("internal", "安全执行环境（SEE）",
        "SEE 认证管理（auth manager）。"),
    "platform/system/core": ("internal", "平台基础库/init",
        "基础运行环境中的部分 Rust 组件（liblog 等 Rust 绑定、少量工具）。"),
    "platform/system/tools/aidl": ("internal", "IPC 工具链",
        "AIDL 编译器的 Rust 后端，生成 AIDL 的 Rust 绑定——Rust 模块间 IPC 的基础。"),
    "platform/system/tools/mkbootimg": ("internal", "构建/打包工具",
        "boot 镜像打包工具 mkbootimg（当前以 Python 为主，正在迁移 Rust）。"),
    "platform/build/soong": ("internal", "构建系统",
        "Soong 的 Rust 支持：rust_binary/rust_library/rust_ffi/rust_proc_macro/rust_test 等模块规则，"
        "负责 AOSP 内所有 Rust 代码的编译（直接调用 rustc，不走 Cargo）。"),
    "toolchain/android_rust": ("internal", "工具链",
        "从源码构建 Android 定制 Rust 工具链（rustc + 标准库 + Android 特有配置），产出 prebuilts/rust。"),
    "device/google/cuttlefish": ("internal", "虚拟设备（Cuttlefish）",
        "云端/本地虚拟 Android 设备，host 工具与 graphics 部分用 Rust。"),
    "kernel/common": ("internal", "内核",
        "Rust-for-Linux 支持（rust/ 目录），使内核支持 Rust 模块。"),
    "trusty/lib": ("internal", "Trusty TEE",
        "Trusty 安全 OS 的 Rust 库。"),
    "trusty/app/keymint": ("internal", "Trusty TEE 应用",
        "Trusty 上的 KeyMint 应用，Rust 实现。"),
    "trusty/app/secretkeeper": ("internal", "Trusty TEE 应用",
        "Trusty 上的 Secret Keeper 应用，Rust 实现。"),
    "trusty/app/authmgr": ("internal", "Trusty TEE 应用",
        "Trusty 上的认证管理应用。"),
    "trusty/app/storage": ("internal", "Trusty TEE 应用",
        "Trusty 安全存储服务（加密、防篡改），Rust 实现。"),
    "trusty/app/sample": ("internal", "Trusty TEE 应用",
        "Trusty 示例应用（Rust 模板/示例）。"),
    "trusty/host/aidl": ("internal", "Trusty TEE host 工具",
        "Trusty host 侧 AIDL 工具（Rust）。"),
    "trusty/host/common": ("internal", "Trusty TEE host 工具",
        "Trusty host 侧公共库。"),
    "trusty/lk/common": ("internal", "Trusty LK 内核",
        "Trusty 内核（LK）相关 Rust 组件。"),
    "trusty/lk/trusty": ("internal", "Trusty LK 内核",
        "Trusty 内核扩展中的 Rust 组件。"),
    "tee/optee/ta/keymint": ("internal", "OP-TEE TEE",
        "KeyMint 的 OP-TEE TA 参考实现，Rust 编写。"),
    "platform/tools/netsim": ("internal", "开发/测试工具",
        "网络仿真工具（多设备网络模拟），Rust 实现。"),
    "platform/tools/rootcanal": ("internal", "蓝牙测试/仿真",
        "rootcanal：HCI 级蓝牙仿真框架（Rust），用于蓝牙互操作/自动化测试。注：gitiles 访问受限（需登录）。"),
    "platform/system/libueventd-rs": ("internal", "平台基础库",
        "libueventd-rs：init/ueventd 的 Rust 库。注：gitiles 访问受限（需登录）。"),
    "platform/packages/modules/RemoteKeyProvisioning": ("internal", "系统安全 / 远程密钥预置",
        "rkpd：Remote Key Provisioning 守护进程（Rust），负责设备 attestation 密钥的远程预置与轮换。"),
    "platform/tools/security": ("internal", "签名/安全工具",
        "系统签名等安全工具，部分 Rust。"),
    "platform/frameworks/native": ("internal", "图形/渲染框架",
        "原生图形/渲染库中的 Rust 部分。"),
    "platform/frameworks/minikin": ("internal", "文本排版",
        "文本排版引擎 minikin 的 Rust 化部分。"),
    "platform/development": ("internal", "平台工程工具",
        "平台工程工具与示例，含 Rust 示例代码。"),

    # ---------------- shared external (Google 维护，external/ 下) ----------------
    "platform/external/crosvm": ("shared", "虚拟化（ChromeOS/Android 共享）",
        "Google 的 Rust 虚拟机监视器（VMM），供 AVF/Microdroid 使用。"),
    "platform/external/n2": ("shared", "构建工具（Android 构建用）",
        "Google 开发的 ninja 替代实现（Rust），用于加速 Android 构建。"),
    "platform/external/minijail": ("shared", "沙箱库",
        "Google 的进程沙箱库（Linux seccomp），部分 Rust。"),
    "platform/external/avb": ("shared", "启动安全",
        "Android Verified Boot 2.0（AVB），Google 维护，含 Rust 实现/绑定。"),
    "platform/external/rust/pica": ("shared", "UWB 测试",
        "Google 的虚拟 UWB Controller（FiRa UCI 规范），Rust，用于 UWB 测试。"),
    "platform/external/rust/rutabaga_gfx": ("shared", "虚拟图形",
        "ChromiumOS/Android 的 virtio-gpu 后端（Rust），供虚拟化使用。"),
    "platform/external/rust/cxx": ("shared", "Rust/C++ 互操作",
        "CXX 安全 FFI 框架（Rust↔C++），AOSP Rust/C++ 互操作的关键依赖。"),
    "platform/external/rust/autocxx": ("shared", "Rust/C++ 互操作",
        "autocxx：自动生成 C++ 的 Rust 绑定（Google 项目）。"),
    "platform/external/rust/crabbyavif": ("shared", "编解码",
        "Google 的 AVIF 解析/解码器（Rust）。"),
    "platform/external/rust/cros-libva": ("shared", "图形/硬件加速",
        "libva 的 Rust 封装（ChromeOS）。"),
    "platform/external/libchromeos-rs": ("shared", "ChromeOS 公共库",
        "ChromeOS 通用 Rust crate 集（Google 维护）。"),
    "platform/external/python/bumble": ("shared", "蓝牙测试",
        "Google 的 Python Bluetooth 库 Bumble（含 Rust 部分），用于蓝牙互操作测试。"),
    "platform/external/vboot_reference": ("shared", "启动安全（ChromeOS）",
        "ChromeOS 已验证启动参考实现，含 Rust 部分。"),
    "platform/external/toolchain-utils": ("shared", "工具链工具（ChromeOS）",
        "ChromeOS 工具链团队的工具集，含 Rust 部分。"),
    "platform/external/uwb": ("shared", "UWB 实验/测试",
        "Google 的 UWB 实验库（Rust），非产品模块。"),
    "platform/external/gsc-utils": ("shared", "安全芯片工具",
        "Google Titan 安全芯片相关工具，含 Rust 部分。"),
    "platform/external/flatbuffers": ("shared", "序列化库",
        "FlatBuffers（Google 开源序列化库），含 Rust 实现。"),
    "platform/external/skia": ("shared", "图形库",
        "Skia 图形库（Google），含 Rust 部分（cargo 信号）。"),
    "platform/external/bazelbuild-rules_rust": ("shared", "构建规则",
        "Bazel 的 Rust 构建规则（开源），供 AOSP 迁移 Bazel 使用。"),
    "platform/external/rust/beto-rust": ("shared", "Google 安全",
        "Google 安全相关 Rust 项目。"),
    "platform/external/rust/ninja-to-soong": ("shared", "构建工具",
        "ninja 到 soong 的构建工具（Android 构建用，Rust）。"),

    # ---------------- third party ----------------
    "toolchain/rustc": ("third", "工具链（上游）",
        "Rust 编译器/标准库源码（上游 rust-lang，AOSP 维护构建）。"),
    "toolchain/cargo-deny": ("third", "工具链依赖审计",
        "cargo-deny：第三方 Rust 依赖检查工具。"),
    "toolchain/cargo-vet": ("third", "工具链依赖审计",
        "cargo-vet：第三方 Rust 依赖供应链验证工具。"),
    "toolchain/sccache": ("third", "编译缓存",
        "sccache：共享编译缓存工具（Mozilla 项目）。"),
}

def gs_link(repo):
    return f"[`{repo}`](https://android.googlesource.com/{repo}/)"


def crate_links(repo):
    name = repo.rsplit("/", 1)[1]
    return (f"[AOSP](https://android.googlesource.com/{repo}/) · "
            f"[crates.io](https://crates.io/crates/{name})")


VERDICT_CN = {"pure": "纯 Rust", "rust_main": "Rust 为主",
              "hybrid": "混合（Rust+其它）", "non_rust": "非 Rust 主体"}

_LANG = None


def lang_cell(repo):
    """Return '语言构成' cell from lang_stats: verdict + counts."""
    global _LANG
    if _LANG is None:
        conn = sqlite3.connect(DB_PATH)
        _LANG = {}
        for r, cj, v in conn.execute("SELECT repo, counts, verdict FROM lang_stats"):
            _LANG[r] = (v, json.loads(cj))
        conn.close()
    if repo not in _LANG:
        return "（未分析/无源码）"
    v, counts = _LANG[repo]
    rs = counts.get("rs", 0)
    cc = counts.get("c", 0) + counts.get("cc", 0) + counts.get("asm", 0)
    jg = counts.get("java", 0) + counts.get("kotlin", 0) + counts.get("go", 0)
    h = counts.get("h", 0)
    parts = [f".rs {rs}"]
    if cc:
        parts.append(f"C/C++ {cc}")
    if jg:
        parts.append(f"Java/Kotlin/Go {jg}")
    if h:
        parts.append(f"头文件 {h}")
    return f"{VERDICT_CN.get(v, v)}（{', '.join(parts)}）"


def classify(repo):
    if repo in CURATED:
        return CURATED[repo]
    if repo.startswith("platform/external/rust/crates/"):
        return ("third", "第三方 crate（vendor）", "crates.io 上游 crate，AOSP 版本化 vendor（源码经 android-crates-io 镜像同步）。")
    if repo.startswith("platform/external/rust/"):
        return ("shared", "共享外部（Google Rust 项目）", "Google 维护、托管于 external/rust/ 的 Rust 开源项目。")
    if repo.startswith("platform/external/"):
        return ("third", "第三方/外部组件", "第三方或上游组件（非 Android 自有模块）。")
    if repo.startswith("platform/prebuilts/rust"):
        return ("third", "工具链预编译", "上游 Rust 工具链预编译产物（各 host 平台）。")
    if repo.startswith("toolchain/") or repo.startswith("external/"):
        return ("third", "第三方/外部", "第三方或上游组件。")
    if repo.startswith(("kernel/", "trusty/", "tee/")):
        return ("internal", "Android 系统组件", "Android 系统内 Rust 组件，见 README。")
    return ("internal", "Android 系统组件", "见 README。")


def main():
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute("SELECT repo, status, rust_signal, readme, desc_root FROM repos").fetchall()
    conn.close()

    strong = {}
    for repo, status, sig, readme, desc in rows:
        if sig and (set(sig.split(",")) & STRONG):
            strong[repo] = (status, sig, readme or desc or "")

    # ensure internal components with only weak/no signal are included
    for repo in CURATED:
        strong.setdefault(repo, ("ok", "", ""))

    L = []
    add = L.append
    add("# AOSP Rust 相关仓库分类")
    add("")
    add("来源：android.googlesource.com（官方仓库清单 + 顶层结构 + README，本目录爬取归档于 aosp_tree.db）。")
    add("分类口径：**内部库**＝Google 为 Android 系统开发的 Rust 模块；**共享外部**＝Google 维护、托管于 external/、供 Android 及其它项目共用的开源组件；**第三方**＝上游 crate/工具，AOSP 仅 vendor。")
    add("链接：表中 repo 名均链接到 android.googlesource.com 仓库；第三方 crate 行另附 crates.io 链接。")
    add("语言构成：对每仓库源码快照统计文件扩展名得出——纯 Rust（仅 .rs）；Rust 为主（≥90%）；混合（含较多 C/C++/Java/Kotlin/Go）；非 Rust 主体（如 soong 为 Go）。")
    add("")

    buckets = {"internal": [], "shared": [], "third": []}
    for repo in strong:
        bucket, loc, role = classify(repo)
        buckets[bucket].append((repo, loc, role, strong[repo]))

    add("## 总览")
    add("")
    add(f"- 含 Rust 信号的仓库：{len(strong)}（其中 external/rust/crates 第三方 crate 有源码的 {sum(1 for r in strong if 'platform/external/rust/crates/' in r)} 个）")
    add(f"- 内部库（Android 系统自有）：**{len(buckets['internal'])}**")
    add(f"- 共享外部（Google 维护开源）：**{len(buckets['shared'])}**")
    add(f"- 第三方（上游 vendor）：**{len(buckets['third'])}**")
    add("")
    from collections import Counter as _C
    vc = _C()
    for repo, *_ in buckets["internal"] + buckets["shared"]:
        cell = lang_cell(repo)
        if cell.startswith("（未分析"):
            vc["空仓库/受限（无源码）"] += 1
        else:
            vc[cell.split("（")[0]] += 1
    add("**语言构成（内部+共享仓库，按源码文件统计）**：" + "；".join(f"{k} {n} 个" for k, n in vc.most_common()))
    add("")

    # ---- internal ----
    add("## 一、Android 内部 Rust 组件（系统定位与作用）")
    add("")
    add("> repo 名称为链接，指向 android.googlesource.com 对应仓库。")
    add("")
    add("| repo | 系统定位/子系统 | 作用 | 语言构成 |")
    add("|---|---|---|---|")
    for repo, loc, role, (status, sig, desc) in sorted(buckets["internal"]):
        add(f"| {gs_link(repo)} | {loc} | {role} | {lang_cell(repo)} |")
    add("")

    # ---- shared ----
    add("## 二、共享外部 Rust 组件（Google 维护，托管于 external/）")
    add("")
    add("| repo | 定位 | 作用 | 语言构成 |")
    add("|---|---|---|---|")
    for repo, loc, role, (status, sig, desc) in sorted(buckets["shared"]):
        add(f"| {gs_link(repo)} | {loc} | {role} | {lang_cell(repo)} |")
    add("")

    # ---- third ----
    add("## 三、第三方/上游 Rust（vendor）")
    add("")
    add("### 3.1 工具链与预编译")
    add("")
    add("| repo | 说明 | 语言构成 |")
    add("|---|---|---|")
    for repo, loc, role, (status, sig, desc) in sorted(buckets["third"]):
        if repo.startswith("toolchain/") or repo.startswith("platform/prebuilts/rust"):
            add(f"| {gs_link(repo)} | {role} | {lang_cell(repo)} |")
    for repo in ["platform/prebuilts/rust",
                 "platform/prebuilts/rust-toolchain/darwin",
                 "platform/prebuilts/rust-toolchain/linux-x86",
                 "platform/prebuilts/rust-toolchain/linux-arm64",
                 "platform/prebuilts/rust-toolchain/linux-musl-x86",
                 "platform/prebuilts/rust-toolchain/windows-x86"]:
        add(f"| {gs_link(repo)} | 上游 Rust 工具链预编译产物（各 host 平台）。 | 预编译二进制 |")
    add("")
    add("### 3.2 其他第三方外部库（platform/external 下的非 crate 上游组件）")
    add("")
    for repo, loc, role, (status, sig, desc) in sorted(buckets["third"]):
        if repo.startswith("platform/external/") and "rust/" not in repo:
            add(f"- {gs_link(repo)} — {desc[:70] or role or '-'}")
    add("")
    add("### 3.3 第三方 Rust crate（external/rust/crates）")
    add("")
    crates = sorted((r for r in strong if "platform/external/rust/crates/" in r))
    add(f"- 仓库总数：{sum(1 for r, *_ in rows if 'platform/external/rust/crates/' in r)} 个"
        f"（含源码 {sum(1 for r, s, *_ in rows if 'platform/external/rust/crates/' in r and s == 'ok')} 个；"
        f"其余为占位仓库，源码经 `external/rust/android-crates-io` 镜像在构建期同步）")
    add(f"- 下表列出含 Rust 信号（Cargo.toml/.rs/rustfmt 等）的 {len(crates)} 个：")
    add("")
    add("| crate | 信号 | 说明 | 链接 |")
    add("|---|---|---|---|")
    for repo in crates:
        status, sig, desc = strong[repo]
        name = repo.rsplit("/", 1)[1]
        note = (desc or "-").replace("|", "/")[:70]
        add(f"| `{name}` | {sig or '-'} | {note} | {crate_links(repo)} |")
    add("")

    open(OUT, "w", encoding="utf-8").write("\n".join(L))
    print(f"wrote {OUT} ({len(L)} lines)")


if __name__ == "__main__":
    main()
