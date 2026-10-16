import MeasuredFeedback

/-! Closes the retained-memory premise along the *same* PI recurrence.
Readout, memory, saturation and subsequent commands are related coordinates of
one feedback history. Physical sensor accuracy and plant response remain explicit
correspondence obligations. A supplied readout domain is not learned by this proof. -/
namespace FeedbackMemory
noncomputable section
open MeasuredFeedback

def outside (v C : ℝ) : Prop := v + C < 0 ∨ 100 < v - C

def inside (v C : ℝ) : Prop := 0 ≤ v - C ∧ v + C ≤ 100

def allowance (v C A b : ℝ) : ℝ :=
  if outside v C then 0 else if inside v C then A else A + |b|

theorem raw_error (g : Gains) (i j r y z dt E M : ℝ)
    (he : |y-z| ≤ E) (hm : |i-j| ≤ M) :
    |raw g i ⟨r,y,dt⟩ - raw g j ⟨r,z,dt⟩| ≤
      |g.proportional + g.integral*dt|*E + M := by
  have eqn : raw g i ⟨r,y,dt⟩ - raw g j ⟨r,z,dt⟩ =
      -(g.proportional+g.integral*dt)*(y-z)+(i-j) := by
    simp [raw,increment]; ring
  rw [eqn]
  calc
    _ ≤ |-(g.proportional+g.integral*dt)*(y-z)|+|i-j| := abs_add_le _ _
    _ = |g.proportional+g.integral*dt|*|y-z|+|i-j| := by rw [abs_mul,abs_neg]
    _ ≤ _ := add_le_add (mul_le_mul_of_nonneg_left he (abs_nonneg _)) hm

theorem increment_error (g : Gains) (r y z dt E : ℝ) (he : |y-z| ≤ E) :
    |increment g ⟨r,y,dt⟩-increment g ⟨r,z,dt⟩| ≤ |g.integral*dt|*E := by
  have eqn : increment g ⟨r,y,dt⟩-increment g ⟨r,z,dt⟩ =
      -(g.integral*dt)*(y-z) := by simp [increment]; ring
  rw [eqn,abs_mul,abs_neg]
  exact mul_le_mul_of_nonneg_left he (abs_nonneg _)

theorem retained_interior_error (g : Gains) (i j : ℝ) (o p : Sample) (A M : ℝ)
    (ho : 0 ≤ raw g i o ∧ raw g i o ≤ 100)
    (hp : 0 ≤ raw g j p ∧ raw g j p ≤ 100)
    (ha : |increment g o-increment g p| ≤ A) (hm : |i-j| ≤ M) :
    |retain g i o-retain g j p| ≤ M+A := by
  rw [interior_updates_integral g i o ho,interior_updates_integral g j p hp]
  have eqn : (i+increment g o)-(j+increment g p) =
      (i-j)+(increment g o-increment g p) := by ring
  rw [eqn]
  exact (abs_add_le _ _).trans (add_le_add hm ha)

theorem retained_mixed_error (g : Gains) (i j : ℝ) (o p : Sample) (A M : ℝ)
    (ha : |increment g o-increment g p| ≤ A) (hm : |i-j| ≤ M) :
    |retain g i o-retain g j p| ≤ M+A+|increment g p| := by
  have hA : 0 ≤ A := (abs_nonneg _).trans ha
  have hb := abs_nonneg (increment g p)
  unfold retain
  split_ifs with hi hj hj
  · exact hm.trans (by linarith)
  · have eqn : i-(j+increment g p) = (i-j) + (-increment g p) := by ring
    rw [eqn]
    have h := (abs_add_le (i-j) (-increment g p)).trans
      (add_le_add hm (by simp : |-increment g p| ≤ |increment g p|))
    linarith
  · have eqn : i+increment g o-j = (i-j)+(increment g o-increment g p)+increment g p := by ring
    rw [eqn]
    exact (abs_add_le _ _).trans (add_le_add
      ((abs_add_le _ _).trans (add_le_add hm ha)) le_rfl)
  · have eqn : i+increment g o-(j+increment g p) = (i-j)+(increment g o-increment g p) := by ring
    rw [eqn]
    exact ((abs_add_le _ _).trans (add_le_add hm ha)).trans (by linarith)

