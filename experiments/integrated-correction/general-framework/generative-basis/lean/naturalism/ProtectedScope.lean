import NaturalismReview

/-!
# A protected scope derived from the process: restraint, commitment and recovery

`NaturalismIdentity` and `NaturalismReview` showed that counting every activity
alike makes restraint, every exclusive commitment and every recovered dip register
as damage. This module derives the protected scope from relations already in the
process, with no ethical label supplied.

* **Eventual realizability.** `Can P s b`: from `s` some actual path reaches a state
  where `b` is enabled. It never increases along a history (`can_of_reach`), so a
  loss of it is irreversible (`eventual_loss_is_irreversible`).
* **Removal between activities.** `Removes P a b`: some actual exercise of `a` takes
  `b` from eventually realizable to never realizable.
* **Protected activities.** Relative to a scope `O` of ongoing activities, `b` is
  protected when it is in `O` and its exercise removes no other activity in `O`.
  `O` can be read off a history as the activities it actually exercises (`exercised`).
* **Damage and generation.** A transition damages when a protected activity loses
  eventual realizability, and generates when a protected activity becomes enabled
  where it was not.

Results on the earlier counterexamples, each under its own scope:

* with every activity in scope, restraint does not damage and harm does, in this
  particular process where the victim's activity removes nothing
  (`restraint_not_damage_harm_is`);
* with the scope the actual history exercises, committing does not damage the untaken
  course; with every activity in scope, it does (`commitment_damage_depends_on_scope`);
* in `dip` every state can climb back, so no step is damage, whether or not recovery
  actually happens; the return step counts as generation
  (`recoverable_dip_not_damage`, `dip_recovery_generates`).

`ProtectedScopeLimits` shows that no single one of these scopes handles both restraint
and commitment, that the restraint verdict depends on the modelling of the victim, and
that an unrecovered fall is not damage either. Damage is measured at the level of eventual
realizability and generation at the level of immediate availability, and neither requires
an actual step; the two are therefore not comparable as a ledger.

Preserved limit: two rival activities that remove each other are both unprotected, so a
step that destroys both registers no damage (`symmetric_rivals_leave_ruin_unregistered`).
`eventual_realizability_never_increases` is composition of reachability. It shows that
eventual realizability measured within one representation cannot register novelty; it
does not show that generation requires a change of process, since a change of process
can be encoded as states of a larger one.

Activities are single actions of a supplied vocabulary; `Can` is existence of a path,
not probability or experience. Nothing here establishes that this scope is the
ethical one.
-/

namespace Generative.Naturalism

universe u v

variable {State : Type u} {Action : Type v}

/-! ## 1. Eventual realizability -/

/-- Some actual path from `s` reaches a state where `b` is enabled. -/
def Can (P : Process State Action) (s : State) (b : Action) : Prop :=
  ∃ word t, Trace P s word t ∧ Enabled P t b

theorem can_of_enabled {P : Process State Action} {s : State} {b : Action}
    (h : Enabled P s b) : Can P s b :=
  ⟨[], s, .nil s, h⟩

/-- What is eventually realizable later was eventually realizable before. -/
theorem can_of_reach {P : Process State Action} {s t : State} {word : List Action} {b : Action}
    (hr : Trace P s word t) (h : Can P t b) : Can P s b := by
  obtain ⟨w', u, hu, hb⟩ := h
  exact ⟨word ++ w', u, trace_append_iff.mpr ⟨t, hr, hu⟩, hb⟩

theorem eventual_realizability_never_increases {P : Process State Action}
    {s t : State} {word : List Action} (hr : Trace P s word t) (b : Action) :
    Can P t b → Can P s b :=
  can_of_reach hr

/-- Once lost, eventual realizability does not return anywhere later. -/
theorem eventual_loss_is_irreversible {P : Process State Action}
    {t u : State} {word : List Action} {b : Action}
    (hlost : ¬ Can P t b) (hr : Trace P t word u) : ¬ Can P u b :=
  fun h => hlost (can_of_reach hr h)

/-! ## 2. Removal, protection, damage, generation -/

/-- Some actual exercise of `a` makes `b` never realizable where it had been. -/
def Removes (P : Process State Action) (a b : Action) : Prop :=
  ∃ s t, P.step s a t ∧ Can P s b ∧ ¬ Can P t b

/-- Ongoing and removing no other ongoing activity. -/
def Protected (P : Process State Action) (O : Action → Prop) (b : Action) : Prop :=
  O b ∧ ∀ c, O c → c ≠ b → ¬ Removes P b c

