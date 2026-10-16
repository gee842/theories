import Becoming.Learning
import Becoming.Assurance

/-!
# Readout: what a reduction keeps of an observable and of a law

A reduction `π : S → K` drops part of a configuration. This module states, for every reduction,
when an observable and a law of change can still be read from what it keeps.

* **Observables.** What an observable `f` reads through `π` is single-valued exactly where `f`
  goes alike across what `π` merges (`reading_single_iff`, with `Learning.Lumped`). A decoder
  of the reduced value forces this (`lumped_of_decodes`); where `π` has a section, it is also
  enough (`decodes_iff_of_section`). On two configurations `π` merges, a decoder agreeing with
  `f` at both exists exactly when `f` agrees there (`decoder_pair_iff`); in particular `π` has no
  inverse on two different configurations it merges (`no_restore`).
* **Laws.** For a law of change with moves, some determined law on the reduced values carries
  every step exactly when configurations `π` merges are taken by each move to configurations it
  merges (`law_through_iff`, the core's `carries_law_iff` read on `Assurance.ofMap`). A reduced
  law that commutes with every move commutes with every course of moves (`foldl_semiconj`).

No premise is added; every declaration has an empty axiom report.
-/

namespace Becoming.Readout

open Generative Becoming.Learning Becoming.Assurance

universe u v w x

variable {S : Type u} {K : Type v} {V : Type w}

/-! ## Observables -/

/-- What `f` reads through `π`: `f` takes the value `v` at some configuration `π` sends to `k`. -/
def Reading (π : S → K) (f : S → V) (k : K) (v : V) : Prop := ∃ s, π s = k ∧ f s = v

/-- A relation that gives at most one value. -/
def SingleValued (R : K → V → Prop) : Prop := ∀ k v v', R k v → R k v' → v = v'

/-- **What an observable reads through a reduction is single-valued exactly where the
observable goes alike across what the reduction merges.** -/
theorem reading_single_iff {π : S → K} {f : S → V} :
    SingleValued (Reading π f) ↔ Lumped π f :=
  ⟨fun single s s' same => single (π s) (f s) (f s') ⟨s, rfl, rfl⟩ ⟨s', same.symm, rfl⟩,
   fun lumped _ _ _ ⟨s, at_k, to_v⟩ ⟨s', at_k', to_v'⟩ =>
    to_v.symm.trans ((lumped s s' (at_k.trans at_k'.symm)).trans to_v')⟩

/-- `g` decodes `f` from the reduced value. -/
def Decodes (π : S → K) (f : S → V) (g : K → V) : Prop := ∀ s, f s = g (π s)

/-- A decoder exists only where the observable goes alike across what is merged. -/
theorem lumped_of_decodes {π : S → K} {f : S → V} {g : K → V} (decodes : Decodes π f g) :
    Lumped π f :=
  fun s s' same => (decodes s).trans ((congrArg g same).trans (decodes s').symm)

/-- **Where the reduction has a section, a decoder exists exactly where the observable goes alike
across what is merged.** -/
theorem decodes_iff_of_section {π : S → K} {f : S → V} (sec : K → S)
    (back : ∀ k, π (sec k) = k) : (∃ g, Decodes π f g) ↔ Lumped π f :=
  ⟨fun ⟨_, decodes⟩ => lumped_of_decodes decodes,
   fun lumped => ⟨fun k => f (sec k), fun s => lumped s (sec (π s)) (back (π s)).symm⟩⟩

/-- **On two configurations the reduction merges, a decoder agreeing with the observable at both
exists exactly when the observable agrees there.** -/
theorem decoder_pair_iff {π : S → K} {f : S → V} {s s' : S} (merged : π s = π s') :
    (∃ g : K → V, g (π s) = f s ∧ g (π s') = f s') ↔ f s = f s' :=
  ⟨fun ⟨g, at_s, at_s'⟩ => at_s.symm.trans ((congrArg g merged).trans at_s'),
   fun same => ⟨fun _ => f s, rfl, same⟩⟩

/-- A reduction has no inverse on two different configurations it merges. -/
theorem no_restore {π : S → K} {s s' : S} (merged : π s = π s') (different : s ≠ s') :
    ¬ ∃ restore : K → S, restore (π s) = s ∧ restore (π s') = s' :=
  fun found => different ((decoder_pair_iff (f := fun x => x) merged).mp found)

/-! ## Laws through a reduction -/

variable {A : Type x}

/-- **Some determined law on the reduced values carries every step of a law of change exactly
when the configurations the reduction merges are taken by each move to configurations it
merges.** -/
theorem law_through_iff (next : S → A → S) (π : S → K) :
    (∃ Q : Process K A, Determined Q ∧ FactorsThrough (ofMap next) π Q) ↔
      ∀ s s' a, π s = π s' → π (next s a) = π (next s' a) :=
  carries_law_iff.trans
    ⟨fun alike s s' a same => alike s s' a (next s a) (next s' a) same rfl rfl,
     fun every s s' a u u' same step step' =>
      have to_u : u = next s a := step
      have to_u' : u' = next s' a := step'
      to_u ▸ to_u' ▸ every s s' a same⟩

/-- **A reduced law that commutes with every move commutes with every course of moves.** -/
theorem foldl_semiconj (next : S → A → S) (π : S → K) (reduced : K → A → K)
    (commutes : ∀ s a, π (next s a) = reduced (π s) a) :
    ∀ (plan : List A) (s : S), π (plan.foldl next s) = plan.foldl reduced (π s)
  | [], _ => rfl
  | a :: rest, s =>
    (foldl_semiconj next π reduced commutes rest (next s a)).trans
      (congrArg (fun k => rest.foldl reduced k) (commutes s a))

end Becoming.Readout
