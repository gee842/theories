import ConnectionistRecovery

noncomputable section
open scoped BigOperators

namespace DevelopmentalMemory
open ConnectionistRecovery

def inner {n : Nat} (x y : Profile n) : ℝ := ∑ i, x i * y i

def store {n : Nat} (η : ℝ) (s : Profile n) (B : Network n) : Network n :=
  fun i j => B i j + η * s i * s j

def inherited {n : Nat} (η : ℝ) : List (Profile n) → Network n
  | [] => fun _ _ => 0
  | s :: history => store η s (inherited η history)

def choose {n : Nat} (η : ℝ) (s : Profile n) (B : Network n)
    (a b : Fin n) : Network n :=
  if score s (step Real.tanh 1 1 B s) <
      score s (step Real.tanh 1 1 (perturb B a b η) s) then perturb B a b η
  else perturb B a b (-η)

theorem tanh_strictMono : StrictMono Real.tanh := by
  apply strictMono_of_deriv_pos
  intro x
  rw [(tanh_derivative x).deriv]
  exact one_div_pos.mpr (sq_pos_of_pos (Real.cosh_pos x))

theorem nonlinear_score_difference {n : Nat} (B : Network n) (s : Profile n)
    (a b : Fin n) (w : ℝ) :
    score s (step Real.tanh 1 1 (perturb B a b w) s) -
      score s (step Real.tanh 1 1 B s) =
    s a * (Real.tanh (input B s a + w * s b) - Real.tanh (input B s a)) := by
  classical
  unfold score
  have hi (i : Fin n) :
      s i * step Real.tanh 1 1 (perturb B a b w) s i -
        s i * step Real.tanh 1 1 B s i =
      if i = a then s a * (Real.tanh (input B s a + w * s b) -
        Real.tanh (input B s a)) else 0 := by
    simp only [step, input_perturb]
    by_cases h : i = a
    · subst i; simp; ring
    · simp [h]
  calc
    _ = ∑ i, (s i * step Real.tanh 1 1 (perturb B a b w) s i -
      s i * step Real.tanh 1 1 B s i) := by rw [Finset.sum_sub_distrib]; ring
    _ = _ := by simp_rw [hi]; simp

theorem positive_proposal_iff {n : Nat} (B : Network n) (s : Profile n)
    (a b : Fin n) (η : ℝ) (hη : 0 < η) (unit : ∀ i, s i * s i = 1) :
    score s (step Real.tanh 1 1 B s) <
      score s (step Real.tanh 1 1 (perturb B a b η) s) ↔ 0 < s a * s b := by
  rw [← sub_pos, nonlinear_score_difference]
  rcases mul_self_eq_one_iff.mp (unit a) with ha | ha <;>
    rcases mul_self_eq_one_iff.mp (unit b) with hb | hb
  · simp only [ha, hb, mul_one, one_mul]
    have h := tanh_strictMono (show input B s a < input B s a + η by linarith)
    constructor <;> intro <;> linarith
  · simp only [ha, hb, mul_neg, mul_one, one_mul]
    have h := tanh_strictMono (show input B s a + -η < input B s a by linarith)
    constructor <;> intro <;> linarith
  · simp only [ha, hb, mul_one, neg_mul, one_mul]
    have h := tanh_strictMono (show input B s a < input B s a + η by linarith)
    constructor <;> intro <;> linarith
  · simp only [ha, hb, mul_neg, mul_one, neg_mul, one_mul]
    have h := tanh_strictMono (show input B s a + -η < input B s a by linarith)
    constructor <;> intro <;> linarith

theorem selected_coefficient {n : Nat} (B : Network n) (s : Profile n)
    (a b : Fin n) (η : ℝ) (hη : 0 < η) (unit : ∀ i, s i * s i = 1) :
    choose η s B a b = perturb B a b (η * s a * s b) := by
  unfold choose
  rw [positive_proposal_iff B s a b η hη unit]
  rcases mul_self_eq_one_iff.mp (unit a) with ha | ha <;>
    rcases mul_self_eq_one_iff.mp (unit b) with hb | hb <;> simp [ha, hb]

