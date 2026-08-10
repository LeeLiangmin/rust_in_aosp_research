#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verify analysis coverage against the live android.googlesource.com listing."""
import json
import re
import sqlite3
import sys

import requests

PROXIES = {"http": "http://127.0.0.1:7890", "https": "http://127.0.0.1:7890"}
UA = {"User-Agent": "Mozilla/5.0 AospVerify/1.0"}
DB = r"F:\lee_space\code\research\android\aosp_tree.db"

r = requests.get("https://android.googlesource.com/?format=HTML", proxies=PROXIES, headers=UA, timeout=90)
html_repos = set(re.findall(r'<a class="RepoList-item" href="/([^"]+)/">', r.text))
print("HTML repos:", len(html_repos))

r2 = requests.get("https://android.googlesource.com/?format=JSON", proxies=PROXIES, headers=UA, timeout=90)
t = r2.text
data = json.loads(t[t.find("{"):])
json_repos = set(data.keys())
print("JSON repos:", len(json_repos))

conn = sqlite3.connect(DB)
db_repos = {row[0] for row in conn.execute("SELECT repo FROM repos")}
print("DB repos:", len(db_repos))

miss_html = sorted(html_repos - db_repos)
extra_db = sorted(db_repos - html_repos)
jh_diff = sorted(json_repos ^ html_repos)
print()
print("HTML-DB (missing from analysis):", len(miss_html))
for x in miss_html:
    print("   ", x)
print("DB-HTML (in DB, not on HTML page):", len(extra_db))
for x in extra_db:
    print("   ", x)
print("JSON xor HTML:", len(jh_diff))
for x in jh_diff:
    print("   ", x)

# restricted repos still unanalyzed
rest = [row[0] for row in conn.execute("SELECT repo FROM repos WHERE status='restricted' ORDER BY repo")]
print()
print("restricted (crawled but content not fetched):", len(rest))
for x in rest:
    print("   ", x)
