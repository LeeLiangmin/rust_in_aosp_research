#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Analyze each Rust-related AOSP repo's language composition (pure Rust vs hybrid).

For every repo we download the gitiles snapshot tarball (+archive/<ref>.tar.gz) and
count file extensions locally. Verdicts:
  - pure        : ~only Rust sources (no real C/C++/Java/Kotlin/Go source)
  - rust+header : Rust + FFI C headers (bindgen) but no C/C++ source
  - hybrid      : Rust + significant C/C++ or other-language source
  - non_rust    : no Rust source (e.g. build/soong is Go, carries Rust rules)
Results stored in aosp_tree.db table `lang_stats` and used by make_rust_report.py.
"""
import argparse
import collections
import json
import os
import re
import sqlite3
import tarfile
import tempfile
import threading
import time

import requests

BASE = "https://android.googlesource.com"
PROXY = "http://127.0.0.1:7890"
PROXIES = {"http": PROXY, "https": PROXY}
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aosp_tree.db")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AospAnalyzer/1.0"
REFS = ["refs/heads/main", "main", "HEAD", "master"]

SRC_EXTS = {
    "rs": ".rs",
    "c": (".c",), "cc": (".cc", ".cpp", ".cxx", ".cp"), "h": (".h", ".hh", ".hpp", ".hxx", ".inl"),
    "asm": (".s", ".S", ".asm"), "java": ".java", "kotlin": (".kt", ".kts"),
    "go": ".go", "python": ".py", "proto": ".proto", "aidl": ".aidl", "sh": ".sh",
    "mk": (".mk", ".bp"), "other": None,
}

C_SRC_EXTS = (".c", ".cc", ".cpp", ".cxx", ".cp", ".m", ".mm")
C_HDR_EXTS = (".h", ".hh", ".hpp", ".hxx", ".inl")
OTHER_SRC_EXTS = (".java", ".kt", ".kts", ".go", ".py", ".js", ".ts", ".proto", ".aidl")

_lock = threading.Lock()


def classify(counts):
    """Ratio-based verdict:
    pure      - only Rust sources
    rust_main - Rust >= 50% of compiled source
    hybrid    - Rust < 50% (mixed, other languages dominate)
    non_rust  - no Rust source (tooling carrying Rust support)
    """
    rs = counts.get("rs", 0)
    other = (counts.get("c", 0) + counts.get("cc", 0) + counts.get("asm", 0)
             + counts.get("java", 0) + counts.get("kotlin", 0) + counts.get("go", 0)
             + counts.get("python", 0) + counts.get("proto", 0) + counts.get("aidl", 0))
    if rs == 0:
        return "non_rust"
    if other == 0:
        return "pure"
    ratio = rs / (rs + other)
    if ratio >= 0.5:
        return "rust_main"
    return "hybrid"


def count_extensions(tar_path):
    counts = collections.Counter()
    with tarfile.open(tar_path, "r:gz") as tf:
        for m in tf:
            if not m.isfile():
                continue
            name = m.name
            if name.startswith((".git/", "out/", "target/", "prebuilts/")):
                continue
            ext = os.path.splitext(name)[1].lower()
            if ext in (".rs",):
                counts["rs"] += 1
            elif ext in C_SRC_EXTS:
                counts["c" if ext in (".c", ".m", ".mm") else "cc"] += 1
            elif ext in C_HDR_EXTS:
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
    return counts


def count_ext(tar_path):
    return count_extensions(tar_path)


def analyze_walk(repo, cap=90):
    """Fallback: walk the repo tree via gitiles JSON, counting extensions (capped)."""
    counts = collections.Counter()
    reqs = [0]

    def bump(ext):
        if ext in (".rs",):
            counts["rs"] += 1
        elif ext in C_SRC_EXTS:
            counts["c" if ext in (".c", ".m", ".mm") else "cc"] += 1
        elif ext in C_HDR_EXTS:
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

    def walk(sub):
        if reqs[0] >= cap:
            return
        reqs[0] += 1
        url = f"{BASE}/{repo}/+/main/{sub}?format=JSON"
        try:
            r = requests.get(url, proxies=PROXIES, headers={"User-Agent": UA}, timeout=25)
            txt = r.text
        except Exception:  # noqa: BLE001
            return
        i = txt.find("{")
        if i < 0:
            return
        try:
            obj = json.loads(txt[i:])
        except Exception:  # noqa: BLE001
            return
        for e in obj.get("entries", []):
            if reqs[0] >= cap:
                return
            if e.get("type") == "blob":
                ext = os.path.splitext(e.get("name", ""))[1].lower()
                bump(ext)
            elif e.get("type") == "tree":
                n = e.get("name", "")
                if n in ("out", "target", ".cargo", "prebuilts", "res", "assets"):
                    continue
                walk(sub + n + "/")

    walk("")
    counts["partial"] = reqs[0]
    return counts


def download(repo, dest):
    for ref in REFS:
        url = f"{BASE}/{repo}/+archive/{ref}.tar.gz"
        try:
            r = requests.get(url, proxies=PROXIES, headers={"User-Agent": UA},
                             timeout=120, stream=True)
            if r.status_code != 200:
                r.close()
                continue
            with open(dest, "wb") as f:
                for chunk in r.iter_content(1 << 20):
                    f.write(chunk)
            if os.path.getsize(dest) < 100:
                os.remove(dest)
                continue
            return url
        except Exception:  # noqa: BLE001
            time.sleep(3)
            continue
    return None


def analyze_one(repo, tmpdir):
    dest = os.path.join(tmpdir, "repo.tar.gz")
    url = download(repo, dest)
    counts = None
    if url is not None:
        try:
            counts = count_extensions(dest)
        except Exception:  # noqa: BLE001
            counts = None
        finally:
            if os.path.exists(dest):
                os.remove(dest)
    if counts is None:
        counts = analyze_walk(repo)
    counts["verdict"] = classify(counts)
    return counts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repos", nargs="*", default=None,
                    help="repos to analyze; default = curated set in make_rust_report")
    ap.add_argument("--db-only", action="store_true",
                    help="only emit missing repos from the curated set")
    ap.add_argument("--reclassify", action="store_true",
                    help="recompute verdicts from already-stored counts (no network)")
    args = ap.parse_args()

    conn = sqlite3.connect(DB_PATH, timeout=30, check_same_thread=False)
    conn.execute("""CREATE TABLE IF NOT EXISTS lang_stats(
        repo TEXT PRIMARY KEY, counts TEXT, verdict TEXT, fetched_at TEXT)""")

    if args.reclassify:
        rows = conn.execute("SELECT repo, counts FROM lang_stats").fetchall()
        n = 0
        for repo, cj in rows:
            counts = json.loads(cj)
            v = classify(counts)
            conn.execute("UPDATE lang_stats SET verdict=? WHERE repo=?", (v, repo))
            n += 1
        conn.commit()
        print(f"reclassified {n} repos")
        return

    if not args.repos:
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "mrr", os.path.join(os.path.dirname(os.path.abspath(__file__)), "make_rust_report.py"))
        mrr = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mrr)
        repos = list(mrr.CURATED.keys()) + ["toolchain/rustc"]
        repos = sorted(set(repos))
    else:
        repos = args.repos

    conn = sqlite3.connect(DB_PATH, timeout=30, check_same_thread=False)
    conn.execute("""CREATE TABLE IF NOT EXISTS lang_stats(
        repo TEXT PRIMARY KEY, counts TEXT, verdict TEXT, fetched_at TEXT)""")
    if args.db_only:
        done = {r[0] for r in conn.execute("SELECT repo FROM lang_stats")}
        repos = [r for r in repos if r not in done]

    print(f"repos to analyze: {len(repos)}")
    tmpdir = tempfile.mkdtemp(prefix="aosp_lang_")
    for i, repo in enumerate(repos, 1):
        if conn.execute("SELECT 1 FROM lang_stats WHERE repo=?", (repo,)).fetchone():
            continue
        counts = analyze_one(repo, tmpdir)
        total = sum(v for k, v in counts.items() if k not in ("verdict", "partial"))
        if counts.get("verdict") == "non_rust" and total == 0:
            print(f"  [{i}/{len(repos)}] {repo} -> SKIPPED (no data, network?)")
            continue
        verdict = counts.pop("verdict")
        conn.execute(
            "INSERT OR REPLACE INTO lang_stats(repo, counts, verdict, fetched_at) VALUES(?,?,?,?)",
            (repo, json.dumps(counts, ensure_ascii=False), verdict,
             time.strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()
        summary = " ".join(f"{k}:{v}" for k, v in sorted(counts.items()))
        print(f"  [{i}/{len(repos)}] {repo} -> {verdict} | {summary}")
        time.sleep(0.4)
    conn.close()


if __name__ == "__main__":
    main()