def accumulate {n : Nat} (η : ℝ) (s : Profile n) (B : Network n) :
    List (Fin n × Fin n) → Network n
  | [] => B
  | (a,b) :: coordinates => accumulate η s (choose η s B a b) coordinates

theorem selected_coordinate_gain {n : Nat} (B : Network n) (s : Profile n)
    (a b : Fin n) (η : ℝ) (hη : 0 < η) (unit : ∀ i, s i * s i = 1) :
    score s (step Real.tanh 1 1 B s) < score s (step Real.tanh 1 1 (choose η s B a b) s) := by
  rw [selected_coefficient B s a b η hη unit, ← sub_pos, nonlinear_score_difference]
  have he : η * s a * s b * s b = η * s a := by
    calc
      _ = η * s a * (s b * s b) := by ring
      _ = _ := by rw [unit, mul_one]
  rw [he]
  rcases mul_self_eq_one_iff.mp (unit a) with ha | ha
  · simp only [ha, mul_one, one_mul]
    exact sub_pos.mpr (tanh_strictMono (by linarith))
  · simp only [ha, mul_neg, mul_one, neg_mul, one_mul]
    have h := tanh_strictMono (show input B s a + -η < input B s a by linarith)
    linarith

theorem input_store {n : Nat} (η : ℝ) (s x : Profile n) (B : Network n)
    (i : Fin n) : input (store η s B) x i = input B x i + η * s i * inner s x := by
  simp only [input, store, inner, add_mul, Finset.sum_add_distrib, Finset.mul_sum]
  congr 1
  apply Finset.sum_congr rfl
  intro j _; ring

theorem history_field {n : Nat} (η : ℝ) (history : List (Profile n))
    (x : Profile n) (i : Fin n) :
    input (inherited η history) x i =
      (history.map (fun s => η * s i * inner s x)).sum := by
  induction history with
  | nil => simp [inherited, input]
  | cons s h ih => simp [inherited, input_store, ih, add_comm]

theorem retrieval_margin {n : Nat} (η : ℝ) (s x : Profile n) (B : Network n)
    (i : Fin n) (unit : s i * s i = 1)
    (margin : |input B x i| < η * inner s x) :
    0 < s i * input (store η s B) x i := by
  rw [input_store]
  have h := neg_abs_le (input B x i)
  have h' := le_abs_self (input B x i)
  rcases mul_self_eq_one_iff.mp unit with hs | hs <;> rw [hs] <;>
    simp only [one_mul, neg_mul, mul_one] <;> nlinarith

theorem signed_tanh_positive (s x : ℝ) (unit : s * s = 1)
    (hx : 0 < s * x) : 0 < s * Real.tanh x := by
  rcases mul_self_eq_one_iff.mp unit with hs | hs
  · subst s; simp only [one_mul] at *
    simpa using tanh_strictMono hx
  · subst s
    have hn : x < 0 := by linarith
    have h := tanh_strictMono hn
    simpa using (show 0 < -Real.tanh x by simpa using neg_pos.mpr h)

def recalls {n : Nat} (s p : Profile n) : Prop := ∀ i, 0 < s i * p i

theorem one_step_recall {n : Nat} (B : Network n) (s x : Profile n)
    (unit : ∀ i, s i * s i = 1) (field : ∀ i, 0 < s i * input B x i) :
    recalls s (step Real.tanh 1 1 B x) := by
  intro i
  simpa [step] using signed_tanh_positive (s i) (input B x i) (unit i) (field i)

