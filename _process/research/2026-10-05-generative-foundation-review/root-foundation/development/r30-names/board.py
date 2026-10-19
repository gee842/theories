#!/usr/bin/env python3
"""R30's landing on the work board (from the checkout root): an R30 sub-row to the history file after R29's,
the R28-R36 row's state, the receipt line and the queue line. Idempotent."""
from pathlib import Path

RID = '20261019T194851.524223Z'
BOARD = Path('_process/BECOMING-WORKBOARD.md')
HIST = Path('_process/history/workboard/BECOMING-WORKBOARD-2026-10-11_to_2026-10-17.md')
b = BOARD.read_text()
h = HIST.read_text()
if '| **R30: one notion, one name' in h:
    raise SystemExit('already applied')

# A sub-row of R30 on the board, if a session added one, goes to history with the landing.
lines = b.split('\n')
for row in [l for l in lines if l.startswith('| **R30')]:
    lines.remove(row)
b = '\n'.join(lines)

pairs = [
    ("the latest core receipt is R29's `20261019T185632.962707Z` (20 October 2026).",
     "the latest core receipt is R30's `" + RID + "` (20 October 2026)."),
    ("- **Queue:** R30 at the head of the queue (the twentieth review's one rename table), built and checked on its branch; its lander fast-forwards main (rule 5).",
     "- **Queue:** empty; R30 landed (core receipt `" + RID + "`); R31 next."),
    ("left to B11's census table, study §220); R30 next |",
     "left to B11's census table, study §220); "
     "R30 landed (one notion, one name, core receipt `" + RID + "`, study §221, sub-row in the history file; the 28 `Unfolding` sites left for R34); R31 next |"),
]
for a, c in pairs:
    assert b.count(a) == 1, a[:60]
    b = b.replace(a, c)

r30 = ('| **R30: one notion, one name** (twentieth review B2, B3, B6, B13, F1, F3, F8, F9, F12, F14, §2f, A10, G9). '
       'One rename table, regenerated on R29\'s head and applied by resolution: a name is renamed where it states a meaning the statement does not have or collides with another declaration\'s name. '
       '336 declarations (137 renamed, 199 moved with their namespace), 11 namespaces (B13\'s collisions qualified by module, `Ranking.Rest` → `Pause`), 4 modules (`Generation` → `Arising`, `Return` → `Restoration`, `Coupling` → `MoveFormation`, `PositiveGround` → `SecuredContent`), the binder `positive` → `relevance` (53 tokens), the Metaethics header structural. '
       '`G0` → `LivingSignificance`, `g0_*` → `livingSignificance_*`, `SelfGood` → `SelfSignificance`, `SecuresPositiveGround` → `SecuresNewContent`, `DependentSelection` → `DependentChoice`, `Learnable.RestsFrom` → `PredictsFrom`, `Web.Returns` → `Restored`, `Flow.Lossless` → `Conserving`, `Web.generation_*` → `embodiedArising_*`, `Clearing.free_rider_loses` → `clearer_loses_dweller`. '
       'No aliases: `development/r30-names/RENAME-TABLE.json` is the lookup for every old name; the glossary lists the retired names. '
       'Kept by decision: `World.RestsFrom`, `Enough.RestsFrom`/`Rests`/`Settles` (D42, D45(4)), and five borderline groups (`Narrowing.Settles`, `GuardHorizon.Closed`, the witness `Generations`, Slowing\'s event names, `Branching.Keeps`). '
       'Not done: the 28 `Unfolding` sites (Ranking 19, Relevance 5, ActiveReading 4), since a port changes what the statement quantifies over; left for R34. OPENING\'s body and the chain name no renamed declaration. One checker run | '
       'Claude Code session of 20 October (R28–R36 programme) | landed 2026-10-20: core receipt `' + RID + '` on `4cc010fb0`, passed (299 core modules, 11,658 theorems and 15,949 declarations as before; every core axiom report empty; every printed type equal after renaming, sigcheck.py); '
       'connectivity unchanged (489 apart of 11,658, World → Process true, 866 statements on both families), nine register entries keyed by their new names; '
       '244 records renamed, rebound or re-pointed after reading; the RO map rebuilt through build_passages.py and the Y1 map renamed, verify_ro.py and verify_mapping.py pass; study §221; kit `development/r30-names/`; render, check, links and test pass | '
       'worktree `.claude/worktrees/agent-a50723498353f7c52` | the 75 changed core modules, the chapter (en, zh) and glossary, the Lean READMEs, the RO and Y1 maps → R31–R36 (R34 the `Unfolding` sites, R36 the prose words) |')
anchor = [l for l in h.split('\n') if l.startswith('| **R29: compression under rule 9')]
assert len(anchor) == 1
h = h.replace(anchor[0], anchor[0] + '\n' + r30)
BOARD.write_text(b)
HIST.write_text(h)
print('board updated')
