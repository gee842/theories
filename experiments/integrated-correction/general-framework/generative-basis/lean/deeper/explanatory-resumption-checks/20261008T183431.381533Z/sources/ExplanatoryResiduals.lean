import ExplanatoryGuardedPrograms

/-! Partial unfolding retains the remaining organization and reached native
conditions together. Administrative steps describe recipe semantics, not extra
physical events. Native traces below erase only that explicit bookkeeping. -/
set_option autoImplicit false

namespace Generative.ExplanatoryResiduals
open ExplanatoryBranching ExplanatoryGuardedPrograms
universe u v w
variable {S : Type u} {A : Type v} {O : Type w}

inductive Advance (m : Model S A O) : (Program A O × S) → (Program A O × S) → Prop where
  | action {s t a} : m.process.step s a t → Advance m (.action a, s) (.skip, t)
  | guard {s q} : Holds m s q → Advance m (.guard q, s) (.skip, s)
  | seqSkip (q : Program A O) (s : S) : Advance m (.seq .skip q, s) (q, s)
  | seq {p p' q : Program A O} {s t} : Advance m (p, s) (p', t) →
      Advance m (.seq p q, s) (.seq p' q, t)
  | left (p q : Program A O) (s : S) : Advance m (.choice p q, s) (p, s)
  | right (p q : Program A O) (s : S) : Advance m (.choice p q, s) (q, s)

def unfolding (m : Model S A O) : Process (Program A O × S) Unit where
  step c _ d := Advance m c d

def Cut (m : Model S A O) (p : Program A O) (s : S) (r : Program A O) (t : S) : Prop :=
  ∃ schedule, Trace (unfolding m) (p, s) schedule (r, t)

theorem advance_resume {m : Model S A O} {c d : Program A O × S}
    (h : Advance m c d) {finish : S} (tail : Executes m d.1 d.2 finish) :
    Executes m c.1 c.2 finish := by
  induction h generalizing finish with
  | action step => exact tail ▸ step
  | guard test => exact ⟨tail, test⟩
  | seqSkip q s => exact ⟨s, rfl, tail⟩
  | @seq p p' q s t step ih =>
    obtain ⟨middle, hp, hq⟩ := tail
    exact ⟨middle, ih hp, hq⟩
  | left p q s => exact Or.inl tail
  | right p q s => exact Or.inr tail

theorem trace_resume {m : Model S A O} {c d : Program A O × S} {schedule : List Unit}
    (h : Trace (unfolding m) c schedule d) {finish : S}
    (tail : Executes m d.1 d.2 finish) : Executes m c.1 c.2 finish := by
  induction h with
  | nil c => exact tail
  | cons step rest ih => exact advance_resume step (ih tail)

theorem cut_resume {m : Model S A O} {p r : Program A O} {s t finish : S}
    (h : Cut m p s r t) (tail : Executes m r t finish) : Executes m p s finish := by
  obtain ⟨schedule, path⟩ := h
  exact trace_resume path tail

theorem advance_has_native_trace {m : Model S A O} {c d : Program A O × S}
    (h : Advance m c d) : ∃ word, Trace m.process c.2 word d.2 := by
  induction h with
  | action step => exact ⟨[_], .cons step (.nil _)⟩
  | guard test => exact ⟨[], .nil _⟩
  | seqSkip q s => exact ⟨[], .nil _⟩
  | seq step ih => exact ih
  | left p q s => exact ⟨[], .nil _⟩
  | right p q s => exact ⟨[], .nil _⟩

theorem residual_trace_has_native_trace {m : Model S A O} {c d : Program A O × S}
    {schedule : List Unit} (h : Trace (unfolding m) c schedule d) :
    ∃ word, Trace m.process c.2 word d.2 := by
  induction h with
  | nil c => exact ⟨[], .nil _⟩
  | cons step rest ih =>
    obtain ⟨first, hf⟩ := advance_has_native_trace step
    obtain ⟨last, hl⟩ := ih
    exact ⟨first ++ last, trace_append_iff.mpr ⟨_, hf, hl⟩⟩

theorem cut_trans {m : Model S A O} {p q r : Program A O} {s t u : S}
    (h : Cut m p s q t) (k : Cut m q t r u) : Cut m p s r u := by
  obtain ⟨first, hf⟩ := h; obtain ⟨last, hl⟩ := k
  exact ⟨first ++ last, trace_append_iff.mpr ⟨_, hf, hl⟩⟩

theorem cut_sequence {m : Model S A O} {p r : Program A O} {s t : S}
    (h : Cut m p s r t) (q : Program A O) : Cut m (.seq p q) s (.seq r q) t := by
  obtain ⟨schedule, path⟩ := h
  refine ⟨schedule, ?_⟩
  exact trace_map (Q := unfolding m) (f := fun c => (Program.seq c.1 q, c.2))
    (fun _ _ _ step => Advance.seq step) path

theorem execution_reaches_skip (m : Model S A O) (p : Program A O) {s t : S}
    (h : Executes m p s t) : Cut m p s .skip t := by
  induction p generalizing s t with
  | skip => subst t; exact ⟨[], .nil _⟩
  | action a => exact ⟨[()], .cons (.action h) (.nil _)⟩
  | guard q =>
    obtain ⟨rfl, hq⟩ := h
    exact ⟨[()], .cons (.guard hq) (.nil _)⟩
  | seq p q ihp ihq =>
    obtain ⟨middle, hp, hq⟩ := h
    have first := cut_sequence (ihp hp) q
    have next : Cut m (.seq .skip q) middle q middle :=
      ⟨[()], .cons (.seqSkip q middle) (.nil _)⟩
    exact cut_trans (cut_trans first next) (ihq hq)
  | choice p q ihp ihq =>
    rcases h with hp | hq
    · exact cut_trans ⟨[()], .cons (.left p q s) (.nil _)⟩ (ihp hp)
    · exact cut_trans ⟨[()], .cons (.right p q s) (.nil _)⟩ (ihq hq)

theorem execution_iff_completed_cut (m : Model S A O) (p : Program A O) (s t : S) :
    Executes m p s t ↔ Cut m p s .skip t :=
  ⟨execution_reaches_skip m p, fun h => cut_resume h rfl⟩

/-- Same reached-position answers preserve all finite guarded continuation
questions, even without finite branching. This does not assert each native
endpoint matches or that inserted activity actually preserves these answers. -/
theorem same_preserves_resumption {m : Model S A O} {s t : S} (same : Same m m s t)
    (r : Program A O) (q : Test A O) :
    (∃ finish, Executes m r s finish ∧ Holds m finish q) ↔
      ∃ finish, Executes m r t finish ∧ Holds m finish q :=
  (diamond_correct m r q s).symm.trans
    ((same (diamond r q)).trans (diamond_correct m r q t))


/-- With the same finite recipe syntax and complete native question agreement,
every partial advance matches, preserving BOTH pending recipe and answers at
the reached position. Stronger coverage than macro-only agreement is explicit. -/
theorem advance_matches {T : Type u} {m : Model S A O} {n : Model T A O}
    (hn : ImageFinite n) {c d : Program A O × S} {t : T}
    (h : Advance m c d) (same : Same m n c.2 t) :
    ∃ t', Advance n (c.1, t) (d.1, t') ∧ Same m n d.2 t' := by
  induction h generalizing t with
  | action step =>
    obtain ⟨t', ht, hs⟩ := same_forces_successor_match hn same step
    exact ⟨t', .action ht, hs⟩
  | guard test => exact ⟨t, .guard ((same _).mp test), same⟩
  | seqSkip q s => exact ⟨t, .seqSkip q t, same⟩
  | seq step ih =>
    obtain ⟨t', ht, hs⟩ := ih same
    exact ⟨t', .seq ht, hs⟩
  | left p q s => exact ⟨t, .left p q t, same⟩
  | right p q s => exact ⟨t, .right p q t, same⟩

