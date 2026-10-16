import ExplanatoryJoiningIncidence

/-! Recover a canonical comparison of different fragment articulations.
Its unique factor preserves joins and commutes with both projections; the
factor is NOT claimed to be an open map. One-position lifting is explicit. -/
namespace Generative.ExplanatoryJoiningRefinement
open ExplanatoryBranching ExplanatoryLocalUnits ExplanatoryJoiningIncidence
universe u v w
variable {F : Type u} {G : Type v} {H : Type w}

theorem occurrence_ext {J : Join F} {e f : Occurrence J}
    (h : ∀ i, e.at i = f.at i) : e = f := by
  rcases e with ⟨a, b, c, hj⟩
  rcases f with ⟨a', b', c', hk⟩
  have ha : a = a' := h .first
  have hb : b = b' := h .second
  have hc : c = c' := h .result
  subst a'; subst b'; subst c'
  rfl

def ofTuple {J : Join F} (t : Role → F) (h : J (t .first) (t .second) (t .result)) :
    Occurrence J := ⟨t .first, t .second, t .result, h⟩

theorem ofTuple_at {J : Join F} (t : Role → F)
    (h : J (t .first) (t .second) (t .result)) (r : Role) : (ofTuple t h).at r = t r := by
  cases r <;> rfl

def mapOccurrence {J : Join F} {K : Join G} (p : F → G)
    (hp : ∀ a b c, J a b c → K (p a) (p b) (p c)) (e : Occurrence J) : Occurrence K :=
  ⟨p e.first, p e.second, p e.result, hp _ _ _ e.formed⟩

theorem mapOccurrence_at {J : Join F} {K : Join G} (p : F → G)
    (hp : ∀ a b c, J a b c → K (p a) (p b) (p c)) (e : Occurrence J) (r : Role) :
    (mapOccurrence p hp e).at r = p (e.at r) := by
  cases r <;> rfl

def mapPosition {J : Join F} {K : Join G} (p : F → G)
    (hp : ∀ a b c, J a b c → K (p a) (p b) (p c)) : Position J → Position K
  | .inl x => .inl (p x)
  | .inr e => .inr (mapOccurrence p hp e)

theorem map_step {J : Join F} {K : Join G} (p : F → G)
    (hp : ∀ a b c, J a b c → K (p a) (p b) (p c))
    {s t : Position J} {a : Move} (h : Step J s a t) :
    Step K (mapPosition p hp s) a (mapPosition p hp t) := by
  cases s <;> cases t <;> cases a <;> simp only [Step] at h
  all_goals try exact False.elim h
  · simpa only [mapPosition, Step, mapOccurrence_at] using congrArg p h
  · simpa only [mapPosition, Step, mapOccurrence_at] using congrArg p h

theorem open_map_lifts_step {J : Join F} {K : Join G} {p : F → G}
    (hp : OpenMap J K p) (s : Position J) (a : Move) (t : Position K)
    (h : Step K (mapPosition p hp.1 s) a t) :
    ∃ s', Step J s a s' ∧ mapPosition p hp.1 s' = t := by
  cases s with
  | inl x =>
    cases a with
    | enter r =>
      cases t with
      | inl _ => exact False.elim h
      | inr e =>
        obtain ⟨t, ht, hx, he⟩ := hp.2 x e r h
        refine ⟨.inr (ofTuple t ht), (ofTuple_at t ht r).trans hx, ?_⟩
        apply congrArg Sum.inr
        apply occurrence_ext
        intro i
        exact (mapOccurrence_at p hp.1 _ i).trans ((congrArg p (ofTuple_at t ht i)).trans (he i))
    | leave r => cases t <;> exact False.elim h
  | inr e =>
    cases a with
    | enter r => cases t <;> exact False.elim h
    | leave r =>
      cases t with
      | inl y =>
        refine ⟨.inl (e.at r), rfl, ?_⟩
        apply congrArg Sum.inl
        exact (mapOccurrence_at p hp.1 e r).symm.trans h.symm
      | inr _ => exact False.elim h

