import ReasonReplayBridge

namespace PublicationSafety

open PaidRecipientReasons
set_option maxRecDepth 8192
set_option maxHeartbeats 2000000

def RouteSafe (z : Bool) (m : ReasonReplay.Mask) : Prop :=
  (m.p=true → z=false) ∧ (m.q=true → z=true)

def prefixMask (s : State W) : ReasonReplay.Mask :=
  (ReasonReplay.paths.take (s.phase-4)).foldl
    (ReasonReplay.applyPath RecipientReasons.star (RecipientReasons.derived s.normalized)) ReasonReplay.emptyMask

def ExactPhase (s : State W) : Prop := s.phase≠0 → s.working=prefixMask s

def ActiveComplete (s : State W) : Prop := s.phase≠0 → PaidArchiveReader.Complete s.reader

def SelectedFromCurrent (s : State W) : Prop := s.phase≠0 →
  (s.normalized.first=none ∨ s.normalized.first=RecipientReasons.normalize false (s.reader.cache 0)) ∧
  (s.normalized.second=none ∨ s.normalized.second=RecipientReasons.normalize true (s.reader.cache 1)) ∧
  (s.normalized.third=none ∨ s.normalized.third=RecipientReasons.normalize false (s.reader.cache 2))

structure Invariant (z : Bool) (s : State W) : Prop where
  cache : PaidArchiveReader.CacheAgrees s.reader
  facts : PaidArchiveReader.Facts z s.reader
  normalized : RecipientReasons.Sound z s.normalized
  working : RouteSafe z s.working
  conflict : s.conflict=RecipientReasons.conflict s.normalized
  exactPhase : ExactPhase s
  complete : ActiveComplete s
  phaseBound : s.phase≤9
  publication : s.current=true → CurrentPublication s
  selected : SelectedFromCurrent s

theorem empty_normalized_sound (z : Bool) : RecipientReasons.Sound z RecipientReasons.empty := by
  simp [RecipientReasons.Sound,RecipientReasons.empty,RecipientReasons.entrySound]

theorem empty_mask_safe (z : Bool) : RouteSafe z ReasonReplay.emptyMask := by
  simp [RouteSafe,ReasonReplay.emptyMask]

theorem put_sound {z : Bool} {t : RecipientReasons.Triple} {x : Option Bool}
    (hs : RecipientReasons.Sound z t) (hx : RecipientReasons.entrySound z x) (i : Nat) :
    RecipientReasons.Sound z (put t i x) := by
  by_cases h0 : i=0
  · simp [put,h0,RecipientReasons.Sound]; exact ⟨hx,hs.2⟩
  · by_cases h1 : i=1
    · simp [put,h1,RecipientReasons.Sound]; exact ⟨hs.1,hx,hs.2.2⟩
    · simp [put,h0,h1,RecipientReasons.Sound]; exact ⟨hs.1,hs.2.1,hx⟩

theorem inferred_sound {z : Bool} {s : State W} {i : Nat} (access : Bool)
    (hi : i<3) (hc : PaidArchiveReader.Complete s.reader)
    (ha : PaidArchiveReader.CacheAgrees s.reader) (hf : PaidArchiveReader.Facts z s.reader)
    (hs : RecipientReasons.Sound z s.normalized) : RecipientReasons.Sound z (inferred s i access) := by
  apply put_sound hs
  cases access with
  | false => simp [RecipientReasons.entrySound]
  | true =>
      apply RecipientReasons.normalization_sound
      intro b hb
      exact PaidArchiveReader.completed_paid_cache_sound hc ha hf hi hb

theorem path_safe {z : Bool} {t : RecipientReasons.Triple} {m : ReasonReplay.Mask}
    (hn : RecipientReasons.Sound z t) (hm : RouteSafe z m) (p : ReasonReplay.Path) :
    RouteSafe z (ReasonReplay.applyPath RecipientReasons.star (RecipientReasons.derived t) m p) := by
  cases ho : RecipientReasons.orientation t with
  | none =>
      cases p <;> simpa [RecipientReasons.derived,ho,ReasonReplay.applyPath,ReasonReplay.endpoint,
        ReasonReplay.pathValid,ReasonReplay.edge,RecipientReasons.star,ReasonReplay.positive] using hm
  | some o =>
      have hz:=RecipientReasons.sound_orientation hn ho
      subst o
      cases z <;> cases p <;>
        simp_all [RouteSafe,RecipientReasons.derived,ReasonReplay.applyPath,ReasonReplay.endpoint,
          ReasonReplay.pathValid,ReasonReplay.edge,RecipientReasons.star,ReasonReplay.positive]

theorem step_normalized_sound {s t : State W} {e : Event} {z : Bool}
    (hi : Invariant z s) (h : Step s e t) : RecipientReasons.Sound z t.normalized := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | activate | cold => exact empty_normalized_sound z
  | infer i access => exact inferred_sound access he.2.1 he.2.2.1 hi.cache hi.facts hi.normalized
  | reader e | fund | path p | publish => exact hi.normalized

