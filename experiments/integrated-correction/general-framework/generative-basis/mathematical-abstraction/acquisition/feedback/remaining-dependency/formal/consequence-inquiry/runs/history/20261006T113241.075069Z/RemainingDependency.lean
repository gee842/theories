import GenerativeCore

/-!
An additive operational model at the actually retained inquiry endpoint. Fuel is
measured in 1/65536 units; source and destination stocks are whole units. The
ancestral learner is a retained coordinate, not reimplemented by this module.
The relay family, tariffs, calibrated weak/full-load relation and preference for
bypass are supplied local laws. No ethical criterion or runtime need oracle is
introduced. Finite correspondence fixtures bind this law to saved native events.
-/
namespace RemainingDependency
set_option maxRecDepth 32768
set_option maxHeartbeats 4000000

def ticks : Nat := 65536

structure Pair (α : Type) where
  zero : α
  one : α
  deriving DecidableEq, Repr

def Pair.get (p : Pair α) (r : Bool) : α := if r then p.one else p.zero

def Pair.set (p : Pair α) (r : Bool) (x : α) : Pair α :=
  if r then {p with one := x} else {p with zero := x}

structure Account where
  fuel : Nat
  start : Nat := 0
  spent : Nat := 0
  live : Nat := 26
  peak : Nat := 33
  capacity : Nat := 256
  deriving DecidableEq, Repr

def tariff (a : Account) (work newLive temporary extra rewrites : Nat) : Nat :=
  1024 * work + (max a.live newLive + temporary) * (work + 1) +
  1024 * (newLive - a.live + rewrites) + extra

inductive Error where
  | none | funding | capacity | source | invalid
  deriving DecidableEq, Repr

/-- Workspace is zero at this exact cut and throughout this suffix. -/
def charge (a : Account) (work newLive temporary extra rewrites : Nat) : Account × Error :=
  let peak := max a.live newLive + temporary
  let bill := tariff a work newLive temporary extra rewrites
  if a.capacity < peak then (a, .capacity)
  else if a.fuel < bill then (a, .funding)
  else ({a with fuel := a.fuel - bill, spent := a.spent + bill,
                 live := newLive, peak := max a.peak peak}, .none)

theorem charge_conserves (a : Account) (w l t e r : Nat) :
    (charge a w l t e r).1.fuel + (charge a w l t e r).1.spent = a.fuel + a.spent := by
  by_cases hc : a.capacity < max a.live l + t
  · simp [charge, hc]
  · by_cases hf : a.fuel < tariff a w l t e r
    · simp [charge, hc, hf]
    · simp only [charge, hc, hf, ↓reduceIte]
      omega

theorem charge_never_increases_fuel (a : Account) (w l t e r : Nat) :
    (charge a w l t e r).1.fuel ≤ a.fuel := by
  unfold charge
  dsimp only
  split
  · exact Nat.le_refl _
  · split
    · exact Nat.le_refl _
    · exact Nat.sub_le _ _

theorem charge_denial_preserves_account (a : Account) (w l t e r : Nat)
    (h : (charge a w l t e r).2 ≠ .none) :
    (charge a w l t e r).1 = a := by
  by_cases hc : a.capacity < max a.live l + t
  · simp [charge, hc]
  · by_cases hf : a.fuel < tariff a w l t e r
    · simp [charge, hc, hf]
    · simp [charge, hc, hf] at h

/-- Complete known evidence is required; unknown is not the negative bit. -/
def choose (p : Pair (Option Bool)) : Option Bool :=
  match p.zero, p.one with
  | some a, some b => if a then some false else if b then some true else none
  | _, _ => none

def faithful (f : Pair Bool) : Pair (Option Bool) := ⟨some f.zero, some f.one⟩

theorem chosen_setting_supported (f : Pair Bool) (r : Bool)
    (h : choose (faithful f) = some r) : f.get r = true := by
  rcases f with ⟨a,b⟩
  cases a <;> cases b <;> cases r <;> simp_all [choose, faithful, Pair.get]

theorem productive_pair_has_selected_setting (f : Pair Bool)
    (h : f.zero = true ∨ f.one = true) :
    ∃ r, choose (faithful f) = some r ∧ f.get r = true := by
  rcases f with ⟨a,b⟩
  cases a <;> cases b <;> simp_all [choose, faithful, Pair.get]

