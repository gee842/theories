import EmbeddedEvaluation

/-!
# Which evaluation persists, from the generative core alone

An evaluation inside the process is itself an activity `e`. It *persists from `s`* when,
for every length, some actual continuation from `s` at least that long ends where `e` is
still eventually realizable. This module characterizes persistence using only
`Process`/`Trace`, with no imported model, no supplied rates or kinds, and no axioms.

* **Persistence needs a regenerating whole.** In a process with finitely many states,
  `e` persists from `s` exactly when `s` can reach a state `c` that the process
  regenerates, by a nonempty actual path from `c` back to `c`, and `e` is eventually
  realizable at `c` (`persists_iff_regenerating_return`). One direction
  (`regenerating_return_gives_persistence`) holds in every process.
* **The regenerating whole loses nothing.** Along such a return path, every activity is
  eventually realizable at each visited state exactly when it is at `c`
  (`return_preserves_realizability`). At the level of eventual realizability, the whole
  on which an evaluation persists damages no activity, the evaluation's own included.

So the evaluations that can persist are exactly those that can reach a whole that
regenerates the conditions of its own later realization, and that whole is non-damaging
in this sense. This does not say which such whole a history reaches, and "eventually
realizable" is existence of a path, not probability or experience.
-/

namespace Generative.Naturalism

universe u v

variable {State : Type u} {Action : Type v}

/-! ## Finite bookkeeping without library lemmas -/

theorem mem_or_not [DecidableEq State] (x : State) : (l : List State) → x ∈ l ∨ ¬ x ∈ l
  | [] => Or.inr (fun h => nomatch h)
  | a :: l =>
    match decEq x a with
    | isTrue h => Or.inl (h ▸ List.Mem.head _)
    | isFalse h =>
      match mem_or_not x l with
      | Or.inl hl => Or.inl (List.Mem.tail _ hl)
      | Or.inr hl => Or.inr (fun hm => by
          cases hm with
          | head => exact h rfl
          | tail _ hm => exact hl hm)

def eraseOne [DecidableEq State] (a : State) : List State → List State
  | [] => []
  | b :: l =>
    match decEq a b with
    | isTrue _ => l
    | isFalse _ => b :: eraseOne a l

theorem eraseOne_length [DecidableEq State] (a : State) :
    (l : List State) → a ∈ l → (eraseOne a l).length + 1 = l.length
  | [], h => nomatch h
  | b :: l, h => by
    unfold eraseOne
    match decEq a b, h with
    | isTrue _, _ => rfl
    | isFalse hne, List.Mem.head _ => exact absurd rfl hne
    | isFalse _, List.Mem.tail _ hl =>
      show (eraseOne a l).length + 1 + 1 = l.length + 1
      rw [eraseOne_length a l hl]

theorem mem_eraseOne_or [DecidableEq State] (a x : State) :
    (l : List State) → x ∈ l → x = a ∨ x ∈ eraseOne a l
  | [], h => nomatch h
  | b :: l, h => by
    unfold eraseOne
    match decEq a b, h with
    | isTrue e, List.Mem.head _ => exact Or.inl e.symm
    | isTrue _, List.Mem.tail _ hl => exact Or.inr hl
    | isFalse _, List.Mem.head _ => exact Or.inr (List.Mem.head _)
    | isFalse _, List.Mem.tail _ hl =>
      cases mem_eraseOne_or a x l hl with
      | inl e => exact Or.inl e
      | inr hm => exact Or.inr (List.Mem.tail _ hm)

/-! ## A long enough continuation returns to a state it has visited -/

/-- Search along a trace, keeping the states already visited (`seen`) and those not yet
visited (`pool`). -/
theorem trace_returns [DecidableEq State] {P : Process State Action} {s₀ : State} :
    (word : List Action) → (s t : State) → (seen pool : List State) →
    Trace P s word t → pool.length ≤ word.length →
    (∀ x, x ∈ seen ∨ x ∈ pool) →
    (∃ w0, Trace P s₀ w0 s) →
    (∀ x, x ∈ seen → ∃ w, w ≠ [] ∧ Trace P x w s ∧ ∃ w1, Trace P s₀ w1 x) →
    ∃ c, (∃ w1, Trace P s₀ w1 c) ∧ (∃ w2, w2 ≠ [] ∧ Trace P c w2 c) ∧ ∃ w3, Trace P c w3 t
  | word, s, t, seen, pool, ht, hlen, cover, hreach, hseen => by
    cases mem_or_not s seen with
    | inl hs =>
      obtain ⟨w, hw, hcyc, hr⟩ := hseen s hs
      exact ⟨s, hr, ⟨w, hw, hcyc⟩, ⟨word, ht⟩⟩
    | inr hs =>
      have hp : s ∈ pool := by
        cases cover s with
        | inl h => exact absurd h hs
        | inr h => exact h
      cases word with
      | nil =>
        cases pool with
        | nil => exact nomatch hp
        | cons _ _ => exact absurd hlen (Nat.not_succ_le_zero _)
      | cons a rest =>
        obtain ⟨m, hsm, hmt⟩ := trace_cons_iff.mp ht
        have hl := eraseOne_length s pool hp
        refine trace_returns rest m t (s :: seen) (eraseOne s pool) hmt ?_ ?_ ?_ ?_
        · have : (eraseOne s pool).length + 1 ≤ rest.length + 1 := hl ▸ hlen
          exact Nat.le_of_succ_le_succ this
        · intro x
          cases cover x with
          | inl h => exact Or.inl (List.Mem.tail _ h)
          | inr h =>
            cases mem_eraseOne_or s x pool h with
            | inl e => exact Or.inl (e ▸ List.Mem.head _)
            | inr h' => exact Or.inr h'
        · obtain ⟨w0, h0⟩ := hreach
          exact ⟨w0 ++ [a], trace_append_iff.mpr ⟨s, h0, .cons hsm (.nil m)⟩⟩
        · intro x hx
          cases hx with
          | head =>
            refine ⟨[a], ?_, Trace.cons hsm (Trace.nil m), hreach⟩
            intro h
            cases h
          | tail _ hx =>
            obtain ⟨w, hw, hxs, hr⟩ := hseen x hx
            refine ⟨w ++ [a], ?_, trace_append_iff.mpr ⟨s, hxs, .cons hsm (.nil m)⟩, hr⟩
            cases w with
            | nil => exact absurd rfl hw
            | cons _ _ => intro h; cases h

