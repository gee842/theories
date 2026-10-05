import Std

/-!
Semantic interface laws, not a physical join. Interpretations, justified
transport relations, provenance and causal effects are explicit parameters.
No upstream package is imported; the finite mask countermodel reproduces the
two documented interpretations without claiming a refinement of their code.
-/
namespace SemanticAction

def Preserves {S T W V : Type} (P : W → S → Prop) (Q : V → T → Prop)
    (scope : W → V → Prop) (translate : S → Option T) : Prop :=
  ∀ w v s t, scope w v → translate s = some t → P w s → Q v t

def Counterexample {S T W V : Type} (P : W → S → Prop) (Q : V → T → Prop)
    (scope : W → V → Prop) (translate : S → Option T) : Prop :=
  ∃ w v s t, scope w v ∧ translate s = some t ∧ P w s ∧ ¬ Q v t

theorem preserves_iff_no_counterexample {S T W V : Type}
    (P : W → S → Prop) (Q : V → T → Prop)
    (scope : W → V → Prop) (translate : S → Option T) :
    Preserves P Q scope translate ↔ ¬ Counterexample P Q scope translate := by
  constructor
  · intro h ⟨w,v,s,t,hr,ht,hp,hn⟩
    exact hn (h w v s t hr ht hp)
  · intro h w v s t hr ht hp
    exact Classical.byContradiction (fun hn => h ⟨w,v,s,t,hr,ht,hp,hn⟩)

def compose {S T U : Type} (f : S → Option T) (g : T → Option U)
    (s : S) : Option U := (f s).bind g

theorem preserves_composition {S T U W V Z : Type}
    {P : W → S → Prop} {Q : V → T → Prop} {R : Z → U → Prop}
    {a : W → V → Prop} {b : V → Z → Prop}
    {f : S → Option T} {g : T → Option U}
    (hf : Preserves P Q a f) (hg : Preserves Q R b g) :
    Preserves P R (fun w z => ∃ v, a w v ∧ b v z) (compose f g) := by
  intro w z s u ⟨v,hav,hbv⟩ hsu hps
  cases hfs : f s with
  | none => simp [compose,hfs] at hsu
  | some t =>
    have hgu : g t = some u := by simpa [compose,hfs] using hsu
    exact hg v z t u hbv hgu (hf w v s t hav hfs hps)

theorem preserves_under_justified_scope_restriction {S T W V : Type}
    {P : W → S → Prop} {Q : V → T → Prop}
    {scope narrower : W → V → Prop} {f : S → Option T}
    (hf : Preserves P Q scope f) (hn : ∀ w v, narrower w v → scope w v) :
    Preserves P Q narrower f := by
  intro w v s t hr ht hp
  exact hf w v s t (hn w v hr) ht hp

theorem rejecting_everything_is_sound_but_exports_nothing {S T W V : Type}
    (P : W → S → Prop) (Q : V → T → Prop) (scope : W → V → Prop) :
    Preserves P Q scope (fun _ => (none : Option T)) ∧
      ∀ s : S, ∀ t : T, (fun _ : S => (none : Option T)) s ≠ some t := by
  constructor
  · intro _ _ _ _ _ impossible _
    cases impossible
  · intro _ _ impossible
    cases impossible

/- The source's two nodes are alternative commands to one fixed recipient.
The target's two nodes are two patients. These interpretations are not equal. -/
inductive Patient where | p | q
deriving DecidableEq, Repr

def routeMask (orientation : Bool) : Bool × Bool := (!orientation, orientation)
def bitAsPatient : Bool → Patient | false => .p | true => .q

theorem raw_route_as_patient_has_counterexample :
    Counterexample (fun z action : Bool => action = z)
      (fun (_ : Unit) patient => patient = Patient.p) (fun _ _ => True)
      (fun action => some (bitAsPatient action)) := by
  exact ⟨true,(),true,Patient.q,True.intro,rfl,rfl,by decide⟩

