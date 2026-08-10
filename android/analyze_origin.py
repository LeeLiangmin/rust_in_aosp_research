#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Classify AOSP repos: external (third-party) vs AOSP-native modules.

Reads aosp_tree.db, writes origin.csv + ORIGIN.md.
"""
import csv
import json
import os
import re
import sqlite3
from collections import Counter, defaultdict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "aosp_tree.db")
CSV_PATH = os.path.join(BASE_DIR, "origin.csv")
MD_PATH = os.path.join(BASE_DIR, "ORIGIN.md")

# Google 自研但按惯例放在 external/ 下的项目（上游仍在 Google）
GOOGLE_ORIGIN_IN_EXTERNAL = {
    "platform/external/avb",
    "platform/external/crosvm",
    "platform/external/flatbuffers",
    "platform/external/gsc-utils",
    "platform/external/libchromeos-rs",
    "platform/external/minijail",
    "platform/external/perfetto",
    "platform/external/pigweed",
    "platform/external/webrtc",
}

META_REPOS = re.compile(
    r"^(mirror/|.*superproject.*|.*-Projects(/|$)|cts_drno_filter|"
    r"pdk_review_filter|third-party-review)$|(^|/)manifest$"
)


def classify(repo):
    """Return (category, sub)."""
    parts = repo.split("/")
    if META_REPOS.search(repo) or parts[0] in ("accessories",):
        return "meta", ""
    if "prebuilts" in parts:
        return "prebuilt", parts[0]
    if parts[0] in ("kernel", "kkernel") or parts[0] == "Kernel-Projects":
        return "kernel", "/".join(parts[:2]) if len(parts) > 1 else parts[0]
    if parts[0] == "toolchain":
        return "toolchain", "/".join(parts[:2]) if len(parts) > 1 else parts[0]
    if "external" in parts:
        sub = "rust_crates" if repo.startswith("platform/external/rust/crates/") else ""
        if repo in GOOGLE_ORIGIN_IN_EXTERNAL:
            sub = "google_origin"
        return "third_party", sub
    if parts[0] in ("device", "product", "tee") or repo.startswith("platform/vendor/"):
        return "vendor_device", "/".join(parts[:2]) if len(parts) > 1 else parts[0]
    return "aosp", "/".join(parts[:2]) if len(parts) > 1 else parts[0]


def desc_of(row):
    return (row["readme"] or row["desc_root"] or "").strip()


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT * FROM repos ORDER BY repo").fetchall()
    conn.close()

    classified = []
    for r in rows:
        cat, sub = classify(r["repo"])
        classified.append((r, cat, sub))

    with open(CSV_PATH, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["repo", "category", "sub", "rust_signal", "description"])
        for r, cat, sub in classified:
            w.writerow([r["repo"], cat, sub, r["rust_signal"] or "", desc_of(r)])

    L = []
    add = L.append
    add("# AOSP 仓库来源分析：外部（third-party）vs AOSP 自研模块")
    add("")
    add(f"- 仓库总数：{len(classified)}")
    add("- 判定规则：路径约定（external/=第三方导入, prebuilts/=预编译, kernel/+toolchain/=外部基础软件, device/=厂商支持），")
    add("  并辅以根目录文件信号校验。")
    add("")
    add("## 1. 总体分类")
    cnt = Counter(cat for _, cat, _ in classified)
    add("| 类别 | 仓库数 | 说明 |")
    add("|---|---|---|")
    notes = {
        "third_party": "第三方/上游开源项目导入 AOSP（platform/external/*, trusty/external/*）",
        "aosp": "AOSP 自研模块（frameworks/system/packages/build/art/bionic…）",
        "prebuilt": "预编译产物仓库（*-prebuilts）",
        "kernel": "Linux 内核及厂商内核模块（上游 kernel.org / SoC 厂商）",
        "toolchain": "编译工具链（llvm/gcc/rust/jdk，上游外部项目）",
        "vendor_device": "设备/厂商适配层（device/*, product/*）",
        "meta": "manifest/superproject/父项目等元仓库",
    }
    for cat, n in cnt.most_common():
        add(f"| {cat} | {n} | {notes.get(cat, '')} |")
    add("")

    # 2. third_party breakdown
    tp = [(r, sub) for r, cat, sub in classified if cat == "third_party"]
    add(f"## 2. 外部第三方仓库（{len(tp)} 个）")
    sub_cnt = Counter(sub or "other" for _, sub in tp)
    add("")
    add("| 子类 | 数量 |")
    add("|---|---|")
    add(f"| Rust crates（platform/external/rust/crates/*，来自 crates.io） | {sub_cnt.get('rust_crates', 0)} |")
    add(f"| Google 上游项目（crosvm/minijail/avb 等，仍由 Google 维护但独立上游） | {sub_cnt.get('google_origin', 0)} |")
    add(f"| 其他第三方项目 | {sub_cnt.get('other', 0)} |")
    add("")
    others = [r for r, sub in tp if sub == ""]
    add(f"### 2.1 其他第三方项目（{len(others)} 个，节选）")
    add("")
    add("| repo | 说明 |")
    add("|---|---|")
    for r in sorted(others, key=lambda x: x["repo"])[:80]:
        add(f"| {r['repo']} | {desc_of(r)[:60].replace('|', '/') or '-'} |")
    if len(others) > 80:
        add(f"| … 其余 {len(others) - 80} 个见 origin.csv | |")
    add("")

    # 3. aosp breakdown
    aosp = [(r, sub) for r, cat, sub in classified if cat == "aosp"]
    add(f"## 3. AOSP 自研模块（{len(aosp)} 个）")
    add("")
    grp = defaultdict(list)
    for r, sub in aosp:
        grp[sub].append(r)
    add("| 子树 | 仓库数 | 代表说明 |")
    add("|---|---|---|")
    for key, items in sorted(grp.items(), key=lambda kv: -len(kv[1])):
        sample = next((i for i in items if desc_of(i)), items[0])
        add(f"| {key} | {len(items)} | {desc_of(sample)[:50].replace('|', '/') or '-'} |")
    add("")

    # 4. vendor_device breakdown
    vd = [(r, sub) for r, cat, sub in classified if cat == "vendor_device"]
    add(f"## 4. 设备/厂商适配（{len(vd)} 个）")
    add("")
    grp = defaultdict(int)
    for r, sub in vd:
        grp[sub] += 1
    for key, n in sorted(grp.items(), key=lambda kv: -kv[1]):
        add(f"- {key}: {n}")
    add("")

    # 5. rust 交叉
    add("## 5. 与 Rust 信号交叉")
    strong = [1 for r, cat, _ in classified
              if cat == "third_party" and r["rust_signal"] and
              set(r["rust_signal"].split(",")) & {"rs_file", "cargo", "rustfmt", "rust_dir"}]
    add(f"- 外部仓库中具 Rust 强信号的：{len(strong)} 个")
    add("")

    open(MD_PATH, "w", encoding="utf-8").write("\n".join(L))
    print(f"wrote {CSV_PATH}, {MD_PATH}")
    for cat, n in cnt.most_common():
        print(f"  {cat}: {n}")


if __name__ == "__main__":
    main()