theorem partial_history_matches {T : Type u} {m : Model S A O} {n : Model T A O}
    (hn : ImageFinite n) {p r : Program A O} {s s' : S} {t : T}
    (h : Cut m p s r s') (same : Same m n s t) :
    ∃ t', Cut n p t r t' ∧ Same m n s' t' := by
  obtain ⟨schedule, path⟩ := h
  have liftPath : ∀ {c d : Program A O × S} {bs : List Unit} {t : T},
      Trace (unfolding m) c bs d → Same m n c.2 t →
      ∃ t', Trace (unfolding n) (c.1, t) bs (d.1, t') ∧ Same m n d.2 t' := by
    intro c d bs t ht he
    induction ht generalizing t with
    | nil c => exact ⟨t, .nil _, he⟩
    | cons step rest ih =>
      obtain ⟨middle, hs, he'⟩ := advance_matches hn step he
      obtain ⟨last, hl, final⟩ := ih he'
      exact ⟨last, .cons hs hl, final⟩
  obtain ⟨t', ht, hs⟩ := liftPath path same
  exact ⟨t', ⟨schedule, ht⟩, hs⟩


/-- Resumption after inserted native activity keeps the actual prefix,
interruption and suffix in one native trace. This deliberately does NOT claim
the inserted history was an execution of the uninterrupted original recipe. -/
theorem resumption_after_inserted_history {m : Model S A O}
    {p r : Program A O} {s reached current finish : S} {inserted : List A}
    (cut : Cut m p s r reached) (change : Trace m.process reached inserted current)
    (resume : Executes m r current finish) :
    ∃ first last, Trace m.process s first reached ∧ Trace m.process current last finish ∧
      Trace m.process s (first ++ inserted ++ last) finish := by
  obtain ⟨schedule, leadPath⟩ := cut
  obtain ⟨first, hf⟩ := residual_trace_has_native_trace leadPath
  obtain ⟨last, hl⟩ := execution_has_native_trace m r resume
  exact ⟨first, last, hf, hl, trace_append_iff.mpr
    ⟨current, trace_append_iff.mpr ⟨reached, hf, change⟩, hl⟩⟩

end Generative.ExplanatoryResiduals

#print axioms Generative.ExplanatoryResiduals.advance_resume
#print axioms Generative.ExplanatoryResiduals.trace_resume
#print axioms Generative.ExplanatoryResiduals.cut_resume
#print axioms Generative.ExplanatoryResiduals.advance_has_native_trace
#print axioms Generative.ExplanatoryResiduals.residual_trace_has_native_trace
#print axioms Generative.ExplanatoryResiduals.cut_trans
#print axioms Generative.ExplanatoryResiduals.cut_sequence
#print axioms Generative.ExplanatoryResiduals.execution_reaches_skip
#print axioms Generative.ExplanatoryResiduals.execution_iff_completed_cut
#print axioms Generative.ExplanatoryResiduals.same_preserves_resumption

#print axioms Generative.ExplanatoryResiduals.advance_matches
#print axioms Generative.ExplanatoryResiduals.partial_history_matches

#print axioms Generative.ExplanatoryResiduals.resumption_after_inserted_history
