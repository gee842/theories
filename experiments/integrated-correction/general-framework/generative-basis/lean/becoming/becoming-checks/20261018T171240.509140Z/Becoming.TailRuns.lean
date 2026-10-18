import Becoming.Tail

/-!
# Tail runs: the omniscience a law of the whole takes, stated of every run

`Becoming.Sensitivity` and `Becoming.Tail` calibrate a law of the whole and no part, and a
counterexample to the least coupling, by principles of omniscience about Boolean sequences
and level sequences. Every sequence is a run: a history is a run of the law it shows
(`Shown.run`), and a Boolean or a level a map takes along a run of any process is a sequence. So
each principle is a statement about every run of every process: deciding, of every run, whether
the Boolean a map takes along it is `false` throughout (`FalseRule`, `FalseDecided`, the weak limited
principle), whether it is ever `true` (`TrueRule`, `TrueDecided`, the limited principle), and
whether the level a map takes along it vanishes from some step on (`VanishRule`). This module states the
calibrations of `Becoming.Sensitivity` and `Becoming.Tail` in these terms and proves them through
them.

* **Every run is a sequence and every sequence a run.** Each rule or principle stated of every
  run is the one stated of every sequence (`falseRule_iff`, `trueRule_iff`, `vanishRule_iff`,
  `wlpo_iff_runs`, `lpo_iff_runs`).
* **A whole and no part is decided of every run.** A number changed by no condition that still
  differs, a law insensitive at a step to every condition that still differs there, and a
  counterexample to the least coupling each exist exactly where it is decided, of every run,
  whether its Boolean is `false` throughout (`changedByNoCondition_iff_runs`,
  `insensitive_differs_iff_runs`, `not_through_sensitive_iff_runs`). Each such law, given, decides
  it of every run (`insensitive_differs_decides`, `not_through_sensitive_decides`).
