import UpdaterConsequences

noncomputable section
open scoped BigOperators

namespace CalibratedUpdater
open ConnectionistRecovery DevelopmentalMemory UpdaterConsequences

structure Channel where
  gain : ℝ
  bias : ℝ

def raw (c : Channel) (x : ℝ) : ℝ := c.gain*x+c.bias

def localReport (zero one : Option ℝ) (observed sign : ℝ) : Option Bool := by
  classical
  exact match zero, one with
    | some z, some o => if o = z then none else some (decide (0 < sign*(o-z)*(observed-z)))
    | _, _ => none

theorem reference_signal (c : Channel) (p s : ℝ) :
    s*(raw c 1-raw c 0)*(raw c p-raw c 0) = c.gain^2*(s*p) := by
  dsimp [raw]; ring

theorem acquired_local_exact (c : Channel) (p s : ℝ) (hg : c.gain ≠ 0) :
    localReport (some (raw c 0)) (some (raw c 1)) (raw c p) s =
      some (decide (0 < s*p)) := by
  classical
  have hd : raw c 1 ≠ raw c 0 := by simp [raw, hg]
  have he : (0 < s*(raw c 1-raw c 0)*(raw c p-raw c 0)) ↔ 0 < s*p := by
    rw [reference_signal]
    exact mul_pos_iff_of_pos_left (sq_pos_of_ne_zero hg)
  simp only [localReport, if_neg hd, he]

theorem constant_channel_unresolved (c : Channel) (p s : ℝ) (hg : c.gain = 0) :
    localReport (some (raw c 0)) (some (raw c 1)) (raw c p) s = none := by
  simp [localReport, raw, hg]

def join : Option Bool → Option Bool → Option Bool
  | some false, _ => some false
  | _, some false => some false
  | some true, some true => some true
  | _, _ => none

theorem join_some (a b : Bool) : join (some a) (some b) = some (a && b) := by
  cases a <;> cases b <;> rfl

theorem join_true_iff (a b : Option Bool) :
    join a b = some true ↔ a = some true ∧ b = some true := by
  cases a with
  | none => cases b with
    | none => simp [join]
    | some b => cases b <;> simp [join]
  | some a => cases a <;> cases b with
    | none => simp [join]
    | some b => cases b <;> simp [join]

@[ext]
structure Apparatus where
  zero : Fin 3 → Option ℝ
  one : Fin 3 → Option ℝ
  wired : Fin 3 → Bool
  inhibit : Bool
  parts : Nat
  fuel : Nat
  spent : Nat

def localRead (h : Apparatus) (observed signs : Profile 3) (i : Fin 3) : Option Bool :=
  if h.wired i then localReport (h.zero i) (h.one i) (observed i) (signs i) else none

def report (h : Apparatus) (observed signs : Profile 3) : Option Bool :=
  join (localRead h observed signs 0)
    (join (localRead h observed signs 1) (localRead h observed signs 2))

theorem report_requires_all (h : Apparatus) (observed signs : Profile 3) :
    report h observed signs = some true ↔ ∀ i, localRead h observed signs i = some true := by
  simp [report, join_true_iff, Fin.forall_fin_succ]

def blank (fuel parts : Nat) : Apparatus :=
  ⟨fun _ => none,fun _ => none,fun _ => false,false,parts,fuel,0⟩

def ready (channels : Fin 3 → Channel) : Apparatus :=
  ⟨fun i => some (raw (channels i) 0),fun i => some (raw (channels i) 1),
    fun _ => true,true,0,0,10⟩

def readings (channels : Fin 3 → Channel) (p : Profile 3) : Profile 3 :=
  fun i => raw (channels i) (p i)

theorem ready_local (channels : Fin 3 → Channel) (hg : ∀ i, (channels i).gain ≠ 0)
    (p s : Profile 3) (i : Fin 3) :
    localRead (ready channels) (readings channels p) s i = some (decide (0 < s i*p i)) := by
  simp only [localRead, ready, readings, ↓reduceIte]
  exact acquired_local_exact (channels i) (p i) (s i) (hg i)

theorem ready_report (channels : Fin 3 → Channel) (hg : ∀ i, (channels i).gain ≠ 0)
    (p s : Profile 3) :
    report (ready channels) (readings channels p) s = some (@decide (recalls s p) (Classical.propDecidable _)) := by
  classical
  simp only [report, ready_local channels hg, join_some]
  congr 1
  simp [recalls, Fin.forall_fin_succ]

