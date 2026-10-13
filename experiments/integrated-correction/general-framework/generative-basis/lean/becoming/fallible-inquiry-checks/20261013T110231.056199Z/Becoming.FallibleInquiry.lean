import Becoming.Counterfactual
import ScientificInquiryNecessity

/-!
# Fallible inquiry through responsive relations (periphery)

This composes the existing Becoming flows, webs and common-law response theorem
with the established finite discrimination bound. It introduces no new world model
and is not imported by the pure core. The two courses are alternatives within one
relational description. The differing part, common law, initial records, complete
reading interface and actual interpretation of the finite weights are supplied.

The output is a necessary bound, not a sufficient condition for knowledge. Reach
is the structural closure in either whole course; it need not transmit a difference
by the answer time. Historical records that already differ violate the named common
start premise. Prediction need not receive a signal from a future target event.
-/
namespace Becoming
namespace FallibleInquiry

open Generative.ScientificInquiryNecessity

variable {F C : Type} {L L' : Flow F C} {W W' : Web F C}
  {obs : F → C → Prop} {part : F → Bool} {g : F} {t : Nat}

/-- Every response through a formation's complete past registration agrees outside
responsive reach. Balance is supplied on all conditions for this adapter. -/
theorem answer_alike_beyond_response
    (balanced : L.Balances W) (balanced' : L'.Balances W')
    (present : ∀ s, L.present s = L'.present s)
    (start : ∀ h, ¬ L.WithinResponse L' W obs part h →
      ∀ c, W.Registers obs h c → W.level 0 c = W'.level 0 c)
    (responds : L.RespondsThroughRegistration L' W W' obs part)
    (read : (Nat → C → Nat) → Option Bool)
    (through : ∀ l l', W.RegistersAlikeUpTo obs g l l' t → read l = read l')
    (beyond : ¬ L.WithinResponse L' W obs part g) :
    read W.level = read W'.level :=
  through _ _ fun s _ => Flow.alike_beyond_response
    (fun s _ c _ _ => balanced.on [c] s)
    (fun s _ c _ _ => balanced'.on [c] s) present start responds s g beyond

/-- Different answers exclude being beyond responsive reach. No decision of reach,
perfect correctness, or conclusion that reach is sufficient is used. -/
theorem different_answers_not_beyond
    (balanced : L.Balances W) (balanced' : L'.Balances W')
    (present : ∀ s, L.present s = L'.present s)
    (start : ∀ h, ¬ L.WithinResponse L' W obs part h →
      ∀ c, W.Registers obs h c → W.level 0 c = W'.level 0 c)
    (responds : L.RespondsThroughRegistration L' W W' obs part)
    (read : (Nat → C → Nat) → Option Bool)
    (through : ∀ l l', W.RegistersAlikeUpTo obs g l l' t → read l = read l')
    (different : read W.level ≠ read W'.level) :
    ¬ ¬ L.WithinResponse L' W obs part g :=
  fun beyond => different (answer_alike_beyond_response
    balanced balanced' present start responds read through beyond)

/-- The response premise is derived from the same exchange law in both courses. -/
theorem answer_alike_beyond_law {law : ExchangeLaw F C}
    (balanced : L.Balances W) (balanced' : L'.Balances W')
    (present : ∀ s, L.present s = L'.present s)
    (start : ∀ h, ¬ L.WithinResponse L' W obs part h →
      ∀ c, W.Registers obs h c → W.level 0 c = W'.level 0 c)
    (lawThrough : law.Through W obs part)
    (follows : L.Follows law part W.level) (follows' : L'.Follows law part W'.level)
    (read : (Nat → C → Nat) → Option Bool)
    (through : ∀ l l', W.RegistersAlikeUpTo obs g l l' t → read l = read l')
    (beyond : ¬ L.WithinResponse L' W obs part g) :
    read W.level = read W'.level :=
  answer_alike_beyond_response balanced balanced' present start
    (lawThrough.responds follows follows') read through beyond

section Weighted

variable {X : Type} (xs : List X) (weight : X → Nat)
    (left right : X → Flow F C) (web web' : X → Web F C)
    (observe : X → F → C → Prop) (vary : X → F → Bool)
    (reader : X → F) (time : X → Nat) (law : X → ExchangeLaw F C)
    (read : X → (Nat → C → Nat) → Option Bool)
    [reachDecision : ∀ x, Decidable ((left x).WithinResponse (right x) (web x) (observe x) (vary x) (reader x))]
    (balanced : ∀ x ∈ xs, (left x).Balances (web x))
    (balanced' : ∀ x ∈ xs, (right x).Balances (web' x))
    (present : ∀ x ∈ xs, ∀ s, (left x).present s = (right x).present s)
    (start : ∀ x ∈ xs, ∀ h,
      ¬ (left x).WithinResponse (right x) (web x) (observe x) (vary x) h →
      ∀ c, (web x).Registers (observe x) h c → (web x).level 0 c = (web' x).level 0 c)
    (lawThrough : ∀ x ∈ xs, (law x).Through (web x) (observe x) (vary x))
    (follows : ∀ x ∈ xs, (left x).Follows (law x) (vary x) (web x).level)
    (follows' : ∀ x ∈ xs, (right x).Follows (law x) (vary x) (web' x).level)
    (through : ∀ x ∈ xs, ∀ l l',
      (web x).RegistersAlikeUpTo (observe x) (reader x) l l' (time x) → read x l = read x l')

include balanced balanced' present start lawThrough follows follows' through

/-- Commitment is bounded by two error weights plus the weight of comparisons
whose varying part can reach the reader. The targets are false/true in the paired
courses; assigning those labels to actual scientific targets is correspondence. -/
theorem coverage_le_errors_add_reach :
    tally weight (fun x => committed (read x (web x).level)) xs ≤
      tally weight (fun x => wrong false (read x (web x).level)) xs +
      tally weight (fun x => wrong true (read x (web' x).level)) xs +
      tally weight (fun x => if (left x).WithinResponse (right x) (web x)
        (observe x) (vary x) (reader x) then 1 else 0) xs := by
  have info := fallible_inquiry_bound xs weight
    (fun x => read x (web x).level) (fun x => read x (web' x).level) (fun _ a => a)
  have bound := tally_mono xs weight
    (fun x => apart (read x (web x).level) (read x (web' x).level))
    (fun x => if (left x).WithinResponse (right x) (web x)
      (observe x) (vary x) (reader x) then 1 else 0) (by
    intro x mem
    by_cases reach : (left x).WithinResponse (right x) (web x) (observe x) (vary x) (reader x)
    · simp only [if_pos reach, apart]
      split <;> omega
    · have same := answer_alike_beyond_law (balanced x mem) (balanced' x mem)
        (present x mem) (start x mem) (lawThrough x mem) (follows x mem) (follows' x mem)
        (read x) (through x mem) reach
      simp [apart, same, reach])
  exact Nat.le_trans info (Nat.add_le_add_left bound _)

/-- An independently specified coverage/error achievement forces enough responsive
reach. Finite weights need not be probabilities; normalization is a separate reading. -/
theorem error_budgets_require_reach (coverage b0 b1 : Nat)
    (hc : coverage ≤ tally weight (fun x => committed (read x (web x).level)) xs)
    (h0 : tally weight (fun x => wrong false (read x (web x).level)) xs ≤ b0)
    (h1 : tally weight (fun x => wrong true (read x (web' x).level)) xs ≤ b1) :
    coverage ≤ b0 + b1 + tally weight (fun x =>
      if (left x).WithinResponse (right x) (web x) (observe x) (vary x) (reader x)
      then 1 else 0) xs := by
  have bound := coverage_le_errors_add_reach xs weight left right web web' observe vary
    reader time law read balanced balanced' present start lawThrough follows follows' through
  omega

omit reachDecision in
/-- If all paired comparisons are beyond reach, every committed answer contributes
exactly one error across the two target alternatives; abstention contributes neither. -/
theorem beyond_reach_coverage_eq_errors
    (beyond : ∀ x ∈ xs,
      ¬ (left x).WithinResponse (right x) (web x) (observe x) (vary x) (reader x)) :
    tally weight (fun x => committed (read x (web x).level)) xs =
      tally weight (fun x => wrong false (read x (web x).level)) xs +
      tally weight (fun x => wrong true (read x (web' x).level)) xs := by
  have same : ∀ x ∈ xs, read x (web x).level = read x (web' x).level :=
    fun x mem => answer_alike_beyond_law (balanced x mem) (balanced' x mem)
      (present x mem) (start x mem) (lawThrough x mem) (follows x mem) (follows' x mem)
      (read x) (through x mem) (beyond x mem)
  have le := tally_mono xs weight
    (fun x => wrong true (read x (web x).level))
    (fun x => wrong true (read x (web' x).level))
    (fun x mem => Nat.le_of_eq (congrArg (wrong true) (same x mem)))
  have ge := tally_mono xs weight
    (fun x => wrong true (read x (web' x).level))
    (fun x => wrong true (read x (web x).level))
    (fun x mem => Nat.le_of_eq (congrArg (wrong true) (same x mem).symm))
  rw [blind_coverage_bound xs weight (fun x => read x (web x).level), Nat.le_antisymm le ge]

end Weighted

/-! Native witnesses: two differentiated formations share one condition. The part
adds to it; a distinct reader registers it. No external truth oracle drives either
flow. The false/true target labels describe absence/presence of the part's giving. -/
namespace Witness

def web (signal : Bool) : Web Bool Unit where
  level := fun t _ => if signal then t else 0
  active := fun _ _ => True
  requires := fun _ _ _ => False
  need := fun _ _ _ => 0
  draws := fun _ _ _ => False

def flow (signal : Bool) : Flow Bool Unit where
  present := fun _ => [true, false]
  take := fun _ _ _ => 0
  give := fun _ h _ => if h && signal then 1 else 0

def law : ExchangeLaw Bool Unit where
  take := fun _ _ _ _ => 0
  give := fun _ _ _ _ => 0

def read (l : Nat → Unit → Nat) : Option Bool := some (decide (0 < l 1 ()))

theorem balanced (b : Bool) : (flow b).Balances (web b) := by
  intro t c
  cases b <;> simp [Flow.taken, Flow.given, flow, web, total]

theorem law_through : law.Through (web false) (fun _ _ => True) (fun h => h) :=
  fun _ _ _ _ _ _ _ => ⟨rfl, rfl⟩

theorem follows (b : Bool) : (flow b).Follows law (fun h => h) (web b).level := by
  intro h out t c
  cases h <;> simp_all [flow, law]

theorem read_through : ∀ l l', (web false).RegistersAlikeUpTo
    (fun _ _ => True) false l l' 1 → read l = read l' :=
  fun _ _ alike => congrArg (fun n => some (decide (0 < n))) ((alike 1 (Nat.le_refl 1)).2 () trivial)

/-- The reader is outside the varying part, starts alike, and receives its effect. -/
theorem connected :
    (∀ c, (web false).level 0 c = (web true).level 0 c) ∧
    (flow false).WithinResponse (flow true) (web false) (fun _ _ => True) (fun h => h) false := by
  refine ⟨fun _ => rfl, true, rfl, WithinClosure.of_rel ?_⟩
  exact .inr ⟨(), .inr trivial, 0, by simp [flow], by simp [flow]⟩

/-- At one step the same reader discriminates perfectly, so positive coverage with
zero error is compatible with all the native mechanism premises. -/
theorem correct_answers : read (web false).level = some false ∧
    read (web true).level = some true := ⟨rfl, rfl⟩

/-- Reach alone cannot force evidence to be used: a constant answering rule passes
through the same registration but errs on the true alternative. -/
theorem ignored_signal :
    (∀ l l', (web false).RegistersAlikeUpTo (fun _ _ => True) false l l' 1 →
      (fun _ : Nat → Unit → Nat => some false) l = (fun _ => some false) l') ∧
    wrong true ((fun _ : Nat → Unit → Nat => some false) (web true).level) = 1 :=
  ⟨fun _ _ _ => rfl, rfl⟩

end Witness
end FallibleInquiry
end Becoming
