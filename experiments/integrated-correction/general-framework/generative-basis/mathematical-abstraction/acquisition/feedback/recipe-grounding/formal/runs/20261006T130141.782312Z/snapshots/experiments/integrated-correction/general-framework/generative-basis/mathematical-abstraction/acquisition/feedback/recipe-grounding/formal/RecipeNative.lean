import CalibrationRevision
import RecipeGrounding

/-!
Exact event-attempt semantics for the additive native decoder branch. The
separate fixture module checks the actual scheduler's words, guards and full
states. Arbitrary event words are not asserted to be native executions.

`referenceFormation` encodes the new controller phase absent from the inherited
phase enumeration: when true its inherited phase is oldInterface. It is a
representation coordinate of that same finite phase, not a new hardware cell.
The reference/use maps are physical-law coordinates, never selector inputs.
-/
namespace RecipeNative
open RemainingDependency
open RecipeGrounding
set_option maxRecDepth 65536
set_option maxHeartbeats 8000000

inductive RecipePhase where
  | absent | referenceFormation | ready | unresolved | active
  deriving DecidableEq, Repr

structure Recipe where
  wires : Pair (Option Bool) := ⟨none, none⟩
  references : Pair (Option Datum) := ⟨none, none⟩
  issued : Option Bool := none
  jig : Option Bool := none
  contact : Option Datum := none
  ready : Bool := false
  conflict : Bool := false
  cursor : Nat := 0
  activated : Bool := false
  address : Option Bool := none
  phase : RecipePhase := .absent
  deriving DecidableEq, Repr

structure Config where
  referenceMap : Table
  initialUseMap : Table
  referenceFaults : Pair Fault := ⟨.faithful, .faithful⟩
  misforce : Bool := false
  formationClamp : Bool := false
  rawClamp : Bool := false
  deriving DecidableEq, Repr

structure State where
  parent : RemainingDependency.State
  config : Config
  body : CalibrationRevision.Body
  recipe : Recipe := {}
  useMap : Table
  referenceFormation : Bool := false
  deriving DecidableEq, Repr

def paid (s : State) (w l t e r : Nat) (effect : State → State) : State :=
  let debit := charge s.body.account w l t e r
  if debit.2 = .none then effect {s with body := {s.body with account := debit.1}} else s

def mapDatum (table : Table) (datum : Option Datum) : Option Datum :=
  datum.map (fun d => {d with response := table.read d.response})

def referenceDatum (s : State) : Option Datum := do
  let issued ← s.recipe.issued
  let jig ← s.recipe.jig
  pure ⟨s.body.context, issued, s.config.referenceMap.read jig⟩

def boundReference (s : State) : Option Datum := do
  let selected ← s.parent.body.selected
  let expected ← s.parent.body.tags.get selected
  let issued ← s.recipe.issued
  let datum ← s.recipe.contact
  if datum.context = expected ∧ datum.relay = issued then some datum else none

def bind (r : Recipe) (setting : Bool) (clamped : Bool) : Recipe :=
  let datum := r.references.get setting
  let t := {r with address := datum.map Datum.response}
  match datum with
  | none => t
  | some d =>
      if clamped then t
      else match r.wires.get d.response with
        | none => {t with wires := r.wires.set d.response (some d.relay)}
        | some previous => if previous = d.relay then t else {t with conflict := true}

def isReady (r : Recipe) : Bool :=
  r.references.zero.isSome && r.references.one.isSome &&
  r.wires.zero.isSome && r.wires.one.isSome && !r.conflict

def decoder (r : Recipe) : Option Table := do
  let zero ← r.wires.zero
  let one ← r.wires.one
  pure ⟨zero, one⟩

def decodeContact (r : Recipe) (rawClamp : Bool) (contact : Option Datum) : Option Datum := do
  let d ← contact
  let value ← r.wires.get d.response
  pure {d with response := if rawClamp then d.response else value}

inductive Event where
  | wait (units : Nat) | assemble | force (setting : Bool) | contact (setting : Bool)
  | recordReference (setting : Bool) | bindRow (setting : Bool) | readiness | activate
  | boundaryChange | unbind | decode | fullContact | weakContact
  | fullWrite | filterFull | reviseApplication | choose | commit | command (setting : Bool)
  | challenge | weakWrite | filterWeak | reviseDiagnosis | retain
  deriving DecidableEq, Repr

