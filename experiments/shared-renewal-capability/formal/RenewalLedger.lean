import Std

/-!
Machine-checked stoichiometric ledger for the CF-storage parent and its three
paid-access extensions. Counts of corresponding A/G types are summed here.
This is a ledger projection, not a kinetic quotient or a positive-reachability
certificate for the typed chemistry. No probabilities or physical rate claims
are assumed or proved by this file.
-/
namespace RenewalLedger

structure State where
  r : Int := 0
  c : Int := 0
  cf : Int := 0
  y : Int := 0
  d : Int := 0
  f : Int := 0
  a : Int := 0
  g : Int := 0
  gf : Int := 0
  yg : Int := 0
  deriving DecidableEq, Repr

def Nonnegative (x : State) : Prop :=
  0 ≤ x.r ∧ 0 ≤ x.c ∧ 0 ≤ x.cf ∧ 0 ≤ x.y ∧ 0 ≤ x.d ∧
  0 ≤ x.f ∧ 0 ≤ x.a ∧ 0 ≤ x.g ∧ 0 ≤ x.gf ∧ 0 ≤ x.yg

def AtLeast (x q : State) : Prop :=
  q.r ≤ x.r ∧ q.c ≤ x.c ∧ q.cf ≤ x.cf ∧ q.y ≤ x.y ∧ q.d ≤ x.d ∧
  q.f ≤ x.f ∧ q.a ≤ x.a ∧ q.g ≤ x.g ∧ q.gf ≤ x.gf ∧ q.yg ≤ x.yg

inductive Event where
  | assemble | cWear | reproduce | yWear | capture | leak
  | recycleC | recycleY | formA | copyA | fabricateG | aWear | gWear
  | bindF | unbindF | boundLeak | gfWear | bindY | unbindY
  | ygGWear | ygYWear | boundReproduce | cfLeak | cfWear
  | accessRepair | accessForm | accessFabricate
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
  | .formA => { r := 1, f := 1 }
  | .copyA => { a := 1, r := 1, f := 1 }
  | .fabricateG => { a := 1, r := 1, f := 1 }
  | .aWear => { a := 1 }
  | .gWear => { g := 1 }
  | .bindF => { g := 1, f := 1 }
  | .unbindF => { gf := 1 }
  | .boundLeak => { gf := 1 }
  | .gfWear => { gf := 1 }
  | .bindY => { g := 1, y := 1 }
  | .unbindY => { yg := 1 }
  | .ygGWear => { yg := 1 }
  | .ygYWear => { yg := 1 }
  | .boundReproduce => { r := 1, yg := 1 }
  | .cfLeak => { cf := 1 }
  | .cfWear => { cf := 1 }
  | .accessRepair => { d := 1, cf := 1 }
  | .accessForm => { r := 1, cf := 1 }
  | .accessFabricate => { a := 1, r := 1, cf := 1 }

def output : Event → State
  | .assemble => { c := 1 }
  | .cWear => { d := 1 }
  | .reproduce => { y := 2 }
  | .yWear => { d := 1 }
  | .capture => { cf := 1 }
  | .leak => {}
  | .recycleC => { r := 1, c := 1 }
  | .recycleY => { r := 1, y := 1 }
  | .formA => { a := 1 }
  | .copyA => { a := 2 }
  | .fabricateG => { a := 1, g := 1 }
  | .aWear => { d := 1 }
  | .gWear => { d := 1 }
  | .bindF => { gf := 1 }
  | .unbindF => { g := 1, f := 1 }
  | .boundLeak => { g := 1 }
  | .gfWear => { d := 1, f := 1 }
  | .bindY => { yg := 1 }
  | .unbindY => { g := 1, y := 1 }
  | .ygGWear => { y := 1, d := 1 }
  | .ygYWear => { g := 1, d := 1 }
  | .boundReproduce => { y := 1, yg := 1 }
  | .cfLeak => { c := 1 }
  | .cfWear => { d := 1, f := 1 }
  | .accessRepair => { r := 1, c := 1 }
  | .accessForm => { a := 1, c := 1 }
  | .accessFabricate => { a := 1, g := 1, c := 1 }

def step (e : Event) (x : State) : State :=
  let i := input e
  let o := output e
  { r := x.r - i.r + o.r, c := x.c - i.c + o.c,
    cf := x.cf - i.cf + o.cf, y := x.y - i.y + o.y,
    d := x.d - i.d + o.d, f := x.f - i.f + o.f,
    a := x.a - i.a + o.a, g := x.g - i.g + o.g,
    gf := x.gf - i.gf + o.gf, yg := x.yg - i.yg + o.yg }

