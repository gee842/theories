"""Re-point every Becoming record's validation scope from one consolidated run to the next.

Usage: repoint.py SPEC.json
SPEC: {"old_run", "new_run", "old_totals": [th, au], "new_totals": [th, au],
       "old_package", "new_package", "old_closure", "new_closure",
       "old_peri", "new_peri", "old_peri_rest", "new_peri_rest",
       "skip": [ids], "history_zh", "history_en"}
Only the receipt identifiers and counts change; claims and proofs do not.
"""
import json
import sys
from pathlib import Path

import os
ROOT = Path(os.environ["P45ROOT"])
REC = ROOT / "theories/becoming/results/records"
s = json.loads(Path(sys.argv[1]).read_text())

pairs = s.get("extra", []) + [
    ("（" + s["old_run"] + "）", "（" + s["new_run"] + "）"),
    ("(" + s["old_run"] + ")", "(" + s["new_run"] + ")"),
    ("共 %d 项定理／%d 项声明审计" % tuple(s["old_totals"]), "共 %d 项定理／%d 项声明审计" % tuple(s["new_totals"])),
    ("%d theorems/%d declaration audits" % tuple(s["old_totals"]), "%d theorems/%d declaration audits" % tuple(s["new_totals"])),
    ("包内 %d 个模块" % s["old_package"], "包内 %d 个模块" % s["new_package"]),
    ("package's %d modules" % s["old_package"], "package's %d modules" % s["new_package"]),
    ("恰为这 %d 个模块" % s["old_closure"], "恰为这 %d 个模块" % s["new_closure"]),
    ("exactly these %d modules" % s["old_closure"], "exactly these %d modules" % s["new_closure"]),
]
if s.get("old_peri"):
    pairs += [
        ("（" + s["old_peri"] + "）", "（" + s["new_peri"] + "）"),
        ("(" + s["old_peri"] + ")", "(" + s["new_peri"] + ")"),
        ("闭包中其余 %d 个模块" % s["old_peri_rest"], "闭包中其余 %d 个模块" % s["new_peri_rest"]),
        ("the other %d modules in its closure" % s["old_peri_rest"], "the other %d modules in its closure" % s["new_peri_rest"]),
    ]

for f in sorted(REC.glob("*.json")):
    r = json.loads(f.read_text())
    scope = r.get("validation_scope", {})
    if s["old_run"] not in scope.get("zh", "") or r["id"] in s.get("skip", []):
        continue
    for lang in ("zh", "en"):
        text = scope[lang]
        for old, new in pairs:
            text = text.replace(old, new)
        assert s["old_run"] not in text and s["new_run"] in text, (r["id"], lang)
        if s.get("old_peri") and s["old_peri"] in scope[lang]:
            assert s["old_peri"] not in text, (r["id"], lang)
        scope[lang] = text
    r["history"].append({"zh": s["history_zh"], "en": s["history_en"]})
    f.write_text(json.dumps(r, ensure_ascii=False, indent=2) + "\n")
    print("re-pointed", r["id"])
