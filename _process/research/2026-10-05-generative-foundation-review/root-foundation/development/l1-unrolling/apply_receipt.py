#!/usr/bin/env python3
"""Apply L1's receipt and connectivity edits to chapter section 9: python3 -B apply_receipt.py."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
C = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
OLD_R, NEW_R = '20261018T060442.434639Z', '20261018T070401.460540Z'
STUDY = '../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'

text = C.read_text()
start = text.index('**The current receipt.**')
end = text.index('| Generated `injEq` lemmas', start)
para = text[start:end]
edits = [
    (f'is run `{OLD_R}`, frozen in [`becoming-checks/{OLD_R}/`](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/becoming-checks/{OLD_R}/verification.json)',
     f'is run `{NEW_R}`, frozen in [`becoming-checks/{NEW_R}/`](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/becoming-checks/{NEW_R}/verification.json)'),
    ('on main bfc3bd6f1 (after R2, `Becoming.CensusCounts`, and the R2b claim) with R2b (`Becoming.CensusBinding`, '
     f'[study §171]({STUDY}#171-the-binding-laws-of-counting-where-the-counts-exist-r2b)) in the working tree',
     'on main e658aa022 (after N5, the N1 renaming, and the L1 claim) with L1 (`Becoming.Unrolling`, '
     f'[study §173]({STUDY}#173-what-an-extrapolation-given-nothing-fixes-l1)) in the working tree'),
    ('| 177 modules, 7,562 theorems |', '| 178 modules, 7,577 theorems |'),
    ('| 180 modules, 7,636 theorems |', '| 181 modules, 7,651 theorems |'),
    ('| Spine (core and bridge) | 8,163 theorems |', '| Spine (core and bridge) | 8,178 theorems |'),
    ('| Audited spine declarations | 10,988 |', '| Audited spine declarations | 11,010 |'),
    ('| Modules in the compile order | 320 |', '| Modules in the compile order | 321 |'),
]
for old, new in edits:
    assert para.count(old) == 1, ('receipt edit does not match once', old[:70])
    para = para.replace(old, new)
text = text[:start] + para + text[end:]
old = '`Counts.pos_of_mem`, an apart root, is now used on the base and left the apart register.'
assert text.count(old) == 1
text = text.replace(old, old + f' Rerun with L1 (receipt {NEW_R}), it counts 177 of 8,178, none in `Becoming.Unrolling`.')
C.write_text(text)
print('applied')
