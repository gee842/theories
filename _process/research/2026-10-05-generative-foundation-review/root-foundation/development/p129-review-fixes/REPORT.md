# P129 复核所见的脊柱整理 / Spine fixes from the release review — report

2026-10-16. Branch `p129-review-fixes`: phase 1 `57f0041cd` (rebased onto `main` `1c5def5fd`) and phase 2 `a83bf5501`, landed through `land-p129`.

This is AI work (Opus 5.5), not Ren's words. The P129 subagent wrote it, and the lead saved it, because the harness kept the subagent from writing report files.

The fixes come from the [release-readiness review](../../BECOMING-RELEASE-READINESS-REVIEW.md) §1–§4 and the [eighteenth review](../../BECOMING-EIGHTEENTH-REVIEW.md), fix list items L1–L18, S41 and S43. No existing name or statement changed.

## 1. Re-definitions

- **`Parting.after`** is now the abbreviation `r.onward k`, with `Parting.after_eq_onward` (`rfl`). Parting already imports Branching, so the import graph is unchanged.
- **`Courses.anyChange`** is now `Parting.free S`, with `Courses.anyChange_eq_free` (`rfl`).
  - Courses now imports Parting, which adds 3 modules to its closure. The reverse direction would have added 13 modules to Parting's and Onward's closures.
  - Courses has no core dependants, and its role is to read the laws on the shared base, so it is the side that should depend on Parting. The graph stays acyclic.
- **`CrossSituational.Distinct`** is universe-polymorphic (`Type v`), while `Becoming.Distinct` lives in `Type`. Re-pointing it would therefore be a type change. Instead, the bridge `CrossSituational.distinct_iff` is placed in Courses, the only core module that imports both.

## 2. Homonyms (no renames)

| Name | Relation | Action |
|---|---|---|
| `Law.Returns` / `Branching.Returns` | One notion | Linked by `law_returns_iff`; docstrings name each other |
| `Web.Returns` / Frequency's `Becoming.Returns` | Different notions | Docstrings on all four |
| `Recurs` (Change / Horizon) | One notion | New `Sequences.recurs_iff`, in Dissipation |
| `RunsDown` (Flow / OneStep) | One notion | Already linked (`Flow.Realizes.runsDown`, `OneStep.runsDown_iff`); docstrings |
| `Registers` (Likeness / `Web.Registers`) | Different notions | Docstrings |
| `Alike` (Unfolding, a bisimulation / ReferencePlan) | Different notions | Docstrings, plus `ReferencePlan.alike_iff_agreeOn` (`Iff.rfl`) |
| `Ranking.Course` | An index of two alternative unfoldings, not a trace | Docstring |

**Proposed renames for Ren** (not applied):
- `Web.Returns` → `Web.MetAgain`
- Frequency's `Returns` → `ReturnsAround`
- Likeness `Registers` → `RespectsClaims`
- `ReferencePlan.Alike` → `AgreeAt`
- `Ranking.Course` / `course` → `Presence` / `unfoldingOf`
- retire `Parting.after` and `Courses.anyChange` in favour of the definitions they now abbreviate.

## 3. Credits and exact strengths (docstrings)

Credits added:
- Gold 1967; Putnam 1963/1965; Kelly 1996 (Learning, Identification, Learnable, Parting).
- Bishop 1967, Bridges–Richman 1987 and Ishihara (Sensitivity, Tail, Change, Frequency); Akama–Berardi–Hayashi–Kohlenbach 2004 (Tail; `RecursOrStops` is Σ⁰₂ excluded middle, strictly stronger than LPO).
- Gaussian elimination over GF(2) and the Fredholm alternative; Abramsky–Barbosa–Kishida–Lal–Mansfield 2015; Abramsky–Brandenburger 2011; Arkhipov 2012; Kochen–Specker 1967; Mermin and Peres 1990 (Gluing, Context, Quantum).
- Bienaymé, Chebyshev, Bernoulli, Chernoff (Typicality, Situations).
- Neumann series and walk sums; nilpotent ⇔ acyclic; the Dyson series (Loops, Remainder, Routes).
- König 1927 and dependent choice (Bernays 1942) (Onward); weak König ⇔ LLPO (Ishihara 1990) (Lasting, Likeness).
- Alpern–Schneider 1985 (Horizon); Goguen–Meseguer 1982 (Observation); May 1952 (Selection); Moore 1956 (Parting).
- For Recurrence: an injective self-map of a finite set is a permutation.

Strengths corrected:
- The least registration holds up to `¬¬`.
- The tail result is relative to the hypothesis `decides`; "exactly" means a rule (`Nonempty (∀ s, Decidable …)`).
- `rests_unrefuted_*` gives `¬¬∃N`.
- `change_readings` is three readings that hold by definition.
- Horizon: not refutable, and never-occurring is not verifiable.
- Gated: "where", not "exactly where".
- Observation: lies within the downstream, in one direction only.
- Propagation: `carrying` takes nothing, so the bound is attained over all laws, not over gainless ones.
- Loops and Frequency: strengths are natural numbers, and the doubling fails below one.

