import AttainableQuestions

/-!
# The existing one-packet comparison: exact attainable questions

This realizes the permissive comparison table in ATTAINABLE-MATHEMATICAL-QUESTIONS
and INQUIRY-CRITERION-MATH §3. Target A/B/C is fixed initial behavior, not current
phase. Ordinary support, computation and retained observation paths are granted
as in that comparison. A macro probe selects the learned-output-1 or -0 test;
this is not a costed refinement theorem for the Python apparatus.

`control o` grants arbitrary target-independent stuttering with known common
output o, so phase/reset/sensor operations are not silently discarded. Their
actual physical schedules and costs are abstracted. After exhaustion, probes
return a distinct denial observation. This permissive extra access reveals no
initial target and strengthens the negative result. No control restores source.
Every inquiry uses one common action and all successors of the represented process.
Termination and answer projection are logical, not new free reporting hardware.
-/

namespace Generative.InquirySufficiency.OnePacketQuestions

open AttainableQuestions

inductive Target where
  | A | B | C

structure State where
  initialTarget : Target
  packet : Bool

inductive Action where
  | probeA | probeB
  | control (output : Fin 3)

def negative : Fin 3 := ⟨0, Nat.zero_lt_succ 2⟩
def positive : Fin 3 := ⟨1, Nat.succ_lt_succ (Nat.zero_lt_succ 1)⟩
def denied : Fin 3 := ⟨2, Nat.lt_succ_self 2⟩

def advance (s : State) : Action → State
  | .probeA => ⟨s.initialTarget, false⟩
  | .probeB => ⟨s.initialTarget, false⟩
  | .control _ => s

def receipt (s : State) : Action → Fin 3
  | .control output => output
  | .probeA => match s.packet with
    | false => denied
    | true => match s.initialTarget with
      | .A => positive
      | .B => negative
      | .C => negative
  | .probeB => match s.packet with
    | false => denied
    | true => match s.initialTarget with
      | .A => negative
      | .B => positive
      | .C => negative

def process : Process State Action where
  step s a t := t = advance s a

def sense (s : State) (a : Action) (_ : State) : Fin 3 := receipt s a
def safe (_ : State) (_ : Action) (_ : State) : Prop := True
def initial (s : State) : Prop := s.packet = true

def start (target : Target) : State := ⟨target, true⟩
def spent (target : Target) : State := ⟨target, false⟩

theorem all_actions_enabled (s : State) (a : Action) : Enabled process s a :=
  ⟨advance s a, rfl⟩

theorem step_retains_initial_target {s t : State} {a : Action}
    (h : process.step s a t) : t.initialTarget = s.initialTarget := by
  cases h
  cases a <;> rfl

theorem trace_retains_initial_target {s t : State} {word : List Action}
    (h : Trace process s word t) : t.initialTarget = s.initialTarget := by
  induction h with
  | nil => rfl
  | cons step tail ih => exact ih.trans (step_retains_initial_target step)

theorem spent_step (target : Target) (a : Action) :
    process.step (spent target) a (spent target) := by
  cases a <;> rfl

theorem spent_observation (x y : Target) (a : Action) :
    sense (spent x) a (spent x) = sense (spent y) a (spent y) := by
  cases a <;> rfl

/-- Any finite policy reaching two exhausted labels must put them in the same
answer class. Control outputs and denials can select branches but never separate
these labels. This is an induction over policy syntax, not a depth-two check. -/
theorem spent_pair_same_class (q : State → State → Prop)
    (policy : Policy Action Unit 3) (B : State → Prop)
    (h : Identifies process safe sense q policy B)
    {x y : Target} (hx : B (spent x)) (hy : B (spent y)) : q (spent x) (spent y) := by
  induction policy generalizing B with
  | abort => exact False.elim (h.1 _ hx)
  | respond r => exact h.2 _ _ hx hy
  | inquire a next ih =>
    let o := sense (spent x) a (spent x)
    have first : After process sense B a o (spent x) :=
      ⟨spent x, hx, spent_step x a, rfl⟩
    have second : After process sense B a o (spent y) :=
      ⟨spent y, hy, spent_step y a, (spent_observation y x a)⟩
    exact ih o _ ⟨h.1.2.2 o, h.2 o⟩ first second

