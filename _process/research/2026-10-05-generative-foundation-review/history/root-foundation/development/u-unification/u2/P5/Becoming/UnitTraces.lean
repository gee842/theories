import Becoming.JoiningBridge

/-!
# Units of the traces of a process

`ExplanatoryLocalUnits` recovers boundary roles from a ternary joining: local units, their
uniqueness under associativity, units carried through a joined product, chain completion, and
units carried along a one-to-one correspondence of joinings. It instantiates them on the admitted
fragments of a process (`ExplanatoryLocalUnits.traceJoin`): a fragment is a trace of the process,
and two fragments join into their concatenation where the first ends where the second begins. The
periphery's associativity and units of that joining carry `propext`; here associativity is proved
with an empty report (`associative`) and the units are the bridge's
(`Joining.trace_has_units_by_core`). This module states the periphery's general laws of the
joining of a process's traces and proves them through those laws.

* **Every trace has exactly one unit on each side** (`units_unique`), and any two assignments of
  units to the traces of a process agree (`boundaries_unique`).
* **A unit of a trace is a unit of what it joins into**, on the left (`left_unit_of_joined`) and
  on the right (`right_unit_of_joined`).
* **A common unit suffices for joining**: two traces of a process join where the unit at the
  finish of the first is the unit at the start of the second (`common_unit_joins`), because the
  joining of traces is chain-complete and that is exactly what chain completion means.
* **A correspondence of traces carrying the joining carries units** (`left_unit_transport`,
  `right_unit_transport`): a one-to-one correspondence between the traces of two processes that
  carries joining exactly carries left and right units.
* **Read through whether a trace takes the step, the one-step process loses chain completion.**
  The traces of `ExplanatoryJoining.budgetProcess`, coded by whether they take its one step
  (`steps`), read through `Joining.image` the periphery's budget joining
  (`budget_reads`). That reading is functional, associative and has local units, and yet two
  composable pairs do not extend to a chain (`budget_not_chain_complete`), while the traces
  themselves are chain-complete (`ExplanatoryLocalUnits.trace_chain_complete`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

universe u v u' v'

namespace UnitTraces

open ExplanatoryLocalUnits ExplanatoryJoining

section Process

variable {S : Type u} {A : Type v}

/-- Concatenating three fragments does not depend on the grouping. -/
theorem merge_assoc (f g h : Fragment S A) : merge f (merge g h) = merge (merge f g) h :=
  congrArg (fun w => (⟨f.start, w, h.finish⟩ : Fragment S A))
    (Joining.appended_assoc f.word g.word h.word).symm

/-- **The joining of the traces of a process is associative**, with an empty axiom report. -/
theorem associative (P : Process S A) : Associative (traceJoin P) := fun a b c _ =>
  ⟨fun ⟨_, ham, hmd⟩ =>
    have jbc : Joint P b.val c.val :=
      ⟨ham.1.2.1, hmd.1.2.1, (congrArg Fragment.finish ham.2).trans hmd.1.2.2⟩
    ⟨⟨merge b.val c.val, joint_merge_valid jbc⟩, ⟨jbc, rfl⟩,
     ⟨ham.1.1, joint_merge_valid jbc, ham.1.2.2⟩,
     (merge_assoc a.val b.val c.val).trans
       ((congrArg (fun f => merge f c.val) ham.2).trans hmd.2)⟩,
   fun ⟨_, hbn, hand⟩ =>
    have jab : Joint P a.val b.val :=
      ⟨hand.1.1, hbn.1.1, hand.1.2.2.trans (congrArg Fragment.start hbn.2).symm⟩
    ⟨⟨merge a.val b.val, joint_merge_valid jab⟩, ⟨jab, rfl⟩,
     ⟨joint_merge_valid jab, hbn.1.2.1, hbn.1.2.2⟩,
     (merge_assoc a.val b.val c.val).symm.trans
       ((congrArg (merge a.val) hbn.2).trans hand.2)⟩⟩

/-- **Every trace of a process has exactly one unit on each side.** -/
theorem units_unique (P : Process S A) (a : Admitted P) :
    (∃ e, LeftUnit (traceJoin P) e a ∧ ∀ f, LeftUnit (traceJoin P) f a → f = e) ∧
    (∃ e, RightUnit (traceJoin P) e a ∧ ∀ f, RightUnit (traceJoin P) f a → f = e) :=
  local_units_exist_uniquely (associative P) (Joining.trace_has_units_by_core P) a

/-- **Any two assignments of units to the traces of a process agree.** -/
theorem boundaries_unique (P : Process S A) (left right left' right' : Admitted P → Admitted P)
    (hl : ∀ a, LeftUnit (traceJoin P) (left a) a) (hr : ∀ a, RightUnit (traceJoin P) (right a) a)
    (hl' : ∀ a, LeftUnit (traceJoin P) (left' a) a)
    (hr' : ∀ a, RightUnit (traceJoin P) (right' a) a) :
    ∀ a, left a = left' a ∧ right a = right' a :=
  boundary_assignments_unique (associative P) left right left' right' hl hr hl' hr'

