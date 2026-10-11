# P64–P68 landing package: the comparison with a general cause–effect system

Ren's go, 12 October 2026: "Great, let's finish all of them, you can spawn sub agents in a wise order if needed"
([source](../../../../../../sources/15-codex-theory-conversations/2026-10-12-cause-effect-comparison.md);
[directive register](../../../../../RESEARCH-DIRECTIVES.md)). Claimed on the
[work board](../../../../../BECOMING-WORKBOARD.md) as P64–P68 by the session "Cause–effect system theory comparison".
The five proposals are the AI's; every reading is marked the AI's, pending Ren.

| Item | Module | Layer | Imports | Record |
|---|---|---|---|---|
| P64 selection through registration | `Becoming.Selection` | L4 | `Testing`, `Capture` (P62) | selection-through-registration (F04) |
| P65 the comparison where the rest responds | `Becoming.Response` | L4 | `Testing` | comparison-where-the-rest-responds (F07) |
| P66 a projection carrying a law; P68 standard causal models | `Becoming.Mechanism` | L3 | `Experiment` | projection-carrying-a-law, causal-models-as-processes (F11) |
| P67 attraction | `Becoming.Attraction` | L3 | `Recurrence` | attraction-is-not-returning (F01) |

No module changes an existing one. Selection imports P62's `Becoming.Capture`, so this package lands after P62.

## Verified in scratch

Against main at 7d8aa838 (core 49 modules, from the shared cache) with P62's `Seeking` and `Capture` from branch
`p62-seeking` (9af94211): all six modules compile with no error or warning; every constant each new module declares
has an empty axiom report (Attraction 83, Mechanism 64, Response 141, Selection 136 constants; Capture 22, Seeking 29);
no `sorry`, `axiom`, `Classical` or `native_decide`. A file importing the root `Becoming` together with all six
modules compiles, so no name clashes. The consolidated checker has not been run on them; that is the landing run.

## Contents

- `lean/Becoming/{Attraction,Mechanism,Response,Selection}.lean`: the modules, to copy into
  `experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming/`.
- `docs/study/p6x_{zh,en}.md`: the four study sections (P66 and P68 share one) and their English summary entries,
  with placeholders.
- `docs/chapter.py`: the chapter edits (sections 1, 2 and 3, Part I stated whole, section 8, the spine table and
  the glossary).
- `docs/plan_rows.md`: the unification plan's four rows and bullets.
- `docs/records/*.json`: the reviewed text of the five new records; `docs/advances.json`: the next_delta and history
  of the six records these results advance (feedback-and-reach, comparison-within-reach, closing-needs-net-draw,
  testing-within-registration, experiment-needs-return, runaway-distance-unregistered), each with the next_delta it
  was written against.
