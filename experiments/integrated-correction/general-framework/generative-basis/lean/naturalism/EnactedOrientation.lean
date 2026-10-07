import RegeneratingPersistence

/-!
# Which orientation can be enacted indefinitely

`EmbeddedEvaluation` showed that one law admits records in both orientations, and
`PremiseNecessity` that the formal credentials do not fix the orientation. Those
comparisons concern records that change nothing: a record neither enables nor blocks
any activity (`recording_enabled_iff`). This module asks what happens when an
evaluation is *enacted*, that is, when the transitions it endorses are transitions
of the history. A marking `Q` picks out the enacted transitions; nothing else is
supplied.

At the level of eventual realizability (`Can`), the level at which persistence is
defined in `RegeneratingPersistence`, the two orientations are not mirror images:

* **No transition gains.** No actual transition makes an activity eventually
  realizable that was not already (`no_transition_gains`). So the loss orientation
  (`converse (CanLe P)`) holds across every actual transition of every history
  (`loss_order_along_every_history`): read non-strictly, it endorses whatever
  happens and distinguishes nothing. Continuation inclusion (`CanLe P`) does
  distinguish: it fails on every transition that loses (`loses_not_canLe`).
* **Loss cannot be enacted indefinitely.** With finitely many states, no history
  contains as many transitions that lose eventual realizability as there are states
  (`strict_loss_bounded`). Any evaluation that endorses only losing transitions can
  be enacted fewer times than there are states, along any history
  (`loss_endorsing_enactment_bounded`). Whatever a marking endorses, if it recurs
  without bound then not all of its reachable enactments lose
  (`recurring_enactment_not_all_loss`). These bounds use only a complete list of
  states, not decidable equality: the start of a losing transition is never reached
  again, so each one closes off a state (`loss_marked_bound`).
* **What recurs keeps.** If transitions of a marking recur without bound, some marked
  transition reachable from the start lies on a return path, and that transition keeps
  every activity's eventual realizability (`recurring_enactment_keeps`; this positive
  form locates the transition and so uses decidable equality of states, as
  `persists_iff_regenerating_return` does). Both
  orientations agree on such a transition (`return_transition_both_orders`). An
  activity enacted without bound persists (`unbounded_enactment_persists`).

So, at this level, persistence of enactment derives the generative direction for
what is enacted indefinitely. It does not derive more:

* **Loss can precede persistence.** In `severing`, a transition removes an activity
  for good, and the evaluating activity persists afterwards
  (`loss_then_persistence`). Persistence bounds enacted loss; it does not exclude it.
* **The bound needs finitely many states.** In `ladder` every transition loses an
  activity and losing transitions recur without bound (`ladder_loss_recurs`).
* **At the level of immediate feasibility the orientation stays open.** In `dip`,
  transitions that fail `ContinuationLe` recur without bound
  (`dip_immediate_loss_recurs`), each recovered on the same return path. The
  counterexample `law_admits_opposite_recordings` stands at that level.

Nothing here identifies persistence with good. The eventual level still counts
every exclusive commitment as a loss (`every_exclusive_choice_registers_as_damage`
in `NaturalismReview` is the immediate-level version; the eventual version is in
`ProtectedScope`).
-/

namespace Generative.Naturalism

open Generative.EthicalOrientation

universe u v

variable {State : Type u} {Action : Type v}

/-! ## Reachability and the two orientations at the eventual level -/

/-- Some actual path leads from `s` to `t`. -/
def Reach (P : Process State Action) (s t : State) : Prop :=
  ∃ w, Trace P s w t

theorem reach_step {P : Process State Action} {s m : State} {a : Action} {x : State}
    (h : Reach P x s) (hs : P.step s a m) : Reach P x m := by
  obtain ⟨w, hw⟩ := h
  exact ⟨w ++ [a], trace_append_iff.mpr ⟨s, hw, .cons hs (.nil m)⟩⟩