theorem absent_evidence_is_not_negative :
    choose ⟨some true, none⟩ = none ∧ choose ⟨some true, some false⟩ = some false := by
  decide

theorem no_constant_setting_serves_opposed_relations :
    ¬ ∃ r : Bool, (Pair.get ⟨false,true⟩ r = true ∧ Pair.get ⟨true,false⟩ r = true) := by
  rintro ⟨r, h⟩
  cases r <;> simp_all [Pair.get]

/-- This is a physical weak/full-load calibration condition, not information
available to the consumer. It may be deliberately violated in adverse cases. -/
def Calibrated (weak full : Pair Bool) : Prop := ∀ r, weak.get r = full.get r

theorem calibrated_selected_setting_transfers (weak full : Pair Bool) (r : Bool)
    (hc : Calibrated weak full) (h : choose (faithful weak) = some r) :
    full.get r = true := by
  rw [← hc r]
  exact chosen_setting_supported weak r h

structure Ancestor where
  alphabet : List String := ["a"]
  initial : Nat := 0
  controlLocation : String := "reported_episode_complete"
  outputs : List Bool := [true, true, false]
  transitions : List Nat := [1, 2, 0]
  table : List (Option Bool) := [some false, some true, none]
  retained : Bool := true
  componentDone : Bool := true
  deriving DecidableEq, Repr

structure Datum where
  context : Nat
  relay : Bool
  response : Bool
  deriving DecidableEq, Repr

/-- Only an actually supplied datum with both matching bindings can be stored. -/
def decode (context : Nat) (r : Bool) (d : Option Datum) : Option Bool :=
  match d with
  | none => none
  | some d => if d.context = context ∧ d.relay = r then some d.response else none

theorem faithful_bound_datum_decodes (c : Nat) (r b : Bool) :
    decode c r (some ⟨c, r, b⟩) = some b := by simp [decode]

