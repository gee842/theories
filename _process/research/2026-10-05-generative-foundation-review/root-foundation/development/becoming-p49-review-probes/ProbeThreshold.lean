import Becoming.Testing

/-!
# Probe A: threshold blindness, sharpened

Sixteenth review of P47. Checks:
* A0  `threshold_blind_no_webs`: `Flow.Balances.threshold_blind` holds with no hypothesis on the
  second web's requirements or needs (they are passed only to the recursive call).
* A1  `alike_keeps_difference`: while `g` registers alike, responses through registration keep
  the difference on every registered condition exactly as it was at the start. No start
  hypothesis, no `DecidableEq`, any number of stocks.
* A2  `alike_while_poorer_supported`: richer (≥) on every registered condition at the start and
  alike on every observed one: `g` registers alike at every step before which the poorer web
  supported it. No `DecidableEq`, several stocks.
* A3  `alike_iff_richer_only`: at a step at which the invariants hold, registering alike is
  exactly: wherever the richer web supports `g`, so does the poorer.
* A4  `changed_after_divergence`: a registered difference changes only after a step at which
  the two webs' support of `g` diverged (richer supported, poorer not), not merely after the
  poorer failed: a joint failure leaves the difference untouched.
* A5  `threshold_blind_of_general`: the module's `threshold_blind` is a corollary of A1 + A2.
* A6  `JointFailure`: the poorer web fails to support `g` at a step and the reserve is still
  untouched after it, because the richer web fails too (failure on another condition).
* A7  `Attracting`: a taker that responds to the stock directly; the richer web ends `g`
  first. `RespondsThrough` fails, and so does the reading "the surplus waits for the break".
-/

namespace Becoming.Review47

open Becoming Generative

variable {F C : Type}

theorem shift_le {a b x y : Nat} (same : a + x = b + y) (le : x ≤ y) : b ≤ a :=
  Becoming.le_of_add_le_add_right x
    (Nat.le_trans (Nat.add_le_add_left le b) (Nat.le_of_eq same.symm))

theorem shift_eq {a b x y : Nat} (same : a + x = b + y) (eq : x = y) : b = a :=
  (add_right_cancel x (same.trans (congrArg (b + ·) eq.symm))).symm

namespace Flow

variable {L L' : Flow F C} {W W' : Web F C} {obs : F → C → Prop} {g : F}