theorem reach_cons {P : Process State Action} {s m t : State} {a : Action}
    (hs : P.step s a m) (h : Reach P m t) : Reach P s t := by
  obtain ⟨w, hw⟩ := h
  exact ⟨a :: w, .cons hs hw⟩

/-- Everything eventually realizable from `s` is still eventually realizable from `t`. -/
def CanLe (P : Process State Action) (s t : State) : Prop :=
  ∀ b, Can P s b → Can P t b

/-- Some activity eventually realizable from `s` no longer is from `t`. -/
def Loses (P : Process State Action) (s t : State) : Prop :=
  ∃ b, Can P s b ∧ ¬ Can P t b

/-- Some activity eventually realizable from `t` was not from `s`. -/
def Gains (P : Process State Action) (s t : State) : Prop :=
  ∃ b, Can P t b ∧ ¬ Can P s b

theorem loses_not_canLe {P : Process State Action} {s t : State}
    (h : Loses P s t) : ¬ CanLe P s t := by
  intro hle
  obtain ⟨b, hb, hnb⟩ := h
  exact hnb (hle b hb)

/-- No actual transition gains eventual realizability. -/
theorem no_transition_gains {P : Process State Action} {s t : State} {a : Action}
    (h : P.step s a t) : ¬ Gains P s t := by
  rintro ⟨b, hb, hnb⟩
  exact hnb (can_of_reach (.cons h (.nil t)) hb)

/-- The loss orientation holds across every actual transition. -/
theorem loss_order_endorses_every_transition {P : Process State Action} {s t : State}
    {a : Action} (h : P.step s a t) : converse (CanLe P) s t :=
  fun _ hb => can_of_reach (.cons h (.nil t)) hb

/-- Hence it holds along every history: it distinguishes no history from another. -/
theorem loss_order_along_every_history {P : Process State Action} :
    {s t : State} → (r : Run P s t) → Along (converse (CanLe P)) r
  | _, _, .nil _ => True.intro
  | _, _, .cons _ h r => ⟨loss_order_endorses_every_transition h, loss_order_along_every_history r⟩

/-- A transition whose end can return to its start keeps every eventual realizability,
and both orientations endorse it. -/
theorem return_transition_keeps {P : Process State Action} {x y : State} {a : Action}
    (h : P.step x a y) (hback : Reach P y x) (b : Action) : Can P x b ↔ Can P y b := by
  obtain ⟨w, hw⟩ := hback
  exact Iff.intro (fun hx => can_of_reach hw hx) (fun hy => can_of_reach (.cons h (.nil y)) hy)

theorem return_transition_both_orders {P : Process State Action} {x y : State} {a : Action}
    (h : P.step x a y) (hback : Reach P y x) :
    CanLe P x y ∧ converse (CanLe P) x y :=
  ⟨fun b => (return_transition_keeps h hback b).mp,
    fun b => (return_transition_keeps h hback b).mpr⟩

/-! ## Enactment: histories with at least `n` marked transitions -/

/-- A history from `s` to `t` with at least `n` transitions marked by `Q`. -/
inductive Marked (P : Process State Action) (Q : State → Action → State → Prop) :
    State → Nat → State → Prop where
  | nil (s : State) : Marked P Q s 0 s
  | pass {s m t : State} {a : Action} {n : Nat} :
      P.step s a m → Marked P Q m n t → Marked P Q s n t
  | mark {s m t : State} {a : Action} {n : Nat} :
      P.step s a m → Q s a m → Marked P Q m n t → Marked P Q s (n + 1) t

/-- Marked transitions recur without bound from `s`. -/
def RecursUnboundedly (P : Process State Action) (Q : State → Action → State → Prop)
    (s : State) : Prop :=
  ∀ n, ∃ t, Marked P Q s n t

