/-!
Many centers, unequal and renewing claims.

`RecordedClaims` treated two centers with equal one-unit claims and flag
records. Here there are `n` centers and the record holds a number per center:
its remaining claim, or the time it was last served. A rule maps a record to
serving one center or withholding. A rule *treats the centers alike* when
exchanging two centers' entries in the record exchanges its output.

Results:

* an alike rule never serves a center whose entry another center shares
  (`tied_not_served`); with all entries equal it withholds
  (`all_tied_forces_withholding`); and for each center there is an alike rule
  serving it exactly when its entry is not shared (`servable_iff_untied`);
* **unequal claims.** With remaining claims as entries, a record admits an
  alike choice that forecloses nothing needlessly exactly when all claims are
  met or some open claim differs in size from every other
  (`alike_nonforeclosing_iff`). Unequal sizes let structure choose, but they
  do not say which claim goes first: with open claims of sizes 1 and 2, each
  center can be served by an alike, nonforeclosing rule
  (`unequal_claims_leave_priority_open`). Priority by size is a further
  premise. Equal open claims remain the `RecordedClaims` obstacle;
* **renewing claims.** With last-service times as entries, the rule "serve
  the least recently served" treats the centers alike. Once an initial order
  is supplied (distinct entries), it serves at every step, and between two
  services of any center it serves every other center
  (`renewing_claims_served_in_turn`). Before any order exists (all entries
  equal), no alike rule serves (`renewing_claims_need_initial_order`).
  Remark, not a theorem: flag records lose the order each time claims renew,
  while time records keep it, so one supplied order suffices for every later
  round. Renewal is modelled implicitly: every center always holds a claim,
  without claim sizes.

Service is one unit per step, centers are fixed, and the least-recent rule is
one alike rule among others (the most-recent rule is alike too and serves one
center forever); that turn-taking is what renewing claims are owed is not
derived here.
-/
namespace PluralRecords

abbrev Record (n : Nat) := Fin n → Nat
abbrev Rule (n : Nat) := Record n → Option (Fin n)

/-- Exchange centers `a` and `b`. -/
def transpose {n : Nat} (a b k : Fin n) : Fin n :=
  if k = a then b else if k = b then a else k

theorem transpose_left {n : Nat} (a b : Fin n) : transpose a b a = b := by
  unfold transpose; rw [if_pos rfl]

theorem transpose_right {n : Nat} (a b : Fin n) : transpose a b b = a := by
  unfold transpose
  match decEq b a with
  | isTrue h => rw [if_pos h]; exact h
  | isFalse h => rw [if_neg h, if_pos rfl]

theorem transpose_other {n : Nat} (a b k : Fin n) (ha : k ≠ a) (hb : k ≠ b) :
    transpose a b k = k := by
  unfold transpose; rw [if_neg ha, if_neg hb]

theorem transpose_transpose {n : Nat} (a b k : Fin n) :
    transpose a b (transpose a b k) = k := by
  match decEq k a with
  | isTrue h => rw [h, transpose_left, transpose_right]
  | isFalse ha =>
    match decEq k b with
    | isTrue h => rw [h, transpose_right, transpose_left]
    | isFalse hb => rw [transpose_other a b k ha hb, transpose_other a b k ha hb]

theorem transpose_inj {n : Nat} (a b : Fin n) {x y : Fin n}
    (h : transpose a b x = transpose a b y) : x = y := by
  rw [← transpose_transpose a b x, h, transpose_transpose]

/-- The record with centers `a` and `b` exchanged. -/
def relabel {n : Nat} (r : Record n) (a b : Fin n) : Record n :=
  fun k => r (transpose a b k)

/-- Exchanging two centers' entries exchanges the rule's output. Stated
pointwise: any record whose entries are another's relabeled; this needs no
equality of functions. -/
def TreatsAlike {n : Nat} (rule : Rule n) : Prop :=
  ∀ r r' a b, (∀ k, r' k = r (transpose a b k)) → rule r' = (rule r).map (transpose a b)

