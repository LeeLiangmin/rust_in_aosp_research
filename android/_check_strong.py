#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect("aosp_tree.db")
strong = set()
for repo, sig in conn.execute(
        "SELECT repo, rust_signal FROM repos WHERE rust_signal IS NOT NULL AND rust_signal<>''"):
    if set(sig.split(",")) - {"androidbp"}:
        strong.add(repo)
done = {r[0] for r in conn.execute("SELECT repo FROM lang_stats")}
print("strong total:", len(strong))
print("strong done:", len(strong & done))
print("strong missing:", len(strong - done))
todo = {ln.strip() for ln in open("todo_repos.txt", encoding="utf-8") if ln.strip()}
print("todo list:", len(todo))
print("strong missing not in todo:", sorted(strong - done - todo))
