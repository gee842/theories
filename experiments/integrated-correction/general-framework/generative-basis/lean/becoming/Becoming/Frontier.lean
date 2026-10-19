import Becoming.Lexical

/-!
# The frontier of a comparison, what it requires, and how a task is handed on

The frontier of a comparison among eligible alternatives is the eligible alternatives no eligible
one betters (`Frontier`). A task is required of a set of admissible alternatives where some is
admissible and every admissible one performs it (`Required`): a nonempty set, so an impossible
menu requires nothing. Which comparison bounds the frontier is supplied: under `BasicPriority`
(J1/J2 as a condition, `Becoming.Lexical`) it is the frontier of the lexical order
(`BasicPriority.frontier_iff`), and with no condition nothing here asserts a comparison.

Ported from `PracticalJudgment` (frontier, requirement, assignment, succession and discharge),
`RelationalOrganization` and `AlignmentDirection` (F3J, 18 October 2026), with the bridge's
constructive readings of them (`Judgment.frontier_exists`, `Judgment.required_of_bettered`),
stated on the core's types. `PracticalJudgment.Robust` is the core's `CommonResponse` of a
judgment (`commonResponse_judge_iff`, `commonResponse_antitone`) and is not restated. No premise
enters beyond what each theorem names; every declaration has an empty axiom report.

* **The frontier.** A bettered eligible alternative is off the frontier (`Frontier.excluded`). On
  an exact listed menu the frontier is the undominated members (`frontier_iff_undominated`), so
  a nonempty listed menu has a frontier member where the comparison is irreflexive, transitive
  and weakly decided on it (`frontier_exists`, from `exists_undominated` of
  `Becoming.Decidedness`); the periphery's `finite_frontier` proved it classically.
* **Requirement.** A required task is performed by any admissible alternative
  (`Required.performed`); one admissible alternative lacking it defeats the requirement
  (`Required.defeated`); an empty menu requires nothing (`Required.impossible`); what every
  admissible alternative performing a requirement performs is required (`Required.means`); and a
  requirement survives a faithful redescription of the alternatives (`Required.redescribed`).
  What every eligible alternative lacking is bettered in is required of the frontier of a
  nonempty listed menu, where the comparison is irreflexive, transitive and weakly decided and the
  task decided (`required_of_bettered`).
* **Assignment and succession.** A unique responder in every admissible joint plan is required
  (`Assigned.unique_required`) and feasible (`Assigned.capable`). A demand is served where every
  demanded step is served by the old support or the successor (`Served`): withdrawing the old
  support at a demanded step needs the successor there (`Served.successor`), a handover with
  no gap in demand serves it (`served_of_handover`), and an unserved demanded step refutes it
  (`Served.not_of_gap`). A settled undertaking leaves no residual (`Settled.no_residual`); an
  unfulfilled, unreleased one remains (`residual_of_unfulfilled`).
* **Witnesses.** Formation of a shared support: the two working routes are exactly the frontier
  of the lexical order, formation is required and neither route is (`Formation.required`,
  `Formation.frontier_iff`, `Formation.no_route_required`), overbuilding defeats its own basis
  (`Formation.overbuilding`), and a report of whether a connection was built cannot judge the
  basis (`Formation.no_report_judge`). Plans of service: transfer is above keeping, keeping above
  expansion, so expansion is off the frontier (`Handover.expansion_excluded`), and a successor
  serves the demand after the old model stops (`Handover.served`). A collective task can be
  required with no individual one (`Collective.required`); a plan common to every world can be
  missing while each world has one (`Collective.no_common_plan`). Under every classification of
  the fresh contents a formed route is required, decided classification by classification
  (`Routes.required`), while no route is on the frontier under every classification
  (`Routes.none_robust`).

Direction as in `PracticalJudgment`: `better a b` says `a` is better.

The formation witness as steps of a process and on its frame (`Requirement.Formation.draw`,
`Requirement.Formation.frame` and their laws) and `Requirement.Required.through_summary` are in
`Becoming.FrontierFrames`, which states the commitments on a frame, so this module does not import
the frame (board item W).
-/

namespace Becoming

open Lexical

namespace Requirement

section Frontier

variable {H : Type}

/-- The eligible alternatives no eligible alternative betters. -/
def Frontier (eligible : H → Prop) (better : H → H → Prop) (a : H) : Prop :=
  eligible a ∧ ∀ b, eligible b → ¬ better b a

/-- A task performed by every admissible alternative, some alternative being admissible. -/
def Required (admissible : H → Prop) (task : H → Prop) : Prop :=
  (∃ a, admissible a) ∧ ∀ a, admissible a → task a

variable {eligible : H → Prop} {better : H → H → Prop}

theorem Frontier.excluded {a b : H} (eligibleB : eligible b) (beats : better b a) :
    ¬ Frontier eligible better a :=
  fun frontier => frontier.2 b eligibleB beats

