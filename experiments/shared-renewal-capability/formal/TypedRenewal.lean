import RenewalLedger

/-!
Concrete two-type CF paid-access reaction system and its verified ledger map.
There is only a type-1 bound-reproduction constructor. Optional bound copying,
CF-catalyzed free-F recycling, CF -> C+F and reverse chemistry are absent.
This is a stoichiometric simulation into the pooled ledger, not kinetic lumping.
-/
namespace TypedRenewal

inductive Kind where | zero | one
  deriving DecidableEq, Repr

structure State where
  r : Int := 0
  c : Int := 0
  cf : Int := 0
  y : Int := 0
  d : Int := 0
  f : Int := 0
  a0 : Int := 0
  a1 : Int := 0
  g0 : Int := 0
  g1 : Int := 0
  gf0 : Int := 0
  gf1 : Int := 0
  yg0 : Int := 0
  yg1 : Int := 0
  deriving DecidableEq, Repr

def choose (k : Kind) (z o : State) : State :=
  match k with | .zero => z | .one => o

def Nonnegative (x : State) : Prop :=
  0 ≤ x.r ∧ 0 ≤ x.c ∧ 0 ≤ x.cf ∧ 0 ≤ x.y ∧ 0 ≤ x.d ∧ 0 ≤ x.f ∧
  0 ≤ x.a0 ∧ 0 ≤ x.a1 ∧ 0 ≤ x.g0 ∧ 0 ≤ x.g1 ∧
  0 ≤ x.gf0 ∧ 0 ≤ x.gf1 ∧ 0 ≤ x.yg0 ∧ 0 ≤ x.yg1

def AtLeast (x q : State) : Prop :=
  q.r ≤ x.r ∧ q.c ≤ x.c ∧ q.cf ≤ x.cf ∧ q.y ≤ x.y ∧ q.d ≤ x.d ∧
  q.f ≤ x.f ∧ q.a0 ≤ x.a0 ∧ q.a1 ≤ x.a1 ∧ q.g0 ≤ x.g0 ∧ q.g1 ≤ x.g1 ∧
  q.gf0 ≤ x.gf0 ∧ q.gf1 ≤ x.gf1 ∧ q.yg0 ≤ x.yg0 ∧ q.yg1 ≤ x.yg1

inductive Event where
  | assemble | cWear | reproduce | yWear | capture | leak | recycleC | recycleY
  | formA (k : Kind) | copyA (k : Kind) | fabricateG (k : Kind)
  | aWear (k : Kind) | gWear (k : Kind)
  | bindF (k : Kind) | unbindF (k : Kind) | boundLeak (k : Kind) | gfWear (k : Kind)
  | bindY (k : Kind) | unbindY (k : Kind) | ygGWear (k : Kind) | ygYWear (k : Kind)
  | boundReproduce1 | cfLeak | cfWear | accessRepair
  | accessForm (k : Kind) | accessFabricate (k : Kind)
  deriving DecidableEq, Repr

def input : Event → State
  | .assemble => { r := 1 }
  | .cWear => { c := 1 }
  | .reproduce => { r := 1, y := 1 }
  | .yWear => { y := 1 }
  | .capture => { c := 1 }
  | .leak => { f := 1 }
  | .recycleC => { d := 1, f := 1, c := 1 }
  | .recycleY => { d := 1, f := 1, y := 1 }
  | .formA _ => { r := 1, f := 1 }
  | .copyA k | .fabricateG k =>
      choose k { a0 := 1, r := 1, f := 1 } { a1 := 1, r := 1, f := 1 }
  | .aWear k => choose k { a0 := 1 } { a1 := 1 }
  | .gWear k => choose k { g0 := 1 } { g1 := 1 }
  | .bindF k => choose k { g0 := 1, f := 1 } { g1 := 1, f := 1 }
  | .unbindF k | .boundLeak k | .gfWear k => choose k { gf0 := 1 } { gf1 := 1 }
  | .bindY k => choose k { g0 := 1, y := 1 } { g1 := 1, y := 1 }
  | .unbindY k | .ygGWear k | .ygYWear k => choose k { yg0 := 1 } { yg1 := 1 }
  | .boundReproduce1 => { r := 1, yg1 := 1 }
  | .cfLeak | .cfWear => { cf := 1 }
  | .accessRepair => { d := 1, cf := 1 }
  | .accessForm _ => { r := 1, cf := 1 }
  | .accessFabricate k =>
      choose k { a0 := 1, r := 1, cf := 1 } { a1 := 1, r := 1, cf := 1 }