theorem step_working_safe {s t : State W} {e : Event} {z : Bool}
    (hi : Invariant z s) (h : Step s e t) : RouteSafe z t.working := by
  rcases h with ⟨_,rfl⟩
  cases e with
  | activate | cold => exact empty_mask_safe z
  | path p => exact path_safe hi.normalized hi.working p
  | reader e | fund | infer i a | publish => exact hi.working

theorem step_conflict_agrees {s t : State W} {e : Event}
    (hi : s.conflict=RecipientReasons.conflict s.normalized) (h : Step s e t) :
    t.conflict=RecipientReasons.conflict t.normalized := by
  rcases h with ⟨_,rfl⟩
  cases e with
  | activate | cold => rfl
  | infer i a => rfl
  | reader e | fund | path p | publish => exact hi

theorem step_active_complete {s t : State W} {e : Event}
    (_hi : ActiveComplete s) (h : Step s e t) : ActiveComplete t := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | reader e | cold => simp [ActiveComplete,advance]
  | fund => simp [ActiveComplete,advance,he.1]
  | activate => intro _; exact he.2.2.1
  | infer i a => intro _; exact he.2.2.1
  | path p => intro _; exact he.2.1
  | publish => intro _; exact he.2

theorem step_phase_bound {s t : State W} {e : Event}
    (hi : s.phase≤9) (h : Step s e t) : t.phase≤9 := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | reader e | activate | publish | cold => simp [advance]
  | fund => exact hi
  | infer i a => simp [advance]; have h1:=he.1; have h2:=he.2.1; omega
  | path p => cases p <;> simp [advance] <;> simp [Enabled,ReasonReplay.pathIndex] at he <;> omega

theorem step_exact_phase {s t : State W} {e : Event}
    (hi : ExactPhase s) (h : Step s e t) : ExactPhase t := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | reader e | cold => simp [ExactPhase,advance]
  | fund => simp [ExactPhase,advance,he.1]
  | activate => simp [ExactPhase,prefixMask,advance]
  | infer i a =>
      have hb : i=0 ∨ i=1 ∨ i=2 := by have hh:=he.2.1; omega
      have hp:=he.1
      have hw:=hi (by omega)
      rcases hb with rfl|rfl|rfl <;>
        simpa [ExactPhase,prefixMask,advance,hp] using hw
  | path p =>
      have hp:=he.1
      have hn : s.phase≠0 := by cases p <;> simp [ReasonReplay.pathIndex] at hp <;> omega
      have hw:=hi hn
      cases p <;> simp only [ReasonReplay.pathIndex] at hp <;>
        simp [prefixMask,hp,ReasonReplay.paths] at hw <;>
        simp [ExactPhase,prefixMask,advance,hp,ReasonReplay.paths,hw]
  | publish =>
      have hp:=he.1
      have hw:=hi (by omega)
      simpa [ExactPhase,prefixMask,advance,hp,ReasonReplay.paths] using hw

theorem step_current_valid {s t : State W} {e : Event}
    (hi : s.current=true → CurrentPublication s) (h : Step s e t) :
    t.current=true → CurrentPublication t := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | reader e | activate | cold => simp [advance]
  | publish => intro _; exact ⟨rfl,rfl,he.2,rfl⟩
  | fund =>
      intro hc
      have hp:=(hi hc).2.1
      have h0:=he.1
      omega
  | infer i a =>
      intro hc
      have hp:=(hi hc).2.1
      have h1:=he.1; have h2:=he.2.1
      omega
  | path p =>
      intro hc
      have hp:=(hi hc).2.1
      have h1:=he.1
      cases p <;> simp [ReasonReplay.pathIndex] at h1 <;> omega

theorem step_selected_current {s t : State W} {e : Event}
    (hi : SelectedFromCurrent s) (h : Step s e t) : SelectedFromCurrent t := by
  rcases h with ⟨he,rfl⟩
  cases e with
  | reader e | cold => simp [SelectedFromCurrent,advance]
  | fund => simp [SelectedFromCurrent,advance,he.1]
  | activate => simp [SelectedFromCurrent,advance,RecipientReasons.empty]
  | infer i a =>
      have hp:=he.1
      have hn : s.phase≠0 := by omega
      have hold:=hi hn
      have hb : i=0 ∨ i=1 ∨ i=2 := by have hlt:=he.2.1; omega
      rcases hb with rfl|rfl|rfl
      · cases a <;> simp [SelectedFromCurrent,advance,inferred,put,RecipientArchive.designated,debit]
        all_goals exact hold.2
      · cases a <;> simp [SelectedFromCurrent,advance,inferred,put,RecipientArchive.designated,debit]
        all_goals exact ⟨hold.1,hold.2.2⟩
      · cases a <;> simp [SelectedFromCurrent,advance,inferred,put,RecipientArchive.designated,debit]
        all_goals exact ⟨hold.1,hold.2.1⟩
  | path p =>
      have hp:=he.1
      have hn : s.phase≠0 := by cases p <;> simp [ReasonReplay.pathIndex] at hp <;> omega
      intro _
      exact hi hn
  | publish =>
      intro _
      exact hi (by have hp:=he.1; omega)

