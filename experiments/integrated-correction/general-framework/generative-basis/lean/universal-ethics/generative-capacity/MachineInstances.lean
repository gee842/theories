import Becoming.Instances
import EncounterChoice
import RetrospectiveBinding
import GoalFormationRevision
import JointPracticeContinuation

/-!
# Constructed machines and histories as instances of the core's laws (periphery)

The definitions of these peripheral machines use standard axioms through their library instances
(membership tests, counting, `Option` binding), so their instances of the core's laws are stated
here rather than in the pure bridge `Becoming.Instances`. The core does not import this module.

* **Reading acquired words.** For every lexicon whose transition record groups the two-word
  encoding (six local bond conditions, `Groups`), interpretation of every encoded sequence is the
  assembly of its atoms exactly when each word form resolves to its atom
  (`interprets_every_iff`, from `Segmentation.reads_every_iff`). The histories `learned 32`,
  `coordinated 37`, `acquired 51` and `retrospective 36` are instances; the fixed decoder of
  `experienced 28` is another (`experienced_parses_every`). The peripheral `bond` is the core's
  majority bond (`bond_eq`), so every transition record bonds each sound to at most one
  successor (`bond_functional`).
* **Readout.** The four-integer summary of the two-qubit fragment carries a law
  (`summary_carries_law`) and is exact after every course of moves (`summary_every_word`), from
  `RelationalReduction.summary_update_exact` and the core's `Readout` laws.
* **Formed goal revision.** For every condition with access loss and kept transition
  maintenance, after acquisition, revision and reform, `n` operations run exactly when `n ≤ 5`;
  each consumes the learning goal and adds no loss, so the earlier loss is retained
  (`revision_continues`). The run of the learning practice from any account `⟨w, q, z⟩` succeeds
  for `n` cycles exactly when `n = 0` or `2 ≤ w` and `2 * (n - q / 2) ≤ w`
  (`cycles_learning_iff`). The `harmful` headline is an instance (`harmful_instance`).
* **Gated change in the practice machine.** Its traces are exactly its completed runs
  (`practice_trace_iff_run`); only revision changes the recorded methods (`methods_kept`) and
  only an organizational adoption changes the rule (`practice_rule_kept`), so courses without
  them keep both (`methods_inherited`, `practice_rule_inherited`).
-/

namespace Becoming.MachineInstances

open Generative Becoming.Assurance

/-! ## Reading acquired words -/

section Reading

open Generative.CompositionalAcquisition Generative.AcquiredSegmentation Generative.AcquiredBinding

/-- The record groups the two-word encoding: `a→b`, `c→d` bonded; `b→a`, `b→c`, `d→a`, `d→c` not. -/
def Groups (log : List (Option Sound)) : Prop :=
  bond log .a .b = true ∧ bond log .c .d = true ∧ bond log .b .a = false ∧
    bond log .b .c = false ∧ bond log .d .a = false ∧ bond log .d .c = false

theorem segments_of_groups {log : List (Option Sound)} (groups : Groups log) (ws : List Bool) :
    chunks (bond log) (encode ws) = ws.map word :=
  (Instances.two_word_iff (bond log)).mpr groups ws

theorem readForms_eq (s : Lexicon) :
    ∀ fs, readForms s fs = Segmentation.readAll (resolve s) fs
  | [] => rfl
  | f :: fs => by
    show (resolve s f).bind (fun e => (readForms s fs).bind fun es => some (e :: es)) = _
    rw [readForms_eq s fs]
    rfl

/-- **Reading acquired words.** For every lexicon whose record groups the two-word encoding,
every encoded sequence is interpreted as the assembly of its atoms exactly when each word form
resolves to its atom. -/
theorem interprets_every_iff (s : Lexicon) (groups : Groups s.percept.log) :
    (∀ ws, interpret s (encode ws) = assembleMessage (ws.map Expr.atom)) ↔
      ∀ b, resolve s (word b) = some (Expr.atom b) := by
  constructor
  · intro every b
    have once := every [b]
    simp only [interpret, segments_of_groups groups, List.map, readForms] at once
    cases hr : resolve s (word b) with
    | none => simp [hr, assembleMessage] at once
    | some e =>
      simp [hr, assembleMessage] at once
      rw [once]
  · intro each ws
    show (readForms s (chunks (bond s.percept.log) (encode ws))).bind assembleMessage = _
    rw [segments_of_groups groups, readForms_eq,
      (Segmentation.readAll_map_iff (resolve s) word Expr.atom ws).mpr (fun w _ => each w)]
    rfl

