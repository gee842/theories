# Handoff: deriving the process law's supplied inputs

7 October 2026. Thread "Ground the remaining process-law obligations". This handoff is written for an agent that has none of this thread's context. Ren asked for the work to stop at a continuable point, be committed on the branch and **not** be merged into `main` by this thread. Your first job is to merge it.

Project rules that apply (from Ren, 6–7 October 2026; see `AGENTS.md` and the team memory):
- No assumptions and no axioms. Every `#print axioms` must be completely empty, including `propext`, `Quot.sound` and `Classical.choice`. No `sorry`, `axiom` or `native_decide`. An input that cannot be derived is either proved necessary in Lean (a countercase where the claim fails without it) or reported to Ren with what was tried and why each attempt failed.
- No market vocabulary in new names or prose. Use `held / enacted / arrived / dissipated / draw` (table: `/mnt/project-files/dependency-map/RENAMES.md`; `main` already applies it to the native port: `bill→draw`, `charge→support`, `fuel→held`, `spent→enacted`, `wasted→dissipated`, `.paid→.sustained`, `.funding→.insufficient`).
- The theory is monist and relational. Do not introduce observer/world, knower/known or inside/outside as independent starting points; derive any split from relations within the one process and state its scope.
- New results go in new modules. Verified sources stay unchanged.

## Branch and merge state

- Branch: `claude/ground-process-law-za6m9z`
- Last commit: see the commit that adds this file (`git log -1 origin/claude/ground-process-law-za6m9z`). Its parent is `b09201fd`, a merge of `origin/main` into the branch.
- Everything earlier from this thread is **already on `main`**: phase cycle, period selection, contact join, recovery rate, formation draw, starting stock (main commits `9bf037f`, `5eab8b2`, `2c2171c4`).
- What the branch adds over `main` is only the last round:
  - `experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/PhasePeriodUniversal.lean` (47 declarations)
  - `.../sufficiency/check_phase_universal.py`, `.../sufficiency/phase-universal-verification.json`, `.../sufficiency/explore_phase_universal.py`
  - `_process/research/2026-10-05-generative-foundation-review/root-foundation/PHASE-PERIOD-ASSUMPTIONS.md`
  - one added line at the top of `RESEARCH.md` and of `experiments/integrated-correction/general-framework/generative-basis/lean/README.md`
  - this handoff and `_process/handoffs/2026-10-07-process-law-build-closure.py`
- Foreseeable conflicts with `main`: only the top lines of `RESEARCH.md` and the lean `README.md`, where every thread adds its line. Keep both sides' lines. `PhasePeriodUniversal.lean` uses no renamed identifiers, so the vocabulary rename does not affect it.

## How to merge and verify

1. Lean 4.29.1. In the cloud container the elan host (`release.lean-lang.org`) is blocked by the proxy; GitHub works:
   ```sh
   mkdir -p /opt/lean && cd /opt/lean
   curl -sSL -o lean.tar.zst https://github.com/leanprover/lean4/releases/download/v4.29.1/lean-4.29.1-linux.tar.zst
   pip install zstandard   # no zstd binary in the image
   python3 -c "import zstandard,tarfile;tarfile.open(fileobj=zstandard.ZstdDecompressor().stream_reader(open('lean.tar.zst','rb')),mode='r|').extractall('.')"
   ```
   The thread's checkers call `lean +leanprover/lean4:v4.29.1 ...` (elan syntax). Without elan, put a shim first on `PATH` that drops the `+...` argument:
   ```sh
   mkdir -p /opt/lean/shim && printf '#!/bin/sh\n[ "${1#+}" != "$1" ] && shift\nexec /opt/lean/lean-4.29.1-linux/bin/lean "$@"\n' > /opt/lean/shim/lean && chmod +x /opt/lean/shim/lean
   ```
2. In a separate worktree at `origin/main`, `git merge origin/claude/ground-process-law-za6m9z` and resolve the index-line conflicts by keeping both.
3. Verify. From `experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/`, with `PATH=/opt/lean/shim:$PATH`, each checker rebuilds its closure from scratch and requires every new audit to be empty:

   | Checker | Expected |
   |---|---|
   | `check_phase_universal.py` | lean passed, 47 of 47 audits empty |
   | `check_stock_derivation.py` | lean passed, 82 of 82 audits empty (14-module closure) |
   | `check_phase_period.py` | lean passed, 43 of 43 audits empty |
   | `check_phase_cycle.py` | lean passed, 52 of 52 audits empty |

   Run them one at a time: two concurrent builds of `PhasePeriodSelection` were killed at 15 GB.
4. Whole-closure audit, from `experiments/integrated-correction/general-framework/generative-basis/lean/`:
   ```sh
   M=$(git rev-parse --show-toplevel)/experiments
   EXTRA=$M/valuation-development/lean:$M/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/feedback/remaining-dependency/formal \
   LEAN=/opt/lean/lean-4.29.1-linux/bin/lean \
   python3 $(git rev-parse --show-toplevel)/_process/handoffs/2026-10-07-process-law-build-closure.py . GenerativeDerivedProcessLawModel $(ls inquiry-root/sufficiency/*.lean | xargs -n1 basename | sed 's/.lean//')
   ```
   It prints `<modules> modules <audits> audits` and a `bad` list. On the branch tip (main merged in) this gave **75 modules, 1591 audits**; the only entries in `bad` were `RemainingDependency` (40 declarations with `propext`) and `InquiryRelevance` (4 with `propext`). Both belong to other threads' packages that the closure imports; every module from this thread was clean.
