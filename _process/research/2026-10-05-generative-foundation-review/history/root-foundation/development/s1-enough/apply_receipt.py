#!/usr/bin/env python3
"""Apply S1's receipt and connectivity edits to chapter section 9: python3 -B apply_receipt.py."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
C = ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
OLD_R, NEW_R = '20261018T070401.460540Z', '20261018T073050.517313Z'
STUDY = '../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md'

text = C.read_text()
start = text.index('**The current receipt.**')
end = text.index('| Generated `injEq` lemmas', start)
para = text[start:end]
edits = [
    (f'is run `{OLD_R}`, frozen in [`becoming-checks/{OLD_R}/`](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/becoming-checks/{OLD_R}/verification.json)',
     f'is run `{NEW_R}`, frozen in [`becoming-checks/{NEW_R}/`](../../../experiments/integrated-correction/general-framework/generative-basis/lean/becoming/becoming-checks/{NEW_R}/verification.json)'),
    ('on main e658aa022 (after N5, the N1 renaming, and the L1 claim) with L1 (`Becoming.Unrolling`, '
     f'[study §173]({STUDY}#173-what-an-extrapolation-given-nothing-fixes-l1)) in the working tree',
     'on main fda157ce8 (after L1, `Becoming.Unrolling`, and the S1 claim) with S1 (`Becoming.Enough`, '
     f'[study §174]({STUDY}#174-the-boundary-of-enough-under-undetermined-laws-s1)) in the working tree'),
    ('| 178 modules, 7,577 theorems |', '| 179 modules, 7,586 theorems |'),
    ('| 181 modules, 7,651 theorems |', '| 182 modules, 7,660 theorems |'),
    ('| Spine (core and bridge) | 8,178 theorems |', '| Spine (core and bridge) | 8,187 theorems |'),
    ('| Audited spine declarations | 11,010 |', '| Audited spine declarations | 11,030 |'),
    ('| Modules in the compile order | 321 |', '| Modules in the compile order | 322 |'),
]
for old, new in edits:
    assert para.count(old) == 1, ('receipt edit does not match once', old[:70])
    para = para.replace(old, new)
text = text[:start] + para + text[end:]
old = 'it counts 177 of 8,178, none in `Becoming.Unrolling`.'
assert text.count(old) == 1
text = text.replace(old, old + f' Rerun with S1 (receipt {NEW_R}), it counts 177 of 8,187, none in `Becoming.Enough`.')
C.write_text(text)
print('applied')
