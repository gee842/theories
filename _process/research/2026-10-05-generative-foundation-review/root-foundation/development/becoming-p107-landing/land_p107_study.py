#!/usr/bin/env python3
"""P107 landing edits to the study and the inventory script that need the checked runs.

usage: land_p107_study.py ROOT N CORE_RECEIPT PERIPHERY_RECEIPT (receipts relative to ROOT)
1. Section N's evidence lines name the landed core run (spine modules, theorems, declaration audits
   from its receipt) and the CorrectionInquiry periphery run, in both languages.
2. DECIDABILITY-INVENTORY.py classifies the one new proof-only binder, Becoming.Novelty's
   upto_or_fails (finitely many steps checked, a failing one found), as finding a step.
Every replacement asserts the text it replaces.
"""
import json
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve()
N = int(sys.argv[2])
CORE, PERI = sys.argv[3], sys.argv[4]
RF = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation'


def sub1(s, old, new):
    assert s.count(old) == 1, (s.count(old), old[:90])
    return s.replace(old, new)


run = json.loads((ROOT / CORE).read_text())
peri = json.loads((ROOT / PERI).read_text())
assert run['status'] == 'passed' and peri['status'] == 'passed', (run['status'], peri['status'])
utc, putc = CORE.split('/')[-2], PERI.split('/')[-2]
spine = [m for m in run['modules'] if m['spine']]
theorems, audits = sum(m['theorems'] for m in spine), sum(len(m['declarations']) for m in spine)
p107 = {m['module']: m['theorems'] for m in spine if m['module'] in ('Becoming.Novelty', 'Becoming.Reading', 'Becoming.Readings')}
assert sum(p107.values()) == 66 and len(p107) == 3, p107
peri_core = sorted(k for k in peri['source_sha256'] if k.startswith('Becoming'))
# the periphery compiles the core closure (the four bridge modules are outside it) on the same bytes
missing = [m for m in run['core_closure'] if peri['source_sha256'].get(m) != run['source_sha256'].get(m)]
assert not missing, ('periphery run does not cover the core closure byte for byte', missing)

p = RF / 'BECOMING-RENEWAL-READING.md'
s = p.read_text()
head = s.index(f'## {N}. 从关系开始的重建：')
nxt = s.find('\n## ', head + 1)
sec = s[head:nxt if nxt != -1 else None]
new_sec = sub1(sec, 'Evidence: scratch_build 实编（对 main a4e4c4a8 的模块）：每条声明公理报告为空，无警告；不是回执，回执见落地提交',
               'Evidence: scratch_build 实编（对 main d8236061 的模块）：每条声明公理报告为空，无警告；落地的核心检查器回执 '
               f'{utc}\n          通过（{len(spine)} 个脊柱模块、{theorems} 项定理、{audits} 项声明审计，核心公理报告为空）；'
               f'外围 CorrectionInquiry 回执 {putc}\n          通过（核心在 Lean 4.30.0-rc2 与 Mathlib 下同样编译）')
s = s[:head] + new_sec + s[head + len(sec):]
s = sub1(s, f'Section {N} adds three core modules (66 theorems, no premise).',
         f'Section {N} adds three core modules (66 theorems, no premise; core receipt {utc}, CorrectionInquiry periphery '
         f'receipt {putc}).')
p.write_text(s)

q = RF / 'DECIDABILITY-INVENTORY.py'
t = q.read_text()
assert "'upto_or_fails'" not in t
t = sub1(t, "\n}\n# Proved to need decidedness where asked of every world: the boundary theorems.",
         "\n    # 2026-10-14, the relation-first re-founding (Becoming.Novelty): finitely many steps checked, a failing one found"
         "\n    'upto_or_fails': 'find',"
         "\n}\n# Proved to need decidedness where asked of every world: the boundary theorems.")
q.write_text(t)
print('study section', N, 'evidence:', utc, len(spine), theorems, audits, '; periphery', putc,
      f'({len(peri_core)} core modules); inventory: upto_or_fails -> find')
