import TypedRenewal

/-!
Turnover accounting without assuming restoration of inherited work/reserve.
This imports the frozen concrete typed-to-ledger projection, with no rates,
original-carrier tags, stochastic laws or positive reachability assumption.
-/
namespace ReserveTurnover

open TypedRenewal

theorem minimum_captures_with_work_change
    {allowed : Event → Prop} {x y : State} {es : List Event}
    (ht : Trace allowed x es y)
    (ha : totalA y = totalA x) (hg : gates y = gates x)
    (n : Int) (hAw : n ≤ tally aWear es) (hGw : n ≤ tally gWear es)
    (hCw : n ≤ tally cWear es) (hYw : n ≤ tally yWear es) :
    6*n + (work y - work x) ≤ tally capture es := by
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
  simp only [totalA, gates] at ha hg
  change n ≤ tally (fun e => RenewalLedger.aWear (eventMap e)) es at hAw
  change n ≤ tally (fun e => RenewalLedger.gWear (eventMap e)) es at hGw
  change n ≤ tally (fun e => RenewalLedger.cWear (eventMap e)) es at hCw
  change n ≤ tally (fun e => RenewalLedger.yWear (eventMap e)) es at hYw
  change 6*n + (RenewalLedger.work (project y) - RenewalLedger.work (project x)) ≤
    tally (fun e => RenewalLedger.capture (eventMap e)) es
  omega

/- P_ij(m): A_i=CF=YG_j=1, free reserve F=m, all other species zero.
Counts remain integer-valued as in the frozen model; the nonnegative lemma
below supplies the physical-state condition when m >= 0. -/
def organization (a g : Kind) (m : Int) : State :=
  { operation a g with f := m }

theorem organization_nonnegative (a g : Kind) (m : Int) (hm : 0 ≤ m) :
    Nonnegative (organization a g m) := by
  cases a <;> cases g <;> simp [organization, operation, Nonnegative, hm]

theorem organization_work (a g : Kind) (m : Int) :
    work (organization a g m) = 5 + m := by
  cases a <;> cases g <;>
    simp [organization, operation, work, project, RenewalLedger.work,
      RenewalLedger.material, RenewalLedger.packets] <;> omega

theorem organization_totalA (a g : Kind) (m : Int) :
    totalA (organization a g m) = 1 := by
  cases a <;> cases g <;> rfl

theorem organization_gates (a g : Kind) (m : Int) :
    gates (organization a g m) = 1 := by
  cases a <;> cases g <;> rfl

theorem organization_turnover_reserve_bound
    {allowed : Event → Prop} {ai gi af gf : Kind} {m m' : Int} {es : List Event}
    (ht : Trace allowed (organization ai gi m) es (organization af gf m'))
    (n : Int) (hAw : n ≤ tally aWear es) (hGw : n ≤ tally gWear es)
    (hCw : n ≤ tally cWear es) (hYw : n ≤ tally yWear es) :
    6*n + m' - m ≤ tally capture es := by
  have h := minimum_captures_with_work_change ht
    (by rw [organization_totalA, organization_totalA])
    (by rw [organization_gates, organization_gates]) n hAw hGw hCw hYw
  rw [organization_work, organization_work] at h
  omega

theorem one_turnover_reserve_bound
    {allowed : Event → Prop} {ai gi af gf : Kind} {m m' : Int} {es : List Event}
    (ht : Trace allowed (organization ai gi m) es (organization af gf m'))
    (hAw : 1 ≤ tally aWear es) (hGw : 1 ≤ tally gWear es)
    (hCw : 1 ≤ tally cWear es) (hYw : 1 ≤ tally yWear es) :
    6 + m' - m ≤ tally capture es := by
  simpa using organization_turnover_reserve_bound ht 1 hAw hGw hCw hYw

end ReserveTurnover

#print axioms ReserveTurnover.minimum_captures_with_work_change
#print axioms ReserveTurnover.organization_nonnegative
#print axioms ReserveTurnover.organization_work
#print axioms ReserveTurnover.organization_turnover_reserve_bound
#print axioms ReserveTurnover.one_turnover_reserve_bound