def output : Event → State
  | .assemble => { c := 1 }
  | .cWear => { d := 1 }
  | .reproduce => { y := 2 }
  | .yWear => { d := 1 }
  | .capture => { cf := 1 }
  | .leak => {}
  | .recycleC => { r := 1, c := 1 }
  | .recycleY => { r := 1, y := 1 }
  | .formA k => choose k { a0 := 1 } { a1 := 1 }
  | .copyA k => choose k { a0 := 2 } { a1 := 2 }
  | .fabricateG k => choose k { a0 := 1, g0 := 1 } { a1 := 1, g1 := 1 }
  | .aWear _ | .gWear _ => { d := 1 }
  | .bindF k => choose k { gf0 := 1 } { gf1 := 1 }
  | .unbindF k => choose k { g0 := 1, f := 1 } { g1 := 1, f := 1 }
  | .boundLeak k => choose k { g0 := 1 } { g1 := 1 }
  | .gfWear _ => { d := 1, f := 1 }
  | .bindY k => choose k { yg0 := 1 } { yg1 := 1 }
  | .unbindY k => choose k { g0 := 1, y := 1 } { g1 := 1, y := 1 }
  | .ygGWear _ => { y := 1, d := 1 }
  | .ygYWear k => choose k { g0 := 1, d := 1 } { g1 := 1, d := 1 }
  | .boundReproduce1 => { y := 1, yg1 := 1 }
  | .cfLeak => { c := 1 }
  | .cfWear => { d := 1, f := 1 }
  | .accessRepair => { r := 1, c := 1 }
  | .accessForm k => choose k { a0 := 1, c := 1 } { a1 := 1, c := 1 }
  | .accessFabricate k =>
      choose k { a0 := 1, g0 := 1, c := 1 } { a1 := 1, g1 := 1, c := 1 }

def step (e : Event) (x : State) : State :=
  let i := input e
  let o := output e
  { r := x.r - i.r + o.r, c := x.c - i.c + o.c,
    cf := x.cf - i.cf + o.cf, y := x.y - i.y + o.y,
    d := x.d - i.d + o.d, f := x.f - i.f + o.f,
    a0 := x.a0 - i.a0 + o.a0, a1 := x.a1 - i.a1 + o.a1,
    g0 := x.g0 - i.g0 + o.g0, g1 := x.g1 - i.g1 + o.g1,
    gf0 := x.gf0 - i.gf0 + o.gf0, gf1 := x.gf1 - i.gf1 + o.gf1,
    yg0 := x.yg0 - i.yg0 + o.yg0, yg1 := x.yg1 - i.yg1 + o.yg1 }

def Enabled (e : Event) (x : State) : Prop := Nonnegative x ∧ AtLeast x (input e)

def project (x : State) : RenewalLedger.State :=
  { r := x.r, c := x.c, cf := x.cf, y := x.y, d := x.d, f := x.f,
    a := x.a0 + x.a1, g := x.g0 + x.g1,
    gf := x.gf0 + x.gf1, yg := x.yg0 + x.yg1 }

def eventMap : Event → RenewalLedger.Event
  | .assemble => .assemble
  | .cWear => .cWear
  | .reproduce => .reproduce
  | .yWear => .yWear
  | .capture => .capture
  | .leak => .leak
  | .recycleC => .recycleC
  | .recycleY => .recycleY
  | .formA _ => .formA
  | .copyA _ => .copyA
  | .fabricateG _ => .fabricateG
  | .aWear _ => .aWear
  | .gWear _ => .gWear
  | .bindF _ => .bindF
  | .unbindF _ => .unbindF
  | .boundLeak _ => .boundLeak
  | .gfWear _ => .gfWear
  | .bindY _ => .bindY
  | .unbindY _ => .unbindY
  | .ygGWear _ => .ygGWear
  | .ygYWear _ => .ygYWear
  | .boundReproduce1 => .boundReproduce
  | .cfLeak => .cfLeak
  | .cfWear => .cfWear
  | .accessRepair => .accessRepair
  | .accessForm _ => .accessForm
  | .accessFabricate _ => .accessFabricate

