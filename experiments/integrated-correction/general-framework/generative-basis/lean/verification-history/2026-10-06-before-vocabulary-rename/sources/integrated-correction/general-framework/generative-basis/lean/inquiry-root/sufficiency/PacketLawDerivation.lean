import NativePacketProcess
import OnePacketAdmissibility

/-!
# Deriving the one-packet probe law from the existing native port

The raw inversion/access coordinates produce exactly three transfer-response
profiles. They are not three independently installed target laws. Both blocked
representatives remain admitted. The quotient concerns probe responses; native
readings additionally retain the sensor parity and phase.

Completed native activity determines the abstract packet consumption, retained
target and calibrated probe observation. Phase alignment uses actual rotations.
Native interface, source and receipt failures remain distinct; a hypothetical
macro denial after exhaustion is not identified with native completion.
The alignment schedule uses the comparison's already-known common phase; its
acquisition is not derived here. Nor is every permissive macro `control o`
identified with an available native command. This is the probe-law interface.

The native port's interaction and accounting recipe remains the identified
source law. Deriving this effective law does not derive fundamental dynamics,
physical calibration or a uniquely necessary generative ontology.
-/

namespace Generative.InquirySufficiency.PacketLawDerivation

open OnePacketQuestions OnePacketAdmissibility

abbrev Native := Generative.NativePacketProcess.State

/-- The two raw coordinates retain all four native configurations. -/
def targetOf (tau blocked : Bool) : Target :=
  match blocked with
  | true => .C
  | false => match tau with
    | false => .A
    | true => .B

def representative : Target → Bool × Bool
  | .A => (false, false)
  | .B => (true, false)
  | .C => (false, true)

theorem every_target_has_raw_representative (target : Target) :
    targetOf (representative target).1 (representative target).2 = target := by
  cases target <;> rfl

theorem blocked_representatives_retained :
    targetOf false true = .C ∧ targetOf true true = .C := ⟨rfl, rfl⟩

/-- A profile is the outcome of the native gate at either learned output. -/
def profile (tau blocked : Bool) : Bool × Bool :=
  (NativePacketProcess.arrivalAt false tau blocked,
    NativePacketProcess.arrivalAt true tau blocked)

theorem raw_profiles :
    profile false false = (false, true) ∧
    profile true false = (true, false) ∧
    profile false true = (false, false) ∧
    profile true true = (false, false) := ⟨rfl, rfl, rfl, rfl⟩

/-- Exactly the three represented classes, preserving both blocked cases. -/
theorem profile_equal_iff_target_equal (tau blocked otherTau otherBlocked : Bool) :
    profile tau blocked = profile otherTau otherBlocked ↔
      targetOf tau blocked = targetOf otherTau otherBlocked := by
  cases tau <;> cases blocked <;> cases otherTau <;> cases otherBlocked <;>
    constructor <;> intro same
  all_goals solve
    | rfl
    | cases same

/-- The macro response follows from the native transfer gate, with the probe
chosen by actual learned output. No A/B/C response table is a proof premise. -/
theorem native_gate_is_macro_receipt (tau blocked output : Bool) :
    (if NativePacketProcess.arrivalAt output tau blocked then positive else negative) =
      receipt (start (targetOf tau blocked)) (test output) := by
  cases tau <;> cases blocked <;> cases output <;> rfl

def sensorParity (s : Native) : Bool := s.tau ^^ s.sigma

/-- Ordinary readings retain sensor parity; a transfer-profile quotient alone
does not erase it or supply its calibration to a learner. -/
theorem native_read_uses_parity (s : Native) :
    NativePacketProcess.readBit s = (NativePacketProcess.output s.phase ^^ sensorParity s) := by
  unfold NativePacketProcess.readBit sensorParity
  cases NativePacketProcess.output s.phase <;> cases s.tau <;> cases s.sigma <;> rfl

theorem same_phase_and_parity_same_reading (s t : Native)
    (phase : s.phase = t.phase) (parity : sensorParity s = sensorParity t) :
    NativePacketProcess.readBit s = NativePacketProcess.readBit t := by
  rw [native_read_uses_parity, native_read_uses_parity, phase, parity]