theorem initial_invariant {z : Bool} (reader : PaidArchiveReader.State W) (reserve : Nat)
    (hc : PaidArchiveReader.CacheAgrees reader) (hf : PaidArchiveReader.Facts z reader) :
    Invariant z (initial reader reserve) := by
  exact ⟨hc,hf,empty_normalized_sound z,empty_mask_safe z,rfl,
    by simp [ExactPhase,initial],by simp [ActiveComplete,initial],by simp [initial],by simp [initial],by simp [SelectedFromCurrent,initial]⟩

theorem step_invariant {z : Bool} {s t : State W} {e : Event}
    (hi : Invariant z s) (h : Step s e t) : Invariant z t := by
  refine ⟨step_cache_agrees hi.cache h,?_,step_normalized_sound hi h,
    step_working_safe hi h,step_conflict_agrees hi.conflict h,
    step_exact_phase hi.exactPhase h,step_active_complete hi.complete h,
    step_phase_bound hi.phaseBound h,step_current_valid hi.publication h,step_selected_current hi.selected h⟩
  intro i r hr
  rw [step_preserves_archive h] at hr
  exact hi.facts i r hr

theorem trace_invariant {z : Bool} {s t : State W} {es : List Event}
    (hi : Invariant z s) (h : Generative.Trace (process W) s es t) : Invariant z t := by
  induction h with
  | nil => exact hi
  | cons hs _ ih => exact ih (step_invariant hi hs)

theorem route_meaning {z : Bool} {m : ReasonReplay.Mask} {G : Prop}
    (root : G) (safe : RouteSafe z m) {v : ReasonReplay.Node} (hv : m.has v) :
    RecipientReasons.Meaning G z v := by
  cases v with
  | root => exact root
  | p => exact ⟨root,(RecipientReasons.compatible_iff _ _).mpr (safe.1 hv).symm⟩
  | q => exact ⟨root,(RecipientReasons.compatible_iff _ _).mpr (safe.2 hv).symm⟩

theorem invariant_publication_sound {z : Bool} {s : State W} {G : Prop}
    (root : G) (hi : Invariant z s) (hc : CurrentPublication s)
    {context : Bool} {mask : ReasonReplay.Mask} (hp : s.published=some (context,mask))
    {v : ReasonReplay.Node} (hm : mask.has v) : RecipientReasons.Meaning G z v := by
  have he:=hp.symm.trans hc.2.2.2
  have hmEq : mask=s.working := (Prod.mk.inj (Option.some.inj he)).2
  subst mask
  exact route_meaning root hi.working hm

theorem invariant_publication_exact {z : Bool} {s : State W}
    (hi : Invariant z s) (hc : CurrentPublication s) :
    s.working=ReasonReplay.closureMask RecipientReasons.star (RecipientReasons.derived s.normalized) := by
  have he:=hi.exactPhase (by rw [hc.2.1]; decide)
  simpa [prefixMask,hc.2.1,ReasonReplay.paths,ReasonReplay.closureMask] using he

theorem invariant_no_conflict {z : Bool} {s : State W} (hi : Invariant z s) : s.conflict=false := by
  rw [hi.conflict]
  exact RecipientReasons.sound_no_conflict hi.normalized

end PublicationSafety

#print axioms PublicationSafety.empty_normalized_sound
#print axioms PublicationSafety.empty_mask_safe
#print axioms PublicationSafety.put_sound
#print axioms PublicationSafety.inferred_sound
#print axioms PublicationSafety.path_safe
#print axioms PublicationSafety.step_normalized_sound
#print axioms PublicationSafety.step_working_safe
#print axioms PublicationSafety.step_conflict_agrees
#print axioms PublicationSafety.step_active_complete
#print axioms PublicationSafety.step_phase_bound
#print axioms PublicationSafety.step_exact_phase
#print axioms PublicationSafety.step_current_valid
#print axioms PublicationSafety.step_selected_current
#print axioms PublicationSafety.initial_invariant
#print axioms PublicationSafety.step_invariant
#print axioms PublicationSafety.trace_invariant
#print axioms PublicationSafety.route_meaning
#print axioms PublicationSafety.invariant_publication_sound
#print axioms PublicationSafety.invariant_publication_exact
#print axioms PublicationSafety.invariant_no_conflict