/-- Before the first source-consuming probe, common controls preserve all three
initial possibilities. Either probe leaves its negative pair inseparable. -/
theorem initial_question_constraint {Value : Type} (f : Target → Value)
    (policy : Policy Action Unit 3) (B : State → Prop)
    (h : Identifies process safe sense (Agreement (fun s => f s.initialTarget)) policy B)
    (hA : B (start .A)) (hB : B (start .B)) (hC : B (start .C)) :
    f .B = f .C ∨ f .A = f .C := by
  induction policy generalizing B with
  | abort => exact False.elim (h.1 _ hA)
  | respond r => exact Or.inl (h.2 _ _ hB hC)
  | inquire a next ih =>
    cases a with
    | probeA =>
      exact Or.inl (spent_pair_same_class _ (next negative) _
        ⟨h.1.2.2 negative, h.2 negative⟩
        ⟨start .B, hB, rfl, rfl⟩ ⟨start .C, hC, rfl, rfl⟩)
    | probeB =>
      exact Or.inr (spent_pair_same_class _ (next negative) _
        ⟨h.1.2.2 negative, h.2 negative⟩
        ⟨start .A, hA, rfl, rfl⟩ ⟨start .C, hC, rfl, rfl⟩)
    | control output =>
      exact ih output _ ⟨h.1.2.2 output, h.2 output⟩
        ⟨start .A, hA, rfl, rfl⟩ ⟨start .B, hB, rfl, rfl⟩
        ⟨start .C, hC, rfl, rfl⟩

/-- true selects the first column (A); false selects the second column (B). -/
def test : Bool → Action
  | true => .probeA
  | false => .probeB

def hit : Bool → Target
  | true => .A
  | false => .B

def stopOnReceipt : Fin 3 → Policy Action Unit 3
  | ⟨0, _⟩ => .respond ()
  | ⟨1, _⟩ => .respond ()
  | ⟨_ + 2, _⟩ => .abort

def oneProbe (which : Bool) : Policy Action Unit 3 :=
  .inquire (test which) stopOnReceipt

theorem first_probe_binary (which : Bool) {s : State} (h : initial s) :
    receipt s (test which) = negative ∨ receipt s (test which) = positive := by
  cases s with
  | mk target packet =>
    cases packet with
    | false => cases h
    | true => cases which <;> cases target <;> first | exact Or.inl rfl | exact Or.inr rfl

theorem after_first_probe_binary (which : Bool) {o : Fin 3} {t : State}
    (h : After process sense initial (test which) o t) : o = negative ∨ o = positive := by
  obtain ⟨s, member, _, observed⟩ := h
  rcases first_probe_binary which member with neg | pos
  · exact Or.inl (observed.symm.trans neg)
  · exact Or.inr (observed.symm.trans pos)

theorem one_probe_sound (which : Bool) :
    InquirySound process safe sense (oneProbe which) initial := by
  refine ⟨⟨start .A, rfl⟩, (fun s _ => ⟨all_actions_enabled s _, fun _ _ => True.intro⟩), ?_⟩
  intro ⟨i, hi⟩
  cases i with
  | zero =>
    refine ⟨⟨spent .C, start .C, rfl, ?_, ?_⟩, fun _ _ => True.intro⟩
    · cases which <;> rfl
    · cases which <;> rfl
  | succ i =>
    cases i with
    | zero =>
      refine ⟨⟨spent (hit which), start (hit which), rfl, ?_, ?_⟩, fun _ _ => True.intro⟩
      · cases which <;> rfl
      · cases which <;> rfl
    | succ i =>
      intro t h
      rcases after_first_probe_binary which h with neg | pos
      · exact Nat.noConfusion (congrArg Fin.val neg)
      · exact Nat.noConfusion (Nat.succ.inj (congrArg Fin.val pos))