/-- Exactly when the acquired bit itself is a calibrated arrival report. -/
theorem native_receipt_calibrated_iff (s : Native) :
    NativePacketProcess.receiptBit s = NativePacketProcess.arrival s ↔ s.receiptFlip = false := by
  unfold NativePacketProcess.receiptBit
  cases NativePacketProcess.arrival s <;> cases s.receiptFlip <;>
    constructor <;> intro same
  all_goals solve | rfl | cases same

theorem inverted_receipt_differs (s : Native) (inverted : s.receiptFlip = true) :
    NativePacketProcess.receiptBit s ≠ NativePacketProcess.arrival s := by
  intro same
  have zero := (native_receipt_calibrated_iff s).mp same
  exact Bool.noConfusion (inverted.symm.trans zero)

/-- This projection is intended for the exact zero-or-ten source domain. It
does not identify a larger source with one packet. -/
def onePacketProjection (s : Native) : State :=
  ⟨targetOf s.tau s.blocked, Nat.beq s.source 10⟩

theorem projection_at_one_packet (s : Native) (source : s.source = 10) :
    onePacketProjection s = start (targetOf s.tau s.blocked) := by
  unfold onePacketProjection start
  rw [source]
  rfl

theorem projection_at_exhaustion (s : Native) (source : s.source = 0) :
    onePacketProjection s = spent (targetOf s.tau s.blocked) := by
  unfold onePacketProjection spent
  rw [source]
  rfl

/-- The old six-state carrier must not silently collapse two available packets
to one. The projection expressly requires its declared source domain. -/
theorem two_packet_state_outside_projection (s : Native) (source : s.source = 20) :
    (onePacketProjection s).packet = false ∧ 10 ≤ s.source := by
  unfold onePacketProjection
  rw [source]
  exact ⟨rfl, by decide⟩

/-- The native three-cycle supplies the finite alignment schedule. The schedule
still has to be executed under the native command guards below. -/
def alignmentCount : NativePacketProcess.Phase → Bool → Nat
  | .p0, false => 0
  | .p1, false => 0
  | .p2, false => 1
  | .p0, true => 2
  | .p1, true => 1
  | .p2, true => 0

def phaseAfter : Nat → NativePacketProcess.Phase → NativePacketProcess.Phase
  | 0, phase => phase
  | count + 1, phase => phaseAfter count (NativePacketProcess.nextPhase phase)

theorem alignment_at_most_two (phase : NativePacketProcess.Phase) (desired : Bool) :
    alignmentCount phase desired ≤ 2 := by
  cases phase <;> cases desired <;> decide

theorem alignment_reaches_requested_output (phase : NativePacketProcess.Phase) (desired : Bool) :
    NativePacketProcess.output (phaseAfter (alignmentCount phase desired) phase) = desired := by
  cases phase <;> cases desired <;> rfl

/-- The endpoint computed by the native paid `.a` operation. -/
def rotateOnce (s : Native) : Native :=
  { NativePacketProcess.debit s with phase := NativePacketProcess.nextPhase s.phase }

def rotations : Nat → Native → Native
  | 0, s => s
  | count + 1, s => rotations count (rotateOnce s)

def rotationEvents : Nat → List NativePacketProcess.Command
  | 0 => []
  | count + 1 => .a :: rotationEvents count

def RotationsReady : Nat → Native → Prop
  | 0, _ => True
  | count + 1, s => NativePacketProcess.Payable s ∧ RotationsReady count (rotateOnce s)

theorem zero_sub_constructive (n : Nat) : 0 - n = 0 := Nat.zero_sub n

theorem sub_sub_constructive (n m k : Nat) : n - m - k = n - (m + k) := by
  induction m generalizing n with
  | zero => rw [Nat.zero_add]; rfl
  | succ m ih =>
    cases n with
    | zero => rw [Nat.zero_sub, Nat.zero_sub, Nat.zero_sub]
    | succ n =>
      rw [Nat.succ_add, Nat.succ_sub_succ, Nat.succ_sub_succ]
      exact ih n

theorem le_sub_from_sum (n k m : Nat) (funded : n + k ≤ m) : n ≤ m - k := by
  induction k generalizing m with
  | zero => exact funded
  | succ k ih =>
    cases m with
    | zero => exact False.elim (Nat.not_succ_le_zero _ funded)
    | succ m =>
      rw [Nat.succ_sub_succ]
      exact ih m (Nat.le_of_succ_le_succ funded)