def Enabled (e : Event) (x : State) : Prop := Nonnegative x ∧ AtLeast x (input e)
def bare : Event → Prop
  | .accessRepair | .accessForm | .accessFabricate => False
  | _ => True

def material (x : State) : Int :=
  x.r + x.c + x.cf + x.y + x.d + x.a + x.g + x.gf + 2*x.yg
def packets (x : State) : Int := x.f + x.cf + x.gf
def work (x : State) : Int := material x - x.d + packets x
def available (x : State) : Int := x.r + x.c + x.cf + x.f + x.gf
def gates (x : State) : Int := x.g + x.gf + x.yg

def capture : Event → Int | .capture => 1 | _ => 0
def leakage : Event → Int | .leak | .boundLeak | .cfLeak => 1 | _ => 0
def aBirth : Event → Int | .formA | .copyA | .accessForm => 1 | _ => 0
def gBirth : Event → Int | .fabricateG | .accessFabricate => 1 | _ => 0
def aWear : Event → Int | .aWear => 1 | _ => 0
def gWear : Event → Int | .gWear | .gfWear | .ygGWear => 1 | _ => 0
def cWear : Event → Int | .cWear | .cfWear => 1 | _ => 0
def yWear : Event → Int | .yWear | .ygYWear => 1 | _ => 0
def loss (e : Event) : Int :=
  leakage e + aBirth e + gBirth e + aWear e + gWear e + cWear e + yWear e

theorem step_nonnegative (e : Event) (x : State) (h : Enabled e x) :
    Nonnegative (step e x) := by
  cases e <;> simp_all [Enabled, Nonnegative, AtLeast, step, input, output] <;> omega

theorem material_step (e : Event) (x : State) : material (step e x) = material x := by
  cases e <;> simp [material, step, input, output] <;> omega

theorem work_step (e : Event) (x : State) :
    work (step e x) = work x + capture e - loss e := by
  cases e <;> simp [work, material, packets, step, input, output, capture, loss,
    leakage, aBirth, gBirth, aWear, gWear, cWear, yWear] <;> omega

theorem a_step (e : Event) (x : State) :
    (step e x).a = x.a + aBirth e - aWear e := by
  cases e <;> simp [step, input, output, aBirth, aWear] <;> omega

theorem g_step (e : Event) (x : State) :
    gates (step e x) = gates x + gBirth e - gWear e := by
  cases e <;> simp [gates, step, input, output, gBirth, gWear] <;> omega

theorem bare_available_step (e : Event) (x : State) (h : bare e) :
    available (step e x) ≤ available x := by
  cases e <;> simp_all [bare, available, step, input, output] <;> omega

inductive Trace (allowed : Event → Prop) : State → List Event → State → Prop where
  | nil (x : State) : Trace allowed x [] x
  | cons {x y : State} {e : Event} {es : List Event}
      (ha : allowed e) (he : Enabled e x)
      (ht : Trace allowed (step e x) es y) : Trace allowed x (e :: es) y

def tally (f : Event → Int) : List Event → Int
  | [] => 0
  | e :: es => f e + tally f es

theorem tally_add (f g : Event → Int) (es : List Event) :
    tally (fun e => f e + g e) es = tally f es + tally g es := by
  induction es with
  | nil => simp [tally]
  | cons e es ih => simp only [tally]; rw [ih]; omega

theorem tally_sub (f g : Event → Int) (es : List Event) :
    tally (fun e => f e - g e) es = tally f es - tally g es := by
  induction es with
  | nil => simp [tally]
  | cons e es ih => simp only [tally]; rw [ih]; omega

theorem tally_nonnegative (f : Event → Int) (h : ∀ e, 0 ≤ f e) (es : List Event) :
    0 ≤ tally f es := by
  induction es with
  | nil => simp [tally]
  | cons e es ih => simp only [tally]; have he := h e; omega

theorem trace_change {allowed : Event → Prop} {x y : State} {es : List Event}
    (v : State → Int) (delta : Event → Int)
    (hstep : ∀ e s, v (step e s) = v s + delta e)
    (ht : Trace allowed x es y) : v y = v x + tally delta es := by
  induction ht with
  | nil => simp [tally]
  | @cons x y e es ha he ht ih =>
    have hs := hstep e x
    simp only [tally]
    omega

