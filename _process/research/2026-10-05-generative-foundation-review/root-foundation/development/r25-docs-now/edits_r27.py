#!/usr/bin/env python3
"""R25 on R27's landing (main 935c0e27c): the measure the changed sentences cite is R27's rerun
(THEOREM-CONNECTIVITY.json at 81f013ca0, core receipt 20261019T174929.247241Z: 495 of 11,676 apart, the same
349 roots in the same six classes), and §8.1 item 2 states what R27 proved (Becoming.Significance: the stepwise
classes meet the order on what can form in one direction). Edits in place; run once after replay.py."""
import sys
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation/'
C = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
Z = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
S = RF + 'BECOMING-RENEWAL-READING.md'
T = RF + 'THEOREM-CONNECTIVITY.md'
E = [
 (C, "on R26's landing tree (20 October 2026), 495 of the 11,670 spine theorems", "on R27's landing tree (20 October 2026), 495 of the 11,676 spine theorems"),
 (C, "finds 495 of the 11,670 spine theorems apart from both base families at the last rerun (on R26's landing tree;", "finds 495 of the 11,676 spine theorems apart from both base families at the last rerun (on R27's landing tree;"),
 (C, "and 495 of the 11,670 spine theorems stand apart from both.", "and 495 of the 11,676 spine theorems stand apart from both."),
 (Z, "脊柱的 11,670 条定理中 495 条与两族都散立", "脊柱的 11,676 条定理中 495 条与两族都散立"),
 (Z, "在 R26 落地树（2026-10-20）上的[定理层面的连通度量]", "在 R27 落地树（2026-10-20）上的[定理层面的连通度量]"),
 (Z, "中，脊柱 11,670 条定理里有 495 条", "中，脊柱 11,676 条定理里有 495 条"),
 (S, "measure (495 of 11,670 apart on R26's landing tree, 349 roots classified);", "measure (495 of 11,676 apart on R27's landing tree, 349 roots classified);"),
 (S, "connectivity figures are THEOREM-CONNECTIVITY.json's (R26's landing tree fb7962bd2, core receipt\n          20261019T172902.786054Z)",
     "connectivity figures are THEOREM-CONNECTIVITY.json's (R27's landing tree 81f013ca0, core receipt\n          20261019T174929.247241Z)"),
 (S, "(the cited\n          modules unchanged at b34ad72b7: R23 added Becoming.ListingRefutations, R26 changed only Horizon,\n          HistoryIdeals and their entries in the root module's documentation)",
     "(the cited\n          declarations unchanged at 935c0e27c: R23 added Becoming.ListingRefutations, R26 changed only Horizon,\n          HistoryIdeals and their entries in the root module's documentation, R27 added six theorems to\n          Significance, whose laws section 8.1 item 2 now cites)"),
 (T, "The [JSON](THEOREM-CONNECTIVITY.json) holds the last run, on R26's landing tree (`fb7962bd2`, core receipt `20261019T172902.786054Z`): 495 of 11,670 spine theorems apart, 349 roots, each classified.",
     "The [JSON](THEOREM-CONNECTIVITY.json) holds the last run, on R27's landing tree (`81f013ca0`, core receipt `20261019T174929.247241Z`): 495 of 11,676 spine theorems apart, 349 roots, each classified."),
 (C, "No theorem joins widening to these, and the one that relates undermining to narrowing is a divergence: a living event whose part narrows what can form (`Preemption.not_undermining_yet_loses`). *Open:* how a part's class over a run relates to its widening,",
     "The stepwise classes meet the order on what can form in one direction only (§6.8, “The stepwise classes and loss”): through dependences that hold across the step at no smaller need, an undermining event leaves the levels exceeded, so a part that keeps what can form does not undermine there (`Web.UnderminingOn.exceeded`, `Web.Includes.not_undermining`); the converse fails, an event within renewal whose part still closes a possibility (`Preemption.within_renewal_yet_loses`). *Open:* how a part's class over a run (consuming, arising) relates to its widening,"),
 (Z, "没有定理把扩大与后者相连，把侵蚀与缩小相连的那一条是一个分歧：一个活的事件，其部分缩小能形成者（`Preemption.not_undermining_yet_loses`）。*开放：*在写明的前提下，一个部分在整段上的类与它的扩大怎样相关，",
     "逐步的类与能形成者之序只在一个方向上相合（§6.8“逐步类别与失去”）：经由跨步持续、所需不减的依存，侵蚀的事件使水平被超出，所以保持能形成者的部分在那里不侵蚀（`Web.UnderminingOn.exceeded`、`Web.Includes.not_undermining`）；反方向不成立，一个在更新之内的事件，其部分仍关闭一个可能（`Preemption.within_renewal_yet_loses`）。*开放：*在写明的前提下，一个部分在整段上的类（消耗、生起）与它的扩大怎样相关，"),
]
fs = {}
for p, o, n in E:
    s = fs.get(p) or open(p, encoding='utf-8').read()
    if s.count(o) != 1: sys.exit(f'{p} {s.count(o)} {o[:70]}')
    fs[p] = s.replace(o, n)
for p, s in fs.items():
    open(p, 'w', encoding='utf-8').write(s)
print('ok')