theorem recall_preserved {n : Nat} (B : Network n) (s p : Profile n)
    (unit : ∀ i, s i * s i = 1) (hB : ∀ i j, 0 ≤ s i * B i j * s j)
    (diag : ∀ i, 0 < B i i) (hp : recalls s p) (t : Nat) :
    recalls s (develop Real.tanh 1 1 B p t) := by
  classical
  induction t with
  | zero => exact hp
  | succ t ih =>
    apply one_step_recall B s _ unit
    intro i
    have he (j : Fin n) : s i * B i j * develop Real.tanh 1 1 B p t j =
        (s i * B i j * s j) * (s j * develop Real.tanh 1 1 B p t j) := by
      calc
        _ = (s i * B i j * develop Real.tanh 1 1 B p t j) * 1 := by ring
        _ = (s i * B i j * develop Real.tanh 1 1 B p t j) * (s j * s j) := by rw [unit]
        _ = _ := by ring
    have ht (j : Fin n) : 0 ≤ s i * B i j * develop Real.tanh 1 1 B p t j := by
      rw [he]; exact mul_nonneg (hB i j) (le_of_lt (ih j))
    have hd : 0 < s i * B i i * develop Real.tanh 1 1 B p t i := by
      have := mul_pos (diag i) (ih i)
      nlinarith only [this]
    have hh := Finset.sum_pos' (s := Finset.univ) (fun j _ => ht j) ⟨i, Finset.mem_univ i, hd⟩
    simpa only [input, Finset.mul_sum, mul_assoc] using hh

theorem develop_after_first {n : Nat} (B : Network n) (x : Profile n) (t : Nat) :
    develop Real.tanh 1 1 B x (t + 1) =
      develop Real.tanh 1 1 B (step Real.tanh 1 1 B x) t := by
  induction t with
  | zero => rfl
  | succ t ih => simp only [develop, ih]

theorem enduring_recall {n : Nat} (B : Network n) (s x : Profile n)
    (unit : ∀ i, s i * s i = 1) (hB : ∀ i j, 0 ≤ s i * B i j * s j)
    (diag : ∀ i, 0 < B i i) (field : ∀ i, 0 < s i * input B x i)
    (t : Nat) : recalls s (develop Real.tanh 1 1 B x (t + 1)) := by
  rw [develop_after_first]
  exact recall_preserved B s _ unit hB diag (one_step_recall B s x unit field) t

def first : Profile 3 := ![1,1,1]
def second : Profile 3 := ![1,1,-1]
def partialFirst : Profile 3 := ![1,0,1]
def partialSecond : Profile 3 := ![1,0,-1]
def both : Network 3 := inherited 1 [second, first]
def overwritten : Network 3 := inherited 1 [second, second, second, second, first]
def restored : Network 3 := inherited 1 [first, first, first, first,
    second, second, second, second, first]

theorem both_recall (t : Nat) :
    recalls first (develop Real.tanh 1 1 both partialFirst (t+1)) ∧
    recalls second (develop Real.tanh 1 1 both partialSecond (t+1)) := by
  constructor
  all_goals apply enduring_recall
  all_goals intro i
  all_goals try intro j
  all_goals fin_cases i
  all_goals try fin_cases j
  all_goals norm_num [both, inherited, store, first, second, partialFirst, partialSecond,
    input, Fin.sum_univ_succ]

theorem overwrite_changes_old_recall (t : Nat) :
    recalls second (develop Real.tanh 1 1 overwritten first (t+1)) := by
  apply enduring_recall
  all_goals intro i
  all_goals try intro j
  all_goals fin_cases i
  all_goals try fin_cases j
  all_goals norm_num [overwritten, inherited, store, first, second, input, Fin.sum_univ_succ]

theorem old_recall_fails (t : Nat) :
    ¬ recalls first (develop Real.tanh 1 1 overwritten first (t+1)) := by
  intro h
  have hn := overwrite_changes_old_recall t (2 : Fin 3)
  have hp := h (2 : Fin 3)
  norm_num [first, second] at hn hp
  linarith

theorem old_recall_restored (t : Nat) :
    recalls first (develop Real.tanh 1 1 restored partialFirst (t+1)) := by
  apply enduring_recall
  all_goals intro i
  all_goals try intro j
  all_goals fin_cases i
  all_goals try fin_cases j
  all_goals norm_num [restored, inherited, store, first, second, partialFirst,
    input, Fin.sum_univ_succ]

end DevelopmentalMemory
