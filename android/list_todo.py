#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Export repos with rust signal but not yet analyzed to todo_repos.txt."""
import sqlite3

conn = sqlite3.connect("aosp_tree.db")
done = {r[0] for r in conn.execute("SELECT repo FROM lang_stats")}
sig = [r[0] for r in conn.execute(
    "SELECT repo FROM repos WHERE rust_signal LIKE '%cargo%' "
    "OR rust_signal LIKE '%rustfmt%' OR rust_signal LIKE '%rust_dir%' "
    "OR rust_signal LIKE '%rs_file%' "
    "OR repo LIKE 'platform/external/rust/crates/%'")]
todo = sorted(r for r in sig if r not in done)
print(f"signal repos: {len(sig)}, already analyzed: {len(sig) - len(todo)}, todo: {len(todo)}")
with open("todo_repos.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(todo))