* **Vanishing along a run is the limited principle.** Deciding of every run whether its level
  vanishes from some step on is exactly deciding of every run whether its Boolean is ever `true`
  (`vanishRule_iff_trueRule`), and it gives the limited principle of every run
  (`vanish_decides`). Given both decisions, the levels a map takes along a run are indicated as vanishing
  or as never vanishing, exactly one (`indicators_sum`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

namespace TailRuns

/-! ## Rules and principles of every run -/

/-- A rule deciding, of every run of every process and every Boolean map along it, whether the
Boolean is `false` throughout. -/
def FalseRule : Type 1 :=
  ∀ (S A : Type) (P : Process S A) (reg : S → Bool) (r : Run P),
    Decidable (∀ n, reg (r.state n) = false)

/-- A rule deciding, of every run and every Boolean map along it, whether it is ever `true`. -/
def TrueRule : Type 1 :=
  ∀ (S A : Type) (P : Process S A) (reg : S → Bool) (r : Run P),
    Decidable (∃ n, reg (r.state n) = true)

/-- A rule deciding, of every run and every level map along it, whether the level vanishes from
some step on. -/
def VanishRule : Type 1 :=
  ∀ (S A : Type) (P : Process S A) (lev : S → Nat) (r : Run P),
    Decidable (VanishFrom fun n => lev (r.state n))

/-- Of every run and every Boolean map along it, the Boolean is `false` throughout or not. -/
def FalseDecided : Prop :=
  ∀ (S A : Type) (P : Process S A) (reg : S → Bool) (r : Run P),
    (∀ n, reg (r.state n) = false) ∨ ¬ ∀ n, reg (r.state n) = false

/-- Of every run and every Boolean map along it, the Boolean is somewhere `true` or `false`
throughout. -/
def TrueDecided : Prop :=
  ∀ (S A : Type) (P : Process S A) (reg : S → Bool) (r : Run P),
    (∃ n, reg (r.state n) = true) ∨ ∀ n, reg (r.state n) = false

/-- The decision for every Boolean sequence, read off a rule of every run. -/
def FalseRule.sequences (decides : FalseRule) (s : Nat → Bool) : Decidable (∀ n, s n = false) :=
  decides Bool Unit _ id (Shown.run s fun _ => ())

/-- **Deciding of every run whether its Boolean is `false` throughout is deciding it of
every Boolean sequence.** -/
theorem falseRule_iff :
    Nonempty FalseRule ↔ Nonempty (∀ s : Nat → Bool, Decidable (∀ n, s n = false)) :=
  ⟨fun ⟨decides⟩ => ⟨decides.sequences⟩,
   fun ⟨decides⟩ => ⟨fun _ _ _ reg r => decides fun n => reg (r.state n)⟩⟩

/-- **Deciding of every run whether its Boolean is ever `true` is deciding it of every
Boolean sequence.** -/
theorem trueRule_iff :
    Nonempty TrueRule ↔ Nonempty (∀ s : Nat → Bool, Decidable (∃ n, s n = true)) :=
  ⟨fun ⟨decides⟩ => ⟨fun s => decides Bool Unit _ id (Shown.run s fun _ => ())⟩,
   fun ⟨decides⟩ => ⟨fun _ _ _ reg r => decides fun n => reg (r.state n)⟩⟩

/-- The decision of vanishing for every level sequence, read off a rule of every run. -/
def VanishRule.sequences (decides : VanishRule) (α : Nat → Nat) : Decidable (VanishFrom α) :=
  decides Nat Unit _ id (Shown.run α fun _ => ())

/-- **Deciding of every run whether its level vanishes from some step on is deciding it of every
level sequence.** -/
theorem vanishRule_iff :
    Nonempty VanishRule ↔ Nonempty (∀ α : Nat → Nat, Decidable (VanishFrom α)) :=
  ⟨fun ⟨decides⟩ => ⟨decides.sequences⟩,
   fun ⟨decides⟩ => ⟨fun _ _ _ lev r => decides fun n => lev (r.state n)⟩⟩

/-- **The weak limited principle is the decision, of every run, whether its Boolean is
`false` throughout.** -/
theorem wlpo_iff_runs : WLPO ↔ FalseDecided :=
  ⟨fun wlpo _ _ _ reg r => wlpo fun n => reg (r.state n),
   fun decided s => decided Bool Unit _ id (Shown.run s fun _ => ())⟩

/-- **The limited principle is the decision, of every run, whether its Boolean is ever
`true`.** -/
theorem lpo_iff_runs : LPO ↔ TrueDecided :=
  ⟨fun lpo _ _ _ reg r => lpo fun n => reg (r.state n),
   fun decided s => decided Bool Unit _ id (Shown.run s fun _ => ())⟩

/-! ## A whole and no part, decided of every run -/

/-- **A number changed by no condition that still differs exists exactly where it is decided, of
every run, whether its Boolean is `false` throughout.** -/
theorem changedByNoCondition_iff_runs :
    (∃ f : (Nat → Nat) → Nat, ChangedByNoCondition f ∧ ∃ α β, f α ≠ f β) ↔ Nonempty FalseRule :=
  changedByNoCondition_iff_rule.trans falseRule_iff.symm

/-- **A law insensitive at a step to every condition that still differs there exists exactly where
it is decided, of every run, whether its Boolean is `false` throughout.** -/
theorem insensitive_differs_iff_runs :
    (∃ (F : Type) (law : ExchangeLaw F Nat) (t : Nat) (h : F) (l l' : Nat → Nat → Nat) (c : Nat),
      (∀ e, law.InsensitiveAt t h e) ∧
        ¬ (law.take t h l c = law.take t h l' c ∧ law.give t h l c = law.give t h l' c)) ↔
      Nonempty FalseRule :=
  insensitive_differs_iff_rule.trans falseRule_iff.symm

/-- **A counterexample to the least coupling exists exactly where it is decided, of every run,
whether its Boolean is `false` throughout**: a law of what has stood, its conditions numbered
by the natural numbers, with two histories agreeing up to a step on every condition it is
sensitive to that still give differently there. -/
theorem not_through_sensitive_iff_runs :
    (∃ (F : Type) (law : ExchangeLaw F Nat) (t : Nat) (h : F) (l l' : Nat → Nat → Nat) (c : Nat),
      law.Nonanticipating ∧ (∀ e, law.Sensitive h e → ∀ s, s ≤ t → l s e = l' s e) ∧
        ¬ (law.take t h l c = law.take t h l' c ∧ law.give t h l c = law.give t h l' c)) ↔
      Nonempty FalseRule :=
  not_through_sensitive_iff_rule.trans falseRule_iff.symm

section Given

variable {F : Type} {law : ExchangeLaw F Nat} {t : Nat} {h : F}

/-- **A law insensitive at a step to every condition that still differs there decides, of every
run, whether its Boolean is `false` throughout.** -/
theorem insensitive_differs_decides (insensitive : ∀ c, law.InsensitiveAt t h c)
    {l l' : Nat → Nat → Nat} {c : Nat}
    (differs : ¬ (law.take t h l c = law.take t h l' c ∧ law.give t h l c = law.give t h l' c)) :
    FalseDecided :=
  wlpo_iff_runs.mp (wlpo_of_insensitive_differs insensitive differs)

/-- **Every counterexample to the least coupling decides, of every run, whether its
Boolean is `false` throughout.** -/
theorem not_through_sensitive_decides (na : law.Nonanticipating) {l l' : Nat → Nat → Nat}
    (agree : ∀ c, law.Sensitive h c → ∀ s, s ≤ t → l s c = l' s c) {c : Nat}
    (differs : ¬ (law.take t h l c = law.take t h l' c ∧ law.give t h l c = law.give t h l' c)) :
    FalseDecided :=
  wlpo_iff_runs.mp (wlpo_of_not_through_sensitive na agree differs)

end Given

/-! ## Vanishing along a run -/

/-- **Deciding of every run whether its level vanishes from some step on is exactly deciding of
every run whether its Boolean is ever `true`.** -/
theorem vanishRule_iff_trueRule : Nonempty VanishRule ↔ Nonempty TrueRule :=
  vanishRule_iff.trans (vanishDecision_iff_lpoRule.trans trueRule_iff.symm)

/-- **Deciding vanishing of every run gives the limited principle of every run.** -/
theorem vanish_decides (decides : VanishRule) : TrueDecided :=
  lpo_iff_runs.mp (lpo_of_vanish_decided decides.sequences)

/-- **Given both decisions, the levels a map takes along a run are indicated as vanishing or as never
vanishing, exactly one**: the two indicators sum to `1`. -/
theorem indicators_sum (falseRule : FalseRule) (vanishRule : VanishRule) {S A : Type}
    {P : Process S A} (lev : S → Nat) (r : Run P) :
    neverIndicator falseRule.sequences (fun n => lev (r.state n)) +
      vanishIndicator vanishRule.sequences (fun n => lev (r.state n)) = 1 :=
  neverIndicator_add_vanishIndicator _ _ _

end TailRuns

end Becoming
