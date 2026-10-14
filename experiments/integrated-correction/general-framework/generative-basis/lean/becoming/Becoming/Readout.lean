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
* **Futures through a reduction.** For a law that need not be determined, the law read through
  a reduction (`image`) takes from each reduced value exactly the words the configuration can
  take, for every configuration, exactly when configurations the reduction merges can take the
  same words (`futures_through_iff`).
* **Fallible witnesses.** A complete report of listed witnesses, some at fault, reduces an
  answer. For two different answers, no report is explained both by the one with some witnesses
  at fault and by the other with others at fault exactly where some witness is in neither fault
  set (`no_common_report_iff`); under admitted envelopes of fault sets, exactly where every two
  fault sets admitted for the two answers leave a common faithful witness
  (`no_common_report_envelopes_iff`). Where every witness is in one of them, the report blaming
  one set explains both (`blame`).
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

/-! ## Futures through a reduction -/

section Futures

/-- The law read through a reduction: a move from `k` to `k'` where it takes some configuration
`π` sends to `k` to one it sends to `k'`. -/
def image (P : Process S A) (π : S → K) : Process K A :=
  ⟨fun k a k' => ∃ s t, π s = k ∧ P.step s a t ∧ π t = k'⟩

/-- The same words can be taken from both configurations. -/
def SameFutures (P : Process S A) (s s' : S) : Prop :=
  ∀ word, Feasible P s word ↔ Feasible P s' word

theorem image_feasible {P : Process S A} {π : S → K} {s : S} {word : List A} :
    Feasible P s word → Feasible (image P π) (π s) word
  | ⟨t, path⟩ => ⟨π t, trace_map (Q := image P π) (f := π) (fun s _ t step => ⟨s, t, rfl, step, rfl⟩) path⟩

theorem feasible_of_image {P : Process S A} {π : S → K}
    (fibers : ∀ s s', π s = π s' → SameFutures P s s') :
    ∀ {s : S} {word : List A}, Feasible (image P π) (π s) word → Feasible P s word
  | s, [], _ => ⟨s, .nil s⟩
  | s, a :: word, ⟨_, .cons ⟨s₁, t₁, here, step, there⟩ rest⟩ =>
    have rest : Feasible (image P π) (π t₁) word :=
      ⟨_, Eq.subst (motive := fun k => Trace (image P π) k word _) there.symm rest⟩
    let ⟨u, path⟩ := feasible_of_image fibers rest
    (fibers s₁ s here (a :: word)).mp ⟨u, .cons step path⟩

/-- **A reduction carries the futures exactly where it merges only configurations with the same
futures.** From the reduced value of each configuration the law read through `π` takes exactly
the words the configuration can take, for every configuration, exactly when configurations `π`
merges can take the same words. The nondeterministic counterpart of `law_through_iff`. -/
theorem futures_through_iff {P : Process S A} {π : S → K} :
    (∀ s word, Feasible (image P π) (π s) word ↔ Feasible P s word) ↔
      ∀ s s', π s = π s' → SameFutures P s s' :=
  ⟨fun exact s s' same word => (exact s word).symm.trans
      ((Eq.subst (motive := fun k => Feasible (image P π) k word ↔ Feasible (image P π) (π s') word)
        same.symm Iff.rfl).trans (exact s' word)),
   fun fibers _ _ => ⟨feasible_of_image fibers, image_feasible⟩⟩

end Futures

/-! ## Fallible witnesses -/

section Witnesses

variable {D : Type} [DecidableEq D]

/-- A complete report of a listed roster of witnesses explains the answer `x` with the witnesses
in `bad` at fault: every witness of the roster outside `bad` reports `x`. -/
def Explains (roster bad : List D) (x : Bool) (report : D → Bool) : Prop :=
  ∀ d ∈ roster, ¬ d ∈ bad → report d = x

/-- A witness of the roster outside both fault sets. -/
def CommonWitness (roster a b : List D) : Prop :=
  ∃ d, d ∈ roster ∧ ¬ d ∈ a ∧ ¬ d ∈ b

/-- Going through the roster: a witness outside both fault sets, or every witness outside `b`
is in `a`. -/
theorem commonWitness_or_covered (a b : List D) :
    ∀ roster : List D, CommonWitness roster a b ∨ ∀ d ∈ roster, ¬ d ∈ b → d ∈ a
  | [] => .inr fun _ mem _ => nomatch mem
  | d :: tail => match commonWitness_or_covered a b tail with
    | .inl ⟨w, mem, na, nb⟩ => .inl ⟨w, .tail d mem, na, nb⟩
    | .inr covered => match decideMem d a, decideMem d b with
      | .isTrue inA, _ => .inr fun w mem nb => match mem_cons_cases mem with
        | .inl same => Eq.subst (motive := fun v => v ∈ a) same.symm inA
        | .inr mem => covered w mem nb
      | .isFalse _, .isTrue inB => .inr fun w mem nb => match mem_cons_cases mem with
        | .inl same => absurd (Eq.subst (motive := fun v => v ∈ b) same.symm inB) nb
        | .inr mem => covered w mem nb
      | .isFalse na, .isFalse nb => .inl ⟨d, .head tail, na, nb⟩

/-- `y` where a decision holds, `x` where it fails. -/
def pick {p : Prop} : Decidable p → Bool → Bool → Bool
  | .isTrue _, y, _ => y
  | .isFalse _, _, x => x

theorem pick_of {p : Prop} (h : p) : ∀ (d : Decidable p) (y x : Bool), pick d y x = y
  | .isTrue _, _, _ => rfl
  | .isFalse no, _, _ => absurd h no

theorem pick_of_not {p : Prop} (h : ¬ p) : ∀ (d : Decidable p) (y x : Bool), pick d y x = x
  | .isTrue yes, _, _ => absurd yes h
  | .isFalse _, _, _ => rfl

/-- The report blaming the witnesses in `a`: they report `y`, the others `x`. -/
def blame (a : List D) (x y : Bool) (d : D) : Bool :=
  pick (decideMem d a) y x

/-- **Fallible witnesses tell two answers apart exactly where their fault sets leave a common
faithful witness.** For different answers, no complete report is explained both by `x` with the
witnesses in `a` at fault and by `y` with those in `b` at fault exactly where some witness of the
roster is in neither. Where every witness is in one of them, the report blaming `a` explains
both. -/
theorem no_common_report_iff {roster a b : List D} {x y : Bool} (different : x ≠ y) :
    (∀ report : D → Bool, Explains roster a x report → ¬ Explains roster b y report) ↔
      CommonWitness roster a b :=
  ⟨fun apart => match commonWitness_or_covered a b roster with
    | .inl common => common
    | .inr covered => absurd (fun d mem nb => pick_of (covered d mem nb) (decideMem d a) y x)
        (apart (blame a x y) fun d _ na => pick_of_not na (decideMem d a) y x),
   fun ⟨d, mem, na, nb⟩ _ first second => different ((first d mem na).symm.trans (second d mem nb))⟩

/-- **With admitted fault envelopes.** No complete report is explained both by `x` under a fault
set admitted in `fa` and by `y` under one admitted in `fb` exactly where every two such fault
sets leave a common faithful witness. -/
theorem no_common_report_envelopes_iff {roster : List D} {fa fb : List (List D)} {x y : Bool}
    (different : x ≠ y) :
    (∀ report : D → Bool, (∃ a, a ∈ fa ∧ Explains roster a x report) →
        ¬ ∃ b, b ∈ fb ∧ Explains roster b y report) ↔
      ∀ a, a ∈ fa → ∀ b, b ∈ fb → CommonWitness roster a b :=
  ⟨fun apart a ma b mb => (no_common_report_iff different).mp
      fun report first second => apart report ⟨a, ma, first⟩ ⟨b, mb, second⟩,
   fun cross report ⟨a, ma, first⟩ ⟨b, mb, second⟩ =>
      (no_common_report_iff different).mpr (cross a ma b mb) report first second⟩

end Witnesses

end Becoming.Readout
