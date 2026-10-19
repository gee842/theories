import Becoming.Frame

/-!
# Strict transport: what a supplied comparison carries along a weak one

`Le a b` is a **supplied** comparison of configurations or histories: `b` is at least as well
supported as `a`. It is a hypothesis of every theorem here, never asserted: not feasibility, not
preference, not a measured score. `Strict Le a b` is `Le a b` without `Le b a`. Board item F3R
(18 October 2026) states here, on the core and constructively, what `GenerativeLossComparison`
(8 October) proved of such an order and what the join `StrictTransportRuns` (17 October) read
along runs.

* **Transport.** For a transitive comparison, a strict anchor is carried by every weak step on
  its upper side (`strict_above_trans`) and every weak step on its lower side
  (`strict_below_trans`); so a relation compatible with the comparison (each of its pairs weakly
  comparable) carries strict anchors (`strict_above_of_compatible`, `strict_below_of_compatible`),
  a supplied link from strict comparison to reason gives the reason for the transported pair
  (`reason_of_strict_above`), and a faithful redescription keeps strictness
  (`strict_iff_of_faithful`).
* **Along runs.** A strict anchor holds along a run that loses no claim and a strict rejection
  along a run that gains none, wherever keeping every claim is weakly comparable
  (`strict_above_along`, `strict_below_along`); strict comparison among configurations reachable
  from one supplies a reason where the link is supplied (`reachable_reason`).
* **Weaker rules, audited.** On `Route` (finishing or a repair after an interruption of length
  `n`), a cutoff order is transitive and prefers shorter interruptions (`cutoff_transitive`,
  `shorter_interruption_no_worse`); it prefers repair exactly below its cutoff and finishing
  exactly above (`cutoff_priority_iff`, `cutoff_rejection_iff`), so two compatible cutoffs
  disagree (`cutoffs_disagree`) and a good anchor licenses no longer interruption
  (`anchor_licenses_no_longer_repair`). The lexicographic rival that puts finishing first is
  transitive, still prefers shorter interruptions, puts finishing above every repair, and so
  supplies no cutoff (`continuation_first_transitive`, `continuation_first_prefers_shorter`,
  `continuation_first_above_every`, `continuation_first_no_cutoff`).

These are transport results for already supplied comparisons. They do not establish a first
mixed comparison, a loss exchange rate or a threshold; completeness and utility representation
are not assumed. Every declaration has an empty axiom report.
-/

namespace Becoming

open Generative

universe u v w

namespace StrictTransport

/-- `b` is strictly better supported than `a` under the supplied comparison. -/
def Strict {H : Type u} (Le : H → H → Prop) (a b : H) : Prop := Le a b ∧ ¬ Le b a

/-- The supplied comparison is transitive. -/
def Transitive {H : Type u} (Le : H → H → Prop) : Prop := ∀ a b c, Le a b → Le b c → Le a c

/-- Each pair of a relation is weakly comparable. -/
def Compatible {H : Type u} (NoWorse Le : H → H → Prop) : Prop := ∀ a b, NoWorse a b → Le a b

/-! ## Transport -/

theorem strict_above_trans {H : Type u} {Le : H → H → Prop} (trans : Transitive Le)
    {baseline original improved : H} (anchor : Strict Le baseline original)
    (improvement : Le original improved) : Strict Le baseline improved :=
  ⟨trans _ _ _ anchor.1 improvement, fun back => anchor.2 (trans _ _ _ improvement back)⟩

theorem strict_below_trans {H : Type u} {Le : H → H → Prop} (trans : Transitive Le)
    {baseline original worsened : H} (anchor : Strict Le original baseline)
    (worsening : Le worsened original) : Strict Le worsened baseline :=
  ⟨trans _ _ _ worsening anchor.1, fun back => anchor.2 (trans _ _ _ back worsening)⟩