def inherited (s : State) (e : CalibrationRevision.Event) : State :=
  {s with body := CalibrationRevision.advance s.parent {} s.body e}

def step (s : State) : Event → State
  | .wait units => inherited s (.wait units)
  | .assemble => paid s 26 60 8 ticks 0 fun t => {t with body := {t.body with installed := true}, referenceFormation := true, recipe := {t.recipe with phase := .referenceFormation}}
  | .force setting => paid s 1 s.body.account.live 2 16384 0 fun t => {t with recipe := {t.recipe with issued := some setting, cursor := (if setting then 1 else 0), jig := some (if t.config.misforce then !setting else setting)}}
  | .contact setting => paid s 0 s.body.account.live 2 16384 0 fun t => {t with recipe := {t.recipe with contact := channel (t.config.referenceFaults.get setting) (referenceDatum t)}}
  | .recordReference setting => paid s 1 s.body.account.live 2 0 2 fun t => {t with recipe := {t.recipe with references := t.recipe.references.set setting (boundReference t), contact := none}}
  | .bindRow setting => paid s 1 s.body.account.live 2 0 1 fun t => {t with recipe := bind t.recipe setting t.config.formationClamp}
  | .readiness => paid s 2 s.body.account.live 2 0 1 fun t => {t with recipe := {t.recipe with ready := isReady t.recipe, phase := if isReady t.recipe then .ready else .unresolved}}
  | .activate => paid s 16 s.body.account.live 2 0 16 fun t => {t with body := {t.body with mask := some 65535, phase := .formed}, referenceFormation := false, recipe := {t.recipe with references := ⟨none,none⟩, issued := none, jig := none, contact := none, address := none, cursor := 0, activated := true, phase := .active}}
  | .boundaryChange => {s with useMap := ⟨!s.config.referenceMap.zero, !s.config.referenceMap.one⟩}
  | .unbind => paid s 1 s.body.account.live 1 0 1 fun t => {t with recipe := {t.recipe with wires := t.recipe.wires.set false none}}
  | .decode => paid s 1 s.body.account.live 1 0 0 fun t => {t with recipe := {t.recipe with address := t.body.contact.map Datum.response}, body := {t.body with contact := decodeContact t.recipe t.config.rawClamp t.body.contact}}
  | .fullContact => paid s 0 s.body.account.live 2 16384 0 fun t => {t with body := {t.body with contact := mapDatum t.useMap (CalibrationRevision.stockDatum t.body t.parent.body.selected)}}
  | .weakContact => paid s 0 s.body.account.live 2 16384 0 fun t => {t with body := {t.body with contact := mapDatum t.useMap t.body.pending, pending := none}}
  | .fullWrite => inherited s .fullWrite
  | .filterFull => inherited s .filterFull
  | .reviseApplication => inherited s .reviseApplication
  | .choose => inherited s .choose
  | .commit => inherited s .commit
  | .command setting => inherited s (.command setting)
  | .challenge => inherited s .challenge
  | .weakWrite => inherited s .weakWrite
  | .filterWeak => inherited s .filterWeak
  | .reviseDiagnosis => inherited s .reviseDiagnosis
  | .retain => inherited s .retain

def run : State → List Event → State
  | s, [] => s
  | s, e :: es => run (step s e) es

def process : Generative.Process State Event where step s e t := step s e = t

def entrance (parent : RemainingDependency.State) (config : Config) : State :=
  {parent := parent, config := config, body := (CalibrationRevision.entrance parent {}).body,
   useMap := config.initialUseMap}

def total (s : State) : Nat := s.body.account.fuel + s.body.account.spent

theorem paid_conserves (s : State) (w l t e r : Nat) (effect : State → State)
    (preserves : ∀ a, (effect a).body.account = a.body.account) :
    total (paid s w l t e r effect) = total s := by
  unfold paid
  dsimp only
  split
  · unfold total
    rw [preserves]
    exact charge_conserves _ _ _ _ _ _
  · rfl

theorem inherited_conserves (s : State) (e : CalibrationRevision.Event) :
    total (inherited s e) = total s :=
  CalibrationRevision.advance_account_conserved _ _ _ _

theorem every_attempt_preserves_account (s : State) (e : Event) : total (step s e) = total s := by
  cases e <;> simp only [step]
  all_goals first | exact inherited_conserves _ _ | rfl | apply paid_conserves; intro a; rfl