/-- A0. The module's theorem without the hypotheses on the second web. -/
theorem threshold_blind_no_webs [DecidableEq C] {c : C} {d : Nat}
    (balances : L.Balances W) (balances' : L'.Balances W')
    (depends : W.DependsOn g c) (unobserved : ¬ obs g c)
    (stock : W'.level 0 c = W.level 0 c + d)
    (start : ∀ e, W.Registers obs g e → e ≠ c → W.level 0 e = W'.level 0 e)
    (responds : L.RespondsThrough W L' W' obs g) :
    ∀ t, (∀ s, s < t → W.Supported s g) →
      W'.level t c = W.level t c + d ∧ (∀ e, W.Registers obs g e → e ≠ c →
        W.level t e = W'.level t e) ∧ ∀ s, s < t → W.RegistersAlike obs g W.level W'.level s :=
  -- `W` itself serves as a web agreeing with itself; the second web's requirements never enter.
  fun t supported =>
    have trivialWeb : ∀ t e, W.requires t g e ↔ W.requires t g e := fun _ _ => Iff.rfl
    -- Use the module's theorem with the second web's requirements replaced by the first's:
    -- the conclusion mentions only `W.level`, `W'.level` and `W.Admits`.
    let W'' : Web F C := { W' with requires := W.requires, need := W.need }
    have balances'' : L'.Balances W'' := balances'
    have responds'' : L.RespondsThrough W L' W'' obs g := responds
    balances.threshold_blind (W' := W'') balances'' trivialWeb (fun _ _ => rfl) depends
      unobserved stock start responds'' t supported

/-- A1. While `g` registers alike, every difference on a registered condition is kept. -/
theorem alike_keeps_difference (balances : L.Balances W) (balances' : L'.Balances W')
    (responds : L.RespondsThrough W L' W' obs g) :
    ∀ t, (∀ s, s < t → W.RegistersAlike obs g W.level W'.level s) →
      ∀ e, W.Registers obs g e → W'.level t e + W.level 0 e = W.level t e + W'.level 0 e
  | 0, _, _, _ => Nat.add_comm _ _
  | t + 1, alike, e, registers =>
    have ih := alike_keeps_difference balances balances' responds t
      (fun s before => alike s (Nat.lt_succ_of_lt before)) e registers
    match responds t (fun s le => alike s (Nat.lt_succ_of_le le)) e registers with
    | ⟨taken, given⟩ => add_right_cancel (L.taken t e)
        (calc W'.level (t + 1) e + W.level 0 e + L.taken t e
            = W'.level (t + 1) e + L.taken t e + W.level 0 e := Nat.add_right_comm _ _ _
          _ = W'.level (t + 1) e + L'.taken t e + W.level 0 e :=
              congrArg (fun x => W'.level (t + 1) e + x + W.level 0 e) taken
          _ = W'.level t e + L'.given t e + W.level 0 e := congrArg (· + W.level 0 e) (balances' t e)
          _ = W'.level t e + W.level 0 e + L'.given t e := Nat.add_right_comm _ _ _
          _ = W.level t e + W'.level 0 e + L'.given t e := congrArg (· + L'.given t e) ih
          _ = W.level t e + W'.level 0 e + L.given t e := congrArg (_ + ·) given.symm
          _ = W.level t e + L.given t e + W'.level 0 e := Nat.add_right_comm _ _ _
          _ = W.level (t + 1) e + L.taken t e + W'.level 0 e :=
              congrArg (· + W'.level 0 e) (balances t e).symm
          _ = W.level (t + 1) e + W'.level 0 e + L.taken t e := Nat.add_right_comm _ _ _)

/-- The invariants at a step: the richer web is at least as rich on every registered condition,
and alike on every observed one. -/
def Richer (W W' : Web F C) (obs : F → C → Prop) (g : F) (t : Nat) : Prop :=
  (∀ e, W.Registers obs g e → W.level t e ≤ W'.level t e) ∧
    ∀ e, obs g e → W.level t e = W'.level t e

/-- A3. Under the invariants, registering alike at a step is exactly: wherever the richer web
supports `g` there, so does the poorer. -/
theorem alike_iff_richer_only {t : Nat} (richer : Richer W W' obs g t) :
    W.RegistersAlike obs g W.level W'.level t ↔ (W.Admits (W'.level t) t g → W.Supported t g) :=
  ⟨fun alike => alike.1.mpr,
   fun back => ⟨⟨fun supported e requires =>
       Nat.le_trans (supported e requires) (richer.1 e (.inl ⟨t, requires⟩)), back⟩,
     richer.2⟩⟩

/-- The invariants hold while `g` registers alike, from richer and observed-alike starts. -/
theorem richer_while_alike (balances : L.Balances W) (balances' : L'.Balances W')
    (richer : ∀ e, W.Registers obs g e → W.level 0 e ≤ W'.level 0 e)
    (observedAlike : ∀ e, obs g e → W.level 0 e = W'.level 0 e)
    (responds : L.RespondsThrough W L' W' obs g) {t : Nat}
    (alike : ∀ s, s < t → W.RegistersAlike obs g W.level W'.level s) : Richer W W' obs g t :=
  ⟨fun e registers => shift_le (alike_keeps_difference balances balances' responds t alike e
      registers) (richer e registers),
   fun e observed => shift_eq (alike_keeps_difference balances balances' responds t alike e
      (.inr observed)) (observedAlike e observed)⟩

/-- A2. Several stocks, no `DecidableEq`: richer on every registered condition and alike on
every observed one at the start, `g` registers alike at every step before which the poorer web
supported it. -/
theorem alike_while_poorer_supported (balances : L.Balances W) (balances' : L'.Balances W')
    (richer : ∀ e, W.Registers obs g e → W.level 0 e ≤ W'.level 0 e)
    (observedAlike : ∀ e, obs g e → W.level 0 e = W'.level 0 e)
    (responds : L.RespondsThrough W L' W' obs g) :
    ∀ t, (∀ s, s < t → W.Supported s g) → ∀ s, s < t → W.RegistersAlike obs g W.level W'.level s
  | 0, _, s, before => absurd before (Nat.not_lt_zero s)
  | t + 1, supported, s, before =>
    have past := alike_while_poorer_supported balances balances' richer observedAlike responds t
      (fun s before => supported s (Nat.lt_succ_of_lt before))
    match Nat.lt_or_eq_of_le (Nat.le_of_lt_succ before) with
    | .inl earlier => past s earlier
    | .inr same => same ▸
        (alike_iff_richer_only (richer_while_alike balances balances' richer observedAlike
          responds past)).mpr fun _ => supported t (Nat.lt_succ_self t)

/-- A4. A registered difference changes only after a step at which the webs' support of `g`
diverged with the richer supporting and the poorer not. A joint failure does not count. -/
theorem changed_after_divergence (balances : L.Balances W) (balances' : L'.Balances W')
    (richer : ∀ e, W.Registers obs g e → W.level 0 e ≤ W'.level 0 e)
    (observedAlike : ∀ e, obs g e → W.level 0 e = W'.level 0 e)
    (responds : L.RespondsThrough W L' W' obs g) {t : Nat} {e : C}
    (registers : W.Registers obs g e)
    (changed : W'.level t e + W.level 0 e ≠ W.level t e + W'.level 0 e) :
    ¬ ∀ s, s < t → (W.Admits (W'.level s) s g → W.Supported s g) :=
  fun never =>
    have alike : ∀ t', t' ≤ t → ∀ s, s < t' → W.RegistersAlike obs g W.level W'.level s :=
      fun t' => Nat.rec (motive := fun t' => t' ≤ t → ∀ s, s < t' → W.RegistersAlike obs g W.level W'.level s)
        (fun _ s before => absurd before (Nat.not_lt_zero s))
        (fun k ih le s before =>
          have past := ih (Nat.le_of_succ_le le)
          match Nat.lt_or_eq_of_le (Nat.le_of_lt_succ before) with
          | .inl earlier => past s earlier
          | .inr same => same ▸ (alike_iff_richer_only (richer_while_alike balances balances'
              richer observedAlike responds past)).mpr (never k (Nat.lt_of_lt_of_le
                (Nat.lt_succ_self k) le)))
        t'
    changed (alike_keeps_difference balances balances' responds t (alike t (Nat.le_refl t)) e
      registers)

/-- A5. The module's theorem follows from A1 and A2. -/
theorem threshold_blind_of_general [DecidableEq C] {c : C} {d : Nat}
    (balances : L.Balances W) (balances' : L'.Balances W')
    (depends : W.DependsOn g c) (unobserved : ¬ obs g c)
    (stock : W'.level 0 c = W.level 0 c + d)
    (start : ∀ e, W.Registers obs g e → e ≠ c → W.level 0 e = W'.level 0 e)
    (responds : L.RespondsThrough W L' W' obs g) :
    ∀ t, (∀ s, s < t → W.Supported s g) →
      W'.level t c = W.level t c + d ∧ (∀ e, W.Registers obs g e → e ≠ c →
        W.level t e = W'.level t e) ∧ ∀ s, s < t → W.RegistersAlike obs g W.level W'.level s :=
  have richer : ∀ e, W.Registers obs g e → W.level 0 e ≤ W'.level 0 e := fun e registers =>
    match decEq e c with
    | isTrue same => same ▸ Nat.le_trans (Nat.le_add_right _ d) (Nat.le_of_eq stock.symm)
    | isFalse other => Nat.le_of_eq (start e registers other)
  have observedAlike : ∀ e, obs g e → W.level 0 e = W'.level 0 e := fun e observed =>
    start e (.inr observed) fun same => unobserved (same ▸ observed)
  fun t supported =>
    have alike := alike_while_poorer_supported balances balances' richer observedAlike responds t
      supported
    have keep := alike_keeps_difference balances balances' responds t alike
    ⟨add_right_cancel (W.level 0 c) ((keep c (.inl depends)).trans
        ((congrArg (W.level t c + ·) stock).trans
          ((Nat.add_assoc _ _ _).symm.trans (Nat.add_right_comm _ _ _)))),
     fun e registers other => shift_eq (keep e registers) (start e registers other),
     alike⟩

end Flow

/-! ### A6. A joint failure leaves the reserve untouched -/

namespace JointFailure

/-- Two conditions: the stock (`true`) and a second requirement (`false`). -/
def flow (draw : Nat → Nat) : Flow Unit Bool where
  present _ := [()]
  take t _ _ := draw t
  give _ _ _ := 0

/-- One unit at step 0 only. -/
def draw : Nat → Nat
  | 0 => 1
  | _ + 1 => 0

/-- Stock starts at `s`, second requirement stands at 1 at step 0 and 0 after. -/
def web (s : Nat) : Web Unit Bool where
  level t c := match c, t with
    | true, 0 => s
    | true, _ + 1 => s - 1
    | false, 0 => 1
    | false, _ + 1 => 0
  active _ _ := True
  requires _ _ _ := True
  need _ _ _ := 1
  draws _ _ _ := True

theorem balances_two : (flow draw).Balances (web 2)
  | 0, true => rfl
  | 0, false => rfl
  | _ + 1, true => rfl
  | _ + 1, false => rfl

theorem balances_three : (flow draw).Balances (web 3)
  | 0, true => rfl
  | 0, false => rfl
  | _ + 1, true => rfl
  | _ + 1, false => rfl

/-- Both webs fail `g` from step 1 on (the second requirement is gone), and responses through
support only agree; yet the stock difference stays one at every step: the poorer web's failure
is not a divergence and nothing draws on the reserve. -/
theorem untouched_after_joint_failure :
    (flow draw).Balances (web 2) ∧ (flow draw).Balances (web 3) ∧
    (flow draw).RespondsThrough (web 2) (flow draw) (web 3) supportOnly () ∧
      ¬ (web 2).Supported 1 () ∧ ¬ (web 3).Supported 1 () ∧
      ∀ t, (web 3).level t true = (web 2).level t true + 1 :=
  ⟨balances_two, balances_three, fun _ _ _ _ => ⟨rfl, rfl⟩,
   fun supported => Nat.not_succ_le_zero 0 (supported false trivial),
   fun supported => Nat.not_succ_le_zero 0 (supported false trivial),
   fun t => match t with
    | 0 => rfl
    | _ + 1 => rfl⟩

end JointFailure

/-! ### A7. A reserve that attracts a taker ends `g` sooner -/

namespace Attracting

inductive Formation where
  | dependent
  | taker

open Formation

/-- Poorer: the dependent draws one unit at steps 0 and 1. -/
def poorFlow : Flow Formation Unit where
  present _ := [dependent, taker]
  take t f _ := match f, t with
    | dependent, 0 => 1
    | dependent, 1 => 1
    | dependent, _ + 2 => 0
    | taker, _ => 0
  give _ _ _ := 0

/-- Richer: the taker, drawn by a stock of three, takes two units at step 0; the dependent draws
one. -/
def richFlow : Flow Formation Unit where
  present _ := [dependent, taker]
  take t f _ := match f, t with
    | dependent, 0 => 1
    | dependent, _ + 1 => 0
    | taker, 0 => 2
    | taker, _ + 1 => 0
  give _ _ _ := 0

def poorLevel : Nat → Nat
  | 0 => 2
  | 1 => 1
  | _ + 2 => 0

def richLevel : Nat → Nat
  | 0 => 3
  | _ + 1 => 0

def web (level : Nat → Nat) : Web Formation Unit where
  level t _ := level t
  active t f := match f with
    | dependent => 1 ≤ level t
    | taker => True
  requires _ f _ := match f with
    | dependent => True
    | taker => False
  need _ _ _ := 1
  draws _ _ _ := True

theorem poor_balances : poorFlow.Balances (web poorLevel)
  | 0, () => rfl
  | 1, () => rfl
  | _ + 2, () => rfl

theorem rich_balances : richFlow.Balances (web richLevel)
  | 0, () => rfl
  | _ + 1, () => rfl

theorem dependent_web (level : Nat → Nat) : (web level).Dependent
  | _, Formation.dependent, active, _, _ => active
  | _, Formation.taker, _, _, no => nomatch no

/-- The richer web, one unit richer at the start, fails the dependent at step 1, where the
poorer still supports it: the richer web breaks first. The flows do not respond through
support only (at step 0 the dependent registers alike, and the totals differ). -/
theorem richer_breaks_first :
    poorFlow.Balances (web poorLevel) ∧ richFlow.Balances (web richLevel) ∧
      (web poorLevel).Dependent ∧ (web richLevel).Dependent ∧
      (web richLevel).level 0 () = (web poorLevel).level 0 () + 1 ∧
      (web poorLevel).RegistersAlike supportOnly dependent (web poorLevel).level
        (web richLevel).level 0 ∧
      (web poorLevel).Supported 1 dependent ∧ ¬ (web richLevel).Supported 1 dependent ∧
      ¬ (web poorLevel).RegistersAlike supportOnly dependent (web poorLevel).level
        (web richLevel).level 1 ∧
      ¬ poorFlow.RespondsThrough (web poorLevel) richFlow (web richLevel) supportOnly dependent :=
  have alike0 : (web poorLevel).RegistersAlike supportOnly dependent (web poorLevel).level
      (web richLevel).level 0 :=
    ⟨⟨fun _ _ _ => Nat.le_succ_of_le (Nat.le_succ 1), fun _ _ _ => Nat.le_succ 1⟩,
     fun _ no => False.elim no⟩
  ⟨poor_balances, rich_balances, dependent_web _, dependent_web _, rfl, alike0,
   fun _ _ => Nat.le_refl 1,
   fun supported => Nat.not_succ_le_zero 0 (supported () trivial),
   fun alike => Nat.not_succ_le_zero 0 ((alike.1.mp fun _ _ => Nat.le_refl 1) () trivial),
   fun responds => absurd (responds 0 (fun s le => match s, le with
       | 0, _ => alike0
       | _ + 1, le => absurd le (Nat.not_succ_le_zero _)) () (.inl ⟨0, trivial⟩)).1
     (fun same => Nat.noConfusion (Nat.succ.inj same))⟩

end Attracting


/-! ### A8. What registers of one condition: its threshold if unobserved, its level if observed -/

namespace Exact

variable {W : Web F C} {obs : F → C → Prop} {g : F} {l l' : Nat → C → Nat} {s : Nat}

/-- With every other registered condition alike at `s`, an unobserved condition registers only
whether it meets the need: if it meets it under both histories or under neither, `g` registers
alike, whatever the two levels are. -/
theorem registers_threshold_only [DecidableEq C] {c : C} (unobserved : ¬ obs g c)
    (others : ∀ e, W.Registers obs g e → e ≠ c → l s e = l' s e)
    (threshold : W.requires s g c → (W.need s g c ≤ l s c ↔ W.need s g c ≤ l' s c)) :
    W.RegistersAlike obs g l l' s :=
  ⟨⟨fun admits e requires => match decEq e c with
      | isTrue same => match e, same, requires with
        | _, rfl, requires => (threshold requires).mp (admits _ requires)
      | isFalse other => Nat.le_trans (admits e requires)
          (Nat.le_of_eq (others e (.inl ⟨s, requires⟩) other)),
    fun admits e requires => match decEq e c with
      | isTrue same => match e, same, requires with
        | _, rfl, requires => (threshold requires).mpr (admits _ requires)
      | isFalse other => Nat.le_trans (admits e requires)
          (Nat.le_of_eq (others e (.inl ⟨s, requires⟩) other).symm)⟩,
   fun e observed => others e (.inr observed) fun same => unobserved (same ▸ observed)⟩

/-- An observed condition registers its level: any difference in it at `s` is registered. -/
theorem observed_registers_level {c : C} (observed : obs g c) (differ : l s c ≠ l' s c) :
    ¬ W.RegistersAlike obs g l l' s :=
  fun alike => differ (alike.2 c observed)

end Exact

end Becoming.Review47

open Becoming.Review47
#print axioms Flow.threshold_blind_no_webs
#print axioms Flow.alike_keeps_difference
#print axioms Flow.alike_iff_richer_only
#print axioms Flow.richer_while_alike
#print axioms Flow.alike_while_poorer_supported
#print axioms Flow.changed_after_divergence
#print axioms Flow.threshold_blind_of_general
#print axioms JointFailure.untouched_after_joint_failure
#print axioms Attracting.richer_breaks_first
#print axioms Exact.registers_threshold_only
#print axioms Exact.observed_registers_level
#print axioms shift_le
#print axioms shift_eq
