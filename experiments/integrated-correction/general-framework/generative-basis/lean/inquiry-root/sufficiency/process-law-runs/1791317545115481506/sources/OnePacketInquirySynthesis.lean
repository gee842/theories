import OnePacketAdmissibility
import DerivedInquiryCertificates

/-!
# Executable inquiry synthesis for the unchanged one-packet interface

All six states and all five actions of OnePacketQuestions are represented.
The table is calculated from its existing `advance`; no replacement transition
law is installed. Packet admissibility and observations are the same native
relations. The finite encodings and their inverses are proved explicitly.

Concrete bounded verdicts are kernel computations of the constructive search.
The selected A/B policies are retained as data and their decoded native policies
are certified. This is a finite comparison-interface realization, not a proof
that the comparison table describes a physical apparatus or a universal law.
-/

namespace Generative.InquirySufficiency.OnePacketInquirySynthesis

open AttainableQuestions OnePacketQuestions OnePacketAdmissibility
open DerivedCertificates FiniteClassification

set_option maxRecDepth 100000
set_option maxHeartbeats 0

def encodeState : State → Fin 6
  | ⟨.A, true⟩ => ⟨0, by decide⟩
  | ⟨.B, true⟩ => ⟨1, by decide⟩
  | ⟨.C, true⟩ => ⟨2, by decide⟩
  | ⟨.A, false⟩ => ⟨3, by decide⟩
  | ⟨.B, false⟩ => ⟨4, by decide⟩
  | ⟨.C, false⟩ => ⟨5, by decide⟩

def decodeState : Fin 6 → State
  | ⟨0, _⟩ => start .A
  | ⟨1, _⟩ => start .B
  | ⟨2, _⟩ => start .C
  | ⟨3, _⟩ => spent .A
  | ⟨4, _⟩ => spent .B
  | ⟨_ + 5, _⟩ => spent .C

theorem decode_encode_state (s : State) : decodeState (encodeState s) = s := by
  cases s with
  | mk target packet => cases target <;> cases packet <;> rfl

theorem encode_decode_state (i : Fin 6) : encodeState (decodeState i) = i := by
  obtain ⟨i, bound⟩ := i
  cases i with
  | zero => rfl
  | succ i => cases i with
    | zero => rfl
    | succ i => cases i with
      | zero => rfl
      | succ i => cases i with
        | zero => rfl
        | succ i => cases i with
          | zero => rfl
          | succ i => cases i with
            | zero => rfl
            | succ i =>
              exact False.elim (Nat.not_lt_zero i
                (Nat.lt_of_succ_lt_succ (Nat.lt_of_succ_lt_succ
                  (Nat.lt_of_succ_lt_succ (Nat.lt_of_succ_lt_succ
                    (Nat.lt_of_succ_lt_succ (Nat.lt_of_succ_lt_succ bound)))))))

def encodeAction : Action → Fin 5
  | .probeA => ⟨0, by decide⟩
  | .probeB => ⟨1, by decide⟩
  | .control ⟨0, _⟩ => ⟨2, by decide⟩
  | .control ⟨1, _⟩ => ⟨3, by decide⟩
  | .control ⟨_ + 2, _⟩ => ⟨4, by decide⟩

def decodeAction : Fin 5 → Action
  | ⟨0, _⟩ => .probeA
  | ⟨1, _⟩ => .probeB
  | ⟨2, _⟩ => .control negative
  | ⟨3, _⟩ => .control positive
  | ⟨_ + 4, _⟩ => .control denied

theorem decode_encode_action (a : Action) : decodeAction (encodeAction a) = a := by
  cases a with
  | probeA => rfl
  | probeB => rfl
  | control output =>
    obtain ⟨i, bound⟩ := output
    cases i with
    | zero => rfl
    | succ i => cases i with
      | zero => rfl
      | succ i => cases i with
        | zero => rfl
        | succ i =>
          exact False.elim (Nat.not_lt_zero i
            (Nat.lt_of_succ_lt_succ (Nat.lt_of_succ_lt_succ
              (Nat.lt_of_succ_lt_succ bound))))