/-- Search along a history, keeping the starts of marked transitions already passed
(`seen`) and the states not yet seen (`pool`). -/
theorem marked_returns [DecidableEq State] {P : Process State Action}
    {Q : State → Action → State → Prop} {s₀ s t : State} {n : Nat}
    (h : Marked P Q s n t) : (seen pool : List State) → pool.length ≤ n →
    (∀ x, x ∈ seen ∨ x ∈ pool) → Reach P s₀ s →
    (∀ x, x ∈ seen → Reach P s₀ x ∧ ∃ a y, P.step x a y ∧ Q x a y ∧ Reach P y s) →
    ∃ x a y, Reach P s₀ x ∧ P.step x a y ∧ Q x a y ∧ Reach P y x := by
  induction h with
  | nil s =>
    intro seen pool hlen cover _ hseen
    cases mem_or_not s seen with
    | inl hs =>
      obtain ⟨hx, a, y, hst, hq, hy⟩ := hseen s hs
      exact ⟨s, a, y, hx, hst, hq, hy⟩
    | inr hs =>
      have hp : s ∈ pool := by
        cases cover s with
        | inl h => exact absurd h hs
        | inr h => exact h
      cases pool with
      | nil => exact nomatch hp
      | cons _ _ => exact absurd hlen (Nat.not_succ_le_zero _)
  | pass hsm _ ih =>
    intro seen pool hlen cover hr hseen
    refine ih seen pool hlen cover (reach_step hr hsm) ?_
    intro x hx
    obtain ⟨h1, a, y, h2, h3, h4⟩ := hseen x hx
    exact ⟨h1, a, y, h2, h3, reach_step h4 hsm⟩
  | @mark s m _ a n hsm hq _ ih =>
    intro seen pool hlen cover hr hseen
    cases mem_or_not s seen with
    | inl hs =>
      obtain ⟨hx, a', y, hst, hq', hy⟩ := hseen s hs
      exact ⟨s, a', y, hx, hst, hq', hy⟩
    | inr hs =>
      have hp : s ∈ pool := by
        cases cover s with
        | inl h => exact absurd h hs
        | inr h => exact h
      have hl := eraseOne_length s pool hp
      refine ih (s :: seen) (eraseOne s pool) ?_ ?_ (reach_step hr hsm) ?_
      · have : (eraseOne s pool).length + 1 ≤ n + 1 := hl ▸ hlen
        exact Nat.le_of_succ_le_succ this
      · intro x
        cases cover x with
        | inl h => exact Or.inl (List.Mem.tail _ h)
        | inr h =>
          cases mem_eraseOne_or s x pool h with
          | inl e => exact Or.inl (e ▸ List.Mem.head _)
          | inr h' => exact Or.inr h'
      · intro x hx
        cases hx with
        | head => exact ⟨hr, a, m, hsm, hq, ⟨[], .nil m⟩⟩
        | tail _ hx =>
          obtain ⟨h1, a', y, h2, h3, h4⟩ := hseen x hx
          exact ⟨h1, a', y, h2, h3, reach_step h4 hsm⟩

/-- With finitely many states, a history with as many marked transitions as there are
states passes a marked transition that lies on a return path. -/
theorem marked_return_exists [DecidableEq State] {P : Process State Action}
    {Q : State → Action → State → Prop} (U : List State) (complete : ∀ x, x ∈ U)
    {s t : State} (h : Marked P Q s U.length t) :
    ∃ x a y, Reach P s x ∧ P.step x a y ∧ Q x a y ∧ Reach P y x :=
  marked_returns h [] U (Nat.le_refl _) (fun x => Or.inr (complete x)) ⟨[], .nil s⟩
    (fun _ hx => nomatch hx)

/-! ## Loss cannot be enacted indefinitely; what recurs keeps -/

