import CompositionalAcquisition

/-!
Formation of one operative composition route from generic connectors, followed
by evidence testing, costly rejection and actual recursive use. Grammar,
connector functionality, proposal order, faithful records and local charges
remain supplied. This refines an operation, not the origin of all cognition.
-/
namespace Generative.CompositionalFormation

open CompositionalAcquisition

abbrev Route := List Bool

def dispatch (route : Route) (left right : List Bool) : List Bool :=
  route.flatMap (fun socket => if socket then right else left)

structure Program where
  first : Bool
  second : Bool
  route : Route
  deriving DecidableEq, Repr

def operate (p : Program) : Expr → List Bool
  | .atom false => [p.first]
  | .atom true => [p.second]
  | .join a b => dispatch p.route (operate p a) (operate p b)
  | .twice a => operate p a ++ operate p a

def routeFor (c : Code) : Route := if c.reversed then [true,false] else [false,true]
def programFor (c : Code) : Program := ⟨c.first,c.second,routeFor c⟩

theorem formed_operation_correspondence (c : Code) (e : Expr) :
    operate (programFor c) e = eval c e := by
  induction e with
  | atom b => cases b <;> rfl
  | join a b ha hb =>
    simp only [operate]
    rw [ha,hb]
    cases hc : c.reversed <;> simp [programFor,routeFor,dispatch,eval,hc]
  | twice a ha => simp only [operate,eval]; rw [ha]

def generatedRoutes : Nat → List Route
  | 0 => [[]]
  | n+1 => (generatedRoutes n).flatMap (fun r => [r ++ [false],r ++ [true]])

theorem two_connector_routes :
    generatedRoutes 2 = [[false,false],[false,true],[true,false],[true,true]] := rfl

def fits (p : Program) (samples : List (Expr × List Bool)) : Bool :=
  samples.all (fun observation => operate p observation.1 == observation.2)

theorem correct_program_fits_actual_records (c : Code) :
    fits (programFor c) (trialRecords c) = true := by
  simp [fits,trialRecords,formed_operation_correspondence]

theorem fit_implies_record_agreement (p : Program) (samples : List (Expr × List Bool))
    (h : fits p samples = true) (e : Expr) (answer : List Bool)
    (present : (e,answer) ∈ samples) : operate p e = answer := by
  have hp := (List.all_eq_true.mp h) (e,answer) present
  simpa using hp

theorem separating_probe_identifies_generated_route (c : Code) (route : Route)
    (distinct : c.first ≠ c.second) (generated : route ∈ generatedRoutes 2)
    (agrees : dispatch route [c.first] [c.second] = eval c orderProbe) :
    route = routeFor c := by
  rw [two_connector_routes] at generated
  simp only [List.mem_cons, List.not_mem_nil, or_false] at generated
  rcases generated with rfl | rfl | rfl | rfl
  all_goals
    rcases c with ⟨a,b,r⟩
    cases a <;> cases b <;> cases r <;>
      simp_all [dispatch,eval,orderProbe,p0,p1,routeFor]

theorem accepted_generated_program_transfers (c : Code) (route : Route)
    (distinct : c.first ≠ c.second) (generated : route ∈ generatedRoutes 2)
    (accepted : fits ⟨c.first,c.second,route⟩ (trialRecords c) = true) (e : Expr) :
    operate ⟨c.first,c.second,route⟩ e = eval c e := by
  have hp := fit_implies_record_agreement ⟨c.first,c.second,route⟩ (trialRecords c)
    accepted orderProbe (eval c orderProbe) (by simp [trialRecords])
  have order := separating_probe_identifies_generated_route c route distinct generated hp
  subst route
  exact formed_operation_correspondence c e

structure Frame where
  wires : Route
  installed : Option Program
  support : Nat
  spent : Nat
  parts : Nat
  usedParts : Nat
  blocked : Bool
  samples : List (Expr × List Bool)
  attempts : List (Route × Bool)
  deriving DecidableEq, Repr

-- The existing learner's records and remaining support are carried forward.
-- Its abstract Code field is not a fallback implementation for this apparatus.
def fromLearner (s : Learner) (parts : Nat) : Frame :=
  ⟨[],none,s.support,0,parts,0,false,s.records,[]⟩