/-- Exchanging two centers with equal entries leaves every entry unchanged. -/
theorem relabel_of_tie {n : Nat} (r : Record n) (j k : Fin n) (tie : r j = r k) :
    ∀ x, r x = r (transpose j k x) := by
  intro x
  match decEq x j with
  | isTrue h => rw [h, transpose_left]; exact tie
  | isFalse hj =>
    match decEq x k with
    | isTrue h => rw [h, transpose_right]; exact tie.symm
    | isFalse hk => rw [transpose_other j k x hj hk]

/-- An alike rule never serves a center whose entry another center shares. -/
theorem tied_not_served {n : Nat} (rule : Rule n) (alike : TreatsAlike rule)
    (r : Record n) (k j : Fin n) (hjk : j ≠ k) (tie : r j = r k) : rule r ≠ some k := by
  intro hk
  have h := alike r r j k (relabel_of_tie r j k tie)
  rw [hk] at h
  have hkk : transpose j k k = j := transpose_right j k
  rw [Option.map_some, hkk] at h
  exact hjk (Option.some.inj h).symm

theorem one_ne_zero' : (1 : Nat) ≠ 0 := by decide

theorem fin_other {n : Nat} (two : 2 ≤ n) (k : Fin n) : ∃ j : Fin n, j ≠ k :=
  match Nat.decEq k.val 0 with
  | isTrue h0 => ⟨⟨1, Nat.lt_of_lt_of_le (by decide) two⟩, fun e =>
      one_ne_zero' ((congrArg Fin.val e).trans h0)⟩
  | isFalse h0 => ⟨⟨0, Nat.lt_of_lt_of_le (by decide) two⟩, fun e =>
      h0 (congrArg Fin.val e).symm⟩

/-- With at least two centers and all entries equal, an alike rule withholds. -/
theorem all_tied_forces_withholding {n : Nat} (rule : Rule n) (alike : TreatsAlike rule)
    (r : Record n) (two : 2 ≤ n) (tied : ∀ i j, r i = r j) : rule r = none := by
  cases hk : rule r with
  | none => rfl
  | some k =>
    exfalso
    obtain ⟨j, hj⟩ := fin_other two k
    exact tied_not_served rule alike r k j hj (tied _ k) hk

/-! A rule built from a predicate that holds of at most one center. -/

def pick {n : Nat} (p : Fin n → Prop) [DecidablePred p] : Option (Fin n) :=
  (List.finRange n).find? (fun i => decide (p i))

