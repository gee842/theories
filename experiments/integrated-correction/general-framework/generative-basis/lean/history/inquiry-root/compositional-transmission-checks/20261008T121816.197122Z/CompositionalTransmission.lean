import CompositionalFormation

/-!
Learning through another participant's actual response, reconstruction and
renewed demonstration. Mature starting variants, grammar, construction/search,
schedule, faithful reception and fresh cohort support remain supplied.
Transmission fidelity is distinct from correctness for an independently
specified task. No biological inheritance or universal cultural progress.
-/
namespace Generative.CompositionalTransmission
open CompositionalAcquisition CompositionalFormation

structure Exchange where
  sender : Frame
  receiver : Frame
  deriving DecidableEq, Repr

def blank (support parts : Nat) : Frame := fromLearner (initial support) parts

-- A mature starting condition, not a new origin theorem.
def source (p : Program) (support : Nat) : Frame :=
  {blank support 0 with wires := p.route, installed := some p}

def send (e : Expr) (x : Exchange) : Exchange :=
  if x.receiver.blocked then x else
  if 1 ≤ x.receiver.support then
    match respond x.sender e with
    | none => {x with receiver := {x.receiver with blocked := true}}
    | some (output,remaining) =>
      ⟨{x.sender with support := remaining, spent := x.sender.spent + (x.sender.support - remaining)},
       {x.receiver with samples := x.receiver.samples ++ [(e,output)], support := x.receiver.support - 1, spent := x.receiver.spent + 1}⟩
  else {x with receiver := {x.receiver with blocked := true}}

def lesson : List Expr → Exchange → Exchange
  | [],x => x
  | e::es,x => lesson es (send e x)

def basic : List Expr := [p0,p1,orderProbe]
def extended : List Expr := basic ++ [novel]
def learn (teacher : Frame) (support parts : Nat) (queries : List Expr := basic) : Frame :=
  develop (lesson queries ⟨teacher,blank support parts⟩).receiver

def programRecords (p : Program) : List (Expr × List Bool) :=
  [(p0,operate p p0),(p1,operate p p1),(orderProbe,operate p orderProbe)]

theorem response_remaining_is_bounded (s : Frame) (e : Expr) (out : List Bool) (left : Nat)
    (h : respond s e = some (out,left)) : left ≤ s.support := by
  unfold respond at h
  split at h
  · contradiction
  · dsimp only at h
    split at h
    · simp only [Option.some.injEq,Prod.mk.injEq] at h
      omega
    · contradiction

theorem send_preserves_joint_support (e : Expr) (x : Exchange) :
    (send e x).sender.support + (send e x).sender.spent +
      (send e x).receiver.support + (send e x).receiver.spent =
    x.sender.support + x.sender.spent + x.receiver.support + x.receiver.spent := by
  unfold send
  split
  · rfl
  · split
    · cases h : respond x.sender e with
      | none => rfl
      | some pair =>
        rcases pair with ⟨out,left⟩
        have bound := response_remaining_is_bounded x.sender e out left h
        simp only
        omega
    · rfl

theorem lesson_preserves_joint_support (es : List Expr) (x : Exchange) :
    (lesson es x).sender.support + (lesson es x).sender.spent +
      (lesson es x).receiver.support + (lesson es x).receiver.spent =
    x.sender.support + x.sender.spent + x.receiver.support + x.receiver.spent := by
  induction es generalizing x with
  | nil => rfl
  | cons e es ih => exact (ih (send e x)).trans (send_preserves_joint_support e x)

theorem delivery_uses_actual_response (e : Expr) (x : Exchange)
    (ready : x.receiver.blocked = false) (support : 1 ≤ x.receiver.support)
    (out : List Bool) (remaining : Nat) (actual : respond x.sender e = some (out,remaining)) :
    (send e x).receiver.samples = x.receiver.samples ++ [(e,out)] ∧
    (send e x).sender.support = remaining := by
  simp [send,ready,support,actual]

theorem absent_response_does_not_fabricate_sample (e : Expr) (x : Exchange)
    (absent : respond x.sender e = none) :
    (send e x).receiver.samples = x.receiver.samples := by
  simp only [send]
  split
  · rfl
  · split <;> simp [absent]