def place (socket : Bool) (s : Frame) : Frame :=
  if s.blocked then s else
  if 1 ≤ s.support ∧ 1 ≤ s.parts then
    {s with wires := s.wires ++ [socket], support := s.support - 1, spent := s.spent + 1, parts := s.parts - 1, usedParts := s.usedParts + 1}
  else {s with blocked := true}

def assemble : Route → Frame → Frame
  | [],s => s
  | socket::rest,s => assemble rest (place socket s)

def inspect (e : Evidence) (s : Frame) : Frame :=
  if s.blocked then s else
  if 1 ≤ s.support then
    let p : Program := ⟨e.first,e.second,s.wires⟩
    let accepted := fits p s.samples
    {s with support := s.support - 1, spent := s.spent + 1, installed := (if accepted then some p else none), attempts := s.attempts ++ [(s.wires,accepted)]}
  else {s with blocked := true}

def discard (s : Frame) : Frame :=
  if s.blocked then s else
  if 1 ≤ s.support then
    {s with wires := [],support := s.support - 1,spent := s.spent + 1,installed := none}
  else {s with blocked := true}

def attempt (e : Evidence) (proposal : Route) (s : Frame) : Frame :=
  let tested := inspect e (assemble proposal s)
  if tested.installed.isSome then tested else discard tested

def search (e : Evidence) : List Route → Frame → Frame
  | [],s => s
  | proposal::rest,s =>
      if s.blocked || s.installed.isSome then s else
      search e rest (attempt e proposal s)

def develop (s : Frame) : Frame :=
  match readEvidence (s.samples.take 3) with
  | none => {s with blocked := true}
  | some e => search e (generatedRoutes 2) s

def respond (s : Frame) (e : Expr) : Option (List Bool × Nat) :=
  match s.installed with
  | none => none
  | some p =>
      let output := operate p e
      if 1 + output.length ≤ s.support then
        some (output,s.support - (1 + output.length)) else none

theorem placing_preserves_support (socket : Bool) (s : Frame) :
    (place socket s).support + (place socket s).spent = s.support+s.spent := by
  simp only [place]
  split
  · rfl
  · split
    · simp only; omega
    · rfl

theorem placing_accounts_parts (socket : Bool) (s : Frame) :
    (place socket s).parts + (place socket s).usedParts = s.parts+s.usedParts := by
  simp only [place]
  split
  · rfl
  · split
    · simp only; omega
    · rfl

theorem assembly_preserves_support (route : Route) (s : Frame) :
    (assemble route s).support+(assemble route s).spent = s.support+s.spent := by
  induction route generalizing s with
  | nil => rfl
  | cons socket rest ih =>
      exact (ih (place socket s)).trans (placing_preserves_support socket s)

theorem inspecting_preserves_support (e : Evidence) (s : Frame) :
    (inspect e s).support+(inspect e s).spent = s.support+s.spent := by
  simp only [inspect]
  split
  · rfl
  · split
    · simp only; omega
    · rfl

theorem discarding_preserves_support (s : Frame) :
    (discard s).support+(discard s).spent = s.support+s.spent := by
  simp only [discard]
  split
  · rfl
  · split
    · simp only; omega
    · rfl

theorem attempt_preserves_support (e : Evidence) (r : Route) (s : Frame) :
    (attempt e r s).support+(attempt e r s).spent = s.support+s.spent := by
  have hi := (inspecting_preserves_support e (assemble r s)).trans
    (assembly_preserves_support r s)
  simp only [attempt]
  split
  · exact hi
  · exact (discarding_preserves_support _).trans hi

theorem search_preserves_support (e : Evidence) (rs : List Route) (s : Frame) :
    (search e rs s).support+(search e rs s).spent = s.support+s.spent := by
  induction rs generalizing s with
  | nil => rfl
  | cons r rs ih =>
    simp only [search]
    split
    · rfl
    · exact (ih (attempt e r s)).trans (attempt_preserves_support e r s)