/-- Branch margins are evaluated on the nominal history and its propagated raw
radius. Uncertain switching pays a nominal increment; it is not silently smooth. -/
theorem retained_margin_error (g : Gains) (i j : ℝ) (o p : Sample) (C A M : ℝ)
    (hr : |raw g i o-raw g j p| ≤ C)
    (ha : |increment g o-increment g p| ≤ A) (hm : |i-j| ≤ M) :
    |retain g i o-retain g j p| ≤
      M+allowance (raw g j p) C A (increment g p) := by
  have hC : 0 ≤ C := (abs_nonneg _).trans hr
  obtain ⟨lo,hi⟩ := abs_le.mp hr
  by_cases ext : outside (raw g j p) C
  · have hs : (raw g i o < 0 ∨ 100 < raw g i o) ∧
        (raw g j p < 0 ∨ 100 < raw g j p) := by
      rcases ext with h | h
      · exact ⟨Or.inl (by linarith),Or.inl (by linarith)⟩
      · exact ⟨Or.inr (by linarith),Or.inr (by linarith)⟩
    rw [saturation_retains_integral g i o hs.1,saturation_retains_integral g j p hs.2]
    simpa [allowance,ext] using hm
  · by_cases int : inside (raw g j p) C
    · have ho : 0 ≤ raw g i o ∧ raw g i o ≤ 100 := by
        obtain ⟨a,b⟩ := int; constructor <;> linarith
      have hp : 0 ≤ raw g j p ∧ raw g j p ≤ 100 := by
        obtain ⟨a,b⟩ := int; constructor <;> linarith
      simpa [allowance,ext,int] using retained_interior_error g i j o p A M ho hp ha hm
    · simpa [allowance,ext,int,add_assoc] using retained_mixed_error g i j o p A M ha hm

def memoryRadius (g : Gains) (j r z dt E : ℕ → ℝ) (initial : ℝ) : ℕ → ℝ
  | 0 => initial
  | n+1 =>
    let M := memoryRadius g j r z dt E initial n
    M + allowance (raw g (j n) ⟨r n,z n,dt n⟩)
      (|g.proportional+g.integral*dt n|*E n+M)
      (|g.integral*dt n|*E n) (increment g ⟨r n,z n,dt n⟩)

/-- No independent per-step memory bound is assumed: it follows from the initial
bound, the readout bounds, the same targets/intervals, and both actual recurrences. -/
theorem memory_horizon (g : Gains) (i j r y z dt E : ℕ → ℝ) (initial : ℝ) (N : ℕ)
    (hi : ∀ t < N, i (t+1) = retain g (i t) ⟨r t,y t,dt t⟩)
    (hj : ∀ t < N, j (t+1) = retain g (j t) ⟨r t,z t,dt t⟩)
    (h0 : |i 0-j 0| ≤ initial) (he : ∀ t < N, |y t-z t| ≤ E t) :
    ∀ n ≤ N, |i n-j n| ≤ memoryRadius g j r z dt E initial n := by
  intro n hn
  induction n with
  | zero => exact h0
  | succ n ih =>
    have hlt : n < N := by omega
    have hm := ih (by omega)
    rw [hi n hlt,hj n hlt]
    exact retained_margin_error g (i n) (j n) _ _ _ _ _
      (raw_error g _ _ _ _ _ _ _ _ (he n hlt) hm)
      (increment_error g _ _ _ _ _ (he n hlt)) hm

def commandRadius (g : Gains) (j r z dt E : ℕ → ℝ) (initial : ℝ) (n : ℕ) : ℝ :=
  min 100 (|g.proportional+g.integral*dt n|*E n + memoryRadius g j r z dt E initial n)

theorem command_difference_at_most_100 (g : Gains) (i j : ℝ) (o p : Sample) :
    |command g i o-command g j p| ≤ 100 := by
  obtain ⟨a,b⟩ := command_bounds g i o
  obtain ⟨c,d⟩ := command_bounds g j p
  apply abs_le.mpr; constructor <;> linarith

