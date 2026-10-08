import EmbodiedChoiceScales

/-!
One joint history with local material changes, serial signal operations, retained
activity, funded movement and changed contact. This is a conditional mechanism,
not a calibrated worm connectome. Signal gains, regional organization, learning
law, costs and schedule are supplied. There is no primitive external chooser.
-/
namespace OrganizedScaleLoop
open SystemsOrganization

/-- A path is an ordered sequence of local signal transformations. -/
def relay : List Nat → Nat → Nat
  | [], x => x
  | g :: rest, x => relay rest (g * x)

theorem relay_product (gs : List Nat) (x : Nat) : relay gs x = gs.prod * x := by
  induction gs generalizing x with
  | nil => simp [relay]
  | cons g gs ih => simp [relay, ih, Nat.mul_assoc, Nat.mul_comm, Nat.mul_left_comm]

theorem relay_append (a b : List Nat) (x : Nat) :
    relay (a ++ b) x = relay b (relay a x) := by
  induction a generalizing x with
  | nil => rfl
  | cons g a ih => exact ih (g * x)

theorem severed_route (a b : List Nat) (x : Nat) :
    relay (a ++ 0 :: b) x = 0 := by
  simp [relay_product]

/-- Grouping consecutive operations into organs preserves this transmitted
signal; arbitrary grouping or a real cellular correspondence is not asserted. -/
theorem grouped_route (groups : List (List Nat)) (x : Nat) :
    relay groups.flatten x = relay (groups.map List.prod) x := by
  induction groups generalizing x with
  | nil => rfl
  | cons a groups ih =>
      simp only [List.flatten_cons, List.map_cons, relay_append, relay]
      rw [relay_product a, ih]

/-- A locally chosen activity can be compared through an exact description
when both dynamics and the operative selection agree under that description. -/
theorem chosen_step_commutes {S Q A : Type} (f : S → A → S) (g : Q → A → Q)
    (p : S → Q) (choose : S → A) (readChoose : Q → A)
    (dynamics : Commuting f g p) (selection : ∀ s, choose s = readChoose (p s)) :
    Commuting (fun s (_ : Unit) => f s (choose s))
      (fun q (_ : Unit) => g q (readChoose q)) p := by
  intro s _
  rw [dynamics, selection]

/-- Transitions at successive descriptions compose also when the event is
selected within the joint state. All three interface hypotheses are explicit. -/
theorem chosen_history_three_views {S Q R A : Type}
    (f : S → A → S) (g : Q → A → Q) (h : R → A → R)
    (p : S → Q) (q : Q → R) (choose : S → A) (cq : Q → A) (cr : R → A)
    (hp : Commuting f g p) (hq : Commuting g h q)
    (sp : ∀ s, choose s = cq (p s)) (sq : ∀ z, cq z = cr (q z))
    (s : S) (w : List Unit) :
    q (p (evolve (fun s (_ : Unit) => f s (choose s)) s w)) =
      evolve (fun r (_ : Unit) => h r (cr r)) (q (p s)) w := by
  exact evolve_semiconjugacy
    (commuting_composes (chosen_step_commutes f g p choose cq hp sp)
      (chosen_step_commutes g h q cq cr hq sq)) s w

structure Joint where
  anterior : Nat
  posterior : Nat
  patch : Nat
  fuel : Nat
  spent : Nat
  retained : Nat
  contact : Bool
  route : List Nat
  deriving DecidableEq, Repr

/-- Regions belong to the same represented organ through transfer and joint
support in the event law. A sum alone is not the definition of an organ. -/
def burden (s : Joint) : Nat := s.anterior + s.posterior
def material (s : Joint) : Nat := burden s + s.patch
def work (s : Joint) : Nat := s.fuel + s.spent

def ingest (s : Joint) : Joint :=
  if s.contact && decide (0 < s.patch) then
    { s with anterior := s.anterior + 1, patch := s.patch - 1 }
  else s

def transit (s : Joint) : Joint :=
  if 0 < s.anterior then
    { s with anterior := s.anterior - 1, posterior := s.posterior + 1 }
  else s

def release (s : Joint) : Joint :=
  if 0 < s.posterior then
    { s with posterior := s.posterior - 1, patch := s.patch + 1 }
  else s

/-- A supplied cumulative retention law. This is a physical-history register,
not a fitted model of synaptic plasticity or a theorem of consciousness. -/
def acquire (s : Joint) : Joint :=
  if 0 < s.fuel then
    { s with retained := s.retained + relay s.route s.anterior, fuel := s.fuel - 1, spent := s.spent + 1 }
  else s

