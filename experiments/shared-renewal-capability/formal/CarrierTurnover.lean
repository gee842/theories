import ReserveTurnover

/-!
Original-carrier observations for the concrete forward event vocabulary.
The observer forgets material-slot assignment and bond consistency; it is an
overapproximation used for necessary accounting bounds, not a kinetic model.
No original can be created by birth or recovered by material recycling.
-/
namespace CarrierTurnover

open TypedRenewal

inductive Role where | a | c | g | y
  deriving DecidableEq, Repr

/- A bound G and its bound Y are two distinct original carriers. -/
inductive Form where
  | a (k : Kind) | c | cf | y | g (k : Kind) | gf (k : Kind)
  | ygGate (k : Kind) | ygY (k : Kind)
  deriving DecidableEq, Repr

def role : Form → Role
  | .a _ => .a
  | .c | .cf => .c
  | .g _ | .gf _ | .ygGate _ => .g
  | .y | .ygY _ => .y

def wear (r : Role) (e : Event) : Int :=
  match r with
  | .a => aWear e | .c => cWear e | .g => gWear e | .y => yWear e

/- None records a permanently lost original, not an empty material slot. Its
material may subsequently be recycled, reused, rebound and worn again. -/
abbrev Tag := Option Form
abbrev Marks := Role → Tag

/- Explicit local event table. Unchanged means this original was not changed
by the chosen reaction assignment (including retained catalysts). Birth and
recycling events have no constructor introducing or resurrecting originals.
-/
inductive Update : Event → Tag → Tag → Prop where
  | unchanged (e : Event) (p : Tag) : Update e p p
  | cWear : Update .cWear (some .c) none
  | yWear : Update .yWear (some .y) none
  | capture : Update .capture (some .c) (some .cf)
  | aWear (k) : Update (.aWear k) (some (.a k)) none
  | gWear (k) : Update (.gWear k) (some (.g k)) none
  | bindF (k) : Update (.bindF k) (some (.g k)) (some (.gf k))
  | unbindF (k) : Update (.unbindF k) (some (.gf k)) (some (.g k))
  | boundLeak (k) : Update (.boundLeak k) (some (.gf k)) (some (.g k))
  | gfWear (k) : Update (.gfWear k) (some (.gf k)) none
  | bindYGate (k) : Update (.bindY k) (some (.g k)) (some (.ygGate k))
  | bindYY (k) : Update (.bindY k) (some .y) (some (.ygY k))
  | unbindYGate (k) : Update (.unbindY k) (some (.ygGate k)) (some (.g k))
  | unbindYY (k) : Update (.unbindY k) (some (.ygY k)) (some .y)
  | ygGWearGate (k) : Update (.ygGWear k) (some (.ygGate k)) none
  | ygGWearY (k) : Update (.ygGWear k) (some (.ygY k)) (some .y)
  | ygYWearGate (k) : Update (.ygYWear k) (some (.ygGate k)) (some (.g k))
  | ygYWearY (k) : Update (.ygYWear k) (some (.ygY k)) none
  | cfLeak : Update .cfLeak (some .cf) (some .c)
  | cfWear : Update .cfWear (some .cf) none
  | accessRepair : Update .accessRepair (some .cf) (some .c)
  | accessForm (k) : Update (.accessForm k) (some .cf) (some .c)
  | accessFabricate (k) : Update (.accessFabricate k) (some .cf) (some .c)

def Consistent (p : Marks) : Prop :=
  ∀ r f, p r = some f → role f = r

/- This checks individual presence, not injective allocation of tags to
particles or a pairing of the two original YG constituents. -/
def copies (x : State) : Form → Int
  | .a .zero => x.a0 | .a .one => x.a1
  | .c => x.c | .cf => x.cf | .y => x.y
  | .g .zero => x.g0 | .g .one => x.g1
  | .gf .zero => x.gf0 | .gf .one => x.gf1
  | .ygGate .zero | .ygY .zero => x.yg0
  | .ygGate .one | .ygY .one => x.yg1

def Present (x : State) (p : Marks) : Prop :=
  ∀ r f, p r = some f → 1 ≤ copies x f

def initial (a g : Kind) : Marks
  | .a => some (.a a) | .c => some .cf
  | .g => some (.ygGate g) | .y => some (.ygY g)

def AllGone (p : Marks) : Prop := ∀ r, p r = none

theorem initial_consistent (a g : Kind) : Consistent (initial a g) := by
  intro r f h
  cases r <;> simp [initial] at h <;> subst f <;> rfl

