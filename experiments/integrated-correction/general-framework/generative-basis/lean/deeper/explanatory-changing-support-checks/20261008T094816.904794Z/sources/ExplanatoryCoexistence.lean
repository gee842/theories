import ExplanatoryFootprints

/-! Operational correspondence for exclusive, persistent holdings. Acquisitions
change one shared occupancy record; there are no releases or changing access
within this local episode. Common final holding is not general concurrency. -/
namespace Generative.ExplanatoryCoexistence
open ExplanatoryJointness ExplanatoryFootprints ExplanatoryUniqueness
universe u v w x y
variable {R : Type u}

def process (available : List R) : Process (List R) R where
  step busy a next := a ∈ available ∧ a ∉ busy ∧ next = busy ++ [a]

def Admissible (available busy requests : List R) : Prop :=
  requests.Nodup ∧ ∀ a, a ∈ requests → a ∈ available ∧ a ∉ busy

theorem admissible_cons (available busy : List R) (a : R) (rest : List R) :
    Admissible available busy (a :: rest) ↔
      a ∈ available ∧ a ∉ busy ∧ Admissible available (busy ++ [a]) rest := by
  constructor
  · intro h
    obtain ⟨absent, nodup⟩ := List.nodup_cons.mp h.1
    refine ⟨(h.2 a List.mem_cons_self).1, (h.2 a List.mem_cons_self).2,
      nodup, ?_⟩
    intro b hb
    have hb' := h.2 b (List.mem_cons_of_mem a hb)
    refine ⟨hb'.1, ?_⟩
    intro bad
    rcases List.mem_append.mp bad with old | same
    · exact hb'.2 old
    · have eq : b = a := List.mem_singleton.mp same
      exact absent (eq ▸ hb)
  · rintro ⟨access, fresh, nodup, all⟩
    have absent : a ∉ rest := fun h => (all a h).2 (List.mem_append_right _ List.mem_cons_self)
    refine ⟨List.nodup_cons.mpr ⟨absent, nodup⟩, ?_⟩
    intro b hb
    rcases List.mem_cons.mp hb with eq | mem
    · subst b; exact ⟨access, fresh⟩
    · exact ⟨(all b mem).1, fun bad => (all b mem).2 (List.mem_append_left _ bad)⟩

theorem trace_iff_admissible (available requests : List R) :
    ∀ busy final, Trace (process available) busy requests final ↔
      Admissible available busy requests ∧ final = busy ++ requests := by
  induction requests with
  | nil =>
    intro busy final
    constructor
    · intro h; cases h; exact ⟨⟨List.nodup_nil, by simp⟩, by simp⟩
    · rintro ⟨_, eq⟩
      have same : final = busy := by simpa using eq
      rw [same]
      exact Trace.nil busy
  | cons a rest ih =>
    intro busy final
    constructor
    · intro h
      cases h with
      | cons step tail =>
        rcases step with ⟨access, fresh, rfl⟩
        obtain ⟨ha, hf⟩ := (ih _ _).mp tail
        refine ⟨(admissible_cons ..).mpr ⟨access, fresh, ha⟩, ?_⟩
        simpa [List.append_assoc] using hf
    · rintro ⟨ha, hf⟩
      obtain ⟨access, fresh, tail⟩ := (admissible_cons ..).mp ha
      apply Trace.cons (m := busy ++ [a])
      · exact ⟨access, fresh, rfl⟩
      · apply (ih _ _).mpr
        exact ⟨tail, by simpa [List.append_assoc] using hf⟩

theorem exists_trace_iff (available busy requests : List R) :
    (∃ final, Trace (process available) busy requests final) ↔ Admissible available busy requests :=
  ⟨fun ⟨_, h⟩ => ((trace_iff_admissible available requests busy _).mp h).1,
    fun h => ⟨busy ++ requests, (trace_iff_admissible available requests busy _).mpr ⟨h, rfl⟩⟩⟩

theorem final_retains_all_requests (available busy requests final : List R)
    (h : Trace (process available) busy requests final) : ∀ a, a ∈ requests → a ∈ final := by
  obtain ⟨_, rfl⟩ := (trace_iff_admissible available requests busy final).mp h
  exact fun _ ha => List.mem_append_right _ ha

theorem empty_trace_iff_supported (available requests : List R) :
    Trace (process available) [] requests requests ↔ Supported support available requests := by
  rw [trace_iff_admissible]
  simp [Admissible, Supported, support]

theorem native_plan_iff_common_holding (available : List R) (p : Plan (List R)) :
    Realizes joint (Supported support) available p ↔
      Trace (process available) [] (Requests p) (Requests p) :=
  (realize_iff_supported p available).trans (empty_trace_iff_supported available (Requests p)).symm