def withdraw (threshold : Nat) (s : Joint) : Joint :=
  if threshold ≤ s.retained ∧ 0 < s.fuel then
    { s with contact := false, fuel := s.fuel - 1, spent := s.spent + 1 }
  else s

inductive Event where
  | ingest | transit | release | acquire | withdraw
  deriving DecidableEq, Repr

def step (threshold : Nat) (s : Joint) : Event → Joint
  | .ingest => ingest s
  | .transit => transit s
  | .release => release s
  | .acquire => acquire s
  | .withdraw => withdraw threshold s

theorem material_step (θ : Nat) (s : Joint) (e : Event) :
    material (step θ s e) = material s := by
  cases e <;> simp only [step, ingest, transit, release, acquire, withdraw]
  all_goals split
  all_goals simp_all [material, burden]
  all_goals omega

theorem work_step (θ : Nat) (s : Joint) (e : Event) :
    work (step θ s e) = work s := by
  cases e <;> simp only [step, ingest, transit, release, acquire, withdraw]
  all_goals split
  all_goals simp_all [work]
  all_goals omega

theorem finite_history_accounts (θ : Nat) (s : Joint) (w : List Event) :
    material (evolve (step θ) s w) = material s ∧
      work (evolve (step θ) s w) = work s := by
  induction w generalizing s with
  | nil => exact ⟨rfl, rfl⟩
  | cons e w ih =>
      obtain ⟨hm, hw⟩ := ih (step θ s e)
      exact ⟨hm.trans (material_step θ s e), hw.trans (work_step θ s e)⟩

theorem same_core_history (θ : Nat) (s : Joint) (w : List Event) :
    Generative.Trace (deterministic (step θ)) s w (evolve (step θ) s w) :=
  deterministic_trace_iff _ _ _ _ |>.mpr rfl

/-- The macro view omits the individual stages but retains their composed
capacity and the regional distinction needed by this particular response. -/
structure View where
  anterior : Nat
  posterior : Nat
  patch : Nat
  fuel : Nat
  spent : Nat
  retained : Nat
  contact : Bool
  capacity : Nat
  deriving DecidableEq, Repr

def view (s : Joint) : View :=
  ⟨s.anterior, s.posterior, s.patch, s.fuel, s.spent, s.retained,
    s.contact, s.route.prod⟩

def liftView (v : View) : Joint :=
  ⟨v.anterior, v.posterior, v.patch, v.fuel, v.spent, v.retained,
    v.contact, [v.capacity]⟩

/-- Reconstructing a representative is justified by the following commutation
proof, not by assuming every representative has the same behavior. -/
def viewStep (θ : Nat) (v : View) (e : Event) : View :=
  view (step θ (liftView v) e)

theorem concrete_view_commutes (θ : Nat) : Commuting (step θ) (viewStep θ) view := by
  intro s e
  cases e <;> simp only [viewStep, step, ingest, transit, release, acquire, withdraw,
    liftView, view]
  all_goals split_ifs <;> simp_all [view, relay_product]

theorem concrete_view_all_histories (θ : Nat) (s : Joint) (w : List Event) :
    view (evolve (step θ) s w) = evolve (viewStep θ) (view s) w :=
  evolve_semiconjugacy (concrete_view_commutes θ) s w

theorem acquisition_amount (s : Joint) (h : 0 < s.fuel) :
    (acquire s).retained = s.retained + s.route.prod * s.anterior := by
  simp [acquire, h, relay_product]

theorem unsupported_acquisition (s : Joint) (h : s.fuel = 0) : acquire s = s := by
  simp [acquire, h]