/-- **A left unit of a trace is a left unit of what it joins into.** -/
theorem left_unit_of_joined {P : Process S A} {a b c e : Admitted P} (joined : traceJoin P a b c)
    (unit : LeftUnit (traceJoin P) e a) : LeftUnit (traceJoin P) e c :=
  left_unit_of_product (associative P) (trace_join_functional P) joined unit

/-- **A right unit of a trace is a right unit of what it is joined into.** -/
theorem right_unit_of_joined {P : Process S A} {a b c e : Admitted P} (joined : traceJoin P a b c)
    (unit : RightUnit (traceJoin P) e b) : RightUnit (traceJoin P) e c :=
  right_unit_of_product (associative P) (trace_join_functional P) joined unit

/-- **A common unit suffices for joining two traces of a process**: the joining of traces is
chain-complete, which is exactly that a common unit suffices. -/
theorem common_unit_joins (P : Process S A) (a b : Admitted P)
    (common : CommonUnit (traceJoin P) a b) : Composable (traceJoin P) a b :=
  (chain_complete_iff_unit_matching_suffices (associative P) (trace_join_functional P)
    (Joining.trace_has_units_by_core P)).mp (trace_chain_complete P) a b common

variable {S' : Type u'} {A' : Type v'}

/-- **A one-to-one correspondence of the traces of two processes that carries joining exactly
carries left units.** -/
theorem left_unit_transport {P : Process S A} {Q : Process S' A'} {f : Admitted P → Admitted Q}
    (one : ∀ a b, f a = f b → a = b) (onto : ∀ b, ∃ a, f a = b)
    (carries : ∀ a b c, traceJoin P a b c ↔ traceJoin Q (f a) (f b) (f c)) (e a : Admitted P) :
    LeftUnit (traceJoin P) e a ↔ LeftUnit (traceJoin Q) (f e) (f a) :=
  ExplanatoryLocalUnits.left_unit_transport one onto carries e a

/-- **A one-to-one correspondence of the traces of two processes that carries joining exactly
carries right units.** -/
theorem right_unit_transport {P : Process S A} {Q : Process S' A'} {f : Admitted P → Admitted Q}
    (one : ∀ a b, f a = f b → a = b) (onto : ∀ b, ∃ a, f a = b)
    (carries : ∀ a b c, traceJoin P a b c ↔ traceJoin Q (f a) (f b) (f c)) (e a : Admitted P) :
    RightUnit (traceJoin P) e a ↔ RightUnit (traceJoin Q) (f e) (f a) :=
  ExplanatoryLocalUnits.right_unit_transport one onto carries e a

end Process

/-! ## The one-step process read through whether a trace takes the step -/

section Budget

/-- Whether a course of moves takes a step. -/
def stepsWord : List Unit → Bool
  | [] => false
  | _ :: _ => true

/-- Whether a trace of `ExplanatoryJoining.budgetProcess` takes its step. -/
def steps (f : Admitted budgetProcess) : Bool := stepsWord f.val.word

