import ExplanatoryBranching
import ExplanatoryLocalUnits

/-! Questions use roles in actual joins, not names from either fragment type.
The two displayed sorts are an existing fragment and a witnessed joining of
fragments, both constructed from one J. Graph walks inspect relationships;
they are not automatically temporal execution histories. -/
namespace Generative.ExplanatoryJoiningIncidence
open ExplanatoryBranching ExplanatoryLocalUnits
universe u v w
variable {F : Type u} {G : Type v} {H : Type w}

inductive Role where | first | second | result
  deriving DecidableEq

structure Occurrence (J : Join F) where
  first : F
  second : F
  result : F
  formed : J first second result

def Occurrence.at {J : Join F} (e : Occurrence J) : Role → F
  | .first => e.first
  | .second => e.second
  | .result => e.result

abbrev Position (J : Join F) := Sum F (Occurrence J)
inductive Move where | enter : Role → Move | leave : Role → Move

def Step (J : Join F) : Position J → Move → Position J → Prop
  | .inl x, .enter r, .inr e => e.at r = x
  | .inr e, .leave r, .inl x => x = e.at r
  | _, _, _ => False

def model (J : Join F) : Model (Position J) Move Empty where
  process.step := Step J
  condition _ o := nomatch o

abbrev Question := Test Move Empty
def Related (J : Join F) (K : Join G) (x : F) (y : G) : Prop :=
  Same (model J) (model K) (.inl x) (.inl y)

/-- Finite incident joins at a fragment and a role. This is stronger than
finite outcomes for a fixed input pair, and is not a universal physical law. -/
def LocallyFinite (J : Join F) : Prop :=
  ∀ x r, ∃ es : List (Occurrence J), ∀ e, e.at r = x ↔ e ∈ es

theorem locally_finite_image_finite {J : Join F} (hf : LocallyFinite J) :
    ImageFinite (model J) := by
  intro p a
  cases p with
  | inl x =>
    cases a with
    | enter r =>
      obtain ⟨es, he⟩ := hf x r
      refine ⟨es.map Sum.inr, ?_⟩
      intro q
      cases q with
      | inl y => simp [model, Step, List.mem_map]
      | inr e => simpa [model, Step, List.mem_map] using he e
    | leave r => exact ⟨[], fun q => by cases q <;> simp [model, Step]⟩
  | inr e =>
    cases a with
    | enter r => exact ⟨[], fun q => by cases q <;> simp [model, Step]⟩
    | leave r =>
      exact ⟨[.inl (e.at r)], fun q => by cases q <;> simp [model, Step]⟩

theorem leave_question {J : Join F} (e : Occurrence J) (r : Role) (q : Question) :
    Holds (model J) (.inr e) (.after (.leave r) q) ↔ Holds (model J) (.inl (e.at r)) q := by
  constructor
  · rintro ⟨p, hp, hq⟩
    cases p with
    | inl x => cases hp; exact hq
    | inr _ => exact False.elim hp
  · intro hq
    exact ⟨.inl (e.at r), rfl, hq⟩

theorem occurrence_same_matches_slots {J : Join F} {K : Join G}
    {e : Occurrence J} {f : Occurrence K}
    (h : Same (model J) (model K) (.inr e) (.inr f)) (r : Role) :
    Related J K (e.at r) (f.at r) := by
  intro q
  exact (leave_question e r q).symm.trans ((h (.after (.leave r) q)).trans (leave_question f r q))

theorem fragment_not_occurrence_same {J : Join F} {K : Join G}
    (x : F) (e : Occurrence K) : ¬ Same (model J) (model K) (.inl x) (.inr e) := by
  intro h
  have yes : Holds (model K) (.inr e) (.after (.leave .first) .top) :=
    ⟨.inl e.first, rfl, True.intro⟩
  obtain ⟨p, hp, _⟩ := (h (.after (.leave .first) .top)).mpr yes
  cases p <;> exact hp