def Damages (P : Process State Action) (O : Action → Prop) (s t : State) : Prop :=
  ∃ b, Protected P O b ∧ Can P s b ∧ ¬ Can P t b

def Generates (P : Process State Action) (O : Action → Prop) (s t : State) : Prop :=
  ∃ b, Protected P O b ∧ ¬ Enabled P s b ∧ Enabled P t b

/-- The scope a history supplies: the activities it actually exercises. -/
def exercised {P : Process State Action} {s t : State} (r : Run P s t) (a : Action) : Prop :=
  a ∈ r.word

def allActivities : Action → Prop := fun _ => True

/-- A non-damaging step keeps every protected activity eventually realizable. -/
theorem not_damages_iff (P : Process State Action) (O : Action → Prop) (s t : State) :
    ¬ Damages P O s t ↔ ∀ b, Protected P O b → Can P s b → ¬¬ Can P t b :=
  Iff.intro (fun h b hp hs ht => h ⟨b, hp, hs, ht⟩)
    (fun h ⟨b, hp, hs, ht⟩ => h b hp hs ht)

/-! ## 3. Restraint is not harm -/

theorem restraint_live_never_removes (b : Deed) : ¬ Removes restraint .live b := by
  rintro ⟨s, t, hst, hs, ht⟩
  have e : t = s := hst.2
  subst e
  exact ht hs

theorem harmed_stuck : (word : List Deed) → (u : Situation) →
    Trace restraint .harmed word u → u = .harmed
  | [], _, h => (trace_nil_iff.mp h).symm
  | a :: _, _, h => by
    obtain ⟨m, hs, _⟩ := trace_cons_iff.mp h
    cases a with
    | live => exact absurd hs.1 (by decide)
    | harm => exact absurd hs.1 (by decide)
    | restrain => exact absurd hs.1 (by decide)

theorem harmed_cannot (b : Deed) : ¬ Can restraint .harmed b := by
  rintro ⟨word, u, hu, ⟨v, hv⟩⟩
  have e := harmed_stuck word u hu
  subst e
  cases b with
  | live => exact absurd hv.1 (by decide)
  | harm => exact absurd hv.1 (by decide)
  | restrain => exact absurd hv.1 (by decide)

theorem restrained_stuck : (word : List Deed) → (u : Situation) →
    Trace restraint .restrained word u → u = .restrained
  | [], _, h => (trace_nil_iff.mp h).symm
  | a :: rest, u, h => by
    obtain ⟨m, hs, hr⟩ := trace_cons_iff.mp h
    cases a with
    | live =>
      have e : m = .restrained := hs.2
      subst e
      exact restrained_stuck rest u hr
    | harm => exact absurd hs.1 (by decide)
    | restrain => exact absurd hs.1 (by decide)

theorem restrained_cannot_harm : ¬ Can restraint .restrained .harm := by
  rintro ⟨word, u, hu, ⟨v, hv⟩⟩
  have e := restrained_stuck word u hu
  subst e
  exact absurd hv.1 (by decide)

theorem restrained_can_live : Can restraint .restrained .live :=
  can_of_enabled ⟨.restrained, show (Situation.restrained = .open ∨
    Situation.restrained = .restrained) ∧ Situation.restrained = .restrained from
    ⟨Or.inr rfl, rfl⟩⟩

theorem open_can (b : Deed) : Can restraint .open b := by
  apply can_of_enabled
  cases b with
  | live => exact ⟨.open, show (Situation.open = .open ∨ Situation.open = .restrained) ∧
      Situation.open = .open from ⟨Or.inl rfl, rfl⟩⟩
  | harm => exact ⟨.harmed, show Situation.open = .open ∧ Situation.harmed = .harmed from
      ⟨rfl, rfl⟩⟩
  | restrain => exact ⟨.restrained, show Situation.open = .open ∧
      Situation.restrained = .restrained from ⟨rfl, rfl⟩⟩

theorem harm_removes_live : Removes restraint .harm .live :=
  ⟨.open, .harmed, ⟨rfl, rfl⟩, open_can .live, harmed_cannot .live⟩

theorem restrain_removes_harm : Removes restraint .restrain .harm :=
  ⟨.open, .restrained, ⟨rfl, rfl⟩, open_can .harm, restrained_cannot_harm⟩

