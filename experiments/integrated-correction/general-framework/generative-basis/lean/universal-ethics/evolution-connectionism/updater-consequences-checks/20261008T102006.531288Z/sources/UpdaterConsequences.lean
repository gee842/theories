import DevelopmentalMemory

noncomputable section
open scoped BigOperators

namespace UpdaterConsequences
open ConnectionistRecovery DevelopmentalMemory

inductive Task where
  | a
  | c
  deriving DecidableEq

inductive Route where
  | continual
  | responsive
  deriving DecidableEq

def profile : Task → Profile 3
  | .a => first
  | .c => second

def weighted (a b : ℝ) : Network 3 :=
  fun i j => a * first i * first j + b * second i * second j

def succeeds (B : Network 3) (task : Task) : Prop :=
  recalls (profile task) (step Real.tanh 1 1 B (profile task))

theorem tanh_positive_iff (x : ℝ) : 0 < Real.tanh x ↔ 0 < x := by
  simpa only [Real.tanh_zero] using tanh_strictMono.lt_iff_lt (a := 0) (b := x)

theorem tanh_negative_iff (x : ℝ) : Real.tanh x < 0 ↔ x < 0 := by
  simpa only [Real.tanh_zero] using tanh_strictMono.lt_iff_lt (a := x) (b := 0)

theorem first_field (a b : ℝ) (i : Fin 3) :
    input (weighted a b) first i = if i.val = 2 then 3*a-b else 3*a+b := by
  fin_cases i <;> norm_num [input, weighted, first, second, Fin.sum_univ_succ] <;> ring

theorem second_field (a b : ℝ) (i : Fin 3) :
    input (weighted a b) second i = if i.val = 2 then a-3*b else a+3*b := by
  fin_cases i <;> norm_num [input, weighted, first, second, Fin.sum_univ_succ] <;> ring

theorem succeeds_first_iff (a b : ℝ) :
    succeeds (weighted a b) .a ↔ 0 < 3*a+b ∧ 0 < 3*a-b := by
  simp only [succeeds, recalls, profile, step, sub_self, zero_mul, zero_add,
    one_mul, first_field]
  simp [first, Fin.forall_fin_succ, tanh_positive_iff]

theorem succeeds_second_iff (a b : ℝ) :
    succeeds (weighted a b) .c ↔ 0 < a+3*b ∧ 0 < 3*b-a := by
  simp only [succeeds, recalls, profile, step, sub_self, zero_mul, zero_add,
    one_mul, second_field]
  simp only [second, Fin.forall_fin_succ]
  simp [tanh_positive_iff, tanh_negative_iff, sub_pos]

theorem profile_binary (task : Task) (i : Fin 3) : profile task i * profile task i = 1 := by
  cases task <;> fin_cases i <;> norm_num [profile, first, second]

theorem learned_first (a b : ℝ) : learn 1 first (weighted a b) = weighted (a+1) b := by
  rw [learned_equals_store 1 first _ (by norm_num) (profile_binary .a)]
  funext i j
  dsimp [store, weighted]
  ring

theorem learned_second (a b : ℝ) : learn 1 second (weighted a b) = weighted a (b+1) := by
  rw [learned_equals_store 1 second _ (by norm_num) (profile_binary .c)]
  funext i j
  dsimp [store, weighted]
  ring

theorem predecessor_networks : both = weighted 1 1 ∧ overwritten = weighted 1 4 := by
  constructor <;> funext i j
  all_goals simp only [both, overwritten, inherited, store, weighted]
  all_goals ring

def update (route : Route) (B : Network 3) (task : Task) : Network 3 := by
  classical
  exact match route with
    | .continual => learn 1 (profile task) B
    | .responsive => if succeeds B task then B else learn 1 (profile task) B

def run (route : Route) (B : Network 3) : List Task → Network 3 × Nat
  | [] => (B,0)
  | task :: rest => by
    classical
    let next := run route (update route B task) rest
    exact (next.1, (if succeeds B task then 1 else 0) + next.2)

def cycle : List Task := [.c,.c,.c,.a]

theorem run_return_bound (route : Route) (B : Network 3) (tasks : List Task) :
    (run route B tasks).2 ≤ tasks.length := by
  classical
  induction tasks generalizing B with
  | nil => simp [run]
  | cons task rest ih =>
    have h := ih (update route B task)
    simp only [run, List.length_cons]
    split_ifs <;> omega

theorem run_append (route : Route) (B : Network 3) (xs ys : List Task) :
    run route B (xs ++ ys) =
      let one := run route B xs
      let two := run route one.1 ys
      (two.1, one.2 + two.2) := by
  classical
  induction xs generalizing B with
  | nil => simp [run]
  | cons task rest ih => simp [run, ih, Nat.add_assoc]