theorem input_project (e : Event) : project (input e) = RenewalLedger.input (eventMap e) := by
  cases e <;> first | rfl | (rename_i k; cases k <;> rfl)

theorem output_project (e : Event) : project (output e) = RenewalLedger.output (eventMap e) := by
  cases e <;> first | rfl | (rename_i k; cases k <;> rfl)

theorem project_step (e : Event) (x : State) :
    project (step e x) = RenewalLedger.step (eventMap e) (project x) := by
  rw [RenewalLedger.step, ← input_project, ← output_project]
  simp only [step, project]
  congr 1 <;> omega

theorem project_nonnegative {x : State} (h : Nonnegative x) :
    RenewalLedger.Nonnegative (project x) := by
  simp only [Nonnegative, RenewalLedger.Nonnegative, project] at *
  omega

theorem project_atLeast {x q : State} (h : AtLeast x q) :
    RenewalLedger.AtLeast (project x) (project q) := by
  simp only [AtLeast, RenewalLedger.AtLeast, project] at *
  omega

theorem enabled_project {e : Event} {x : State} (h : Enabled e x) :
    RenewalLedger.Enabled (eventMap e) (project x) := by
  constructor
  · exact project_nonnegative h.1
  · rw [← input_project]
    exact project_atLeast h.2

theorem output_nonnegative (e : Event) : Nonnegative (output e) := by
  cases e <;> (try (rename_i k; cases k)) <;> simp [output, Nonnegative, choose]

theorem step_nonnegative {e : Event} {x : State} (h : Enabled e x) :
    Nonnegative (step e x) := by
  have ho := output_nonnegative e
  simp only [Enabled, Nonnegative, AtLeast, step] at *
  omega

def bare : Event → Prop
  | .accessRepair | .accessForm _ | .accessFabricate _ => False
  | _ => True

theorem bare_map (e : Event) : bare e ↔ RenewalLedger.bare (eventMap e) := by
  cases e <;> rfl

inductive Trace (allowed : Event → Prop) : State → List Event → State → Prop where
  | nil (x : State) : Trace allowed x [] x
  | cons {x y : State} {e : Event} {es : List Event}
      (ha : allowed e) (he : Enabled e x)
      (ht : Trace allowed (step e x) es y) : Trace allowed x (e :: es) y

theorem trace_project {allowed : Event → Prop} {pooled : RenewalLedger.Event → Prop}
    {x y : State} {es : List Event}
    (hm : ∀ e, allowed e → pooled (eventMap e)) (ht : Trace allowed x es y) :
    RenewalLedger.Trace pooled (project x) (es.map eventMap) (project y) := by
  induction ht with
  | nil => exact RenewalLedger.Trace.nil _
  | @cons x y e es ha he ht ih =>
    rw [project_step] at ih
    exact RenewalLedger.Trace.cons (hm e ha) (enabled_project he) ih

theorem trace_nonnegative {allowed : Event → Prop} {x y : State} {es : List Event}
    (ht : Trace allowed x es y) (hx : Nonnegative x) : Nonnegative y := by
  induction ht with
  | nil => exact hx
  | cons ha he ht ih => exact ih (step_nonnegative he)

def material (x : State) : Int := RenewalLedger.material (project x)
def work (x : State) : Int := RenewalLedger.work (project x)
def totalA (x : State) : Int := (project x).a
def gates (x : State) : Int := RenewalLedger.gates (project x)

theorem trace_material {allowed : Event → Prop} {x y : State} {es : List Event}
    (ht : Trace allowed x es y) : material y = material x := by
  exact RenewalLedger.trace_material (trace_project (pooled := fun _ => True) (by simp) ht)

def operation (a g : Kind) : State :=
  match a, g with
  | .zero, .zero => { a0 := 1, cf := 1, yg0 := 1 }
  | .zero, .one => { a0 := 1, cf := 1, yg1 := 1 }
  | .one, .zero => { a1 := 1, cf := 1, yg0 := 1 }
  | .one, .one => { a1 := 1, cf := 1, yg1 := 1 }

theorem operation_project (a g : Kind) :
    project (operation a g) = RenewalLedger.operation := by
  cases a <;> cases g <;> rfl

