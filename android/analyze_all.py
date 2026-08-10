#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Analyze remaining repos via TUNA AOSP mirror (googlesource unreachable).

Fetches only git tree objects (no blobs): git clone --bare --depth 1
--filter=blob:none, then `git ls-tree -r --name-only HEAD` to count file
extensions. Classifies with analyze_lang.classify and stores in lang_stats.
"""
import json
import os
import shutil
import sqlite3
import subprocess
import tempfile
import time
import collections

import analyze_lang as al

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aosp_tree.db")
MIRROR = "https://aosp.tuna.tsinghua.edu.cn"
REFS = ["main", "master"]
BATCH_SIZE = 40  # repos per git invocation batch (sequential clones)


def bump(counts, path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".rs":
        counts["rs"] += 1
    elif ext in al.C_SRC_EXTS:
        counts["c" if ext in (".c", ".m", ".mm") else "cc"] += 1
    elif ext in al.C_HDR_EXTS:
        counts["h"] += 1
    elif ext in (".s", ".asm"):
        counts["asm"] += 1
    elif ext == ".java":
        counts["java"] += 1
    elif ext in (".kt", ".kts"):
        counts["kotlin"] += 1
    elif ext == ".go":
        counts["go"] += 1
    elif ext == ".py":
        counts["python"] += 1
    elif ext == ".proto":
        counts["proto"] += 1
    elif ext == ".aidl":
        counts["aidl"] += 1
    elif ext in (".mk", ".bp"):
        counts["mk"] += 1
    elif ext:
        counts["other"] += 1


def force_rmtree(path):
    def onerror(func, p, exc_info):
        os.chmod(p, 0o777)
        func(p)
    shutil.rmtree(path, onerror=onerror)


def analyze_repo(repo, workdir):
    dest = os.path.join(workdir, "r.git")
    if os.path.exists(dest):
        force_rmtree(dest)
    os.makedirs(dest, exist_ok=True)
    for ref in REFS:
        url = f"{MIRROR}/{repo}"
        r = subprocess.run(
            ["git", "clone", "--bare", "--depth", "1", "--filter=blob:none",
             "--single-branch", "--branch", ref, url, dest],
            capture_output=True, timeout=600)
        if r.returncode != 0:
            continue
        ls = subprocess.run(["git", "--git-dir", dest, "ls-tree", "-r",
                             "--name-only", "HEAD"], capture_output=True,
                            timeout=300)
        if ls.returncode != 0:
            continue
        counts = collections.Counter()
        for line in ls.stdout.decode("utf-8", "replace").splitlines():
            top = line.split("/", 1)[0]
            if top in (".git", "out", "target", "prebuilts"):
                continue
            bump(counts, line)
        return counts
    return None


def worker(repo, idx, total, workdir, conn, lock):
    try:
        counts = analyze_repo(repo, workdir)
    except Exception as e:
        print(f"  [{idx}/{total}] {repo} -> ERROR {e}", flush=True)
        return
    if not counts:
        print(f"  [{idx}/{total}] {repo} -> SKIPPED (clone failed)", flush=True)
        return
    verdict = al.classify(counts)
    with lock:
        conn.execute(
            "INSERT OR REPLACE INTO lang_stats(repo, counts, verdict, fetched_at) "
            "VALUES(?,?,?,?)",
            (repo, json.dumps(dict(counts), ensure_ascii=False), verdict,
             time.strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()
    summary = " ".join(f"{k}:{v}" for k, v in sorted(counts.items()))
    print(f"  [{idx}/{total}] {repo} -> {verdict} | {summary}", flush=True)


def main():
    import concurrent.futures
    import threading
    with open("todo_repos.txt", encoding="utf-8") as f:
        repos = [ln.strip() for ln in f if ln.strip()]
    conn = sqlite3.connect(DB_PATH, timeout=60, check_same_thread=False)
    conn.execute("""CREATE TABLE IF NOT EXISTS lang_stats(
        repo TEXT PRIMARY KEY, counts TEXT, verdict TEXT, fetched_at TEXT)""")
    lock = threading.Lock()
    todo = [r for r in repos
            if not conn.execute("SELECT 1 FROM lang_stats WHERE repo=?",
                                (r,)).fetchone()]
    total = len(todo)
    print(f"remaining: {total}", flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        futs = []
        for i, repo in enumerate(todo, 1):
            wd = tempfile.mkdtemp(prefix="aosp_git_")
            futs.append(ex.submit(worker, repo, i, total, wd, conn, lock))
        for f in concurrent.futures.as_completed(futs):
            f.result()
    conn.close()


if __name__ == "__main__":
    main()