theorem sub_add_cancel_constructive (m k : Nat) (bound : k ≤ m) : (m - k) + k = m := by
  induction k generalizing m with
  | zero => rfl
  | succ k ih =>
    cases m with
    | zero => exact False.elim (Nat.not_succ_le_zero _ bound)
    | succ m =>
      rw [Nat.succ_sub_succ]
      exact congrArg Nat.succ (ih m (Nat.le_of_succ_le_succ bound))

theorem sum_le_from_remainder (n k m : Nat) (spent : k ≤ m) (remaining : n ≤ m - k) :
    n + k ≤ m := by
  have total := Nat.add_le_add_right remaining k
  rw [sub_add_cancel_constructive m k spent] at total
  exact total

theorem rotations_ready_implies_budget (count : Nat) (s : Native)
    (ready : RotationsReady count s) : count * NativePacketProcess.bill s ≤ s.fuel := by
  induction count generalizing s with
  | zero => rw [Nat.zero_mul]; exact Nat.zero_le _
  | succ count ih =>
    have remaining := ih (rotateOnce s) ready.2
    change count * NativePacketProcess.bill s ≤ s.fuel - NativePacketProcess.bill s at remaining
    rw [Nat.succ_mul]
    exact sum_le_from_remainder _ _ _ ready.1.2 remaining

theorem rotation_fields (count : Nat) (s : Native) :
    (rotations count s).phase = phaseAfter count s.phase ∧
    (rotations count s).tau = s.tau ∧
    (rotations count s).blocked = s.blocked ∧
    (rotations count s).receiptFlip = s.receiptFlip ∧
    (rotations count s).source = s.source ∧
    NativePacketProcess.peak (rotations count s) = NativePacketProcess.peak s ∧
    NativePacketProcess.bill (rotations count s) = NativePacketProcess.bill s ∧
    (rotations count s).capacity = s.capacity := by
  induction count generalizing s with
  | zero => exact ⟨rfl, rfl, rfl, rfl, rfl, rfl, rfl, rfl⟩
  | succ count ih => exact ih (rotateOnce s)

theorem rotation_fuel (count : Nat) (s : Native) :
    (rotations count s).fuel = s.fuel - count * NativePacketProcess.bill s := by
  induction count generalizing s with
  | zero => rw [Nat.zero_mul]; rfl
  | succ count ih =>
    rw [rotations, ih]
    change s.fuel - NativePacketProcess.bill s - count * NativePacketProcess.bill s = _
    rw [Nat.succ_mul]
    exact (sub_sub_constructive _ _ _).trans
      (congrArg (fun spent => s.fuel - spent) (Nat.add_comm _ _))

/-- Funding and capacity are sufficient for every prefix, not a promised final
path. The source is never used to pay these preceding alignment commands. -/
theorem rotations_ready_from_budget (count : Nat) (s : Native)
    (capacity : NativePacketProcess.peak s ≤ s.capacity)
    (funding : count * NativePacketProcess.bill s ≤ s.fuel) : RotationsReady count s := by
  induction count generalizing s with
  | zero => exact True.intro
  | succ count ih =>
    have total := funding
    rw [Nat.succ_mul] at total
    have current : NativePacketProcess.bill s ≤ s.fuel :=
      Nat.le_trans (Nat.le_add_left _ _) total
    refine ⟨⟨capacity, current⟩, ih (rotateOnce s) capacity ?_⟩
    change count * NativePacketProcess.bill s ≤ s.fuel - NativePacketProcess.bill s
    exact le_sub_from_sum _ _ _ total

theorem rotations_have_native_trace (count : Nat) (s : Native)
    (ready : RotationsReady count s) :
    Generative.Trace NativePacketProcess.process s (rotationEvents count) (rotations count s) := by
  induction count generalizing s with
  | zero => exact .nil s
  | succ count ih =>
    exact .cons ⟨.silent, NativePacketProcess.a_complete s ready.1⟩ (ih _ ready.2)

def alignedState (desired : Bool) (s : Native) : Native := rotations (alignmentCount s.phase desired) s

def alignedEvents (desired : Bool) (s : Native) : List NativePacketProcess.Command :=
  rotationEvents (alignmentCount s.phase desired) ++ [.probe]

theorem common_phase_same_schedule (desired : Bool) (left right : Native)
    (phase : left.phase = right.phase) : alignedEvents desired left = alignedEvents desired right :=
  congrArg (fun phase => rotationEvents (alignmentCount phase desired) ++ [.probe]) phase

