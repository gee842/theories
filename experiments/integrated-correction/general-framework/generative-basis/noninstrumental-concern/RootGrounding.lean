import GroundingContract

/-!
An elimination audit, not a new ethical axiom or a new helping controller.
For a fixed patient event, universal eligible-operator reasons are exactly
event-anchor coverage plus eligible-operator locality. Replacing C2 by the
two conjuncts therefore relocates rather than discharges its normative content.
The final adapter uses the existing costed process without modifying it.
-/
namespace NoninstrumentalConcern.RootGrounding

variable {Context Actor : Type}

def UniversalReason (Bad : Context → Prop)
    (Can Reason : Context → Actor → Prop) : Prop :=
  ∀ c a, Bad c → Can c a → Reason c a

def EventAnchors (Bad : Context → Prop)
    (Can Reason : Context → Actor → Prop) : Prop :=
  ∀ c, Bad c → (∃ a, Can c a) → ∃ a, Can c a ∧ Reason c a

def OperatorLocality (Bad : Context → Prop)
    (Can Reason : Context → Actor → Prop) : Prop :=
  ∀ c a b, Bad c → Can c a → Can c b → (Reason c a ↔ Reason c b)

theorem universal_gives_anchors {Bad : Context → Prop}
    {Can Reason : Context → Actor → Prop} (h : UniversalReason Bad Can Reason) :
    EventAnchors Bad Can Reason := by
  rintro c hb ⟨a,ha⟩
  exact ⟨a,ha,h c a hb ha⟩

theorem universal_gives_locality {Bad : Context → Prop}
    {Can Reason : Context → Actor → Prop} (h : UniversalReason Bad Can Reason) :
    OperatorLocality Bad Can Reason := by
  intro c a b hb ha hc
  exact ⟨fun _ => h c b hb hc, fun _ => h c a hb ha⟩

theorem anchors_and_locality_give_universal {Bad : Context → Prop}
    {Can Reason : Context → Actor → Prop}
    (anchor : EventAnchors Bad Can Reason)
    (locality : OperatorLocality Bad Can Reason) :
    UniversalReason Bad Can Reason := by
  intro c a hb ha
  obtain ⟨b,hbcan,hbr⟩ := anchor c hb ⟨a,ha⟩
  exact (locality c b a hb hbcan ha).mp hbr

theorem universal_iff_anchors_and_locality {Bad : Context → Prop}
    {Can Reason : Context → Actor → Prop} :
    UniversalReason Bad Can Reason ↔
      EventAnchors Bad Can Reason ∧ OperatorLocality Bad Can Reason := by
  exact ⟨fun h => ⟨universal_gives_anchors h,universal_gives_locality h⟩,
    fun h => anchors_and_locality_give_universal h.1 h.2⟩

/- Factorization says that the reason on the declared domain is a function
   of the fixed event alone. Its positive value is a separate requirement. -/
def FactorsThroughEvent (Bad : Context → Prop)
    (Can Reason : Context → Actor → Prop) : Prop :=
  ∃ support : Context → Prop,
    ∀ c a, Bad c → Can c a → (Reason c a ↔ support c)

theorem factorization_gives_locality {Bad : Context → Prop}
    {Can Reason : Context → Actor → Prop}
    (h : FactorsThroughEvent Bad Can Reason) :
    OperatorLocality Bad Can Reason := by
  obtain ⟨support,hs⟩ := h
  intro c a b hb ha hc
  exact (hs c a hb ha).trans (hs c b hb hc).symm

theorem locality_gives_factorization {Bad : Context → Prop}
    {Can Reason : Context → Actor → Prop}
    (h : OperatorLocality Bad Can Reason) :
    FactorsThroughEvent Bad Can Reason := by
  refine ⟨fun c => ∃ a, Can c a ∧ Reason c a, ?_⟩
  intro c a hb ha
  constructor
  · intro hr
    exact ⟨a,ha,hr⟩
  · rintro ⟨b,hbcan,hbr⟩
    exact (h c b a hb hbcan ha).mp hbr

theorem factorization_iff_locality {Bad : Context → Prop}
    {Can Reason : Context → Actor → Prop} :
    FactorsThroughEvent Bad Can Reason ↔ OperatorLocality Bad Can Reason :=
  ⟨factorization_gives_locality,locality_gives_factorization⟩

theorem zero_reasons_factor (Bad : Context → Prop)
    (Can : Context → Actor → Prop) :
    FactorsThroughEvent Bad Can (fun _ _ => False) := by
  exact ⟨fun _ => False,fun _ _ _ _ => Iff.rfl⟩

theorem zero_reasons_lack_anchor {Bad : Context → Prop}
    {Can : Context → Actor → Prop} (c : Context) (a : Actor)
    (hb : Bad c) (ha : Can c a) :
    ¬ EventAnchors Bad Can (fun _ _ => False) := by
  intro h
  obtain ⟨_,_,hf⟩ := h c hb ⟨a,ha⟩
  exact hf