theorem basic_lesson_reads_program (p : Program) (n : Nat)
    (routes : p.route ∈ generatedRoutes 2) (enough : 7 ≤ n) :
    (lesson basic ⟨source p n,blank 25 8⟩).receiver =
      {blank 22 8 with spent := 3, samples := programRecords p} := by
  rcases p with ⟨a,b,r⟩
  rw [two_connector_routes] at routes
  simp only [List.mem_cons,List.not_mem_nil,or_false] at routes
  have h2 : 2 ≤ n := by omega
  have h4 : 2 ≤ n-2 := by omega
  have h7 : 3 ≤ n-2-2 := by omega
  rcases routes with rfl | rfl | rfl | rfl <;>
    simp [basic,lesson,send,respond,source,blank,fromLearner,initial,operate,dispatch,
      p0,p1,orderProbe,programRecords,h2,h4,h7]

theorem reconstructed_program_from_actual_outputs (p : Program) (n : Nat)
    (routes : p.route ∈ generatedRoutes 2) (distinct : p.first ≠ p.second)
    (enough : 7 ≤ n) :
    (learn (source p n) 25 8).installed = some p ∧
    7 ≤ (learn (source p n) 25 8).support := by
  unfold learn
  rw [basic_lesson_reads_program p n routes enough]
  rcases p with ⟨a,b,r⟩
  rw [two_connector_routes] at routes
  simp only [List.mem_cons,List.not_mem_nil,or_false] at routes
  rcases routes with rfl | rfl | rfl | rfl
  all_goals
    cases a <;> cases b <;> simp_all <;> decide

-- This variant ignores the second argument at each join. It can recur through
-- perfect output transmission while failing the forward-composition task.
def selective : Program := ⟨false,true,[false,false]⟩
def joint00 : Expr := .join p0 p0

def firstLearner : Frame := learn developed 25 8

theorem formed_teacher_can_teach_after_supported_preparation :
    (develop (prepared 25 4)).installed = some (programFor usual) ∧
    (learn (develop (prepared 25 4)) 25 8).installed = some (programFor usual) := by decide

theorem execution_only_budget_can_interrupt_teaching :
    (lesson basic ⟨developed,blank 25 8⟩).receiver.samples =
      [(p0,[false]),(p1,[true])] ∧
    firstLearner.installed = none ∧ firstLearner.blocked = true := by decide

theorem teacher_program_changes_received_evidence :
    (lesson basic ⟨source selective 7,blank 25 8⟩).receiver.samples = programRecords selective ∧
    programRecords selective ≠ trialRecords usual := by decide

theorem faithfully_reconstructed_operation_can_lose_a_task_distinction :
    (learn (source selective 7) 25 8).installed = some selective ∧
    operate selective joint00 = operate selective orderProbe ∧
    eval usual joint00 ≠ eval usual orderProbe := by decide

theorem extra_funding_does_not_fix_transmitted_content :
    (learn (source selective 70) 100 80).installed = some selective := by decide

theorem same_teacher_different_encounters_change_reconstruction :
    (learn (source (programFor collapsed) 11) 25 8 basic).installed = some duplicated ∧
    (learn (source (programFor collapsed) 11) 25 8 extended).installed = some (programFor collapsed) := by decide

def misleadingPeer : Frame := learn (source (programFor collapsed) 11) 25 8 basic
def revisedPeer : Frame :=
  reconsider (send novel ⟨source (programFor collapsed) 4,misleadingPeer⟩).receiver

theorem peer_demonstration_can_repair_without_new_generation :
    misleadingPeer.installed = some duplicated ∧
    revisedPeer.installed = some (programFor collapsed) ∧
    respond revisedPeer further = some ([false,false,false],5) := by decide

theorem erroneous_peer_demonstration_can_preserve_error :
    (reconsider (send novel ⟨source duplicated 5,misleadingPeer⟩).receiver).installed =
      some duplicated := by decide

theorem received_disagreement_is_not_automatically_repaired :
    (learn (source (programFor collapsed) 11) 5 8 extended).installed = none := by decide

end Generative.CompositionalTransmission
