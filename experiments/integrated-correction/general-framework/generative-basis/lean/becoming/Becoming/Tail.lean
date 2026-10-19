import Becoming.Sensitivity

/-!
# Tail: what a law of the whole and no part takes

`Becoming.Sensitivity` shows that sensitivity is the least coupling, up to double negation,
wherever a law reads finitely many conditions under each history, and that with infinitely many
conditions this cannot be dropped relative to a decision taken as a hypothesis. Given a decision
of whether levels vanish from some condition on, which gives the
limited principle of omniscience (`LPO`), the tail law is sensitive to no condition and still
differs. Where the conditions are numbered by the natural numbers, every counterexample gives the
weak limited principle (`WLPO`). It leaves open where between the two the existence of a
counterexample lies. This module answers within the theory without axiom, with no premise beyond what each statement
names: a counterexample exists exactly where a rule decides, of every Boolean sequence, whether it
is `false` throughout, which is `WLPO` given as a rule; the decision of vanishing is exactly `LPO`
given as a rule.

* **A whole and no part.** A number read off levels is changed by no condition where levels
  differing at one condition only give it alike (`ChangedByNoCondition`). That holds exactly where
  levels agreeing from some condition on give it alike, the conditions below being changed one at
  a time (`ChangedByNoCondition.eq_of_agree_from`, `ChangedByNoCondition.of_agree_from`): what no
  part changes, only the tail sets. The law exchanging such a number of the levels at step `0`
  (`wholeLaw`) reads what has stood, is insensitive at every step to every condition and so
  sensitive to none, and reads through the conditions from any one on (`wholeLaw_nonanticipating`,
  `wholeLaw_insensitive`, `wholeLaw_not_sensitive`, `wholeLaw_through_from`). Where the number
  differs between two levels, the law does not read through what it is sensitive to, nor finitely
  many conditions, and the couplings it reads through have no least one
  (`wholeLaw_not_through_sensitive`, `wholeLaw_not_readsFinitely`,
  `wholeLaw_no_least_coupling`). The tail law of `Becoming.Sensitivity` is the instance of the
  indicator of vanishing (`tailLaw_eq_wholeLaw`, `vanishIndicator_changedByNoCondition`).
* **A counterexample gives a rule.** The comparison by which `Becoming.Sensitivity` mixes two
  histories along a Boolean sequence decides the sequence as a rule (`mixedDecision`). So a law
  insensitive at a step to every condition that still differs there, and a counterexample to the
  least coupling, each give a rule deciding, of every Boolean sequence, whether it is `false`
  throughout (`insensitiveDiffersDecision`, `notThroughSensitiveDecision`). Such a rule gives
  `WLPO` (`WLPO.of_rule`).
* **A rule gives a counterexample.** With such a rule, whether levels vanish from condition `N` on
  is decided, as whether no level from `N` on is above `0` (`Tail.levelsFrom`, `vanishesFrom`),
  and whether they vanish from no condition on is decided by the rule again, applied to the
  sequence of these answers (`neverIndicator`, `vanishesFrom_never_iff`). The indicator of never
  vanishing is changed by no condition and differs between levels all `0` and levels all `1`
  (`neverIndicator_changedByNoCondition`, `neverIndicator_zeros`, `neverIndicator_ones`); where
  the indicator of vanishing is also given, the two sum to `1`
  (`neverIndicator_add_vanishIndicator`). Its law (`neverLaw`) reads what has stood, is
  insensitive at every step to every condition and still differs (`neverLaw_nonanticipating`,
  `neverLaw_insensitive`, `neverLaw_not_sensitive`, `neverLaw_differs`): a counterexample built
  from the rule alone.
* **Exactly.** A number changed by no condition that still differs, a law insensitive at a step to
  every condition that still differs there, and a counterexample to the least coupling each
  exist exactly where such a rule does (`changedByNoCondition_iff_rule`,
  `insensitive_differs_iff_rule`, `not_through_sensitive_iff_rule`).