/-- Exact direct native bills for alignment, probe dispatch, and later receipt.
The final receipt may use only an actual arrival, after source consumption.
This feasibility condition reads phase and actual arrival; it is not an
installed observable admission policy or a granted predictor of the outcome. -/
def AlignmentGuard (desired : Bool) (s : Native) : Prop :=
  NativePacketProcess.peak s ≤ s.capacity ∧
  (alignmentCount s.phase desired + 1) * NativePacketProcess.bill s ≤ s.fuel ∧
  10 ≤ s.source ∧
  NativePacketProcess.bill s ≤
    s.fuel - (alignmentCount s.phase desired + 1) * NativePacketProcess.bill s +
      NativePacketProcess.gain (alignedState desired s)

theorem alignment_guard_supplies_native_guards (desired : Bool) (s : Native)
    (guard : AlignmentGuard desired s) :
    RotationsReady (alignmentCount s.phase desired) s ∧
      NativePacketProcess.ProbeReady (alignedState desired s) := by
  have fields := rotation_fields (alignmentCount s.phase desired) s
  have funds := rotation_fuel (alignmentCount s.phase desired) s
  obtain ⟨capacity, funding, source, receipt⟩ := guard
  have prior : alignmentCount s.phase desired * NativePacketProcess.bill s ≤ s.fuel := by
    rw [Nat.succ_mul] at funding
    exact Nat.le_trans (Nat.le_add_right _ _) funding
  refine ⟨rotations_ready_from_budget _ s capacity prior, ?_⟩
  apply (NativePacketProcess.probeReady_exact _).mpr
  change NativePacketProcess.peak (rotations _ s) ≤ (rotations _ s).capacity ∧
    NativePacketProcess.bill (rotations _ s) ≤ (rotations _ s).fuel ∧
    10 ≤ (rotations _ s).source ∧
    NativePacketProcess.bill (rotations _ s) ≤
      (rotations _ s).fuel - NativePacketProcess.bill (rotations _ s) +
        NativePacketProcess.gain (alignedState desired s)
  rw [fields.2.2.2.2.2.1, fields.2.2.2.2.2.2.1, fields.2.2.2.2.2.2.2,
    fields.2.2.2.2.1, funds]
  refine ⟨capacity, ?_, source, ?_⟩
  · rw [Nat.succ_mul] at funding
    exact le_sub_from_sum _ _ _ ((Nat.add_comm _ _).symm ▸ funding)
  · rw [Nat.succ_mul] at receipt
    rw [sub_sub_constructive]
    exact receipt

theorem alignment_guard_iff_native_guards (desired : Bool) (s : Native) :
    AlignmentGuard desired s ↔
      RotationsReady (alignmentCount s.phase desired) s ∧
        NativePacketProcess.ProbeReady (alignedState desired s) := by
  constructor
  · exact alignment_guard_supplies_native_guards desired s
  · rintro ⟨rotationsReady, probeReady⟩
    have fields := rotation_fields (alignmentCount s.phase desired) s
    have funds := rotation_fuel (alignmentCount s.phase desired) s
    have exactProbe := (NativePacketProcess.probeReady_exact (alignedState desired s)).mp probeReady
    change NativePacketProcess.peak (rotations _ s) ≤ (rotations _ s).capacity ∧
      NativePacketProcess.bill (rotations _ s) ≤ (rotations _ s).fuel ∧
      10 ≤ (rotations _ s).source ∧
      NativePacketProcess.bill (rotations _ s) ≤
        (rotations _ s).fuel - NativePacketProcess.bill (rotations _ s) +
          NativePacketProcess.gain (alignedState desired s) at exactProbe
    rw [fields.2.2.2.2.2.1, fields.2.2.2.2.2.2.1, fields.2.2.2.2.2.2.2,
      fields.2.2.2.2.1, funds] at exactProbe
    have prior := rotations_ready_implies_budget _ s rotationsReady
    refine ⟨exactProbe.1, ?_, exactProbe.2.2.1, ?_⟩
    · have total := sum_le_from_remainder _ _ _ prior exactProbe.2.1
      rw [Nat.add_comm] at total
      rw [Nat.succ_mul]
      exact total
    · have receipt := exactProbe.2.2.2
      rw [sub_sub_constructive] at receipt
      rw [Nat.succ_mul]
      exact receipt

