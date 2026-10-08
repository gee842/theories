import RelationsAcrossScales

/-! Choice and action are relations inside the process being described.
The metric theorem separates state error from changed action effects. The
finite witness is an idealized acquired-signal/choice/shared-support episode,
not a physiological fit or an origin theorem for cognition. -/
namespace EmbodiedChoiceScales

noncomputable section

variable {X Y A : Type} [PseudoMetricSpace Y]

theorem controlled_one_step (p nextP : X → Y)
    (F : X → A → X) (G : Y → A → Y) (x : X) (y : Y) (a b : A)
    (L ε σ : ℝ)
    (defect : dist (nextP (F x a)) (G (p x) a) ≤ ε)
    (propagation : dist (G (p x) a) (G y a) ≤ L * dist (p x) y)
    (changedAction : dist (G y a) (G y b) ≤ σ) :
    dist (nextP (F x a)) (G y b) ≤ ε + L * dist (p x) y + σ := by
  exact (dist_triangle _ _ _).trans
    (add_le_add ((dist_triangle _ _ _).trans (add_le_add defect propagation)) changedAction)

/-- Policies may use retained cognitive relations in the respective states.
The error caused by distinct selected actions cannot silently be set to zero. -/
theorem closed_loop_horizon (p : ℕ → X → Y)
    (F : ℕ → X → A → X) (G : ℕ → Y → A → Y)
    (act : ℕ → X → A) (representAct : ℕ → Y → A)
    (x : ℕ → X) (y : ℕ → Y) (L ε σ : ℕ → ℝ) (initial : ℝ) (N : ℕ)
    (hx : ∀ t < N, x (t+1) = F t (x t) (act t (x t)))
    (hy : ∀ t < N, y (t+1) = G t (y t) (representAct t (y t)))
    (h0 : dist (p 0 (x 0)) (y 0) ≤ initial)
    (hL : ∀ t < N, 0 ≤ L t)
    (hd : ∀ t < N, dist (p (t+1) (F t (x t) (act t (x t))))
      (G t (p t (x t)) (act t (x t))) ≤ ε t)
    (hp : ∀ t < N, dist (G t (p t (x t)) (act t (x t)))
      (G t (y t) (act t (x t))) ≤ L t * dist (p t (x t)) (y t))
    (ha : ∀ t < N, dist (G t (y t) (act t (x t)))
      (G t (y t) (representAct t (y t))) ≤ σ t) :
    ∀ n ≤ N, dist (p n (x n)) (y n) ≤
      RelationsAcrossScales.budget L (fun t => ε t + σ t) initial n := by
  intro n hn
  induction n with
  | zero => exact h0
  | succ n ih =>
    have ht : n < N := by omega
    have prev := ih (by omega)
    rw [hx n ht, hy n ht]
    have step := controlled_one_step (p n) (p (n+1)) (F n) (G n)
      (x n) (y n) (act n (x n)) (representAct n (y n))
      (L n) (ε n) (σ n) (hd n ht) (hp n ht) (ha n ht)
    have scaled := mul_le_mul_of_nonneg_left prev (hL n ht)
    simp only [RelationsAcrossScales.budget]
    linarith

theorem equal_actions_remove_action_error (G : Y → A → Y) (y : Y) {a b : A}
    (equal : a = b) : dist (G y a) (G y b) = 0 := by simp [equal]

def choose (threshold score : ℝ) : Bool := decide (threshold ≤ score)

theorem upper_margin_preserves_choice (actual estimate error threshold : ℝ)
    (he : 0 ≤ error) (calibrated : |actual - estimate| ≤ error)
    (margin : threshold + error ≤ estimate) :
    choose threshold actual = true ∧ choose threshold estimate = true := by
  have low := (abs_le.mp calibrated).1
  have ha : threshold ≤ actual := by linarith
  have hy : threshold ≤ estimate := by linarith
  simp [choose, ha, hy]

theorem lower_margin_preserves_choice (actual estimate error threshold : ℝ)
    (he : 0 ≤ error) (calibrated : |actual - estimate| ≤ error)
    (margin : estimate + error < threshold) :
    choose threshold actual = false ∧ choose threshold estimate = false := by
  have high := (abs_le.mp calibrated).2
  have ha : ¬ threshold ≤ actual := by linarith
  have hy : ¬ threshold ≤ estimate := by linarith
  simp [choose, ha, hy]

def effect (a : Bool) : ℝ := if a then 1 else 0

/-- Arbitrarily close scores on opposite sides can select unit-separated
effects. Accuracy of a state estimate alone does not preserve chosen action. -/
theorem arbitrarily_small_score_error_changes_effect (δ : ℝ) (hδ : 0 < δ) :
    |(-δ) - δ| = 2 * δ ∧
    choose 0 (-δ) = false ∧ choose 0 δ = true ∧
    |effect (choose 0 (-δ)) - effect (choose 0 δ)| = 1 := by
  have hn : ¬ (0 : ℝ) ≤ -δ := by linarith
  have hp : (0 : ℝ) ≤ δ := le_of_lt hδ
  have habs : |(-δ) - δ| = 2 * δ := by
    rw [abs_of_nonpos (by linarith)]
    ring
  refine ⟨habs, ?_, ?_, ?_⟩ <;> simp [choose, hn, hp, effect]