theorem command_horizon (g : Gains) (i j r y z dt E : ℕ → ℝ) (initial : ℝ) (N : ℕ)
    (hi : ∀ t < N, i (t+1) = retain g (i t) ⟨r t,y t,dt t⟩)
    (hj : ∀ t < N, j (t+1) = retain g (j t) ⟨r t,z t,dt t⟩)
    (h0 : |i 0-j 0| ≤ initial) (he : ∀ t < N, |y t-z t| ≤ E t) :
    ∀ n < N, |command g (i n) ⟨r n,y n,dt n⟩-command g (j n) ⟨r n,z n,dt n⟩| ≤
      commandRadius g j r z dt E initial n := by
  intro n hn
  apply le_min (command_difference_at_most_100 _ _ _ _ _)
  exact command_error_bound _ _ _ _ _ _ _ _ _ (he n hn)
    (memory_horizon g i j r y z dt E initial N hi hj h0 he n (by omega))

/-- Supplies the generated whole-history command radii to the already checked
plant recurrence. Plant defect/sensitivity and actual trajectories remain inputs. -/
theorem controller_plant_horizon {X Y : Type} [PseudoMetricSpace Y]
    (p : ℕ → X → Y) (F : ℕ → X → ℝ → X) (G : ℕ → Y → ℝ → Y)
    (x : ℕ → X) (w : ℕ → Y) (g : Gains) (i j r y z dt E : ℕ → ℝ)
    (L ε B : ℕ → ℝ) (initialMemory initialState : ℝ) (N : ℕ)
    (hi : ∀ t < N, i (t+1) = retain g (i t) ⟨r t,y t,dt t⟩)
    (hj : ∀ t < N, j (t+1) = retain g (j t) ⟨r t,z t,dt t⟩)
    (hm : |i 0-j 0| ≤ initialMemory) (he : ∀ t < N, |y t-z t| ≤ E t)
    (hx : ∀ t < N, x (t+1) = F t (x t) (command g (i t) ⟨r t,y t,dt t⟩))
    (hw : ∀ t < N, w (t+1) = G t (w t) (command g (j t) ⟨r t,z t,dt t⟩))
    (h0 : dist (p 0 (x 0)) (w 0) ≤ initialState)
    (hL : ∀ t < N, 0 ≤ L t) (hB : ∀ t < N, 0 ≤ B t)
    (hd : ∀ t < N, dist (p (t+1) (F t (x t) (command g (i t) ⟨r t,y t,dt t⟩)))
      (G t (p t (x t)) (command g (i t) ⟨r t,y t,dt t⟩)) ≤ ε t)
    (hp : ∀ t < N, dist (G t (p t (x t)) (command g (i t) ⟨r t,y t,dt t⟩))
      (G t (w t) (command g (i t) ⟨r t,y t,dt t⟩)) ≤ L t * dist (p t (x t)) (w t))
    (response : ∀ t < N, ∀ a b, dist (G t (w t) a) (G t (w t) b) ≤ B t * |a-b|) :
    ∀ n ≤ N, dist (p n (x n)) (w n) ≤
      RelationsAcrossScales.budget L
        (fun t => ε t+B t*commandRadius g j r z dt E initialMemory t) initialState n := by
  apply measured_feedback_horizon p F G
    (fun t _ => command g (i t) ⟨r t,y t,dt t⟩)
    (fun t _ => command g (j t) ⟨r t,z t,dt t⟩)
    x w L ε B (commandRadius g j r z dt E initialMemory) initialState N
    hx hw h0 hL hB hd hp
  · exact command_horizon g i j r y z dt E initialMemory N hi hj hm he
  · exact response