def report (bit : Bool) : Fin 3 := if bit then positive else negative

/-- Exact observation correspondence, with the native receipt calibration named.
This mathematical condition does not install a calibration reader. -/
theorem calibrated_receipt_matches_macro (s : Native) (calibrated : s.receiptFlip = false) :
    report (NativePacketProcess.receiptBit s) =
      receipt (start (targetOf s.tau s.blocked)) (test (NativePacketProcess.output s.phase)) := by
  rw [(native_receipt_calibrated_iff s).mpr calibrated]
  exact native_gate_is_macro_receipt s.tau s.blocked (NativePacketProcess.output s.phase)

/-- Projection of an actual completed native probe, not a selected favorable
endpoint. The native completion itself entails all sequential guards. -/
theorem completed_probe_projects (s t : Native) (bit : Bool)
    (source : s.source = 10) (calibrated : s.receiptFlip = false)
    (completed : NativePacketProcess.execute s .probe =
      .complete t (.receipt bit)) :
    NativePacketProcess.ProbeReady s ∧
      process.step (onePacketProjection s) (test (NativePacketProcess.output s.phase))
        (onePacketProjection t) ∧
      report bit = sense (onePacketProjection s) (test (NativePacketProcess.output s.phase))
        (onePacketProjection t) ∧
      t.source = 0 ∧ targetOf t.tau t.blocked = targetOf s.tau s.blocked := by
  obtain ⟨ready, endpoint, observation⟩ :=
    (NativePacketProcess.probe_complete_iff s t (.receipt bit)).mp completed
  subst t
  have bitEq : bit = NativePacketProcess.receiptBit s :=
    NativePacketProcess.Observation.receipt.inj observation
  have exhausted : (NativePacketProcess.probeFinal s).source = 0 := by
    change s.source - 10 = 0
    rw [source]
  refine ⟨ready, ?_, ?_, exhausted, rfl⟩
  · rw [projection_at_one_packet s source,
      projection_at_exhaustion (NativePacketProcess.probeFinal s) exhausted]
    change spent (targetOf s.tau s.blocked) =
      advance (start (targetOf s.tau s.blocked)) (test (NativePacketProcess.output s.phase))
    cases NativePacketProcess.output s.phase <;> rfl
  · rw [bitEq, projection_at_one_packet s source]
    exact calibrated_receipt_matches_macro s calibrated

/-- Conversely, the independently calculated native guard supplies the entire
completed implementation with its actual successor and acquired receipt. -/
theorem native_guard_realizes_macro_probe (s : Native)
    (source : s.source = 10) (calibrated : s.receiptFlip = false)
    (ready : NativePacketProcess.ProbeReady s) :
    ∃ t bit, NativePacketProcess.execute s .probe = .complete t (.receipt bit) ∧
      process.step (onePacketProjection s) (test (NativePacketProcess.output s.phase))
        (onePacketProjection t) ∧
      report bit = sense (onePacketProjection s) (test (NativePacketProcess.output s.phase))
        (onePacketProjection t) := by
  have actual := NativePacketProcess.probe_complete s ready
  have projected := completed_probe_projects s _ _ source calibrated actual
  exact ⟨NativePacketProcess.probeFinal s, NativePacketProcess.receiptBit s,
    actual, projected.2.1, projected.2.2.1⟩

/-- The prep phase is reached by actual paid rotations; the source and target
coordinates are retained throughout those operations. -/
theorem aligned_state_properties (desired : Bool) (s : Native) :
    NativePacketProcess.output (alignedState desired s).phase = desired ∧
      onePacketProjection (alignedState desired s) = onePacketProjection s ∧
      (alignedState desired s).source = s.source ∧
      (alignedState desired s).receiptFlip = s.receiptFlip ∧
      targetOf (alignedState desired s).tau (alignedState desired s).blocked =
        targetOf s.tau s.blocked := by
  have fields := rotation_fields (alignmentCount s.phase desired) s
  refine ⟨?_, ?_, fields.2.2.2.2.1, fields.2.2.2.1, ?_⟩
  · change NativePacketProcess.output (rotations _ s).phase = desired
    rw [fields.1]
    exact alignment_reaches_requested_output s.phase desired
  · unfold alignedState onePacketProjection
    rw [fields.2.1, fields.2.2.1, fields.2.2.2.2.1]
  · unfold alignedState
    rw [fields.2.1, fields.2.2.1]

