import Becoming.Unfolding

/-!
# A law through a projection along one run, and exactness

`Becoming.Mechanism` characterized when a projection carries a law over every configuration
(`carries_law_iff`: configurations alike go alike). Chapter §8.2 left open a constructive criterion
along one run, and the bridge to `GenerativeCore`'s exact projection of finite paths
(`Generative.projection_exact_iff`). This module states both. Ren, 18 October 2026: "please see
what else is there to do - keep pushing the frontier till finishing". No premise enters beyond
what each theorem names.

* **Along one run.** A run's steps before `t`, read through `π`, are consistent when any two of
  them from configurations alike under `π`, by the same move, reach configurations alike under `π`
  (`Run.ConsistentThrough`). Some determined process on the description admits the run's steps
  before `t` read through `π` exactly where they are consistent (`Run.law_through_iff`), with no
  premise: the witness is the record itself read through `π` (`Run.recordThrough`), which is the
  least process admitting those steps (`Run.record_least`) and is determined exactly where they
  are consistent (`Run.record_determined_iff`). Consistency up to a step holds at every earlier
  step, so once a law through `π` fails along a run it fails from then on
  (`Run.ConsistentThrough.earlier`, `Run.no_law_later`). `Becoming.Unfolding` stated the case
  through the identity over the whole history (`Consistent`, `exists_law_iff`); it is the
  instance of this criterion at every step (`Run.consistent_id_iff`).
* **One run shows less than the process.** Where configurations alike go alike, every run is
  consistent at every step (`Run.consistent_of_goAlike`). The converse fails: in `Constant`, a run
  that stays at one configuration of a process allowing every step is consistent through the
  identity at every step, and the process does not go alike (`Constant.consistent`,
  `Constant.not_goAlike`). `Switching.no_state_law` follows from the criterion: its run's first two
  steps, read through the state, are inconsistent (`Switching.inconsistent`).
* **Exactness.** The image of a process through `π` represents every finite path exactly, in the
  sense of `Generative.projection_exact_iff`, exactly where configurations alike under `π` match
  each other's steps up to `π` (`MatchesThrough`, `image_exact_iff`). Some determined process on
  the description both admits every step read through `π` and represents every finite path
  exactly where configurations alike go alike and match each other's steps (`exact_law_iff`).
  Going alike does not give exactness: in `Stuck` one configuration has a step and the other none,
  and through the description that tells them apart from nothing, they go alike and do not match
  (`Stuck.goAlike_not_matches`). `Coarse` is exact through its first bit (`Coarse.matching`, `Coarse.exact_law`).