theorem responsive_stable (B : Network 3)
    (ha : succeeds B .a) (hc : succeeds B .c) (tasks : List Task) :
    run .responsive B tasks = (B,tasks.length) := by
  classical
  induction tasks with
  | nil => rfl
  | cons task rest ih =>
    have ht : succeeds B task := by cases task <;> assumption
    simp [run, update, ht, ih, Nat.add_comm]

theorem continual_cycle (n : Nat) :
    run .continual (weighted (n+1) (3*n+1)) cycle =
      (weighted (n+2) (3*n+4),3) := by
  classical
  have hn : (0:ℝ) ≤ n := Nat.cast_nonneg n
  have hc0 : succeeds (weighted (n+1) (3*n+1)) .c := by
    rw [succeeds_second_iff]; constructor <;> linarith
  have hc1 : succeeds (weighted (n+1) ((3*n+1)+1)) .c := by
    rw [succeeds_second_iff]; constructor <;> linarith
  have hc2 : succeeds (weighted (n+1) (((3*n+1)+1)+1)) .c := by
    rw [succeeds_second_iff]; constructor <;> linarith
  have ha : ¬ succeeds (weighted (n+1) ((((3*n+1)+1)+1)+1)) .a := by
    rw [succeeds_first_iff]; intro h; linarith [h.2]
  simp only [cycle, run, update, profile, learned_second, learned_first]
  rw [if_pos hc0, if_pos hc1, if_pos hc2, if_neg ha]
  congr 2 <;> ring

def cycles : Nat → List Task
  | 0 => []
  | n+1 => cycles n ++ cycle

theorem repeated_continual_cycles (n : Nat) :
    run .continual (weighted 1 1) (cycles n) =
      (weighted (n+1) (3*n+1),3*n) := by
  induction n with
  | zero => norm_num [cycles, run]
  | succ n ih =>
    rw [cycles, run_append, ih]
    simp only
    rw [continual_cycle]
    simp only [Nat.cast_add, Nat.cast_one]
    congr 2 <;> ring

theorem post_failure_both : succeeds (weighted 2 4) .a ∧ succeeds (weighted 2 4) .c := by
  norm_num [succeeds_first_iff, succeeds_second_iff]

theorem repaired_by_responsive : update .responsive (weighted 1 4) .a = weighted 2 4 := by
  have h : ¬ succeeds (weighted 1 4) .a := by norm_num [succeeds_first_iff]
  norm_num [update, h, profile, learned_first]

theorem responsive_after_failure (tasks : List Task) :
    run .responsive (weighted 2 4) tasks = (weighted 2 4,tasks.length) :=
  responsive_stable _ post_failure_both.1 post_failure_both.2 tasks

theorem routes_differ_after_failure :
    update .continual (weighted 2 4) .c ≠ update .responsive (weighted 2 4) .c := by
  intro h
  have h0 := congrFun (congrFun h 0) 0
  simp only [update, if_pos post_failure_both.2, profile, learned_second] at h0
  norm_num [weighted, first, second] at h0

theorem changed_route_cycle :
    run .responsive (weighted 2 4) cycle = (weighted 2 4,4) ∧
    run .continual (weighted 2 4) cycle = (weighted 3 7,3) := by
  constructor
  · simpa [cycle] using responsive_after_failure cycle
  · convert continual_cycle 1 using 1 <;> norm_num

theorem unchanged_context_no_return_gain :
    (run .continual (weighted 1 1) [.c,.c,.c,.c]).2 = 4 ∧
    (run .responsive (weighted 1 1) [.c,.c,.c,.c]).2 = 4 := by
  classical
  have hc (b : ℝ) (hb : 1 ≤ b) : succeeds (weighted 1 b) .c := by
    rw [succeeds_second_iff]; constructor <;> linarith
  have ha : succeeds (weighted 1 1) .a := by norm_num [succeeds_first_iff]
  constructor
  · simp only [run, update, profile, learned_second]
    norm_num [succeeds_second_iff]
  · rw [responsive_stable _ ha (hc 1 (by norm_num))]; rfl

theorem extra_cost_threshold (continualCost responsiveCost : ℝ) :
    (4-responsiveCost > 3-continualCost) ↔ responsiveCost-continualCost < 1 := by
  constructor <;> intro h <;> linarith

structure Carrier where
  network : Network 3
  route : Option Route
  stock : Nat
  source : Nat
  spent : Nat
  waste : Nat

def total (x : Carrier) : Nat := x.stock + x.source + x.spent + x.waste