theorem encode_decode_action (i : Fin 5) : encodeAction (decodeAction i) = i := by
  obtain ⟨i, bound⟩ := i
  cases i with
  | zero => rfl
  | succ i => cases i with
    | zero => rfl
    | succ i => cases i with
      | zero => rfl
      | succ i => cases i with
        | zero => rfl
        | succ i => cases i with
          | zero => rfl
          | succ i =>
            exact False.elim (Nat.not_lt_zero i
              (Nat.lt_of_succ_lt_succ (Nat.lt_of_succ_lt_succ
                (Nat.lt_of_succ_lt_succ (Nat.lt_of_succ_lt_succ
                  (Nat.lt_of_succ_lt_succ bound))))))

def table (s : Fin 6) (a : Fin 5) (t : Fin 6) : Bool :=
  Nat.beq t.val (encodeState (advance (decodeState s) (decodeAction a))).val

def condition (s : Fin 6) (a : Fin 5) (_ : Fin 6) : Bool :=
  match decodeAction a with
  | .probeA => (decodeState s).packet
  | .probeB => (decodeState s).packet
  | .control _ => true

def tableSense (s : Fin 6) (a : Fin 5) (t : Fin 6) : Fin 3 :=
  sense (decodeState s) (decodeAction a) (decodeState t)

def initialTable (s : Fin 6) : Bool := (decodeState s).packet
def exhaustedTable (s : Fin 6) : Bool := !(decodeState s).packet

theorem nat_beq_reflexive (n : Nat) : Nat.beq n n = true := by
  induction n with
  | zero => rfl
  | succ n ih => exact ih

theorem table_correspondence (s : Fin 6) (a : Fin 5) (t : Fin 6) :
    table s a t = true ↔ process.step (decodeState s) (decodeAction a) (decodeState t) := by
  constructor
  · intro h
    have same : t = encodeState (advance (decodeState s) (decodeAction a)) :=
      Fin.ext (Nat.eq_of_beq_eq_true h)
    exact (congrArg decodeState same).trans (decode_encode_state _)
  · intro h
    have same : t = encodeState (advance (decodeState s) (decodeAction a)) :=
      (encode_decode_state t).symm.trans (congrArg encodeState h)
    show Nat.beq t.val (encodeState (advance (decodeState s) (decodeAction a))).val = true
    exact same ▸ nat_beq_reflexive _

theorem condition_correspondence (s : Fin 6) (a : Fin 5) (t : Fin 6) :
    condition s a t = true ↔ packetSafe (decodeState s) (decodeAction a) (decodeState t) := by
  unfold condition packetSafe
  cases decodeAction a with
  | probeA => exact Iff.rfl
  | probeB => exact Iff.rfl
  | control _ => exact ⟨fun _ => True.intro, fun _ => rfl⟩

theorem initial_correspondence (s : Fin 6) :
    initialTable s = true ↔ initial (decodeState s) := Iff.rfl

def question (f : Target → Bool) (s t : Fin 6) : Bool :=
  (f (decodeState s).initialTarget == f (decodeState t).initialTarget)

def jointQuestion (s t : Fin 6) : Bool := question isA s t && question isB s t

theorem question_correspondence (f : Target → Bool) (s t : Fin 6) :
    question f s t = true ↔
      Agreement (fun x => f x.initialTarget) (decodeState s) (decodeState t) := by
  change (f (decodeState s).initialTarget == f (decodeState t).initialTarget) = true ↔
    f (decodeState s).initialTarget = f (decodeState t).initialTarget
  cases f (decodeState s).initialTarget <;> cases f (decodeState t).initialTarget <;>
    constructor <;> intro h <;> first | rfl | exact Bool.noConfusion h

/-- All reported values below are reductions of the actual certificate search. -/
theorem empty_initial_rejected :
    canIdentify table condition tableSense (fun _ _ => true) 1 (fun _ => false) = false := rfl

theorem constant_at_depth_zero :
    canIdentify table condition tableSense (fun _ _ => true) 0 initialTable = true := rfl

