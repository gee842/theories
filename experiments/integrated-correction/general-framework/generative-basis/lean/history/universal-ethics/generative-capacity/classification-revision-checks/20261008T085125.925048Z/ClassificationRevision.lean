import PracticalJudgment

/- Classification concerns a route to an independently specified target within
one jointly eligible continuation menu. Readings, eligibility and the target's
normative significance have separate correspondence obligations. No basic ethical
standing is learned merely by passing a task. -/
namespace ClassificationRevision
open PracticalJudgment

def NecessaryRoute {H : Type} (eligible target route : H → Prop) : Prop :=
  Required (fun a => eligible a ∧ target a) route

def Observed {H : Type} (records : List (H × Bool)) (a : H) : Prop :=
  (a, true) ∈ records

def Faithful {H : Type} (records : List (H × Bool)) (target : H → Prop) : Prop :=
  ∀ a b, (a,b) ∈ records → (b = true ↔ target a)

def Covered {H : Type} (records : List (H × Bool)) (eligible : H → Prop) : Prop :=
  ∀ a, eligible a → ∃ b, (a,b) ∈ records

def AssessedRoute {H : Type} (records : List (H × Bool))
    (eligible route : H → Prop) : Prop := NecessaryRoute eligible (Observed records) route

theorem observed_target_exact_on_covered_menu {H : Type}
    (records : List (H × Bool)) (eligible target : H → Prop)
    (faithful : Faithful records target) (covered : Covered records eligible)
    (a : H) (ha : eligible a) : Observed records a ↔ target a := by
  constructor
  · intro h
    exact (faithful a true h).1 rfl
  · intro ht
    obtain ⟨b,hb⟩ := covered a ha
    have eq := (faithful a b hb).2 ht
    subst b
    exact hb

theorem acquired_classification_exact {H : Type}
    (records : List (H × Bool)) (eligible target route : H → Prop)
    (faithful : Faithful records target) (covered : Covered records eligible) :
    AssessedRoute records eligible route ↔ NecessaryRoute eligible target route := by
  have exactness := observed_target_exact_on_covered_menu records eligible target faithful covered
  constructor
  · rintro ⟨⟨a,ha,ho⟩,all⟩
    exact ⟨⟨a,ha,(exactness a ha).1 ho⟩,
      fun b hb => all b ⟨hb.1,(exactness b hb.1).2 hb.2⟩⟩
  · rintro ⟨⟨a,ha,ht⟩,all⟩
    exact ⟨⟨a,ha,(exactness a ha).2 ht⟩,
      fun b hb => all b ⟨hb.1,(exactness b hb.1).1 hb.2⟩⟩

theorem one_faithful_alternative_defeats_necessity {H : Type}
    (records : List (H × Bool)) (eligible target route : H → Prop)
    (faithful : Faithful records target) (a : H)
    (ha : eligible a) (observed : Observed records a) (without : ¬ route a) :
    ¬ NecessaryRoute eligible target route :=
  alternative_defeats_specific_duty ⟨ha,(faithful a true observed).1 rfl⟩ without

theorem restriction_can_only_strengthen_necessity_with_witness {H : Type}
    (broad narrow target route : H → Prop) (subset : Included narrow broad)
    (viable : ∃ a, narrow a ∧ target a) (h : NecessaryRoute broad target route) :
    NecessaryRoute narrow target route :=
  ⟨viable,fun a ha => h.2 a ⟨subset a ha.1,ha.2⟩⟩

theorem alternative_survives_menu_expansion {H : Type}
    (old new target route : H → Prop) (subset : Included old new)
    (witness : ∃ a, old a ∧ target a ∧ ¬ route a) :
    ∃ a, new a ∧ target a ∧ ¬ route a := by
  obtain ⟨a,ha,ht,hr⟩ := witness
  exact ⟨a,subset a ha,ht,hr⟩

/-- Narrowing supported interpretations and expanding an eligible menu are
opposite quantifier changes; neither is automatically licensed by 'learning'. -/
def CommonNecessity {W H : Type} (live : W → Prop)
    (eligible : H → Prop) (target : W → H → Prop) (route : H → Prop) : Prop :=
  ∀ w, live w → NecessaryRoute eligible (target w) route

