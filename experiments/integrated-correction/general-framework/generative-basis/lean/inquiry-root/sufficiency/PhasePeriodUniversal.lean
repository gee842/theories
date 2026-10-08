import PhasePeriodSelection

/-!
# Toward the period lower bound for every period: the reduction lemmas

Study note: _process/research/2026-10-05-generative-foundation-review/root-foundation/
PHASE-PERIOD-ASSUMPTIONS.md.

`PhasePeriodSelection` proved by exhaustive enumeration, for periods one through
eight only, that no two-valued contact pattern lets both contact values be
settled within six native commands, and that seven suffice only for patterns
that repeat a three-phase pattern. This module proves the general lemmas on
which the unbounded statement is to rest. It does **not** yet prove the
unbounded statement; the study note records the exact resume point.

1. **Fewer candidates never make settling harder** (`knows_sub`). The game
   `knowsWithin` succeeds on every sub-collection of a belief on which it
   succeeds, for every pattern and period.
2. **Only what is read nearby matters** (`knows_transfer`). Two beliefs whose
   candidates are paired, with equal inversions and equal contact values along
   every advance up to the remaining number of commands, are settled by exactly
   the same command counts, even when the two patterns and periods differ.
3. **Arithmetic of the advance without `propext`.** The core lemmas on `%`
   (`Nat.mod_eq_of_lt`, `Nat.add_mod_right`, `Nat.mod_mod`, ...) depend on
   `propext`; they are re-proved here from the definition of `Nat.modCore`
   (`mod_of_lt`, `add_period_mod`, `add_periods_mod`, `succ_mod_mod`), giving the
   closed form of repeated advance (`iter_formula`) and its composition
   (`iter_add`).
4. **Stretches read forward from a phase** (`walk`, `bitAt_walk`): the contact
   values met by successive advances, the local data to which items 1 and 2
   reduce the whole game.

Not yet proved here: the finite check that every fourteen-value stretch with a
defect after a non-defect (or a defect everywhere, or no variation) loses its
seven-phase local game within seven commands, the extraction of such a stretch
from every pattern that does not repeat with step three, and the resulting
general theorems. The retained-cell count, the unsettled start and the
requirement to settle both values remain supplied as in `PhasePeriodSelection`.
-/

namespace Generative.InquirySufficiency.PhasePeriodUniversal

open Generative.InquirySufficiency.PacketLawDerivation (sub_add_cancel_constructive)
open Generative.InquirySufficiency.PhaseCycleDerivation (bitAt allOf anyOf upto patterns)
open Generative.InquirySufficiency.PhasePeriodSelection
  (contactKnown readsAs advanceAll knowsWithin unknownStart allOf_member
    member_append_left member_append_right member_map member_upto)

/-! ## Boolean and list facts, without extensionality axioms -/

theorem or_cases {a b : Bool} (both : (a || b) = true) : a = true ∨ b = true := by
  cases a with
  | false => exact Or.inr both
  | true => exact Or.inl rfl

theorem and_cases {a b : Bool} (both : (a && b) = true) : a = true ∧ b = true := by
  cases a with
  | false => cases both
  | true => exact ⟨rfl, both⟩

theorem or_left {a : Bool} (b : Bool) (left : a = true) : (a || b) = true := by
  rw [left]
  rfl

theorem or_right (a : Bool) {b : Bool} (right : b = true) : (a || b) = true := by
  rw [right]
  cases a <;> rfl

theorem and_both {a b : Bool} (left : a = true) (right : b = true) : (a && b) = true := by
  rw [left, right]
  rfl

theorem allOf_intro {α : Type} (test : α → Bool) :
    ∀ (items : List α), (∀ item, item ∈ items → test item = true) → allOf items test = true
  | [], _ => rfl
  | head :: rest, all => by
    change (test head && allOf rest test) = true
    exact and_both (all head (.head _))
      (allOf_intro test rest (fun item member => all item (.tail _ member)))

