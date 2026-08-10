#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AOSP repo crawler (android.googlesource.com).

Phase 0: fetch root project list (?format=JSON + ?format=HTML).
Phase 1: for every repo, fetch <repo>/+/main/ (HTML) and extract:
         - rendered README text  -> repo purpose
         - top-level file/dir listing (free byproduct)
         - Rust signal flags (for later Rust mapping)
Store everything in a resumable SQLite DB. Run through local proxy.
"""
import argparse
import base64
import html
import json
import os
import re
import sqlite3
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

BASE = "https://android.googlesource.com"
PROXY = "http://127.0.0.1:7890"
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aosp_tree.db")
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AospCrawler/1.0"

REFS = ["main", "refs/heads/main", "master", "refs/heads/master"]

PROXIES = {"http": PROXY, "https": PROXY}

_lock = threading.Lock()
_tls = threading.local()


def _session():
    s = getattr(_tls, "sess", None)
    if s is None:
        s = requests.Session()
        s.headers.update({"User-Agent": UA})
        _tls.sess = s
    return s


# ---------------------------------------------------------------- http helpers
def http_get(url, timeout=25, retries=3):
    last = None
    for i in range(retries):
        try:
            r = _session().get(url, proxies=PROXIES, timeout=timeout)
            text = r.text
            # gitiles returns 200 even for some error pages; detect by content
            if re.search(r"(Error NOT_FOUND|NOT_FOUND: Requested entity|Cannot parse URL as a Gitiles URL|Object is not found)", text[:4000]):
                return r.status_code, None
            return r.status_code, text
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(2 * (i + 1))
    return -1, str(last)


# ---------------------------------------------------------------- parsing
def strip_tags(blob):
    blob = re.sub(r"<script[\s\S]*?</script>", " ", blob)
    blob = re.sub(r"<style[\s\S]*?</style>", " ", blob)
    blob = re.sub(r"<[^>]+>", " ", blob)
    blob = html.unescape(blob)
    blob = re.sub(r"\s+", " ", blob)
    return blob.strip()


TYPE_MAP = {"gitTree": "dir", "gitBlob": "file", "regularFile": "file",
             "symlink": "file", "gitCommitLink": "file"}

TITLE_MAP = {"Tree": "dir", "Blob": "file", "Regular file": "file",
             "Symlink": "file"}


def _extract_div_depth(html_text, open_tag):
    """Return inner HTML of the first <open_tag>...</div> matched by div depth.

    Only <div>/</div> tags are counted for depth; all other tags are ignored.
    """
    i = html_text.find(open_tag)
    if i < 0:
        return ""
    j = html_text.find(">", i)
    if j < 0:
        return ""
    start = j + 1
    depth = 0
    k = start
    while True:
        nxt = html_text.find("<", k)
        if nxt < 0:
            return ""
        end = html_text.find(">", nxt)
        if end < 0:
            return ""
        tag = html_text[nxt + 1:end].strip()
        if tag.startswith("div"):
            depth += 1
        elif tag == "/div":
            depth -= 1
            if depth < 0:
                return html_text[start:nxt]
        k = end + 1


def parse_repo_page(html_text):
    """Return (entries, readme) from a gitiles <repo>/+/main/ HTML page."""
    entries = []
    # entries appear both on repo-root page and subdir pages
    for mm in re.finditer(
        r'<li[^>]*class="FileList-item FileList-item--([a-zA-Z]+)"[^>]*title="[^"]*?-\s*([^"]+)"[^>]*>',
        html_text,
    ):
        cls = mm.group(1)
        raw_name = html.unescape(mm.group(2)).strip().strip("/")
        kind = TYPE_MAP.get(cls) or ("dir" if "Tree" in cls else "file")
        if raw_name:
            entries.append({"type": kind, "name": raw_name})
    # fallback: title-only anchors
    if not entries:
        for mm in re.finditer(r'title="((?:Tree|Blob|Regular file|Symlink)) - ([^"]+)"', html_text):
            entries.append({"type": TITLE_MAP.get(mm.group(1), "file"), "name": mm.group(2).strip(" /")})
    seen = set()
    uniq = []
    for e in entries:
        key = (e["type"], e["name"])
        if key not in seen:
            seen.add(key)
            uniq.append(e)
    entries = uniq

    readme = ""
    inner = _extract_div_depth(html_text, '<div class="InlineReadme">')
    if inner:
        # drop the "path" header line, keep the doc body
        m = re.search(r'<div class="doc">([\s\S]*?)(</div>\s*</div>|\Z)', inner)
        body = m.group(1) if m else inner
        readme = strip_tags(body)
    return entries, readme[:1000]


def rust_signals(entries):
    signals = []
    for e in entries:
        n = e["name"].lower()
        if e["name"].endswith(".rs"):
            signals.append("rs_file")
        elif n == "cargo.toml" or n == "cargo.lock":
            signals.append("cargo")
        elif n == "rustfmt.toml":
            signals.append("rustfmt")
        elif n == "android.bp":
            signals.append("androidbp")
        elif n == "rust" or n.startswith("rust_"):
            signals.append("rust_dir")
    return sorted(set(signals))


# ---------------------------------------------------------------- db
def db_connect():
    conn = sqlite3.connect(DB_PATH, timeout=30, check_same_thread=False)
    conn.execute("PRAGMA journal_mode=WAL")
    return conn


def init_db(conn):
    conn.executescript("""
    CREATE TABLE IF NOT EXISTS repos (
        repo TEXT PRIMARY KEY,
        clone_url TEXT,
        prefix TEXT,
        desc_root TEXT,
        readme TEXT,
        top_level_json TEXT,
        rust_signal TEXT,
        status TEXT,
        fetched_at TEXT
    );
    CREATE TABLE IF NOT EXISTS crawl_log (
        repo TEXT,
        url TEXT,
        status_code INTEGER,
        note TEXT,
        ts TEXT
    );
    """)
    conn.commit()


# ---------------------------------------------------------------- phase 0
def phase0(conn):
    cur = conn.cursor()
    code, text = http_get(BASE + "/?format=JSON", timeout=60, retries=4)
    if text is None:
        raise SystemExit(f"phase0 JSON failed: {code}")
    i = text.find("{")
    data = json.loads(text[i:])
    desc = {}
    code, htext = http_get(BASE + "/?format=HTML", timeout=60, retries=4)
    if htext:
        for mm in re.finditer(
            r'<a class="RepoList-item" href="/([^"]+)/">[\s\S]*?'
            r'<span class="RepoList-itemName">([^<]*)</span>'
            r'<span class="RepoList-itemDescription">([^<]*)</span>',
            htext,
        ):
            desc[mm.group(1)] = html.unescape(mm.group(3)).strip()
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    n = 0
    for name, info in data.items():
        prefix = name.split("/")[0]
        cur.execute(
            "INSERT OR IGNORE INTO repos(repo, clone_url, prefix, desc_root, status, fetched_at)"
            " VALUES(?,?,?,?,NULL,?)",
            (name, info.get("clone_url", ""), prefix, desc.get(name, ""), now),
        )
        n += 1
    conn.commit()
    print(f"[phase0] {n} repos in DB")
    return n


# ---------------------------------------------------------------- phase 1
def fetch_one(repo):
    """Return (status, url, entries, readme) for one repo.

    Tries the repo's default HEAD first, then common branch names, and keeps
    the first NON-EMPTY tree (repos often keep content on a branch other than
    'main'). status: 'ok' | 'empty_ok' | 'retry' | 'restricted'.
    """
    refs = ["HEAD", "master", "main"]
    empty_seen = None
    anom = False
    last_url = None
    for ref in refs:
        url = f"{BASE}/{repo}/+/{ref}/"
        last_url = url
        code, text = http_get(url)
        if text is None:
            if code in (403, 404):
                continue
            anom = True
            time.sleep(1.5)
            continue
        entries, readme = parse_repo_page(text)
        if entries or readme:
            return "ok", url, entries, readme
        if "This tree is empty" in text:
            if empty_seen is None:
                empty_seen = ("empty_ok", url, [], "")
        else:
            anom = True  # suspicious page (throttle/edge); keep looking
    if empty_seen:
        return empty_seen
    if anom:
        return "retry", last_url, [], ""
    return "restricted", None, [], ""


def worker(repo, conn):
    status, url, entries, readme = fetch_one(repo)
    signal = ",".join(rust_signals(entries)) if status == "ok" else ""
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    with _lock:
        cur = conn.cursor()
        if status in ("ok", "empty_ok"):
            cur.execute(
                "UPDATE repos SET readme=?, top_level_json=?, rust_signal=?, status=?, fetched_at=? WHERE repo=?",
                (readme, json.dumps(entries, ensure_ascii=False), signal, status, now, repo),
            )
        elif status == "retry":
            cur.execute("UPDATE repos SET status='retry', fetched_at=? WHERE repo=?", (now, repo))
        else:
            cur.execute("UPDATE repos SET status='restricted', fetched_at=? WHERE repo=?", (now, repo))
        cur.execute("INSERT INTO crawl_log(repo,url,status_code,note,ts) VALUES(?,?,?,?,?)",
                    (repo, url, 200 if status in ("ok", "empty_ok") else 404, status, now))
        conn.commit()
    return status


_last_slot = [0.0]
_slot_lock = threading.Lock()


def _rate_gate(min_interval):
    with _slot_lock:
        now = time.time()
        wait = _last_slot[0] + min_interval - now
        if wait > 0:
            time.sleep(wait)
        _last_slot[0] = time.time()


def run_phase1(limit=None, start_after=None, workers=6, min_interval=0.25, max_passes=6):
    conn = db_connect()
    init_db(conn)
    pending_status = ["NULL", "retry"]
    total_done = 0
    for pass_no in range(1, max_passes + 1):
        q = "SELECT repo FROM repos WHERE (status IS NULL OR status='retry')"
        params = []
        if start_after:
            q += " AND repo > ?"
            params.append(start_after)
        q += " ORDER BY repo"
        if limit:
            q += " LIMIT ?"
            params.append(limit)
        repos = [r[0] for r in conn.execute(q, params).fetchall()]
        if not repos:
            break
        print(f"[phase1 pass{pass_no}] pending: {len(repos)}")
        done = [0]
        t0 = time.time()
        last_log = [0]

        def _worker(repo):
            _rate_gate(min_interval)
            st = worker(repo, conn)
            with _lock:
                done[0] += 1
                if done[0] - last_log[0] >= 100 or done[0] == len(repos):
                    last_log[0] = done[0]
                    el = time.time() - t0
                    rate = done[0] / el if el > 0 else 0
                    print(f"  [{done[0]}/{len(repos)}] last={repo} rate={rate:.2f}/s")
            return repo, st

        results = {}
        with ThreadPoolExecutor(max_workers=workers) as ex:
            futs = [ex.submit(_worker, r) for r in repos]
            for f in as_completed(futs):
                repo, st = f.result()
                results[st] = results.get(st, 0) + 1
        total_done += sum(results.values())
        print(f"[phase1 pass{pass_no}] results={results}")
        # if nothing retryable remains, stop; else cool down before another pass
        nretry = results.get("retry", 0)
        if nretry == 0 or pass_no == max_passes:
            break
        print(f"  cooldown 60s before re-crawling {nretry} retry repos...")
        time.sleep(60)
    conn.close()
    return total_done


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", choices=["0", "1", "all"], default="all")
    ap.add_argument("--limit", type=int, default=None, help="only process N pending repos")
    ap.add_argument("--start-after", default=None, help="resume after this repo name")
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--min-interval", type=float, default=0.25,
                    help="global minimum interval between requests (seconds)")
    ap.add_argument("--max-passes", type=int, default=6,
                    help="max re-crawl passes for throttled (retry) repos")
    args = ap.parse_args()

    conn = db_connect()
    init_db(conn)
    if args.phase in ("0", "all"):
        phase0(conn)
    conn.close()
    if args.phase in ("1", "all"):
        run_phase1(limit=args.limit, start_after=args.start_after, workers=args.workers,
                   min_interval=args.min_interval, max_passes=args.max_passes)
    print("done.")


if __name__ == "__main__":
    main()