5. Push to `main` only if the modules from this thread are clean and `origin/main` is still an ancestor of your merge; otherwise fetch, merge again and re-verify. `check_process_law.py` pins Ren's macOS compiler path and hash, so it cannot run in the cloud; the steps above are its equivalent.

## What is proved (all audits empty)

All modules are in `experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/`; each has a study note in `_process/research/2026-10-05-generative-foundation-review/root-foundation/`.

| Module (note) | Result |
|---|---|
| `PhaseCycleDerivation` (PHASE-CYCLE-DERIVATION.md) | The three phases are the orbit of one distinction-retaining advance; retaining advances on finite sets close into cycles, merging ones leave transients. Periods 1, 2, 4 fail the alignment requirements, 3 and 5 meet them. The phase recurs; the whole configuration never does. |
| `PhasePeriodSelection` (PHASE-PERIOD-SELECTION.md) | For periods 3–8, the three-phase pattern has the least guaranteed number of native commands (7) to settle both contact values from an unsettled start, so the least draw. Countercases kept: averaged starts favour period 5; a single value selects nothing; `001001` ties on commands. |
| `FormedContactCycle` | Contact formation is exactly what makes the contact two-valued (`formation_supplies_two_valued_arrival`, `two_valued_arrival_requires_formation`). Phase recovery does not join: readings never depend on `blocked`. |
| `RecoveryQuantum` (RECOVERY-QUANTUM.md) | The recovery rate is the dissipation quantum of one failed conversion: one pair per failure holds exactly at rate 10 (`rate_determined`); rates 11 and 9 fail. |
| `FormationDraw` (FORMATION-DRAW.md) | Under one draw law for the whole extended process, formation and recovery must draw the native `draw` (`one_law_forces_formation_draw`); a free formation splits the process into two laws. This answers the formation-draw item that `2026-10-07-formal-unification.md` still lists as assumed, relative to the one-law claim. |
| `StartingStock` (STARTING-STOCK.md) | Zero spare pairs at the start is forced by backing (`backing_iff_empty_stock`); the closure history's least start is 114702 held and 20 source (`least_starting_stock`); without any held amount nothing proceeds. |
| `PhasePeriodUniversal` (PHASE-PERIOD-ASSUMPTIONS.md) | Reduction lemmas toward the unbounded lower bound: `knows_sub`, `knows_transfer`, and propext-free arithmetic for the advance (`iter_formula`, `add_period_mod`, …). |

## What is open, and the resume point

Ren flagged the four premises of the period selection as unacceptable. None is removed yet. `PHASE-PERIOD-ASSUMPTIONS.md` has the full analysis; in short:

1. **Lower bound only for periods 3–8. Resume here.** Next step is `factor_knows` (a local stretch of 14 contact values is no harder than the whole game), then a finite `decide +kernel` check over 14-value words split into 16 theorems by four-bit prefix (about 1 minute each; watch memory), then the extraction of a deciding stretch from every non-repeating pattern (`n = 3q + r` by induction, no `Nat.div_add_mod`), then the general selection theorem. Python evidence covers periods up to 16 (`explore_phase_universal.py`).
2. **Cell count `1 + 2n` from Python.** Representation-dependent. Plan: prove a storage-independent pigeonhole bound (`⌈log₂ n⌉` binary cells); it is only needed to break the tie with repetitions `001001…`. Necessity already shown by `six_cycle_repetition_ties_in_commands`.
3. **Unsettled start.** Plan: readings depend only on phase and `tau xor sigma`, silent commands change neither, so no conduct separates starts before its first reading; a reset with unsettled fault never helps. What stays: that a beginning carries no observation. Necessity countercase (not yet in Lean): with a settled phase, period 2 beats 3.
4. **Both values required.** Plan: arrival needs value `!tau`, readings never reveal `tau`, so indistinguishable starts contain both values of `tau`. Necessity countercase (not yet in Lean): with `tau` settled, a constant period-1 pattern needs 0 commands.

Other inputs still supplied, by module: why the native conversion moves ten units and why each operation draws `16384 + peak` (inherited from `diagnosis.py`); the claim that one recovered pair matches one recorded failure (RecoveryQuantum's theorem shows it is equivalent to rate 10); "nothing dissipated at the beginning" (StartingStock); the existence of any held amount and source, which belongs to the renewal question.

## Open items for Ren

- The four period-selection premises above. If the plans for 3 and 4 succeed, what remains is one statement, "a beginning carries no observation". Whether that counts as a premise or as the definition of a beginning is Ren's call.
- Other threads' packages that the whole-closure build pulls in (`RemainingDependency`, `InquiryRelevance`) still report `propext`; they are not this thread's modules.