* **The decision of vanishing is the limited principle as a rule.** It gives a rule deciding, of
  every Boolean sequence, whether it has a `true` (`lpoRuleOfVanishDecision`), and such a rule
  decides vanishing, again in two passes (`raisedFrom`, `vanishDecisionOfLPORule`,
  `vanishDecision_iff_lpoRule`). That rule gives the weak one (`wlpoRuleOfLPORule`) and `LPO`
  (`LPO.of_rule`). So the tail law takes the limited principle as a rule, and a law of the whole
  and no part takes only the weak one.

**Readings (the AI's, D43).**
- A whole that depends on no part of it is given exactly where it can be decided, of every
  unending record of yes and no, whether it says no throughout: every such whole gives that
  decision, and that decision gives one. With the conditions numbered, the least coupling
  fails exactly at this omniscience and needs no more of it; the core does not assume it.
- Read as whether levels vanish eventually, the whole takes the limited principle as a rule; read
  as whether they never vanish, the same whole, telling apart the same histories, takes only the
  weak rule. Here, a whole said through what never happens is given by the weak rule alone.

What is not derived: whether the proposition `WLPO` alone gives a rule (that step chooses a
function from a relation, a principle the core does not assume); whether the weak rule gives the
limited one, or the decision of vanishing; what a counterexample gives where the conditions are not
numbered by the natural numbers; sensitivity read in time, step by step; a measure of how much a
formation's exchange depends on a condition. Equality of numbers is decided where histories are
compared, as in `Becoming.Sensitivity`, and no premise is added. No ethical predicate, ranking or
axiom occurs.

**Classical sources and scope.** `LPO` and `WLPO` are Bishop's limited and weak limited
principles of omniscience (Bishop 1967; Bridges and Richman 1987), and the exact statements here
are constructive reverse mathematics in Ishihara's sense. That `WLPO`, as a proposition, does not
give `LPO` is shown by the arithmetical hierarchy of classical principles of Akama, Berardi,
Hayashi and Kohlenbach (2004); the core neither states nor refutes the step. "Exactly" is relative to rules: the
existence of a counterexample is equivalent to a rule `Nonempty (∀ s, Decidable …)`, which is at
least as strong as the proposition `WLPO`, and the decision of vanishing is equivalent to the
rule form of `LPO`. Without such a rule the core gives no counterexample and does not refute one.
-/

namespace Becoming

variable {F C : Type}

namespace Tail

/-- Whether a level is above `0`. -/
def nonzero : Nat → Bool
  | 0 => false
  | _ + 1 => true

theorem eq_zero_of_nonzero_false : ∀ {x : Nat}, nonzero x = false → x = 0
  | 0, _ => rfl
  | _ + 1, no => Bool.noConfusion no

/-- Whether each level from condition `N` on is above `0`. -/
def levelsFrom (α : Nat → Nat) (N : Nat) : Nat → Bool :=
  fun n => nonzero (α (N + n))

theorem add_eq {a b c d : Nat} (first : a = c) (second : b = d) : a + b = c + d :=
  (congrArg (· + b) first).trans (congrArg (c + ·) second)

end Tail

/-! ## A whole and no part -/

/-- **No condition changes `f`**: levels differing at one condition only give one number. -/
def ChangedByNoCondition (f : (Nat → Nat) → Nat) : Prop :=
  ∀ (c : Nat) (α β : Nat → Nat), (∀ m, m ≠ c → α m = β m) → f α = f β

/-- **What no condition changes, only the tail sets.** Levels agreeing from some condition on give
one number, the conditions below being changed one at a time. -/
theorem ChangedByNoCondition.eq_of_agree_from {f : (Nat → Nat) → Nat}
    (fixed : ChangedByNoCondition f) :
    ∀ (n : Nat) {α β : Nat → Nat}, (∀ m, n ≤ m → α m = β m) → f α = f β
  | 0, α, β, agree => fixed 0 α β fun m _ => agree m (Nat.zero_le m)
  | n + 1, α, β, agree =>
    (fixed n α (fun m => if m = n then β m else α m) fun _ other => (if_neg other).symm).trans
      (ChangedByNoCondition.eq_of_agree_from fixed n (α := fun m => if m = n then β m else α m)
        fun m above =>
          match Nat.decEq m n with
          | isTrue same => if_pos same
          | isFalse other =>
            (if_neg other).trans
              (agree m (Nat.lt_of_le_of_ne above fun same => other same.symm)))

/-- Conversely, a number given alike by levels agreeing from some condition on is changed by no
condition. -/
theorem ChangedByNoCondition.of_agree_from {f : (Nat → Nat) → Nat}
    (tail : ∀ (n : Nat) (α β : Nat → Nat), (∀ m, n ≤ m → α m = β m) → f α = f β) :
    ChangedByNoCondition f :=
  fun c α β off => tail (c + 1) α β fun m above => off m (Nat.ne_of_gt above)

/-- **The law of a whole**: one formation exchanges with every condition, across every step, the
number `f` reads off the levels at step `0`, and gives nothing. -/
def wholeLaw (f : (Nat → Nat) → Nat) : ExchangeLaw Unit Nat :=
  ⟨fun _ _ l _ => f (l 0), fun _ _ _ _ => 0⟩

section Whole

variable {f : (Nat → Nat) → Nat}

/-- The law of a number no condition changes reads what has stood. -/
theorem wholeLaw_nonanticipating (fixed : ChangedByNoCondition f) :
    (wholeLaw f).Nonanticipating :=
  fun t _ _ _ agree _ => ⟨fixed.eq_of_agree_from 0 fun m _ => agree 0 (Nat.zero_le t) m, rfl⟩

/-- **It reads through the conditions from any one on.** Two histories agreeing up to `t` on the
conditions from `n` on give alike at `t`, whatever `n`. -/
theorem wholeLaw_reads_from (fixed : ChangedByNoCondition f) (n : Nat) {t : Nat}
    {l l' : Nat → Nat → Nat} (agree : ∀ s, s ≤ t → ∀ m, n ≤ m → l s m = l' s m) :
    (wholeLaw f).GivesAlike t () l l' :=
  fun _ => ⟨fixed.eq_of_agree_from n fun m le => agree 0 (Nat.zero_le t) m le, rfl⟩

/-- **It is insensitive to every condition at every step.** -/
theorem wholeLaw_insensitive (fixed : ChangedByNoCondition f) (t c : Nat) :
    (wholeLaw f).InsensitiveAt t () c :=
  fun l l' off _ => ⟨fixed c (l 0) (l' 0) fun m other => off 0 (Nat.zero_le t) m other, rfl⟩

