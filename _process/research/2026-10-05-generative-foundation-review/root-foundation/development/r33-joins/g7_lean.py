#!/usr/bin/env python3
"""R33 (G7): the tolerating law as the activity of a web, in Becoming.Tolerance (no new import)."""
from pathlib import Path
B = Path(__file__).resolve().parents[6] / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/Becoming'
p = B / 'Tolerance.lean'
s = p.read_text()
block = '''/-! ## The tolerating law on a web

The formations of a web are relata, each read with one condition, its own (`Web β β`). A formation
`a` requires its own condition at need `k a`, and every formation it waits on, at a step where it
is supported, gives one unit to that condition, nothing being held from one step to the next: the
level of `a`'s condition at the next step is the number of what `a` waits on that is supported now.
Admission at need `k a` is then giving where at least `k a` of what `a` waits on gave: the
tolerating law with tolerance `(ups a).length - k a`. -/

section OnWebs

/-- The number of members of a list that pass a Boolean test. -/
def countTrue (p : α → Bool) : List α → Nat
  | [] => 0
  | b :: l => bif p b then countTrue p l + 1 else countTrue p l

/-- Those that pass and those that fail make up the list. -/
theorem countTrue_add_not (p : α → Bool) : ∀ l : List α,
    countTrue p l + countTrue (fun b => !p b) l = l.length
  | [] => rfl
  | b :: l => match h : p b with
    | true =>
      show (bif p b then countTrue p l + 1 else countTrue p l) +
          (bif !p b then countTrue (fun b => !p b) l + 1 else countTrue (fun b => !p b) l) =
        l.length + 1 from
      h ▸ (Nat.succ_add _ _).trans (congrArg (· + 1) (countTrue_add_not p l))
    | false =>
      show (bif p b then countTrue p l + 1 else countTrue p l) +
          (bif !p b then countTrue (fun b => !p b) l + 1 else countTrue (fun b => !p b) l) =
        l.length + 1 from
      h ▸ congrArg (· + 1) (countTrue_add_not p l)

/-- **All but `f` is a count.** All but at most `f` members of `l` pass a Boolean test exactly
where at most `f` of them fail it. -/
theorem allBut_iff_count (p : α → Bool) : ∀ (f : Nat) (l : List α),
    AllBut (fun b => p b = true) f l ↔ countTrue (fun b => !p b) l ≤ f
  | f, [] => ⟨fun _ => Nat.zero_le f, fun _ => AllBut.nil f⟩
  | f, b :: l => match h : p b with
    | true =>
      have fails : countTrue (fun b => !p b) (b :: l) = countTrue (fun b => !p b) l :=
        show (bif !p b then countTrue (fun b => !p b) l + 1 else countTrue (fun b => !p b) l) =
          countTrue (fun b => !p b) l from h ▸ rfl
      ⟨fun all => match all with
        | AllBut.holds _ rest =>
          Nat.le_trans (Nat.le_of_eq fails) ((allBut_iff_count p f l).mp rest)
        | AllBut.spare _ rest =>
          Nat.le_trans (Nat.le_of_eq fails) (Nat.le_succ_of_le ((allBut_iff_count p _ l).mp rest)),
       fun le => AllBut.holds h
          ((allBut_iff_count p f l).mpr (Nat.le_trans (Nat.le_of_eq fails.symm) le))⟩
    | false =>
      have fails : countTrue (fun b => !p b) (b :: l) = countTrue (fun b => !p b) l + 1 :=
        show (bif !p b then countTrue (fun b => !p b) l + 1 else countTrue (fun b => !p b) l) =
          countTrue (fun b => !p b) l + 1 from h ▸ rfl
      ⟨fun all => match all with
        | AllBut.holds passes _ => Bool.noConfusion (passes.symm.trans h)
        | AllBut.spare _ rest =>
          Nat.le_trans (Nat.le_of_eq fails)
            (Nat.succ_le_succ ((allBut_iff_count p _ l).mp rest)),
       fun le => match f, le with
        | 0, le => absurd (Nat.le_trans (Nat.le_of_eq fails.symm) le) (Nat.not_succ_le_zero _)
        | f + 1, le => AllBut.spare b ((allBut_iff_count p f l).mpr
            (Nat.le_of_succ_le_succ (Nat.le_trans (Nat.le_of_eq fails.symm) le)))⟩

/-- Sparing `m - k` of `m`, all but that many is at least `k` passing. -/
theorem allBut_sub_iff (p : α → Bool) {k : Nat} {l : List α} (within : k ≤ l.length) :
    AllBut (fun b => p b = true) (l.length - k) l ↔ k ≤ countTrue p l :=
  (allBut_iff_count p _ l).trans
    ⟨fun le => Naturals.le_of_add_le_add_right (k := countTrue (fun b => !p b) l)
        (Nat.le_trans (Naturals.add_le_of_le_sub within le)
          (Nat.le_of_eq (countTrue_add_not p l).symm)),
     fun le => Naturals.le_sub_of_add_le
        (Nat.le_trans (Nat.add_le_add_right le _) (Nat.le_of_eq (countTrue_add_not p l)))⟩

/-- Under a law keeping inclusion, starts holding at the same formations give courses holding at
the same formations, at every step. -/
theorem KeepsInclusion.course_iff {next : (α → Prop) → α → Prop} (keeps : KeepsInclusion next)
    {s s' : α → Prop} (same : ∀ a, s a ↔ s' a) (n : Nat) (a : α) :
    (Law.run next s).state n a ↔ (Law.run next s').state n a :=
  ⟨keeps.course (fun b => (same b).mp) n a, keeps.course (fun b => (same b).mpr) n a⟩

variable {β : Type}

/-- **Admission at need `k`, where each supported formation gives one unit to what waits on it, is
the tolerating law.** Let a web of formations `β`, each read with its own condition, have each
formation require its own condition and only it, at need `k a` no more than the number it waits
on, and let the level of `a`'s condition
at each next step be the number of the formations listed in `ups a` supported now. Then a formation
is supported at every step exactly where the tolerating law with tolerance `(ups a).length - k a`,
run from the support at the start, has it give. -/
theorem web_tolerating (W : Web β β) (ups : β → List β) (k : β → Nat)
    (requires : ∀ t a c, W.requires t a c ↔ c = a) (need : ∀ t a, W.need t a a = k a)
    (gives : ∀ t a, W.level (t + 1) a =
      countTrue (fun b => Nat.ble (k b) (W.level t b)) (ups a))
    (within : ∀ a, k a ≤ (ups a).length) :
    ∀ n a, W.Supported n a ↔
      (Law.run (tolerating (fun a => (ups a).length - k a) ups) (W.Supported 0)).state n a :=
  have supported : ∀ t a, W.Supported t a ↔ Nat.ble (k a) (W.level t a) = true := fun t a =>
    ⟨fun admitted => Nat.ble_eq_true_of_le
        (Eq.subst (motive := fun x => x ≤ W.level t a) (need t a)
          (admitted a ((requires t a a).mpr rfl))),
     fun le c required =>
        Eq.subst (motive := fun c => W.need t a c ≤ W.level t c) ((requires t a c).mp required).symm
          (Eq.subst (motive := fun x => x ≤ W.level t a) (need t a).symm
            (Nat.le_of_ble_eq_true le))⟩
  fun n => Nat.rec (motive := fun n => ∀ a, W.Supported n a ↔
      (Law.run (tolerating (fun a => (ups a).length - k a) ups) (W.Supported 0)).state n a)
    (fun _ => Iff.rfl)
    (fun n ih a =>
      have count : W.Supported (n + 1) a ↔
          k a ≤ countTrue (fun b => Nat.ble (k b) (W.level n b)) (ups a) :=
        (supported (n + 1) a).trans
          ⟨fun le => Eq.subst (motive := fun x => k a ≤ x) (gives n a) (Nat.le_of_ble_eq_true le),
           fun le => Nat.ble_eq_true_of_le
             (Eq.subst (motive := fun x => k a ≤ x) (gives n a).symm le)⟩
      count.trans (allBut_sub_iff _ (within a)).symm |>.trans
        ⟨AllBut.mono_set fun b passes => (ih b).mp ((supported n b).mpr passes),
         AllBut.mono_set fun b gives => (supported n b).mp ((ih b).mpr gives)⟩)
    n

/-- **The web's activity runs the tolerating law** where a formation is active exactly where it is
supported: activity at every step is the course of the tolerating law from the activity at the
start. -/
theorem web_activity_tolerating (W : Web β β) (ups : β → List β) (k : β → Nat)
    (requires : ∀ t a c, W.requires t a c ↔ c = a) (need : ∀ t a, W.need t a a = k a)
    (gives : ∀ t a, W.level (t + 1) a =
      countTrue (fun b => Nat.ble (k b) (W.level t b)) (ups a))
    (within : ∀ a, k a ≤ (ups a).length) (acts : ∀ t a, W.active t a ↔ W.Supported t a)
    (n : Nat) (a : β) :
    W.active n a ↔
      (Law.run (tolerating (fun a => (ups a).length - k a) ups) (W.active 0)).state n a :=
  (acts n a).trans ((web_tolerating W ups k requires need gives within n a).trans
    ((tolerating_keeps _ ups).course_iff (fun b => (acts 0 b).symm) n a))

/-- **Waiting on all is the case of need equal to the number waited on**: the web's support runs
`Withholding.answers` on the listed waits. -/
theorem web_answers (W : Web β β) (ups : β → List β) (k : β → Nat)
    (requires : ∀ t a c, W.requires t a c ↔ c = a) (need : ∀ t a, W.need t a a = k a)
    (gives : ∀ t a, W.level (t + 1) a =
      countTrue (fun b => Nat.ble (k b) (W.level t b)) (ups a))
    (all : ∀ a, k a = (ups a).length) (n : Nat) (a : β) :
    W.Supported n a ↔ (Law.run (answers (Listed ups)) (W.Supported 0)).state n a :=
  have none : ∀ a, (ups a).length - k a = 0 := fun a =>
    Eq.subst (motive := fun x => (ups a).length - x = 0) (all a).symm (Nat.sub_self _)
  have zero : ∀ n a,
      (Law.run (tolerating (fun a => (ups a).length - k a) ups) (W.Supported 0)).state n a ↔
        (Law.run (tolerating (fun _ => 0) ups) (W.Supported 0)).state n a := fun n =>
    Nat.rec (motive := fun n => ∀ a,
        (Law.run (tolerating (fun a => (ups a).length - k a) ups) (W.Supported 0)).state n a ↔
          (Law.run (tolerating (fun _ => 0) ups) (W.Supported 0)).state n a)
      (fun _ => Iff.rfl)
      (fun _ ih a =>
        ⟨fun spared => AllBut.mono_set (fun b => (ih b).mp)
            (Eq.subst (motive := fun f => AllBut _ f (ups a)) (none a) spared),
         fun spared => Eq.subst (motive := fun f => AllBut _ f (ups a)) (none a).symm
            (AllBut.mono_set (fun b => (ih b).mpr) spared)⟩)
      n
  (web_tolerating W ups k requires need gives (fun a => Nat.le_of_eq (all a)) n a).trans
    ((zero n a).trans (tolerating_zero ups _ n a))

/-- The levels of the web built from what each formation waits on, the needs and the levels at the
start: at each next step, the number of what a formation waits on that its need admits now. -/
def giftLevels (ups : β → List β) (k : β → Nat) (start : β → Nat) : Nat → β → Nat
  | 0 => start
  | t + 1 => fun a => countTrue (fun b => Nat.ble (k b) (giftLevels ups k start t b)) (ups a)

/-- **The web of giving one unit to what waits.** Each formation requires its own condition at need
`k a`, is active where its need is met, draws on nothing, and its condition's level is
`giftLevels`. -/
def giftWeb (ups : β → List β) (k : β → Nat) (start : β → Nat) : Web β β :=
  ⟨giftLevels ups k start, fun t a => k a ≤ giftLevels ups k start t a, fun _ a c => c = a,
   fun _ a _ => k a, fun _ _ _ => False⟩

/-- **The web of giving one unit to what waits runs the tolerating law**, from every start, with
every need at most the number waited on. -/
theorem giftWeb_tolerating (ups : β → List β) (k : β → Nat) (start : β → Nat)
    (within : ∀ a, k a ≤ (ups a).length) (n : Nat) (a : β) :
    (giftWeb ups k start).active n a ↔
      (Law.run (tolerating (fun a => (ups a).length - k a) ups)
        ((giftWeb ups k start).active 0)).state n a :=
  web_activity_tolerating (giftWeb ups k start) ups k (fun _ _ _ => Iff.rfl) (fun _ _ => rfl)
    (fun _ _ => rfl) within
    (fun _ a => ⟨fun le _ same => Eq.subst (motive := fun c => k a ≤ giftLevels ups k start _ c)
        same.symm le, fun admitted => admitted a rfl⟩) n a

end OnWebs

'''
anchor = '/-! ## Witness: three formations each waiting on the other two -/'
assert s.count(anchor) == 1
s = s.replace(anchor, block + anchor)
p.write_text(s)