theorem necessity_survives_supported_refinement {W H : Type}
    (old new : W → Prop) (eligible : H → Prop)
    (target : W → H → Prop) (route : H → Prop) (subset : Included new old)
    (h : CommonNecessity old eligible target route) :
    CommonNecessity new eligible target route :=
  robust_under_refinement subset h

theorem common_necessity_at_actual {W H : Type}
    (live : W → Prop) (eligible : H → Prop)
    (target : W → H → Prop) (route : H → Prop) (actual : W)
    (truth : live actual) (h : CommonNecessity live eligible target route) :
    NecessaryRoute eligible (target actual) route := robust_at_actual truth h

inductive Arrangement where
  | relay | direct | shut
  deriving DecidableEq

/-- These exact local access laws are stipulated. The implementation does not
establish semantic adequacy, ordinary human communication or permission. -/
def access : Arrangement → Bool
  | .relay => true
  | .direct => true
  | .shut => false

def target (a : Arrangement) : Prop := access a = true
def usesRelay (a : Arrangement) : Prop := a = .relay
def oldMenu (a : Arrangement) : Prop := a = .relay ∨ a = .shut
def enlargedMenu (_ : Arrangement) : Prop := True

def acquire (menu : List Arrangement) : List (Arrangement × Bool) :=
  menu.map (fun a => (a,access a))

def firstRecords := acquire [.relay,.shut]
def laterRecords := firstRecords ++ acquire [.direct]

theorem acquisition_faithful (menu : List Arrangement) :
    Faithful (acquire menu) target := by
  intro a b h
  obtain ⟨x,hx,eq⟩ := List.mem_map.mp h
  cases eq
  exact Iff.rfl

theorem first_classification_scoped :
    AssessedRoute firstRecords oldMenu usesRelay := by
  refine ⟨⟨.relay,Or.inl rfl,by decide⟩,?_⟩
  intro a ha
  rcases ha.1 with h | h
  · exact h
  · subst a
    simp [Observed,firstRecords,acquire,access] at ha

theorem later_record_preserves_previous_records :
    ∀ r, r ∈ firstRecords → r ∈ laterRecords := by
  intro r h
  exact List.mem_append_left _ h

theorem later_records_faithful : Faithful laterRecords target := by
  intro a b h
  rcases List.mem_append.mp h with h | h
  · exact acquisition_faithful [.relay,.shut] a b h
  · exact acquisition_faithful [.direct] a b h

theorem later_records_cover_enlarged_menu : Covered laterRecords enlargedMenu := by
  intro a ha
  cases a <;> exact ⟨_,by simp [laterRecords,firstRecords,acquire,access]⟩

theorem discovered_route_revises_classification :
    ¬ AssessedRoute laterRecords enlargedMenu usesRelay ∧
    ¬ NecessaryRoute enlargedMenu target usesRelay := by
  have hn : ¬ NecessaryRoute enlargedMenu target usesRelay :=
    one_faithful_alternative_defeats_necessity laterRecords enlargedMenu target usesRelay
      later_records_faithful .direct True.intro (by decide) (by decide)
  exact ⟨fun h => hn ((acquired_classification_exact laterRecords enlargedMenu target usesRelay
    later_records_faithful later_records_cover_enlarged_menu).1 h),hn⟩

theorem broader_target_remains_realized_without_old_route :
    target .direct ∧ ¬ usesRelay .direct := by decide

theorem withholding_available_route_creates_apparent_necessity :
    NecessaryRoute oldMenu target usesRelay ∧
    ¬ NecessaryRoute enlargedMenu target usesRelay := by
  constructor
  · refine ⟨⟨.relay,Or.inl rfl,rfl⟩,?_⟩
    intro a ha
    rcases ha.1 with h | h
    · exact h
    · subst a
      cases ha.2
  · exact discovered_route_revises_classification.2

/-- A false positive is a retained actual counterexample, not an assumption
that every reading meets the Faithful premise. -/
def corruptRecords : List (Arrangement × Bool) := [(.shut,true)]

theorem false_reading_defeats_correspondence :
    Observed corruptRecords .shut ∧ ¬ target .shut ∧ ¬ Faithful corruptRecords target := by
  refine ⟨by decide,by decide,?_⟩
  intro h
  have impossible := (h .shut true (by decide)).1 rfl
  cases impossible

end ClassificationRevision