theorem footprint_plan_has_holding_history {S : Type v} {F : S → R → Prop}
    {J : S → S → S → Prop} (within : Within F J) (separate : Separate F J)
    (available busy : List R) (s : S) (p : Plan (List R))
    (access : ∀ a, F s a → a ∈ available)
    (fresh : ∀ a, F s a → a ∉ busy)
    (h : Realizes J (Supported F) s p) :
    Trace (process available) busy (Requests p) (busy ++ Requests p) := by
  obtain ⟨nodup, all⟩ := realized_requests_supported within separate p s h
  exact (trace_iff_admissible available (Requests p) busy _).mpr
    ⟨⟨nodup, fun a ha => ⟨access a (all a ha), fresh a (all a ha)⟩⟩, rfl⟩

theorem code_plan_has_holding_history {S : Type v} {A : Type w} {O : Type x} {C : Type y}
    {m : Model S A O} {account : Presentation S (Test A O) C}
    (compact : JointCompact m) (exact : Exact (Holds m) account)
    (reduced : Reduced (Holds m) account) (F : S → R → Prop)
    (within : Within F m.joint) (separate : Separate F m.joint)
    (read : C → List R → Prop)
    (correct : ∀ s xs, read (account.encode s) xs ↔ Supported F s xs)
    (available busy : List R) (s : S) (p : Plan (List R))
    (access : ∀ a, F s a → a ∈ available)
    (fresh : ∀ a, F s a → a ∉ busy)
    (h : Realizes (codeJoint m account) read (account.encode s) p) :
    Trace (process available) busy (Requests p) (busy ++ Requests p) :=
  footprint_plan_has_holding_history within separate available busy s p access fresh
    ((joint_plan_lifts compact exact reduced (Supported F) read correct p s).mp h)

theorem permutation_preserves_holding (available busy xs ys : List R) (perm : xs.Perm ys) :
    (∃ final, Trace (process available) busy xs final) ↔
      ∃ final, Trace (process available) busy ys final := by
  rw [exists_trace_iff, exists_trace_iff]
  constructor
  · intro h; exact ⟨perm.nodup h.1, fun a ha => h.2 a (perm.mem_iff.mpr ha)⟩
  · intro h; exact ⟨perm.symm.nodup h.1, fun a ha => h.2 a (perm.mem_iff.mp ha)⟩

theorem frame_holding_iff (available busy extra requests : List R) :
    (∃ final, Trace (process available) (busy ++ extra) requests final) ↔
      (∃ final, Trace (process available) busy requests final) ∧ Apart requests extra := by
  rw [exists_trace_iff, exists_trace_iff]
  constructor
  · intro h
    exact ⟨⟨h.1, fun a ha => ⟨(h.2 a ha).1,
      fun hb => (h.2 a ha).2 (List.mem_append_left _ hb)⟩⟩,
      fun a ha he => (h.2 a ha).2 (List.mem_append_right _ he)⟩
  · rintro ⟨h, apart⟩
    refine ⟨h.1, ?_⟩
    intro a ha
    exact ⟨(h.2 a ha).1, fun hb => (List.mem_append.mp hb).elim
      (h.2 a ha).2 (apart a ha)⟩

theorem successful_history_preserves_distinctness (available busy requests final : List R)
    (clean : busy.Nodup) (h : Trace (process available) busy requests final) : final.Nodup := by
  obtain ⟨ha, rfl⟩ := (trace_iff_admissible available requests busy final).mp h
  apply List.nodup_append.mpr
  refine ⟨clean, ha.1, ?_⟩
  intro a hb b hr eq
  subst b
  exact (ha.2 a hr).2 hb

end Generative.ExplanatoryCoexistence

#print axioms Generative.ExplanatoryCoexistence.admissible_cons
#print axioms Generative.ExplanatoryCoexistence.trace_iff_admissible
#print axioms Generative.ExplanatoryCoexistence.exists_trace_iff
#print axioms Generative.ExplanatoryCoexistence.final_retains_all_requests
#print axioms Generative.ExplanatoryCoexistence.empty_trace_iff_supported
#print axioms Generative.ExplanatoryCoexistence.native_plan_iff_common_holding
#print axioms Generative.ExplanatoryCoexistence.footprint_plan_has_holding_history
#print axioms Generative.ExplanatoryCoexistence.code_plan_has_holding_history
#print axioms Generative.ExplanatoryCoexistence.permutation_preserves_holding
#print axioms Generative.ExplanatoryCoexistence.frame_holding_iff
#print axioms Generative.ExplanatoryCoexistence.successful_history_preserves_distinctness