theorem development_preserves_support (s : Frame) :
    (develop s).support+(develop s).spent = s.support+s.spent := by
  unfold develop
  cases h : readEvidence (s.samples.take 3) with
  | none => rfl
  | some e => exact search_preserves_support e (generatedRoutes 2) s

def prepared (n parts : Nat) (c : Code := usual) : Frame :=
  fromLearner (train c (initial n)) parts
def developed : Frame := develop (prepared 18 4)

theorem interpretation_alone_does_not_supply_route :
    (train usual (initial 18)).code = some usual ∧
    respond (prepared 18 4) novel = none := by decide

theorem incorrect_route_is_built_tried_and_replaced :
    developed.attempts = [([false,false],false),([false,true],true)] ∧
    developed.installed = some (programFor usual) := by decide

theorem development_retains_actual_acquisition :
    developed.samples = (train usual (initial 18)).records := by decide

theorem formed_route_executes_novel_expression :
    respond developed novel = some ([false,false,true],0) := by decide

theorem whole_example_account :
    developed.spent = 7 ∧ developed.support = 4 ∧
    developed.usedParts = 4 ∧ developed.parts = 0 ∧
    7 + developed.spent + developed.support = 18 := by decide

theorem no_parts_preserves_record_but_blocks_formation :
    (develop (prepared 18 0)).samples = trialRecords usual ∧
    (develop (prepared 18 0)).blocked = true ∧
    respond (develop (prepared 18 0)) novel = none := by decide

theorem partial_assembly_keeps_consumption :
    (develop (prepared 18 1)).wires = [false] ∧
    (develop (prepared 18 1)).spent = 1 ∧
    (develop (prepared 18 1)).parts = 0 ∧
    respond (develop (prepared 18 1)) novel = none := by decide

theorem interpreted_and_formed_can_lack_execution_support :
    (develop (prepared 14 4)).installed = some (programFor usual) ∧
    respond (develop (prepared 14 4)) novel = none := by decide

theorem reverse_order_requires_different_formed_route :
    (develop (prepared 22 6 switched)).attempts =
      [([false,false],false),([false,true],false),([true,false],true)] ∧
    respond (develop (prepared 22 6 switched)) novel = some ([true,false,false],0) := by decide

def damaged : Frame := {developed with installed := none}

theorem retained_verdict_does_not_replace_damaged_connection :
    damaged.attempts = developed.attempts ∧ respond damaged novel = none := by decide

-- Enlarging the constructible repertoire can invalidate an earlier probe's
-- sufficiency: duplicate routes are new alternatives, not mere order changes.
def collapsed : Code := ⟨false,false,false⟩
def duplicated : Program := ⟨false,false,[false,false]⟩

theorem old_record_can_admit_wrong_constructed_operation :
    fits duplicated (trialRecords collapsed) = true ∧
    operate duplicated novel ≠ eval collapsed novel := by decide

theorem expanded_repertoire_can_form_a_failing_route :
    (develop (prepared 15 2 collapsed)).installed = some duplicated ∧
    respond (develop (prepared 15 2 collapsed)) novel = some ([false,false,false,false],0) := by decide

theorem asymmetric_composition_exposes_the_new_failure :
    fits duplicated (trialRecords collapsed ++ [(novel,eval collapsed novel)]) = false ∧
    fits (programFor collapsed) (trialRecords collapsed ++ [(novel,eval collapsed novel)]) = true := by decide


-- A further encounter is a supplied reference demonstration, not the output
-- of the presently installed (possibly wrong) operation.
def encounter (c : Code) (e : Expr) (s : Frame) : Frame :=
  if s.blocked then s else
  let cost := 1 + (eval c e).length
  if cost ≤ s.support then
    {s with samples := s.samples ++ [(e,eval c e)], support := s.support - cost, spent := s.spent + cost}
  else {s with blocked := true}

def reconsider (s : Frame) : Frame :=
  match readEvidence (s.samples.take 3) with
  | none => {s with blocked := true}
  | some e =>
    let tested := inspect e s
    if tested.installed.isSome then tested else develop (discard tested)

theorem encounter_preserves_support (c : Code) (e : Expr) (s : Frame) :
    (encounter c e s).support + (encounter c e s).spent = s.support+s.spent := by
  simp only [encounter]
  split
  · rfl
  · dsimp only
    split
    · simp only; omega
    · rfl