theorem separate_at_depth_one :
    canIdentify table condition tableSense (question isA) 1 initialTable = true ∧
    canIdentify table condition tableSense (question isB) 1 initialTable = true := ⟨rfl, rfl⟩

theorem blocked_and_joint_rejected :
    canIdentify table condition tableSense (question isC) 1 initialTable = false ∧
    canIdentify table condition tableSense (question isC) 2 initialTable = false ∧
    canIdentify table condition tableSense jointQuestion 1 initialTable = false ∧
    canIdentify table condition tableSense jointQuestion 2 initialTable = false :=
  ⟨rfl, rfl, rfl, rfl⟩

theorem exhausted_verdicts :
    canIdentify table condition tableSense (fun _ _ => true) 0 exhaustedTable = true ∧
    canIdentify table condition tableSense (question isA) 2 exhaustedTable = false ∧
    canIdentify table condition tableSense (question isB) 2 exhaustedTable = false ∧
    canIdentify table condition tableSense (question isC) 2 exhaustedTable = false ∧
    canIdentify table condition tableSense jointQuestion 2 exhaustedTable = false :=
  ⟨rfl, rfl, rfl, rfl, rfl⟩


/-- The finite constructor used by the search's three observed branches. -/
def finiteStops : Fin 3 → Policy (Fin 5) Unit 3 :=
  finiteCons (.respond ()) (finiteCons (.respond ())
    (finiteCons .abort (fun i : Fin 0 => Fin.elim0 i)))

def finiteProbe (which : Bool) : Policy (Fin 5) Unit 3 :=
  .inquire (encodeAction (test which)) finiteStops

def answer : Bool → Target → Bool
  | true => isA
  | false => isB

def decodePolicy : Policy (Fin 5) Unit 3 → Policy Action Unit 3
  | .abort => .abort
  | .respond r => .respond r
  | .inquire a next => .inquire (decodeAction a) (fun o => decodePolicy (next o))

/-- An equality of concrete search results, not a separately chosen policy. -/
theorem search_selects_probe (which : Bool) :
    policyOption (inquirySearch table condition tableSense (question (answer which))
      1 initialTable) = some (finiteProbe which) := by
  cases which <;> rfl

/-- Only pointwise branch equality is used; no equality of functions is needed. -/
theorem decoded_stop (o : Fin 3) : decodePolicy (finiteStops o) = stopOnReceipt o := by
  obtain ⟨i, bound⟩ := o
  cases i with
  | zero => rfl
  | succ i => cases i with
    | zero => rfl
    | succ i => cases i with
      | zero => rfl
      | succ i =>
        exact False.elim (Nat.not_lt_zero i
          (Nat.lt_of_succ_lt_succ (Nat.lt_of_succ_lt_succ
            (Nat.lt_of_succ_lt_succ bound))))

/-- The very policy returned by finite search is certified after decoding into
native actions. All native successor branches retain the packet contract. -/
theorem decoded_probe_identifies (which : Bool) :
    Identifies process packetSafe sense
      (Agreement (fun s => answer which s.initialTarget))
      (decodePolicy (finiteProbe which)) initial := by
  have pair : match which with
      | true => answer which .B = answer which .C
      | false => answer which .A = answer which .C := by
    cases which <;> rfl
  have native : Identifies process packetSafe sense
      (Agreement (fun s => answer which s.initialTarget))
      (.inquire (test which) (fun o => decodePolicy (finiteStops o))) initial := by
    constructor
    · refine ⟨initial_is_inhabited, initial_probe_admissible which, ?_⟩
      intro o
      exact Eq.mp (congrArg (fun p => InquirySound process packetSafe sense p
        (After process sense initial (test which) o)) (decoded_stop o).symm)
        ((one_probe_packet_sound which).2.2 o)
    · intro o
      exact Eq.mp (congrArg (fun p => RefinesLeaves process sense
        (Agreement (fun s => answer which s.initialTarget)) p
        (After process sense initial (test which) o)) (decoded_stop o).symm)
        ((one_probe_identifies (answer which) which pair).2 o)
  change Identifies process packetSafe sense
    (Agreement (fun s => answer which s.initialTarget))
    (.inquire (decodeAction (encodeAction (test which)))
      (fun o => decodePolicy (finiteStops o))) initial
  exact (decode_encode_action (test which)).symm ▸ native