end

/-! One shared history, with differentiated stores, sensing and retention.
All quantities count the same abstract support units. No biological energy
conversion rate, time scale, sensor genesis or welfare value is inferred. -/

structure Episode where
  bodily : Nat
  otherLiving : Nat
  shared : Nat
  sensor : Bool
  retained : Bool
  deriving DecidableEq, Repr

inductive Activity where
  | sense
  | otherConsumes
  | respond
  deriving DecidableEq, Repr

def signal (s : Episode) : Bool := s.sensor && decide (0 < s.shared)
def choice (s : Episode) : Bool := s.retained
def total (s : Episode) : Nat := s.bodily + s.otherLiving + s.shared

def evolve (s : Episode) (event : Activity) : Episode :=
  match event with
  | .sense => {s with retained := signal s}
  | .otherConsumes =>
      if 0 < s.shared then {s with otherLiving := s.otherLiving + 1, shared := s.shared - 1}
      else s
  | .respond =>
      if choice s = true ∧ 0 < s.shared then
        {s with bodily := s.bodily + 1, shared := s.shared - 1, retained := false}
      else {s with retained := false}

def process : Generative.Process Episode Activity where
  step s a t := t = evolve s a

def history : Episode → List Activity → Episode
  | s, [] => s
  | s, a :: rest => history (evolve s a) rest

theorem computed_history_is_actual (s : Episode) (word : List Activity) :
    Generative.Trace process s word (history s word) := by
  induction word generalizing s with
  | nil => exact .nil s
  | cons a rest ih => exact .cons rfl (ih _)

theorem event_conserves_shared_support (s : Episode) (a : Activity) :
    total (evolve s a) = total s := by
  cases a with
  | sense => rfl
  | otherConsumes =>
    simp only [evolve]
    split
    · simp only [total]; omega
    · rfl
  | respond =>
    simp only [evolve]
    split
    · rename_i h
      simp only [total]
      omega
    · rfl

theorem history_conserves_shared_support (s : Episode) (word : List Activity) :
    total (history s word) = total s := by
  induction word generalizing s with
  | nil => rfl
  | cons a rest ih => exact (ih _).trans (event_conserves_shared_support s a)

def start : Episode := ⟨0, 0, 1, true, false⟩
def clamped : Episode := {start with sensor := false}

theorem acquired_signal_selects_effective_activity :
    choice (evolve start .sense) = true ∧
    (history start [.sense, .respond]).bodily = 1 ∧
    (history start [.sense, .respond]).shared = 0 := by decide

theorem sensory_intervention_changes_choice_and_effect :
    total clamped = total start ∧
    choice (evolve clamped .sense) = false ∧
    (history clamped [.sense, .respond]).bodily = 0 ∧
    (history clamped [.sense, .respond]).shared = 1 := by decide

/-- The same body amount does not determine the retained cognitive state. -/
theorem bodily_amount_does_not_determine_choice :
    (evolve start .sense).bodily = (evolve clamped .sense).bodily ∧
    choice (evolve start .sense) ≠ choice (evolve clamped .sense) := by decide

/-- Another living participant changes shared availability after sensing;
retained evidence and chosen attempt can outlast its material opportunity. -/
theorem intervening_participation_defeats_retained_plan :
    choice (history start [.sense, .otherConsumes]) = true ∧
    (history start [.sense, .otherConsumes]).shared = 0 ∧
    (history start [.sense, .otherConsumes, .respond]).bodily = 0 ∧
    (history start [.sense, .otherConsumes, .respond]).otherLiving = 1 ∧
    choice (history start [.sense, .otherConsumes, .respond]) = false := by decide

theorem response_does_not_create_unavailable_support (s : Episode)
    (empty : s.shared = 0) : (evolve s .respond).bodily = s.bodily := by
  simp [evolve, empty]

end EmbodiedChoiceScales

#print axioms EmbodiedChoiceScales.controlled_one_step
#print axioms EmbodiedChoiceScales.closed_loop_horizon
#print axioms EmbodiedChoiceScales.equal_actions_remove_action_error
#print axioms EmbodiedChoiceScales.upper_margin_preserves_choice
#print axioms EmbodiedChoiceScales.lower_margin_preserves_choice
#print axioms EmbodiedChoiceScales.arbitrarily_small_score_error_changes_effect
#print axioms EmbodiedChoiceScales.computed_history_is_actual
#print axioms EmbodiedChoiceScales.event_conserves_shared_support
#print axioms EmbodiedChoiceScales.history_conserves_shared_support
#print axioms EmbodiedChoiceScales.acquired_signal_selects_effective_activity
#print axioms EmbodiedChoiceScales.sensory_intervention_changes_choice_and_effect
#print axioms EmbodiedChoiceScales.bodily_amount_does_not_determine_choice
#print axioms EmbodiedChoiceScales.intervening_participation_defeats_retained_plan
#print axioms EmbodiedChoiceScales.response_does_not_create_unavailable_support