theorem find?_some_true {α : Type} (q : α → Bool) :
    ∀ (l : List α) {x : α}, l.find? q = some x → q x = true
  | [], x, h => by
    have h' : (none : Option α) = some x := h
    exact nomatch h'
  | a :: as, x, h => by
    rw [List.find?_cons] at h
    cases hq : q a with
    | true =>
      rw [hq] at h
      have h' : some a = some x := h
      rw [← Option.some.inj h']; exact hq
    | false =>
      rw [hq] at h
      exact find?_some_true q as h

theorem find?_none_false {α : Type} (q : α → Bool) :
    ∀ (l : List α), l.find? q = none → ∀ y, y ∈ l → q y = false
  | [], _, _, hy => nomatch hy
  | a :: as, h, y, hy => by
    rw [List.find?_cons] at h
    cases hq : q a with
    | true =>
      rw [hq] at h
      have h' : some a = none := h
      exact nomatch h'
    | false =>
      rw [hq] at h
      cases hy with
      | head => exact hq
      | tail _ hy' => exact find?_none_false q as h y hy'

theorem mem_finRange_loop {n : Nat} : ∀ (i : Nat) (h : i ≤ n) (x : List (Fin n)),
    (∀ y, y ∈ x → y ∈ Fin.foldr.loop n (fun j acc => j :: acc) i h x) ∧
    (∀ k : Fin n, k.val < i → k ∈ Fin.foldr.loop n (fun j acc => j :: acc) i h x)
  | 0, _, _ => ⟨fun _ hy => hy, fun _ hk => absurd hk (Nat.not_lt_zero _)⟩
  | i + 1, h, x => by
    have ih := mem_finRange_loop i (Nat.le_of_lt h) (⟨i, h⟩ :: x)
    refine ⟨fun y hy => ih.1 y (List.Mem.tail _ hy), fun k hk => ?_⟩
    match Nat.lt_or_ge k.val i with
    | .inl lt => exact ih.2 k lt
    | .inr ge =>
      have e : k = ⟨i, h⟩ := Fin.ext (Nat.le_antisymm (Nat.le_of_lt_succ hk) ge)
      rw [e]; exact ih.1 _ (List.Mem.head _)

theorem mem_finRange' {n : Nat} (i : Fin n) : i ∈ List.finRange n :=
  (mem_finRange_loop n (Nat.le_refl n) []).2 i i.isLt

theorem pick_some {n : Nat} (p : Fin n → Prop) [DecidablePred p] {i : Fin n}
    (h : pick p = some i) : p i :=
  of_decide_eq_true (find?_some_true (fun i => decide (p i)) (List.finRange n) h)

theorem pick_none {n : Nat} (p : Fin n → Prop) [DecidablePred p]
    (h : pick p = none) (i : Fin n) : ¬ p i :=
  of_decide_eq_false (find?_none_false (fun i => decide (p i)) (List.finRange n) h i
    (mem_finRange' i))

theorem pick_unique {n : Nat} (p : Fin n → Prop) [DecidablePred p]
    (uniq : ∀ i j, p i → p j → i = j) {i : Fin n} (hi : p i) : pick p = some i := by
  cases h : pick p with
  | none => exact absurd hi (pick_none p h i)
  | some j => rw [uniq j i (pick_some p h) hi]

/-- If `P r` holds of at most one center and relabeling the record relabels
`P`, the rule `pick (P r)` treats the centers alike. -/
theorem pick_alike {n : Nat} (P : Record n → Fin n → Prop) [∀ r, DecidablePred (P r)]
    (uniq : ∀ r i j, P r i → P r j → i = j)
    (equi : ∀ r r' a b, (∀ k, r' k = r (transpose a b k)) →
      ∀ i, P r' i ↔ P r (transpose a b i)) :
    TreatsAlike (fun r => pick (P r)) := by
  intro r r' a b hr
  show pick (P r') = (pick (P r)).map (transpose a b)
  cases h : pick (P r) with
  | some i =>
    have hi := pick_some (P r) h
    apply pick_unique _ (uniq _)
    exact (equi r r' a b hr _).mpr (by rw [transpose_transpose]; exact hi)
  | none =>
    cases h' : pick (P r') with
    | none => rfl
    | some i =>
      exact absurd ((equi r r' a b hr i).mp (pick_some _ h')) (pick_none (P r) h _)

/-- The centers holding a given entry `v` alone. -/
def Alone {n : Nat} (v : Nat) (r : Record n) (i : Fin n) : Prop :=
  r i = v ∧ ∀ j, j ≠ i → r j ≠ v

instance {n : Nat} (v : Nat) (r : Record n) : DecidablePred (Alone v r) :=
  fun _ => inferInstanceAs (Decidable (_ ∧ _))

theorem alone_alike {n : Nat} (v : Nat) : TreatsAlike (fun r : Record n => pick (Alone v r)) := by
  apply pick_alike
  · intro r i j hi hj
    exact Decidable.byContradiction fun h => hj.2 i h hi.1
  · intro r r' a b hr i
    constructor
    · intro ⟨h1, h2⟩
      refine ⟨(hr i).symm.trans h1, fun j hj => ?_⟩
      have := h2 (transpose a b j) (fun e => hj (by rw [← e, transpose_transpose]))
      have e2 : r' (transpose a b j) = r j := by rw [hr, transpose_transpose]
      rw [e2] at this; exact this
    · intro ⟨h1, h2⟩
      exact ⟨(hr i).trans h1, fun j hj e =>
        h2 _ (fun e' => hj (transpose_inj a b e')) ((hr j).symm.trans e)⟩

/-- An alike rule can serve center `k` exactly when no other center shares
its entry. -/
theorem servable_iff_untied {n : Nat} (r : Record n) (k : Fin n) :
    (∃ rule : Rule n, TreatsAlike rule ∧ rule r = some k) ↔ ∀ j, j ≠ k → r j ≠ r k := by
  constructor
  · intro ⟨rule, alike, hk⟩ j hj tie
    exact tied_not_served rule alike r k j hj tie hk
  · intro h
    exact ⟨_, alone_alike (r k), pick_unique _ (fun i j hi hj =>
      Decidable.byContradiction fun e => hj.2 i e hi.1) ⟨rfl, h⟩⟩

/-! Unequal remaining claims. The entry is the claim still open (`0` means
fulfilled). `ServesOpenClaim` counts withholding, or serving a fulfilled
claim, while some claim is open as needless. Unlike `ContinuationScope`, it
gives no credit to support retained by withholding: support is taken to
perish with the step, as in `RecordedClaims`. -/

def ServesOpenClaim {n : Nat} (r : Record n) : Option (Fin n) → Prop
  | none => ∀ j, r j = 0
  | some k => 0 < r k ∨ ∀ j, r j = 0

theorem withholding_alike {n : Nat} : TreatsAlike (fun _ : Record n => none) := by
  intro _ _ _ _ _; rfl

/-- A record admits an alike, nonforeclosing choice exactly when all claims
are fulfilled or some open claim differs in size from every other claim. -/
theorem alike_nonforeclosing_iff {n : Nat} (r : Record n) :
    (∃ rule : Rule n, TreatsAlike rule ∧ ServesOpenClaim r (rule r)) ↔
      (∀ j, r j = 0) ∨ ∃ k, 0 < r k ∧ ∀ j, j ≠ k → r j ≠ r k := by
  constructor
  · intro ⟨rule, alike, nf⟩
    cases hk : rule r with
    | none => rw [hk] at nf; exact .inl nf
    | some k =>
      rw [hk] at nf
      cases nf with
      | inl pos => exact .inr ⟨k, pos, (servable_iff_untied r k).mp ⟨rule, alike, hk⟩⟩
      | inr all => exact .inl all
  · intro hyp
    cases hyp with
    | inl all => exact ⟨_, withholding_alike, all⟩
    | inr hk =>
      obtain ⟨k, pos, untied⟩ := hk
      obtain ⟨rule, alike, hk⟩ := (servable_iff_untied r k).mpr untied
      exact ⟨rule, alike, by rw [hk]; exact .inl pos⟩

/-- Unequal claims let structure choose, but not which: with open claims of
sizes 1 and 2, serving either center is alike and nonforeclosing. -/
theorem unequal_claims_leave_priority_open :
    let r : Record 2 := fun i => i.val + 1
    (∃ rule : Rule 2, TreatsAlike rule ∧ rule r = some ⟨0, by decide⟩ ∧
      ServesOpenClaim r (rule r)) ∧
    (∃ rule : Rule 2, TreatsAlike rule ∧ rule r = some ⟨1, by decide⟩ ∧
      ServesOpenClaim r (rule r)) := by
  intro r
  have s : ∀ k : Fin 2, pick (Alone (r k) r) = some k := fun k =>
    pick_unique _ (fun i j hi hj => Decidable.byContradiction fun e => hj.2 i e hi.1)
      ⟨rfl, fun j hj e => hj (Fin.ext (Nat.succ.inj e))⟩
  exact ⟨⟨_, alone_alike (r ⟨0, by decide⟩), s ⟨0, by decide⟩,
      by rw [s ⟨0, by decide⟩]; exact .inl (Nat.zero_lt_succ _)⟩,
    ⟨_, alone_alike (r ⟨1, by decide⟩), s ⟨1, by decide⟩,
      by rw [s ⟨1, by decide⟩]; exact .inl (Nat.zero_lt_succ _)⟩⟩

/-! Renewing claims. The entry is the time a center was last served. Each
step serves the least recently served center and records the current time. -/

def LeastRecent {n : Nat} (r : Record n) (i : Fin n) : Prop := ∀ j, j ≠ i → r i < r j

instance {n : Nat} (r : Record n) : DecidablePred (LeastRecent r) :=
  fun _ => inferInstanceAs (Decidable (∀ _, _))

def leastRecent {n : Nat} : Rule n := fun r => pick (LeastRecent r)

theorem leastRecent_unique {n : Nat} (r : Record n) (i j : Fin n)
    (hi : LeastRecent r i) (hj : LeastRecent r j) : i = j :=
  Decidable.byContradiction fun e =>
    Nat.lt_asymm (hi j (fun h => e h.symm)) (hj i e)

theorem leastRecent_alike {n : Nat} : TreatsAlike (@leastRecent n) := by
  apply pick_alike _ leastRecent_unique
  intro r r' a b hr i
  constructor
  · intro h j hj
    have := h (transpose a b j) (fun e => hj (by rw [← e, transpose_transpose]))
    have e2 : r' (transpose a b j) = r j := by rw [hr, transpose_transpose]
    rw [e2, hr i] at this; exact this
  · intro h j hj
    have := h _ (fun e => hj (transpose_inj a b e))
    rw [hr i, hr j]; exact this

def Injective {n : Nat} (r : Record n) : Prop := ∀ i j, r i = r j → i = j

theorem exists_min {n : Nat} (r : Record n) (i0 : Fin n) : ∃ i, ∀ j, r i ≤ r j := by
  suffices ∀ v, (∃ i, r i ≤ v) → ∃ i, ∀ j, r i ≤ r j from this _ ⟨i0, Nat.le_refl _⟩
  intro v
  induction v with
  | zero => intro ⟨i, hi⟩; exact ⟨i, fun j => Nat.le_trans hi (Nat.zero_le _)⟩
  | succ v ih =>
    intro ⟨i, hi⟩
    cases h : pick (fun k => r k ≤ v) with
    | some k => exact ih ⟨k, pick_some _ h⟩
    | none =>
      exact ⟨i, fun j => Nat.le_trans hi
        (Nat.succ_le_of_lt (Nat.lt_of_not_le (pick_none _ h j)))⟩

theorem leastRecent_serves {n : Nat} (r : Record n) (inj : Injective r) (i0 : Fin n) :
    ∃ k, leastRecent r = some k := by
  obtain ⟨i, hi⟩ := exists_min r i0
  exact ⟨i, pick_unique _ (leastRecent_unique r) (fun j hj =>
    Nat.lt_of_le_of_ne (hi j) (fun e => hj (inj _ _ e).symm))⟩

/-- Serve `rule`'s choice at time `t`, recording `t`. -/
def step {n : Nat} (rule : Rule n) (r : Record n) (t : Nat) : Record n :=
  match rule r with
  | none => r
  | some k => fun j => if j = k then t else r j

/-- The record after `s` steps, starting at time `t0`. -/
def run {n : Nat} (rule : Rule n) (r0 : Record n) (t0 : Nat) : Nat → Record n
  | 0 => r0
  | s + 1 => step rule (run rule r0 t0 s) (t0 + s)

def served {n : Nat} (rule : Rule n) (r0 : Record n) (t0 s : Nat) : Option (Fin n) :=
  rule (run rule r0 t0 s)

section Run
variable {n : Nat} (rule : Rule n) (r0 : Record n) (t0 : Nat)

theorem run_succ_apply (s : Nat) (j : Fin n) :
    run rule r0 t0 (s + 1) j =
      if served rule r0 t0 s = some j then t0 + s else run rule r0 t0 s j := by
  show step rule (run rule r0 t0 s) (t0 + s) j =
    if rule (run rule r0 t0 s) = some j then t0 + s else run rule r0 t0 s j
  unfold step
  cases h : rule (run rule r0 t0 s) with
  | none => exact (if_neg (fun e => nomatch e)).symm
  | some k =>
    show (if j = k then t0 + s else run rule r0 t0 s j) = _
    match decEq j k with
    | isTrue hjk => rw [if_pos hjk, if_pos (congrArg some hjk.symm)]
    | isFalse hjk => rw [if_neg hjk, if_neg (fun e => hjk (Option.some.inj e).symm)]

theorem run_lt (fresh : ∀ j, r0 j < t0) (s : Nat) (j : Fin n) : run rule r0 t0 s j < t0 + s := by
  induction s with
  | zero => exact fresh j
  | succ s ih =>
    rw [run_succ_apply]
    match decEq (served rule r0 t0 s) (some j) with
    | isTrue h => rw [if_pos h]; exact Nat.lt_add_one _
    | isFalse h => rw [if_neg h]; exact Nat.lt_succ_of_lt ih

theorem run_mono (fresh : ∀ j, r0 j < t0) (s : Nat) (j : Fin n) :
    run rule r0 t0 s j ≤ run rule r0 t0 (s + 1) j := by
  rw [run_succ_apply]
  match decEq (served rule r0 t0 s) (some j) with
  | isTrue h => rw [if_pos h]; exact Nat.le_of_lt (run_lt rule r0 t0 fresh s j)
  | isFalse h => rw [if_neg h]; exact Nat.le_refl _

theorem run_mono_le (fresh : ∀ j, r0 j < t0) (s d : Nat) (j : Fin n) :
    run rule r0 t0 s j ≤ run rule r0 t0 (s + d) j := by
  induction d with
  | zero => exact Nat.le_refl _
  | succ d ih => exact Nat.le_trans ih (run_mono rule r0 t0 fresh _ j)

/-- An entry at least `t0 + s` was written by a service at or after step `s`. -/
theorem recent_entry_was_served (fresh : ∀ j, r0 j < t0) (s d : Nat) (j : Fin n)
    (h : t0 + s ≤ run rule r0 t0 (s + d) j) :
    ∃ u, s ≤ u ∧ u < s + d ∧ served rule r0 t0 u = some j := by
  induction d with
  | zero => exact absurd h (Nat.not_le_of_lt (run_lt rule r0 t0 fresh s j))
  | succ d ih =>
    rw [← Nat.add_assoc, run_succ_apply] at h
    match decEq (served rule r0 t0 (s + d)) (some j) with
    | isTrue hs => exact ⟨s + d, Nat.le_add_right s d, Nat.lt_add_one _, hs⟩
    | isFalse hs =>
      rw [if_neg hs] at h
      obtain ⟨u, h1, h2, h3⟩ := ih h; exact ⟨u, h1, Nat.lt_succ_of_lt h2, h3⟩

theorem run_injective (fresh : ∀ j, r0 j < t0) (inj : Injective r0) (s : Nat) :
    Injective (run rule r0 t0 s) := by
  induction s with
  | zero => exact inj
  | succ s ih =>
    intro i j e
    rw [run_succ_apply, run_succ_apply] at e
    have li := run_lt rule r0 t0 fresh s i
    have lj := run_lt rule r0 t0 fresh s j
    match decEq (served rule r0 t0 s) (some i), decEq (served rule r0 t0 s) (some j) with
    | isTrue hi, isTrue hj => rw [hi] at hj; exact Option.some.inj hj
    | isTrue hi, isFalse hj =>
      rw [if_pos hi, if_neg hj] at e; rw [← e] at lj; exact absurd lj (Nat.lt_irrefl _)
    | isFalse hi, isTrue hj =>
      rw [if_neg hi, if_pos hj] at e; rw [e] at li; exact absurd li (Nat.lt_irrefl _)
    | isFalse hi, isFalse hj =>
      rw [if_neg hi, if_neg hj] at e; exact ih i j e

end Run

/-- After one supplied initial order (distinct entries before time `t0`),
the least-recent rule, which treats the centers alike, serves at every step,
and between two services of any center it serves every other center. -/
theorem renewing_claims_served_in_turn {n : Nat} (r0 : Record n) (t0 : Nat)
    (fresh : ∀ j, r0 j < t0) (inj : Injective r0) :
    TreatsAlike (@leastRecent n) ∧
    (∀ s, 0 < n → ∃ k, served leastRecent r0 t0 s = some k) ∧
    (∀ s d (k j : Fin n), j ≠ k →
      served leastRecent r0 t0 s = some k → served leastRecent r0 t0 (s + 1 + d) = some k →
      ∃ u, s < u ∧ u < s + 1 + d ∧ served leastRecent r0 t0 u = some j) := by
  refine ⟨leastRecent_alike, fun s pos =>
    leastRecent_serves _ (run_injective _ r0 t0 fresh inj s) ⟨0, pos⟩, ?_⟩
  intro s d k j hjk hs hs'
  have least := pick_some _ hs'
  have hk1 : run leastRecent r0 t0 (s + 1) k = t0 + s := by
    rw [run_succ_apply, if_pos hs]
  have hk := run_mono_le leastRecent r0 t0 fresh (s + 1) d k
  have hlt := least j hjk
  rw [hk1] at hk
  obtain ⟨u, h1, h2, h3⟩ :=
    recent_entry_was_served leastRecent r0 t0 fresh (s + 1) d j
      (Nat.succ_le_of_lt (Nat.lt_of_le_of_lt hk hlt))
  exact ⟨u, h1, h2, h3⟩

/-- Before any order is supplied (all entries equal), no alike rule serves. -/
theorem renewing_claims_need_initial_order {n : Nat} (two : 2 ≤ n) (rule : Rule n)
    (alike : TreatsAlike rule) (t : Nat) : rule (fun _ => t) = none :=
  all_tied_forces_withholding rule alike _ two (fun _ _ => rfl)

end PluralRecords

#print axioms PluralRecords.Record
#print axioms PluralRecords.Rule
#print axioms PluralRecords.transpose
#print axioms PluralRecords.transpose_transpose
#print axioms PluralRecords.transpose_inj
#print axioms PluralRecords.relabel
#print axioms PluralRecords.TreatsAlike
#print axioms PluralRecords.relabel_of_tie
#print axioms PluralRecords.tied_not_served
#print axioms PluralRecords.all_tied_forces_withholding
#print axioms PluralRecords.pick
#print axioms PluralRecords.pick_some
#print axioms PluralRecords.pick_none
#print axioms PluralRecords.pick_unique
#print axioms PluralRecords.pick_alike
#print axioms PluralRecords.Alone
#print axioms PluralRecords.alone_alike
#print axioms PluralRecords.servable_iff_untied
#print axioms PluralRecords.ServesOpenClaim
#print axioms PluralRecords.withholding_alike
#print axioms PluralRecords.alike_nonforeclosing_iff
#print axioms PluralRecords.unequal_claims_leave_priority_open
#print axioms PluralRecords.LeastRecent
#print axioms PluralRecords.leastRecent
#print axioms PluralRecords.leastRecent_unique
#print axioms PluralRecords.leastRecent_alike
#print axioms PluralRecords.Injective
#print axioms PluralRecords.exists_min
#print axioms PluralRecords.leastRecent_serves
#print axioms PluralRecords.step
#print axioms PluralRecords.run
#print axioms PluralRecords.served
#print axioms PluralRecords.run_succ_apply
#print axioms PluralRecords.run_lt
#print axioms PluralRecords.run_mono
#print axioms PluralRecords.run_mono_le
#print axioms PluralRecords.recent_entry_was_served
#print axioms PluralRecords.run_injective
#print axioms PluralRecords.renewing_claims_served_in_turn
#print axioms PluralRecords.renewing_claims_need_initial_order
#print axioms PluralRecords.transpose_left
#print axioms PluralRecords.transpose_right
#print axioms PluralRecords.transpose_other
#print axioms PluralRecords.fin_other
#print axioms PluralRecords.find?_some_true
#print axioms PluralRecords.find?_none_false
#print axioms PluralRecords.mem_finRange_loop
#print axioms PluralRecords.mem_finRange'
#print axioms PluralRecords.one_ne_zero'