/-- On an exact listed menu, the frontier is the undominated members. -/
theorem frontier_iff_undominated {menu : List H} (exact : ∀ a, eligible a ↔ a ∈ menu) {a : H} :
    Frontier eligible better a ↔ Undominated menu better a :=
  ⟨fun ⟨admitted, unbeaten⟩ =>
    ⟨(exact a).mp admitted, fun b mem => unbeaten b ((exact b).mpr mem)⟩,
   fun ⟨mem, unbeaten⟩ =>
    ⟨(exact a).mpr mem, fun b admitted => unbeaten b ((exact b).mp admitted)⟩⟩

/-- **The frontier of a nonempty listed menu is not empty** where the comparison is irreflexive,
transitive and weakly decided on it. -/
theorem frontier_exists (x : H) (rest : List H) (exact : ∀ a, eligible a ↔ a ∈ x :: rest)
    (weakly : ∀ a b, eligible a → eligible b → WeaklyDecided (better a b))
    (irreflexive : ∀ a, ¬ better a a)
    (transitive : ∀ {a b c}, better a b → better b c → better a c) :
    ∃ a, Frontier eligible better a :=
  match exists_undominated x rest (fun a b ma mb => weakly a b ((exact a).mpr ma) ((exact b).mpr mb))
      (fun a _ => irreflexive a) (fun _ _ _ _ _ _ first second => transitive first second) with
  | ⟨a, undominated⟩ => ⟨a, (frontier_iff_undominated exact).mpr undominated⟩

variable {admissible task : H → Prop}

theorem Required.performed (required : Required admissible task) {a : H} (chosen : admissible a) :
    task a :=
  required.2 a chosen

/-- One admissible alternative lacking the task defeats its requirement. -/
theorem Required.defeated {a : H} (admitted : admissible a) (lacking : ¬ task a) :
    ¬ Required admissible task :=
  fun required => lacking (required.2 a admitted)

/-- An empty menu requires nothing. -/
theorem Required.impossible (empty : ∀ a, ¬ admissible a) : ¬ Required admissible task :=
  fun required => match required.1 with
    | ⟨a, admitted⟩ => empty a admitted

/-- What every admissible alternative performing a requirement performs is required. -/
theorem Required.means {means : H → Prop} (required : Required admissible task)
    (law : ∀ a, admissible a → task a → means a) : Required admissible means :=
  ⟨required.1, fun a admitted => law a admitted (required.2 a admitted)⟩

