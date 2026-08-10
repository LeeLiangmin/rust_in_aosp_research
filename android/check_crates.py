import sqlite3
c = sqlite3.connect("aosp_tree.db")
q = "SELECT COUNT(*) FROM repos WHERE repo LIKE 'platform/external/rust/crates/%'"
print("crates total:", c.execute(q).fetchone()[0])
q2 = q + " AND rust_signal != ''"
print("crates with signal:", c.execute(q2).fetchone()[0])
print("done:", c.execute(
    "SELECT COUNT(*) FROM lang_stats WHERE repo LIKE 'platform/external/rust/crates/%'"
).fetchone()[0])
for r in c.execute(
    "SELECT repo, rust_signal, status FROM repos WHERE repo LIKE "
    "'platform/external/rust/crates/%' AND (rust_signal='' OR rust_signal IS NULL) LIMIT 10"
):
    print(" ", r)