theorem learned_groups : Groups (learned 32).percept.log := by unfold Groups; decide

/-- `learned 32` as an instance. -/
theorem learned_interprets_every (ws : List Bool) :
    interpret (learned 32) (encode ws) = assembleMessage (ws.map Expr.atom) :=
  (interprets_every_iff _ learned_groups).mpr actual_encounters_acquire_both_bindings ws

theorem coordinated_groups : Groups (EnactedScene.coordinated 37).lexicon.percept.log := by unfold Groups; decide

theorem coordinated_resolves (b : Bool) :
    resolve (EnactedScene.coordinated 37).lexicon (word b) = some (Expr.atom b) := by
  cases b <;> decide

/-- `coordinated 37` as an instance. -/
theorem coordinated_interprets_every (ws : List Bool) :
    interpret (EnactedScene.coordinated 37).lexicon (encode ws) =
      assembleMessage (ws.map Expr.atom) :=
  (interprets_every_iff _ coordinated_groups).mpr coordinated_resolves ws

theorem acquired_groups :
    Groups (EncounterChoice.acquired 51).situation.lexicon.percept.log := by unfold Groups; decide

theorem acquired_resolves (b : Bool) :
    resolve (EncounterChoice.acquired 51).situation.lexicon (word b) = some (Expr.atom b) := by
  cases b <;> decide

/-- `acquired 51` as an instance. -/
theorem acquired_interprets_every (ws : List Bool) :
    interpret (EncounterChoice.acquired 51).situation.lexicon (encode ws) =
      assembleMessage (ws.map Expr.atom) :=
  (interprets_every_iff _ acquired_groups).mpr acquired_resolves ws

theorem retrospective_groups :
    Groups (RetrospectiveBinding.bindingView (RetrospectiveBinding.retrospective 36)
      SourceReliance.allFaults).percept.log := by unfold Groups; decide

/-- `retrospective 36` as an instance. -/
theorem retrospective_interprets_every (ws : List Bool) :
    interpret (RetrospectiveBinding.bindingView (RetrospectiveBinding.retrospective 36)
        SourceReliance.allFaults) (encode ws) = assembleMessage (ws.map Expr.atom) :=
  (interprets_every_iff _ retrospective_groups).mpr
    RetrospectiveBinding.late_calibration_changes_both_bindings ws

theorem experienced_groups : Groups (experienced 28).log := by unfold Groups; decide

/-- The fixed decoder after `experienced 28` as an instance of grouping. -/
theorem experienced_parses_every (ws : List Bool) :
    parse (experienced 28) (encode ws) = assembleMessage (ws.map Expr.atom) := by
  show (decodeChunks (chunks (bond (experienced 28).log) (encode ws))).bind assembleMessage = _
  rw [segments_of_groups experienced_groups, decoded_word_sequence]
  rfl

/-! ### The peripheral bond is the core's majority bond -/

theorem edges_eq : ∀ (x : Option Sound) (rest : List (Option Sound)),
    AcquiredSegmentation.edges (x :: rest) = Segmentation.edges.edgesFrom x rest
  | _, [] => by simp [AcquiredSegmentation.edges, Segmentation.edges.edgesFrom]
  | none, y :: rest => by
    simp [AcquiredSegmentation.edges, Segmentation.edges.edgesFrom, edges_eq y rest]
  | some u, none :: rest => by
    simp [AcquiredSegmentation.edges, Segmentation.edges.edgesFrom, edges_eq none rest]
  | some u, some v :: rest => by
    simp [AcquiredSegmentation.edges, Segmentation.edges.edgesFrom, edges_eq (some v) rest]

theorem edges_all_eq : ∀ log : List (Option Sound),
    AcquiredSegmentation.edges log = Segmentation.edges log
  | [] => by simp [AcquiredSegmentation.edges, Segmentation.edges]
  | x :: rest => (edges_eq x rest).trans rfl

theorem countP_eq {β : Type} (p q : β → Bool) (same : ∀ b, p b = q b) :
    ∀ l : List β, l.countP p = Segmentation.countIf q l
  | [] => rfl
  | b :: bs => by
    rw [List.countP_cons, countP_eq p q same bs, same b]
    simp only [Segmentation.countIf]
    cases q b <;> simp