/-- A trace of the one-step process is idle or is the one step. -/
theorem trace_cases : ∀ {s t : Bool} {w : List Unit}, Trace budgetProcess s w t →
    (w = [] ∧ s = t) ∨ (w = [()] ∧ s = false ∧ t = true)
  | _, _, _, .nil _ => .inl ⟨rfl, rfl⟩
  | _, _, _, .cons step (.nil _) => .inr ⟨rfl, step.1, step.2⟩
  | _, _, _, .cons step (.cons step' _) => nomatch step.2.symm.trans step'.1

/-- The idle trace at `s`. -/
def idleAt (s : Bool) : Admitted budgetProcess := traceIdle budgetProcess s

/-- The trace of the one step. -/
def stepTrace : Admitted budgetProcess := ⟨spend, spend_valid⟩

/-- The traces of the one-step process read through whether they take the step. -/
def budgetImage : Joining Bool := Joining.image (traceJoin budgetProcess) steps

/-- What the traces of the one-step process join into, read through whether they take the step,
is in the periphery's budget joining. -/
theorem budget_reads_mp {a b c : Bool} : budgetImage a b c → budgetJoin a b c :=
  fun ⟨x, y, z, hx, hy, hz, joined⟩ =>
    have word : z.val.word = x.val.word ++ y.val.word := (congrArg Fragment.word joined.2).symm
    match trace_cases x.property, trace_cases y.property with
    | .inl ⟨wx, _⟩, _ =>
      have ha : false = a := (congrArg stepsWord wx).symm.trans hx
      have hc : b = c :=
        hy.symm.trans ((congrArg (fun w => stepsWord (w ++ y.val.word)) wx).symm.trans
          ((congrArg stepsWord word).symm.trans hz))
      by subst ha; subst hc; exact ⟨.inl rfl, rfl⟩
    | .inr ⟨_, _, _⟩, .inl ⟨wy, _⟩ =>
      have hb : false = b := (congrArg stepsWord wy).symm.trans hy
      have hc : a = c :=
        hx.symm.trans ((congrArg stepsWord (Joining.appended_nil x.val.word)).symm.trans
          ((congrArg (fun w => stepsWord (x.val.word ++ w)) wy).symm.trans
            ((congrArg stepsWord word).symm.trans hz)))
      by
        subst hb; subst hc
        cases a with
        | false => exact ⟨.inl rfl, rfl⟩
        | true => exact ⟨.inr rfl, rfl⟩
    | .inr ⟨_, _, fx⟩, .inr ⟨_, sy, _⟩ =>
      nomatch fx.symm.trans (joined.1.2.2.trans sy)

/-- The periphery's budget joining is what the traces of the one-step process join into, read
through whether they take the step. -/
theorem budget_reads_mpr : ∀ {a b c : Bool}, budgetJoin a b c → budgetImage a b c
  | false, false, _, ⟨_, hc⟩ => by
    subst hc
    exact ⟨idleAt false, idleAt false, idleAt false, rfl, rfl, rfl,
      ⟨idle_valid _ _, idle_valid _ _, rfl⟩, rfl⟩
  | false, true, _, ⟨_, hc⟩ => by
    subst hc
    exact ⟨idleAt false, stepTrace, stepTrace, rfl, rfl, rfl, ⟨idle_valid _ _, spend_valid, rfl⟩, rfl⟩
  | true, false, _, ⟨_, hc⟩ => by
    subst hc
    exact ⟨stepTrace, idleAt true, stepTrace, rfl, rfl, rfl, ⟨spend_valid, idle_valid _ _, rfl⟩, rfl⟩
  | true, true, _, ⟨.inl no, _⟩ => nomatch no
  | true, true, _, ⟨.inr no, _⟩ => nomatch no

/-- **Read through whether a trace takes the step, the joining of the traces of the one-step
process is the periphery's budget joining.** -/
theorem budget_reads (a b c : Bool) : budgetImage a b c ↔ budgetJoin a b c :=
  ⟨budget_reads_mp, budget_reads_mpr⟩

/-- Neutrality carries along relations holding at the same triples. -/
theorem neutral_of_iff {F : Type u} {J K : Join F} (same : ∀ a b c, J a b c ↔ K a b c) {e : F}
    (neutral : Neutral K e) : Neutral J e :=
  ⟨fun a c joined => neutral.1 a c ((same e a c).mp joined),
   fun a c joined => neutral.2 a c ((same a e c).mp joined)⟩

/-- **Read through whether a trace takes the step, the one-step process joins in at most one
way.** -/
theorem budget_functional : Functional budgetImage := fun a b c d first second =>
  ExplanatoryLocalUnits.budget_functional a b c d ((budget_reads a b c).mp first)
    ((budget_reads a b d).mp second)

/-- **Read through whether a trace takes the step, the joining of the one-step process is
associative.** -/
theorem budget_associative : Associative budgetImage := fun a b c d =>
  ⟨fun ⟨m, first, second⟩ =>
    match (ExplanatoryLocalUnits.budget_associative a b c d).mp
        ⟨m, (budget_reads a b m).mp first, (budget_reads m c d).mp second⟩ with
    | ⟨n, first', second'⟩ => ⟨n, (budget_reads b c n).mpr first', (budget_reads a n d).mpr second'⟩,
   fun ⟨n, first, second⟩ =>
    match (ExplanatoryLocalUnits.budget_associative a b c d).mpr
        ⟨n, (budget_reads b c n).mp first, (budget_reads a n d).mp second⟩ with
    | ⟨m, first', second'⟩ => ⟨m, (budget_reads a b m).mpr first', (budget_reads m c d).mpr second'⟩⟩

/-- **Read through whether a trace takes the step, the joining of the one-step process has local
units.** -/
theorem budget_has_units : HasUnits budgetImage :=
  ⟨fun a => match ExplanatoryLocalUnits.budget_has_units.1 a with
    | ⟨e, neutral, joined⟩ =>
      ⟨e, neutral_of_iff budget_reads neutral, (budget_reads e a a).mpr joined⟩,
   fun a => match ExplanatoryLocalUnits.budget_has_units.2 a with
    | ⟨e, neutral, joined⟩ =>
      ⟨e, neutral_of_iff budget_reads neutral, (budget_reads a e a).mpr joined⟩⟩

/-- **Read through whether a trace takes the step, the joining of the one-step process is not
chain-complete**, though the traces themselves are (`ExplanatoryLocalUnits.trace_chain_complete`):
the description loses the chain of two steps. -/
theorem budget_not_chain_complete : ¬ ChainComplete budgetImage := fun complete =>
  ExplanatoryLocalUnits.budget_not_chain_complete fun a b c ⟨m, first⟩ ⟨n, second⟩ =>
    match complete a b c ⟨m, (budget_reads a b m).mpr first⟩ ⟨n, (budget_reads b c n).mpr second⟩ with
    | ⟨m', d, first', second'⟩ =>
      ⟨m', d, (budget_reads a b m').mp first', (budget_reads m' c d).mp second'⟩

end Budget

end UnitTraces

end Becoming