theorem bare_no_later_construction {a g : Kind} {y : State} {es : List Event}
    (ht : Trace bare (operation a g) es y) :
    ∀ j, ¬ Enabled (.formA j) y ∧ ¬ Enabled (.copyA j) y ∧ ¬ Enabled (.fabricateG j) y := by
  have hp := trace_project (pooled := RenewalLedger.bare)
    (fun e he => (bare_map e).mp he) ht
  rw [operation_project] at hp
  have hb := RenewalLedger.bare_no_later_construction hp
  intro j
  constructor
  · intro he
    exact hb.1 (enabled_project he)
  constructor
  · intro he
    exact hb.2.1 (enabled_project he)
  · intro he
    exact hb.2.2 (enabled_project he)

def tally (f : Event → Int) : List Event → Int
  | [] => 0
  | e :: es => f e + tally f es

theorem tally_project (f : RenewalLedger.Event → Int) (es : List Event) :
    RenewalLedger.tally f (es.map eventMap) = tally (fun e => f (eventMap e)) es := by
  induction es with
  | nil => rfl
  | cons e es ih => simp only [List.map_cons, RenewalLedger.tally, tally, ih]

def capture (e : Event) : Int := RenewalLedger.capture (eventMap e)
def leakage (e : Event) : Int := RenewalLedger.leakage (eventMap e)
def aBirth (e : Event) : Int := RenewalLedger.aBirth (eventMap e)
def gBirth (e : Event) : Int := RenewalLedger.gBirth (eventMap e)
def aWear (e : Event) : Int := RenewalLedger.aWear (eventMap e)
def gWear (e : Event) : Int := RenewalLedger.gWear (eventMap e)
def cWear (e : Event) : Int := RenewalLedger.cWear (eventMap e)
def yWear (e : Event) : Int := RenewalLedger.yWear (eventMap e)

theorem minimum_repeated_turnover_captures
    {allowed : Event → Prop} {x y : State} {es : List Event}
    (ht : Trace allowed x es y)
    (hw : work y = work x) (ha : totalA y = totalA x) (hg : gates y = gates x)
    (n : Int) (hAw : n ≤ tally aWear es) (hGw : n ≤ tally gWear es)
    (hCw : n ≤ tally cWear es) (hYw : n ≤ tally yWear es) :
    6*n ≤ tally capture es := by
  have hp := trace_project (pooled := fun _ => True) (by simp) ht
  have h := RenewalLedger.minimum_repeated_turnover_captures hp hw ha hg n
    (by simpa only [tally_project] using hAw)
    (by simpa only [tally_project] using hGw)
    (by simpa only [tally_project] using hCw)
    (by simpa only [tally_project] using hYw)
  simpa only [tally_project] using h

theorem minimum_full_turnover_captures
    {allowed : Event → Prop} {x y : State} {es : List Event}
    (ht : Trace allowed x es y)
    (hw : work y = work x) (ha : totalA y = totalA x) (hg : gates y = gates x)
    (hAw : 1 ≤ tally aWear es) (hGw : 1 ≤ tally gWear es)
    (hCw : 1 ≤ tally cWear es) (hYw : 1 ≤ tally yWear es) :
    6 ≤ tally capture es := by
  simpa using minimum_repeated_turnover_captures ht hw ha hg 1 hAw hGw hCw hYw