theorem strict_above_of_compatible {H : Type u} {Le NoWorse : H → H → Prop}
    (trans : Transitive Le) (comparison : Compatible NoWorse Le) {baseline original reduced : H}
    (anchor : Strict Le baseline original) (matched : NoWorse original reduced) :
    Strict Le baseline reduced :=
  strict_above_trans trans anchor (comparison _ _ matched)

theorem strict_below_of_compatible {H : Type u} {Le NoWorse : H → H → Prop}
    (trans : Transitive Le) (comparison : Compatible NoWorse Le) {baseline original increased : H}
    (anchor : Strict Le original baseline) (matched : NoWorse increased original) :
    Strict Le increased baseline :=
  strict_below_trans trans anchor (comparison _ _ matched)

/-- A supplied link: strict comparison of the realizations of two feasible options gives a
reason between them. -/
def SuppliesReason {H : Type u} {O : Type v} (Le : H → H → Prop) (feasible : O → Prop)
    (realize : O → H) (Reason : O → O → Prop) : Prop :=
  ∀ a b, feasible a → feasible b → Strict Le (realize a) (realize b) → Reason a b

theorem reason_of_strict_above {H : Type u} {O : Type v} {Le : H → H → Prop}
    {feasible : O → Prop} {realize : O → H} {Reason : O → O → Prop} (trans : Transitive Le)
    (link : SuppliesReason Le feasible realize Reason) {baseline original improved : O}
    (fb : feasible baseline) (fi : feasible improved)
    (anchor : Strict Le (realize baseline) (realize original))
    (improvement : Le (realize original) (realize improved)) : Reason baseline improved :=
  link _ _ fb fi (strict_above_trans trans anchor improvement)