/-- Either macro probe has an actual native realization from every admitted
representative, with at most two paid rotations followed by the completed probe.
No reset, restored packet or free movement is inserted at the interface. -/
theorem aligned_probe_realizes_macro (desired : Bool) (s : Native)
    (source : s.source = 10) (calibrated : s.receiptFlip = false)
    (guard : AlignmentGuard desired s) :
    let prepared := alignedState desired s
    let final := NativePacketProcess.probeFinal prepared
    Generative.Trace NativePacketProcess.process s (alignedEvents desired s) final ∧
      NativePacketProcess.execute prepared .probe =
        .complete final (.receipt (NativePacketProcess.receiptBit prepared)) ∧
      process.step (onePacketProjection s) (test desired) (onePacketProjection final) ∧
      report (NativePacketProcess.receiptBit prepared) =
        sense (onePacketProjection s) (test desired) (onePacketProjection final) ∧
      final.source = 0 ∧ targetOf final.tau final.blocked = targetOf s.tau s.blocked := by
  obtain ⟨rotationsReady, probeReady⟩ := alignment_guard_supplies_native_guards desired s guard
  have properties := aligned_state_properties desired s
  have actual := NativePacketProcess.probe_complete (alignedState desired s) probeReady
  have projected := completed_probe_projects (alignedState desired s) _ _
    (properties.2.2.1.trans source) (properties.2.2.2.1.trans calibrated) actual
  have nativeTrace : Generative.Trace NativePacketProcess.process s (alignedEvents desired s)
      (NativePacketProcess.probeFinal (alignedState desired s)) := by
    apply Generative.trace_append_iff.mpr
    exact ⟨alignedState desired s,
      rotations_have_native_trace _ s rotationsReady,
      .cons ⟨_, actual⟩ (.nil _)⟩
  refine ⟨nativeTrace, actual, ?_, ?_, projected.2.2.2.1,
    projected.2.2.2.2.trans properties.2.2.2.2⟩
  · rw [properties.1, properties.2.1] at projected
    exact projected.2.1
  · rw [properties.1, properties.2.1] at projected
    exact projected.2.2.1

/-- After exhaustion the old macro denial is extra permissive access. Native
execution cannot complete another probe, irrespective of available fuel. -/
theorem exhausted_native_probe_cannot_complete (s : Native) (source : s.source = 0)
    (t : Native) (observation : NativePacketProcess.Observation) :
    ¬ NativePacketProcess.execute s .probe = .complete t observation := by
  intro completed
  have available := ((NativePacketProcess.probe_complete_iff s t observation).mp completed).1.2.1
  rw [source] at available
  exact Nat.not_succ_le_zero _ available

theorem macro_denial_is_not_native_completion (s : Native) (source : s.source = 0)
    (which : Bool) :
    Enabled process (onePacketProjection s) (test which) ∧
      receipt (onePacketProjection s) (test which) = denied ∧
      ∀ t observation, ¬ NativePacketProcess.execute s .probe = .complete t observation := by
  refine ⟨all_actions_enabled _ _, ?_, exhausted_native_probe_cannot_complete s source⟩
  rw [projection_at_exhaustion s source]
  cases which <;> rfl

/-- A real completed two-packet attempt still leaves native source for another
attempt. Its later funding remains separate. This excludes extending the
one-packet projection to arbitrary positive source stocks. -/
theorem two_packet_completion_retains_source (s t : Native)
    (observation : NativePacketProcess.Observation) (source : s.source = 20)
    (completed : NativePacketProcess.execute s .probe = .complete t observation) :
    t.source = 10 := by
  obtain ⟨_, endpoint, _⟩ := (NativePacketProcess.probe_complete_iff s t observation).mp completed
  subst t
  change s.source - 10 = 10
  rw [source]

end Generative.InquirySufficiency.PacketLawDerivation