theorem allOf_witness {α : Type} (test : α → Bool) :
    ∀ (items : List α), allOf items test = false → ∃ item, item ∈ items ∧ test item = false
  | [], failing => by cases failing
  | head :: rest, failing => by
    change (test head && allOf rest test) = false at failing
    cases first : test head with
    | false => exact ⟨head, .head _, first⟩
    | true =>
      rw [first] at failing
      obtain ⟨item, member, failed⟩ := allOf_witness test rest failing
      exact ⟨item, .tail _ member, failed⟩

theorem member_map_inv {α β : Type} (f : α → β) {item : β} :
    ∀ {items : List α}, item ∈ items.map f → ∃ x, x ∈ items ∧ f x = item
  | [], member => nomatch member
  | head :: rest, member => by
    change item ∈ f head :: rest.map f at member
    cases member with
    | head => exact ⟨head, .head _, rfl⟩
    | tail _ later =>
      obtain ⟨x, inside, same⟩ := member_map_inv f later
      exact ⟨x, .tail _ inside, same⟩

theorem member_append_inv {α : Type} {item : α} :
    ∀ {left : List α} {right : List α}, item ∈ left ++ right → item ∈ left ∨ item ∈ right
  | [], _, member => Or.inr member
  | head :: rest, right, member => by
    change item ∈ head :: (rest ++ right) at member
    cases member with
    | head => exact Or.inl (.head _)
    | tail _ later =>
      cases member_append_inv later with
      | inl inside => exact Or.inl (.tail _ inside)
      | inr inside => exact Or.inr inside

theorem member_filter_inv {α : Type} (test : α → Bool) {item : α} :
    ∀ {items : List α}, item ∈ items.filter test → item ∈ items ∧ test item = true
  | [], member => nomatch member
  | head :: rest, member => by
    cases keep : test head with
    | true =>
      rw [List.filter_cons_of_pos keep] at member
      cases member with
      | head => exact ⟨.head _, keep⟩
      | tail _ later =>
        obtain ⟨inside, passes⟩ := member_filter_inv test later
        exact ⟨.tail _ inside, passes⟩
    | false =>
      rw [List.filter_cons_of_neg (fun h => by rw [keep] at h; cases h)] at member
      obtain ⟨inside, passes⟩ := member_filter_inv test member
      exact ⟨.tail _ inside, passes⟩

theorem member_filter {α : Type} (test : α → Bool) {item : α} :
    ∀ {items : List α}, item ∈ items → test item = true → item ∈ items.filter test
  | [], member, _ => nomatch member
  | head :: rest, member, passes => by
    cases keep : test head with
    | true =>
      rw [List.filter_cons_of_pos keep]
      cases member with
      | head => exact .head _
      | tail _ later => exact .tail _ (member_filter test later passes)
    | false =>
      rw [List.filter_cons_of_neg (fun h => by rw [keep] at h; cases h)]
      cases member with
      | head => rw [keep] at passes; cases passes
      | tail _ later => exact member_filter test later passes

theorem member_upto_inv : ∀ {count index : Nat}, index ∈ upto count → index < count
  | 0, _, member => nomatch member
  | count + 1, index, member => by
    change index ∈ upto count ++ [count] at member
    cases member_append_inv member with
    | inl earlier => exact Nat.lt_trans (member_upto_inv earlier) (Nat.lt_succ_self count)
    | inr last =>
      cases last with
      | head => exact Nat.lt_succ_self count
      | tail _ none => nomatch none

theorem member_unknownStart {period phase : Nat} (inside : phase < period) (inversion : Bool) :
    (phase, inversion) ∈ unknownStart period := by
  cases inversion with
  | false =>
    exact member_append_left _
      (member_map (fun phase => (phase, false)) (member_upto period phase inside))
  | true =>
    exact member_append_right _
      (member_map (fun phase => (phase, true)) (member_upto period phase inside))