theorem no_injective_mask_decoder_preserves_fixed_bearer
    (decode : (Bool × Bool) → Patient) (patient : Patient)
    (hi : Function.Injective (fun z => decode (routeMask z)))
    (h0 : decode (routeMask false) = patient)
    (h1 : decode (routeMask true) = patient) : False := by
  have he : (false : Bool) = true := hi (h0.trans h1.symm)
  have hn : (false : Bool) ≠ true := by decide
  exact hn he

structure CommandClaim where
  patient : Patient
  command : Bool
deriving DecidableEq, Repr

theorem addressed_command_keeps_bearer_and_changes_action (patient : Patient) :
    let left : CommandClaim := ⟨patient,false⟩
    let right : CommandClaim := ⟨patient,true⟩
    left.patient = right.patient ∧ left.command ≠ right.command := by
  exact ⟨rfl,show (false : Bool) ≠ true from by decide⟩

/- A supplied role-sensitive semantic scope can permit a new software actor.
The example deliberately does not infer legitimate role or goal from bytes. -/
structure World where
  actor : Nat
  role : Nat
  patient : Patient
  contextLabel : Bool
  generation : Nat
  law : Bool
deriving DecidableEq, Repr

def RoleScope (w v : World) : Prop :=
  w.role = v.role ∧ w.patient = v.patient ∧
  w.contextLabel = v.contextLabel ∧ w.generation = v.generation ∧ w.law = v.law

instance (w v : World) : Decidable (RoleScope w v) := by unfold RoleScope; infer_instance

def Instrumental (purpose : Nat → Patient → Prop) (w : World) (c : CommandClaim) : Prop :=
  c.patient = w.patient ∧ purpose w.role w.patient ∧ c.command = w.law

theorem role_scope_composes {a b c : World}
    (hab : RoleScope a b) (hbc : RoleScope b c) : RoleScope a c := by
  exact ⟨hab.1.trans hbc.1,hab.2.1.trans hbc.2.1,
    hab.2.2.1.trans hbc.2.2.1,hab.2.2.2.1.trans hbc.2.2.2.1,
    hab.2.2.2.2.trans hbc.2.2.2.2⟩

theorem justified_role_scope_transports_instrumental
    (purpose : Nat → Patient → Prop) :
    Preserves (Instrumental purpose) (Instrumental purpose) RoleScope some := by
  intro w v s t hscope hst hs
  have he : s = t := Option.some.inj hst
  subst t
  rcases hscope with ⟨hr,hp,_,_,hl⟩
  rcases hs with ⟨hbearer,hpurpose,hcommand⟩
  exact ⟨hbearer.trans hp,hr ▸ hp ▸ hpurpose,hcommand.trans hl⟩

theorem changed_actor_can_preserve_role_scope :
    let old : World := ⟨0,7,.p,false,4,true⟩
    let successor : World := ⟨1,7,.p,false,4,true⟩
    old.actor ≠ successor.actor ∧ RoleScope old successor := by decide

theorem matching_label_is_insufficient_after_reopening :
    let old : World := ⟨0,7,.p,false,4,true⟩
    let reopened : World := ⟨0,7,.p,false,5,true⟩
    old.contextLabel = reopened.contextLabel ∧ ¬ RoleScope old reopened := by decide

/- Reason truth, justified premises and actual admission remain different
predicates. Even sound complete admission supplies no action dynamics. -/
structure Status where
  reasonTrue : Bool
  justified : Bool
  admitted : Bool
  authorized : Bool
  feasible : Bool
  delivered : Bool
deriving DecidableEq, Repr

def SoundAdmission (s : Status) : Prop :=
  (s.justified = true → s.reasonTrue = true) ∧
  (s.admitted = true → s.justified = true)

instance (s : Status) : Decidable (SoundAdmission s) := by unfold SoundAdmission; infer_instance

theorem sound_admission_preserves_reason (s : Status) (hs : SoundAdmission s)
    (ha : s.admitted = true) : s.reasonTrue = true := hs.1 (hs.2 ha)