/-- Arbitrarily close readings can give equal current commands and a fixed
retained-memory jump. The next shared sample exposes the previously hidden gap. -/
theorem saturation_boundary_hidden_memory (δ : ℝ) (hδ : 0 < δ) :
    let g : Gains := ⟨1,1⟩
    let o : Sample := ⟨100,50,1⟩
    let p : Sample := ⟨100,50-δ,1⟩
    let next : Sample := ⟨0,0,1⟩
    |o.reading-p.reading| = δ ∧ command g 0 o = command g 0 p ∧
      |retain g 0 o-retain g 0 p| = 50 ∧
      |command g (retain g 0 o) next-command g (retain g 0 p) next| = 50 := by
  dsimp
  have hb : raw ⟨1,1⟩ 0 ⟨100,50-δ,1⟩ > 100 := by simp [raw,increment]; linarith
  have hn : retain ⟨1,1⟩ 0 ⟨100,50,1⟩ = 50 := by norm_num [retain,raw,increment]
  have hp : retain ⟨1,1⟩ 0 ⟨100,50-δ,1⟩ = 0 := saturation_retains_integral _ _ _ (Or.inr hb)
  rw [hn,hp]
  constructor
  · have eqn : (50:ℝ)-(50-δ) = δ := by ring
    rw [eqn,abs_of_pos hδ]
  constructor
  · change clip (raw ⟨1,1⟩ 0 ⟨100,50,1⟩) = clip (raw ⟨1,1⟩ 0 ⟨100,50-δ,1⟩)
    rw [clip,min_eq_left hb.le]
    norm_num [raw,increment,clip]
  · norm_num [command,raw,increment,clip]

def movement (u : ℕ → ℝ) : ℕ → ℝ
  | 0 => 0
  | n+1 => movement u n + |u (n+1)-u n|

def movementRadius (C : ℕ → ℝ) : ℕ → ℝ
  | 0 => 0
  | n+1 => movementRadius C n+C (n+1)+C n

theorem movement_error (u v C : ℕ → ℝ) (N : ℕ)
    (h : ∀ n ≤ N, |u n-v n| ≤ C n) :
    |movement u N-movement v N| ≤ movementRadius C N := by
  induction N with
  | zero => simp [movement,movementRadius]
  | succ n ih =>
    have prev := ih (fun k hk => h k (by omega))
    have step : ||u (n+1)-u n|-|v (n+1)-v n|| ≤ C (n+1)+C n := by
      calc
        _ ≤ |(u (n+1)-u n)-(v (n+1)-v n)| := abs_abs_sub_abs_le_abs_sub _ _
        _ = |(u (n+1)-v (n+1))-(u n-v n)| := by congr 1; ring
        _ ≤ |u (n+1)-v (n+1)|+|u n-v n| := abs_sub_le _ _
        _ ≤ _ := add_le_add (h _ (by omega)) (h _ (by omega))
    simp only [movement,movementRadius]
    have eqn : (movement u n+|u (n+1)-u n|)-(movement v n+|v (n+1)-v n|) =
        (movement u n-movement v n)+(|u (n+1)-u n|-|v (n+1)-v n|) := by ring
    rw [eqn]
    simpa [add_assoc] using (abs_add_le _ _).trans (add_le_add prev step)

def exposure (u dt : ℕ → ℝ) : ℕ → ℝ
  | 0 => 0
  | n+1 => exposure u dt n+dt n*u n

theorem exposure_error (u v dt C : ℕ → ℝ) (N : ℕ)
    (ht : ∀ n < N, 0 ≤ dt n) (hc : ∀ n < N, |u n-v n| ≤ C n) :
    |exposure u dt N-exposure v dt N| ≤ exposure C dt N := by
  induction N with
  | zero => simp [exposure]
  | succ n ih =>
    have prev := ih (fun k hk => ht k (by omega)) (fun k hk => hc k (by omega))
    simp only [exposure]
    have eqn : exposure u dt n+dt n*u n-(exposure v dt n+dt n*v n) =
        (exposure u dt n-exposure v dt n)+dt n*(u n-v n) := by ring
    rw [eqn]
    apply (abs_add_le _ _).trans
    apply add_le_add prev
    rw [abs_mul,abs_of_nonneg (ht n (by omega))]
    exact mul_le_mul_of_nonneg_left (hc n (by omega)) (ht n (by omega))

/-- A comparison follows when warranted uncertainty intervals separate; absence
of that margin is not itself a reversal or a moral verdict. -/
theorem separated_costs (actualA actualB estimatedA estimatedB radiusA radiusB : ℝ)
    (ha : |actualA-estimatedA| ≤ radiusA) (hb : |actualB-estimatedB| ≤ radiusB)
    (gap : estimatedA+radiusA < estimatedB-radiusB) : actualA < actualB := by
  have a := (abs_le.mp ha).2
  have b := (abs_le.mp hb).1
  linarith

end
end FeedbackMemory