theorem missing_contact_blocks_success (h : Apparatus) (i : Fin 3)
    (hi : h.wired i = false) (observed signs : Profile 3) :
    report h observed signs ≠ some true := by
  intro ht
  have := (report_requires_all h observed signs).mp ht i
  simp [localRead, hi] at this

def connect (i : Fin 3) (h : Apparatus) : Apparatus :=
  if h.wired i = false ∧ 0 < h.parts ∧ 0 < h.fuel then
    { h with wired := Function.update h.wired i true
             parts := h.parts-1
             fuel := h.fuel-1
             spent := h.spent+1 }
  else h

def acquire (channels : Fin 3 → Channel) (i : Fin 3) (one : Bool)
    (h : Apparatus) : Apparatus :=
  if h.wired i = true ∧ 0 < h.fuel then
    if one then
      { h with one := Function.update h.one i (some (raw (channels i) 1))
               fuel := h.fuel-1
               spent := h.spent+1 }
    else
      { h with zero := Function.update h.zero i (some (raw (channels i) 0))
               fuel := h.fuel-1
               spent := h.spent+1 }
  else h

def connectInhibitor (h : Apparatus) : Apparatus :=
  if h.inhibit = false ∧ 0 < h.parts ∧ 0 < h.fuel then
    { h with inhibit := true
             parts := h.parts-1
             fuel := h.fuel-1
             spent := h.spent+1 }
  else h

inductive Build where
  | contact (i : Fin 3)
  | reference (i : Fin 3) (one : Bool)
  | inhibitor

def buildStep (channels : Fin 3 → Channel) (b : Build) (h : Apparatus) : Apparatus :=
  match b with
  | .contact i => connect i h
  | .reference i one => acquire channels i one h
  | .inhibitor => connectInhibitor h

def buildPlan : List Build :=
  [.contact 0,.reference 0 false,.reference 0 true,
   .contact 1,.reference 1 false,.reference 1 true,
   .contact 2,.reference 2 false,.reference 2 true,.inhibitor]

def build (channels : Fin 3 → Channel) (h : Apparatus) : Apparatus :=
  buildPlan.foldl (fun state b => buildStep channels b state) h

set_option maxHeartbeats 2000000 in
theorem acquired_assembly (channels : Fin 3 → Channel) : build channels (blank 10 4) = ready channels := by
  apply Apparatus.ext
  all_goals try funext i
  all_goals try fin_cases i
  all_goals norm_num [build, buildPlan, List.foldl, buildStep, connect, acquire,
    connectInhibitor, blank, ready, Function.update]

theorem no_fuel_no_build (channels : Fin 3 → Channel) (b : Build) (h : Apparatus)
    (hf : h.fuel = 0) : buildStep channels b h = h := by
  cases b <;> simp [buildStep, connect, acquire, connectInhibitor, hf]

theorem no_contact_no_acquisition (channels : Fin 3 → Channel) (i : Fin 3)
    (one : Bool) (h : Apparatus) (hi : h.wired i = false) : acquire channels i one h = h := by
  simp [acquire, hi]

theorem build_step_support (channels : Fin 3 → Channel) (b : Build) (h : Apparatus) :
    (buildStep channels b h).fuel + (buildStep channels b h).spent = h.fuel+h.spent := by
  cases b with
  | contact i => dsimp only [buildStep]; unfold connect; split_ifs <;> (dsimp; omega)
  | reference i one =>
    dsimp only [buildStep]; unfold acquire
    split_ifs <;> dsimp <;> omega
  | inhibitor => dsimp only [buildStep]; unfold connectInhibitor; split_ifs <;> (dsimp; omega)

theorem finite_build_support (channels : Fin 3 → Channel) (events : List Build) (h : Apparatus) :
    let out := events.foldl (fun state b => buildStep channels b state) h
    out.fuel+out.spent = h.fuel+h.spent := by
  induction events generalizing h with
  | nil => rfl
  | cons b rest ih =>
    simp only [List.foldl_cons]
    rw [ih]
    exact build_step_support channels b h

theorem three_unit_build_incomplete (channels : Fin 3 → Channel) :
    (build channels (blank 3 4)).inhibit = false ∧
    (build channels (blank 3 4)).fuel = 0 ∧
    (build channels (blank 3 4)).spent = 3 := by
  norm_num [build, buildPlan, List.foldl, buildStep, connect, acquire,
    connectInhibitor, blank, Function.update]