/-- Removing one occurrence of `x` from a list, using only the membership proof. -/
theorem mem_split {x : State} {l : List State} (h : x ∈ l) :
    ∃ l' : List State, l'.length + 1 = l.length ∧ ∀ y, y ∈ l → ¬ y = x → y ∈ l' := by
  induction h with
  | head rest =>
    refine ⟨rest, rfl, ?_⟩
    intro y hy hne
    cases hy with
    | head => exact absurd rfl hne
    | tail _ h => exact h
  | tail b _ ih =>
    obtain ⟨l', hlen, hsub⟩ := ih
    refine ⟨b :: l', congrArg (· + 1) hlen, ?_⟩
    intro y hy hne
    cases hy with
    | head => exact List.Mem.head _
    | tail _ h => exact List.Mem.tail _ (hsub y h hne)

theorem length_pos_of_mem {x : State} {l : List State} (h : x ∈ l) : 1 ≤ l.length := by
  cases h with
  | head => exact Nat.succ_le_succ (Nat.zero_le _)
  | tail => exact Nat.succ_le_succ (Nat.zero_le _)

/-- Along a history whose marked transitions all lose, the start of each marked
transition is never reached again, so the marked transitions are fewer than the states
reachable at the outset. No decidable equality is used. -/
theorem loss_marked_bound {P : Process State Action} {Q : State → Action → State → Prop}
    {s₀ s t : State} {n : Nat} (h : Marked P Q s n t)
    (hQ : ∀ x a y, Reach P s₀ x → Q x a y → Loses P x y) (hr : Reach P s₀ s) :
    (pool : List State) → (∀ x, Reach P s x → x ∈ pool) → n + 1 ≤ pool.length := by
  induction h with
  | nil s =>
    intro pool hpool
    exact length_pos_of_mem (hpool s ⟨[], .nil s⟩)
  | pass hsm _ ih =>
    intro pool hpool
    exact ih (reach_step hr hsm) pool (fun x hx => hpool x (reach_cons hsm hx))
  | @mark s m _ a n hsm hq _ ih =>
    intro pool hpool
    obtain ⟨pool', hlen, hsub⟩ := mem_split (hpool s ⟨[], .nil s⟩)
    have hloss := hQ s a m hr hq
    have hnot : ∀ x, Reach P m x → ¬ x = s := by
      intro x hx hxs
      subst hxs
      exact loses_not_canLe hloss (return_transition_both_orders hsm hx).1
    have := ih (reach_step hr hsm) pool'
      (fun x hx => hsub x (hpool x (reach_cons hsm hx)) (hnot x hx))
    rw [← hlen]
    exact Nat.succ_le_succ this

/-- An evaluation that endorses only losing transitions is enacted fewer times than
there are states, along every history. -/
theorem loss_endorsing_enactment_bounded {P : Process State Action}
    {Q : State → Action → State → Prop} (U : List State) (complete : ∀ x, x ∈ U)
    (hQ : ∀ x a y, Q x a y → Loses P x y) (s t : State) :
    ¬ Marked P Q s U.length t := by
  intro h
  have := loss_marked_bound h (s₀ := s) (fun x a y _ hq => hQ x a y hq) ⟨[], .nil s⟩ U
    (fun x _ => complete x)
  exact Nat.not_succ_le_self _ this

/-- No history contains as many losing transitions as there are states. -/
theorem strict_loss_bounded {P : Process State Action}
    (U : List State) (complete : ∀ x, x ∈ U) (s t : State) :
    ¬ Marked P (fun x _ y => Loses P x y) s U.length t :=
  loss_endorsing_enactment_bounded U complete (fun _ _ _ h => h) s t

/-- Whatever a recurring marking endorses, not all of its reachable enactments lose.
No decidable equality is used. -/
theorem recurring_enactment_not_all_loss {P : Process State Action}
    {Q : State → Action → State → Prop} (U : List State) (complete : ∀ x, x ∈ U)
    {s : State} (h : RecursUnboundedly P Q s) :
    ¬ ∀ x a y, Reach P s x → Q x a y → Loses P x y := by
  intro hQ
  obtain ⟨t, ht⟩ := h U.length
  exact Nat.not_succ_le_self _
    (loss_marked_bound ht hQ ⟨[], .nil s⟩ U (fun x _ => complete x))