theorem member_unknownStart_inv {period : Nat} {candidate : Nat × Bool}
    (member : candidate ∈ unknownStart period) : candidate.1 < period := by
  cases member_append_inv member with
  | inl low =>
    obtain ⟨phase, inside, rfl⟩ := member_map_inv _ low
    exact member_upto_inv inside
  | inr high =>
    obtain ⟨phase, inside, rfl⟩ := member_map_inv _ high
    exact member_upto_inv inside

/-! ## 1. Fewer candidates never make settling harder -/

/-- One unfolding of the game, by definition. -/
theorem knows_step (pattern : List Bool) (period : Nat) (value : Bool) (commands : Nat)
    (belief : List (Nat × Bool)) :
    knowsWithin pattern period value (commands + 1) belief =
      (contactKnown pattern value belief ||
        knowsWithin pattern period value commands (advanceAll period belief) ||
        (knowsWithin pattern period value commands (belief.filter (readsAs pattern false)) &&
          knowsWithin pattern period value commands (belief.filter (readsAs pattern true)))) :=
  rfl

theorem contact_sub (pattern : List Bool) (value : Bool) (small large : List (Nat × Bool))
    (sub : ∀ candidate, candidate ∈ small → candidate ∈ large)
    (known : contactKnown pattern value large = true) :
    contactKnown pattern value small = true :=
  allOf_intro _ small fun candidate member =>
    allOf_member _ large candidate known (sub candidate member)

theorem advance_sub (period : Nat) (small large : List (Nat × Bool))
    (sub : ∀ candidate, candidate ∈ small → candidate ∈ large) :
    ∀ candidate, candidate ∈ advanceAll period small → candidate ∈ advanceAll period large := by
  intro candidate member
  obtain ⟨x, inside, rfl⟩ := member_map_inv _ member
  exact member_map _ (sub x inside)

theorem filter_sub (test : Nat × Bool → Bool) (small large : List (Nat × Bool))
    (sub : ∀ candidate, candidate ∈ small → candidate ∈ large) :
    ∀ candidate, candidate ∈ small.filter test → candidate ∈ large.filter test := by
  intro candidate member
  obtain ⟨inside, passes⟩ := member_filter_inv test member
  exact member_filter test (sub candidate inside) passes

/-- Settling on a belief settles on every sub-collection of it. -/
theorem knows_sub (pattern : List Bool) (period : Nat) (value : Bool) :
    ∀ (commands : Nat) (small large : List (Nat × Bool)),
      (∀ candidate, candidate ∈ small → candidate ∈ large) →
      knowsWithin pattern period value commands large = true →
        knowsWithin pattern period value commands small = true
  | 0, small, large, sub, known => contact_sub pattern value small large sub known
  | commands + 1, small, large, sub, known => by
    rw [knows_step] at known ⊢
    cases or_cases known with
    | inl early =>
      cases or_cases early with
      | inl now => exact or_left _ (or_left _ (contact_sub pattern value small large sub now))
      | inr moved =>
        exact or_left _ (or_right _ (knows_sub pattern period value commands _ _
          (advance_sub period small large sub) moved))
    | inr split =>
      obtain ⟨low, high⟩ := and_cases split
      exact or_right _ (and_both
        (knows_sub pattern period value commands _ _
          (filter_sub _ small large sub) low)
        (knows_sub pattern period value commands _ _
          (filter_sub _ small large sub) high))

/-! ## 2. Only what is read nearby matters -/

/-- The phase reached by a number of advances. -/
def iter (period : Nat) : Nat → Nat → Nat
  | 0, phase => phase
  | steps + 1, phase => iter period steps ((phase + 1) % period)