/-! ## Persistence -/

/-- Arbitrarily long actual continuations from `s` end where `e` is eventually realizable. -/
def PersistsFrom (P : Process State Action) (s : State) (e : Action) : Prop :=
  ∀ n, ∃ word t, n ≤ word.length ∧ Trace P s word t ∧ Can P t e

def loopWord (w : List Action) : Nat → List Action
  | 0 => []
  | k + 1 => w ++ loopWord w k

theorem loop_trace {P : Process State Action} {c : State} {w : List Action}
    (h : Trace P c w c) : (k : Nat) → Trace P c (loopWord w k) c
  | 0 => .nil c
  | k + 1 => trace_append_iff.mpr ⟨c, h, loop_trace h k⟩

theorem length_append_word : (xs ys : List Action) → (xs ++ ys).length = xs.length + ys.length
  | [], ys => (Nat.zero_add ys.length).symm
  | _ :: xs, ys => by
    show (xs ++ ys).length + 1 = xs.length + 1 + ys.length
    rw [length_append_word xs ys, Nat.add_right_comm]

theorem loop_length {w : List Action} (hw : w ≠ []) : (k : Nat) → k ≤ (loopWord w k).length
  | 0 => Nat.zero_le _
  | k + 1 => by
    show k + 1 ≤ (w ++ loopWord w k).length
    rw [length_append_word]
    have h1 : 1 ≤ w.length := by
      cases w with
      | nil => exact absurd rfl hw
      | cons _ _ => exact Nat.succ_le_succ (Nat.zero_le _)
    have := Nat.add_le_add h1 (loop_length hw k)
    rw [Nat.add_comm 1 k] at this
    exact this

/-- In every process, reaching a regenerated state where `e` is realizable gives persistence. -/
theorem regenerating_return_gives_persistence {P : Process State Action} {s c : State}
    {e : Action} (hreach : ∃ w1, Trace P s w1 c) (hcyc : ∃ w2, w2 ≠ [] ∧ Trace P c w2 c)
    (he : Can P c e) : PersistsFrom P s e := by
  intro n
  obtain ⟨w1, h1⟩ := hreach
  obtain ⟨w2, hw2, h2⟩ := hcyc
  refine ⟨w1 ++ loopWord w2 n, c, ?_, trace_append_iff.mpr ⟨c, h1, loop_trace h2 n⟩, he⟩
  rw [length_append_word]
  exact Nat.le_trans (loop_length hw2 n) (Nat.le_add_left _ _)

/-- With finitely many states, persistence is exactly reaching a regenerated state where
`e` is eventually realizable. -/
theorem persists_iff_regenerating_return [DecidableEq State] {P : Process State Action}
    (U : List State) (complete : ∀ x, x ∈ U) (s : State) (e : Action) :
    PersistsFrom P s e ↔
      ∃ c, (∃ w1, Trace P s w1 c) ∧ (∃ w2, w2 ≠ [] ∧ Trace P c w2 c) ∧ Can P c e := by
  constructor
  · intro h
    obtain ⟨word, t, hlen, ht, he⟩ := h U.length
    obtain ⟨c, hr, hc, w3, h3⟩ := trace_returns (s₀ := s) word s t [] U ht hlen
      (fun x => Or.inr (complete x)) ⟨[], .nil s⟩ (fun _ hx => nomatch hx)
    exact ⟨c, hr, hc, can_of_reach h3 he⟩
  · rintro ⟨c, hr, hc, he⟩
    exact regenerating_return_gives_persistence hr hc he

/-- On a return path, every activity's eventual realizability is the same as at `c`. -/
theorem return_preserves_realizability {P : Process State Action} {c m : State}
    {u v : List Action} (hu : Trace P c u m) (hv : Trace P m v c) (b : Action) :
    Can P m b ↔ Can P c b :=
  Iff.intro (fun h => can_of_reach hu h) (fun h => can_of_reach hv h)

end Generative.Naturalism

#print axioms Generative.Naturalism.mem_or_not
#print axioms Generative.Naturalism.eraseOne_length
#print axioms Generative.Naturalism.mem_eraseOne_or
#print axioms Generative.Naturalism.trace_returns
#print axioms Generative.Naturalism.loop_trace
#print axioms Generative.Naturalism.length_append_word
#print axioms Generative.Naturalism.loop_length
#print axioms Generative.Naturalism.regenerating_return_gives_persistence
#print axioms Generative.Naturalism.persists_iff_regenerating_return
#print axioms Generative.Naturalism.return_preserves_realizability
