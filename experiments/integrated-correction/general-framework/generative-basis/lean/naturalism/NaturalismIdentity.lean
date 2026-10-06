import WholeQualityNaturalism

/-!
# Which natural property? Orientation, the reflexive premise and rival candidates

`WholeQualityNaturalism` gives the history quality `Along R` the credentials the
four naturalist arguments ask for. This module shows three things.

* **The credentials do not select the orientation** (`naturalist_criteria_do_not_fix_orientation`).
  The conditions-of-continuation order and its converse are both preorders, both
  invariant under exact re-representation, both supervenient on the visited
  states and both compositional. On one actual transition of `dip` they give
  opposite verdicts. This is the formal content of the open-question and
  is/ought objection against reading "good" off these facts alone. It sharpens
  `EthicalOrientation.coherence_and_annotation_invariance_do_not_select_growth`.
* **A further premise does select it** (`generation_order_greatest`,
  `unprivileged_scope_is_whole_scope`, `guided_history_preserves`). Call an orientation
  non-undermining for a scope of activities when following it never removes the
  realizability of an activity in that scope. Evaluation, updating and correction are
  themselves activities inside the unfolding. If no activity, including any evaluator's
  own, is privileged or fixed in advance, the scope is all activities. Then the
  admissible orientations are exactly the sub-relations of the conditions-of-continuation
  order. The premise is normative; it is stated, not derived.
* **Rival candidates under the same premise.** A scope fixed in advance, whether
  the activities of a given life form (Foot) or of one center (Railton's
  individual good), admits orientations that remove an activity outside it
  (`fixed_scope_permits_loss`). Every complete ranking, in particular every scalar
  welfare ranking, removes some realizable activity in `incomparable`
  (`total_orders_undermine`, `scalar_ranking_undermines`). The conditions-of-continuation
  order keeps the premise by leaving that pair unranked (`generation_leaves_pair_unranked`).
  This is a trade-off between completeness and non-undermining, not a refutation of
  those theories.
* **A preserved counterexample to the premise as stated** (`restraint_registers_as_damage`).
  With every activity counted alike, preventing an activity that would remove another
  center's activity counts as a loss of conditions, as the harm itself does, while
  leaving the harm possible counts as no loss. The premise therefore cannot yet be the
  ethical identity; the scope of protected activities needs a principled refinement.

Processes, scopes and rankings are supplied inputs. No theorem says which
history occurs, that the premise is true, or how to choose when every option
removes something.
-/

namespace Generative.Naturalism

open Generative.EthicalOrientation

universe u v

variable {State : Type u} {Action : Type v}

/-! ## 1. The naturalist credentials are orientation-neutral -/

/-- Exact re-representation also preserves and reflects the converse comparison. -/
theorem converse_projection_iff {Other : Type u}
    {P : Process State Action} {Q : Process Other Action} {q : State → Other}
    (hexact : ∀ s word, Feasible P s word ↔ Feasible Q (q s) word) (s t : State) :
    converse (ContinuationLe P) s t ↔ converse (ContinuationLe Q) (q s) (q t) :=
  continuation_projection_iff hexact t s

