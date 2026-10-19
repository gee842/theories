#!/usr/bin/env python3
"""R25 replayed on R26's landing (main 14c4fa5db): R26 took study section 216, so R25's is 217; S4's scratch
result (twentieth-review/S4-ONE-BASE-FEASIBILITY.md) replaces "being checked" in §8.1 item 1; and the board's
R25 row, queue line and the two proposals pending Ren are applied to R26's board. Edits in place; run once."""
import re, sys
RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation/'
C = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
Z = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md'
B = '_process/BECOMING-WORKBOARD.md'
H = '_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md'
K = RF + 'development/r25-docs-now/repoint_drift.py'
A216 = '216-r25-the-twentieth-reviews-step-1-docs-now'
A217 = '217-r25-the-twentieth-reviews-step-1-docs-now'
files = {}
def get(p):
    if p not in files: files[p] = open(p, encoding='utf-8').read()
    return files[p]
def r(p, old, new, count=1):
    s = get(p); n = s.count(old)
    if n != count: sys.exit(f'{p}: {n} != {count}: {old[:80]}')
    files[p] = s.replace(old, new)

for p in (C, Z):
    s, n = re.subn(r'(§|section )216(\]\([^)]*#)' + A216, r'\g<1>217\g<2>' + A217, get(p))
    assert n == 3, (p, n); files[p] = s
S4 = '../../../_process/research/2026-10-05-generative-foundation-review/root-foundation/twentieth-review/S4-ONE-BASE-FEASIBILITY.md'
r(C, "its feasibility is being checked in scratch (board item S4).",
  "its definitional part was built in scratch: `Web` as `Dependence Nat`, `World` as a history of webs and exchanges and the run as root, with `Law.*` as abbreviations at `Law.process` after five unfolding lemmas, build together with every axiom report empty, and nothing has landed ([S4](" + S4 + ")).")
r(Z, "其可行性正在草稿中检查（工作板 S4 项）。",
  "其定义部分已在草稿中构建：`Web` 作为 `Dependence Nat`、`World` 作为网与交换的历史并以运行为根、`Law.*` 经五条展开引理作为 `Law.process` 上的缩写，合在一起构建，所有公理报告为空，尚未落地（[S4](" + S4 + ")）。")
r(K, "('section 216 added (R25); earlier sections unchanged', '新增第 216 节（R25）；前面各节不变')",
     "('section 217 added (R25); earlier sections unchanged', '新增第 217 节（R25）；前面各节不变')")

# board: the R25 row to the history file (rule 4), the queue line, two proposals pending Ren
b = get(B); lines = b.split('\n')
i = [k for k, l in enumerate(lines) if l.startswith("| **R25: the twentieth review's step 1, docs now**")]
assert len(i) == 1; row = lines.pop(i[0]); files[B] = '\n'.join(lines)
old_state = "| claimed 2026-10-20 on `05ed62b00` | worktree `.claude/worktrees/wizardly-goldstine-4e6de8` (branch `claude/wizardly-goldstine-4e6de8`) |"
assert row.count(old_state) == 1
row = row.replace(old_state, "| landed 2026-10-20 (docs only, no checker run), replayed on R23's and R26's landings: (a)–(e) applied; the old §8 targets and area table moved verbatim to `theories/becoming/history/THE-THEORY-OF-BECOMING-open-programme-2026-10-20.md`, the connectivity log to THEOREM-CONNECTIVITY.md §10; records re-pointed after reading (three with corrected text: `one-axiom-yields-g0`, `own-count-misses-joint-excess`, `reserve-defers-ending`); Becoming.lean's and World.lean's module docs left for the next checker run; K1–K7 and target 1's restatement offered under “Decisions pending Ren” | [study §217](../../research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md#" + A217 + "), kit `development/r25-docs-now/` |")
row = row.replace("](research/", "](../../research/")
hl = get(H).split('\n')
j = [k for k, l in enumerate(hl) if l.startswith("| **R25: the twentieth review's step 1")]
if j:   # the claimed row came in with the replayed patch; replace it with the landed row
    hl[j[0]] = row
else:
    j = [k for k, l in enumerate(hl) if l.startswith("| **R24: twentieth review")]; hl.insert(j[0] + 1, row)
files[H] = '\n'.join(hl)
r(B, "- **Queue:** empty; R26 landed (see the landing queue below).", "- **Queue:** empty; R25 landed after R26 (docs only; see the landing queue below).")
r(B, "R26, Horizon's refutation laws derived from the laws of ideals, landed, core receipt `20261019T172902.786054Z`, its row moved likewise): nothing is queued.",
     "R26, Horizon's refutation laws derived from the laws of ideals, landed, core receipt `20261019T172902.786054Z`, its row moved likewise; R25, the twentieth review's step 1, landed, docs and records with no checker run, its row moved likewise): nothing is queued.")
r(B, "## Decisions pending Ren\n\nNone since 19 October 2026. Ren answered the register as a whole:",
  "## Decisions pending Ren\n\n"
  "Two proposals, from R25 (20 October 2026; [study §217](research/2026-10-05-generative-foundation-review/root-foundation/BECOMING-RENEWAL-READING.md#" + A217 + ")), neither applied:\n"
  "- **Target 1's formal part** (a goal scope). The target asks “that every becoming can be represented as the spine represents worlds”, which no proof settles as worded. Proposed restatement: every central law of the spine stated over every law, or relation, of exchange (`ExchangeLaw`, `ExchangeRelation`), each `World` premise shown to be a reading of the exchange or a state of the law, and the process and world families joined by definition; that the whole's determinations are internally related moments of one unfolding stays the philosophical part. GOALS and the record `theory-of-becoming-foundation` keep the current wording until decided.\n"
  "- **A completion criterion a script can check, K1–K7** (coverage, unity, premises, representation, enclosure, the ethics chain, the open register; twentieth review D1). Adopting it changes this page's target sentence and RESEARCH-DIRECTIVES' four parts; until it runs, the chapter's item 11 claims completeness only in the qualified sense it now states.\n\n"
  "Readings: none since 19 October 2026. Ren answered the register as a whole:")

for p, s in files.items():
    open(p, 'w', encoding='utf-8').write(s)
print('ok', len(files))