/- A historical relation can select reasons without an ungenerated owner
   variable. Reindexing the whole history preserves it. This is not a proof
   that such a selector is ethically justified or derived from physics. -/
def Linked {A P : Type} (history : List (A × P)) (a : A) (p : P) : Prop :=
  (a,p) ∈ history

def reindexHistory {A P A' P' : Type} (f : A → A') (g : P → P')
    (history : List (A × P)) : List (A' × P') :=
  history.map (fun ap => (f ap.1,g ap.2))

theorem historical_link_covariant {A P A' P' : Type}
    (f : A → A') (g : P → P') (hf : Function.Injective f)
    (hg : Function.Injective g) (history : List (A × P)) (a : A) (p : P) :
    Linked (reindexHistory f g history) (f a) (g p) ↔ Linked history a p := by
  unfold Linked reindexHistory
  rw [List.mem_map]
  constructor
  · rintro ⟨⟨b,q⟩,hmem,heq⟩
    have hab : b = a := hf (congrArg Prod.fst heq)
    have hpq : q = p := hg (congrArg Prod.snd heq)
    subst b
    subst q
    exact hmem
  · intro hm
    exact ⟨(a,p),hm,rfl⟩

theorem linked_after_append {A P : Type} (history : List (A × P))
    (a : A) (p : P) : Linked (history ++ [(a,p)]) a p := by
  simp [Linked]

def diagonalHistory : List (Bool × Bool) := [(false,false),(true,true)]
def historicalReason (p a : Bool) : Prop := Linked diagonalHistory a p

/- This supplied formation law records relations; it is not a derivation
   of the law, living organization, experienced ownership, or ethical validity. -/
def recordProcess (A P : Type) : Generative.Process (List (A × P)) (A × P) where
  step history event next := next = history ++ [event]

theorem no_historical_link_at_origin {A P : Type} (a : A) (p : P) :
    ¬ Linked ([] : List (A × P)) a p := by
  simp [Linked]

theorem diagonal_history_forms_by_actual_trace :
    Generative.Trace (recordProcess Bool Bool) []
      [(false,false),(true,true)] diagonalHistory := by
  exact .cons rfl (.cons rfl (.nil diagonalHistory))

theorem history_all_events_anchored :
    EventAnchors (fun _ : Bool => True) (fun _ _ : Bool => True) historicalReason := by
  intro p _ _
  refine ⟨p,trivial,?_⟩
  cases p <;> simp [historicalReason,Linked,diagonalHistory]

theorem history_fixed_event_operator_substitution_fails :
    ¬ OperatorLocality (fun _ : Bool => True)
      (fun _ _ : Bool => True) historicalReason := by
  intro h
  have hr : historicalReason false false := by
    simp [historicalReason,Linked,diagonalHistory]
  have hn : ¬ historicalReason false true := by
    simp [historicalReason,Linked,diagonalHistory]
  exact hn ((h false false true trivial trivial trivial).mp hr)

theorem history_simultaneous_swap_preserves_reason (p a : Bool) :
    historicalReason (!p) (!a) ↔ historicalReason p a := by
  cases p <;> cases a <;> simp [historicalReason,Linked,diagonalHistory]

/- The second event is never in an actor's own-case image. All eligible
   operators agree, but their agreement does not manufacture its first anchor. -/
def silentPatientReason (p : Bool) (_a : Unit) : Prop := p = false
def ownPatient (_a : Unit) : Bool := false

theorem never_agent_patient_not_in_own_image (a : Unit) : ownPatient a ≠ true := by
  simp [ownPatient]

theorem silent_patient_locality :
    OperatorLocality (fun _ : Bool => True)
      (fun _ : Bool => fun _ : Unit => True) silentPatientReason := by
  intro _ _ _ _ _ _
  exact Iff.rfl

theorem silent_patient_own_anchor : silentPatientReason false () := rfl

theorem silent_patient_no_reason : ¬ silentPatientReason true () := by
  simp [silentPatientReason]

theorem silent_patient_not_covered :
    ¬ EventAnchors (fun _ : Bool => True)
      (fun _ : Bool => fun _ : Unit => True) silentPatientReason := by
  intro h
  obtain ⟨a,_,hr⟩ := h true trivial ⟨(),trivial⟩
  exact Bool.noConfusion hr

/- Direct audit of the existing C2. A response instance is a state and its
   patient index. Substitution stays in one PatientCondition fiber. These are
   possibly counterfactual local process instances, not a claim that all States
   coexist in one world or that the old implementation contains many actors. -/
def responseAt (c : PatientCondition) (x : State × Patient) : Prop :=
  condition x.1 x.2 = c ∧ Eligible x.1 x.2