#print axioms Generative.InquirySufficiency.PacketLawDerivation.Native
#print axioms Generative.InquirySufficiency.PacketLawDerivation.targetOf
#print axioms Generative.InquirySufficiency.PacketLawDerivation.representative
#print axioms Generative.InquirySufficiency.PacketLawDerivation.every_target_has_raw_representative
#print axioms Generative.InquirySufficiency.PacketLawDerivation.blocked_representatives_retained
#print axioms Generative.InquirySufficiency.PacketLawDerivation.profile
#print axioms Generative.InquirySufficiency.PacketLawDerivation.raw_profiles
#print axioms Generative.InquirySufficiency.PacketLawDerivation.profile_equal_iff_target_equal
#print axioms Generative.InquirySufficiency.PacketLawDerivation.native_gate_is_macro_receipt
#print axioms Generative.InquirySufficiency.PacketLawDerivation.sensorParity
#print axioms Generative.InquirySufficiency.PacketLawDerivation.native_read_uses_parity
#print axioms Generative.InquirySufficiency.PacketLawDerivation.same_phase_and_parity_same_reading
#print axioms Generative.InquirySufficiency.PacketLawDerivation.native_receipt_calibrated_iff
#print axioms Generative.InquirySufficiency.PacketLawDerivation.inverted_receipt_differs
#print axioms Generative.InquirySufficiency.PacketLawDerivation.onePacketProjection
#print axioms Generative.InquirySufficiency.PacketLawDerivation.projection_at_one_packet
#print axioms Generative.InquirySufficiency.PacketLawDerivation.projection_at_exhaustion
#print axioms Generative.InquirySufficiency.PacketLawDerivation.two_packet_state_outside_projection
#print axioms Generative.InquirySufficiency.PacketLawDerivation.alignmentCount
#print axioms Generative.InquirySufficiency.PacketLawDerivation.phaseAfter
#print axioms Generative.InquirySufficiency.PacketLawDerivation.alignment_at_most_two
#print axioms Generative.InquirySufficiency.PacketLawDerivation.alignment_reaches_requested_output
#print axioms Generative.InquirySufficiency.PacketLawDerivation.rotateOnce
#print axioms Generative.InquirySufficiency.PacketLawDerivation.rotations
#print axioms Generative.InquirySufficiency.PacketLawDerivation.rotationEvents
#print axioms Generative.InquirySufficiency.PacketLawDerivation.RotationsReady
#print axioms Generative.InquirySufficiency.PacketLawDerivation.rotation_fields
#print axioms Generative.InquirySufficiency.PacketLawDerivation.rotation_fuel
#print axioms Generative.InquirySufficiency.PacketLawDerivation.rotations_ready_from_budget
#print axioms Generative.InquirySufficiency.PacketLawDerivation.rotations_have_native_trace
#print axioms Generative.InquirySufficiency.PacketLawDerivation.alignedState
#print axioms Generative.InquirySufficiency.PacketLawDerivation.alignedEvents
#print axioms Generative.InquirySufficiency.PacketLawDerivation.AlignmentGuard
#print axioms Generative.InquirySufficiency.PacketLawDerivation.alignment_guard_supplies_native_guards
#print axioms Generative.InquirySufficiency.PacketLawDerivation.zero_sub_constructive
#print axioms Generative.InquirySufficiency.PacketLawDerivation.sub_sub_constructive
#print axioms Generative.InquirySufficiency.PacketLawDerivation.le_sub_from_sum
#print axioms Generative.InquirySufficiency.PacketLawDerivation.report
#print axioms Generative.InquirySufficiency.PacketLawDerivation.calibrated_receipt_matches_macro
#print axioms Generative.InquirySufficiency.PacketLawDerivation.completed_probe_projects
#print axioms Generative.InquirySufficiency.PacketLawDerivation.native_guard_realizes_macro_probe
#print axioms Generative.InquirySufficiency.PacketLawDerivation.aligned_state_properties
#print axioms Generative.InquirySufficiency.PacketLawDerivation.aligned_probe_realizes_macro
#print axioms Generative.InquirySufficiency.PacketLawDerivation.exhausted_native_probe_cannot_complete
#print axioms Generative.InquirySufficiency.PacketLawDerivation.macro_denial_is_not_native_completion
#print axioms Generative.InquirySufficiency.PacketLawDerivation.sub_add_cancel_constructive
#print axioms Generative.InquirySufficiency.PacketLawDerivation.sum_le_from_remainder
#print axioms Generative.InquirySufficiency.PacketLawDerivation.rotations_ready_implies_budget
#print axioms Generative.InquirySufficiency.PacketLawDerivation.alignment_guard_iff_native_guards
#print axioms Generative.InquirySufficiency.PacketLawDerivation.common_phase_same_schedule
#print axioms Generative.InquirySufficiency.PacketLawDerivation.two_packet_completion_retains_source