/-- So it is sensitive to no condition. -/
theorem wholeLaw_not_sensitive (fixed : ChangedByNoCondition f) (c : Nat) :
    ¬ (wholeLaw f).Sensitive () c :=
  fun ⟨t, notInsensitive⟩ => notInsensitive (wholeLaw_insensitive fixed t c)

/-- It reads through the coupling of the conditions from any one on. -/
theorem wholeLaw_through_from (fixed : ChangedByNoCondition f) {W : Web Unit Nat} (n : Nat) :
    (wholeLaw f).Through W (fun _ c => n ≤ c) (fun _ => false) :=
  fun _ _ _ _ _ alike => wholeLaw_reads_from fixed n fun s le m above => (alike s le).2 m above

/-- **Where the number differs, the law does not read through what it is sensitive to.** -/
theorem wholeLaw_not_through_sensitive (fixed : ChangedByNoCondition f) {α β : Nat → Nat}
    (differs : f α ≠ f β) :
    ¬ ∀ t l l', (∀ c, (wholeLaw f).Sensitive () c → ∀ s, s ≤ t → l s c = l' s c) →
      (wholeLaw f).GivesAlike t () l l' :=
  fun reads => differs (reads 0 (fun _ => α) (fun _ => β)
    (fun c sensitive => absurd sensitive (wholeLaw_not_sensitive fixed c)) 0).1

/-- **Nor does it read finitely many conditions.** -/
theorem wholeLaw_not_readsFinitely (fixed : ChangedByNoCondition f) {α β : Nat → Nat}
    (differs : f α ≠ f β) : ¬ (wholeLaw f).ReadsFinitely :=
  fun fin => differs
    ((fin.alike_of_insensitive (wholeLaw_not_sensitive fixed) 0 (fun _ => α) (fun _ => β)) 0).1