/-- Generation (`dip` from 1 back to 2) is upward for one order and downward for the other. -/
theorem dip_two_dominates_one : ContinuationLe dip 1 2 := by
  intro word hw
  cases word with
  | nil => exact ⟨2, .nil 2⟩
  | cons a rest =>
    obtain ⟨t, h⟩ := hw
    cases h with
    | cons hs hr =>
      cases a with
      | use => exact absurd (hs.1 : (1 : Nat) = 2) (by decide)
      | go =>
        -- From 2, `go` may reach every level that `go` reaches from 1 except 0;
        -- reaching 1 instead of 0 keeps every continuation (0 and 1 are equivalent).
        rename_i m
        have hm : m ≤ 2 := hs.1
        have same : ∀ word, Feasible dip m word → Feasible dip (if m = 0 then 1 else m) word := by
          intro w' hw'
          by_cases h0 : m = 0
          · subst h0
            cases w' with
            | nil => exact ⟨1, .nil 1⟩
            | cons b rest' =>
              obtain ⟨u, hu⟩ := hw'
              cases hu with
              | cons hs' hr' =>
                cases b with
                | use => exact absurd (hs'.1 : (0 : Nat) = 2) (by decide)
                | go =>
                  rename_i n
                  exact ⟨u, .cons (show n ≤ 2 ∧ (1 : Nat) ≤ n + 1 from
                    ⟨hs'.1, Nat.succ_le_succ (Nat.zero_le n)⟩) hr'⟩
          · rw [if_neg h0]
            exact hw'
        obtain ⟨u, hu⟩ := same rest ⟨t, hr⟩
        refine ⟨u, .cons ?_ hu⟩
        show (if m = 0 then 1 else m) ≤ 2 ∧ (2 : Nat) ≤ (if m = 0 then 1 else m) + 1
        by_cases h0 : m = 0
        · rw [if_pos h0]
          decide
        · rw [if_neg h0]
          exact ⟨hm, Nat.succ_le_succ (Nat.pos_of_ne_zero h0)⟩

/-- Both orientations meet every naturalist criterion proved so far; they rank the
actual damaging transition of `dipped` (from 2 to 1) oppositely. -/
theorem naturalist_criteria_do_not_fix_orientation :
    (PreorderLaws (ContinuationLe dip) ∧ PreorderLaws (converse (ContinuationLe dip))) ∧
    (Covaries (fun h : History dip => Along (ContinuationLe dip) h.2.2) History.states ∧
      Covaries (fun h : History dip => Along (converse (ContinuationLe dip)) h.2.2)
        History.states) ∧
    ((2, 1) ∈ dipped.steps ∧
      ¬ ContinuationLe dip 2 1 ∧ converse (ContinuationLe dip) 2 1) :=
  ⟨⟨continuation_preorder dip, converse_preorder (continuation_preorder dip)⟩,
    ⟨along_supervenes_on_states dip _, along_supervenes_on_states dip _⟩,
    ⟨List.Mem.head _,
      witness_refutes_preservation ⟨dip_use_at_two, dip_no_use_at_one⟩,
      dip_two_dominates_one⟩⟩

/-! ## 2. The reflexive premise and the greatest admissible orientation -/

/-- Following `R` never removes the realizability of an activity in scope `W`. -/
def NonUndermining (P : Process State Action) (W : List Action → Prop)
    (R : State → State → Prop) : Prop :=
  ∀ s t, R s t → ∀ word, W word → Feasible P s word → Feasible P t word

/-- The whole scope: no activity is excluded in advance. -/
def wholeScope : List Action → Prop := fun _ => True

theorem nonUndermining_whole_iff (P : Process State Action) (R : State → State → Prop) :
    NonUndermining P wholeScope R ↔ ∀ s t, R s t → ContinuationLe P s t :=
  Iff.intro (fun h s t hst word hw => h s t hst word True.intro hw)
    (fun h s t hst word _ hw => h s t hst word hw)

/-- The conditions-of-continuation order is admissible, and contains every admissible orientation. -/
theorem generation_order_greatest (P : Process State Action) :
    NonUndermining P wholeScope (ContinuationLe P) ∧
      ∀ R, NonUndermining P wholeScope R → ∀ s t, R s t → ContinuationLe P s t :=
  ⟨(nonUndermining_whole_iff P _).mpr (fun _ _ h => h),
    fun R h => (nonUndermining_whole_iff P R).mp h⟩

/-- Non-undermining for each single activity, none privileged, is non-undermining for all. -/
theorem unprivileged_scope_is_whole_scope (P : Process State Action) (R : State → State → Prop) :
    (∀ e : List Action, NonUndermining P (fun word => word = e) R) ↔
      NonUndermining P wholeScope R := by
  constructor
  · intro h s t hst word _ hw
    exact h word s t hst word rfl hw
  · intro h e s t hst word _ hw
    exact h s t hst word True.intro hw

/-- A history guided by an admissible orientation keeps every initially realizable
activity, the evaluator's own included, realizable at every visited state. -/
theorem guided_history_preserves {P : Process State Action} {R : State → State → Prop}
    (hR : NonUndermining P wholeScope R) {s t : State} (r : Run P s t)
    (hguided : Along R r) (word : List Action) (hw : Feasible P s word) :
    AvailableThroughout word r :=
  preserved_throughout word r
    (along_mono ((nonUndermining_whole_iff P R).mp hR) r hguided) hw

/-- The converse orientation is not admissible in `dip`. -/
theorem converse_undermines_in_dip :
    ¬ NonUndermining dip wholeScope (converse (ContinuationLe dip)) := by
  intro h
  exact dip_no_use_at_one
    (h 2 1 dip_two_dominates_one [DipAct.use] True.intro dip_use_at_two)

/-! ## 3. A scope fixed in advance: life form or single center -/

/-- `false` is a listed activity, `true` a further one available only in state `true`.
Doing the listed activity may lose the further one. -/
def novel : Process Bool Bool where
  step s a t := (a = false ∧ t = false) ∨ (a = true ∧ s = true ∧ t = true)

/-- Words made only of the listed activity. -/
def listedScope (word : List Bool) : Prop := ∀ a ∈ word, a = false

theorem novel_listed_feasible : (word : List Bool) → listedScope word →
    ∀ s, Feasible novel s word
  | [], _, s => ⟨s, .nil s⟩
  | a :: rest, h, _ => by
    obtain ⟨t, ht⟩ := novel_listed_feasible rest (fun b hb => h b (List.Mem.tail _ hb)) false
    have ha : a = false := h a (List.Mem.head _)
    subst ha
    exact ⟨t, .cons (Or.inl ⟨rfl, rfl⟩) ht⟩

theorem novel_further_at_true : Feasible novel true [true] :=
  ⟨true, .cons (Or.inr ⟨rfl, rfl, rfl⟩) (.nil true)⟩

theorem novel_no_further_at_false : ¬ Feasible novel false [true] := by
  rintro ⟨t, h⟩
  cases h with
  | cons hs _ =>
    cases hs with
    | inl h => exact absurd h.1 (by decide)
    | inr h => exact absurd h.2.1 (by decide)

/-- Admissible for the fixed scope, yet it removes an activity outside it. -/
theorem fixed_scope_permits_loss :
    NonUndermining novel listedScope (fun s t => s = true ∧ t = false) ∧
      ¬ NonUndermining novel wholeScope (fun s t => s = true ∧ t = false) := by
  constructor
  · intro _ t _ word hw _
    exact novel_listed_feasible word hw t
  · intro h
    exact novel_no_further_at_false
      (h true false ⟨rfl, rfl⟩ [true] True.intro novel_further_at_true)

/-! ## 4. Complete rankings and scalar welfare -/

/-- Each state keeps an activity the other lacks. -/
def incomparable : Process Bool Bool where
  step s a t := a = s ∧ t = s

theorem incomparable_own (s : Bool) : Feasible incomparable s [s] :=
  ⟨s, .cons ⟨rfl, rfl⟩ (.nil s)⟩

theorem incomparable_not_other (s : Bool) : ¬ Feasible incomparable s [!s] := by
  rintro ⟨t, h⟩
  cases h with
  | cons hs _ => cases s <;> exact absurd hs.1 (by decide)

/-- The conditions-of-continuation order leaves the two states unranked. -/
theorem generation_leaves_pair_unranked :
    ¬ ContinuationLe incomparable true false ∧ ¬ ContinuationLe incomparable false true :=
  ⟨witness_refutes_preservation ⟨incomparable_own true, incomparable_not_other false⟩,
    witness_refutes_preservation ⟨incomparable_own false, incomparable_not_other true⟩⟩

/-- Every complete ranking removes some realizable activity. -/
theorem total_orders_undermine (R : Bool → Bool → Prop) (htotal : ∀ x y, R x y ∨ R y x) :
    ¬ NonUndermining incomparable wholeScope R := by
  intro h
  cases htotal true false with
  | inl hr =>
    exact incomparable_not_other false
      (h true false hr [true] True.intro (incomparable_own true))
  | inr hr =>
    exact incomparable_not_other true
      (h false true hr [false] True.intro (incomparable_own false))

/-- In particular, ranking states by any scalar welfare does. -/
theorem scalar_ranking_undermines (welfare : Bool → Nat) :
    ¬ NonUndermining incomparable wholeScope (fun x y => welfare x ≤ welfare y) :=
  total_orders_undermine _ (fun x y => Nat.le_total (welfare x) (welfare y))

/-! ## 5. A preserved counterexample: restraint registers as damage -/

inductive Situation where
  | open
  | restrained
  | harmed
  deriving DecidableEq

inductive Deed where
  | live
  | harm
  | restrain
  deriving DecidableEq

/-- `live` is the other center's activity; `harm` removes it; `restrain` removes `harm`. -/
def restraint : Process Situation Deed where
  step s a t := match a with
    | .live => (s = .open ∨ s = .restrained) ∧ t = s
    | .harm => s = .open ∧ t = .harmed
    | .restrain => s = .open ∧ t = .restrained

theorem restraint_live_words : (word : List Deed) → (∀ a ∈ word, a = .live) →
    Feasible restraint .restrained word → Feasible restraint .open word
  | [], _, _ => ⟨.open, .nil _⟩
  | a :: rest, h, _ => by
    have ha : a = .live := h a (List.Mem.head _)
    subst ha
    have hall : ∀ b ∈ rest, b = .live := fun b hb => h b (List.Mem.tail _ hb)
    have tail : ∀ (r : List Deed), (∀ b ∈ r, b = .live) → Feasible restraint .open r := by
      intro r
      induction r with
      | nil => intro _; exact ⟨.open, .nil _⟩
      | cons b r ih =>
        intro hb
        have hb0 : b = .live := hb b (List.Mem.head _)
        subst hb0
        obtain ⟨u, hu⟩ := ih (fun c hc => hb c (List.Mem.tail _ hc))
        exact ⟨u, .cons (show (Situation.open = .open ∨ Situation.open = .restrained) ∧
          Situation.open = .open from ⟨Or.inl rfl, rfl⟩) hu⟩
    obtain ⟨u, hu⟩ := tail rest hall
    exact ⟨u, .cons (show (Situation.open = .open ∨ Situation.open = .restrained) ∧
      Situation.open = .open from ⟨Or.inl rfl, rfl⟩) hu⟩

theorem restraint_only_live_from_restrained : (word : List Deed) →
    Feasible restraint .restrained word → ∀ a ∈ word, a = .live
  | [], _ => fun _ h => by cases h
  | a :: rest, ⟨t, h⟩ => by
    cases h with
    | cons hs hr =>
      rename_i m
      cases a with
      | live =>
        have hm : m = .restrained := hs.2
        subst hm
        intro b hb
        cases hb with
        | head => rfl
        | tail _ hb => exact restraint_only_live_from_restrained rest ⟨t, hr⟩ b hb
      | harm => exact absurd hs.1 (by decide)
      | restrain => exact absurd hs.1 (by decide)

/-- Read through feasible activities with none excluded, preventing harm counts as a
loss of conditions just as harm does, while leaving harm possible counts as no loss. -/
theorem restraint_registers_as_damage :
    ¬ ContinuationLe restraint .open .restrained ∧
      ContinuationLe restraint .restrained .open ∧
      ¬ ContinuationLe restraint .open .harmed := by
  have harmHere : Feasible restraint .open [Deed.harm] :=
    ⟨.harmed, .cons (show Situation.open = .open ∧ Situation.harmed = .harmed from ⟨rfl, rfl⟩)
      (.nil _)⟩
  have liveHere : Feasible restraint .open [Deed.live] :=
    ⟨.open, .cons (show (Situation.open = .open ∨ Situation.open = .restrained) ∧
      Situation.open = .open from ⟨Or.inl rfl, rfl⟩) (.nil _)⟩
  refine ⟨?_, ?_, ?_⟩
  · apply witness_refutes_preservation (word := [Deed.harm])
    refine ⟨harmHere, ?_⟩
    intro h
    have := restraint_only_live_from_restrained [Deed.harm] h Deed.harm (List.Mem.head _)
    exact absurd this (by decide)
  · intro word hw
    exact restraint_live_words word (restraint_only_live_from_restrained word hw) hw
  · apply witness_refutes_preservation (word := [Deed.live])
    refine ⟨liveHere, ?_⟩
    rintro ⟨t, h⟩
    cases h with
    | cons hs _ =>
      cases hs.1 with
      | inl h => exact absurd h (by decide)
      | inr h => exact absurd h (by decide)

end Generative.Naturalism

#print axioms Generative.Naturalism.converse_projection_iff
#print axioms Generative.Naturalism.dip_two_dominates_one
#print axioms Generative.Naturalism.naturalist_criteria_do_not_fix_orientation
#print axioms Generative.Naturalism.nonUndermining_whole_iff
#print axioms Generative.Naturalism.generation_order_greatest
#print axioms Generative.Naturalism.unprivileged_scope_is_whole_scope
#print axioms Generative.Naturalism.guided_history_preserves
#print axioms Generative.Naturalism.converse_undermines_in_dip
#print axioms Generative.Naturalism.novel_listed_feasible
#print axioms Generative.Naturalism.novel_further_at_true
#print axioms Generative.Naturalism.novel_no_further_at_false
#print axioms Generative.Naturalism.fixed_scope_permits_loss
#print axioms Generative.Naturalism.incomparable_own
#print axioms Generative.Naturalism.incomparable_not_other
#print axioms Generative.Naturalism.generation_leaves_pair_unranked
#print axioms Generative.Naturalism.total_orders_undermine
#print axioms Generative.Naturalism.scalar_ranking_undermines
#print axioms Generative.Naturalism.restraint_live_words
#print axioms Generative.Naturalism.restraint_only_live_from_restrained
#print axioms Generative.Naturalism.restraint_registers_as_damage
