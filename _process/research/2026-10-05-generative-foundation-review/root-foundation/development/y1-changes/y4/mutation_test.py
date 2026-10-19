#!/usr/bin/env python3
"""Y4: mutate each census (the Lean lists of Becoming.HexagramSites and the exceptions verify_mapping.py records), one
at a time, and confirm that verify_mapping.py fails; every file is restored after each run.
usage (from the repository root): python3 -B mutation_test.py
(the module in the package if it is there, as verify_mapping.py reads it, else the kit's copy)"""
import subprocess, sys
from pathlib import Path
K = Path('_process/research/2026-10-05-generative-foundation-review/root-foundation/development/y1-changes')
LEAN = Path('experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/HexagramSites.lean')
if not LEAN.exists():
    LEAN = K / 'y4/Becoming/HexagramSites.lean'
VM = K / 'verify_mapping.py'
M = [
 (LEAN, '(9, .p4, true), (13, .p2, true)', '(13, .p2, true)', '彖 place: one statement dropped'),
 (LEAN, '(53, true), (54, false)', '(53, true), (54, true)', '彖 whole: 歸妹 flipped'),
 (LEAN, '(8, .p5), (9, .p4), (14, .p5)', '(8, .p5), (14, .p5)', '彖 上下應: 小畜 dropped'),
 (LEAN, '(3, .p3), (7, .p2)', '(7, .p2)', '爻辭 中: 屯六三 dropped'),
 (LEAN, '[(45, .p5)]', '[(45, .p4)]', '爻辭 位: wrong place'),
 (LEAN, '(1, .p6, false), (5, .p6, false)', '(5, .p6, false)', '文言/小象 top: 乾上九 dropped'),
 (VM, None, None, '大象 中: one dropped'),
 (VM, None, None, '大象 位: one dropped'),
 (VM, None, None, '小象 中: one exception dropped'),
]
vm_text = VM.read_text()
import re
vm_mut = [
 re.sub(r'DAXIANG_WITHIN = \{7, ', 'DAXIANG_WITHIN = {', vm_text, count=1),
 re.sub(r"DAXIANG_PLACE = \{50: '君子以正位凝命', ", 'DAXIANG_PLACE = {', vm_text, count=1),
 re.sub(r"XIAOXIANG_MIDDLE_OTHER = \{\(11, 4\): '中心', ", 'XIAOXIANG_MIDDLE_OTHER = {', vm_text, count=1),
]
ok = True
for i, (path, old, new, label) in enumerate(M):
    orig = path.read_text()
    if path == VM:
        mutated = vm_mut[i - 6]
    else:
        assert orig.count(old) == 1, label
        mutated = orig.replace(old, new)
    assert mutated != orig, label
    path.write_text(mutated)
    try:
        r = subprocess.run([sys.executable, '-B', str(VM)], capture_output=True, text=True)
    finally:
        path.write_text(orig)
    caught = r.returncode != 0 and 'FAIL' in r.stdout + r.stderr
    ok &= caught
    print('caught' if caught else 'MISSED', label, '|', [l for l in (r.stdout + r.stderr).splitlines() if 'FAIL' in l][:1])
r = subprocess.run([sys.executable, '-B', str(VM)], capture_output=True, text=True)
print('clean after:', r.returncode, 'all caught:', ok)