theorem wrong_context_stays_unknown (c c' : Nat) (r r' b : Bool) (h : c' ≠ c) :
    decode c r (some ⟨c',r',b⟩) = none := by simp [decode, h]

theorem missing_stays_unknown (c : Nat) (r : Bool) : decode c r none = none := rfl

structure Stocks where
  source : Nat := 10
  load : Nat := 0
  waste : Nat := 0
  deriving DecidableEq, Repr

/-- This distinct full-load effect is never executed by the weak challenges. -/
def discharge (p : Stocks) (response : Bool) : Stocks :=
  if p.source < 10 then p
  else {source := p.source - 10, load := p.load + if response then 10 else 0,
        waste := p.waste + if response then 0 else 10}

def Stocks.total (p : Stocks) : Nat := p.source + p.load + p.waste

theorem discharge_conserves (p : Stocks) (b : Bool) :
    (discharge p b).total = p.total := by
  unfold discharge
  split
  · rfl
  · cases b <;> simp only [Stocks.total, Bool.false_eq_true, ↓reduceIte] <;> omega

theorem supported_discharge_delivers (p : Stocks) (hs : 10 ≤ p.source) :
    (discharge p true).load = p.load + 10 ∧
    (discharge p true).source = p.source - 10 ∧
    (discharge p true).waste = p.waste := by
  simp [discharge, Nat.not_lt.mpr hs]

theorem unsupported_discharge_wastes (p : Stocks) (hs : 10 ≤ p.source) :
    (discharge p false).load = p.load ∧ (discharge p false).waste = p.waste + 10 := by
  simp [discharge, Nat.not_lt.mpr hs]

/-- Source availability precedes all transfer charges. Future load stock never
prefinances actor expenditure and is never credited to that actor's fuel. -/
def fullTransfer (a : Account) (p : Stocks) (response : Bool) : Account × Stocks × Error :=
  if p.source < 10 then (a, p, .source)
  else
    let q := charge a 1 a.live 2 16384 0
    if q.2 = .none then (q.1, discharge p response, .none)
    else (q.1, p, q.2)

theorem transfer_actor_account_conserved (a : Account) (p : Stocks) (b : Bool) :
    (fullTransfer a p b).1.fuel + (fullTransfer a p b).1.spent = a.fuel + a.spent := by
  unfold fullTransfer
  split
  · rfl
  · dsimp only
    split
    · exact charge_conserves _ _ _ _ _ _
    · exact charge_conserves _ _ _ _ _ _

theorem transfer_stocks_conserved (a : Account) (p : Stocks) (b : Bool) :
    (fullTransfer a p b).2.1.total = p.total := by
  unfold fullTransfer
  split
  · rfl
  · dsimp only
    split
    · exact discharge_conserves p b
    · rfl

theorem empty_source_cannot_debit_actor (a : Account) (p : Stocks) (b : Bool)
    (hs : p.source < 10) : fullTransfer a p b = (a, p, .source) := by
  simp [fullTransfer, hs]

theorem affordable_calibrated_selection_delivers (a : Account) (p : Stocks)
    (weak full : Pair Bool) (r : Bool)
    (hc : Calibrated weak full) (hh : choose (faithful weak) = some r)
    (hs : 10 ≤ p.source)
    (hp : (charge a 1 a.live 2 16384 0).2 = .none) :
    (fullTransfer a p (full.get r)).2.1.load = p.load + 10 := by
  have hr := calibrated_selected_setting_transfers weak full r hc hh
  simp [fullTransfer, Nat.not_lt.mpr hs, hp, hr, discharge]

inductive Mode where
  | componentComplete | awaitingAssay | unresolved | noSupportedRoute
  | componentCompleteStop | selectedBypass | selectedRelay | serviceIssued
  deriving DecidableEq, Repr

def resultMode (p : Pair (Option Bool)) : Mode :=
  match p.zero, p.one with
  | some a, some b => if a then .selectedBypass else if b then .selectedRelay else .noSupportedRoute
  | _, _ => .unresolved

inductive Fault where
  | faithful | missing | wrongContext | wrongSetting | flip
  deriving DecidableEq, Repr

structure Config where
  weak : Pair Bool
  full : Pair Bool
  channels : Pair Fault := ⟨.faithful, .faithful⟩
  clamp : Bool := false
  deriving DecidableEq, Repr

structure Body where
  account : Account
  stocks : Stocks
  context : Nat := 1
  relay : Bool := false
  pending : Option Datum := none
  held : Bool := false
  installed : Bool := false
  retained : Bool := false
  mode : Mode := .componentComplete
  values : Pair (Option Bool) := ⟨none,none⟩
  tags : Pair (Option Nat) := ⟨none,none⟩
  contact : Option Datum := none
  candidate : Option Bool := none
  readMode : Option Mode := none
  selected : Option Bool := none
  deriving DecidableEq, Repr

structure State where
  ancestor : Ancestor
  config : Config
  body : Body
  deriving DecidableEq, Repr

/-- A denied charge changes no physical, acquired or control coordinate. -/
def paid (b : Body) (w l t e r : Nat) (effect : Body → Body) : Body :=
  let debit := charge b.account w l t e r
  if debit.2 = .none then effect {b with account := debit.1} else b

def channel (fault : Fault) : Option Datum → Option Datum
  | none => none
  | some d => match fault with
    | .faithful => some d
    | .missing => none
    | .wrongContext => some {d with context := 2}
    | .wrongSetting => some {d with relay := !d.relay}
    | .flip => some {d with response := !d.response}

inductive Event where
  | wait (units : Nat) | install | command (r : Bool) | challenge
  | contact (probe : Bool) | write (r : Bool) | read | commit
  | contextChange | hold | release | transfer | retain
  deriving DecidableEq, Repr

/-- Meaningful operations compute their own bills and effects. Denials leave
state intact; the externally supplied protocol chooses the next request.
This total law describes event attempts. Arbitrary request words need not obey
the native scheduler; fixture correspondence separately checks its actual words. -/
def advance (cfg : Config) (b : Body) : Event → Body
  | .wait n => paid b 0 b.account.live 0 (ticks*n) 0 id
  | .install => paid b 8 (b.account.live+8) 8 ticks 0 fun t =>
      {t with installed := true, mode := .awaitingAssay}
  | .command r => paid b 1 b.account.live 2 16384 0 fun t =>
      {t with relay := r, held := false}
  | .challenge => paid b 1 b.account.live 2 16384 0 fun t =>
      {t with pending := some ⟨t.context,t.relay,cfg.weak.get t.relay⟩}
  | .contact r => paid b 0 b.account.live 2 16384 0 fun t =>
      {t with contact := channel (cfg.channels.get r) t.pending, pending := none}
  | .write r => paid b 1 b.account.live 2 0 2 fun t =>
      let datum := decode 1 r t.contact
      {t with values := t.values.set r datum,
              tags := t.tags.set r (if datum.isSome then some 1 else none), contact := none}
  | .read => paid b 2 b.account.live 2 0 0 fun t =>
      {t with candidate := choose t.values, readMode := some (resultMode t.values)}
  | .commit => paid b 1 b.account.live 2 0 2 fun t =>
      if cfg.clamp then {t with selected := none, mode := .componentCompleteStop}
      else {t with selected := t.candidate, mode := t.readMode.getD .componentComplete}
  | .contextChange => {b with context := 2}
  | .hold => paid b 1 b.account.live 2 16384 0 fun t => {t with held := true}
  | .release => paid b 1 b.account.live 2 0 0 fun t => {t with held := false}
  | .transfer =>
      let response := (cfg.full.get b.relay) && ((!b.relay) || b.held)
      let moved := fullTransfer b.account b.stocks response
      if moved.2.2 = .none then
        {b with account := moved.1, stocks := moved.2.1, held := false, mode := .serviceIssued}
      else b
  | .retain => paid b 1 b.account.live 0 (1024*b.account.live) 0 fun t => {t with retained := true}

def step (s : State) (e : Event) : State := {s with body := advance s.config s.body e}

def process : Generative.Process State Event where step s e t := step s e = t

def run : State → List Event → State
  | s, [] => s
  | s, e::es => run (step s e) es

theorem ancestral_coordinates_unchanged (s : State) (e : Event) :
    (step s e).ancestor = s.ancestor := rfl

theorem run_ancestral_coordinates_unchanged (s : State) (es : List Event) :
    (run s es).ancestor = s.ancestor := by
  induction es generalizing s with
  | nil => rfl
  | cons e es ih => exact ih (step s e)

theorem completed_component_stays_complete (s : State) (es : List Event)
    (h : s.ancestor.componentDone = true) : (run s es).ancestor.componentDone = true := by
  rw [run_ancestral_coordinates_unchanged]
  exact h

theorem run_is_core_trace (s : State) (es : List Event) :
    Generative.Trace process s es (run s es) := by
  induction es generalizing s with
  | nil => exact .nil s
  | cons e es ih => exact .cons rfl (ih (step s e))

/-- Native truth is not an input to the acquired pair's decision function. -/
theorem consumer_read_ignores_latent_law (a b : Config) (s : Body) :
    advance a s .read = advance b s .read := rfl

theorem weak_challenge_does_not_supply_load (cfg : Config) (s : Body) :
    (advance cfg s .challenge).stocks = s.stocks := by
  simp only [advance, paid]
  split <;> rfl

theorem slot_write_does_not_supply_load (cfg : Config) (s : Body) (r : Bool) :
    (advance cfg s (.write r)).stocks = s.stocks := by
  simp only [advance, paid]
  split <;> rfl

def actorTotal (b : Body) : Nat := b.account.fuel + b.account.spent

theorem paid_account_conserved (b : Body) (w l t e r : Nat) (f : Body → Body)
    (h : ∀ z, (f z).account = z.account) :
    actorTotal (paid b w l t e r f) = actorTotal b := by
  unfold paid
  dsimp only
  split
  · unfold actorTotal
    rw [h]
    exact charge_conserves _ _ _ _ _ _
  · rfl

theorem paid_stocks_preserved (b : Body) (w l t e r : Nat) (f : Body → Body)
    (h : ∀ z, (f z).stocks = z.stocks) : (paid b w l t e r f).stocks = b.stocks := by
  unfold paid
  dsimp only
  split
  · exact h _
  · rfl

theorem advance_actor_account_conserved (cfg : Config) (s : Body) (e : Event) :
    actorTotal (advance cfg s e) = actorTotal s := by
  cases e with
  | contextChange => rfl
  | transfer =>
    unfold advance
    dsimp only
    split
    · exact transfer_actor_account_conserved _ _ _
    · rfl
  | commit =>
    apply paid_account_conserved
    intro z
    cases cfg.clamp <;> rfl
  | _ => apply paid_account_conserved; intro z; rfl

theorem advance_stock_account_conserved (cfg : Config) (s : Body) (e : Event) :
    (advance cfg s e).stocks.total = s.stocks.total := by
  cases e with
  | contextChange => rfl
  | transfer =>
    unfold advance
    dsimp only
    split
    · exact transfer_stocks_conserved _ _ _
    · rfl
  | commit =>
    have h := paid_stocks_preserved s 1 s.account.live 2 0 2
      (fun t => if cfg.clamp then {t with selected := none, mode := .componentCompleteStop}
        else {t with selected := t.candidate, mode := t.readMode.getD .componentComplete})
      (by intro z; cases cfg.clamp <;> rfl)
    exact congrArg Stocks.total h
  | _ =>
    apply congrArg Stocks.total
    apply paid_stocks_preserved
    intro z
    rfl

theorem run_actor_account_conserved (s : State) (es : List Event) :
    actorTotal (run s es).body = actorTotal s.body := by
  induction es generalizing s with
  | nil => rfl
  | cons e es ih =>
    rw [run, ih]
    exact advance_actor_account_conserved _ _ _

theorem run_stock_account_conserved (s : State) (es : List Event) :
    (run s es).body.stocks.total = s.body.stocks.total := by
  induction es generalizing s with
  | nil => rfl
  | cons e es ih =>
    rw [run, ih]
    exact advance_stock_account_conserved _ _ _

/-- The fixed inherited consumption closes the original whole history. It is
not restored fuel; stock at the load never becomes actor income. -/
def wholeTotal (inherited : Nat) (s : State) : Nat :=
  inherited + actorTotal s.body + ticks * s.body.stocks.total

theorem whole_history_conserved (inherited : Nat) (s : State) (es : List Event) :
    wholeTotal inherited (run s es) = wholeTotal inherited s := by
  unfold wholeTotal
  rw [run_actor_account_conserved, run_stock_account_conserved]

theorem finite_original_support_bounds_fuel (s : State) (es : List Event) :
    (run s es).body.account.fuel ≤ actorTotal s.body := by
  have h := run_actor_account_conserved s es
  unfold actorTotal at h ⊢
  omega

/-- The primary actual retained cut, after its old retention charge. -/
def entrance (cfg : Config) : State :=
  {ancestor := {}, config := cfg,
   body := {account := {fuel := 713012, start := 713012}, stocks := {}}}

def assayEvents : List Event :=
  [.install, .command false, .challenge, .contact false, .write false,
   .command true, .challenge, .contact true, .write true, .read, .commit]

/-- The final requested operations depend on the acquired/committed selection.
The two identifying probes and the response repertoire remain supplied. -/
def serviceEvents (s : State) : List Event :=
  match s.body.selected with
  | none => [.retain]
  | some r => [.command r, if r then .hold else .release, .transfer, .retain]

/-- Nominal funded protocol. Native adverse histories abort remaining assay/use
requests after denial and separately attempt retention; saved fixtures check them. -/
def continuation (s : State) : State :=
  let acquired := run s assayEvents
  run acquired (serviceEvents acquired)

theorem truthful_paid_assay_acquires_pair (f : Pair Bool) :
    (run (entrance {weak := f, full := f}) assayEvents).body.values = faithful f := by
  rcases f with ⟨a,b⟩
  cases a <;> cases b <;> decide

theorem truthful_paid_assay_commits_supported_choice (f : Pair Bool) :
    (run (entrance {weak := f, full := f}) assayEvents).body.selected = choose (faithful f) := by
  rcases f with ⟨a,b⟩
  cases a <;> cases b <;> decide

theorem actual_dependent_service :
    let t := continuation (entrance {weak := ⟨false,true⟩, full := ⟨false,true⟩})
    t.ancestor.componentDone = true ∧ t.body.values = ⟨some false,some true⟩ ∧
    t.body.selected = some true ∧ t.body.stocks = ⟨0,10,0⟩ ∧
    t.body.account.fuel = 428018 ∧ t.body.account.spent = 284994 ∧
    t.body.account.live = 34 ∧ t.body.retained = true := by decide

theorem opposed_dependency_changes_the_enacted_relation :
    let requiring := continuation (entrance {weak := ⟨false,true⟩, full := ⟨false,true⟩})
    let obstructed := continuation (entrance {weak := ⟨true,false⟩, full := ⟨true,false⟩})
    requiring.ancestor = obstructed.ancestor ∧
    requiring.body.selected = some true ∧ obstructed.body.selected = some false ∧
    requiring.body.stocks.load = 10 ∧ obstructed.body.stocks.load = 10 := by decide

theorem matched_clamp_preserves_acquisition_but_withholds_use :
    let cfg : Config := {weak := ⟨false,true⟩, full := ⟨false,true⟩}
    let learned := continuation (entrance cfg)
    let clamped := continuation (entrance {cfg with clamp := true})
    learned.body.values = clamped.body.values ∧
    learned.ancestor = clamped.ancestor ∧
    learned.body.stocks.load = 10 ∧ clamped.body.stocks = ⟨10,0,0⟩ ∧
    clamped.body.mode = .componentCompleteStop := by decide

theorem matched_assay_cost_through_commit :
    let cfg : Config := {weak := ⟨false,true⟩, full := ⟨false,true⟩}
    let learned := run (entrance cfg) assayEvents
    let clamped := run (entrance {cfg with clamp := true}) assayEvents
    learned.body.account = clamped.body.account ∧
    learned.body.values = clamped.body.values ∧ learned.body.tags = clamped.body.tags ∧
    learned.body.candidate = clamped.body.candidate ∧ learned.body.readMode = clamped.body.readMode := by
  decide

theorem missing_contact_is_unresolved :
    let cfg : Config := {weak := ⟨false,true⟩, full := ⟨false,true⟩,
                         channels := ⟨.faithful,.missing⟩}
    let t := continuation (entrance cfg)
    t.body.values = ⟨some false,none⟩ ∧ t.body.mode = .unresolved ∧
    t.body.stocks = ⟨10,0,0⟩ := by decide

theorem false_positive_can_misdirect_remaining_packet :
    let cfg : Config := {weak := ⟨false,true⟩, full := ⟨false,true⟩,
                         channels := ⟨.flip,.faithful⟩}
    let t := continuation (entrance cfg)
    t.body.values = ⟨some true,some true⟩ ∧ t.body.selected = some false ∧
    t.body.stocks = ⟨0,0,10⟩ ∧ t.ancestor.componentDone = true := by decide

theorem broken_calibration_defeats_correct_weak_record :
    let cfg : Config := {weak := ⟨false,true⟩, full := ⟨false,false⟩}
    let t := continuation (entrance cfg)
    t.body.values = ⟨some false,some true⟩ ∧ t.body.selected = some true ∧
    t.body.stocks = ⟨0,0,10⟩ := by decide

theorem unavailable_relation_is_not_old_unfulfillment :
    let t := continuation (entrance {weak := ⟨false,false⟩, full := ⟨false,false⟩})
    t.ancestor.componentDone = true ∧ t.body.mode = .noSupportedRoute ∧
    t.body.stocks = ⟨10,0,0⟩ := by decide

#print axioms charge_conserves
#print axioms charge_never_increases_fuel
#print axioms charge_denial_preserves_account
#print axioms chosen_setting_supported
#print axioms productive_pair_has_selected_setting
#print axioms absent_evidence_is_not_negative
#print axioms no_constant_setting_serves_opposed_relations
#print axioms calibrated_selected_setting_transfers
#print axioms faithful_bound_datum_decodes
#print axioms wrong_context_stays_unknown
#print axioms missing_stays_unknown
#print axioms discharge_conserves
#print axioms supported_discharge_delivers
#print axioms unsupported_discharge_wastes
#print axioms transfer_actor_account_conserved
#print axioms transfer_stocks_conserved
#print axioms empty_source_cannot_debit_actor
#print axioms affordable_calibrated_selection_delivers
#print axioms ancestral_coordinates_unchanged
#print axioms run_ancestral_coordinates_unchanged
#print axioms completed_component_stays_complete
#print axioms run_is_core_trace
#print axioms consumer_read_ignores_latent_law
#print axioms weak_challenge_does_not_supply_load
#print axioms slot_write_does_not_supply_load
#print axioms paid_account_conserved
#print axioms paid_stocks_preserved
#print axioms advance_actor_account_conserved
#print axioms advance_stock_account_conserved
#print axioms run_actor_account_conserved
#print axioms run_stock_account_conserved
#print axioms whole_history_conserved
#print axioms finite_original_support_bounds_fuel
#print axioms truthful_paid_assay_acquires_pair
#print axioms truthful_paid_assay_commits_supported_choice
#print axioms actual_dependent_service
#print axioms opposed_dependency_changes_the_enacted_relation
#print axioms matched_clamp_preserves_acquisition_but_withholds_use
#print axioms matched_assay_cost_through_commit
#print axioms missing_contact_is_unresolved
#print axioms false_positive_can_misdirect_remaining_packet
#print axioms broken_calibration_defeats_correct_weak_record
#print axioms unavailable_relation_is_not_old_unfulfillment
end RemainingDependency