/-- With every activity in scope, only `live` is protected. -/
theorem restraint_protected_iff (b : Deed) :
    Protected restraint allActivities b ↔ b = .live := by
  constructor
  · rintro ⟨_, h⟩
    cases b with
    | live => rfl
    | harm => exact absurd harm_removes_live (h .live True.intro (by decide))
    | restrain => exact absurd restrain_removes_harm (h .harm True.intro (by decide))
  · intro e
    subst e
    exact ⟨True.intro, fun c _ _ => restraint_live_never_removes c⟩

/-- Restraint does not damage; harm does. No ethical label is supplied. -/
theorem restraint_not_damage_harm_is :
    ¬ Damages restraint allActivities .open .restrained ∧
      Damages restraint allActivities .open .harmed := by
  constructor
  · rintro ⟨b, hp, _, ht⟩
    have e := (restraint_protected_iff b).mp hp
    subst e
    exact ht restrained_can_live
  · exact ⟨.live, (restraint_protected_iff .live).mpr rfl, open_can .live, harmed_cannot .live⟩

/-! ## 4. Commitment: the untaken course and the scope a history supplies -/

theorem committed_stuck (b : Bool) : (word : List (Option Bool)) → (u : Option Bool) →
    Trace committing (some b) word u → u = some b
  | [], _, h => (trace_nil_iff.mp h).symm
  | a :: rest, u, h => by
    obtain ⟨m, hs, hr⟩ := trace_cons_iff.mp h
    cases a with
    | none => exact absurd hs (fun x => x)
    | some c =>
      have e : m = some b := hs.2
      subst e
      exact committed_stuck b rest u hr

theorem committed_cannot_other (b : Bool) : ¬ Can committing (some b) (some (!b)) := by
  rintro ⟨word, u, hu, ⟨v, hv⟩⟩
  have e := committed_stuck b word u hu
  subst e
  have : (!b) = b := hv.1
  cases b <;> exact absurd this (by decide)

theorem committed_can_own (b : Bool) : Can committing (some b) (some b) :=
  can_of_enabled ⟨some b, show b = b ∧ some b = some b from ⟨rfl, rfl⟩⟩

theorem open_can_each (b : Bool) : Can committing none (some b) :=
  ⟨[none], some b, .cons (show some b = some true ∨ some b = some false by
      cases b
      · exact Or.inr rfl
      · exact Or.inl rfl) (.nil _),
    ⟨some b, show b = b ∧ some b = some b from ⟨rfl, rfl⟩⟩⟩

theorem course_never_removes (b : Bool) (c : Option Bool) :
    ¬ Removes committing (some b) c := by
  rintro ⟨s, t, hst, hs, ht⟩
  cases s with
  | none => exact hst
  | some d =>
    have e : t = some d := hst.2
    subst e
    exact ht hs

/-- The history that commits to `true` and then carries it on. -/
def commitThenCarry : Run committing none (some true) :=
  .cons none (show some true = some true ∨ some true = some false from Or.inl rfl)
    (.cons (some true) (show true = true ∧ some true = some true from ⟨rfl, rfl⟩) (.nil _))

/-- With every activity in scope, committing damages the untaken course. With the
scope the actual history exercises, it does not. -/
theorem commitment_damage_depends_on_scope :
    Damages committing allActivities none (some true) ∧
      ¬ Damages committing (exercised commitThenCarry) none (some true) := by
  constructor
  · exact ⟨some false, ⟨True.intro, fun c _ _ => course_never_removes false c⟩,
      open_can_each false, committed_cannot_other true⟩
  · rintro ⟨b, ⟨hO, hp⟩, _, ht⟩
    have hmem : b ∈ [none, some true] := hO
    cases hmem with
    | head =>
      -- Committing is in scope but removes the carried course, so it is not protected.
      exact hp (some true) (show some true ∈ [none, some true] from
          List.Mem.tail _ (List.Mem.head _)) (by decide)
        ⟨none, some false, (show some false = some true ∨ some false = some false
          from Or.inr rfl), open_can_each true, committed_cannot_other false⟩
    | tail _ h =>
      cases h with
      | head => exact ht (committed_can_own true)
      | tail _ h => cases h

/-! ## 5. Recovery -/

theorem dip_can_from_one (b : DipAct) : Can dip 1 b := by
  cases b with
  | go => exact can_of_enabled ⟨2, show (2 : Nat) ≤ 2 ∧ (1 : Nat) ≤ 2 + 1 by decide⟩
  | use =>
    exact ⟨[DipAct.go], 2, .cons (show (2 : Nat) ≤ 2 ∧ (1 : Nat) ≤ 2 + 1 by decide) (.nil 2),
      ⟨2, show (2 : Nat) = 2 ∧ (2 : Nat) = 2 from ⟨rfl, rfl⟩⟩⟩

