#!/usr/bin/env python3
"""R25 after rebasing on R23 (main 1705fe0d8): the study section is 216 (R23 took 215), and the measure
the changed sentences cite is R23's rerun (THEOREM-CONNECTIVITY.json at 6436e26b1, core receipt
20261019T170714.008572Z: 495 of 11,675 apart, the same 349 roots in the same six classes). Edits in place. (Run once, on 20 October 2026; the section 8 drafts it also touched were removed
afterwards, their text being the chapter's and the history excerpt's.)"""
import re, sys
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation/'
C = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
Z = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
S = RF + 'BECOMING-RENEWAL-READING.md'
T = RF + 'THEOREM-CONNECTIVITY.md'
K = RF + 'development/r25-docs-now/'
files = {}
def get(p):
    if p not in files: files[p] = open(p, encoding='utf-8').read()
    return files[p]
def r(p, old, new, count=1):
    s = get(p); n = s.count(old)
    if n != count: sys.exit(f'{p}: {n} != {count}: {old[:80]}')
    files[p] = s.replace(old, new)

# section number and anchor
for p in [C, Z]:
    s, n = re.subn(r'(§|section )215(\]\([^)]*#)215-r25-the-twentieth-reviews-step-1-docs-now', r'\g<1>216\g<2>216-r25-the-twentieth-reviews-step-1-docs-now', get(p))
    print(p, n); files[p] = s
r(S, '## 215. R25: the twentieth review', '<a id="216-r25-the-twentieth-reviews-step-1-docs-now"></a>\n## 216. R25: the twentieth review')

# the measure
r(C, "on R22's landing tree (19 October 2026), 495 of the 11,647 spine theorems", "on R23's landing tree (20 October 2026), 495 of the 11,675 spine theorems")
r(C, "finds 495 of the 11,647 spine theorems apart from both base families at the last rerun (on R22's landing tree;", "finds 495 of the 11,675 spine theorems apart from both base families at the last rerun (on R23's landing tree;")
r(C, "and 495 of the 11,647 spine theorems stand apart from both.", "and 495 of the 11,675 spine theorems stand apart from both.")
r(Z, "脊柱的 11,647 条定理中 495 条与两族都散立", "脊柱的 11,675 条定理中 495 条与两族都散立", count=1)
r(S, "measure (495 of 11,647 apart, 349 roots classified);", "measure (495 of 11,675 apart on R23's landing tree, 349 roots classified);")
r(S, "connectivity figures are THEOREM-CONNECTIVITY.json's (commit 05f075f77, receipt\n          20261019T164609.214116Z); no Lean changed, no checker run needed",
     "connectivity figures are THEOREM-CONNECTIVITY.json's (R23's landing tree 6436e26b1, core receipt\n          20261019T170714.008572Z); no Lean changed, no checker run needed")
r(S, "was read in the source at 1c6569436", "was read in the source at 1c6569436 (the cited\n          modules unchanged at 1705fe0d8, where R23 added only Becoming.ListingRefutations)")
r(T, "The [JSON](THEOREM-CONNECTIVITY.json) holds the last run, on R22's landing tree (`05f075f77`, core receipt `20261019T164609.214116Z`): 495 of 11,647 spine theorems apart, 349 roots, each classified.",
     "The [JSON](THEOREM-CONNECTIVITY.json) holds the last run, on R23's landing tree (`6436e26b1`, core receipt `20261019T170714.008572Z`): 495 of 11,675 spine theorems apart, 349 roots, each classified.")
# zh chapter: what this completeness is, item 11
for p in (C, Z, S, T):
    if '11,647' in get(p) and p != T and p != S: print('left 11,647 in', p)

for p, s in files.items():
    open(p, 'w', encoding='utf-8').write(s)