/-- A requirement survives a faithful redescription of the alternatives: every admissible
alternative maps to an admissible one, every admissible one is covered, and the task keeps its
meaning. -/
theorem Required.redescribed {K : Type} {admissible' task' : K → Prop} (f : H → K)
    (forward : ∀ a, admissible a → admissible' (f a))
    (cover : ∀ b, admissible' b → ∃ a, admissible a ∧ f a = b)
    (meaning : ∀ a, task a ↔ task' (f a)) (required : Required admissible task) :
    Required admissible' task' :=
  ⟨match required.1 with
    | ⟨a, admitted⟩ => ⟨f a, forward a admitted⟩,
   fun b admitted => match cover b admitted with
    | ⟨a, admittedA, same⟩ => same ▸ (meaning a).mp (required.2 a admittedA)⟩

/-- **What every eligible alternative lacking it is bettered in is required of the frontier** of a
nonempty listed menu, with the comparison irreflexive, transitive and weakly decided and the task
decided on it. -/
theorem required_of_bettered (x : H) (rest : List H) (exact : ∀ a, eligible a ↔ a ∈ x :: rest)
    (weakly : ∀ a b, eligible a → eligible b → WeaklyDecided (better a b))
    (irreflexive : ∀ a, ¬ better a a)
    (transitive : ∀ {a b c}, better a b → better b c → better a c)
    (decided : ∀ a, eligible a → Decided (task a))
    (bettered : ∀ a, eligible a → ¬ task a → ∃ b, eligible b ∧ better b a) :
    Required (Frontier eligible better) task :=
  ⟨frontier_exists x rest exact weakly irreflexive transitive,
   fun a frontier => undominated_has (menu := x :: rest) (better := better)
     (fun a mem => decided a ((exact a).mpr mem))
     (fun a mem fails => match bettered a ((exact a).mpr mem) fails with
       | ⟨b, admitted, beats⟩ => ⟨b, (exact b).mp admitted, beats⟩)
     a ((frontier_iff_undominated exact).mp frontier)⟩

variable {C G : Type} {basic : H → C → Prop} {gain : H → G → Prop}

/-- **Under `BasicPriority` the frontier is that of the lexical order.** -/
theorem _root_.Becoming.Lexical.BasicPriority.frontier_iff (priority : BasicPriority basic gain better) {a : H} :
    Frontier eligible better a ↔ Frontier eligible (Lexical.Above basic gain) a :=
  ⟨fun ⟨admitted, unbeaten⟩ =>
    ⟨admitted, fun b other above => unbeaten b other ((priority.iff b a).mpr above)⟩,
   fun ⟨admitted, unbeaten⟩ =>
    ⟨admitted, fun b other beats => unbeaten b other ((priority.iff b a).mp beats)⟩⟩

/-- Under `BasicPriority` what is required of the frontier is what is required of the lexical
frontier. -/
theorem _root_.Becoming.Lexical.BasicPriority.required_iff (priority : BasicPriority basic gain better) :
    Required (Frontier eligible better) task ↔
      Required (Frontier eligible (Lexical.Above basic gain)) task :=
  ⟨fun ⟨⟨a, frontier⟩, all⟩ => ⟨⟨a, (priority.frontier_iff).mp frontier⟩,
     fun b frontier => all b ((priority.frontier_iff).mpr frontier)⟩,
   fun ⟨⟨a, frontier⟩, all⟩ => ⟨⟨a, (priority.frontier_iff).mpr frontier⟩,
     fun b frontier => all b ((priority.frontier_iff).mp frontier)⟩⟩

end Frontier

/-! ## Assignment, succession and discharge -/

section Assignment

variable {P A T : Type}

/-- In plan `p`, responder `a` takes task `t`. Assignment is part of a joint plan, not read off
causation. -/
def Assigned (allocation : P → T → A → Prop) (p : P) (a : A) (t : T) : Prop := allocation p t a

/-- **A unique responder in every admissible plan is required.** -/
theorem Assigned.unique_required {admissible : P → Prop} {allocation : P → T → A → Prop} {a : A}
    {t : T} (inhabited : ∃ p, admissible p) (coverage : ∀ p, admissible p → ∃ b, allocation p t b)
    (unique : ∀ p b, admissible p → allocation p t b → b = a) :
    Required admissible (fun p => Assigned allocation p a t) :=
  ⟨inhabited, fun p admitted => match coverage p admitted with
    | ⟨b, held⟩ => unique p b admitted held ▸ held⟩

/-- An assignment in an admissible plan is feasible where every admissible plan's assignments are. -/
theorem Assigned.capable {admissible : P → Prop} {allocation : P → T → A → Prop}
    {capable : P → A → T → Prop}
    (feasible : ∀ p a t, admissible p → allocation p t a → capable p a t) {p : P} {a : A} {t : T}
    (admitted : admissible p) (assigned : Assigned allocation p a t) : capable p a t :=
  feasible p a t admitted assigned

/-- Every demanded step is served by the old support or the successor. Service is indexed by
demand: no provider where nothing is demanded is no failure. -/
def Served (demand old successor : Nat → Prop) : Prop :=
  ∀ t, demand t → old t ∨ successor t

variable {demand old next : Nat → Prop}

/-- Withdrawing the old support at a demanded step needs the successor there. -/
theorem Served.successor (served : Served demand old next) {t : Nat} (needed : demand t)
    (withdrawn : ¬ old t) : next t :=
  match served t needed with
  | .inl kept => absurd kept withdrawn
  | .inr taken => taken

/-- **A handover with no gap in demand serves it**: the old support serves before the handover, the
successor from it on. -/
theorem served_of_handover (handover : Nat) (before : ∀ t, t < handover → demand t → old t)
    (after : ∀ t, handover ≤ t → demand t → next t) : Served demand old next :=
  fun t needed => match Nat.lt_or_ge t handover with
  | .inl early => .inl (before t early needed)
  | .inr late => .inr (after t late needed)

/-- An unserved demanded step refutes service. -/
theorem Served.not_of_gap {t : Nat} (needed : demand t) (withdrawn : ¬ old t)
    (missing : ¬ next t) : ¬ Served demand old next :=
  fun served => missing (served.successor needed withdrawn)

variable {T : Type}

/-- Every due undertaking is done or released. -/
def Settled (due done released : T → Prop) : Prop :=
  ∀ t, due t → done t ∨ released t

/-- A due undertaking neither done nor released. -/
def Residual (due done released : T → Prop) (t : T) : Prop :=
  due t ∧ ¬ done t ∧ ¬ released t

theorem Settled.no_residual {due done released : T → Prop} (settled : Settled due done released)
    (t : T) : ¬ Residual due done released t :=
  fun ⟨isDue, notDone, notReleased⟩ => match settled t isDue with
    | .inl yes => notDone yes
    | .inr yes => notReleased yes

theorem residual_of_unfulfilled {due done released : T → Prop} {t : T} (isDue : due t)
    (notDone : ¬ done t) (notReleased : ¬ released t) : Residual due done released t :=
  ⟨isDue, notDone, notReleased⟩

/-- Separate capacities for one unit each do not give joint capacity for two. -/
theorem separate_not_joint : (1 ≤ 1 ∧ 1 ≤ 1) ∧ ¬ (1 + 1 ≤ (1 : Nat)) :=
  ⟨⟨Nat.le_refl 1, Nat.le_refl 1⟩, Nat.not_succ_le_self 1⟩

end Assignment

/-! ## Witnesses -/

/-- A decidable proposition is decided. -/
theorem decided_of_decidable (p : Prop) [inst : Decidable p] : Decided p :=
  match inst with
  | isTrue yes => .inl yes
  | isFalse no => .inr no

/-- Inclusion of claims indexed by `Bool` is decided where each claim is. -/
theorem decided_included_bool {a b : Bool → Prop} (da : ∀ i, Decided (a i))
    (db : ∀ i, Decided (b i)) : Decided (Included a b) :=
  match da false, db false, da true, db true with
  | .inr nf, _, .inr nt, _ => .inl fun i => match i with
    | false => fun held => absurd held nf
    | true => fun held => absurd held nt
  | .inr nf, _, .inl _, .inl bt => .inl fun i => match i with
    | false => fun held => absurd held nf
    | true => fun _ => bt
  | .inr _, _, .inl at', .inr nbt => .inr fun included => nbt (included true at')
  | .inl _, .inl bf, .inr nt, _ => .inl fun i => match i with
    | false => fun _ => bf
    | true => fun held => absurd held nt
  | .inl _, .inl bf, .inl _, .inl bt => .inl fun i => match i with
    | false => fun _ => bf
    | true => fun _ => bt
  | .inl _, .inl _, .inl at', .inr nbt => .inr fun included => nbt (included true at')
  | .inl af, .inr nbf, _, _ => .inr fun included => nbf (included false af)

/-- Inclusion of claims indexed by `Unit` is decided where each claim is. -/
theorem decided_included_unit {a b : Unit → Prop} (da : Decided (a ())) (db : Decided (b ())) :
    Decided (Included a b) :=
  match da, db with
  | .inr no, _ => .inl fun i held => match i with | () => absurd held no
  | .inl _, .inl yes => .inl fun i _ => match i with | () => yes
  | .inl yes, .inr no => .inr fun included => no (included () yes)

/-- Inclusion over a sum is decided where it is on each side. -/
theorem decided_included_sum_of {I J : Type} {a b : Sum I J → Prop}
    (left : Decided (Included (fun i => a (.inl i)) (fun i => b (.inl i))))
    (right : Decided (Included (fun j => a (.inr j)) (fun j => b (.inr j)))) :
    Decided (Included a b) :=
  match left, right with
  | .inl l, .inl r => .inl fun x => match x with
    | .inl i => l i
    | .inr j => r j
  | .inr no, _ => .inr fun included => no fun i => included (.inl i)
  | _, .inr no => .inr fun included => no fun j => included (.inr j)

/-- Inclusion over `Sum Unit Bool` is decided where each claim is. -/
theorem decided_included_sum {a b : Sum Unit Bool → Prop} (da : ∀ i, Decided (a i))
    (db : ∀ i, Decided (b i)) : Decided (Included a b) :=
  decided_included_sum_of (decided_included_unit (da (.inl ())) (db (.inl ())))
    (decided_included_bool (fun j => da (.inr j)) (fun j => db (.inr j)))

namespace Formation

/-- Four continuations of one shared support history: no formation, formation by the left or the
right route, and overbuilding. The available amount is six; retaining two is the continuing
basis. These laws and the reading of the basic claims are stipulated. -/
inductive Form where
  | idle | left | right | overbuild

def drawn : Form → Nat
  | .idle => 0
  | .left => 2
  | .right => 2
  | .overbuild => 5

def remaining (f : Form) : Nat := 6 - drawn f

def linked : Form → Prop
  | .idle => False
  | .left => True
  | .right => True
  | .overbuild => True

def basis (f : Form) : Prop := 2 ≤ remaining f

def renewed (f : Form) : Prop := basis f ∧ linked f

/-- The two basic claims: the continuing basis (`false`) and its renewal (`true`). They are
contents of one history, not two owners. -/
def protect (f : Form) : Bool → Prop
  | true => renewed f
  | false => basis f

/-- The free occasion that formation spends. -/
def freeOccasion (f : Form) (_ : Unit) : Prop := drawn f = 0

def eligible (f : Form) : Prop := drawn f ≤ 6

def formed (f : Form) : Prop := linked f ∧ basis f

def menu : List Form := [.idle, .left, .right, .overbuild]

def usesLeft (f : Form) : Prop := f = .left

def usesRight (f : Form) : Prop := f = .right

theorem decided_linked : ∀ f, Decided (linked f)
  | .idle => .inr fun no => no
  | .left => .inl True.intro
  | .right => .inl True.intro
  | .overbuild => .inl True.intro

theorem decided_basis (f : Form) : Decided (basis f) := decided_of_decidable (2 ≤ remaining f)

theorem decided_protect (f : Form) : ∀ c, Decided (protect f c)
  | true => (decided_basis f).and (decided_linked f)
  | false => decided_basis f

theorem decided_free (f : Form) : Decided (freeOccasion f ()) := decided_of_decidable (drawn f = 0)

theorem decided_above (a b : Form) : Decided (Above protect freeOccasion a b) :=
  Above.decided (decided_included_bool (decided_protect b) (decided_protect a))
    (decided_included_bool (decided_protect a) (decided_protect b))
    (decided_included_unit (decided_free b) (decided_free a))
    (decided_included_unit (decided_free a) (decided_free b))

theorem basis_left : basis .left := (by decide : 2 ≤ 4)
theorem basis_right : basis .right := (by decide : 2 ≤ 4)
theorem not_basis_overbuild : ¬ basis .overbuild := (by decide : ¬ 2 ≤ 1)

theorem left_retains_basis : remaining .left = 4 ∧ basis .left ∧ renewed .left :=
  ⟨rfl, basis_left, basis_left, True.intro⟩

/-- **Formation has a real loss**: the free occasion. -/
theorem formation_loses_occasion : freeOccasion .idle () ∧ ¬ freeOccasion .left () :=
  ⟨rfl, (by decide : ¬ (2 : Nat) = 0)⟩

theorem left_above_idle : Above protect freeOccasion .left .idle :=
  Above.anchor (fun c held => match c with
      | true => absurd held.2 fun no => no
      | false => basis_left)
    true ⟨basis_left, True.intro⟩ fun held => held.2

theorem left_above_overbuild : Above protect freeOccasion .left .overbuild :=
  Above.anchor (fun c held => match c with
      | true => absurd held.1 not_basis_overbuild
      | false => absurd held not_basis_overbuild)
    false basis_left not_basis_overbuild

theorem eligible_all : ∀ f, eligible f
  | .idle => Nat.zero_le 6
  | .left => (by decide : 2 ≤ 6)
  | .right => (by decide : 2 ≤ 6)
  | .overbuild => (by decide : 5 ≤ 6)

theorem exact_menu : ∀ a, eligible a ↔ a ∈ menu
  | .idle => ⟨fun _ => .head _, fun _ => eligible_all _⟩
  | .left => ⟨fun _ => .tail _ (.head _), fun _ => eligible_all _⟩
  | .right => ⟨fun _ => .tail _ (.tail _ (.head _)), fun _ => eligible_all _⟩
  | .overbuild => ⟨fun _ => .tail _ (.tail _ (.tail _ (.head _))), fun _ => eligible_all _⟩

theorem bettered_unformed : ∀ a, eligible a → ¬ formed a →
    ∃ b, eligible b ∧ Above protect freeOccasion b a
  | .idle, _, _ => ⟨.left, eligible_all _, left_above_idle⟩
  | .left, _, unformed => absurd ⟨True.intro, basis_left⟩ unformed
  | .right, _, unformed => absurd ⟨True.intro, basis_right⟩ unformed
  | .overbuild, _, _ => ⟨.left, eligible_all _, left_above_overbuild⟩

theorem decided_formed (f : Form) : Decided (formed f) := (decided_linked f).and (decided_basis f)

/-- **Formation is required of the lexical frontier.** -/
theorem required : Required (Frontier eligible (Above protect freeOccasion)) formed :=
  required_of_bettered .idle [.left, .right, .overbuild] exact_menu
    (fun a b _ _ => (decided_above a b).weakly) Above.irrefl
    (fun first second => first.trans second) (fun a _ => decided_formed a) bettered_unformed

/-- An alternative holding both basic claims is below no alternative. -/
theorem unbeaten_of {a : Form} (both : ∀ c, protect a c) :
    ∀ b, ¬ Above protect freeOccasion b a
  | .idle => Above.no_trade true (both true) fun held => held.2
  | .overbuild => Above.no_trade false (both false) not_basis_overbuild
  | .left => Above.not_of_included (fun c _ => both c)
      fun _ held => absurd held (by decide : ¬ (2 : Nat) = 0)
  | .right => Above.not_of_included (fun c _ => both c)
      fun _ held => absurd held (by decide : ¬ (2 : Nat) = 0)

/-- Neither working route is below any alternative. -/
theorem working_unbeaten : ∀ a : Form, (a = .left ∨ a = .right) →
    ∀ b, ¬ Above protect freeOccasion b a
  | .left, _ => unbeaten_of (fun c => match c with
      | true => ⟨basis_left, True.intro⟩
      | false => basis_left)
  | .right, _ => unbeaten_of (fun c => match c with
      | true => ⟨basis_right, True.intro⟩
      | false => basis_right)
  | .idle, .inl no => Form.noConfusion no
  | .idle, .inr no => Form.noConfusion no
  | .overbuild, .inl no => Form.noConfusion no
  | .overbuild, .inr no => Form.noConfusion no

/-- **The frontier is exactly the two working routes.** -/
theorem frontier_iff (a : Form) :
    Frontier eligible (Above protect freeOccasion) a ↔ a = .left ∨ a = .right :=
  ⟨fun frontier => match a, frontier with
    | .idle, frontier => absurd left_above_idle (frontier.2 .left (eligible_all _))
    | .left, _ => .inl rfl
    | .right, _ => .inr rfl
    | .overbuild, frontier => absurd left_above_overbuild (frontier.2 .left (eligible_all _)),
   fun working => ⟨eligible_all a, fun b _ => working_unbeaten a working b⟩⟩

/-- **Neither named route is required.** -/
theorem no_route_required :
    ¬ Required (Frontier eligible (Above protect freeOccasion)) usesLeft ∧
      ¬ Required (Frontier eligible (Above protect freeOccasion)) usesRight :=
  ⟨Required.defeated ((frontier_iff .right).mpr (.inr rfl)) fun same => Form.noConfusion same,
   Required.defeated ((frontier_iff .left).mpr (.inl rfl)) fun same => Form.noConfusion same⟩

/-- **More construction can defeat its own basis.** -/
theorem overbuilding :
    drawn .left < drawn .overbuild ∧ linked .overbuild ∧ ¬ basis .overbuild ∧
      ¬ Frontier eligible (Above protect freeOccasion) .overbuild :=
  ⟨by decide, True.intro, not_basis_overbuild,
   Frontier.excluded (eligible_all .left) left_above_overbuild⟩

/-- Whether a connection was constructed. -/
def report : Form → Bool
  | .idle => false
  | .left => true
  | .right => true
  | .overbuild => true

theorem same_report_different_basis :
    report .left = report .overbuild ∧ basis .left ∧ ¬ basis .overbuild :=
  ⟨rfl, basis_left, not_basis_overbuild⟩

/-- **No judge reading only the report judges the basis.** -/
theorem no_report_judge : ¬ ∃ judge : Bool → Prop, ∀ f, judge (report f) ↔ basis f :=
  fun ⟨_, correct⟩ =>
    not_basis_overbuild ((correct .overbuild).mp ((correct .left).mpr basis_left))

/-- Read faithfully, the retained amount recovers the basis. -/
def amountJudge (amount : Nat) : Prop := 2 ≤ amount

theorem amount_recovers_basis (f : Form) : amountJudge (remaining f) ↔ basis f := Iff.rfl

/-! ### The continuations as steps on the amount

From the join `DrawnAmountProcesses` (and its inherited part): the continuations are the moves of
a process on the shared amount, each step drawing what the continuation draws. -/

/-- Within the amount, drawing leaves the amount as it was only where nothing is drawn. -/
theorem eq_zero_of_sub_eq : ∀ {a x : Nat}, x ≤ a → a - x = a → x = 0
  | _, 0, _, _ => rfl
  | 0, _ + 1, within, _ => absurd within (Nat.not_succ_le_zero _)
  | a + 1, x + 1, _, same =>
    absurd (Nat.le_trans (Nat.le_of_eq (same.symm.trans (Nat.succ_sub_succ a x)))
      (Nat.sub_le a x)) (Nat.not_succ_le_self a)

/-- Within the amount, drawing more leaves less. -/
theorem sub_lt_sub_of_lt : ∀ {a x y : Nat}, x < y → y ≤ a → a - y < a - x
  | 0, _, _ + 1, _, within => absurd within (Nat.not_succ_le_zero _)
  | _ + 1, 0, y + 1, _, _ => Nat.sub_lt (Nat.succ_pos _) (Nat.succ_pos y)
  | a + 1, x + 1, y + 1, less, within =>
    Nat.lt_of_le_of_lt (Nat.le_of_eq (Nat.succ_sub_succ a y))
      (Nat.lt_of_lt_of_le (sub_lt_sub_of_lt (Nat.lt_of_succ_lt_succ less)
          (Nat.le_of_succ_le_succ within))
        (Nat.le_of_eq (Nat.succ_sub_succ a x).symm))
  | _, _ + 1, 0, less, _ => absurd less (Nat.not_lt_zero _)
  | _, 0, 0, less, _ => absurd less (Nat.lt_irrefl 0)

end Formation

namespace Handover

/-- Plans `0` expand capability, `1` keep service, `2` transfer service, `3` withdraw abruptly;
claim `true` is a protection every plan keeps, `false` the protection that expansion and
withdrawal lose. -/
def protection (plan : Nat) (claim : Bool) : Prop :=
  claim = true ∨ plan = 1 ∨ plan = 2

/-- The gains: expansion's capability, transfer's successor. -/
def realization (plan : Nat) (claim : Bool) : Prop :=
  (plan = 0 ∧ claim = false) ∨ (plan = 2 ∧ claim = true)

def eligible (plan : Nat) : Prop := plan < 4

theorem keep_above_expansion : Above protection realization 1 0 :=
  Above.anchor (fun _ _ => .inr (.inl rfl)) false (.inr (.inl rfl)) fun
    | .inl no => Bool.noConfusion no
    | .inr (.inl no) => absurd no (by decide)
    | .inr (.inr no) => absurd no (by decide)

theorem expansion_has_real_gain : realization 0 false ∧ ¬ realization 1 false :=
  ⟨.inl ⟨rfl, rfl⟩, fun
    | .inl ⟨no, _⟩ => absurd no (by decide)
    | .inr ⟨no, _⟩ => absurd no (by decide)⟩

theorem transfer_above_keep : Above protection realization 2 1 :=
  .inr ⟨fun _ _ => .inr (.inr rfl), fun _ _ => .inr (.inl rfl),
    fun c held => match held with
      | .inl ⟨no, _⟩ => absurd no (by decide)
      | .inr ⟨no, _⟩ => absurd no (by decide),
    fun back => match back true (.inr ⟨rfl, rfl⟩) with
      | .inl ⟨no, _⟩ => absurd no (by decide)
      | .inr ⟨no, _⟩ => absurd no (by decide)⟩

theorem transfer_above_expansion : Above protection realization 2 0 :=
  transfer_above_keep.trans keep_above_expansion

/-- **Expansion is off the frontier.** -/
theorem expansion_excluded : ¬ Frontier eligible (Above protection realization) 0 :=
  Frontier.excluded (show 2 < 4 by decide) transfer_above_expansion

def demand (t : Nat) : Prop := t < 4
def oldService (t : Nat) : Prop := t < 2
def successorService (t : Nat) : Prop := 2 ≤ t ∧ t < 4

/-- **Service continues while the old model stops.** -/
theorem served : Served demand oldService successorService ∧ ¬ oldService 2 :=
  ⟨served_of_handover 2 (fun _ early _ => early) (fun _ late needed => ⟨late, needed⟩),
   Nat.lt_irrefl 2⟩

/-- A promised successor that delivers nothing does not serve. -/
theorem undelivered_fails : ¬ Served demand oldService fun _ => False :=
  Served.not_of_gap (t := 2) (show 2 < 4 by decide) (Nat.lt_irrefl 2) fun no => no

/-- Where transfer harms a contributor's basic life, the two basic protections cross. -/
def crossed (transfer : Bool) (claim : Bool) : Prop := transfer = claim

theorem crossed_unranked :
    ¬ Above crossed Crossed.noGain true false ∧ ¬ Above crossed Crossed.noGain false true :=
  Crossed.incomparable

end Handover

namespace Collective

/-- **A collective task can be required with no individual one.** -/
theorem required :
    Required (fun _ : Bool => True) (fun p => p = true ∨ p = false) ∧
      ¬ Required (fun _ : Bool => True) (fun p => p = true) ∧
      ¬ Required (fun _ : Bool => True) (fun p => p = false) :=
  ⟨⟨⟨true, True.intro⟩, fun p _ => match p with
      | true => .inl rfl
      | false => .inr rfl⟩,
   Required.defeated (a := false) True.intro Bool.noConfusion,
   Required.defeated (a := true) True.intro Bool.noConfusion⟩

/-- **Each world can have a plan with no plan common to every world.** -/
theorem no_common_plan :
    (∀ w : Bool, ∃ a : Bool, a = w) ∧ ¬ ∃ a : Bool, ∀ w : Bool, a = w :=
  ⟨fun w => ⟨w, rfl⟩, fun ⟨_, all⟩ => Bool.noConfusion ((all true).symm.trans (all false))⟩

end Collective

/-! ## Formation required under every classification -/

section ClassifiedFrontier

variable {H C G N : Type} {p : H → C → Prop} {g : H → G → Prop} {f : H → N → Prop}

/-- **Formation required without a fixed classification**: where every eligible alternative
lacking the formation is bettered, under the fresh contents adjoined as gains, by one retaining its
fresh contents, formation is required of the frontier under every classification, on a nonempty
listed menu with the comparisons weakly decided, formation decided, and the decisions of
`classified_of_decided` named. -/
theorem required_under_every_classification {eligible formed : H → Prop} (x : H) (rest : List H)
    (exact : ∀ a, eligible a ↔ a ∈ x :: rest)
    (weakly : ∀ (q : N → Prop) a b, eligible a → eligible b →
      WeaklyDecided (classified p g f q a b))
    (decidedFormed : ∀ a, eligible a → Decided (formed a))
    (held : ∀ a n, eligible a → Decided (f a n))
    (tie : ∀ (q : N → Prop) a b, eligible a → eligible b → Decided (∀ n, f a n → q n → f b n))
    (construction : ∀ a, eligible a → ¬ formed a →
      ∃ b, eligible b ∧ Included (f a) (f b) ∧ Above p (Lexical.adjoin g f) b a) :
    ∀ q, Required (Frontier eligible (classified p g f q)) formed :=
  fun q => required_of_bettered x rest exact (weakly q) Above.irrefl
    (fun first second => first.trans second) decidedFormed
    fun a admitted unformed => match construction a admitted unformed with
    | ⟨b, eligibleB, retain, above⟩ =>
      ⟨b, eligibleB, classified_of_decided retain above q (fun n => held a n admitted)
        (tie q b a eligibleB admitted)⟩

end ClassifiedFrontier

namespace Routes

/-- One formative history can open either of two contents of positive relevance. -/
inductive Route where
  | absent | left | right

def basic (_ : Route) (_ : Unit) : Prop := True
def gain (_ : Route) (_ : Unit) : Prop := False

def fresh : Route → Bool → Prop
  | .absent, _ => False
  | .left, n => n = false
  | .right, n => n = true

def formed (r : Route) : Prop := r ≠ .absent

/-- With the classification decided content by content, the left route is above absence. -/
theorem left_above_absent (q : Bool → Prop) (decided : ∀ n, Decided (q n)) :
    classified basic gain fresh q .left .absent :=
  match decided false with
  | .inl basicFresh => .inl ⟨fun i => match i with
        | .inl _ => fun _ => True.intro
        | .inr _ => fun held => False.elim held.1,
      fun back => (back (.inr false) ⟨rfl, basicFresh⟩).1⟩
  | .inr gainFresh => .inr ⟨fun i => match i with
        | .inl _ => fun _ => True.intro
        | .inr _ => fun held => False.elim held.1,
      fun i => match i with
        | .inl _ => fun _ => True.intro
        | .inr n => fun held => match n, held with
          | false, ⟨_, yes⟩ => absurd yes gainFresh
          | true, ⟨no, _⟩ => Bool.noConfusion no,
      fun i => match i with
        | .inl _ => fun held => False.elim held
        | .inr _ => fun held => False.elim held.1,
      fun back => (back (.inr false) ⟨rfl, gainFresh⟩).1⟩

/-- Absence is off the frontier under a classification decided content by content: the left route
is above it. -/
theorem formed_of_frontier (q : Bool → Prop) (decided : ∀ n, Decided (q n)) (r : Route)
    (frontier : Frontier (fun _ => True) (classified basic gain fresh q) r) : formed r :=
  fun same => frontier.2 .left True.intro (same ▸ left_above_absent q decided)

theorem decided_fresh : ∀ r n, Decided (fresh r n)
  | .absent, _ => .inr fun no => no
  | .left, false => .inl rfl
  | .left, true => .inr Bool.noConfusion
  | .right, false => .inr Bool.noConfusion
  | .right, true => .inl rfl

theorem decided_basic (q : Bool → Prop) (decided : ∀ n, Decided (q n)) (r : Route) :
    ∀ i, Decided (classifiedBasic basic fresh q r i)
  | .inl _ => .inl True.intro
  | .inr n => (decided_fresh r n).and (decided n)

theorem decided_gain (q : Bool → Prop) (decided : ∀ n, Decided (q n)) (r : Route) :
    ∀ i, Decided (classifiedGain gain fresh q r i)
  | .inl _ => .inr fun no => no
  | .inr n => (decided_fresh r n).and (decided n).not

theorem decided_classified (q : Bool → Prop) (decided : ∀ n, Decided (q n)) (a b : Route) :
    Decided (classified basic gain fresh q a b) :=
  Above.decided
    (decided_included_sum (decided_basic q decided b) (decided_basic q decided a))
    (decided_included_sum (decided_basic q decided a) (decided_basic q decided b))
    (decided_included_sum (decided_gain q decided b) (decided_gain q decided a))
    (decided_included_sum (decided_gain q decided a) (decided_gain q decided b))

/-- **Under every classification decided content by content, a formed route is required.** -/
theorem required (q : Bool → Prop) (decided : ∀ n, Decided (q n)) :
    Required (Frontier (fun _ => True) (classified basic gain fresh q)) formed :=
  ⟨frontier_exists (eligible := fun _ => True) (better := classified basic gain fresh q)
      .absent [.left, .right]
      (fun a => ⟨fun _ => match a with
          | .absent => .head _
          | .left => .tail _ (.head _)
          | .right => .tail _ (.tail _ (.head _)),
        fun _ => True.intro⟩)
      (fun a b _ _ => (decided_classified q decided a b).weakly) Above.irrefl
      (fun first second => first.trans second),
   fun r frontier => formed_of_frontier q decided r frontier⟩

/-- **Mixed classifications can favour opposite routes.** -/
theorem opposite_routes :
    classified basic gain fresh (fun n => n = false) .left .right ∧
      classified basic gain fresh (fun n => n = true) .right .left :=
  ⟨Above.anchor (fun i held => match i, held with
      | .inl _, _ => True.intro
      | .inr false, ⟨no, _⟩ => Bool.noConfusion no
      | .inr true, ⟨_, no⟩ => Bool.noConfusion no)
    (.inr false) ⟨rfl, rfl⟩ fun held => Bool.noConfusion held.1,
   Above.anchor (fun i held => match i, held with
      | .inl _, _ => True.intro
      | .inr false, ⟨_, no⟩ => Bool.noConfusion no
      | .inr true, ⟨no, _⟩ => Bool.noConfusion no)
    (.inr true) ⟨rfl, rfl⟩ fun held => Bool.noConfusion held.1⟩

/-- **No route is on the frontier under every classification**: the role is required, a common
undefeated implementation is not. -/
theorem none_robust :
    ¬ ∃ r, ∀ q, Frontier (fun _ => True) (classified basic gain fresh q) r :=
  fun ⟨r, all⟩ => match r with
  | .absent => formed_of_frontier (fun _ => False) (fun _ => .inr fun no => no) .absent
      (all fun _ => False) rfl
  | .left => (all fun n => n = true).2 .right True.intro opposite_routes.2
  | .right => (all fun n => n = false).2 .left True.intro opposite_routes.1

end Routes

end Requirement

end Becoming