theorem beq_sound (x y : Sound) : (x == y) = decide (x = y) := by
  cases x <;> cases y <;> rfl

theorem beq_pair (e : Sound × Sound) (x y : Sound) : (e == (x, y)) = decide (e = (x, y)) := by
  obtain ⟨e₁, e₂⟩ := e
  cases e₁ <;> cases e₂ <;> cases x <;> cases y <;> rfl

/-- **The peripheral bond is the core's majority bond.** -/
theorem bond_eq (log : List (Option Sound)) (x y : Sound) :
    AcquiredSegmentation.bond log x y = Segmentation.bond log x y := by
  have departing : AcquiredSegmentation.departures log x = Segmentation.departures log x := by
    unfold AcquiredSegmentation.departures Segmentation.departures
    rw [edges_all_eq]
    exact countP_eq _ _ (fun (e : Sound × Sound) => beq_sound e.1 x) _
  have moving : AcquiredSegmentation.edgeCount log x y = Segmentation.transitions log x y := by
    unfold AcquiredSegmentation.edgeCount List.count Segmentation.transitions
    rw [edges_all_eq]
    exact countP_eq _ _ (fun (e : Sound × Sound) => beq_pair e x y) _
  unfold AcquiredSegmentation.bond Segmentation.bond
  rw [departing, moving]

/-- **Every transition record bonds each sound to at most one successor.** -/
theorem bond_functional (log : List (Option Sound)) {x y z : Sound}
    (toY : AcquiredSegmentation.bond log x y = true)
    (toZ : AcquiredSegmentation.bond log x z = true) : y = z :=
  Segmentation.bond_unique log ((bond_eq log x y) ▸ toY) ((bond_eq log x z) ▸ toZ)

end Reading

/-! ## Readout -/

section Quantum

open Generative.OperativeCoherence Generative.RelationalReduction