/- Exact minimum expenditure leaves no room for leakage, extra births or
extra wears. The four wear assumptions are role-count assumptions; original
carrier identities are not represented by this unlabelled state. -/
theorem exact_six_capture_budget
    {allowed : Event → Prop} {x y : State} {es : List Event}
    (ht : Trace allowed x es y)
    (hw : work y = work x) (ha : totalA y = totalA x) (hg : gates y = gates x)
    (hAw : 1 ≤ tally aWear es) (hGw : 1 ≤ tally gWear es)
    (hCw : 1 ≤ tally cWear es) (hYw : 1 ≤ tally yWear es)
    (hcap : tally capture es = 6) :
    tally leakage es = 0 ∧ tally aBirth es = 1 ∧ tally gBirth es = 1 ∧
    tally aWear es = 1 ∧ tally gWear es = 1 ∧
    tally cWear es = 1 ∧ tally yWear es = 1 := by
  have hp := trace_project (pooled := fun _ => True) (by simp) ht
  have hwork := RenewalLedger.trace_change RenewalLedger.work
    (fun e => RenewalLedger.capture e - RenewalLedger.loss e)
    (fun e s => by dsimp only; have h := RenewalLedger.work_step e s; omega) hp
  have hA := RenewalLedger.trace_change (fun s => s.a)
    (fun e => RenewalLedger.aBirth e - RenewalLedger.aWear e)
    (fun e s => by dsimp only; have h := RenewalLedger.a_step e s; omega) hp
  have hG := RenewalLedger.trace_change RenewalLedger.gates
    (fun e => RenewalLedger.gBirth e - RenewalLedger.gWear e)
    (fun e s => by dsimp only; have h := RenewalLedger.g_step e s; omega) hp
  rw [RenewalLedger.tally_sub] at hwork hA hG
  have hloss : RenewalLedger.tally RenewalLedger.loss (es.map eventMap) =
      RenewalLedger.tally RenewalLedger.leakage (es.map eventMap) +
      RenewalLedger.tally RenewalLedger.aBirth (es.map eventMap) +
      RenewalLedger.tally RenewalLedger.gBirth (es.map eventMap) +
      RenewalLedger.tally RenewalLedger.aWear (es.map eventMap) +
      RenewalLedger.tally RenewalLedger.gWear (es.map eventMap) +
      RenewalLedger.tally RenewalLedger.cWear (es.map eventMap) +
      RenewalLedger.tally RenewalLedger.yWear (es.map eventMap) := by
    change RenewalLedger.tally (fun e => RenewalLedger.leakage e +
      RenewalLedger.aBirth e + RenewalLedger.gBirth e + RenewalLedger.aWear e +
      RenewalLedger.gWear e + RenewalLedger.cWear e + RenewalLedger.yWear e) _ = _
    repeat rw [RenewalLedger.tally_add]
  have hn := RenewalLedger.tally_nonnegative RenewalLedger.leakage
    (by intro e; cases e <;> decide) (es.map eventMap)
  simp only [tally_project] at hwork hA hG hloss hn
  simp only [work, totalA, gates] at hw ha hg
  change 1 ≤ tally (fun e => RenewalLedger.aWear (eventMap e)) es at hAw
  change 1 ≤ tally (fun e => RenewalLedger.gWear (eventMap e)) es at hGw
  change 1 ≤ tally (fun e => RenewalLedger.cWear (eventMap e)) es at hCw
  change 1 ≤ tally (fun e => RenewalLedger.yWear (eventMap e)) es at hYw
  change tally (fun e => RenewalLedger.capture (eventMap e)) es = 6 at hcap
  change tally (fun e => RenewalLedger.leakage (eventMap e)) es = 0 ∧
    tally (fun e => RenewalLedger.aBirth (eventMap e)) es = 1 ∧
    tally (fun e => RenewalLedger.gBirth (eventMap e)) es = 1 ∧
    tally (fun e => RenewalLedger.aWear (eventMap e)) es = 1 ∧
    tally (fun e => RenewalLedger.gWear (eventMap e)) es = 1 ∧
    tally (fun e => RenewalLedger.cWear (eventMap e)) es = 1 ∧
    tally (fun e => RenewalLedger.yWear (eventMap e)) es = 1
  omega

/- Projection is one-way: type-0 inhibition is retained by the concrete
event vocabulary but forgotten by the pooled overapproximation. -/
def blockedExample : State := { r := 1, yg0 := 1 }

theorem pooled_enabled_does_not_lift :
    RenewalLedger.Enabled .boundReproduce (project blockedExample) ∧
    ¬ Enabled .boundReproduce1 blockedExample := by
  simp [RenewalLedger.Enabled, RenewalLedger.Nonnegative, RenewalLedger.AtLeast,
    RenewalLedger.input, Enabled, Nonnegative, AtLeast, input, project, blockedExample]

end TypedRenewal

#print axioms TypedRenewal.input_project
#print axioms TypedRenewal.output_project
#print axioms TypedRenewal.project_step
#print axioms TypedRenewal.enabled_project
#print axioms TypedRenewal.step_nonnegative
#print axioms TypedRenewal.trace_project
#print axioms TypedRenewal.trace_nonnegative
#print axioms TypedRenewal.trace_material
#print axioms TypedRenewal.bare_no_later_construction
#print axioms TypedRenewal.minimum_repeated_turnover_captures
#print axioms TypedRenewal.minimum_full_turnover_captures
#print axioms TypedRenewal.exact_six_capture_budget
#print axioms TypedRenewal.pooled_enabled_does_not_lift