/-- **The couplings it reads through have no least one.** For a web in which the formation
depends on nothing, a least one would hold no condition, the conditions from each one on being read
through, and the law does not read through the coupling of nothing. -/
theorem wholeLaw_no_least_coupling (fixed : ChangedByNoCondition f) {α β : Nat → Nat}
    (differs : f α ≠ f β) {W : Web Unit Nat} (free : ∀ t c, ¬ W.requires t () c) :
    ¬ ∃ obs : Unit → Nat → Prop, (wholeLaw f).Through W obs (fun _ => false) ∧
      ∀ obs' : Unit → Nat → Prop, (wholeLaw f).Through W obs' (fun _ => false) →
        ∀ c, obs () c → obs' () c :=
  fun ⟨_, through, least⟩ =>
    differs
      (through () rfl 0 (fun _ => α) (fun _ => β) (fun s _ =>
        ⟨⟨fun _ c requires => absurd requires (free s c),
          fun _ c requires => absurd requires (free s c)⟩,
         fun c seen => absurd (least _ (wholeLaw_through_from fixed (c + 1)) c seen)
           (Nat.not_succ_le_self c)⟩) 0).1

end Whole

/-- The indicator of vanishing is changed by no condition. -/
theorem vanishIndicator_changedByNoCondition
    (decides : ∀ α : Nat → Nat, Decidable (VanishFrom α)) :
    ChangedByNoCondition (vanishIndicator decides) :=
  ChangedByNoCondition.of_agree_from fun n _ _ agree => vanishIndicator_eq_of_agree decides n agree

/-- **The tail law is the law of the indicator of vanishing.** -/
theorem tailLaw_eq_wholeLaw (decides : ∀ α : Nat → Nat, Decidable (VanishFrom α)) :
    tailLaw decides = wholeLaw (vanishIndicator decides) :=
  rfl

/-! ## A counterexample gives a rule -/