def nativeUpdate (h : Apparatus) (channels : Fin 3 → Channel)
    (B : Network 3) (task : Task) : Network 3 := by
  classical
  let p := step Real.tanh 1 1 B (profile task)
  exact if h.inhibit = true ∧ report h (readings channels p) (profile task) = some true
    then B else learn 1 (profile task) B

theorem no_inhibitor_continual (h : Apparatus) (channels : Fin 3 → Channel)
    (hi : h.inhibit = false) (B : Network 3) (task : Task) :
    nativeUpdate h channels B task = update .continual B task := by
  simp [nativeUpdate, hi, update]

theorem formed_update_responsive (channels : Fin 3 → Channel)
    (hg : ∀ i, (channels i).gain ≠ 0) (B : Network 3) (task : Task) :
    nativeUpdate (ready channels) channels B task = update .responsive B task := by
  classical
  change (if report (ready channels) (readings channels (step Real.tanh 1 1 B (profile task)))
    (profile task) = some true then B else learn 1 (profile task) B) = _
  rw [ready_report channels hg]
  simp only [Option.some.injEq, decide_eq_true_eq]
  rfl

def nativeRun (h : Apparatus) (channels : Fin 3 → Channel) (B : Network 3) :
    List Task → Network 3 × Nat
  | [] => (B,0)
  | task :: rest => by
    classical
    let next := nativeRun h channels (nativeUpdate h channels B task) rest
    exact (next.1,(if succeeds B task then 1 else 0)+next.2)

theorem native_run_bound (h : Apparatus) (channels : Fin 3 → Channel)
    (B : Network 3) (tasks : List Task) : (nativeRun h channels B tasks).2 ≤ tasks.length := by
  classical
  induction tasks generalizing B with
  | nil => simp [nativeRun]
  | cons task rest ih =>
    have hb := ih (nativeUpdate h channels B task)
    simp only [nativeRun, List.length_cons]
    split_ifs <;> omega

theorem formed_run_responsive (channels : Fin 3 → Channel)
    (hg : ∀ i, (channels i).gain ≠ 0) (B : Network 3) (tasks : List Task) :
    nativeRun (ready channels) channels B tasks = run .responsive B tasks := by
  induction tasks generalizing B with
  | nil => rfl
  | cons task rest ih => simp [nativeRun, run, formed_update_responsive channels hg, ih]

theorem unformed_run_continual (channels : Fin 3 → Channel)
    (B : Network 3) (tasks : List Task) (fuel parts : Nat) :
    nativeRun (blank fuel parts) channels B tasks = run .continual B tasks := by
  induction tasks generalizing B with
  | nil => rfl
  | cons task rest ih =>
    rw [nativeRun, run, no_inhibitor_continual _ _ (by rfl), ih]

def usable (h : Apparatus) : Prop :=
  h.inhibit = true ∧ ∀ i, h.wired i = true ∧
    ∃ z o, h.zero i = some z ∧ h.one i = some o ∧ o ≠ z

theorem ready_usable (channels : Fin 3 → Channel) (hg : ∀ i, (channels i).gain ≠ 0) :
    usable (ready channels) := by
  constructor
  · rfl
  · intro i
    refine ⟨rfl,raw (channels i) 0,raw (channels i) 1,rfl,rfl,?_⟩
    simp [raw, hg i]

structure NativeState where
  network : Network 3
  active : Bool
  stock : Nat
  source : Nat
  spent : Nat
  waste : Nat

def project (route : Route) (x : NativeState) : Carrier :=
  ⟨x.network, if x.active then some route else none,x.stock,x.source,x.spent,x.waste⟩

def activate (h : Apparatus) (x : NativeState) : NativeState := by
  classical
  exact if usable h ∧ x.active = false ∧ 2 ≤ x.stock then
    { x with active := true
             stock := x.stock-2
             spent := x.spent+2 }
  else x

def nativeCycle (h : Apparatus) (channels : Fin 3 → Channel) (x : NativeState) : NativeState := by
  classical
  exact if x.active = true ∧ 4 ≤ x.source then
    let result := nativeRun h channels x.network cycle
    let available := x.stock+result.2
    if 4 ≤ available then
      { x with network := result.1
               stock := available-4
               source := x.source-4
               spent := x.spent+4
               waste := x.waste+(4-result.2) }
    else
      { x with network := result.1
               active := false
               stock := available
               source := x.source-4
               waste := x.waste+(4-result.2) }
  else x