/-- If marked transitions recur without bound, some reachable marked transition keeps
every activity's eventual realizability. -/
theorem recurring_enactment_keeps [DecidableEq State] {P : Process State Action}
    {Q : State → Action → State → Prop} (U : List State) (complete : ∀ x, x ∈ U)
    {s : State} (h : RecursUnboundedly P Q s) :
    ∃ x a y, Reach P s x ∧ P.step x a y ∧ Q x a y ∧ Reach P y x ∧
      ∀ b, Can P x b ↔ Can P y b := by
  obtain ⟨t, ht⟩ := h U.length
  obtain ⟨x, a, y, hx, hst, hq, hyx⟩ := marked_return_exists U complete ht
  exact ⟨x, a, y, hx, hst, hq, hyx, return_transition_keeps hst hyx⟩

/-- An activity enacted without bound persists. -/
theorem unbounded_enactment_persists [DecidableEq State] {P : Process State Action}
    (U : List State) (complete : ∀ x, x ∈ U) {s : State} {e : Action}
    (h : RecursUnboundedly P (fun _ a _ => a = e) s) : PersistsFrom P s e := by
  obtain ⟨x, a, y, ⟨w1, h1⟩, hst, hae, ⟨w2, h2⟩, _⟩ := recurring_enactment_keeps U complete h
  refine regenerating_return_gives_persistence ⟨w1, h1⟩ ⟨a :: w2, ?_, .cons hst h2⟩ ?_
  · intro hnil
    cases hnil
  · exact can_of_enabled ⟨y, hae ▸ hst⟩

/-! ## What persistence does not exclude: loss before persistence -/

inductive SevAct where
  | other
  | cut
  | e

/-- From `false`, `other` and `e` can recur; `cut` leads to `true`, where only `e`
remains. Supplied for illustration only. -/
def severing : Process Bool SevAct where
  step s a t := match a with
    | .other => s = false ∧ t = false
    | .cut => s = false ∧ t = true
    | .e => t = s

theorem severing_stays_true : {w : List SevAct} → {t : Bool} → Trace severing true w t → t = true
  | [], _, h => (trace_nil_iff.mp h).symm
  | a :: _, _, h => by
    obtain ⟨m, hs, hr⟩ := trace_cons_iff.mp h
    cases a with
    | other => exact Bool.noConfusion hs.1
    | cut => exact Bool.noConfusion hs.1
    | e =>
      have hm : m = true := hs
      subst hm
      exact severing_stays_true hr

theorem severing_no_other_from_true : ¬ Can severing true .other := by
  rintro ⟨w, t, hw, m, hs⟩
  have ht := severing_stays_true hw
  subst ht
  exact Bool.noConfusion hs.1

/-- A transition removes `other` for good, and the evaluating activity `e` persists
afterwards. -/
theorem loss_then_persistence :
    severing.step false .cut true ∧ Loses severing false true ∧
      PersistsFrom severing true .e :=
  ⟨⟨rfl, rfl⟩,
    ⟨.other, can_of_enabled ⟨false, rfl, rfl⟩, severing_no_other_from_true⟩,
    regenerating_return_gives_persistence ⟨[], .nil true⟩
      ⟨[.e], (fun h => nomatch h), .cons (show severing.step true .e true from rfl) (.nil true)⟩
      (can_of_enabled ⟨true, rfl⟩)⟩

/-! ## The bound needs finitely many states -/

/-- On `Nat`, activity `n` is possible only at `n`, and leads to `n + 1`. -/
def ladder : Process Nat Nat where
  step s a t := a = s ∧ t = s + 1

theorem ladder_trace_le : {w : List Nat} → {s t : Nat} → Trace ladder s w t → s ≤ t
  | [], _, _, h => by
    have := trace_nil_iff.mp h
    subst this
    exact Nat.le_refl _
  | _ :: _, s, _, h => by
    obtain ⟨m, hs, hr⟩ := trace_cons_iff.mp h
    have hm : m = s + 1 := hs.2
    subst hm
    exact Nat.le_trans (Nat.le_succ s) (ladder_trace_le hr)

