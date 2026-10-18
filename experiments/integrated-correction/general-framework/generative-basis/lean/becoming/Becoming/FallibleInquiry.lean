import Becoming.Counterfactual
import Becoming.TimedResponse
import Becoming.Imbalance
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
      ∀ c, W.CoupledInto obs h c → W.level 0 c = W'.level 0 c)
    (responds : L.RespondsThroughCoupling L' W W' obs part)
    (read : (Nat → C → Nat) → Option Bool)
    (through : ∀ l l', W.AlikeThroughUpTo obs g l l' t → read l = read l')
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
      ∀ c, W.CoupledInto obs h c → W.level 0 c = W'.level 0 c)
    (responds : L.RespondsThroughCoupling L' W W' obs part)
    (read : (Nat → C → Nat) → Option Bool)
    (through : ∀ l l', W.AlikeThroughUpTo obs g l l' t → read l = read l')
    (different : read W.level ≠ read W'.level) :
    ¬ ¬ L.WithinResponse L' W obs part g :=
  fun beyond => different (answer_alike_beyond_response
    balanced balanced' present start responds read through beyond)

/-- The response premise is derived from the same exchange law in both courses. -/
theorem answer_alike_beyond_law {law : ExchangeLaw F C}
    (balanced : L.Balances W) (balanced' : L'.Balances W')
    (present : ∀ s, L.present s = L'.present s)
    (start : ∀ h, ¬ L.WithinResponse L' W obs part h →
      ∀ c, W.CoupledInto obs h c → W.level 0 c = W'.level 0 c)
    (lawThrough : law.Through W obs part)
    (follows : L.Follows law part W.level) (follows' : L'.Follows law part W'.level)
    (read : (Nat → C → Nat) → Option Bool)
    (through : ∀ l l', W.AlikeThroughUpTo obs g l l' t → read l = read l')
    (beyond : ¬ L.WithinResponse L' W obs part g) :
    read W.level = read W'.level :=
  answer_alike_beyond_response balanced balanced' present start
    (lawThrough.responds follows follows') read through beyond


/-! ## A weaker sufficient mechanism condition: common unaccounted change

Use P59's existing balancing extension, without making the added accounting relatum
an observer. Its exchanges may be nonzero. If they agree between the alternatives,
they cannot introduce a distinction into the region beyond the original reach.
-/

/-- Extend the original registration without registering anything in the accounting
relatum. Existing formations retain exactly the original registration. -/
def observeWithResidual (obs : F → C → Prop) : Option F → C → Prop
  | none, _ => False
  | some h, c => obs h c

/-- The accounting relatum belongs to the compared region, along with its original
members; no new world or original formation is introduced by this region notation. -/
def regionWithResidual (region : F → Prop) : Option F → Prop
  | none => True
  | some h => region h

theorem residual_couples_nothing (c : C) :
    ¬ W.withRefinement.CoupledInto (observeWithResidual obs) none c := by
  intro registers
  rcases registers with ⟨_, impossible⟩ | impossible <;> exact impossible

/-- Every original closed region remains closed after counting an arbitrary
imbalance, when it includes the added relatum but that relatum registers nothing. -/
theorem closed_with_imbalance {region : F → Prop} (V : Web F C)
    (closed : ClosedUnder (L.CoupledFrom W obs) region) :
    ClosedUnder ((L.withImbalance V).CoupledFrom W.withRefinement
      (observeWithResidual obs)) (regionWithResidual region) := by
  intro g h member edge
  cases h with
  | none => exact True.intro
  | some h =>
    rcases edge with ⟨c, registers, t, present, positive⟩
    cases g with
    | none => exact False.elim (residual_couples_nothing c registers)
    | some g =>
      apply closed g h member
      refine ⟨c, registers, t, ?_, positive⟩
      simpa [Flow.withImbalance] using present

/-- The earlier balanced condition is a special case: both accounting residuals
are zero, hence they agree. This reuses P59's exact characterization of balance. -/
theorem common_imbalance_of_balanced
    (balanced : L.Balances W) (balanced' : L'.Balances W') :
    ∀ s c,
      (L.withImbalance W).take s none c = (L'.withImbalance W').take s none c ∧
      (L.withImbalance W).give s none c = (L'.withImbalance W').give s none c :=
  fun s c =>
    have left := Flow.balances_iff_idle.mp balanced s c
    have right := Flow.balances_iff_idle.mp balanced' s c
    ⟨left.2.trans right.2.symm, left.1.trans right.1.symm⟩

/-- Absolute balance is stronger than needed for blindness. The same unaccounted
change in the two courses suffices: after P59 accounts for it, the added relatum
responds alike, and the original closed-region theorem applies. -/
theorem alike_with_common_imbalance
    (present : ∀ s, L.present s = L'.present s)
    (start : ∀ h, ¬ L.WithinResponse L' W obs part h →
      ∀ c, W.CoupledInto obs h c → W.level 0 c = W'.level 0 c)
    (responds : L.RespondsThroughCoupling L' W W' obs part)
    (residual : ∀ s c,
      (L.withImbalance W).take s none c = (L'.withImbalance W').take s none c ∧
      (L.withImbalance W).give s none c = (L'.withImbalance W').give s none c) :
    ∀ s h, ¬ L.WithinResponse L' W obs part h →
      W.AlikeThrough obs h W.level W'.level s := by
  let region : F → Prop := fun h => ¬ L.WithinResponse L' W obs part h
  have closed := Flow.beyond_response_closed (L := L) (L' := L') (W := W)
    (obs := obs) (part := part)
  have common := Flow.alike_within_closed
    (L := L.withImbalance W) (L' := L'.withImbalance W')
    (W := W.withRefinement) (W' := W'.withRefinement)
    (obs := observeWithResidual obs) (region := regionWithResidual region)
    (fun s _ c _ _ => Flow.withImbalance_balancesOn [c] s)
    (fun s _ c _ _ => Flow.withImbalance_balancesOn [c] s)
    (closed_with_imbalance W closed.1) (closed_with_imbalance W' closed.2)
    (fun s => congrArg (fun fs : List F => (none : Option F) :: fs.map some) (present s))
    (by
      intro h member c registers
      cases h with
      | none => exact False.elim (residual_couples_nothing c registers)
      | some h => exact start h member c registers)
    (by
      intro h member s alike g c _ _
      cases h with
      | none => exact residual s c
      | some h => exact responds h (Flow.outside_part_of_beyond_response member) s alike c)
  exact fun s h beyond => common s (some h) beyond

/-- Responses through registration are blind under common, possibly nonzero,
unaccounted change. No reach decision and no absolute balance are assumed. -/
theorem answer_alike_with_common_imbalance
    (present : ∀ s, L.present s = L'.present s)
    (start : ∀ h, ¬ L.WithinResponse L' W obs part h →
      ∀ c, W.CoupledInto obs h c → W.level 0 c = W'.level 0 c)
    (responds : L.RespondsThroughCoupling L' W W' obs part)
    (residual : ∀ s c,
      (L.withImbalance W).take s none c = (L'.withImbalance W').take s none c ∧
      (L.withImbalance W).give s none c = (L'.withImbalance W').give s none c)
    (read : (Nat → C → Nat) → Option Bool)
    (through : ∀ l l', W.AlikeThroughUpTo obs g l l' t → read l = read l')
    (beyond : ¬ L.WithinResponse L' W obs part g) : read W.level = read W'.level :=
  through _ _ fun s _ => alike_with_common_imbalance present start responds residual s g beyond

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
      ∀ c, (web x).CoupledInto (observe x) h c → (web x).level 0 c = (web' x).level 0 c)
    (lawThrough : ∀ x ∈ xs, (law x).Through (web x) (observe x) (vary x))
    (follows : ∀ x ∈ xs, (left x).Follows (law x) (vary x) (web x).level)
    (follows' : ∀ x ∈ xs, (right x).Follows (law x) (vary x) (web' x).level)
    (through : ∀ x ∈ xs, ∀ l l',
      (web x).AlikeThroughUpTo (observe x) (reader x) l l' (time x) → read x l = read x l')

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
theorem error_bounds_require_reach (coverage b0 b1 : Nat)
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

theorem read_through : ∀ l l', (web false).AlikeThroughUpTo
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
    (∀ l l', (web false).AlikeThroughUpTo (fun _ _ => True) false l l' 1 →
      (fun _ : Nat → Unit → Nat => some false) l = (fun _ => some false) l') ∧
    wrong true ((fun _ : Nat → Unit → Nat => some false) (web true).level) = 1 :=
  ⟨fun _ _ _ => rfl, rfl⟩


/-! ## Testing whether balance is necessary for the task or for this description

Keep the very same native level histories and readout. Describing both alternatives
by `flow false` omits the true course's giving. Prediction is unchanged, but the
exchange description no longer explains the change of level. This is a witness
against dropping the balance premise, not a counterexample to the fuller account.
-/

/-- The reduced exchange description contains no exchange at any step. -/
theorem omitted_exchange_none (h : Bool) (c : Unit) : ¬ (flow false).Exchanges h c := by
  rintro ⟨t, _, positive⟩
  simp [flow] at positive

/-- In that reduced description the distinct reader is beyond the varying part's
reach, even though the level histories (and the readout) still distinguish it. -/
theorem omitted_exchange_no_reach :
    ¬ (flow false).WithinResponse (flow false) (web false)
      (fun _ _ => True) (fun h => h) false := by
  rintro ⟨h, member, within⟩
  have impossible : false = true := within (fun k => k = true)
    (fun a _ _ edge => by
      cases edge with
      | inl edge =>
          rcases edge with ⟨c, _, exchange⟩
          exact False.elim (omitted_exchange_none a c exchange)
      | inr edge =>
          rcases edge with ⟨c, _, exchange⟩
          exact False.elim (omitted_exchange_none a c exchange)) member
  exact Bool.noConfusion impossible

/-- The reduced description fails balance on the true history. -/
theorem omitted_exchange_unbalanced : ¬ (flow false).Balances (web true) := by
  intro balances
  have first := balances 0 ()
  simp [web, flow, Flow.taken, Flow.given, total] at first

/-- Even the same rest-law still holds: the missing premise here is not secretly
being repaired by changing the reader's exchange law. -/
theorem omitted_exchange_follows :
    (flow false).Follows law (fun h => h) (web true).level := follows false

/-- The original response and target discrimination survive the omission, while
putting zero for reachable comparisons would make the coverage bound false. -/
theorem omitted_exchange_keeps_task :
    read (web false).level = some false ∧ read (web true).level = some true ∧
    ¬ (committed (read (web false).level) ≤
      wrong false (read (web false).level) + wrong true (read (web true).level) + 0) :=
  ⟨rfl, rfl, Nat.not_succ_le_zero 0⟩

/-- P59 balances both histories by retaining the missing difference as one more
relatum. The original levels and reader are unchanged. -/
theorem counted_residual_balances (b : Bool) :
    ((flow false).withImbalance (web b)).Balances (web b).withRefinement :=
  Flow.withImbalance_balances

/-- The added relatum's first exchange differs despite identical initial levels. -/
theorem counted_residual_differs :
    ((flow false).withImbalance (web false)).give 0 none () = 0 ∧
    ((flow false).withImbalance (web true)).give 0 none () = 1 := ⟨rfl, rfl⟩

/-- If the residual is placed outside the varying part, the response premise fails:
it registers alike initially but gives differently immediately. Balance by accounting
therefore cannot discharge the whole inquiry mechanism without further explanation. -/
theorem counted_residual_not_response :
    ¬ ((flow false).withImbalance (web false)).RespondsThroughCoupling
      ((flow false).withImbalance (web true)) (web false).withRefinement
      (web true).withRefinement (fun _ _ => True)
      (fun h => match h with | none => false | some k => k) := by
  intro responds
  have alike : (web false).withRefinement.AlikeThroughUpTo (fun _ _ => True)
      none (web false).withRefinement.level (web true).withRefinement.level 0 := by
    intro s le
    have zero : s = 0 := Nat.le_zero.mp le
    subst s
    exact ⟨Iff.rfl, fun _ _ => rfl⟩
  have same := (responds none rfl 0 alike ()).2
  exact Nat.noConfusion same

/-- If the residual is counted among the differences, it reaches the reader. The
new accounting relocates the relevant relation; it does not explain it away. -/
theorem counted_residual_reaches :
    ((flow false).withImbalance (web false)).WithinResponse
      ((flow false).withImbalance (web true)) (web false).withRefinement
      (fun _ _ => True) (fun h => match h with | none => true | some k => k) (some false) := by
  refine ⟨none, rfl, WithinClosure.of_rel ?_⟩
  exact .inr ⟨(), .inr trivial, 0, .head _, .inr (Nat.zero_lt_succ 0)⟩

/-- Common unaccounted change is strictly more permissive than balance: this
existing rising history with the exchange omitted has the same nonzero residual
on both sides, although the original exchange description is unbalanced. -/
theorem common_nonzero_imbalance :
    (∀ s c,
      ((flow false).withImbalance (web true)).take s none c =
        ((flow false).withImbalance (web true)).take s none c ∧
      ((flow false).withImbalance (web true)).give s none c =
        ((flow false).withImbalance (web true)).give s none c) ∧
    ¬ (flow false).Balances (web true) ∧
    ((flow false).withImbalance (web true)).give 0 none () = 1 :=
  ⟨fun _ _ => ⟨rfl, rfl⟩, omitted_exchange_unbalanced, rfl⟩

end Witness
end FallibleInquiry
end Becoming

/-! P104: the existing statistical bound now consumes the pure spine's timed
blindness result. This section does not change the historical structural bound.
All mechanism conditions are restricted to the prefix before the answer. -/
namespace Becoming.FallibleInquiry
open Generative.ScientificInquiryNecessity

section TimedWeighted
variable {F C X : Type} (xs : List X) (weight : X → Nat)
    (left right : X → Flow F C) (web web' : X → Web F C)
    (observe : X → F → C → Prop) (source : X → Nat → F → Prop)
    (reader : X → F) (time : X → Nat)
    (read : X → (Nat → C → Nat) → Option Bool)
    [reachDecision : ∀ x, Decidable (TimedResponse.ReachedBy (left x) (right x)
      (web x) (observe x) (source x) (reader x) (time x))]
    (balanced : ∀ x ∈ xs, ∀ t, t < time x → ∀ c,
      (web x).level (t+1) c + (left x).taken t c =
        (web x).level t c + (left x).given t c)
    (balanced' : ∀ x ∈ xs, ∀ t, t < time x → ∀ c,
      (web' x).level (t+1) c + (right x).taken t c =
        (web' x).level t c + (right x).given t c)
    (present : ∀ x ∈ xs, ∀ t, t < time x → (left x).present t = (right x).present t)
    (start : ∀ x ∈ xs, ∀ c, (web x).level 0 c = (web' x).level 0 c)
    (responds : ∀ x ∈ xs, ∀ t, t < time x → ∀ h, ¬ source x t h →
      (web x).AlikeThroughUpTo (observe x) h (web x).level (web' x).level t →
      ∀ c, (left x).take t h c = (right x).take t h c ∧
        (left x).give t h c = (right x).give t h c)
    (through : ∀ x ∈ xs, ∀ l l',
      (web x).AlikeThroughUpTo (observe x) (reader x) l l' (time x) → read x l = read x l')

include balanced balanced' present start responds through

/-- Commitment is at most the two error weights plus timely-route weight.
The pair's target labels and interpretation of weights remain application premises. -/
theorem coverage_le_errors_add_timed_reach :
    tally weight (fun x => committed (read x (web x).level)) xs ≤
      tally weight (fun x => wrong false (read x (web x).level)) xs +
      tally weight (fun x => wrong true (read x (web' x).level)) xs +
      tally weight (fun x => if TimedResponse.ReachedBy (left x) (right x) (web x)
        (observe x) (source x) (reader x) (time x) then 1 else 0) xs := by
  have info := fallible_inquiry_bound xs weight
    (fun x => read x (web x).level) (fun x => read x (web' x).level) (fun _ a => a)
  have bound := tally_mono xs weight
    (fun x => apart (read x (web x).level) (read x (web' x).level))
    (fun x => if TimedResponse.ReachedBy (left x) (right x) (web x)
      (observe x) (source x) (reader x) (time x) then 1 else 0) (by
    intro x mem
    by_cases reached : TimedResponse.ReachedBy (left x) (right x) (web x)
      (observe x) (source x) (reader x) (time x)
    · simp only [if_pos reached, apart]
      split <;> omega
    · have same := TimedResponse.answer_alike_before (balanced x mem) (balanced' x mem)
        (present x mem) (start x mem) (responds x mem) (read x) (through x mem) reached
      simp [apart, same, reached])
  exact Nat.le_trans info (Nat.add_le_add_left bound _)

theorem error_bounds_require_timed_reach (coverage b0 b1 : Nat)
    (hc : coverage ≤ tally weight (fun x => committed (read x (web x).level)) xs)
    (h0 : tally weight (fun x => wrong false (read x (web x).level)) xs ≤ b0)
    (h1 : tally weight (fun x => wrong true (read x (web' x).level)) xs ≤ b1) :
    coverage ≤ b0 + b1 + tally weight (fun x =>
      if TimedResponse.ReachedBy (left x) (right x) (web x) (observe x) (source x)
        (reader x) (time x) then 1 else 0) xs := by
  have bound := coverage_le_errors_add_timed_reach xs weight left right web web' observe source
    reader time read balanced balanced' present start responds through
  omega

omit reachDecision in
/-- If no paired case is reached by its answer time, commitment equals paired error. -/
theorem unreached_in_time_coverage_eq_errors
    (unreached : ∀ x ∈ xs, ¬ TimedResponse.ReachedBy (left x) (right x) (web x)
      (observe x) (source x) (reader x) (time x)) :
    tally weight (fun x => committed (read x (web x).level)) xs =
      tally weight (fun x => wrong false (read x (web x).level)) xs +
      tally weight (fun x => wrong true (read x (web' x).level)) xs := by
  have same : ∀ x ∈ xs, read x (web x).level = read x (web' x).level :=
    fun x mem => TimedResponse.answer_alike_before (balanced x mem) (balanced' x mem)
      (present x mem) (start x mem) (responds x mem) (read x) (through x mem) (unreached x mem)
  have le := tally_mono xs weight
    (fun x => wrong true (read x (web x).level))
    (fun x => wrong true (read x (web' x).level))
    (fun x mem => Nat.le_of_eq (congrArg (wrong true) (same x mem)))
  have ge := tally_mono xs weight
    (fun x => wrong true (read x (web' x).level))
    (fun x => wrong true (read x (web x).level))
    (fun x mem => Nat.le_of_eq (congrArg (wrong true) (same x mem).symm))
  rw [blind_coverage_bound xs weight (fun x => read x (web x).level), Nat.le_antisymm le ge]

end TimedWeighted
end Becoming.FallibleInquiry