/-- The dip loses immediate availability of `use` but nothing eventually realizable.
This holds because every `dip` state can climb back, not because recovery happens. -/
theorem recoverable_dip_not_damage (O : DipAct → Prop) : ¬ Damages dip O 2 1 :=
  fun ⟨b, _, _, ht⟩ => ht (dip_can_from_one b)

theorem dip_never_removes (a b : DipAct) : ¬ Removes dip a b := by
  rintro ⟨s, t, hst, _, ht⟩
  apply ht
  cases a with
  | use =>
    have e : t = 2 := hst.2
    subst e
    cases b with
    | go => exact can_of_enabled ⟨2, show (2 : Nat) ≤ 2 ∧ (2 : Nat) ≤ 2 + 1 by decide⟩
    | use => exact can_of_enabled ⟨2, show (2 : Nat) = 2 ∧ (2 : Nat) = 2 from ⟨rfl, rfl⟩⟩
  | go =>
    have ht2 : t ≤ 2 := hst.1
    cases b with
    | go => exact can_of_enabled ⟨2, show (2 : Nat) ≤ 2 ∧ t ≤ 2 + 1 from
        ⟨Nat.le_refl 2, Nat.le_succ_of_le ht2⟩⟩
    | use =>
      exact ⟨[DipAct.go], 2, .cons (show (2 : Nat) ≤ 2 ∧ t ≤ 2 + 1 from
          ⟨Nat.le_refl 2, Nat.le_succ_of_le ht2⟩) (.nil 2),
        ⟨2, show (2 : Nat) = 2 ∧ (2 : Nat) = 2 from ⟨rfl, rfl⟩⟩⟩

/-- The return from 1 to 2 regenerates immediate availability of a protected activity. -/
theorem dip_recovery_generates : Generates dip allActivities 1 2 :=
  ⟨.use, ⟨True.intro, fun c _ _ => dip_never_removes .use c⟩, dip_no_use_at_one |> fun h =>
      fun ⟨t, ht⟩ => h ⟨t, .cons ht (.nil t)⟩,
    ⟨2, show (2 : Nat) = 2 ∧ (2 : Nat) = 2 from ⟨rfl, rfl⟩⟩⟩

/-! ## 6. A preserved limit: symmetric rivals -/

inductive Field where
  | shared
  | onlyA
  | onlyB
  | ruined
  deriving DecidableEq

inductive Move where
  | a
  | b
  | ruin
  deriving DecidableEq

/-- Each of `a`, `b` excludes the other; `ruin` ends both. -/
def rivals : Process Field Move where
  step s m t := match m with
    | .a => (s = .shared ∨ s = .onlyA) ∧ t = .onlyA
    | .b => (s = .shared ∨ s = .onlyB) ∧ t = .onlyB
    | .ruin => s = .shared ∧ t = .ruined

theorem rivals_stuck (f : Field) (hf : f ≠ .shared) (m : Move) :
    (word : List Move) → (u : Field) → Trace rivals f word u →
    (Enabled rivals u m → Enabled rivals f m)
  | [], _, h, he => by
    have e := trace_nil_iff.mp h
    subst e
    exact he
  | x :: rest, u, h, he => by
    obtain ⟨n, hs, hr⟩ := trace_cons_iff.mp h
    have stay : n = f := by
      cases x with
      | a =>
        cases hs.1 with
        | inl e => exact absurd e hf
        | inr e => rw [hs.2, e]
      | b =>
        cases hs.1 with
        | inl e => exact absurd e hf
        | inr e => rw [hs.2, e]
      | ruin => exact absurd hs.1 hf
    subst stay
    exact rivals_stuck n hf m rest u hr he

theorem rivals_can_iff_enabled (f : Field) (hf : f ≠ .shared) (m : Move) :
    Can rivals f m → Enabled rivals f m :=
  fun ⟨word, u, hu, he⟩ => rivals_stuck f hf m word u hu he

theorem rivals_shared_can (m : Move) : Can rivals .shared m := by
  apply can_of_enabled
  cases m with
  | a => exact ⟨.onlyA, show (Field.shared = .shared ∨ Field.shared = .onlyA) ∧
      Field.onlyA = .onlyA from ⟨Or.inl rfl, rfl⟩⟩
  | b => exact ⟨.onlyB, show (Field.shared = .shared ∨ Field.shared = .onlyB) ∧
      Field.onlyB = .onlyB from ⟨Or.inl rfl, rfl⟩⟩
  | ruin => exact ⟨.ruined, show Field.shared = .shared ∧ Field.ruined = .ruined from
      ⟨rfl, rfl⟩⟩