theorem trace_nonnegative {allowed : Event → Prop} {x y : State} {es : List Event}
    (ht : Trace allowed x es y) (hx : Nonnegative x) : Nonnegative y := by
  induction ht with
  | nil => exact hx
  | cons ha he ht ih => exact ih (step_nonnegative _ _ he)

theorem trace_material {allowed : Event → Prop} {x y : State} {es : List Event}
    (ht : Trace allowed x es y) : material y = material x := by
  induction ht with
  | nil => rfl
  | cons ha he ht ih => rw [ih, material_step]

theorem trace_available {x y : State} {es : List Event}
    (ht : Trace bare x es y) : available y ≤ available x := by
  induction ht with
  | nil => exact Int.le_refl _
  | cons ha he ht ih => exact Int.le_trans ih (bare_available_step _ _ ha)

theorem no_two_inputs (x : State) (h : Nonnegative x) (hv : available x ≤ 1) :
    ¬ (1 ≤ x.r ∧ 1 ≤ x.f) := by
  simp only [Nonnegative] at h
  simp only [available] at hv
  omega

def operation : State := { a := 1, cf := 1, yg := 1 }

theorem bare_no_later_construction {y : State} {es : List Event}
    (ht : Trace bare operation es y) :
    ¬ Enabled .formA y ∧ ¬ Enabled .copyA y ∧ ¬ Enabled .fabricateG y := by
  have hn := trace_nonnegative ht (by simp [Nonnegative, operation])
  have hv := trace_available ht
  have hrf := no_two_inputs y hn (by simpa [operation, available] using hv)
  simp only [Enabled, AtLeast, input]
  constructor
  · intro h; exact hrf ⟨h.2.1, h.2.2.2.2.2.2.1⟩
  constructor
  · intro h; exact hrf ⟨h.2.1, h.2.2.2.2.2.2.1⟩
  · intro h; exact hrf ⟨h.2.1, h.2.2.2.2.2.2.1⟩

theorem minimum_repeated_turnover_captures
    {allowed : Event → Prop} {x y : State} {es : List Event}
    (ht : Trace allowed x es y)
    (hw : work y = work x) (ha : y.a = x.a) (hg : gates y = gates x)
    (n : Int) (hAw : n ≤ tally aWear es) (hGw : n ≤ tally gWear es)
    (hCw : n ≤ tally cWear es) (hYw : n ≤ tally yWear es) :
    6*n ≤ tally capture es := by
  have hwork := trace_change work (fun e => capture e - loss e)
    (fun e s => by dsimp only; have h := work_step e s; omega) ht
  have ha' := trace_change (fun s => s.a) (fun e => aBirth e - aWear e)
    (fun e s => by dsimp only; have h := a_step e s; omega) ht
  have hg' := trace_change gates (fun e => gBirth e - gWear e)
    (fun e s => by dsimp only; have h := g_step e s; omega) ht
  rw [tally_sub] at hwork ha' hg'
  have hloss : tally loss es = tally leakage es + tally aBirth es +
      tally gBirth es + tally aWear es + tally gWear es +
      tally cWear es + tally yWear es := by
    change tally (fun e => leakage e + aBirth e + gBirth e + aWear e +
      gWear e + cWear e + yWear e) es = _
    repeat rw [tally_add]
  have hn := tally_nonnegative leakage (by intro e; cases e <;> decide) es
  dsimp only at ha' hg'
  omega

theorem minimum_full_turnover_captures
    {allowed : Event → Prop} {x y : State} {es : List Event}
    (ht : Trace allowed x es y)
    (hw : work y = work x) (ha : y.a = x.a) (hg : gates y = gates x)
    (hAw : 1 ≤ tally aWear es) (hGw : 1 ≤ tally gWear es)
    (hCw : 1 ≤ tally cWear es) (hYw : 1 ≤ tally yWear es) :
    6 ≤ tally capture es := by
  simpa using minimum_repeated_turnover_captures ht hw ha hg 1 hAw hGw hCw hYw

end RenewalLedger

#print axioms RenewalLedger.material_step
#print axioms RenewalLedger.work_step
#print axioms RenewalLedger.bare_no_later_construction
#print axioms RenewalLedger.minimum_repeated_turnover_captures
#print axioms RenewalLedger.minimum_full_turnover_captures
