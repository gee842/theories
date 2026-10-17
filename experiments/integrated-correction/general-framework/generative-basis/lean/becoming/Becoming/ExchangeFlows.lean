import Becoming.Evolution
import Becoming.Sampling

/-!
# Exchange flows: uniform descent, and what a sampled flow keeps of an absent relatum

`Becoming.Evolution` states the counting form of Price's equation and the selection bound it gives
on a flow (`Flow.selection_within`), and that the parents' amounts weighted by their offspring are,
where every parent has `k` offspring, `k` times the parents' total (`selected_uniform`).
`Becoming.Sampling` reads a flow at coarser times (`Flow.sample`), keeping each relatum's exchanges
at the fine steps it takes part in through a gate that is zero where the decision fails
(`gateBy_of_not`). This module states both of flows.

* **Uniform descent.** Where only active formations give and activity needs support, and every
  parent of a family depending on a condition leaves `k` descendants across the step, `k` times the
  parents' total need is at most `k` times the condition's level once for each parent
  (`selected_le_uniform`), and the descendants' total of any amount with what transmission lowered
  is at most that with what transmission raised (`selection_within_uniform`).
* **An absent relatum in a sampled flow.** A relatum taking part in no fine step of a coarse step
  takes nothing and gives nothing across it in the sampled flow (`sample_take_absent`,
  `sample_give_absent`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

namespace ExchangeFlows

/-! ## Uniform descent -/

section Descent

variable {X : Type} {L : Flow X X} {W : Web X X}

/-- **Uniform descent bounds the parents' need.** Where only active formations give, activity
needs support, and each of a family of parents depending on `c` leaves `k` descendants across the
step from `t`, `k` times the parents' total need on `c` is at most `k` times the level of `c`
counted once for each parent. -/
theorem selected_le_uniform (acting : L.Acting W) (dependent : W.Dependent) {t : Nat} {c : X}
    {ps : List X} {kids : X → List X} (descend : ∀ p k, p ∈ ps → k ∈ kids p → L.DescendsAt W t k p)
    (depends : ∀ p, p ∈ ps → W.requires t p c) {k : Nat} (uniform : ∀ p, (kids p).length = k) :
    k * total ps (fun p => W.need t p c) ≤ k * (ps.length * W.level t c) :=
  Nat.le_trans (Nat.le_of_eq (selected_uniform ps kids _ k uniform).symm)
    (Nat.le_trans (Flow.selected_le acting dependent descend depends)
      (Nat.le_of_eq ((selected_uniform ps kids _ k uniform).trans
        (congrArg (k * ·) (total_const (W.level t c) ps)))))

/-- **Uniform descent bounds what the descendants carry.** Under the same premises, the
descendants' total of any amount, with what transmission lowered from the parents' needs, is at
most `k` times the level of `c` counted once for each parent, with what transmission raised. -/
theorem selection_within_uniform (acting : L.Acting W) (dependent : W.Dependent) {t : Nat}
    {c : X} {ps : List X} {kids : X → List X}
    (descend : ∀ p k, p ∈ ps → k ∈ kids p → L.DescendsAt W t k p)
    (depends : ∀ p, p ∈ ps → W.requires t p c) {k : Nat} (uniform : ∀ p, (kids p).length = k)
    (b : X → Nat) :
    offspring ps kids b + lowered ps kids (fun p => W.need t p c) b ≤
      k * (ps.length * W.level t c) + raised ps kids (fun p => W.need t p c) b :=
  Nat.le_trans (Flow.selection_within acting dependent descend depends b)
    (Nat.le_of_eq (congrArg (· + raised ps kids (fun p => W.need t p c) b)
      ((selected_uniform ps kids _ k uniform).trans
        (congrArg (k * ·) (total_const (W.level t c) ps)))))

end Descent

/-! ## An absent relatum in a sampled flow -/

section Sampled

variable {F C : Type} [DecidableEq F]

/-- **An absent relatum takes nothing in the sampled flow.** A relatum taking part in no fine step
of the coarse step `s` takes nothing from any condition across it. -/
theorem sample_take_absent (L : Flow F C) (σ : Nat → Nat) {s : Nat} {f : F}
    (absent : ∀ j, j ∈ span σ s → ¬ f ∈ L.present j) (c : C) : (L.sample σ).take s f c = 0 :=
  (total_congr_on fun j mem => gateBy_of_not (absent j mem) _ _).trans (total_zero _)

/-- **An absent relatum gives nothing in the sampled flow.** -/
theorem sample_give_absent (L : Flow F C) (σ : Nat → Nat) {s : Nat} {f : F}
    (absent : ∀ j, j ∈ span σ s → ¬ f ∈ L.present j) (c : C) : (L.sample σ).give s f c = 0 :=
  (total_congr_on fun j mem => gateBy_of_not (absent j mem) _ _).trans (total_zero _)

end Sampled

end ExchangeFlows

end Becoming