## 4. New declarations

```lean
theorem Becoming.Parting.after_eq_onward (r : Run P) (k : Nat) : after r k = r.onward k := rfl
theorem Becoming.Courses.anyChange_eq_free (S : Type u) : anyChange S = Parting.free S := rfl
theorem Becoming.CrossSituational.distinct_iff {M : Type} :
    ∀ l : List M, CrossSituational.Distinct l ↔ Becoming.Distinct l
theorem Becoming.Sequences.recurs_iff (r : Run (Becoming.Sequences.process Bool)) :
    Becoming.Sequences.Recurs r ↔ Becoming.Recurs [()] (fun _ m => r.act m = true)
theorem Becoming.ReferencePlan.alike_iff_agreeOn (plan : List Nat) (x y : Nat → Bool) :
    Alike plan x y ↔ Learning.Training.AgreeOn (fun i => i ∈ plan) x y := Iff.rfl
```

**`Becoming/Likeness.lean`**, where LLPO is defined in its standard form beside `EitherThroughout`:
- `Becoming.LLPO`, `Becoming.LLPOForDecided`
- `eitherNever_iff_llpoForDecided`
- `eitherThroughout_iff_llpoForDecided` (R18 item 41, in the decided-family form)
- `LLPO.of_eitherThroughout`, `LLPO.of_forDecided`, `LLPO.of_lpo`, `LLPO.decidable`
- helpers in `LLPO.*`: local `succ_ne_zero` and `succ_inj` (the prelude's `Nat.succ_ne_zero` depends on `propext`), `FirstAt`, `Interleave`.

Going from LLPO over Bool to the family form needs the decisions as data. Turning a Prop-valued `Decided` into a Bool would need unique choice, which the core does not have.

**`Becoming/Horizon.lean`** (R18 item 43):
- `Adheres.closed`
- `refutable_adheres_iff`: refutable exactly where its closure is witnessed.
- `refutable_adheres_of_em`.

A version with no premise is not provable: it would turn `¬∀` into `¬¬∃¬`. Accordingly, `Refutable.adheres_least` is now titled "Refutable supersets hold where the subset is adhered to".

R18 item 42 was skipped.

## 5. Builds

- **Phase 1.** `scratch_build.py` over 120 modules: exit 0, no warnings. The 119 spine modules have 6,784 theorems and 9,217 declarations, with every axiom report empty.
- **Phase 2.** 99 targets: exit 0. They have 5,850 theorems and 7,837 declarations, with every report empty except the periphery module `FallibleInquiry`, which by design uses `propext`/`Quot.sound` and whose bytes are unchanged.
- The landing receipt comes from the integrator's `check_becoming.py` run on `land-p129`.

## 6. `learning-by-refutation`

The review's finding that the record lists no declarations is inaccurate: its `references` bind 84 names, and all of them resolve. What it lacks:
- per-law `laws[].declarations`, as the subagent proposed, in six groups: no record fixes the next value; diagonal; learning by refutation; lassos; induction in a listed world; meta level;
- the two instances `Learning.decRefuted` and `Learning.decRefutedAt`.

These are for the record pass.

## 7. Study section draft (§164)

**中文.** 发布准备度审查与第十八次复核发现了几类问题，这里一并处理，不加新律，不改已有名称与陈述：
- 三处重复定义：两处改为缩写，相等由 `rfl` 给出；`CrossSituational.Distinct` 的宇宙更一般，只给桥接。
- 同名异义：同一概念者给出连接（`recurs_iff`、`alike_iff_agreeOn` 及既有连接）；不同者在说明中写出另一义。改名建议交 Ren。
- 未署名的经典来源：已署名。
- 说明比 Lean 说得强：改到与 Lean 一致。
- 新证：LLPO（标准形式）与 `EitherThroughout ⇔ LLPOForDecided`；“依守可被否证”恰当其闭包有见证。
- 作者反审：没有新数学，价值在一个概念只有一个定义、说明不超出定理；文献年份由 AI 依通常引用给出，发布前宜人工核对。

**English.** This section covers the spine fixes from the release review and the eighteenth review. No new law is added, and no existing name or statement changes.
- **Re-definitions.** Two of the three re-definitions are now abbreviations, each equal by `rfl`. `CrossSituational.Distinct` lives in a more general universe and is bridged instead.
- **Homonyms.** Notions that are one are linked; the others are annotated. Renames are proposed to Ren.
- **Credits and strengths.** Classical sources are credited, and every docstring now matches the strength its theorem proves.
- **New results.** LLPO in its standard form, with `EitherThroughout ⇔ LLPOForDecided`; adhering is refutable exactly where its closure is witnessed.
- **Author's counter-review.** There is no new mathematics here. The value is one definition per notion and no docstring saying more than its theorem. The literature years come from the usual citations and should be checked by hand before release.