**Reading (the AI's).** A run is evidence of a law at a description exactly as far as its own
steps agree with each other: the record is the least candidate, and it is a law exactly where no
two recorded occasions alike under the description went apart. What the run never visits it does
not test, so a run can show a law where the process has none. A law at a description is also not
yet a faithful model of finite paths: that needs every configuration of a class to be able to do
what any of them did. Going alike and matching are the two halves of a mechanism stated exactly at
a description.

What is not derived: which projection an actual unfolding carries a law through; that any
formation forms or uses one; the instance with `Becoming.Testing`'s couplings
(`Web.AlikeThroughUpTo`) as the projection. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

universe u v w

variable {S : Type u} {A : Type v} {K : Type w}

namespace Run

variable {P : Process S A}

/-- The run's steps before `t`, read through `π`, are consistent: two of them from
configurations alike under `π`, by the same move, reach configurations alike under `π`. -/
def ConsistentThrough (r : Run P) (π : S → K) (t : Nat) : Prop :=
  ∀ n m, n < t → m < t → π (r.state n) = π (r.state m) → r.act n = r.act m →
    π (r.state (n + 1)) = π (r.state (m + 1))

/-- The record read through `π` before `t`: a move goes from `k` to `κ` where the run took it,
before `t`, from a configuration projecting to `k` to one projecting to `κ`. -/
def recordThrough (r : Run P) (π : S → K) (t : Nat) : Process K A :=
  ⟨fun k a κ => ∃ n, n < t ∧ π (r.state n) = k ∧ r.act n = a ∧ π (r.state (n + 1)) = κ⟩

/-- The record admits the run's steps before `t` read through `π`. -/
theorem stepsThrough_record (r : Run P) (π : S → K) (t : Nat) :
    r.StepsThrough π (r.recordThrough π t) t :=
  fun n before => ⟨n, before, rfl, rfl, rfl⟩

/-- **The record is the least candidate.** Every process admitting the run's steps before `t`
read through `π` admits every step of the record. -/
theorem record_least (r : Run P) {π : S → K} {Q : Process K A} {t : Nat}
    (steps : r.StepsThrough π Q t) {k : K} {a : A} {κ : K} :
    (r.recordThrough π t).step k a κ → Q.step k a κ
  | ⟨n, before, at_k, by_a, to⟩ =>
    Eq.subst (motive := fun x => Q.step k a x) to
      (Eq.subst (motive := fun b => Q.step k b (π (r.state (n + 1)))) by_a
        (Eq.subst (motive := fun x => Q.step x (r.act n) (π (r.state (n + 1)))) at_k
          (steps n before)))

/-- The record is determined exactly where the run's steps so read are consistent. -/
theorem record_determined_iff (r : Run P) (π : S → K) (t : Nat) :
    Determined (r.recordThrough π t) ↔ r.ConsistentThrough π t :=
  ⟨fun determined n m before before' same same' =>
     determined (π (r.state n)) (r.act n) _ _ ⟨n, before, rfl, rfl, rfl⟩
       ⟨m, before', same.symm, same'.symm, rfl⟩,
   fun consistent _ _ _ _ ⟨n, before, at_k, by_a, to⟩ ⟨m, before', at_k', by_a', to'⟩ =>
     to.symm.trans ((consistent n m before before' (at_k.trans at_k'.symm)
       (by_a.trans by_a'.symm)).trans to')⟩

/-- **A law through a projection along one run.** Some determined process on the description
admits the run's steps before `t` read through `π` exactly where those steps are consistent. No
premise: the witness is the record. -/
theorem law_through_iff (r : Run P) (π : S → K) (t : Nat) :
    (∃ Q : Process K A, Determined Q ∧ r.StepsThrough π Q t) ↔ r.ConsistentThrough π t :=
  ⟨fun ⟨Q, determined, steps⟩ n m before before' same same' =>
     determined _ _ _ _ (steps n before)
       (Eq.subst (motive := fun k => Q.step k (r.act n) (π (r.state (m + 1)))) same.symm
         (Eq.subst (motive := fun b => Q.step (π (r.state m)) b (π (r.state (m + 1))))
           same'.symm (steps m before'))),
   fun consistent =>
     ⟨r.recordThrough π t, (r.record_determined_iff π t).mpr consistent, r.stepsThrough_record π t⟩⟩

/-- Consistency up to a step holds at every earlier step. -/
theorem ConsistentThrough.earlier {r : Run P} {π : S → K} {t t' : Nat}
    (consistent : r.ConsistentThrough π t') (le : t ≤ t') : r.ConsistentThrough π t :=
  fun n m before before' => consistent n m (Nat.lt_of_lt_of_le before le)
    (Nat.lt_of_lt_of_le before' le)

/-- **Once failed, failed from then on.** Where no determined process on the description admits
the run's steps before `t` read through `π`, none admits them before any later step. -/
theorem no_law_later (r : Run P) {π : S → K} {t t' : Nat} (le : t ≤ t')
    (none : ¬ ∃ Q : Process K A, Determined Q ∧ r.StepsThrough π Q t) :
    ¬ ∃ Q : Process K A, Determined Q ∧ r.StepsThrough π Q t' :=
  fun law => none ((r.law_through_iff π t).mpr (((r.law_through_iff π t').mp law).earlier le))

/-- **`Becoming.Unfolding`'s history law is the instance through the identity.** A run is
consistent through the identity at every step exactly where it is consistent in the sense of
`Consistent`, so `exists_law_iff` is `Run.law_through_iff` through the identity, at every
step. -/
theorem consistent_id_iff (r : Run P) :
    (∀ t, r.ConsistentThrough id t) ↔ Becoming.Consistent r.state r.act :=
  ⟨fun consistent i j same same' =>
     consistent (i + j + 1) i j (Nat.lt_succ_of_le (Nat.le_add_right i j))
       (Nat.lt_succ_of_le (Nat.le_add_left j i)) same same',
   fun consistent _ n m _ _ same same' => consistent n m same same'⟩

/-- Where configurations alike under `π` go alike, every run is consistent through `π` at every
step. -/
theorem consistent_of_goAlike (r : Run P) {π : S → K} (alike : GoAlike P π) (t : Nat) :
    r.ConsistentThrough π t :=
  fun n m _ _ same same' => alike _ _ _ _ _ same (r.step n)
    (Eq.subst (motive := fun b => P.step (r.state m) b (r.state (m + 1))) same'.symm (r.step m))

end Run

/-! ## Exactness -/

/-- Configurations alike under `π` match each other's steps up to `π`: wherever one of two
configurations alike under `π` takes a step, the other takes one by the same move to a
configuration alike under `π` with its end. -/
def MatchesThrough (P : Process S A) (π : S → K) : Prop :=
  ∀ s s' a u', π s = π s' → P.step s' a u' → ∃ u, P.step s a u ∧ π u = π u'

/-- **The image is exact exactly where configurations alike match.** The image of `P` through
`π` represents every finite path exactly, in the sense of `Generative.projection_exact_iff`,
exactly where configurations alike under `π` match each other's steps up to `π`. -/
theorem image_exact_iff {P : Process S A} {π : S → K} :
    (∀ s as r, Trace (Image P π) (π s) as r ↔ ∃ t, Trace P s as t ∧ π t = r) ↔
      MatchesThrough P π :=
  (projection_exact_iff (P := P) (Q := Image P π) (q := π)).symm.trans
    ⟨fun ⟨_, lift⟩ s s' a u' same step' => lift s a (π u') ⟨s', u', same.symm, step', rfl⟩,
     fun matching => ⟨factors_image P π, fun s a _ ⟨s', u', at_k, step', to⟩ =>
       match matching s s' a u' at_k.symm step' with
       | ⟨u, step, same⟩ => ⟨u, step, same.trans to⟩⟩⟩

/-- **An exact law at a description.** Some determined process on the description admits every
step of `P` read through `π` and lifts each of its steps from every configuration in the fibre,
so that it represents every finite path exactly, exactly where configurations alike under `π`
go alike and match each other's steps. -/
theorem exact_law_iff {P : Process S A} {π : S → K} :
    (∃ Q : Process K A, Determined Q ∧ FactorsThrough P π Q ∧
        ∀ s a r, Q.step (π s) a r → ∃ t, P.step s a t ∧ π t = r) ↔
      GoAlike P π ∧ MatchesThrough P π :=
  ⟨fun ⟨Q, determined, factors, lift⟩ =>
     ⟨carries_law_iff.mp ⟨Q, determined, factors⟩, fun s s' a u' same step' =>
       lift s a (π u') (Eq.subst (motive := fun k => Q.step k a (π u')) same.symm
         (factors s' a u' step'))⟩,
   fun ⟨alike, matching⟩ => ⟨Image P π, image_determined_iff.mpr alike, factors_image P π,
     fun s a _ ⟨s', u', at_k, step', to⟩ => match matching s s' a u' at_k.symm step' with
       | ⟨u, step, same⟩ => ⟨u, step, same.trans to⟩⟩⟩

/-! ## Witnesses -/

/-! A process on two configurations allowing every step, and the run that stays at one. -/

namespace Constant

/-- Every step is allowed. -/
def process : Process Bool Unit := ⟨fun _ _ _ => True⟩

/-- The run that stays at `true`. -/
def run : Run process := ⟨fun _ => true, fun _ => (), fun _ => trivial⟩

/-- The staying run is consistent through the identity at every step. -/
theorem consistent (t : Nat) : run.ConsistentThrough id t :=
  fun _ _ _ _ _ _ => rfl

/-- The process does not go alike through the identity: from `true` it goes to either. -/
theorem not_goAlike : ¬ GoAlike process id :=
  fun alike => Bool.noConfusion (alike true true () true false rfl trivial trivial)

end Constant

namespace Switching

/-- The run's first two steps, read through the state, are inconsistent: from the same state by
the same move, one stays and the other changes. -/
theorem inconsistent : ¬ run.ConsistentThrough Prod.fst 2 :=
  fun consistent =>
    Bool.noConfusion (consistent 0 1 (Nat.zero_lt_succ 1) (Nat.lt_succ_self 1) rfl rfl)

end Switching

/-! One configuration has a step and the other none. -/

namespace Stuck

/-- `true` steps to itself; `false` has no step. -/
def process : Process Bool Unit := ⟨fun s _ u => s = true ∧ u = true⟩

/-- **Going alike does not give exactness.** Through the description that tells nothing apart,
the process goes alike, and its configurations do not match each other's steps. -/
theorem goAlike_not_matches :
    GoAlike process (fun _ => ()) ∧ ¬ MatchesThrough process (fun _ => ()) :=
  ⟨goAlike_const process (),
   fun matching => match matching false true () true rfl ⟨rfl, rfl⟩ with
     | ⟨_, step, _⟩ => Bool.noConfusion step.1⟩

end Stuck

namespace Coarse

/-- Coarse's configurations alike in their first bit match each other's steps. -/
theorem matching : MatchesThrough process Prod.fst :=
  fun _ _ _ u' same step' =>
    ⟨u', Eq.trans step' (congrArg (fun b => !b) same.symm), rfl⟩

/-- So its image through the first bit is an exact law. -/
theorem exact_law :
    ∃ Q : Process Bool Unit, Determined Q ∧ FactorsThrough process Prod.fst Q ∧
      ∀ s a r, Q.step s.1 a r → ∃ t, process.step s a t ∧ t.1 = r :=
  exact_law_iff.mpr ⟨goAlike, matching⟩

end Coarse

end Becoming