theorem distinct_reason_and_action_stages_have_models :
    (∃ s : Status, SoundAdmission s ∧ s.reasonTrue = true ∧ s.justified = false) ∧
    (∃ s : Status, SoundAdmission s ∧ s.justified = true ∧ s.admitted = false) ∧
    (∃ s : Status, SoundAdmission s ∧ s.admitted = true ∧ s.authorized = false ∧ s.delivered = false) ∧
    (∃ s : Status, SoundAdmission s ∧ s.admitted = true ∧ s.authorized = true ∧ s.feasible = true ∧ s.delivered = false) ∧
    (∃ s : Status, SoundAdmission s ∧ s.admitted = false ∧ s.delivered = true) := by
  refine ⟨?_,?_,?_,?_,?_⟩
  · exact ⟨⟨true,false,false,false,false,false⟩,by decide⟩
  · exact ⟨⟨true,true,false,false,false,false⟩,by decide⟩
  · exact ⟨⟨true,true,true,false,true,false⟩,by decide⟩
  · exact ⟨⟨true,true,true,true,true,false⟩,by decide⟩
  · exact ⟨⟨true,true,false,true,true,true⟩,by decide⟩

theorem authorization_and_feasibility_do_not_supply_ground :
    ∃ s : Status, SoundAdmission s ∧ s.authorized = true ∧ s.feasible = true ∧
      s.reasonTrue = false ∧ s.justified = false := by
  exact ⟨⟨false,false,false,true,true,false⟩,by decide⟩

def receipt (command law available : Bool) : Bool := available && (command == law)
def Compatible (law command : Bool) : Prop := ∀ available, receipt command law available = available

theorem compatibility_does_not_supply_evaluative_good :
    ∃ law command : Bool, ∃ good : Bool → Prop,
      Compatible law command ∧ receipt command law true = true ∧ ¬ good true := by
  refine ⟨false,false,fun _ => False,?_,rfl,id⟩
  intro available
  cases available <;> rfl

/- This is the precise extra causal obligation for the selected execution,
not a claim that either active implementation already meets it. -/
def Realizes {W A : Type} (enabled : W → A → Prop) (execute : W → A → W)
    (effect : W → A → W → Prop) : Prop :=
  ∀ w a, enabled w a → effect w a (execute w a)

theorem selected_action_requires_two_independent_contracts {W A : Type}
    {warranted admitted selected enabled : W → A → Prop}
    {execute : W → A → W} {effect : W → A → W → Prop}
    (audit_sound : ∀ w a, admitted w a → warranted w a)
    (causal : Realizes enabled execute effect)
    (chosen : ∀ w a, selected w a → admitted w a ∧ enabled w a) :
    ∀ w a, selected w a → warranted w a ∧ effect w a (execute w a) := by
  intro w a ha
  exact ⟨audit_sound w a (chosen w a ha).1,causal w a (chosen w a ha).2⟩

end SemanticAction

#print axioms SemanticAction.preserves_iff_no_counterexample
#print axioms SemanticAction.preserves_composition
#print axioms SemanticAction.preserves_under_justified_scope_restriction
#print axioms SemanticAction.rejecting_everything_is_sound_but_exports_nothing
#print axioms SemanticAction.raw_route_as_patient_has_counterexample
#print axioms SemanticAction.no_injective_mask_decoder_preserves_fixed_bearer
#print axioms SemanticAction.addressed_command_keeps_bearer_and_changes_action
#print axioms SemanticAction.role_scope_composes
#print axioms SemanticAction.justified_role_scope_transports_instrumental
#print axioms SemanticAction.changed_actor_can_preserve_role_scope
#print axioms SemanticAction.matching_label_is_insufficient_after_reopening
#print axioms SemanticAction.sound_admission_preserves_reason
#print axioms SemanticAction.distinct_reason_and_action_stages_have_models
#print axioms SemanticAction.authorization_and_feasibility_do_not_supply_ground
#print axioms SemanticAction.compatibility_does_not_supply_evaluative_good
#print axioms SemanticAction.selected_action_requires_two_independent_contracts
