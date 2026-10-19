import Becoming.Evolution
import Becoming.Locality
import Becoming.Recurrence

/-!
# Capture: how a target that cannot rest is selected, and where the selection is held

The fifth candidate condition of the boundary for 无明 (B5): targets are formed and passed on,
and where winning buys more power to win, formations whose targets cannot be met at rest take
more and pass their targets on more, until enclosure binds; the winners write the rule by which
seeking is judged. Ren gave the go on 11 October 2026: "b5". This module states three parts of
it, with no axiom and no premise beyond what each law names.

* **A target's share among descendants.** `Becoming.Evolution` states the counting form of
  Price's equation and leaves its selection term unstated. For a target carried by some parents
  and not by others: where each carrier leaves at least as many offspring as each other parent,
  the carriers' offspring stand to the others' at least as the carriers stand to the others
  (`share_not_lower`), and strictly where each carrier leaves more and both kinds are present
  (`share_rises`). Where the carriers' offspring carry the target and the others' do not, which
  is transmission and a premise as in `Becoming.Evolution`, this is the target's share among
  the offspring not falling below, or rising above, its share among the parents.
* **Until enclosure binds.** A descent is a coming to stand, so a rise. Where what stands is
  listed at each step, descent at arbitrarily late steps needs, at arbitrarily late steps, steps
  across which what stands does not run down (`Flow.descent_needs_unrun`); where it runs down at
  every step from some step on, descent does not recur and the selection stops
  (`Flow.descent_exhausted`).
* **The rule holds the outcome.** Read the configuration as a state scored and a rule that
  scores it. Where the next configuration depends on the rule and not on the state, perturbing
  the state alone is re-absorbed: from the next step on the unfolding is as if it had not been
  perturbed (`Law.perturbation_reabsorbed`, the instance of `Law.reabsorbed` of `Becoming.Mechanism`
  with the rule as the projection). In `Captured` the state follows the rule and the rule keeps
  itself: a perturbed state returns at once, and a perturbed rule changes the outcome
  (`Captured.state_perturbation_returns`, `Captured.rule_perturbation_changes`).

**Readings (the AI's, adopted on Ren's delegation of 15 October 2026, DELEGATED-CHOICES D26).**
- The meta-attractor's selection of minds: where a target of more than now, or of above all
  others (`Becoming.Seeking`), leads its carriers to take more, and taking more leads to more
  offspring, the target's share rises; it does so only while the world is open, and enclosed,
  the selection stops with the descent.
- The winner rewrites the test: where the winners' state shapes the rule, and the rule fixes
  the state, the outcome is held in the rule. Perturbation of the state alone is re-absorbed;
  escape needs the rule changed. The rule can reach the standard of reason itself.
- Hijacking is this: a target formed and passed on by a selection that rewards what cannot
  rest, held in place by a rule its winners write.

What is not derived: that taking more yields more offspring; that offspring carry their
parents' targets; that winners shape the rule; which rules actual formations live under. No
ethical predicate, ranking or axiom occurs.

`Law.perturbation_reabsorbed` is in `Becoming.SeekingRuns` (board item W).
-/

namespace Becoming

universe u v

/-! ## A target's share among descendants -/

section Share

variable {α : Type}

/-- The offspring of a family of parents, counted. -/
def offspringCount (ps : List α) (kids : α → List α) : Nat :=
  total ps fun p => (kids p).length

/-- Each parent leaving at least `a` offspring, the family leaves at least `a` for each parent. -/
theorem le_offspringCount {kids : α → List α} {a : Nat} :
    ∀ {ps : List α}, (∀ p, p ∈ ps → a ≤ (kids p).length) → ps.length * a ≤ offspringCount ps kids
  | [], _ => Nat.le_of_eq (Nat.zero_mul a)
  | p :: ps, each =>
    Nat.le_trans (Nat.le_of_eq (Nat.succ_mul ps.length a))
      (Nat.le_trans (Nat.le_of_eq (Nat.add_comm _ _))
        (Nat.add_le_add (each p (.head ps))
          (le_offspringCount fun q mem => each q (.tail p mem))))

/-- Each parent leaving at most `b` offspring, the family leaves at most `b` for each parent. -/
theorem offspringCount_le {kids : α → List α} {b : Nat} :
    ∀ {ps : List α}, (∀ p, p ∈ ps → (kids p).length ≤ b) → offspringCount ps kids ≤ ps.length * b
  | [], _ => Nat.le_of_eq (Nat.zero_mul b).symm
  | p :: ps, each =>
    Nat.le_trans
      (Nat.add_le_add (each p (.head ps)) (offspringCount_le fun q mem => each q (.tail p mem)))
      (Nat.le_trans (Nat.le_of_eq (Nat.add_comm _ _)) (Nat.le_of_eq (Nat.succ_mul ps.length b).symm))