theorem open_map_bisimulation {J : Join F} {K : Join G} {p : F → G}
    (hp : OpenMap J K p) :
    Bisimulation (model J) (model K) (fun s t => mapPosition p hp.1 s = t) := by
  refine ⟨⟨?_, ?_⟩, ?_⟩
  · intro s t a s' he hs
    subst t
    exact ⟨mapPosition p hp.1 s', map_step p hp.1 hs, rfl⟩
  · intro s t a t' he ht
    subst t
    exact open_map_lifts_step hp s a t' ht
  · intro s t he o
    exact nomatch o

theorem open_map_preserves_questions {J : Join F} {K : Join G} {p : F → G}
    (hp : OpenMap J K p) (x : F) : Related J K x (p x) :=
  bisimulation_implies_same (open_map_bisimulation hp) rfl

theorem identity_open (J : Join F) : OpenMap J J id := by
  refine ⟨fun _ _ _ h => h, ?_⟩
  intro x e r he
  exact ⟨e.at, e.formed, he, fun _ => rfl⟩

def commonFactor {L : Join H} {J : Join F} {K : Join G}
    {p : H → F} {q : H → G} (hp : OpenMap L J p) (hq : OpenMap L K q)
    (x : H) : Span J K :=
  ⟨(p x, q x), same_trans (same_symm (open_map_preserves_questions hp x))
    (open_map_preserves_questions hq x)⟩

theorem common_factor_preserves_joins {L : Join H} {J : Join F} {K : Join G}
    {p : H → F} {q : H → G} (hp : OpenMap L J p) (hq : OpenMap L K q)
    {a b c : H} (h : L a b c) :
    spanJoin J K (commonFactor hp hq a) (commonFactor hp hq b) (commonFactor hp hq c) :=
  ⟨hp.1 _ _ _ h, hq.1 _ _ _ h⟩

/-- Canonical only relative to the two maps. This does not identify all
underlying fragment sets or make the factor preserve one-position lifting. -/
theorem common_factor_unique {L : Join H} {J : Join F} {K : Join G}
    {p : H → F} {q : H → G} (hp : OpenMap L J p) (hq : OpenMap L K q)
    (f : H → Span J K) (left : ∀ x, (f x).val.1 = p x) (right : ∀ x, (f x).val.2 = q x) :
    f = commonFactor hp hq := by
  funext x
  apply Subtype.ext
  exact Prod.ext (left x) (right x)

theorem universal_common_factor {L : Join H} {J : Join F} {K : Join G}
    {p : H → F} {q : H → G} (hp : OpenMap L J p) (hq : OpenMap L K q) :
    ∃ f : H → Span J K,
      (∀ x, (f x).val.1 = p x ∧ (f x).val.2 = q x) ∧
      (∀ a b c, L a b c → spanJoin J K (f a) (f b) (f c)) ∧
      ∀ g : H → Span J K, (∀ x, (g x).val.1 = p x ∧ (g x).val.2 = q x) → g = f := by
  exact ⟨commonFactor hp hq, fun _ => ⟨rfl, rfl⟩,
    fun _ _ _ h => common_factor_preserves_joins hp hq h,
    fun g h => common_factor_unique hp hq g (fun x => (h x).1) (fun x => (h x).2)⟩

end Generative.ExplanatoryJoiningRefinement

#print axioms Generative.ExplanatoryJoiningRefinement.occurrence_ext
#print axioms Generative.ExplanatoryJoiningRefinement.ofTuple_at
#print axioms Generative.ExplanatoryJoiningRefinement.mapOccurrence_at
#print axioms Generative.ExplanatoryJoiningRefinement.map_step
#print axioms Generative.ExplanatoryJoiningRefinement.open_map_lifts_step
#print axioms Generative.ExplanatoryJoiningRefinement.open_map_bisimulation
#print axioms Generative.ExplanatoryJoiningRefinement.open_map_preserves_questions
#print axioms Generative.ExplanatoryJoiningRefinement.identity_open
#print axioms Generative.ExplanatoryJoiningRefinement.common_factor_preserves_joins
#print axioms Generative.ExplanatoryJoiningRefinement.common_factor_unique
#print axioms Generative.ExplanatoryJoiningRefinement.universal_common_factor