/-- Two candidates, one in each game, agree on inversion and on every contact
value met within `depth` advances. -/
def Related (pattern : List Bool) (period : Nat) (other : List Bool) (otherPeriod : Nat)
    (depth : Nat) (pair : (Nat × Bool) × (Nat × Bool)) : Prop :=
  pair.1.2 = pair.2.2 ∧ ∀ steps, steps ≤ depth →
    bitAt pattern (iter period steps pair.1.1) = bitAt other (iter otherPeriod steps pair.2.1)

theorem allOf_pairs {α β : Type} (left : α → Bool) (right : β → Bool) :
    ∀ (pairs : List (α × β)), (∀ pair, pair ∈ pairs → left pair.1 = right pair.2) →
      allOf (pairs.map Prod.fst) left = allOf (pairs.map Prod.snd) right
  | [], _ => rfl
  | head :: rest, same => by
    change (left head.1 && allOf (rest.map Prod.fst) left) =
      (right head.2 && allOf (rest.map Prod.snd) right)
    rw [same head (.head _), allOf_pairs left right rest
      (fun pair member => same pair (.tail _ member))]

def advancePair (period otherPeriod : Nat) (pair : (Nat × Bool) × (Nat × Bool)) :
    (Nat × Bool) × (Nat × Bool) :=
  (((pair.1.1 + 1) % period, pair.1.2), ((pair.2.1 + 1) % otherPeriod, pair.2.2))

theorem advance_fst (period otherPeriod : Nat) :
    ∀ (pairs : List ((Nat × Bool) × (Nat × Bool))),
      advanceAll period (pairs.map Prod.fst) =
        (pairs.map (advancePair period otherPeriod)).map Prod.fst
  | [] => rfl
  | head :: rest => by
    change _ :: advanceAll period (rest.map Prod.fst) = _ :: _
    rw [advance_fst period otherPeriod rest]
    rfl

theorem advance_snd (period otherPeriod : Nat) :
    ∀ (pairs : List ((Nat × Bool) × (Nat × Bool))),
      advanceAll otherPeriod (pairs.map Prod.snd) =
        (pairs.map (advancePair period otherPeriod)).map Prod.snd
  | [] => rfl
  | head :: rest => by
    change _ :: advanceAll otherPeriod (rest.map Prod.snd) = _ :: _
    rw [advance_snd period otherPeriod rest]
    rfl

theorem filter_map_comm {α β : Type} (f : α → β) (test : β → Bool) :
    ∀ (items : List α), (items.map f).filter test = (items.filter (fun x => test (f x))).map f
  | [] => rfl
  | head :: rest => by
    change (f head :: rest.map f).filter test = _
    cases keep : test (f head) with
    | true =>
      rw [List.filter_cons_of_pos keep, List.filter_cons_of_pos (p := fun x => test (f x)) keep,
        filter_map_comm f test rest]
      rfl
    | false =>
      have drop : ¬ test (f head) = true := fun h => by rw [keep] at h; cases h
      rw [List.filter_cons_of_neg drop, List.filter_cons_of_neg (p := fun x => test (f x)) drop,
        filter_map_comm f test rest]