theorem acquisition_withdrawal (s : Joint) (θ : Nat)
    (funded : 2 ≤ s.fuel) (elicited : θ ≤ s.retained + s.route.prod * s.anterior) :
    (withdraw θ (acquire s)).contact = false := by
  have hf : 0 < s.fuel := by omega
  have hf' : 0 < s.fuel - 1 := by omega
  simp [withdraw, acquire, hf, hf', relay_product, elicited]

theorem withdrawal_changes_next_exposure (s : Joint) (θ : Nat)
    (funded : 2 ≤ s.fuel) (elicited : θ ≤ s.retained + s.route.prod * s.anterior) :
    ingest (withdraw θ (acquire s)) = withdraw θ (acquire s) := by
  have hc := acquisition_withdrawal s θ funded elicited
  simp [ingest, hc]

/-- A composition of stages with a zero link cannot add a signal in this law. -/
theorem disrupted_acquisition (s : Joint) (a b : List Nat)
    (broken : s.route = a ++ 0 :: b) : (acquire s).retained = s.retained := by
  simp only [acquire]
  split
  · simp [broken, severed_route]
  · rfl

/-- Resources, route and current regional burden do not determine withdrawal
when the continuing effect of prior acquisition has been omitted. -/
def physical (s : Joint) : Nat × Nat × Nat × Nat × Bool × List Nat :=
  (s.anterior, s.posterior, s.patch, s.fuel, s.contact, s.route)

def initial : Joint := ⟨0, 0, 3, 4, 0, 0, true, [1, 1, 1]⟩
def trained : Joint := { initial with retained := 1 }
def broken : Joint := { initial with route := [1, 0, 1] }
def episode : List Event := [.ingest, .acquire, .withdraw, .ingest]

theorem joined_endpoint :
    evolve (step 1) initial episode = ⟨1, 0, 2, 2, 2, 1, false, [1,1,1]⟩ := by
  decide

theorem disrupted_endpoint :
    evolve (step 1) broken episode = ⟨2, 0, 1, 3, 1, 0, true, [1,0,1]⟩ := by
  decide

theorem history_changes_choice : physical initial = physical trained ∧
    (withdraw 1 initial).contact = true ∧ (withdraw 1 trained).contact = false := by
  decide

/-- Witnesses establish failure of these particular coarse descriptions. They
are not alleged counterexamples to a fuller generative ontology. -/
theorem no_memoryless_choice_readout :
    ¬ ∃ predict : (Nat × Nat × Nat × Nat × Bool × List Nat) → Bool, ∀ s : Joint, predict (physical s) = (withdraw 1 s).contact := by
  rintro ⟨predict, hp⟩
  have a := hp initial
  have b := hp trained
  have he := history_changes_choice.1
  rw [← he, ← a] at b
  have bad : true = false := b
  cases bad

def frontLoaded : Joint := { initial with anterior := 1 }
def backLoaded : Joint := { initial with posterior := 1 }

theorem same_organ_amount_distinct_signal :
    burden frontLoaded = burden backLoaded ∧
    (acquire frontLoaded).retained ≠ (acquire backLoaded).retained := by
  decide

theorem no_amount_only_acquisition :
    ¬ ∃ predict : Nat → Nat, ∀ s : Joint, predict (burden s) = (acquire s).retained := by
  rintro ⟨predict, hp⟩
  have h := congrArg predict same_organ_amount_distinct_signal.1
  rw [hp, hp] at h
  exact same_organ_amount_distinct_signal.2 h

theorem support_can_prevent_enactment :
    let s := { frontLoaded with fuel := 1 }
    (acquire s).retained = 1 ∧ (withdraw 1 (acquire s)).contact = true := by
  decide

theorem release_changes_shared_conditions :
    let s := evolve (step 1) initial [.ingest, .transit]
    (release s).patch = s.patch + 1 ∧ (release s).posterior + 1 = s.posterior := by
  decide

end OrganizedScaleLoop

#print axioms OrganizedScaleLoop.relay_product
#print axioms OrganizedScaleLoop.relay_append
#print axioms OrganizedScaleLoop.severed_route
#print axioms OrganizedScaleLoop.grouped_route
#print axioms OrganizedScaleLoop.chosen_step_commutes
#print axioms OrganizedScaleLoop.chosen_history_three_views
#print axioms OrganizedScaleLoop.material_step
#print axioms OrganizedScaleLoop.work_step
#print axioms OrganizedScaleLoop.finite_history_accounts
#print axioms OrganizedScaleLoop.same_core_history
#print axioms OrganizedScaleLoop.concrete_view_commutes
#print axioms OrganizedScaleLoop.concrete_view_all_histories
#print axioms OrganizedScaleLoop.acquisition_amount
#print axioms OrganizedScaleLoop.unsupported_acquisition
#print axioms OrganizedScaleLoop.acquisition_withdrawal
#print axioms OrganizedScaleLoop.withdrawal_changes_next_exposure
#print axioms OrganizedScaleLoop.disrupted_acquisition
#print axioms OrganizedScaleLoop.joined_endpoint
#print axioms OrganizedScaleLoop.disrupted_endpoint
#print axioms OrganizedScaleLoop.history_changes_choice
#print axioms OrganizedScaleLoop.no_memoryless_choice_readout
#print axioms OrganizedScaleLoop.same_organ_amount_distinct_signal
#print axioms OrganizedScaleLoop.no_amount_only_acquisition
#print axioms OrganizedScaleLoop.support_can_prevent_enactment
#print axioms OrganizedScaleLoop.release_changes_shared_conditions