theorem ladder_loses (s : Nat) : Loses ladder s (s + 1) := by
  refine ⟨s, can_of_enabled ⟨s + 1, rfl, rfl⟩, ?_⟩
  rintro ⟨w, t, hw, m, hs⟩
  have hle := ladder_trace_le hw
  have hts : s = t := hs.1
  rw [← hts] at hle
  exact Nat.not_succ_le_self s hle

theorem ladder_marked : (n s : Nat) → ∃ t, Marked ladder (fun x _ y => Loses ladder x y) s n t
  | 0, s => ⟨s, .nil s⟩
  | n + 1, s => by
    obtain ⟨t, ht⟩ := ladder_marked n (s + 1)
    exact ⟨t, .mark (a := s) ⟨rfl, rfl⟩ (ladder_loses s) ht⟩

/-- With infinitely many states, losing transitions recur without bound. -/
theorem ladder_loss_recurs : RecursUnboundedly ladder (fun x _ y => Loses ladder x y) 0 :=
  fun n => ladder_marked n 0

/-! ## At immediate feasibility, loss recurs -/

theorem dip_marked : (n : Nat) →
    ∃ t, Marked dip (fun x _ y => ¬ ContinuationLe dip x y) 2 n t
  | 0 => ⟨2, .nil 2⟩
  | n + 1 => by
    obtain ⟨t, ht⟩ := dip_marked n
    refine ⟨t, .mark (m := 1) (a := DipAct.go)
      (show (1 : Nat) ≤ 2 ∧ (2 : Nat) ≤ 1 + 1 by decide)
      (fun h => law_admits_opposite_recordings.1 ⟨True.intro, h⟩)
      (.pass (m := 2) (a := DipAct.go) (show (2 : Nat) ≤ 2 ∧ (1 : Nat) ≤ 2 + 1 by decide) ht)⟩

/-- In `dip`, transitions that fail continuation inclusion recur without bound. -/
theorem dip_immediate_loss_recurs :
    RecursUnboundedly dip (fun x _ y => ¬ ContinuationLe dip x y) 2 :=
  dip_marked

end Generative.Naturalism

#print axioms Generative.Naturalism.reach_step
#print axioms Generative.Naturalism.reach_cons
#print axioms Generative.Naturalism.loses_not_canLe
#print axioms Generative.Naturalism.no_transition_gains
#print axioms Generative.Naturalism.loss_order_endorses_every_transition
#print axioms Generative.Naturalism.loss_order_along_every_history
#print axioms Generative.Naturalism.return_transition_keeps
#print axioms Generative.Naturalism.return_transition_both_orders
#print axioms Generative.Naturalism.marked_returns
#print axioms Generative.Naturalism.marked_return_exists
#print axioms Generative.Naturalism.mem_split
#print axioms Generative.Naturalism.length_pos_of_mem
#print axioms Generative.Naturalism.loss_marked_bound
#print axioms Generative.Naturalism.loss_endorsing_enactment_bounded
#print axioms Generative.Naturalism.strict_loss_bounded
#print axioms Generative.Naturalism.recurring_enactment_not_all_loss
#print axioms Generative.Naturalism.recurring_enactment_keeps
#print axioms Generative.Naturalism.unbounded_enactment_persists
#print axioms Generative.Naturalism.severing_stays_true
#print axioms Generative.Naturalism.severing_no_other_from_true
#print axioms Generative.Naturalism.loss_then_persistence
#print axioms Generative.Naturalism.ladder_trace_le
#print axioms Generative.Naturalism.ladder_loses
#print axioms Generative.Naturalism.ladder_marked
#print axioms Generative.Naturalism.ladder_loss_recurs
#print axioms Generative.Naturalism.dip_marked
#print axioms Generative.Naturalism.dip_immediate_loss_recurs
