import AlignmentInquiry
import ReformEvidence

/- Contingent query/remedy selection consumes the actual inherited reformed
history. It is a complete finite search over a disclosed repertoire, not an
inventor of arbitrary sensors or ethical standards. -/
namespace ReformInquiry
open AlignmentInquiry GoalFormationRevision ReformEvidence

inductive Query where
  | reuse | selected | direct | slow
  deriving DecidableEq, Repr

inductive Remedy where
  | continue | provide
  deriving DecidableEq, Repr

def reported (s : Field) : Bool :=
  s.core.ground.any Ground.transitionLoss

def probe (s : Field) (q : Query) : Option (Bool × Field) := do
  let t ← match q with
    | .reuse => some s
    | .selected => inspect .selected s
    | .direct => inspect .direct s
    | .slow => do
      let a ← charge 3 s.core.account
      inspect .direct {s with core := {s.core with account := a}}
  pure (reported t,t)

def respond (authorized : Bool) (s : Field) (a : Remedy) : Option Field :=
  match a with
  | .continue => advance s
  | .provide => repair authorized s >>= advance

/-- A real subsequent operation must retain access and maintenance and consume
the revised goal. This covers those named conditions, not every ethical effect. -/
def achieved (s : Field) : Bool :=
  s.core.archive.getLast? |>.any (fun e =>
    e.outcome.access && e.outcome.maintenance &&
    (e.practice == .learning) && (s.core.goal == some .learning))

def interface (authorized : Bool) : Interface Field Query Remedy :=
  ⟨probe,respond authorized,achieved⟩

def plans : List (Plan Query Remedy) :=
  repertoire [.reuse,.selected,.direct,.slow] [.continue,.provide]

def uncertainty : List Field := (masked false).toList ++ (masked true).toList

def chosen : Option (Plan Query Remedy) := choose (interface true) uncertainty plans

def execute (harm : Bool) : Option Field := do
  let p ← chosen
  let s ← masked harm
  run (interface true) p s

theorem chosen_query_and_contingent_remedy :
    chosen = some ⟨.direct,.continue,.provide⟩ := by decide

theorem faithful_query_both_ways :
    (masked false >>= fun s => probe s .direct).map Prod.fst = some false ∧
    (masked true >>= fun s => probe s .direct).map Prod.fst = some true := by decide

theorem selected_report_cannot_support_uniform_remedy :
    choose (interface true) uncertainty
      (repertoire [.reuse,.selected] [.continue,.provide]) = none := by decide

theorem actual_harmful_history_is_repaired :
    (execute true).map (fun s => (s.provisioned,achieved s,s.core.goal,s.core.selector,
      s.core.losses,s.core.archive.length,s.core.account)) =
      some (true,true,some .learning,.learning,2,4,⟨2,6,18⟩) := by rfl

theorem actual_supported_reform_continues :
    (execute false).map (fun s => (s.provisioned,achieved s,s.core.goal,s.core.selector,
      s.core.losses,s.core.archive.length,s.core.account)) =
      some (false,true,some .learning,.learning,1,4,⟨3,8,15⟩) := by rfl

theorem both_branches_preserve_historical_losses (harm : Bool) :
    (execute harm).map (fun s => s.core.losses) =
      (masked harm).map (fun s => s.core.losses) := by
  cases harm <;> decide

theorem both_branches_keep_total_support (harm : Bool) :
    (execute harm).map (fun s => total s.core.account) = some 26 := by
  cases harm <;> decide

theorem known_supported_case_avoids_unneeded_inquiry :
    choose (interface true) (masked false).toList plans =
      some ⟨.reuse,.continue,.continue⟩ := by decide

theorem absent_authority_blocks_joint_solution :
    choose (interface false) uncertainty plans = none := by decide

theorem accurate_inquiry_can_consume_the_remedy :
    (masked true >>= fun s => probe s .slow).map Prod.fst = some true ∧
    (masked true >>= run (interface true) ⟨.slow,.continue,.provide⟩) = none := by decide

theorem omitted_harmful_model_invalidates_selection :
    choose (interface true) (masked false).toList plans =
      some ⟨.reuse,.continue,.continue⟩ ∧
    (masked true >>= run (interface true) ⟨.reuse,.continue,.continue⟩).map achieved =
      some false := by decide

theorem selected_policy_works_for_all_retained_candidates :
    ∀ s, s ∈ uncertainty → ∃ t,
      run (interface true) ⟨.direct,.continue,.provide⟩ s = some t ∧ achieved t = true := by
  exact (chosen_sound (interface true) uncertainty plans _ chosen_query_and_contingent_remedy).2.2

end ReformInquiry