theorem initial_present (a g : Kind) (m : Int) :
    Present (ReserveTurnover.organization a g m) (initial a g) := by
  intro r f h
  cases r <;> simp [initial] at h <;> subst f <;>
    cases a <;> cases g <;>
    simp [copies, ReserveTurnover.organization, operation]

theorem update_gone_permanent {e : Event} {q : Tag}
    (h : Update e none q) : q = none := by
  cases h
  rfl

theorem update_live_role {e : Event} {f f' : Form}
    (h : Update e (some f) (some f')) : role f' = role f := by
  cases h <;> rfl

theorem update_first_loss {e : Event} {f : Form}
    (h : Update e (some f) none) : wear (role f) e = 1 := by
  cases h <;> rfl

theorem wear_nonnegative (r : Role) (e : Event) : 0 ≤ wear r e := by
  cases r <;> cases e <;> simp [wear, aWear, cWear, gWear, yWear,
    eventMap, RenewalLedger.aWear, RenewalLedger.cWear,
    RenewalLedger.gWear, RenewalLedger.yWear]

theorem update_consistent {p q : Marks} {e : Event}
    (hc : Consistent p) (hu : ∀ r, Update e (p r) (q r)) : Consistent q := by
  intro r f hq
  have h := hu r
  rw [hq] at h
  cases hp : p r with
  | none =>
    rw [hp] at h
    have hf := update_gone_permanent h
    contradiction
  | some f0 =>
    rw [hp] at h
    exact (update_live_role h).trans (hc r f0 hp)

def gone : Tag → Int | none => 1 | some _ => 0

theorem update_gone_bound {e : Event} {p q : Tag} {r : Role}
    (hc : ∀ f, p = some f → role f = r) (hu : Update e p q) :
    gone q ≤ gone p + wear r e := by
  have hn := wear_nonnegative r e
  cases p with
  | none =>
    have hq := update_gone_permanent hu
    simp [hq, gone]
    omega
  | some f =>
    cases q with
    | some f' => simpa [gone] using hn
    | none =>
      have hw := update_first_loss hu
      rw [hc f rfl] at hw
      simp [gone, hw]

/- Count-state enabledness and tag updates are both required. Presence is
required at both ends of each event; role consistency is proved by induction.
This remains a permissive observer, not the material-slot lift itself.
-/
inductive MarkedTrace (allowed : Event → Prop) :
    State → Marks → List Event → State → Marks → Prop where
  | nil (x : State) (p : Marks) (hp : Present x p) :
      MarkedTrace allowed x p [] x p
  | cons {x y : State} {p q z : Marks} {e : Event} {es : List Event}
      (ha : allowed e) (he : Enabled e x) (hp : Present x p)
      (hu : ∀ r, Update e (p r) (q r))
      (ht : MarkedTrace allowed (step e x) q es y z) :
      MarkedTrace allowed x p (e :: es) y z

theorem marked_trace_project {allowed : Event → Prop} {x y : State}
    {p q : Marks} {es : List Event} (ht : MarkedTrace allowed x p es y q) :
    Trace allowed x es y := by
  induction ht with
  | nil => exact Trace.nil _
  | cons ha he hp hu ht ih => exact Trace.cons ha he ih

def lost : Marks := fun _ => none

theorem lost_present (x : State) : Present x lost := by
  intro r f h
  simp [lost] at h

/- Once all originals are gone, their marks exclude no subsequently enabled
typed history. In particular, later wear and type changes remain allowed. -/
theorem all_gone_continuation {allowed : Event → Prop} {x y : State}
    {es : List Event} (ht : Trace allowed x es y) :
    MarkedTrace allowed x lost es y lost := by
  induction ht with
  | nil => exact MarkedTrace.nil _ _ (lost_present _)
  | cons ha he ht ih =>
    exact MarkedTrace.cons ha he (lost_present _)
      (fun _ => Update.unchanged _ none) ih

theorem marked_trace_consistent {allowed : Event → Prop} {x y : State}
    {p q : Marks} {es : List Event} (ht : MarkedTrace allowed x p es y q)
    (hc : Consistent p) : Consistent q := by
  induction ht with
  | nil => exact hc
  | cons ha he hp hu ht ih => exact ih (update_consistent hc hu)

theorem marked_trace_gone_permanent {allowed : Event → Prop} {x y : State}
    {p q : Marks} {es : List Event} (ht : MarkedTrace allowed x p es y q)
    (r : Role) (hg : p r = none) : q r = none := by
  induction ht with
  | nil => exact hg
  | cons ha he hp hu ht ih =>
    have h := hu r
    rw [hg] at h
    exact ih (update_gone_permanent h)

theorem marked_trace_gone_bound {allowed : Event → Prop} {x y : State}
    {p q : Marks} {es : List Event} (ht : MarkedTrace allowed x p es y q)
    (hc : Consistent p) (r : Role) :
    gone (q r) ≤ gone (p r) + tally (wear r) es := by
  induction ht with
  | nil => simp [tally]
  | @cons x y p q z e es ha he hp hu ht ih =>
    have hstep := update_gone_bound (fun f hf => hc r f hf) (hu r)
    have htail := ih (update_consistent hc hu)
    simp only [tally]
    omega

theorem original_loss_requires_role_wear
    {allowed : Event → Prop} {x y : State} {a g : Kind}
    {q : Marks} {es : List Event}
    (ht : MarkedTrace allowed x (initial a g) es y q)
    (r : Role) (hg : q r = none) : 1 ≤ tally (wear r) es := by
  have hb := marked_trace_gone_bound ht (initial_consistent a g) r
  rw [hg] at hb
  cases r <;> simpa [initial, gone] using hb

theorem all_original_losses_require_four_wears
    {allowed : Event → Prop} {x y : State} {a g : Kind}
    {q : Marks} {es : List Event}
    (ht : MarkedTrace allowed x (initial a g) es y q) (hg : AllGone q) :
    1 ≤ tally aWear es ∧ 1 ≤ tally cWear es ∧
    1 ≤ tally gWear es ∧ 1 ≤ tally yWear es := by
  exact ⟨original_loss_requires_role_wear ht .a (hg .a),
    original_loss_requires_role_wear ht .c (hg .c),
    original_loss_requires_role_wear ht .g (hg .g),
    original_loss_requires_role_wear ht .y (hg .y)⟩

theorem original_turnover_work_bound
    {allowed : Event → Prop} {x y : State} {a g : Kind}
    {q : Marks} {es : List Event}
    (ht : MarkedTrace allowed x (initial a g) es y q) (hg : AllGone q)
    (ha : totalA y = totalA x) (hgate : gates y = gates x) :
    6 + (work y - work x) ≤ tally capture es := by
  obtain ⟨hA, hC, hG, hY⟩ := all_original_losses_require_four_wears ht hg
  simpa using ReserveTurnover.minimum_captures_with_work_change
    (marked_trace_project ht) ha hgate 1 hA hG hC hY

theorem original_turnover_reserve_bound
    {allowed : Event → Prop} {ai gi af gf : Kind} {m m' : Int}
    {q : Marks} {es : List Event}
    (ht : MarkedTrace allowed (ReserveTurnover.organization ai gi m)
      (initial ai gi) es (ReserveTurnover.organization af gf m') q)
    (hg : AllGone q) : 6 + m' - m ≤ tally capture es := by
  obtain ⟨hA, hC, hG, hY⟩ := all_original_losses_require_four_wears ht hg
  exact ReserveTurnover.one_turnover_reserve_bound
    (marked_trace_project ht) hA hG hC hY

theorem original_turnover_restored_reserve
    {allowed : Event → Prop} {ai gi af gf : Kind} {m m' : Int}
    {q : Marks} {es : List Event}
    (ht : MarkedTrace allowed (ReserveTurnover.organization ai gi m)
      (initial ai gi) es (ReserveTurnover.organization af gf m') q)
    (hg : AllGone q) (hr : m ≤ m') : 6 ≤ tally capture es := by
  have h := original_turnover_reserve_bound ht hg
  omega

end CarrierTurnover

#print axioms CarrierTurnover.update_gone_permanent
#print axioms CarrierTurnover.update_live_role
#print axioms CarrierTurnover.update_first_loss
#print axioms CarrierTurnover.marked_trace_project
#print axioms CarrierTurnover.all_gone_continuation
#print axioms CarrierTurnover.marked_trace_consistent
#print axioms CarrierTurnover.marked_trace_gone_permanent
#print axioms CarrierTurnover.original_loss_requires_role_wear
#print axioms CarrierTurnover.all_original_losses_require_four_wears
#print axioms CarrierTurnover.original_turnover_work_bound
#print axioms CarrierTurnover.original_turnover_reserve_bound
#print axioms CarrierTurnover.original_turnover_restored_reserve