theorem old_c2_iff_decomposition (Bad : PatientCondition → Prop)
    (Merit : State → Patient → Prop) :
    C2 Bad Merit ↔
      EventAnchors Bad responseAt (fun _ x => Merit x.1 x.2) ∧
      OperatorLocality Bad responseAt (fun _ x => Merit x.1 x.2) := by
  have same : C2 Bad Merit ↔
      UniversalReason Bad responseAt (fun _ x => Merit x.1 x.2) := by
    constructor
    · intro h c x hb hx
      exact h x.1 x.2 (hx.1 ▸ hb) hx.2
    · intro h s i hb he
      exact h (condition s i) (s,i) hb ⟨rfl,he⟩
  exact same.trans universal_iff_anchors_and_locality

/- An independently interpreted event is retained while a responder's
   resource-bearing local process varies. Actual same-event identification
   is an explicit compatibility premise, not created by a relabeling. -/
def SamePatientEvent (states : Actor → State) (i : Patient) : Prop :=
  ∀ a b, condition (states a) i = condition (states b) i

theorem same_event_preserves_badness (Bad : PatientCondition → Prop)
    (states : Actor → State) (i : Patient) (same : SamePatientEvent states i)
    (a b : Actor) :
    Bad (condition (states a) i) ↔ Bad (condition (states b) i) := by
  rw [same a b]

theorem local_anchor_actual_service
    (states : Context → Actor → State) (target : Context → Patient)
    (Bad : Context → Prop) (Reason : Context → Actor → Prop)
    (same : ∀ c, SamePatientEvent (states c) (target c))
    (anchor : EventAnchors Bad (fun c a => Eligible (states c a) (target c)) Reason)
    (locality : OperatorLocality Bad
      (fun c a => Eligible (states c a) (target c)) Reason)
    (c : Context) (a : Actor) (hb : Bad c)
    (he : Eligible (states c a) (target c)) :
    Reason c a ∧
      Trace (states c a) (servicePlan (states c a) (target c))
        (run (states c a) (servicePlan (states c a) (target c))) ∧
      (get (run (states c a) (servicePlan (states c a) (target c))) (target c)).burden = 0 ∧
      (get (run (states c a) (servicePlan (states c a) (target c))) (target c)).episode =
        (get (states c a) (target c)).episode ∧
      (∀ b, (get (run (states c a) (servicePlan (states c a) (target c))) (target c)).episode =
        (get (states c b) (target c)).episode) ∧
      (run (states c a) (servicePlan (states c a) (target c))).fuel +
        remainingCost (states c a) (target c) = (states c a).fuel := by
  have hr := anchors_and_locality_give_universal anchor locality c a hb he
  obtain ⟨hz,hp⟩ := eligible_service_delivers_to_same_episode (states c a) (target c) he
  refine ⟨hr,eligible_has_actual_service_trace (states c a) (target c) he,hz,hp,?_,
    eligible_service_is_paid (states c a) (target c) he⟩
  intro b
  have hep := congrArg PatientCondition.episode (same c a b)
  exact hp.trans hep

end NoninstrumentalConcern.RootGrounding

#print axioms NoninstrumentalConcern.RootGrounding.universal_gives_anchors
#print axioms NoninstrumentalConcern.RootGrounding.universal_gives_locality
#print axioms NoninstrumentalConcern.RootGrounding.anchors_and_locality_give_universal
#print axioms NoninstrumentalConcern.RootGrounding.universal_iff_anchors_and_locality
#print axioms NoninstrumentalConcern.RootGrounding.factorization_gives_locality
#print axioms NoninstrumentalConcern.RootGrounding.locality_gives_factorization
#print axioms NoninstrumentalConcern.RootGrounding.factorization_iff_locality
#print axioms NoninstrumentalConcern.RootGrounding.zero_reasons_factor
#print axioms NoninstrumentalConcern.RootGrounding.zero_reasons_lack_anchor
#print axioms NoninstrumentalConcern.RootGrounding.historical_link_covariant
#print axioms NoninstrumentalConcern.RootGrounding.linked_after_append
#print axioms NoninstrumentalConcern.RootGrounding.no_historical_link_at_origin
#print axioms NoninstrumentalConcern.RootGrounding.diagonal_history_forms_by_actual_trace
#print axioms NoninstrumentalConcern.RootGrounding.history_all_events_anchored
#print axioms NoninstrumentalConcern.RootGrounding.history_fixed_event_operator_substitution_fails
#print axioms NoninstrumentalConcern.RootGrounding.history_simultaneous_swap_preserves_reason
#print axioms NoninstrumentalConcern.RootGrounding.never_agent_patient_not_in_own_image
#print axioms NoninstrumentalConcern.RootGrounding.silent_patient_locality
#print axioms NoninstrumentalConcern.RootGrounding.silent_patient_own_anchor
#print axioms NoninstrumentalConcern.RootGrounding.silent_patient_no_reason
#print axioms NoninstrumentalConcern.RootGrounding.silent_patient_not_covered
#print axioms NoninstrumentalConcern.RootGrounding.old_c2_iff_decomposition
#print axioms NoninstrumentalConcern.RootGrounding.same_event_preserves_badness
#print axioms NoninstrumentalConcern.RootGrounding.local_anchor_actual_service