/-- **The summary with the joint cross term carries a law of the fragment.** -/
theorem summary_carries_law :
    ∃ Q : Process Summary Event, Determined Q ∧
      FactorsThrough (ofMap RelationalReduction.next) summarize Q :=
  (Readout.law_through_iff RelationalReduction.next summarize).mpr fun s s' a same =>
    (summary_update_exact s a).trans
      ((congrArg (reducedNext · a) same).trans (summary_update_exact s' a).symm)

/-- **After every course of moves, the summary is the reduced law's course.** -/
theorem summary_every_word (v : Joint) (word : List Event) :
    summarize (word.foldl RelationalReduction.next v) = word.foldl reducedNext (summarize v) :=
  Readout.foldl_semiconj RelationalReduction.next summarize reducedNext summary_update_exact word v

end Quantum

/-! ## Formed goal revision -/

section Revision

open GoalFormationRevision

/-- One cycle of a practice under a selector, from an account. -/
theorem cycle_eq (r : Selection) (p : Practice) (w q z : Nat) :
    cycle r p ⟨w, q, z⟩ =
      if 2 ≤ w then
        some (if feedback r p = 2 ∧ 2 ≤ q then ⟨w, q - 2, z + 2⟩ else ⟨w - 2, q, z + 2⟩)
      else none := by
  unfold cycle charge
  by_cases hw : 2 ≤ w
  · by_cases hf : feedback r p = 2 ∧ 2 ≤ q
    · simp [hw, hf]
    · rw [if_pos hw, if_pos hw, if_neg hf]
      show (if feedback r p = 2 ∧ 2 ≤ q then _ else _) = _
      rw [if_neg hf]
      rfl
  · rw [if_neg hw, if_neg hw]
    rfl

/-- **A practice runs `n` cycles from `⟨w, q, z⟩` exactly when `n = 0`, or `2 ≤ w` and the work
covers the cycles the reserve does not support**: twice `n` less the supported cycles (`q / 2`
where the selector feeds the practice back, none otherwise) is at most `w`. -/
theorem cycles_iff (r : Selection) (p : Practice) : ∀ (n w q z : Nat),
    (cycles r p n ⟨w, q, z⟩).isSome = true ↔
      n = 0 ∨ (2 ≤ w ∧ 2 * (n - (if feedback r p = 2 then q / 2 else 0)) ≤ w)
  | 0, _, _, _ => ⟨fun _ => Or.inl rfl, fun _ => rfl⟩
  | n + 1, w, q, z => by
    have unfolds : cycles r p (n + 1) ⟨w, q, z⟩ = (cycle r p ⟨w, q, z⟩).bind (cycles r p n) := rfl
    rw [unfolds, cycle_eq]
    by_cases hw : 2 ≤ w
    · rw [if_pos hw]
      by_cases hf : feedback r p = 2 ∧ 2 ≤ q
      · rw [if_pos hf]
        change (cycles r p n ⟨w, q - 2, z + 2⟩).isSome = true ↔ _
        rw [cycles_iff r p n w (q - 2) (z + 2)]
        simp only [if_pos hf.1]
        have := hf.2
        constructor <;> intro h <;> omega
      · rw [if_neg hf]
        change (cycles r p n ⟨w - 2, q, z + 2⟩).isSome = true ↔ _
        rw [cycles_iff r p n (w - 2) q (z + 2)]
        by_cases hfb : feedback r p = 2
        · have hq : q < 2 := Nat.lt_of_not_le fun hq => hf ⟨hfb, hq⟩
          simp only [if_pos hfb]
          constructor <;> intro h <;> omega
        · simp only [if_neg hfb]
          constructor <;> intro h <;> omega
    · rw [if_neg hw]
      constructor
      · intro h
        exact nomatch h
      · intro h
        exfalso
        omega

/-- The learning practice under the learning selector. -/
theorem cycles_learning_iff (n w q z : Nat) :
    (cycles .learning .learning n ⟨w, q, z⟩).isSome = true ↔
      n = 0 ∨ (2 ≤ w ∧ 2 * (n - q / 2) ≤ w) := by
  have fed : feedback .learning .learning = 2 := rfl
  rw [cycles_iff, if_pos fed]

/-- The learning practice under the attendance selector: no reserve support. -/
theorem cycles_unselected_iff (n w q z : Nat) :
    (cycles .attendance .learning n ⟨w, q, z⟩).isSome = true ↔ 2 * n ≤ w := by
  have unfed : feedback .attendance .learning ≠ 2 := fun same => nomatch same
  rw [cycles_iff, if_neg unfed]
  constructor <;> intro h <;> omega

/-- The loss a learning operation adds: one where transition maintenance is lost. -/
def lossPer (c : GoalFormationRevision.Conditions) : Nat := if c.transitionLoss = true then 1 else 0

theorem learning_loss (c : GoalFormationRevision.Conditions) :
    (if ((perform c .learning).access && (perform c .learning).maintenance) = true then 0 else 1) =
      lossPer c := by
  obtain ⟨a, t, r⟩ := c
  cases t <;> rfl

/-- The record a learning operation appends. -/
def learningRecord (c : GoalFormationRevision.Conditions) (r : Selection) : Record :=
  ⟨.learning, perform c .learning, feedback r .learning⟩

/-- **Operating the learning goal**, for every condition, state and number of operations: every
operation consumes the learning goal, keeps the selector, adds the transition loss if any and
appends one record; the operations run exactly as the account's cycles. -/
theorem operateMany_learning (c : GoalFormationRevision.Conditions) :
    ∀ (n : Nat) (s : State), s.goal = some .learning →
      ((operateMany c n s).isSome = (cycles s.selector .learning n s.account).isSome) ∧
      ∀ t, operateMany c n s = some t →
        t.goal = s.goal ∧ t.selector = s.selector ∧ t.losses = s.losses + n * lossPer c ∧
          t.archive.length = s.archive.length + n
  | 0, s, _ => by
    refine ⟨rfl, fun t ran => ?_⟩
    have same : s = t := Option.some.inj ran
    subst same
    exact ⟨rfl, rfl, by rw [Nat.zero_mul, Nat.add_zero], (Nat.add_zero _).symm⟩
  | n + 1, s, goal => by
    have step : operate c s = (cycle s.selector .learning s.account).bind (fun a => some
        { s with account := a, archive := s.archive ++ [learningRecord c s.selector],
                 losses := s.losses + (if ((perform c .learning).access &&
                   (perform c .learning).maintenance) = true then 0 else 1) }) := by
      unfold operate
      rw [goal]
      rfl
    have unfoldOps : operateMany c (n + 1) s = (operate c s).bind (operateMany c n) := rfl
    have unfoldCycles : cycles s.selector .learning (n + 1) s.account =
        (cycle s.selector .learning s.account).bind (cycles s.selector .learning n) := rfl
    rw [unfoldOps, unfoldCycles, step]
    cases hc : cycle s.selector .learning s.account with
    | none => exact ⟨rfl, fun t ran => absurd ran (fun h => nomatch h)⟩
    | some a =>
      have ih := operateMany_learning c n
        { s with account := a, archive := s.archive ++ [learningRecord c s.selector],
                 losses := s.losses + (if ((perform c .learning).access &&
                   (perform c .learning).maintenance) = true then 0 else 1) } goal
      refine ⟨ih.1, fun t ran => ?_⟩
      obtain ⟨g, sel, los, len⟩ := ih.2 t ran
      refine ⟨g, sel, ?_, ?_⟩
      · rw [los]
        show s.losses + (if ((perform c .learning).access &&
          (perform c .learning).maintenance) = true then 0 else 1) + n * lossPer c = _
        rw [learning_loss, Nat.succ_mul]
        omega
      · rw [len]
        show (s.archive ++ [learningRecord c s.selector]).length + n = _
        rw [List.length_append]
        show s.archive.length + 1 + n = _
        omega

/-- **Revision happens exactly under access loss with kept transition maintenance**: acquisition,
revision and reform complete for exactly these conditions. -/
theorem completed_isSome_iff (c : GoalFormationRevision.Conditions) :
    (completed c).isSome = true ↔ c.accessLoss = true ∧ c.transitionLoss = false := by
  obtain ⟨a, t, r⟩ := c
  cases a <;> cases t <;> cases r <;> decide

/-- After revision, every condition with access loss and kept maintenance holds the learning goal
under the attendance selector with one loss, the account `⟨5, 8, 5⟩` and two records; reform
moves the selector to learning at the account `⟨3, 8, 7⟩`. -/
theorem revised_class (c : GoalFormationRevision.Conditions) :
    c.accessLoss = true → c.transitionLoss = false →
      (revised c).map (fun s => (s.goal, s.selector, s.losses, s.account, s.archive.length)) =
        some (some .learning, .attendance, 1, ⟨5, 8, 5⟩, 2) ∧
      (completed c).map (fun s => (s.goal, s.selector, s.losses, s.account, s.archive.length)) =
        some (some .learning, .learning, 1, ⟨3, 8, 7⟩, 2) := by
  obtain ⟨a, t, r⟩ := c
  cases a <;> cases t <;> cases r <;> decide

/-- The fields of a state read off a class equation. -/
theorem fields_of {o : Option State} {g : Option Goal} {r : Selection} {l : Nat} {acc : Account}
    {k : Nat}
    (known : o.map (fun s => (s.goal, s.selector, s.losses, s.account, s.archive.length)) =
      some (g, r, l, acc, k)) :
    ∃ s, o = some s ∧ s.goal = g ∧ s.selector = r ∧ s.losses = l ∧ s.account = acc ∧
      s.archive.length = k := by
  cases o with
  | none => exact absurd known (fun h => nomatch h)
  | some s =>
    have fields := Option.some.inj known
    simp only [Prod.mk.injEq] at fields
    obtain ⟨g', r', l', a', k'⟩ := fields
    exact ⟨s, rfl, g', r', l', a', k'⟩

/-- **Formed goal revision continues, for every condition with access loss and kept transition
maintenance and every number of operations.** After acquisition, revision and reform, `n`
operations run exactly when `n ≤ 5`; each consumes the learning goal and adds no loss, so the
earlier loss is retained. Without reform, the unchanged selector supports none of them, and `n`
operations run exactly when `n ≤ 2`. -/
theorem revision_continues (c : GoalFormationRevision.Conditions) (harm : c.accessLoss = true)
    (retain : c.transitionLoss = false) (n : Nat) :
    ((completed c >>= operateMany c n).isSome = true ↔ n ≤ 5) ∧
      (∀ t, (completed c >>= operateMany c n) = some t →
        t.goal = some .learning ∧ t.losses = 1 ∧ t.archive.length = 2 + n) ∧
      ((revised c >>= operateMany c n).isSome = true ↔ n ≤ 2) := by
  have none_lost : lossPer c = 0 := by
    unfold lossPer
    rw [retain]
    rfl
  obtain ⟨s, hs, goal, sel, los, acc, len⟩ := fields_of (revised_class c harm retain).2
  obtain ⟨u, hu, goalU, selU, _, accU, _⟩ := fields_of (revised_class c harm retain).1
  rw [hs, hu]
  have laws := operateMany_learning c n s goal
  have lawsU := operateMany_learning c n u goalU
  refine ⟨?_, fun t ran => ?_, ?_⟩
  · show (operateMany c n s).isSome = true ↔ _
    rw [laws.1, sel, acc, cycles_learning_iff]
    constructor <;> intro h <;> omega
  · obtain ⟨g, _, l, a⟩ := laws.2 t ran
    refine ⟨g.trans goal, ?_, ?_⟩
    · rw [l, los, none_lost, Nat.mul_zero]
    · rw [a, len, Nat.add_comm]
  · show (operateMany c n u).isSome = true ↔ _
    rw [lawsU.1, selU, accU, cycles_unselected_iff]
    constructor <;> intro h <;> omega

/-- **The `harmful` headline as an instance** (`joined_revision_has_warrant_and_actual_continuation`). -/
theorem harmful_instance :
    PracticalJudgment.Better (protects harmful) (gains harmful) .learning .attendance ∧
    (acquire harmful .attendance).map State.goal = some (some .attendance) ∧
    (completed harmful >>= operateMany harmful 5).map State.goal = some (some .learning) ∧
    (completed harmful >>= operateMany harmful 5).map State.losses = some 1 := by
  have law := revision_continues harmful rfl rfl 5
  have runs := law.1.mpr (Nat.le_refl 5)
  cases hr : (completed harmful >>= operateMany harmful 5) with
  | none => rw [hr] at runs; exact absurd runs (fun h => nomatch h)
  | some t =>
    obtain ⟨g, l, _⟩ := law.2.1 t hr
    exact ⟨warranted_revision harmful rfl rfl,
      (goal_depends_on_actual_formative_rule harmful).1,
      congrArg some g, congrArg some l⟩

/-- `reform_does_not_make_support_infinite` and `unchanged_selection_exhausts_revised_practice`
as instances. -/
theorem harmful_bounds :
    (completed harmful >>= operateMany harmful 6) = none ∧
      (revised harmful >>= operateMany harmful 3) = none := by
  have law6 := revision_continues harmful rfl rfl 6
  have law3 := revision_continues harmful rfl rfl 3
  constructor
  · cases h : (completed harmful >>= operateMany harmful 6) with
    | none => rfl
    | some t => exact absurd (law6.1.mp (by rw [h]; rfl)) (by decide)
  · cases h : (revised harmful >>= operateMany harmful 3) with
    | none => rfl
    | some t => exact absurd (law3.2.2.mp (by rw [h]; rfl)) (by decide)

end Revision

/-! ## Gated change in the practice machine -/

section Practice

open JointPracticeContinuation

/-- The gate on methods: revision. -/
def revises : Event → Bool
  | .revise => true
  | _ => false

/-- The gate on the rule: an organizational adoption. -/
def adoptsRule : Event → Bool
  | .organizational (.adopt _) => true
  | _ => false

theorem practice_process_eq : JointPracticeContinuation.process = ofPartial step := rfl

theorem practice_run_eq : ∀ (s : State) (es : List Event), run s es = runPartial step s es
  | _, [] => rfl
  | s, e :: es => by
    show (step s e).bind (fun t => run t es) = (step s e).bind (fun t => runPartial step t es)
    cases step s e with
    | none => rfl
    | some t => exact practice_run_eq t es

/-- **The traces of the practice machine are exactly its completed runs.** -/
theorem practice_trace_iff_run {s t : State} {es : List Event} :
    Trace JointPracticeContinuation.process s es t ↔ run s es = some t :=
  (trace_ofPartial_iff step).trans
    ⟨fun ran => (practice_run_eq s es).trans ran, fun ran => (practice_run_eq s es).symm.trans ran⟩

/-- **Only revision changes the recorded methods.** -/
theorem methods_kept : Gated.KeptBy JointPracticeContinuation.process revises State.methods := by
  intro s e t step gated
  change JointPracticeContinuation.step s e = some t at step
  cases e with
  | attempt w x =>
    simp only [JointPracticeContinuation.step] at step
    split at step <;> simp_all
    subst step; rfl
  | respond r =>
    simp only [JointPracticeContinuation.step] at step
    split at step
    · simp at step
    · split at step <;> simp_all
      subst step; rfl
  | revise => simp [revises] at gated
  | retry =>
    simp only [JointPracticeContinuation.step] at step
    split at step
    · simp at step
    · split at step
      · obtain ⟨org, _, rfl⟩ := Option.map_eq_some_iff.mp step
        rfl
      · simp at step
  | organizational e =>
    cases e with
    | review _ _ => simp [JointPracticeContinuation.step] at step
    | _ =>
      simp only [JointPracticeContinuation.step] at step
      obtain ⟨org, _, rfl⟩ := Option.map_eq_some_iff.mp step
      rfl
  | changeContext c =>
    simp only [JointPracticeContinuation.step, Option.some.injEq] at step
    subst step; rfl

/-- **Every course without revision keeps the recorded methods.** -/
theorem methods_inherited {s t : State} {es : List Event}
    (path : Trace JointPracticeContinuation.process s es t)
    (none_revise : ∀ e, e ∈ es → revises e = false) : t.methods = s.methods :=
  Gated.kept_along methods_kept path none_revise

/-- **Only an organizational adoption changes the rule.** -/
theorem practice_rule_kept :
    Gated.KeptBy JointPracticeContinuation.process adoptsRule (fun s => s.org.rule) := by
  intro s e t step gated
  change JointPracticeContinuation.step s e = some t at step
  cases e with
  | attempt w x =>
    simp only [JointPracticeContinuation.step] at step
    split at step <;> simp_all
    subst step; rfl
  | respond r =>
    simp only [JointPracticeContinuation.step] at step
    split at step
    · simp at step
    · split at step <;> simp_all
      subst step; rfl
  | revise =>
    simp only [JointPracticeContinuation.step] at step
    split at step
    · simp at step
    · split at step <;> simp_all
      subst step; rfl
  | retry =>
    simp only [JointPracticeContinuation.step] at step
    split at step
    · simp at step
    · split at step
      · obtain ⟨org, moved, rfl⟩ := Option.map_eq_some_iff.mp step
        exact Instances.rule_kept _ _ _ moved rfl
      · simp at step
  | organizational e =>
    cases e with
    | review _ _ => simp [JointPracticeContinuation.step] at step
    | adopt _ => simp [adoptsRule] at gated
    | enroll c b =>
      simp only [JointPracticeContinuation.step] at step
      obtain ⟨org, moved, rfl⟩ := Option.map_eq_some_iff.mp step
      exact Instances.rule_kept _ _ _ moved rfl
    | propose c p =>
      simp only [JointPracticeContinuation.step] at step
      obtain ⟨org, moved, rfl⟩ := Option.map_eq_some_iff.mp step
      exact Instances.rule_kept _ _ _ moved rfl
    | integrate b =>
      simp only [JointPracticeContinuation.step] at step
      obtain ⟨org, moved, rfl⟩ := Option.map_eq_some_iff.mp step
      exact Instances.rule_kept _ _ _ moved rfl
    | handoff cs =>
      simp only [JointPracticeContinuation.step] at step
      obtain ⟨org, moved, rfl⟩ := Option.map_eq_some_iff.mp step
      exact Instances.rule_kept _ _ _ moved rfl
  | changeContext c =>
    simp only [JointPracticeContinuation.step, Option.some.injEq] at step
    subst step; rfl

/-- **Every course without an organizational adoption keeps the rule.** -/
theorem practice_rule_inherited {s t : State} {es : List Event}
    (path : Trace JointPracticeContinuation.process s es t)
    (none_adopt : ∀ e, e ∈ es → adoptsRule e = false) : t.org.rule = s.org.rule :=
  Gated.kept_along practice_rule_kept path none_adopt

/-- The complete practice history as an instance: one trace, and the run it completes. -/
theorem complete_history_instance :
    Trace JointPracticeContinuation.process initial
      (firstHistory ++ secondHistory ++ continuationHistory) continued :=
  practice_trace_iff_run.mpr (by decide)

end Practice

end Becoming.MachineInstances