theorem run_preserves_account (s : State) (events : List Event) : total (run s events) = total s := by
  induction events generalizing s with
  | nil => rfl
  | cons e es ih => exact (ih _).trans (every_attempt_preserves_account s e)

theorem every_attempt_preserves_ancestor_and_stocks (s : State) (e : Event) :
    (step s e).parent = s.parent ∧ (step s e).body.stocks = s.body.stocks := by
  cases e <;> simp only [step]
  all_goals first
    | exact ⟨rfl, CalibrationRevision.advance_stocks_preserved _ _ _ _⟩
    | exact ⟨rfl, rfl⟩
    | exact ⟨True.intro, True.intro⟩
    | unfold paid; dsimp only; split <;> exact ⟨rfl, rfl⟩

theorem run_preserves_ancestor_and_stocks (s : State) (events : List Event) :
    (run s events).parent = s.parent ∧ (run s events).body.stocks = s.body.stocks := by
  induction events generalizing s with
  | nil => exact ⟨rfl, rfl⟩
  | cons e es ih =>
      have a := ih (step s e)
      have b := every_attempt_preserves_ancestor_and_stocks s e
      exact ⟨a.1.trans b.1, a.2.trans b.2⟩

theorem run_is_core_trace (s : State) (events : List Event) :
    Generative.Trace process s events (run s events) := by
  induction events generalizing s with
  | nil => exact .nil s
  | cons e es ih => exact .cons rfl (ih _)

/-- The native non-overwriting binder uses exactly the acquired reference rows. -/
def recordedPair (zeroReply oneReply : Bool) : Recipe :=
  {references := ⟨some ⟨1,false,zeroReply⟩, some ⟨1,true,oneReply⟩⟩}

theorem actual_binder_matches_selected_decoder (zeroReply oneReply : Bool) :
    let wired := bind (bind (recordedPair zeroReply oneReply) false false) true false
    (if wired.conflict then none else decoder wired) = selectDecoder zeroReply oneReply := by
  cases zeroReply <;> cases oneReply <;> decide

theorem actual_bound_decoder_recovers (f : Bool → Bool) (table : Table)
    (selected : (let wired := bind (bind (recordedPair (f false) (f true)) false false) true false
      if wired.conflict then none else decoder wired) = some table) : Recovers f table := by
  rw [actual_binder_matches_selected_decoder] at selected
  exact actual_selected_decoder_recovers f table selected

theorem decoding_uses_the_actual_stored_rows (r : Recipe) (table : Table)
    (formed : decoder r = some table) (context : Nat) (setting raw : Bool) :
    decodeContact r false (some ⟨context,setting,raw⟩) =
      some ⟨context,setting,table.read raw⟩ := by
  rcases r with ⟨⟨zero,one⟩,rest⟩
  cases zero <;> cases one <;> simp [decoder] at formed
  all_goals subst table; cases raw <;> rfl

theorem absent_row_is_not_repaired_by_ready (r : Recipe) (context : Nat) (setting raw : Bool)
    (missing : r.wires.get raw = none) :
    decodeContact {r with ready := true} false (some ⟨context,setting,raw⟩) = none := by
  simp [decodeContact, missing]

theorem inherited_complete_pipeline_account :
    let old := CalibrationRevision.continuation
      (CalibrationRevision.entrance CalibrationRevision.mismatchParent {})
    old.body.account.start = 428018 ∧ old.body.account.spent = 363251 ∧
    old.body.account.fuel = 64767 := by decide

/-- A lower bound for this declared tariff, not a universal calibration cost. -/
theorem old_pipeline_plus_four_reference_surcharges_is_unfunded (fuel spent : Nat)
    (closed : fuel + spent = 428018) (unreducedWork : 363251 + 4 * 16384 ≤ spent) : False := by
  omega

#print axioms paid_conserves
#print axioms inherited_conserves
#print axioms every_attempt_preserves_account
#print axioms run_preserves_account
#print axioms every_attempt_preserves_ancestor_and_stocks
#print axioms run_preserves_ancestor_and_stocks
#print axioms run_is_core_trace
#print axioms actual_binder_matches_selected_decoder
#print axioms actual_bound_decoder_recovers
#print axioms decoding_uses_the_actual_stored_rows
#print axioms absent_row_is_not_repaired_by_ready
#print axioms inherited_complete_pipeline_account
#print axioms old_pipeline_plus_four_reference_surcharges_is_unfunded

end RecipeNative
