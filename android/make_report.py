#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate repos.csv + STRUCTURE.md from aosp_tree.db."""
import csv
import json
import os
import sqlite3
from collections import Counter, defaultdict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "aosp_tree.db")
CSV_PATH = os.path.join(BASE_DIR, "repos.csv")
MD_PATH = os.path.join(BASE_DIR, "STRUCTURE.md")

STRONG_SIGNALS = {"rs_file", "cargo", "rustfmt", "rust_dir"}


def desc_of(row):
    return (row["readme"] or row["desc_root"] or "").strip()


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT * FROM repos ORDER BY repo").fetchall()
    conn.close()

    # ---- CSV ----
    with open(CSV_PATH, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(["repo", "prefix", "status", "rust_signal", "description", "top_level"])
        for r in rows:
            w.writerow([r["repo"], r["prefix"], r["status"], r["rust_signal"],
                        desc_of(r), r["top_level_json"] or ""])

    # ---- STRUCTURE.md ----
    L = []
    add = L.append
    add("# AOSP 仓库结构概览（android.googlesource.com）")
    add("")
    add(f"- 生成时间：{os.path.getmtime(DB_PATH) and '见文件 mtime'}")
    add(f"- 仓库总数：{len(rows)}")
    by_status = Counter(r["status"] for r in rows)
    add("- 状态统计：" + "; ".join(f"{k or 'pending'}={v}" for k, v in by_status.most_common()))
    add("")
    add("## 1. 顶层前缀分组")
    groups = defaultdict(list)
    for r in rows:
        groups[r["prefix"]].append(r)
    add("| 前缀 | 仓库数 | 说明(代表仓库 README) |")
    add("|---|---|---|")
    for prefix, items in sorted(groups.items(), key=lambda kv: -len(kv[1])):
        sample = next((i for i in items if desc_of(i)), items[0])
        note = desc_of(sample)[:60].replace("|", "/") or "-"
        add(f"| {prefix} | {len(items)} | {note} |")
    add("")
    add("## 2. Rust 相关仓库（信号初筛）")
    strong = [r for r in rows if r["rust_signal"] and
              (set(r["rust_signal"].split(",")) & STRONG_SIGNALS)]
    add(f"- 强信号（.rs/Cargo.toml/rustfmt/rust 目录）仓库数：{len(strong)}")
    add("")
    add("| repo | 信号 | 说明 |")
    add("|---|---|---|")
    for r in sorted(strong, key=lambda x: x["repo"]):
        add(f"| {r['repo']} | {r['rust_signal']} | {desc_of(r)[:50].replace('|','/') or '-'} |")
    add("")
    bp = [r for r in rows if r["rust_signal"] and "androidbp" in r["rust_signal"] and
          not (set(r["rust_signal"].split(",")) & STRONG_SIGNALS)]
    add(f"- 仅有 Android.bp（无法单独判断语言）仓库数：{len(bp)}")
    add("")
    add("## 3. 各前缀下的重点仓库")
    for prefix in ["platform", "kernel", "device", "toolchain", "trusty", "packages", "external", "prebuilts", "frameworks", "system", "hardware"]:
        items = [r for r in rows if r["prefix"] == prefix and r["status"] == "ok"]
        if not items:
            continue
        add(f"### {prefix}（{len(items)} 个 ok）")
        sub = defaultdict(list)
        for r in items:
            parts = r["repo"].split("/")
            key = "/".join(parts[1:3]) if len(parts) > 2 else parts[1] if len(parts) > 1 else parts[0]
            sub[key].append(r)
        for key in sorted(sub):
            grp = sub[key]
            sample = next((i for i in grp if desc_of(i)), grp[0])
            add(f"- **{key}**（{len(grp)}）：{desc_of(sample)[:60] or '-'}")
        add("")
    add("## 4. 受限/不可访问仓库")
    for r in rows:
        if r["status"] == "restricted":
            add(f"- {r['repo']}")
    add("")
    add("## 5. 待补爬仓库（retry/pending）")
    for r in rows:
        if r["status"] in ("retry",) or r["status"] is None:
            add(f"- {r['repo']}")
    open(MD_PATH, "w", encoding="utf-8").write("\n".join(L))
    print(f"wrote {CSV_PATH}, {MD_PATH}")


if __name__ == "__main__":
    main()