theorem rivals_not_enabled {f : Field} {m : Move}
    (h : ∀ t, ¬ rivals.step f m t) : ¬ Enabled rivals f m :=
  fun ⟨t, ht⟩ => h t ht

theorem a_removes_b : Removes rivals .a .b :=
  ⟨.shared, .onlyA, ⟨Or.inl rfl, rfl⟩, rivals_shared_can .b, fun h => by
    obtain ⟨t, ht⟩ := rivals_can_iff_enabled .onlyA (by decide) .b h
    cases ht.1 with
    | inl e => exact absurd e (by decide)
    | inr e => exact absurd e (by decide)⟩

theorem b_removes_a : Removes rivals .b .a :=
  ⟨.shared, .onlyB, ⟨Or.inl rfl, rfl⟩, rivals_shared_can .a, fun h => by
    obtain ⟨t, ht⟩ := rivals_can_iff_enabled .onlyB (by decide) .a h
    cases ht.1 with
    | inl e => exact absurd e (by decide)
    | inr e => exact absurd e (by decide)⟩

theorem ruin_removes_a : Removes rivals .ruin .a :=
  ⟨.shared, .ruined, ⟨rfl, rfl⟩, rivals_shared_can .a, fun h => by
    obtain ⟨t, ht⟩ := rivals_can_iff_enabled .ruined (by decide) .a h
    cases ht.1 with
    | inl e => exact absurd e (by decide)
    | inr e => exact absurd e (by decide)⟩

/-- No activity is protected, so ruining both registers no damage. -/
theorem symmetric_rivals_leave_ruin_unregistered :
    (∀ m, ¬ Protected rivals allActivities m) ∧
      ¬ Damages rivals allActivities .shared .ruined := by
  have none : ∀ m, ¬ Protected rivals allActivities m := by
    intro m ⟨_, h⟩
    cases m with
    | a => exact h .b True.intro (by decide) a_removes_b
    | b => exact h .a True.intro (by decide) b_removes_a
    | ruin => exact h .a True.intro (by decide) ruin_removes_a
  exact ⟨none, fun ⟨m, hp, _, _⟩ => none m hp⟩

end Generative.Naturalism

#print axioms Generative.Naturalism.can_of_enabled
#print axioms Generative.Naturalism.can_of_reach
#print axioms Generative.Naturalism.eventual_realizability_never_increases
#print axioms Generative.Naturalism.eventual_loss_is_irreversible
#print axioms Generative.Naturalism.not_damages_iff
#print axioms Generative.Naturalism.restraint_live_never_removes
#print axioms Generative.Naturalism.harmed_stuck
#print axioms Generative.Naturalism.harmed_cannot
#print axioms Generative.Naturalism.restrained_stuck
#print axioms Generative.Naturalism.restrained_cannot_harm
#print axioms Generative.Naturalism.restrained_can_live
#print axioms Generative.Naturalism.open_can
#print axioms Generative.Naturalism.harm_removes_live
#print axioms Generative.Naturalism.restrain_removes_harm
#print axioms Generative.Naturalism.restraint_protected_iff
#print axioms Generative.Naturalism.restraint_not_damage_harm_is
#print axioms Generative.Naturalism.committed_stuck
#print axioms Generative.Naturalism.committed_cannot_other
#print axioms Generative.Naturalism.committed_can_own
#print axioms Generative.Naturalism.open_can_each
#print axioms Generative.Naturalism.course_never_removes
#print axioms Generative.Naturalism.commitment_damage_depends_on_scope
#print axioms Generative.Naturalism.dip_can_from_one
#print axioms Generative.Naturalism.recoverable_dip_not_damage
#print axioms Generative.Naturalism.dip_never_removes
#print axioms Generative.Naturalism.dip_recovery_generates
#print axioms Generative.Naturalism.rivals_stuck
#print axioms Generative.Naturalism.rivals_can_iff_enabled
#print axioms Generative.Naturalism.rivals_shared_can
#print axioms Generative.Naturalism.rivals_not_enabled
#print axioms Generative.Naturalism.a_removes_b
#print axioms Generative.Naturalism.b_removes_a
#print axioms Generative.Naturalism.ruin_removes_a
#print axioms Generative.Naturalism.symmetric_rivals_leave_ruin_unregistered