/-- **A faithful redescription keeps strictness.** -/
theorem strict_iff_of_faithful {H : Type u} {J : Type v} {Le : H → H → Prop} {Le' : J → J → Prop}
    (f : H → J) (faithful : ∀ a b, Le' (f a) (f b) ↔ Le a b) (a b : H) :
    Strict Le' (f a) (f b) ↔ Strict Le a b :=
  ⟨fun ⟨forward, back⟩ => ⟨(faithful a b).mp forward, fun h => back ((faithful b a).mpr h)⟩,
   fun ⟨forward, back⟩ => ⟨(faithful a b).mpr forward, fun h => back ((faithful b a).mp h)⟩⟩

/-! ## Along runs -/

variable {S : Type u} {A : Type v} {C : Type w}

/-- **A strict anchor holds along a run that loses no claim**, where keeping every claim is
weakly comparable. -/
theorem strict_above_along {F : Frame S A C} {Le : S → S → Prop} (trans : Transitive Le)
    (compatible : Compatible (fun s t => ∀ c, F.realized s c → F.realized t c) Le)
    (r : Run F.P) {baseline : S} (anchor : Strict Le baseline (r.state 0))
    (keeps : ∀ n c, F.realized (r.state n) c → F.realized (r.state (n + 1)) c) :
    ∀ n, Strict Le baseline (r.state n)
  | 0 => anchor
  | n + 1 => strict_above_of_compatible trans compatible
      (strict_above_along trans compatible r anchor keeps n) (keeps n)

/-- **A strict rejection holds along a run that gains no claim**, where keeping every claim is
weakly comparable. -/
theorem strict_below_along {F : Frame S A C} {Le : S → S → Prop} (trans : Transitive Le)
    (compatible : Compatible (fun s t => ∀ c, F.realized s c → F.realized t c) Le)
    (r : Run F.P) {baseline : S} (anchor : Strict Le (r.state 0) baseline)
    (gainsNone : ∀ n c, F.realized (r.state (n + 1)) c → F.realized (r.state n) c) :
    ∀ n, Strict Le (r.state n) baseline
  | 0 => anchor
  | n + 1 => strict_below_of_compatible trans compatible
      (strict_below_along trans compatible r anchor gainsNone n) (gainsNone n)

/-! ## Weaker rules, audited -/

/-- Finishing, or a repair after an interruption of the given length. -/
inductive Route where
  | finish
  | repair (interruption : Nat)
  deriving DecidableEq

/-- An at-least-as-supported order with a supplied cutoff. -/
def Cutoff (k : Nat) : Route → Route → Prop
  | .finish, .finish => True
  | .finish, .repair n => n ≤ k
  | .repair n, .finish => k ≤ n
  | .repair n, .repair m => m ≤ n

theorem cutoff_transitive (k : Nat) : Transitive (Cutoff k)
  | .finish, .finish, .finish, _, _ => trivial
  | .finish, .finish, .repair _, _, bc => bc
  | .finish, .repair _, .finish, _, _ => trivial
  | .finish, .repair _, .repair _, ab, bc => Nat.le_trans bc ab
  | .repair _, .finish, .finish, ab, _ => ab
  | .repair _, .finish, .repair _, ab, bc => Nat.le_trans bc ab
  | .repair _, .repair _, .finish, ab, bc => Nat.le_trans bc ab
  | .repair _, .repair _, .repair _, ab, bc => Nat.le_trans bc ab

theorem shorter_interruption_no_worse (k n m : Nat) (h : m ≤ n) : Cutoff k (.repair n) (.repair m) :=
  h

theorem cutoff_priority_iff (k n : Nat) : Strict (Cutoff k) .finish (.repair n) ↔ n < k :=
  ⟨fun h => Nat.gt_of_not_le h.2, fun h => ⟨Nat.le_of_lt h, Nat.not_le_of_gt h⟩⟩

theorem cutoff_rejection_iff (k n : Nat) : Strict (Cutoff k) (.repair n) .finish ↔ k < n :=
  ⟨fun h => Nat.gt_of_not_le h.2, fun h => ⟨Nat.le_of_lt h, Nat.not_le_of_gt h⟩⟩

theorem cutoffs_disagree : Strict (Cutoff 2) (.repair 4) .finish ∧ Strict (Cutoff 6) .finish (.repair 4) :=
  ⟨(cutoff_rejection_iff 2 4).mpr (by decide), (cutoff_priority_iff 6 4).mpr (by decide)⟩

theorem anchor_licenses_no_longer_repair :
    Strict (Cutoff 2) .finish (.repair 1) ∧ Strict (Cutoff 2) (.repair 4) .finish :=
  ⟨(cutoff_priority_iff 2 1).mpr (by decide), (cutoff_rejection_iff 2 4).mpr (by decide)⟩

/-- The lexicographic rival that puts finishing first; allowed by the weak rules, not endorsed. -/
def ContinuationFirst : Route → Route → Prop
  | .finish, .finish => True
  | .finish, .repair _ => True
  | .repair _, .finish => False
  | .repair n, .repair m => m ≤ n

theorem continuation_first_transitive : Transitive ContinuationFirst
  | .finish, .finish, .finish, _, _ => trivial
  | .finish, .finish, .repair _, _, _ => trivial
  | .finish, .repair _, .finish, _, _ => trivial
  | .finish, .repair _, .repair _, _, _ => trivial
  | .repair _, .finish, _, ab, _ => ab.elim
  | .repair _, .repair _, .finish, _, bc => bc
  | .repair _, .repair _, .repair _, ab, bc => Nat.le_trans bc ab

theorem continuation_first_prefers_shorter (n m : Nat) (h : m < n) :
    Strict ContinuationFirst (.repair n) (.repair m) :=
  ⟨Nat.le_of_lt h, Nat.not_le_of_gt h⟩

theorem continuation_first_above_every (n : Nat) : Strict ContinuationFirst .finish (.repair n) :=
  ⟨trivial, fun h => h⟩

theorem continuation_first_no_cutoff :
    ¬ ∃ k, ∀ n, k < n → Strict ContinuationFirst (.repair n) .finish
  | ⟨k, bound⟩ => (bound (k + 1) (Nat.lt_succ_self k)).1

end StrictTransport

end Becoming