/-- An incident join is matched as one join, so its three participants are
related together. The correspondence is extracted from role questions. -/
theorem match_incident {J : Join F} {K : Join G} (fk : LocallyFinite K)
    {x : F} {y : G} (h : Related J K x y) (e : Occurrence J) (r : Role)
    (he : e.at r = x) :
    ∃ f : Occurrence K, f.at r = y ∧ ∀ i, Related J K (e.at i) (f.at i) := by
  obtain ⟨p, hp, hs⟩ := same_forces_successor_match (locally_finite_image_finite fk) h
    (a := .enter r) (s' := .inr e) he
  cases p with
  | inl _ => exact False.elim hp
  | inr f => exact ⟨f, hp, occurrence_same_matches_slots hs⟩

/-- Reachability here follows the incidence graph in either relational role,
not only a physical arrow of time. -/
def ConnectedFrom (J : Join F) (root : F) : Prop :=
  ∀ x, ∃ word, Trace (model J).process (.inl root) word (.inl x)

theorem related_covers_connected {J : Join F} {K : Join G}
    (fj : LocallyFinite J) (fk : LocallyFinite K) {x : F} {y : G}
    (h : Related J K x y) (reach : ConnectedFrom J x) :
    ∀ a, ∃ b, Related J K a b := by
  intro a
  obtain ⟨word, trace⟩ := reach a
  obtain ⟨p, _, hp⟩ := bisimulation_lifts_trace
    (same_is_bisimulation (locally_finite_image_finite fj) (locally_finite_image_finite fk)) h trace
  cases p with
  | inl b => exact ⟨b, hp⟩
  | inr e => exact False.elim (fragment_not_occurrence_same a e hp)

abbrev Span (J : Join F) (K : Join G) := {p : F × G // Related J K p.1 p.2}

def spanJoin (J : Join F) (K : Join G) : Join (Span J K) :=
  fun a b c => J a.val.1 b.val.1 c.val.1 ∧ K a.val.2 b.val.2 c.val.2

/-- Preserve joins and lift each incident join while fixing ONE participant.
The other two participants are obtained together, not independently chosen. -/
def OpenMap (J : Join F) (K : Join G) (p : F → G) : Prop :=
  (∀ a b c, J a b c → K (p a) (p b) (p c)) ∧
    ∀ x (e : Occurrence K) r, e.at r = p x →
      ∃ t : Role → F, J (t .first) (t .second) (t .result) ∧ t r = x ∧ ∀ i, p (t i) = e.at i

theorem span_left_open {J : Join F} {K : Join G} (fk : LocallyFinite K) :
    OpenMap (spanJoin J K) J (fun p => p.val.1) := by
  refine ⟨fun _ _ _ h => h.1, ?_⟩
  intro p e r he
  obtain ⟨f, hf, hs⟩ := match_incident fk p.property e r he
  let t : Role → Span J K := fun i => ⟨(e.at i, f.at i), hs i⟩
  refine ⟨t, ⟨e.formed, f.formed⟩, ?_, fun _ => rfl⟩
  apply Subtype.ext
  exact Prod.ext he hf

theorem span_right_open {J : Join F} {K : Join G} (fj : LocallyFinite J) :
    OpenMap (spanJoin J K) K (fun p => p.val.2) := by
  refine ⟨fun _ _ _ h => h.2, ?_⟩
  intro p e r he
  obtain ⟨f, hf, hs⟩ := match_incident fj (same_symm p.property) e r he
  let t : Role → Span J K := fun i => ⟨(f.at i, e.at i), same_symm (hs i)⟩
  refine ⟨t, ⟨f.formed, e.formed⟩, ?_, fun _ => rfl⟩
  apply Subtype.ext
  exact Prod.ext hf he

theorem connected_common_refinement {J : Join F} {K : Join G}
    (fj : LocallyFinite J) (fk : LocallyFinite K) {x : F} {y : G}
    (h : Related J K x y) (rj : ConnectedFrom J x) (rk : ConnectedFrom K y) :
    OpenMap (spanJoin J K) J (fun p => p.val.1) ∧
    OpenMap (spanJoin J K) K (fun p => p.val.2) ∧
    (∀ a, ∃ p : Span J K, p.val.1 = a) ∧ (∀ b, ∃ p : Span J K, p.val.2 = b) := by
  refine ⟨span_left_open fk, span_right_open fj, ?_, ?_⟩
  · intro a
    obtain ⟨b, hb⟩ := related_covers_connected fj fk h rj a
    exact ⟨⟨(a, b), hb⟩, rfl⟩
  · intro b
    obtain ⟨a, ha⟩ := related_covers_connected fk fj (same_symm h) rk b
    exact ⟨⟨(a, b), same_symm ha⟩, rfl⟩

end Generative.ExplanatoryJoiningIncidence

#print axioms Generative.ExplanatoryJoiningIncidence.locally_finite_image_finite
#print axioms Generative.ExplanatoryJoiningIncidence.leave_question
#print axioms Generative.ExplanatoryJoiningIncidence.occurrence_same_matches_slots
#print axioms Generative.ExplanatoryJoiningIncidence.fragment_not_occurrence_same
#print axioms Generative.ExplanatoryJoiningIncidence.match_incident
#print axioms Generative.ExplanatoryJoiningIncidence.related_covers_connected
#print axioms Generative.ExplanatoryJoiningIncidence.span_left_open
#print axioms Generative.ExplanatoryJoiningIncidence.span_right_open
#print axioms Generative.ExplanatoryJoiningIncidence.connected_common_refinement
