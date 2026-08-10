#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate aosp_tree.html: interactive collapsible tree of all AOSP repos.
Rust-related nodes are colored by language verdict:
  pure      - pure Rust (only .rs)
  rust_main - Rust >= 50% of compiled source
  hybrid    - Rust mixed with C/C++/Java/Go etc.
  signal    - has Rust signal (cargo/rustfmt/.rs) but not analyzed
"""
import html
import json
import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "aosp_tree.db")
OUT = os.path.join(BASE_DIR, "aosp_tree.html")

conn = sqlite3.connect(DB_PATH)
repos = conn.execute("SELECT repo, rust_signal, status FROM repos").fetchall()
verdicts = dict(conn.execute("SELECT repo, verdict FROM lang_stats").fetchall())
conn.close()

HAS_SIGNAL = {"cargo", "rustfmt", "rust_dir", "rs_file"}


def has_rust_signal(sig):
    return bool(sig) and bool(HAS_SIGNAL & set(sig.split(",")))


root = {}
counts = {"total": 0, "pure": 0, "rust_main": 0, "hybrid": 0, "signal": 0, "non_rust": 0}

for repo, sig, status in repos:
    parts = repo.split("/")
    node = root
    for p in parts:
        node = node.setdefault(p, {})
    verdict = verdicts.get(repo)
    rust = verdict in ("pure", "rust_main", "hybrid") or (verdict is None and has_rust_signal(sig))
    cls = verdict if verdict in ("pure", "rust_main", "hybrid", "non_rust") else ("signal" if has_rust_signal(sig) else "")
    node["__leaf__"] = (repo, cls, status)
    counts["total"] += 1
    counts[cls if cls else "non_rust"] += 1


def render(node, name, depth):
    children = {k: v for k, v in node.items() if k != "__leaf__"}
    leaf = node.get("__leaf__")
    total_sub = rust_sub = 0

    def count(n):
        nonlocal total_sub, rust_sub
        for k, v in n.items():
            if k == "__leaf__":
                total_sub += 1
                if v[1] in ("pure", "rust_main", "hybrid", "signal"):
                    rust_sub += 1
            else:
                count(v)

    count(node)
    if leaf and not children:
        repo, cls, status = leaf
        url = f"https://android.googlesource.com/{repo}"
        badge = f' <span class="st">{status}</span>' if status not in ("ok", None) else ""
        return (f'<li class="leaf {cls}"><a href="{url}" target="_blank">{html.escape(name)}</a>{badge}</li>',
                total_sub, rust_sub)
    open_attr = " open" if depth < 1 and rust_sub else ""
    tag = f'<span class="cnt">{rust_sub}/{total_sub}</span>' if rust_sub else f'<span class="cnt dim">{total_sub}</span>'
    hl = " hasrust" if rust_sub else ""
    items = []
    if leaf:
        items.append(render({"__leaf__": leaf}, "(self)", depth)[0])
    for k in sorted(children):
        items.append(render(children[k], k, depth + 1)[0])
    body = "".join(items)
    return (f'<li class="dir{hl}"><details{open_attr}><summary>{html.escape(name)} {tag}</summary>'
            f'<ul>{body}</ul></details></li>', total_sub, rust_sub)


rows = "".join(render(root[k], k, 0)[0] for k in sorted(root))

page = f"""<!DOCTYPE html>
<html lang="zh">
<head>
<meta charset="utf-8">
<title>AOSP Repo Tree - Rust Map</title>
<style>
body {{ font-family: Consolas, "Courier New", monospace; background:#1e1e1e; color:#d4d4d4; margin:2em; }}
h1 {{ font-size:1.3em; }}
.legend span {{ padding:2px 8px; margin-right:6px; border-radius:3px; font-size:.85em; }}
ul {{ list-style:none; margin:0; padding-left:1.4em; }}
li {{ line-height:1.5; }}
summary {{ cursor:pointer; }}
summary:hover {{ color:#fff; }}
a {{ color:inherit; text-decoration:none; }}
a:hover {{ text-decoration:underline; }}
.cnt {{ color:#4ec9b0; font-size:.8em; margin-left:.5em; }}
.cnt.dim {{ color:#666; }}
.st {{ color:#c586c0; font-size:.75em; }}
.pure > a, .pure > summary {{ background:#2d6a2d; color:#fff; }}
.rust_main > a {{ background:#7a5c00; color:#fff; }}
.hybrid > a {{ background:#7a3b00; color:#ffd8a8; }}
.signal > a {{ background:#23415e; color:#9cdcfe; }}
li.pure > a, li.rust_main > a, li.hybrid > a, li.signal > a {{ padding:0 4px; border-radius:3px; }}
.lg-pure {{ background:#2d6a2d; color:#fff; }}
.lg-main {{ background:#7a5c00; color:#fff; }}
.lg-hybrid {{ background:#7a3b00; color:#ffd8a8; }}
.lg-signal {{ background:#23415e; color:#9cdcfe; }}
.lg-plain {{ background:#333; color:#aaa; }}
.dir.hasrust > summary {{ color:#e8e8e8; font-weight:bold; }}
</style>
</head>
<body>
<h1>AOSP 仓库树（{counts['total']} repos）— Rust 分布图</h1>
<p class="legend">
图例：
<span class="lg-pure">纯 Rust ×{counts['pure']}</span>
<span class="lg-main">Rust 为主 ×{counts['rust_main']}</span>
<span class="lg-hybrid">混合(Rust+C/C++/Java…) ×{counts['hybrid']}</span>
<span class="lg-signal">有 Rust 信号(未分析) ×{counts['signal']}</span>
<span class="lg-plain">非 Rust / 无信号</span>
<br>节点旁 <span class="cnt">rust数/总数</span>；点击仓库名跳转 gitiles。
</p>
<ul>{rows}</ul>
</body>
</html>"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(page)
print(f"wrote {OUT} ({os.path.getsize(OUT)} bytes)")
print(counts)