theorem reconsideration_preserves_support (s : Frame) :
    (reconsider s).support+(reconsider s).spent = s.support+s.spent := by
  unfold reconsider
  cases h : readEvidence (s.samples.take 3) with
  | none => rfl
  | some e =>
    dsimp only
    split
    · exact inspecting_preserves_support e s
    · exact (development_preserves_support _).trans
        ((discarding_preserves_support _).trans (inspecting_preserves_support e s))

def corrected (n parts : Nat) : Frame :=
  reconsider (encounter collapsed novel (develop (prepared n parts collapsed)))
def further : Expr := .join p0 (.twice p1)

theorem fresh_record_changes_actual_reconstruction :
    (corrected 27 6).samples = trialRecords collapsed ++ [(novel,eval collapsed novel)] ∧
    (corrected 27 6).attempts =
      [([false,false],true),([false,false],false),([false,false],false),([false,true],true)] ∧
    (corrected 27 6).installed = some (programFor collapsed) := by decide

theorem repaired_operation_uses_a_further_untrained_expression :
    further ∉ ((corrected 27 6).samples.map Prod.fst) ∧
    respond (corrected 27 6) further = some ([false,false,false],0) := by decide

theorem repair_keeps_the_cost_of_failure :
    (corrected 27 6).spent = 16 ∧ (corrected 27 6).support = 4 ∧
    (corrected 27 6).usedParts = 6 ∧ (corrected 27 6).parts = 0 ∧
    7 + (corrected 27 6).spent + (corrected 27 6).support = 27 := by decide

theorem discrepancy_alone_does_not_supply_repair_parts :
    (corrected 27 2).blocked = true ∧
    (corrected 27 2).samples = trialRecords collapsed ++ [(novel,eval collapsed novel)] ∧
    (corrected 27 2).installed = none ∧
    respond (corrected 27 2) further = none := by decide

theorem unobserved_failure_can_retain_wrong_operation :
    (develop (prepared 27 6 collapsed)).installed = some duplicated ∧
    respond (develop (prepared 27 6 collapsed)) further = some ([false,false],14) := by decide

def extent : Expr → Nat
  | .atom _ => 1
  | .join a b => extent a + extent b
  | .twice a => extent a + extent a

theorem equal_primitive_effects_preserve_extent (c : Code) (same : c.second = c.first)
    (e : Expr) : eval c e = List.replicate (extent e) c.first := by
  induction e with
  | atom b => cases b <;> simp [eval,extent,same]
  | join a b ha hb =>
    cases h : c.reversed <;>
      simp [eval,h,ha,hb,extent,List.replicate_add,Nat.add_comm]
  | twice a ha => simp [eval,ha,extent,List.replicate_add]

theorem indistinguishable_reversal_preserves_every_expression
    (b r : Bool) (e : Expr) : eval ⟨b,b,r⟩ e = eval ⟨b,b,!r⟩ e := by
  rw [equal_primitive_effects_preserve_extent _ rfl,
      equal_primitive_effects_preserve_extent _ rfl]

theorem extra_probe_restores_transfer_for_generated_routes
    (c : Code) (route : Route) (generated : route ∈ generatedRoutes 2)
    (accepted : fits ⟨c.first,c.second,route⟩
      (trialRecords c ++ [(novel,eval c novel)]) = true) (e : Expr) :
    operate ⟨c.first,c.second,route⟩ e = eval c e := by
  rw [two_connector_routes] at generated
  simp only [List.mem_cons,List.not_mem_nil,or_false] at generated
  rcases generated with rfl | rfl | rfl | rfl
  all_goals
    rcases c with ⟨a,b,r⟩
    cases a <;> cases b <;> cases r
    simp [fits,trialRecords,operate,dispatch,eval,p0,p1,orderProbe,novel] at accepted
  all_goals
    first
    | exact formed_operation_correspondence _ e
    | exact (formed_operation_correspondence _ e).trans
        (indistinguishable_reversal_preserves_every_expression _ _ e)

end Generative.CompositionalFormation

