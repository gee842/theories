import Becoming.LearnableRuns
import KnowledgeCorrespondence

/-!
# Exact readings of a run's prefix through a map

`KnowledgeCorrespondence` states, for histories, an evidence projection and a two-valued target,
when a reading of the evidence answers the target soundly (never wrongly) or exactly (always
rightly) on a domain of histories, and when the evidence resolves the target (histories with one
evidence have one target). Here the histories are the runs of a process, the evidence at step `t`
is the prefix before `t` of the run's course through a map `reg` (`recordBefore`), and the
target is a two-valued feature `val` of the run's configuration at `t` (`valueAt`). A reading of
the prefix is then an extrapolation at one step: for a determined law, an extrapolation proposes
the feature's value along every run from `T` on exactly where it reads the prefix exactly at
every step from `T` on (`exact_iff_restsFrom`, through `LearnableRuns.RestsFrom`). This module
states the periphery's general laws of these readings of runs and proves them through those laws.

* **Exact is sound** (`exact_sound`), and **an exact reading needs resolution**: runs of the
  domain with one prefix before `t` have one value at `t` (`exact_resolves`).
* **A sound reading abstains where the prefix leaves the value open**: where two runs of the
  domain have one prefix before `t` and different values at `t`, a sound reading gives nothing on
  that prefix (`sound_abstains`).
* **Soundness holds on every smaller domain of runs** (`sound_within`), and **resolution survives
  reading through a second map beside the first** (`finer_resolves`).
* **A faithfully kept prefix keeps exactness** (`kept_exact`): reading the prefix through what a
  retention keeps is exact where the retention is read back faithfully on the domain.
* **Abstaining is sound and, on a domain holding a run, not exact** (`abstaining_sound`,
  `abstaining_not_exact`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

universe u v w

namespace ExactRecordRuns

open KnowledgeCorrespondence

section AnyProcess

variable {S : Type u} {A : Type v} {R : Type w} {P : Process S A}

/-- The prefix before step `t` of a run's course through the map `reg`, latest first. -/
def recordBefore (reg : S → R) (t : Nat) (r : Run P) : List R :=
  Learning.prefixOf (Parting.course reg r) t

/-- The two-valued reading `val` of a run's configuration at step `t`. -/
def valueAt (val : S → Bool) (t : Nat) (r : Run P) : Bool := val (r.state t)

/-- **A reading of the prefix exact on a domain of runs is sound there.** -/
theorem exact_sound {D : Run P → Prop} {reg : S → R} {val : S → Bool} {t : Nat}
    {answer : List R → Option Bool} (exact : ExactOn D (recordBefore reg t) (valueAt val t) answer) :
    SoundOn D (recordBefore reg t) (valueAt val t) answer :=
  exact_is_sound exact

/-- **An exact reading of the prefix needs resolution**: runs of the domain with one prefix before
`t` have one value at `t`. -/
theorem exact_resolves {D : Run P → Prop} {reg : S → R} {val : S → Bool} {t : Nat}
    {answer : List R → Option Bool} (exact : ExactOn D (recordBefore reg t) (valueAt val t) answer) :
    Resolves D (recordBefore reg t) (valueAt val t) :=
  exact_requires_resolution exact

/-- **A sound reading abstains where the prefix leaves the value open**: where two runs of the
domain have one prefix before `t` and different values at `t`, a sound reading gives nothing on
that prefix. -/
theorem sound_abstains {D : Run P → Prop} {reg : S → R} {val : S → Bool} {t : Nat}
    {answer : List R → Option Bool} (sound : SoundOn D (recordBefore reg t) (valueAt val t) answer)
    {r r' : Run P} (hr : D r) (hr' : D r') (same : recordBefore reg t r = recordBefore reg t r')
    (different : val (r.state t) ≠ val (r'.state t)) : answer (recordBefore reg t r) = none :=
  conflicting_fibre_forces_abstention sound hr hr' same different

/-- **Soundness on a domain of runs holds on every smaller one.** -/
theorem sound_within {D D' : Run P → Prop} {reg : S → R} {val : S → Bool} {t : Nat}
    {answer : List R → Option Bool} (sound : SoundOn D (recordBefore reg t) (valueAt val t) answer)
    (within : ∀ r, D' r → D r) : SoundOn D' (recordBefore reg t) (valueAt val t) answer :=
  sound_restricts_domain sound within

/-- **Resolution survives reading through a second map beside the first.** -/
theorem finer_resolves {R' : Type} {D : Run P → Prop} {reg : S → R} {val : S → Bool} {t : Nat}
    (resolves : Resolves D (recordBefore reg t) (valueAt val t)) (reg' : S → R') :
    Resolves D (fun r => (recordBefore reg t r, recordBefore reg' t r)) (valueAt val t) :=
  refinement_preserves_resolution resolves (recordBefore reg' t)

/-- **A faithfully kept prefix keeps exactness**: reading the prefix through what a retention
keeps is exact where the retention is read back faithfully on the prefixes of the domain. -/
theorem kept_exact {M : Type} {D : Run P → Prop} {reg : S → R} {val : S → Bool} {t : Nat}
    {answer : List R → Option Bool} (exact : ExactOn D (recordBefore reg t) (valueAt val t) answer)
    (retain : List R → M) (read : M → List R)
    (faithful : ∀ r, D r → read (retain (recordBefore reg t r)) = recordBefore reg t r) :
    ExactOn D (fun r => retain (recordBefore reg t r)) (valueAt val t) (fun m => answer (read m)) :=
  preserved_record_preserves_exactness exact retain read faithful

/-- **Abstaining from every prefix is sound** on every domain of runs. -/
theorem abstaining_sound (D : Run P → Prop) (reg : S → R) (val : S → Bool) (t : Nat) :
    SoundOn D (recordBefore reg t) (valueAt val t) (fun _ => none) :=
  abstention_sound D (recordBefore reg t) (valueAt val t)

/-- **Abstaining is not exact on a domain holding a run.** -/
theorem abstaining_not_exact {D : Run P → Prop} (reg : S → R) (val : S → Bool) (t : Nat)
    {r : Run P} (hr : D r) : ¬ ExactOn D (recordBefore reg t) (valueAt val t) (fun _ => none) :=
  abstention_not_exact (recordBefore reg t) (valueAt val t) hr

end AnyProcess

section Law

variable {S : Type u} {R : Type w} {next : S → S}

/-- **An extrapolation proposes the feature's value along every run of a determined law from `T`
on exactly where, at every step from `T` on, it reads the prefix exactly on all runs.** -/
theorem exact_iff_restsFrom {reg : S → R} {val : S → Bool} {pred : List R → Option Bool} {T : Nat} :
    (∀ t, T ≤ t → ExactOn (fun _ : Run (Law.process next) => True) (recordBefore reg t)
        (valueAt val t) pred) ↔
      ∀ r : Run (Law.process next), LearnableRuns.RestsFrom reg val pred r T :=
  ⟨fun exact r t late => exact t late r trivial, fun rests t late r _ => rests r t late⟩

end Law

end ExactRecordRuns

end Becoming