/-- Closed synthesis-to-native certificate: no soundness, nonemptiness, branch
classification or success certificate is assumed. The finite certificate is
extracted from the search and the same decoded policy has native validity. -/
theorem extracted_policy_native_certificate (which : Bool) :
    ∃ policy : Policy (Fin 5) Unit 3,
      policyOption (inquirySearch table condition tableSense (question (answer which))
        1 initialTable) = some policy ∧
      Certified table condition tableSense (question (answer which))
        1 (fun s => initialTable s = true) policy ∧
      Identifies process packetSafe sense
        (Agreement (fun s => answer which s.initialTarget)) (decodePolicy policy) initial := by
  refine ⟨finiteProbe which, search_selects_probe which, ?_, decoded_probe_identifies which⟩
  exact (policyOption_certified
    (inquirySearch table condition tableSense (question (answer which)) 1 initialTable)
    (search_selects_probe which)).2

/-- These verdicts compute prefix validity and actual-leaf continuations too.
The joint refusal has the stated fixed prefix and one-step continuation bound;
the inherited native impossibility covers arbitrary finite alternatives. -/
theorem continuation_verdicts :
    canContinue table condition tableSense (question isA) 0 (finiteProbe true) initialTable = true ∧
    canContinue table condition tableSense jointQuestion 1 (finiteProbe true) initialTable = false ∧
    canContinue table condition tableSense (fun _ _ => true) 0
      (finiteProbe true) exhaustedTable = false := ⟨rfl, rfl, rfl⟩

/-- The exhausted native configuration leaves only constant questions, for
arbitrary finite policies and answer types, not just the computed horizons. -/
theorem exhausted_native_iff {Value : Type} (f : Target → Value) :
    Attainable process packetSafe sense (Agreement (fun s => f s.initialTarget))
      (fun s => s.packet = false) ↔ f .A = f .C ∧ f .B = f .C := by
  constructor
  · rintro ⟨_, policy, sound, leaves⟩
    have forgotten : Identifies process safe sense
        (Agreement (fun s => f s.initialTarget)) policy (fun s => s.packet = false) :=
      ⟨forget_packet_safety policy _ sound, leaves⟩
    exact ⟨spent_pair_same_class _ policy _ forgotten (x := .A) (y := .C) rfl rfl,
      spent_pair_same_class _ policy _ forgotten (x := .B) (y := .C) rfl rfl⟩
  · intro h
    refine ⟨⟨spent .A, rfl⟩, .respond (), ⟨⟨spent .A, rfl⟩, fun _ _ => True.intro⟩, ?_⟩
    intro s t hs ht
    cases s with
    | mk x sx => cases t with
      | mk y sy => cases sx with
        | true => cases hs
        | false => cases sy with
          | true => cases ht
          | false =>
            cases x <;> cases y <;>
              first | rfl | exact h.1 | exact h.2 | exact h.1.symm | exact h.2.symm |
                exact h.1.trans h.2.symm | exact h.2.trans h.1.symm

end Generative.InquirySufficiency.OnePacketInquirySynthesis

#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.encodeState
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.decodeState
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.decode_encode_state
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.encode_decode_state
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.encodeAction
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.decodeAction
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.decode_encode_action
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.encode_decode_action
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.table
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.condition
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.tableSense
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.initialTable
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.exhaustedTable
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.nat_beq_reflexive
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.table_correspondence
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.condition_correspondence
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.initial_correspondence
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.question
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.jointQuestion
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.question_correspondence
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.empty_initial_rejected
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.constant_at_depth_zero
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.separate_at_depth_one
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.blocked_and_joint_rejected
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.exhausted_verdicts
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.finiteStops
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.finiteProbe
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.answer
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.decodePolicy
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.search_selects_probe
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.decoded_stop
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.decoded_probe_identifies
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.extracted_policy_native_certificate
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.continuation_verdicts
#print axioms Generative.InquirySufficiency.OnePacketInquirySynthesis.exhausted_native_iff
