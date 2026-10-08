import Std

/-
Positive chances and a candidate maximization implementation, 8 October 2026.

One jointly supplied opportunity has two routes: A protects two positions,
B protects a different one. In the intended crossed case B's loss is graver;
the equivalent-rescue conditions of BC1 are not being assumed. Every remaining
request gets positive protection probability exactly when both ticket counts
are positive. Permission, timing and reliable implementation are not inferred.

The tested public score is expected protected headcount. It is NOT our ethical
utility, a severity scale, or a consequence of CP. The point is to audit the
proposal to add only strict positivity to this maximization objective.
Unbounded refinement and fixed ticket resolution are separate supplied domains.
Nothing here derives a fair lower bound, proves CP inconsistent, or requires
arbitrarily fine physical randomization.
-/
namespace ChanceGrounding

abbrev Tickets := Nat × Nat

def Positive (t : Tickets) : Prop := 0 < t.1 ∧ 0 < t.2

def total (t : Tickets) : Nat := t.1 + t.2

/-- Dividing by the positive total gives the candidate expected headcount. -/
def scoreNumerator (t : Tickets) : Nat := 2 * t.1 + t.2

/-- Strict comparison by cross multiplication, used only with positive totals. -/
def Improves (before after : Tickets) : Prop :=
  scoreNumerator before * total after < scoreNumerator after * total before

def refine (t : Tickets) : Tickets := (2 * t.1 + t.2, t.2)

/-- The B-ticket numerator is unchanged while the denominator doubles. -/
theorem positive_refinement_improves_score (t : Tickets) (h : Positive t) :
    Positive (refine t) ∧ total (refine t) = 2 * total t ∧
    (refine t).2 = t.2 ∧ Improves t (refine t) := by
  have hTotal : 0 < total t := by
    unfold Positive at h
    unfold total
    omega
  have totalEq : total (refine t) = 2 * total t := by
    unfold total refine
    omega
  have scoreEq : scoreNumerator (refine t) = 2 * scoreNumerator t + t.2 := by
    unfold scoreNumerator refine
    omega
  have positive : Positive (refine t) := by
    unfold Positive refine at *
    omega
  refine ⟨positive, totalEq, rfl, ?_⟩
  unfold Improves
  rw [totalEq, scoreEq, Nat.add_mul]
  have productPositive : 0 < t.2 * total t := Nat.mul_pos h.2 hTotal
  have rearrange : scoreNumerator t * (2 * total t) =
      (2 * scoreNumerator t) * total t := by
    rw [← Nat.mul_assoc, Nat.mul_comm (scoreNumerator t) 2]
  rw [rearrange]
  omega

/-- No maximizer exists in the domain admitting every positive natural ticket
pair and its refinement. This does not concern a fixed physical resolution. -/
theorem no_maximum_in_unbounded_positive_ticket_domain :
    ¬ ∃ best : Tickets, Positive best ∧
      ∀ alternative, Positive alternative → ¬ Improves best alternative := by
  rintro ⟨best, positive, maximal⟩
  obtain ⟨positive', _, _, better⟩ := positive_refinement_improves_score best positive
  exact maximal (refine best) positive' better

theorem every_positive_score_is_below_two (t : Tickets) (h : Positive t) :
    scoreNumerator t < 2 * total t := by
  unfold scoreNumerator total
  unfold Positive at h
  omega

/-- At fixed resolution, the unique maximum leaves B exactly one ticket.
That ticket's probability 1/n is imposed by this representation and objective,
not certified as adequate or fair by the theorem. -/
theorem fixed_resolution_unique_maximum (n : Nat) (hn : 2 ≤ n) :
    Positive (n - 1, 1) ∧ total (n - 1, 1) = n ∧
    ∀ t : Tickets, Positive t → total t = n →
      scoreNumerator t ≤ scoreNumerator (n - 1, 1) ∧
      (scoreNumerator t = scoreNumerator (n - 1, 1) ↔ t = (n - 1, 1)) := by
  constructor
  · unfold Positive
    omega
  constructor
  · unfold total
    omega
  intro t ht hTotal
  rcases t with ⟨a, b⟩
  unfold Positive at ht
  unfold total at hTotal
  unfold scoreNumerator
  constructor
  · omega
  · constructor
    · intro equal
      have ha : a = n - 1 := by omega
      have hb : b = 1 := by omega
      simp [ha, hb]
    · intro equal
      cases equal
      rfl

end ChanceGrounding