theorem filter_congr {α : Type} (left right : α → Bool) :
    ∀ (items : List α), (∀ x, x ∈ items → left x = right x) →
      items.filter left = items.filter right
  | [], _ => rfl
  | head :: rest, same => by
    have rest' := filter_congr left right rest (fun x member => same x (.tail _ member))
    cases keep : right head with
    | true =>
      have keepLeft : left head = true := (same head (.head _)).trans keep
      rw [List.filter_cons_of_pos keepLeft, List.filter_cons_of_pos keep, rest']
    | false =>
      have dropLeft : ¬ left head = true := fun h => by
        rw [same head (.head _), keep] at h; cases h
      have drop : ¬ right head = true := fun h => by rw [keep] at h; cases h
      rw [List.filter_cons_of_neg dropLeft, List.filter_cons_of_neg drop, rest']

theorem related_reading (p : List Bool) (n : Nat) (u : List Bool) (N : Nat) (depth : Nat)
    (observed : Bool) (pair : (Nat × Bool) × (Nat × Bool))
    (related : Related p n u N depth pair) :
    readsAs p observed pair.1 = readsAs u observed pair.2 := by
  have bit : bitAt p pair.1.1 = bitAt u pair.2.1 := related.2 0 (Nat.zero_le _)
  unfold readsAs
  rw [related.1, bit]

/-- Paired beliefs are settled by exactly the same command counts. -/
theorem knows_transfer (p : List Bool) (n : Nat) (u : List Bool) (N : Nat) (value : Bool) :
    ∀ (depth : Nat) (pairs : List ((Nat × Bool) × (Nat × Bool))),
      (∀ pair, pair ∈ pairs → Related p n u N depth pair) →
      knowsWithin p n value depth (pairs.map Prod.fst) =
        knowsWithin u N value depth (pairs.map Prod.snd)
  | 0, pairs, related =>
    allOf_pairs _ _ pairs fun pair member => by
      have bit : bitAt p pair.1.1 = bitAt u pair.2.1 := (related pair member).2 0 (Nat.le_refl 0)
      rw [bit]
  | depth + 1, pairs, related => by
    rw [knows_step, knows_step]
    have now : contactKnown p value (pairs.map Prod.fst) =
        contactKnown u value (pairs.map Prod.snd) :=
      allOf_pairs _ _ pairs fun pair member => by
        have bit : bitAt p pair.1.1 = bitAt u pair.2.1 :=
          (related pair member).2 0 (Nat.zero_le _)
        rw [bit]
    have moved : knowsWithin p n value depth (advanceAll n (pairs.map Prod.fst)) =
        knowsWithin u N value depth (advanceAll N (pairs.map Prod.snd)) := by
      rw [advance_fst n N pairs, advance_snd n N pairs]
      apply knows_transfer p n u N value depth
      intro pair member
      obtain ⟨original, inside, rfl⟩ := member_map_inv _ member
      obtain ⟨same, bits⟩ := related original inside
      exact ⟨same, fun steps bound => bits (steps + 1) (Nat.succ_le_succ bound)⟩
    have split : ∀ observed,
        knowsWithin p n value depth ((pairs.map Prod.fst).filter (readsAs p observed)) =
          knowsWithin u N value depth ((pairs.map Prod.snd).filter (readsAs u observed)) := by
      intro observed
      rw [filter_map_comm, filter_map_comm,
        filter_congr (fun x => readsAs p observed x.1) (fun x => readsAs u observed x.2) pairs
          (fun pair member => related_reading p n u N (depth + 1) observed pair
            (related pair member))]
      apply knows_transfer p n u N value depth
      intro pair member
      obtain ⟨inside, _⟩ := member_filter_inv _ member
      obtain ⟨same, bits⟩ := related pair inside
      exact ⟨same, fun steps bound => bits steps (Nat.le_succ_of_le bound)⟩
    rw [now, moved, split false, split true]

/-! ## Arithmetic of the advance, without `propext` -/

theorem mod_of_lt : ∀ {x n : Nat}, x < n → x % n = x
  | 0, _, _ => rfl
  | x + 1, n, less => by
    show (if n ≤ x + 1 then Nat.modCore (x + 1) n else x + 1) = x + 1
    exact if_neg (Nat.not_le_of_lt less)

theorem modCore_go_step (y : Nat) (hy : 0 < y) (room x : Nat) (fits : x < room + 1) :
    Nat.modCore.go y hy (room + 1) x fits =
      if h : y ≤ x then Nat.modCore.go y hy room (x - y) (Nat.div_rec_fuel_lemma hy h fits)
      else x :=
  rfl

theorem modCore_go_bound (y : Nat) (hy : 0 < y) :
    ∀ (first second x : Nat) (firstFits : x < first) (secondFits : x < second),
      Nat.modCore.go y hy first x firstFits = Nat.modCore.go y hy second x secondFits
  | 0, _, _, firstFits, _ => absurd firstFits (Nat.not_lt_zero _)
  | _ + 1, 0, _, _, secondFits => absurd secondFits (Nat.not_lt_zero _)
  | first + 1, second + 1, x, firstFits, secondFits => by
    rw [modCore_go_step, modCore_go_step]
    by_cases reduces : y ≤ x
    · rw [dif_pos reduces, dif_pos reduces]
      exact modCore_go_bound y hy first second _ _ _
    · rw [dif_neg reduces, dif_neg reduces]

theorem modCore_unfold (x y : Nat) (hy : 0 < y) :
    Nat.modCore x y = Nat.modCore.go y hy (x + 1) x (Nat.lt_succ_self x) := by
  unfold Nat.modCore
  exact dif_pos hy

theorem modCore_small (x y : Nat) (hy : 0 < y) (small : x < y) : Nat.modCore x y = x := by
  rw [modCore_unfold x y hy, modCore_go_step]
  exact dif_neg (Nat.not_le_of_lt small)

theorem modCore_reduce (x y : Nat) (hy : 0 < y) (large : y ≤ x) :
    Nat.modCore x y = Nat.modCore (x - y) y := by
  rw [modCore_unfold x y hy, modCore_go_step, dif_pos large, modCore_unfold (x - y) y hy]
  exact modCore_go_bound y hy _ _ _ _ _

theorem modCore_is_mod (y : Nat) (hy : 0 < y) : ∀ x, Nat.modCore x y = x % y
  | 0 => modCore_small 0 y hy hy
  | x + 1 => by
    show Nat.modCore (x + 1) y = if y ≤ x + 1 then Nat.modCore (x + 1) y else x + 1
    by_cases large : y ≤ x + 1
    · rw [if_pos large]
    · rw [if_neg large]
      exact modCore_small (x + 1) y hy (Nat.lt_of_not_le large)

theorem add_sub_self : ∀ (a n : Nat), a + n - n = a
  | _, 0 => rfl
  | a, n + 1 => (Nat.succ_sub_succ (a + n) n).trans (add_sub_self a n)

/-- Adding the period does not change the phase. -/
theorem add_period_mod (a : Nat) : ∀ {n : Nat}, 0 < n → (a + n) % n = a % n
  | 0, positive => absurd positive (Nat.lt_irrefl 0)
  | m + 1, positive => by
    show (if m + 1 ≤ a + m + 1 then Nat.modCore (a + m + 1) (m + 1) else a + m + 1) = _
    rw [if_pos (Nat.succ_le_succ (Nat.le_add_left m a))]
    rw [modCore_reduce _ _ positive (Nat.succ_le_succ (Nat.le_add_left m a))]
    rw [show a + m + 1 - (m + 1) = a from add_sub_self a (m + 1)]
    exact modCore_is_mod (m + 1) positive a

theorem add_periods_mod (a n : Nat) (positive : 0 < n) : ∀ k, (a + k * n) % n = a % n
  | 0 => by rw [Nat.zero_mul, Nat.add_zero]
  | k + 1 => by
    rw [Nat.succ_mul, ← Nat.add_assoc, add_period_mod _ positive]
    exact add_periods_mod a n positive k

theorem succ_mod_mod (n : Nat) (positive : 0 < n) :
    ∀ (bound a : Nat), a < bound → (a % n + 1) % n = (a + 1) % n
  | 0, _, less => absurd less (Nat.not_lt_zero _)
  | bound + 1, a, less => by
    cases Nat.lt_or_ge a n with
    | inl small => rw [mod_of_lt small]
    | inr large =>
      have split : a - n + n = a := sub_add_cancel_constructive a n large
      have smaller : a - n < bound :=
        Nat.lt_of_lt_of_le (Nat.sub_lt (Nat.lt_of_lt_of_le positive large) positive)
          (Nat.le_of_lt_succ less)
      rw [← split, add_period_mod _ positive, Nat.add_right_comm (a - n) n 1,
        add_period_mod _ positive]
      exact succ_mod_mod n positive bound (a - n) smaller

theorem iter_mod (n : Nat) (positive : 0 < n) : ∀ (steps x : Nat), iter n steps (x % n) = (x + steps) % n
  | 0, _ => rfl
  | steps + 1, x => by
    show iter n steps ((x % n + 1) % n) = _
    rw [succ_mod_mod n positive (x + 1) x (Nat.lt_succ_self x), iter_mod n positive steps (x + 1),
      Nat.add_assoc, Nat.add_comm 1 steps]

theorem iter_formula (n : Nat) (positive : 0 < n) (steps x : Nat) (inside : x < n) :
    iter n steps x = (x + steps) % n := by
  have same := iter_mod n positive steps x
  rw [mod_of_lt inside] at same
  exact same

theorem iter_add (n : Nat) : ∀ (first second x : Nat),
    iter n (first + second) x = iter n second (iter n first x)
  | 0, second, x => by rw [Nat.zero_add]; rfl
  | first + 1, second, x => by
    rw [Nat.succ_add]
    exact iter_add n first second ((x + 1) % n)

theorem iter_lt (n : Nat) : ∀ (steps x : Nat), x < n → iter n steps x < n
  | 0, _, inside => inside
  | steps + 1, x, inside =>
    iter_lt n steps ((x + 1) % n) (Nat.mod_lt _ (Nat.lt_of_le_of_lt (Nat.zero_le x) inside))

/-! ## 3. A local stretch of the cycle -/

/-- Contact values read forward from a phase, one per advance. -/
def walk (pattern : List Bool) (period : Nat) : Nat → Nat → List Bool
  | 0, _ => []
  | length + 1, phase => bitAt pattern phase :: walk pattern period length ((phase + 1) % period)

theorem walk_length (pattern : List Bool) (period : Nat) :
    ∀ (length phase : Nat), (walk pattern period length phase).length = length
  | 0, _ => rfl
  | length + 1, phase => by
    change (walk pattern period length ((phase + 1) % period)).length + 1 = length + 1
    rw [walk_length pattern period length]

theorem bitAt_walk (pattern : List Bool) (period : Nat) :
    ∀ (length index phase : Nat), index < length →
      bitAt (walk pattern period length phase) index = bitAt pattern (iter period index phase)
  | 0, _, _, less => absurd less (Nat.not_lt_zero _)
  | _ + 1, 0, _, _ => rfl
  | length + 1, index + 1, phase, less =>
    bitAt_walk pattern period length index ((phase + 1) % period) (Nat.lt_of_succ_lt_succ less)

end Generative.InquirySufficiency.PhasePeriodUniversal

#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.or_cases
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.and_cases
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.or_left
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.or_right
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.and_both
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.allOf_intro
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.allOf_witness
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.member_map_inv
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.member_append_inv
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.member_filter_inv
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.member_filter
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.member_upto_inv
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.member_unknownStart
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.member_unknownStart_inv
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.knows_step
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.contact_sub
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.advance_sub
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.filter_sub
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.knows_sub
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.iter
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.Related
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.allOf_pairs
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.advancePair
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.advance_fst
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.advance_snd
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.filter_map_comm
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.filter_congr
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.related_reading
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.knows_transfer
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.mod_of_lt
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.modCore_go_step
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.modCore_go_bound
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.modCore_unfold
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.modCore_small
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.modCore_reduce
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.modCore_is_mod
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.add_sub_self
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.add_period_mod
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.add_periods_mod
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.succ_mod_mod
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.iter_mod
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.iter_formula
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.iter_add
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.iter_lt
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.walk
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.walk_length
#print axioms Generative.InquirySufficiency.PhasePeriodUniversal.bitAt_walk