def cycleStep (x : Carrier) : Carrier := by
  classical
  exact match x.route with
    | none => x
    | some route =>
      if 4 ≤ x.source then
        let result := run route x.network cycle
        let available := x.stock + result.2
        if 4 ≤ available then
          { x with network := result.1
                   stock := available-4
                   source := x.source-4
                   spent := x.spent+4
                   waste := x.waste+(4-result.2) }
        else
          { x with network := result.1
                   route := none
                   stock := available
                   source := x.source-4
                   waste := x.waste+(4-result.2) }
      else x

def install (proposal : Route) (x : Carrier) : Carrier :=
  if x.route = none ∧ 2 ≤ x.stock then
    { x with route := some proposal, stock := x.stock-2, spent := x.spent+2 }
  else x

theorem cycle_conserves (x : Carrier) : total (cycleStep x) = total x := by
  classical
  unfold cycleStep
  cases hr : x.route with
  | none => rfl
  | some route =>
    have bound : (run route x.network cycle).2 ≤ 4 := by
      simpa [cycle] using run_return_bound route x.network cycle
    by_cases hs : 4 ≤ x.source
    · simp only [if_pos hs]
      dsimp only
      split_ifs <;> simp only [total] <;> omega
    · simp only [if_neg hs]

theorem installation_conserves (proposal : Route) (x : Carrier) :
    total (install proposal x) = total x := by
  unfold install
  split_ifs with h
  · simp only [total]; omega
  · rfl

theorem installation_preserves_network (proposal : Route) (x : Carrier) :
    (install proposal x).network = x.network := by
  unfold install
  split_ifs <;> rfl

theorem insufficient_stock_blocks (proposal : Route) (x : Carrier) (h : x.stock < 2) :
    install proposal x = x := by
  simp [install, show ¬ 2 ≤ x.stock by omega]

theorem exhausted_source_blocks (x : Carrier) (h : x.source < 4) : cycleStep x = x := by
  unfold cycleStep
  cases x.route <;> simp [show ¬ 4 ≤ x.source by omega]

inductive Event where
  | expose
  | construct (proposal : Route)

def event (e : Event) (x : Carrier) : Carrier :=
  match e with
  | .expose => cycleStep x
  | .construct proposal => install proposal x

theorem finite_history_conserves (events : List Event) (x : Carrier) :
    total (events.foldl (fun state e => event e state) x) = total x := by
  induction events generalizing x with
  | nil => rfl
  | cons e rest ih =>
    rw [List.foldl_cons, ih]
    cases e
    · exact cycle_conserves x
    · exact installation_conserves _ x

def initial : Carrier := ⟨weighted 1 1, some .continual,0,12,0,0⟩
def retired : Carrier := ⟨weighted 2 4,none,3,8,0,1⟩
def replacement : Carrier := ⟨weighted 2 4,some .responsive,1,8,2,1⟩
def renewedOnce : Carrier := ⟨weighted 2 4,some .responsive,1,4,6,1⟩
def renewedTwice : Carrier := ⟨weighted 2 4,some .responsive,1,0,10,1⟩

theorem loss_retires_old_route : cycleStep initial = retired := by
  have h := continual_cycle 0
  norm_num at h
  simp [cycleStep, initial, h, retired]

theorem actual_replacement : install .responsive retired = replacement := by
  simp [install, retired, replacement]

theorem new_route_renews : cycleStep replacement = renewedOnce := by
  simp [cycleStep, replacement, changed_route_cycle.1, renewedOnce]

theorem new_route_renews_again : cycleStep renewedOnce = renewedTwice := by
  simp [cycleStep, renewedOnce, changed_route_cycle.1, renewedTwice]

theorem complete_replacement_history :
    cycleStep (cycleStep (install .responsive (cycleStep initial))) = renewedTwice := by
  rw [loss_retires_old_route, actual_replacement, new_route_renews, new_route_renews_again]

theorem final_account_and_exhaustion :
    total renewedTwice = 12 ∧ cycleStep renewedTwice = renewedTwice := by
  constructor
  · norm_num [total, renewedTwice]
  · apply exhausted_source_blocks; norm_num [renewedTwice]

theorem old_proposal_fails_again :
    cycleStep (cycleStep (install .continual retired)) =
      (⟨weighted 4 10,none,3,0,6,3⟩ : Carrier) := by
  have h1 := continual_cycle 1
  have h2 := continual_cycle 2
  norm_num at h1 h2
  simp [install, retired, cycleStep, h1, h2]

def reportedUpdate (reportedSuccess : Bool) (B : Network 3) (task : Task) : Network 3 :=
  if reportedSuccess then B else learn 1 (profile task) B

theorem false_success_blocks_repair :
    reportedUpdate true (weighted 1 4) .a = weighted 1 4 ∧
    ¬ succeeds (reportedUpdate true (weighted 1 4) .a) .a := by
  norm_num [reportedUpdate, succeeds_first_iff]

end UpdaterConsequences