theorem native_cycle_projection (h : Apparatus) (channels : Fin 3 → Channel)
    (route : Route) (corresponds : ∀ B tasks, nativeRun h channels B tasks = run route B tasks)
    (x : NativeState) : project route (nativeCycle h channels x) = cycleStep (project route x) := by
  classical
  cases hx : x.active <;> simp only [nativeCycle, hx, project, Bool.false_eq_true,
    false_and, true_and, ↓reduceIte, cycleStep, corresponds]
  split_ifs <;> simp_all

theorem activation_projection (h : Apparatus) (hu : usable h) (x : NativeState) :
    project .responsive (activate h x) = install .responsive (project .responsive x) := by
  classical
  cases hx : x.active <;> simp [activate, hu, hx, project, install]
  split_ifs <;> simp_all

theorem projection_injective (route : Route) : Function.Injective (project route) := by
  intro x y h
  cases x with | mk xn xa xs xo xp xw =>
    cases y with | mk yn ya ys yo yp yw =>
      cases xa <;> cases ya <;> simp_all [project]

def entrance : NativeState := ⟨weighted 1 1,true,0,12,0,0⟩
def afterFailure : NativeState := ⟨weighted 2 4,false,3,8,0,1⟩
def finalState : NativeState := ⟨weighted 2 4,true,1,0,10,1⟩

theorem actual_unformed_failure (channels : Fin 3 → Channel) :
    nativeCycle (blank 10 4) channels entrance = afterFailure := by
  apply projection_injective .continual
  rw [native_cycle_projection _ _ _ (fun B tasks => unformed_run_continual channels B tasks 10 4)]
  exact loss_retires_old_route

theorem constructed_full_continuation (channels : Fin 3 → Channel)
    (hg : ∀ i, (channels i).gain ≠ 0) :
    let h := build channels (blank 10 4)
    nativeCycle h channels (nativeCycle h channels
      (activate h (nativeCycle (blank 10 4) channels entrance))) = finalState := by
  rw [acquired_assembly]
  simp only
  rw [actual_unformed_failure]
  apply projection_injective .responsive
  rw [native_cycle_projection _ _ _ (formed_run_responsive channels hg),
    native_cycle_projection _ _ _ (formed_run_responsive channels hg),
    activation_projection _ (ready_usable channels hg)]
  exact (by
    change cycleStep (cycleStep (install .responsive retired)) = renewedTwice
    rw [actual_replacement,new_route_renews,new_route_renews_again])

theorem complete_support_account (channels : Fin 3 → Channel) :
    (build channels (blank 10 4)).fuel + (build channels (blank 10 4)).spent +
      finalState.stock+finalState.source+finalState.spent+finalState.waste = 22 := by
  rw [acquired_assembly]
  norm_num [ready,finalState]

theorem exhausted_native_source (h : Apparatus) (channels : Fin 3 → Channel)
    (x : NativeState) (hs : x.source < 4) : nativeCycle h channels x = x := by
  simp [nativeCycle, show ¬ 4 ≤ x.source by omega]

def identityChannels : Fin 3 → Channel := fun _ => ⟨1,0⟩
def changedChannels : Fin 3 → Channel := fun i => ⟨second i,0⟩

theorem identity_reference_changed_use (p : Profile 3) (hp : recalls second p) :
    report (ready identityChannels) (readings changedChannels p) first = some true := by
  apply (report_requires_all _ _ _).2
  intro i
  have hi := hp i
  have hfirst : first i = 1 := by fin_cases i <;> norm_num [first]
  simp [localRead,ready,identityChannels,readings,changedChannels,raw,localReport,hfirst,hi]

theorem stale_channel_blocks_actual_repair :
    nativeUpdate (ready identityChannels) changedChannels (weighted 1 4) .a = weighted 1 4 ∧
    ¬ succeeds (weighted 1 4) .a := by
  have hp : recalls second (step Real.tanh 1 1 (weighted 1 4) first) := by
    have h := overwrite_changes_old_recall 0
    rw [predecessor_networks.2] at h
    simpa [develop] using h
  have hr := identity_reference_changed_use _ hp
  constructor
  · simp only [nativeUpdate, profile, hr, and_true]
    rfl
  · norm_num [succeeds_first_iff]

end CalibratedUpdater