/-- **A target's share does not fall.** Carriers `ms` each leaving at least `a` offspring, the
others `es` each at most `b`, with `b ≤ a`: the carriers' offspring stand to the others' at least
as the carriers stand to the others. -/
theorem share_not_lower {kids : α → List α} {ms es : List α} {a b : Nat}
    (carriers : ∀ p, p ∈ ms → a ≤ (kids p).length) (others : ∀ p, p ∈ es → (kids p).length ≤ b)
    (le : b ≤ a) : ms.length * offspringCount es kids ≤ offspringCount ms kids * es.length :=
  calc ms.length * offspringCount es kids
      ≤ ms.length * (es.length * b) := Nat.mul_le_mul_left _ (offspringCount_le others)
    _ = ms.length * b * es.length :=
        (congrArg (ms.length * ·) (Nat.mul_comm es.length b)).trans (mul_assoc_nat _ _ _).symm
    _ ≤ ms.length * a * es.length := Nat.mul_le_mul_right _ (Nat.mul_le_mul_left _ le)
    _ ≤ offspringCount ms kids * es.length := Nat.mul_le_mul_right _ (le_offspringCount carriers)

/-- **A target's share rises.** Where each carrier leaves more offspring than each other parent
and both kinds are present, the carriers' offspring stand to the others' strictly more than the
carriers stand to the others. -/
theorem share_rises {kids : α → List α} {ms es : List α} {a b : Nat}
    (carriers : ∀ p, p ∈ ms → a ≤ (kids p).length) (others : ∀ p, p ∈ es → (kids p).length ≤ b)
    (lt : b < a) (some : 0 < ms.length) (some' : 0 < es.length) :
    ms.length * offspringCount es kids < offspringCount ms kids * es.length :=
  calc ms.length * offspringCount es kids
      ≤ ms.length * (es.length * b) := Nat.mul_le_mul_left _ (offspringCount_le others)
    _ = ms.length * es.length * b := (mul_assoc_nat _ _ _).symm
    _ < ms.length * es.length * a := Nat.mul_lt_mul_of_pos_left lt (Nat.mul_pos some some')
    _ = ms.length * a * es.length := (mul_assoc_nat _ _ _).trans
        ((congrArg (ms.length * ·) (Nat.mul_comm es.length a)).trans (mul_assoc_nat _ _ _).symm)
    _ ≤ offspringCount ms kids * es.length := Nat.mul_le_mul_right _ (le_offspringCount carriers)

end Share

/-! ## Until enclosure binds -/

namespace Flow

variable {X : Type} {L : Flow X X} {W : Web X X} {stand : Nat → List X}

/-- **Selection needs a beyond.** Where what stands is listed at each step, descent at
arbitrarily late steps needs, at arbitrarily late steps, steps across which what stands does not
run down. -/
theorem descent_needs_unrun (census : W.StandingCensus stand)
    (descent : ∀ N, ∃ t, N ≤ t ∧ ∃ x g, L.DescendsAt W t x g) :
    ∀ N, ∃ t, N ≤ t ∧ ¬ L.RunsDown W t :=
  fun N => match (change_recurs_iff (L := L) census).mp
      (fun N => match descent N with
        | ⟨t, le, _, _, descends⟩ => ⟨t, le, _, .inl descends.2.2.rises⟩) N with
    | ⟨t, le, unrun, _⟩ => ⟨t, le, unrun⟩

/-- **Enclosed, the selection stops.** Where what stands is listed at each step and runs down at
every step from `T` on, descent does not recur. -/
theorem descent_exhausted (census : W.StandingCensus stand) {T : Nat}
    (runs : ∀ t, T ≤ t → L.RunsDown W t) : ¬ ∀ N, ∃ t, N ≤ t ∧ ∃ x g, L.DescendsAt W t x g :=
  fun descent => match descent_needs_unrun census descent T with
    | ⟨t, le, unrun⟩ => unrun (runs t le)

end Flow

/-! ## The rule holds the outcome -/

/-! ## A captured rule

The state is which of two variants prevails, the rule which it favours. The state follows the
rule, and the rule keeps itself. -/

namespace Captured

/-- The state follows the rule; the rule keeps itself. -/
def next (s : Bool × Bool) : Bool × Bool := (s.2, s.2)

theorem byRule (x x' g : Bool) : next (x, g) = next (x', g) := rfl

/-- **A perturbed state returns at once.** Perturbing the state against the rule, the unfolding is
back where the rule holds it at the next step and stays there. -/
theorem state_perturbation_returns (g : Bool) :
    ∀ n, Law.orbit next (!g, g) (n + 1) = (g, g) ∧ Law.orbit next (g, g) (n + 1) = (g, g)
  | 0 => ⟨rfl, rfl⟩
  | n + 1 => match state_perturbation_returns g n with
    | ⟨back, here⟩ => ⟨congrArg next back, congrArg next here⟩

/-- **A perturbed rule changes the outcome.** Perturbing the rule, the state follows the new rule
from the next step on. -/
theorem rule_perturbation_changes (g : Bool) :
    ∀ n, Law.orbit next (g, !g) (n + 1) = (!g, !g)
  | 0 => rfl
  | n + 1 => congrArg next (rule_perturbation_changes g n)

end Captured

end Becoming

section CaptureWorlds

/-!
## Capture in worlds: a target's share among descendants

`Becoming.Capture` states the share of a target among offspring for any family of parents and
any listing of their offspring (`share_not_lower`, `share_rises`), and `Becoming.Evolution` states
selection through support in a world: where only active formations give and activity needs
support, a formation unsupported at a step leaves no descendant across it
(`unsupported_childless`). This section joins the two. Read the offspring of each parent as
relata descending from it across a step of a world's flow (`Flow.DescendsAt`).

* **Unsupported others, rising share.** Where the formations not carrying a target are
  unsupported at the step, and each carrier leaves at least one descendant across it, the
  carriers' descendants stand to the others' strictly more than the carriers stand to the others
  (`share_rises_of_unsupported`), and the others leave none (`unsupported_leave_none`); with no
  count of the carriers' descendants, the share does not fall (`share_not_lower_of_unsupported`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

namespace CaptureWorlds

variable {X : Type} {L : Flow X X} {W : Web X X}

/-- A list with no member has length zero. -/
theorem length_le_zero {l : List X} (none : ∀ k, k ∈ l → False) : l.length ≤ 0 :=
  match l, none with
  | [], _ => Nat.le_refl 0
  | k :: _, none => (none k (.head _)).elim

/-- **Formations unsupported at a step leave no descendant listed across it.** Where only
active formations give and activity needs support, an unsupported formation's listed
descendants across the step number none. -/
theorem unsupported_leave_none (acting : L.Acting W) (dependent : W.Dependent) {t : Nat}
    {es : List X} {kids : X → List X} (descend : ∀ p k, p ∈ es → k ∈ kids p → L.DescendsAt W t k p)
    (unsupported : ∀ p, p ∈ es → ¬ W.Supported t p) : ∀ p, p ∈ es → (kids p).length ≤ 0 :=
  fun p mem => length_le_zero fun k kid =>
    Flow.unsupported_childless acting dependent (unsupported p mem) k (descend p k mem kid)

/-- **Selection through support raises a target's share.** Where only active formations give
and activity needs support, the formations not carrying a target are unsupported at the step and
their listed offspring descend from them across it, and each carrier leaves at least one listed
descendant, the carriers' descendants stand to the others' strictly more than the carriers stand
to the others, both kinds present. -/
theorem share_rises_of_unsupported (acting : L.Acting W) (dependent : W.Dependent) {t : Nat}
    {ms es : List X} {kids : X → List X} {a : Nat}
    (descend : ∀ p k, p ∈ es → k ∈ kids p → L.DescendsAt W t k p)
    (unsupported : ∀ p, p ∈ es → ¬ W.Supported t p)
    (carriers : ∀ p, p ∈ ms → a ≤ (kids p).length) (pos : 0 < a)
    (some : 0 < ms.length) (some' : 0 < es.length) :
    ms.length * offspringCount es kids < offspringCount ms kids * es.length :=
  share_rises carriers (unsupported_leave_none acting dependent descend unsupported) pos some some'

/-- **Selection through support keeps a target's share from falling.** Where only active
formations give and activity needs support, and the formations not carrying a target are
unsupported at the step with their listed offspring descending from them across it, the carriers'
descendants stand to the others' at least as the carriers stand to the others. -/
theorem share_not_lower_of_unsupported (acting : L.Acting W) (dependent : W.Dependent) {t : Nat}
    {ms es : List X} {kids : X → List X}
    (descend : ∀ p k, p ∈ es → k ∈ kids p → L.DescendsAt W t k p)
    (unsupported : ∀ p, p ∈ es → ¬ W.Supported t p) :
    ms.length * offspringCount es kids ≤ offspringCount ms kids * es.length :=
  share_not_lower (a := 0) (fun _ _ => Nat.zero_le _)
    (unsupported_leave_none acting dependent descend unsupported) (Nat.le_refl 0)

end CaptureWorlds

end Becoming

end CaptureWorlds