/-- The only pair merged by each first experiment is precisely the pair named
in the hypothesis. The hypothesis is a question constraint, not a process law. -/
theorem same_first_receipt_same_answer {Value : Type} (f : Target → Value) (which : Bool)
    (pair : match which with | true => f .B = f .C | false => f .A = f .C)
    {s t : State} (hs : initial s) (ht : initial t)
    (observed : receipt s (test which) = receipt t (test which)) :
    f s.initialTarget = f t.initialTarget := by
  cases s with
  | mk x sx =>
    cases t with
    | mk y sy =>
      cases sx with
      | false => cases hs
      | true =>
        cases sy with
        | false => cases ht
        | true =>
          cases which <;> cases x <;> cases y <;>
            first | rfl | exact pair | exact pair.symm |
              exact False.elim (Nat.noConfusion (congrArg Fin.val observed))

theorem after_probe_homogeneous {Value : Type} (f : Target → Value) (which : Bool)
    (pair : match which with | true => f .B = f .C | false => f .A = f .C)
    (o : Fin 3) :
    Homogeneous (Agreement (fun s => f s.initialTarget))
      (After process sense initial (test which) o) := by
  intro s t hs ht
  obtain ⟨beforeS, memberS, stepS, readS⟩ := hs
  obtain ⟨beforeT, memberT, stepT, readT⟩ := ht
  have answer := same_first_receipt_same_answer f which pair memberS memberT (readS.trans readT.symm)
  have preservedS := step_retains_initial_target stepS
  have preservedT := step_retains_initial_target stepT
  exact (congrArg f preservedS).trans (answer.trans (congrArg f preservedT).symm)

theorem one_probe_identifies {Value : Type} (f : Target → Value) (which : Bool)
    (pair : match which with | true => f .B = f .C | false => f .A = f .C) :
    Identifies process safe sense (Agreement (fun s => f s.initialTarget))
      (oneProbe which) initial := by
  refine ⟨one_probe_sound which, ?_⟩
  intro ⟨i, hi⟩
  cases i with
  | zero => exact after_probe_homogeneous f which pair _
  | succ i =>
    cases i with
    | zero => exact after_probe_homogeneous f which pair _
    | succ i => exact True.intro

/-- Exact family of attainable answer partitions, for every answer type and
arbitrary finite observation-dependent policies including stuttering controls. -/
theorem attainable_iff {Value : Type} (f : Target → Value) :
    Attainable process safe sense (Agreement (fun s => f s.initialTarget)) initial ↔
      f .B = f .C ∨ f .A = f .C := by
  constructor
  · rintro ⟨_, policy, identifies⟩
    exact initial_question_constraint f policy initial identifies rfl rfl rfl
  · intro h
    refine ⟨⟨start .A, rfl⟩, ?_⟩
    cases h with
    | inl pair => exact ⟨oneProbe true, one_probe_identifies f true pair⟩
    | inr pair => exact ⟨oneProbe false, one_probe_identifies f false pair⟩

def isA : Target → Bool
  | .A => true
  | .B => false
  | .C => false

def isB : Target → Bool
  | .A => false
  | .B => true
  | .C => false

def isC : Target → Bool
  | .A => false
  | .B => false
  | .C => true

theorem separately_attainable :
    Attainable process safe sense (Agreement (fun s => isA s.initialTarget)) initial ∧
    Attainable process safe sense (Agreement (fun s => isB s.initialTarget)) initial :=
  ⟨(attainable_iff isA).mpr (Or.inl rfl), (attainable_iff isB).mpr (Or.inr rfl)⟩

theorem joint_answer_unattainable :
    ¬ Attainable process safe sense
      (Agreement (fun s => (isA s.initialTarget, isB s.initialTarget))) initial := by
  intro h
  rcases (attainable_iff (fun x => (isA x, isB x))).mp h with eq | eq
  · exact Bool.noConfusion (congrArg Prod.snd eq)
  · exact Bool.noConfusion (congrArg Prod.fst eq)

theorem blocked_question_unattainable :
    ¬ Attainable process safe sense (Agreement (fun s => isC s.initialTarget)) initial := by
  intro h
  rcases (attainable_iff isC).mp h with eq | eq <;> exact Bool.noConfusion eq