- `apply_docs.py`, `make_records.py`, `repoint.py` (P53's, skipping the five new records).

## Landing steps

1. Copy the four modules. Add to `Becoming.lean` (root) and to `CORE` in `check_becoming.py`, with the edits below.
2. Run the consolidated checker once (with P62's modules if they land in the same run).
3. `python3 -B apply_docs.py ROOT S PLAN_ZH_AFTER PLAN_EN_AFTER`: `S` is the first of four consecutive study
   sections (P64, P65, P66+P68, P67 in that order); the plan prefixes are those of the row and bullet these go
   after (on 7d8aa838: `'| Tower 时间之塔'` and `'- **Tower:**'`).
4. `python3 -B make_records.py ROOT REVIEWED_AT_UTC S` (`REVIEWED_AT_UTC` as `2026-10-12T12:00:00+00:00`), then
   `python3 -B repoint.py ROOT BASE`.
5. Update the chapter's section 9 totals and the Lean README with the receipt's counts; `make research-render`,
   `make research-check`.

The package was dry-run on a copy of 7d8aa838 with P62's modules and a stand-in receipt (theorem counts by the
checker's parser: Attraction 47, Mechanism 31, Response 30, Selection 43), with P62's `target-capture` written by its
own script: every anchor matched once; the records script wrote the five records, advanced the six and, rerun, did
not repeat a history entry; after `repoint.py`, `make research-render` and `make research-check` passed with no error
and no drift; the 51 links in the inserted text resolve, anchors included.

## Root module, checker and Lean README

`Becoming.lean`: add `import Becoming.Mechanism` and `import Becoming.Attraction` after `import Becoming.Experiment`,
and `import Becoming.Response` and `import Becoming.Selection` after `import Becoming.Runaway` (Selection after
P62's `import Becoming.Capture`). Docstring bullets, after Experiment's and after Runaway's:

```text
* `Becoming.Mechanism` (L3): a projection of configuration carries a determined law exactly
  where configurations alike under it go alike, the image of the step being the least
  candidate; what the step does not depend on is re-absorbed in one step; a system changing its
  own rule is one determined process on the joint configuration, and the state has a law of its
  own exactly where the rule makes no difference to it; a law through a projection is not fixed
  where not yet taken. The standard causal model x′ = F(x, u, ε) is a determined process whose
  move is the input and the noise: an intervention is a move not taken, noise a move not
  represented.
* `Becoming.Attraction` (L3): for every determined law, with no premise, a configuration is
  drawn into an absorbing region exactly where it does not return, and what is drawn in never
  comes back; what can be had n steps on is absorbing and every lost possibility is drawn into
  it; of two merged configurations not both return; within finitely many configurations
  attraction is merging and what returns draws in everything else, while an open world
  separates them; under a process, entering an invariant region locks in.
* `Becoming.Response` (L4): where the rest responds through its registration, a supplied
  premise, the comparison is decided within the part's responsive reach, its closure under
  affecting what is registered: the dual of the registration closure, and, registering support
  only, the union of the members' reach closures. Beyond it every formation registers and
  exchanges alike.
* `Becoming.Selection` (L4): two histories are selected alike by every selection through a
  selector's registration exactly when it registers them alike; with the rest fixed, selection
  is blind beyond the registration closure, so an ending within a candidate's reach closure and
  beyond the selector's registration closure is not selected, while pooled registration selects
  it; where reaching beyond raises what registers, selection favours it.
```

`check_becoming.py`: add `"Becoming.Mechanism", "Becoming.Attraction"` after `"Becoming.Experiment"` and
`"Becoming.Response", "Becoming.Selection"` after `"Becoming.Runaway"` in `CORE`. Scope sentences, after the
Experiment and Runaway ones:

```text
"Mechanism: a projection of configuration carries a determined law exactly where configurations "
"alike under it go alike under it, the image of the step being the least process the step factors "
"through; what the step does not depend on is re-absorbed in one step, and with the configuration "
"read as a state and a rule, re-forming the state alone is re-absorbed where the rule holds the "
"outcome; a system changing its own rule is one determined process on the joint configuration, the "
"state having a law of its own exactly where the rule makes no difference to it; a law through a "
"projection is not fixed where not yet taken; the standard model x' = F(x, u, e) is a determined "
"process whose move is the input and the noise, an intervention is a move not taken and noise a "
"move not represented, the model with the noise forgotten being determined exactly where the noise "
"makes no difference. "
"Attraction: for every determined law, with no premise, a configuration is drawn into an absorbing "
"region exactly where it does not return, and what is drawn in never comes back; what can be had n "
"steps on is absorbing and every possibility lost by step n is drawn into it; of two merged "
"configurations not both return; within finitely many configurations attraction is merging and "
"what returns draws in everything else, while counting on draws without merging; under any "
"process, once inside an invariant region what lies outside cannot be had again, and leaving a "
"region needs a move that does not keep it. "
"Response: where every formation outside a part exchanges alike across each step up to which it "
"has registered alike, a supplied premise of which the rest held fixed is a case, every formation "
"beyond the part's responsive reach, its closure under affecting what is registered, registers and "
"exchanges alike, the difference between two flows reaches none of them and the comparison is "
"decided within the reach; registering support only, with one flow, the responsive reach is the "
"union of the members' reach closures; in the trophic cascade it is the wolves, the deer and the "
"forest, and in a two-party loop the difference returns to the part's own support. "
"Selection: two histories are selected alike by every selection through a selector's registration "
"exactly when the selector registers them alike, and likewise for pooled registration; with the "
"rest fixed, selection and scoring are blind beyond the registration closure; the clearer's "
"selection misses the dweller's ending, which the dweller's and the pooled registration select; a "
"flow reaching beyond the registration closure to raise a gauged store is selected, alike with "
"raising it without reaching beyond; selection supplying the carriers, their share rises among "
"descendants. "
```

Lean README: rows after Experiment (`Mechanism`, `Attraction`) and after Runaway (`Response`, `Selection`) use the
chapter's spine-table descriptions in `docs/chapter.py` (`SPINE_L3`, `SPINE_L4`) with an English half from the
docstring bullets above; the import sentences gain "`Mechanism` 导入 `Experiment`；`Attraction` 导入 `Recurrence`"
(L3) and "`Response` 导入 `Testing`；`Selection` 导入 `Testing` 与 `Capture`" (L4), and the English likewise.

## For the integrator to decide

- `Law.rule_reabsorbs` (Mechanism) and P62's `Law.reform_reabsorbed` (Capture) have the same statement. A one-line
  proof of Capture's from Mechanism's compiles (`Law.rule_reabsorbs byRule x x' g`), but that needs Capture to import
  Mechanism; keep both, or make Capture's an instance after both land.
- General facts that could move down: `Web.RegistersAlike.trans`, `Web.RegistersAlikeUpTo.trans` and
  `Web.RegistersAlikeAll.refl/symm/trans` (Selection) to `Becoming.Testing`; `WithinClosure.converse` and
  `Flow.withinReach_iff_withinInfluence` (Response) to `Becoming.Feedback`.
- The work board's P66 row title said "a level of description"; the package says "projection" or "description"
  throughout, never level.