/-- **A mixed history decides the sequence, as a rule.** Where a history gives alike with the first
of two histories when a Boolean sequence is `false` throughout, and with the second when it has a
`true`, and the two histories give differently with a condition, comparing two numbers decides
whether the sequence is `false` throughout. -/
def mixedDecision {law : ExchangeLaw F C} {t : Nat} {h : F} {l l' γ : Nat → C → Nat} {c : C}
    (differs : ¬ (law.take t h l c = law.take t h l' c ∧ law.give t h l c = law.give t h l' c))
    {s : Nat → Bool} (toFirst : (∀ n, s n = false) → law.GivesAlike t h γ l)
    (toSecond : ∀ n, s n = true → law.GivesAlike t h γ l') :
    Decidable (∀ n, s n = false) :=
  match Nat.decEq (law.take t h γ c) (law.take t h l c),
    Nat.decEq (law.give t h γ c) (law.give t h l c) with
  | isTrue sameTake, isTrue sameGive => isTrue fun n =>
    match hs : s n with
    | false => rfl
    | true =>
      absurd ⟨sameTake.symm.trans (toSecond n hs c).1, sameGive.symm.trans (toSecond n hs c).2⟩
        differs
  | isFalse differTake, _ => isFalse fun all => differTake (toFirst all c).1
  | isTrue _, isFalse differGive => isFalse fun all => differGive (toFirst all c).2

/-- **A law insensitive at a step to every condition that still differs there gives a rule**
deciding, of every Boolean sequence, whether it is `false` throughout. The law need not read what
has stood. -/
def insensitiveDiffersDecision {law : ExchangeLaw F Nat} {t : Nat} {h : F}
    (insensitive : ∀ c, law.InsensitiveAt t h c) {l l' : Nat → Nat → Nat} {c : Nat}
    (differs : ¬ (law.take t h l c = law.take t h l' c ∧ law.give t h l c = law.give t h l' c))
    (s : Nat → Bool) : Decidable (∀ n, s n = false) :=
  mixedDecision (γ := fun r m => bif seenBy s m then l' r m else l r m) differs
    (fun all => alike_of_agree_from insensitive 0 fun r _ e _ =>
      (congrArg (fun b => bif b then l' r e else l r e) (seenBy_false all e) : _))
    (fun n yes => alike_of_agree_from insensitive n fun r _ e above =>
      (congrArg (fun b => bif b then l' r e else l r e) (seenBy_true yes above) : _))

/-- **Every counterexample to the least coupling gives a rule** deciding, of every Boolean
sequence, whether it is `false` throughout: a law of what has stood, its conditions numbered by the
natural numbers, with two histories agreeing up to `t` on every condition it is sensitive to that
still give differently there. -/
def notThroughSensitiveDecision {law : ExchangeLaw F Nat} (na : law.Nonanticipating)
    {t : Nat} {h : F} {l l' : Nat → Nat → Nat}
    (agree : ∀ c, law.Sensitive h c → ∀ s, s ≤ t → l s c = l' s c) {c : Nat}
    (differs : ¬ (law.take t h l c = law.take t h l' c ∧ law.give t h l c = law.give t h l' c))
    (s : Nat → Bool) : Decidable (∀ n, s n = false) :=
  mixedDecision (γ := fun r m => bif seenBy s m then l' r m else l r m) differs
    (fun all => na t h _ l fun r _ e =>
      (congrArg (fun b => bif b then l' r e else l r e) (seenBy_false all e) : _))
    (fun n yes => alike_of_agree_from_sensitive na agree n
      (fun r _ e => Sensitivity.cond_either (seenBy s e) (l r e) (l' r e))
      fun r _ e above =>
        (congrArg (fun b => bif b then l' r e else l r e) (seenBy_true yes above) : _))

/-- A rule deciding, of every Boolean sequence, whether it is `false` throughout gives `WLPO`. -/
theorem WLPO.of_rule (decides : ∀ s : Nat → Bool, Decidable (∀ n, s n = false)) : WLPO :=
  fun s =>
    match decides s with
    | isTrue all => .inl all
    | isFalse notAll => .inr notAll

/-! ## A rule gives a counterexample -/

section Rule

variable (decides : ∀ s : Nat → Bool, Decidable (∀ n, s n = false))

/-- Whether the levels vanish from condition `N` on, decided by the rule: whether no level from `N`
on is above `0`. -/
def vanishesFrom (α : Nat → Nat) (N : Nat) : Bool :=
  @decide (∀ n, Tail.levelsFrom α N n = false) (decides (Tail.levelsFrom α N))

theorem vanishesFrom_true {α : Nat → Nat} {N : Nat} (yes : vanishesFrom decides α N = true) :
    ∀ m, N ≤ m → α m = 0 :=
  fun _ le =>
    match Nat.le.dest le with
    | ⟨d, eq⟩ =>
      eq ▸ Tail.eq_zero_of_nonzero_false
        (@of_decide_eq_true _ (decides (Tail.levelsFrom α N)) yes d)

theorem vanishesFrom_of {α : Nat → Nat} {N : Nat} (zero : ∀ m, N ≤ m → α m = 0) :
    vanishesFrom decides α N = true :=
  @decide_eq_true _ (decides (Tail.levelsFrom α N)) fun n =>
    (congrArg Tail.nonzero (zero (N + n) (Nat.le_add_right N n)) : _)

/-- **The levels vanish from no condition on exactly where the rule's answers are all `false`.** -/
theorem vanishesFrom_never_iff {α : Nat → Nat} :
    (∀ N, vanishesFrom decides α N = false) ↔ ¬ VanishFrom α :=
  ⟨fun never ⟨N, zero⟩ => Bool.noConfusion ((never N).symm.trans (vanishesFrom_of decides zero)),
   fun stays N => ListTests.false_of_not_true fun yes => stays ⟨N, vanishesFrom_true decides yes⟩⟩

/-- **The indicator of never vanishing, read off the rule twice**: `1` where the levels vanish from
no condition on, else `0`. -/
def neverIndicator (α : Nat → Nat) : Nat :=
  @ite Nat (∀ N, vanishesFrom decides α N = false) (decides (vanishesFrom decides α)) 1 0

theorem neverIndicator_eq_one {α : Nat → Nat} (stays : ¬ VanishFrom α) :
    neverIndicator decides α = 1 :=
  @if_pos _ (decides (vanishesFrom decides α)) ((vanishesFrom_never_iff decides).mpr stays) Nat 1 0

theorem neverIndicator_eq_zero {α : Nat → Nat} (vanishes : VanishFrom α) :
    neverIndicator decides α = 0 :=
  @if_neg _ (decides (vanishesFrom decides α))
    (fun never => (vanishesFrom_never_iff decides).mp never vanishes) Nat 1 0

/-- Levels agreeing from some condition on have one indicator of never vanishing. -/
theorem neverIndicator_eq_of_agree {α β : Nat → Nat} (n : Nat)
    (agree : ∀ m, n ≤ m → α m = β m) : neverIndicator decides α = neverIndicator decides β :=
  have toSecond : ¬ VanishFrom α → ¬ VanishFrom β := fun stays vanishes =>
    stays (VanishFrom.of_agree n (fun m le => (agree m le).symm) vanishes)
  have toFirst : ¬ VanishFrom β → ¬ VanishFrom α := fun stays vanishes =>
    stays (VanishFrom.of_agree n agree vanishes)
  match decides (vanishesFrom decides α) with
  | isTrue never =>
    have stays := (vanishesFrom_never_iff decides).mp never
    (neverIndicator_eq_one decides stays).trans
      (neverIndicator_eq_one decides (toSecond stays)).symm
  | isFalse notNever =>
    (@if_neg _ (decides (vanishesFrom decides α)) notNever Nat 1 0).trans
      (@if_neg _ (decides (vanishesFrom decides β))
        (fun never => notNever ((vanishesFrom_never_iff decides).mpr
          (toFirst ((vanishesFrom_never_iff decides).mp never)))) Nat 1 0).symm

/-- **The indicator of never vanishing is changed by no condition.** -/
theorem neverIndicator_changedByNoCondition : ChangedByNoCondition (neverIndicator decides) :=
  ChangedByNoCondition.of_agree_from fun n _ _ agree => neverIndicator_eq_of_agree decides n agree

/-- Levels all `0` vanish. -/
theorem neverIndicator_zeros : neverIndicator decides (fun _ => 0) = 0 :=
  neverIndicator_eq_zero decides ⟨0, fun _ _ => rfl⟩

/-- Levels all `1` never do. -/
theorem neverIndicator_ones : neverIndicator decides (fun _ => 1) = 1 :=
  neverIndicator_eq_one decides fun ⟨n, zero⟩ => Nat.noConfusion (zero n (Nat.le_refl n))

/-- **The same whole from the other side.** Where the decision of vanishing is also given, the
indicators of vanishing and of never vanishing sum to `1`. -/
theorem neverIndicator_add_vanishIndicator
    (vanishDecides : ∀ α : Nat → Nat, Decidable (VanishFrom α)) (α : Nat → Nat) :
    neverIndicator decides α + vanishIndicator vanishDecides α = 1 :=
  match vanishDecides α with
  | isTrue vanishes =>
    (Tail.add_eq (neverIndicator_eq_zero decides vanishes)
      (vanishIndicator_eq_one vanishDecides vanishes) : _)
  | isFalse stays =>
    (Tail.add_eq (neverIndicator_eq_one decides stays)
      (vanishIndicator_eq_zero vanishDecides stays) : _)

/-- **The law of levels that never vanish**: one formation exchanges with every condition, across
every step, the indicator of the levels at step `0` vanishing from no condition on, and gives
nothing. -/
def neverLaw : ExchangeLaw Unit Nat :=
  wholeLaw (neverIndicator decides)

/-- It reads what has stood. -/
theorem neverLaw_nonanticipating : (neverLaw decides).Nonanticipating :=
  wholeLaw_nonanticipating (neverIndicator_changedByNoCondition decides)

/-- It is insensitive to every condition at every step. -/
theorem neverLaw_insensitive (t c : Nat) : (neverLaw decides).InsensitiveAt t () c :=
  wholeLaw_insensitive (neverIndicator_changedByNoCondition decides) t c

/-- So it is sensitive to no condition. -/
theorem neverLaw_not_sensitive (c : Nat) : ¬ (neverLaw decides).Sensitive () c :=
  wholeLaw_not_sensitive (neverIndicator_changedByNoCondition decides) c

/-- **Yet it differs between two histories**: all levels `0` and all levels `1`. -/
theorem neverLaw_differs (t c : Nat) :
    (neverLaw decides).take t () (fun _ _ => 0) c ≠ (neverLaw decides).take t () (fun _ _ => 1) c :=
  fun same => Nat.noConfusion
    ((neverIndicator_zeros decides).symm.trans (same.trans (neverIndicator_ones decides)))

end Rule

/-! ## Exactly -/

/-- **A number changed by no condition that still differs exists exactly where a rule decides, of
every Boolean sequence, whether it is `false` throughout.** -/
theorem changedByNoCondition_iff_rule :
    (∃ f : (Nat → Nat) → Nat, ChangedByNoCondition f ∧ ∃ α β, f α ≠ f β) ↔
      Nonempty (∀ s : Nat → Bool, Decidable (∀ n, s n = false)) :=
  ⟨fun ⟨_, fixed, α, β, differs⟩ =>
    ⟨insensitiveDiffersDecision (l := fun _ => α) (l' := fun _ => β) (c := 0)
      (wholeLaw_insensitive fixed 0) fun same => differs same.1⟩,
   fun ⟨decides⟩ =>
    ⟨neverIndicator decides, neverIndicator_changedByNoCondition decides, fun _ => 0, fun _ => 1,
     fun same => Nat.noConfusion
       ((neverIndicator_zeros decides).symm.trans (same.trans (neverIndicator_ones decides)))⟩⟩

/-- **A law insensitive at a step to every condition that still differs there exists exactly where
such a rule does.** -/
theorem insensitive_differs_iff_rule :
    (∃ (F : Type) (law : ExchangeLaw F Nat) (t : Nat) (h : F) (l l' : Nat → Nat → Nat) (c : Nat),
      (∀ e, law.InsensitiveAt t h e) ∧
        ¬ (law.take t h l c = law.take t h l' c ∧ law.give t h l c = law.give t h l' c)) ↔
      Nonempty (∀ s : Nat → Bool, Decidable (∀ n, s n = false)) :=
  ⟨fun ⟨_, _, _, _, _, _, _, insensitive, differs⟩ =>
    ⟨insensitiveDiffersDecision insensitive differs⟩,
   fun ⟨decides⟩ =>
    ⟨Unit, neverLaw decides, 0, (), fun _ _ => 0, fun _ _ => 1, 0, neverLaw_insensitive decides 0,
     fun same => neverLaw_differs decides 0 0 same.1⟩⟩

/-- **A counterexample to the least coupling exists exactly where such a rule does**: a law of
what has stood, its conditions numbered by the natural numbers, with two histories agreeing up to a
step on every condition it is sensitive to that still give differently there. -/
theorem not_through_sensitive_iff_rule :
    (∃ (F : Type) (law : ExchangeLaw F Nat) (t : Nat) (h : F) (l l' : Nat → Nat → Nat) (c : Nat),
      law.Nonanticipating ∧ (∀ e, law.Sensitive h e → ∀ s, s ≤ t → l s e = l' s e) ∧
        ¬ (law.take t h l c = law.take t h l' c ∧ law.give t h l c = law.give t h l' c)) ↔
      Nonempty (∀ s : Nat → Bool, Decidable (∀ n, s n = false)) :=
  ⟨fun ⟨_, _, _, _, _, _, _, na, agree, differs⟩ =>
    ⟨notThroughSensitiveDecision na agree differs⟩,
   fun ⟨decides⟩ =>
    ⟨Unit, neverLaw decides, 0, (), fun _ _ => 0, fun _ _ => 1, 0,
     neverLaw_nonanticipating decides,
     fun e sensitive => absurd sensitive (neverLaw_not_sensitive decides e),
     fun same => neverLaw_differs decides 0 0 same.1⟩⟩

/-! ## The decision of vanishing is the limited principle as a rule -/

/-- **The decision of vanishing gives a rule** deciding, of every Boolean sequence, whether it has a
`true`: levels `1` before its first `true` and `0` from it on vanish exactly where it has one. -/
def lpoRuleOfVanishDecision (decides : ∀ α : Nat → Nat, Decidable (VanishFrom α))
    (s : Nat → Bool) : Decidable (∃ n, s n = true) :=
  match decides (fun m => bif seenBy s m then 0 else 1) with
  | isTrue vanishes =>
    isTrue
      (match vanishes with
       | ⟨n, zero⟩ =>
         seenBy_exists (m := n)
           (match seen : seenBy s n with
            | true => rfl
            | false =>
              Nat.noConfusion
                ((congrArg (fun b => bif b then 0 else 1) seen).symm.trans
                  (zero n (Nat.le_refl n)) : 1 = 0)))
  | isFalse stays =>
    isFalse fun ⟨n, yes⟩ =>
      stays ⟨n, fun _ le => ((congrArg (fun b => bif b then 0 else 1) (seenBy_true yes le)) : _)⟩

section LimitedRule

variable (decides : ∀ s : Nat → Bool, Decidable (∃ n, s n = true))

/-- Whether some level from condition `N` on is above `0`, decided by the rule. -/
def raisedFrom (α : Nat → Nat) (N : Nat) : Bool :=
  @decide (∃ n, Tail.levelsFrom α N n = true) (decides (Tail.levelsFrom α N))

theorem raisedFrom_false {α : Nat → Nat} {N : Nat} (quiet : raisedFrom decides α N = false) :
    ∀ m, N ≤ m → α m = 0 :=
  fun _ le =>
    match Nat.le.dest le with
    | ⟨d, eq⟩ =>
      eq ▸ Tail.eq_zero_of_nonzero_false (ListTests.false_of_not_true fun yes =>
        @of_decide_eq_false _ (decides (Tail.levelsFrom α N)) quiet ⟨d, yes⟩)

theorem raisedFrom_of {α : Nat → Nat} {N : Nat} (zero : ∀ m, N ≤ m → α m = 0) :
    raisedFrom decides α N = false :=
  @decide_eq_false _ (decides (Tail.levelsFrom α N)) fun ⟨n, yes⟩ =>
    Bool.noConfusion
      ((congrArg Tail.nonzero (zero (N + n) (Nat.le_add_right N n))).symm.trans yes)

/-- **The limited principle as a rule decides vanishing**, in two passes: whether some level from
`N` on is above `0`, for each `N`, and whether the answer is no for some `N`. -/
def vanishDecisionOfLPORule (α : Nat → Nat) : Decidable (VanishFrom α) :=
  match decides (fun N => !raisedFrom decides α N) with
  | isTrue quiet =>
    isTrue
      (match quiet with
       | ⟨N, yes⟩ => ⟨N, raisedFrom_false decides (ListTests.false_of_not yes)⟩)
  | isFalse loud =>
    isFalse fun ⟨N, zero⟩ => loud ⟨N, ListTests.not_eq_true_of_false (raisedFrom_of decides zero)⟩

/-- **The limited principle as a rule gives the weak one as a rule.** -/
def wlpoRuleOfLPORule (s : Nat → Bool) : Decidable (∀ n, s n = false) :=
  match decides s with
  | isTrue found =>
    isFalse fun all =>
      match found with
      | ⟨n, yes⟩ => Bool.noConfusion ((all n).symm.trans yes)
  | isFalse absent => isTrue fun n => ListTests.false_of_not_true fun yes => absent ⟨n, yes⟩

end LimitedRule

/-- A rule deciding, of every Boolean sequence, whether it has a `true` gives `LPO`. -/
theorem LPO.of_rule (decides : ∀ s : Nat → Bool, Decidable (∃ n, s n = true)) : LPO :=
  fun s =>
    match decides s with
    | isTrue found => .inl found
    | isFalse absent => .inr fun n => ListTests.false_of_not_true fun yes => absent ⟨n, yes⟩

/-- **The decision of vanishing is exactly the limited principle as a rule.** -/
theorem vanishDecision_iff_lpoRule :
    Nonempty (∀ α : Nat → Nat, Decidable (VanishFrom α)) ↔
      Nonempty (∀ s : Nat → Bool, Decidable (∃ n, s n = true)) :=
  ⟨fun ⟨decides⟩ => ⟨lpoRuleOfVanishDecision decides⟩,
   fun ⟨decides⟩ => ⟨vanishDecisionOfLPORule decides⟩⟩

end Becoming