/-- The logical conjunction of the two attainable initial-target questions is
unattainable, even though each has its own one-probe policy. -/
theorem join_question_unattainable :
    ¬ Attainable process safe sense
      (Join (Agreement (fun s => isA s.initialTarget))
        (Agreement (fun s => isB s.initialTarget))) initial := by
  intro h
  exact joint_answer_unattainable (attainable_downward process safe sense
    (fun s t same => (agreement_pair_iff
      (fun x => isA x.initialTarget) (fun x => isB x.initialTarget) s t).mp same) h)

/-- No attainable refinement of both fixed initial-target questions exists.
Consequently, no family of attainable questions containing these two can have
an attainable greatest refinement; this is stronger than failure of one chosen
joint-answer encoding. -/
theorem no_attainable_common_upper :
    ¬ ∃ upper : Question State,
      Attainable process safe sense upper initial ∧
      Coarser (Agreement (fun s => isA s.initialTarget)) upper ∧
      Coarser (Agreement (fun s => isB s.initialTarget)) upper :=
  missing_join_no_attainable_common_upper process safe sense join_question_unattainable


end Generative.InquirySufficiency.OnePacketQuestions

#print axioms Generative.InquirySufficiency.OnePacketQuestions.negative
#print axioms Generative.InquirySufficiency.OnePacketQuestions.positive
#print axioms Generative.InquirySufficiency.OnePacketQuestions.denied
#print axioms Generative.InquirySufficiency.OnePacketQuestions.advance
#print axioms Generative.InquirySufficiency.OnePacketQuestions.receipt
#print axioms Generative.InquirySufficiency.OnePacketQuestions.process
#print axioms Generative.InquirySufficiency.OnePacketQuestions.sense
#print axioms Generative.InquirySufficiency.OnePacketQuestions.safe
#print axioms Generative.InquirySufficiency.OnePacketQuestions.initial
#print axioms Generative.InquirySufficiency.OnePacketQuestions.start
#print axioms Generative.InquirySufficiency.OnePacketQuestions.spent
#print axioms Generative.InquirySufficiency.OnePacketQuestions.all_actions_enabled
#print axioms Generative.InquirySufficiency.OnePacketQuestions.step_retains_initial_target
#print axioms Generative.InquirySufficiency.OnePacketQuestions.trace_retains_initial_target
#print axioms Generative.InquirySufficiency.OnePacketQuestions.spent_step
#print axioms Generative.InquirySufficiency.OnePacketQuestions.spent_observation
#print axioms Generative.InquirySufficiency.OnePacketQuestions.spent_pair_same_class
#print axioms Generative.InquirySufficiency.OnePacketQuestions.initial_question_constraint
#print axioms Generative.InquirySufficiency.OnePacketQuestions.test
#print axioms Generative.InquirySufficiency.OnePacketQuestions.hit
#print axioms Generative.InquirySufficiency.OnePacketQuestions.stopOnReceipt
#print axioms Generative.InquirySufficiency.OnePacketQuestions.oneProbe
#print axioms Generative.InquirySufficiency.OnePacketQuestions.first_probe_binary
#print axioms Generative.InquirySufficiency.OnePacketQuestions.after_first_probe_binary
#print axioms Generative.InquirySufficiency.OnePacketQuestions.one_probe_sound
#print axioms Generative.InquirySufficiency.OnePacketQuestions.same_first_receipt_same_answer
#print axioms Generative.InquirySufficiency.OnePacketQuestions.after_probe_homogeneous
#print axioms Generative.InquirySufficiency.OnePacketQuestions.one_probe_identifies
#print axioms Generative.InquirySufficiency.OnePacketQuestions.attainable_iff
#print axioms Generative.InquirySufficiency.OnePacketQuestions.isA
#print axioms Generative.InquirySufficiency.OnePacketQuestions.isB
#print axioms Generative.InquirySufficiency.OnePacketQuestions.isC
#print axioms Generative.InquirySufficiency.OnePacketQuestions.separately_attainable
#print axioms Generative.InquirySufficiency.OnePacketQuestions.joint_answer_unattainable
#print axioms Generative.InquirySufficiency.OnePacketQuestions.blocked_question_unattainable
#print axioms Generative.InquirySufficiency.OnePacketQuestions.join_question_unattainable
#print axioms Generative.InquirySufficiency.OnePacketQuestions.no_attainable_common_upper
