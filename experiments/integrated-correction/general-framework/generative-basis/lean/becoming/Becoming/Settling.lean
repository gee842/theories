import Becoming.Enough
import Becoming.Change

/-!
# Settling: when the runs of a process stop changing

`Becoming.Enough` splits assured enough into two parts: every reachable configuration with a step
that stays meets the target, and every run settles (`Enough.assured_iff`). The second part does
not mention the target. This module states when the runs of a process keep changing and when they
settle, with no premise beyond what each theorem names.

* **A change within a loop keeps recurring.** A run changes within a loop where its configuration
  at `i` is its configuration at `i + (p + 1)` and it changes between them. Such a run gives a run
  from the same configuration that follows it to the loop and then goes round it again and again,
  so that its change recurs at arbitrarily late steps (`Settling.recurs_of_loop`), and a run whose
  change recurs does not settle (`Settling.not_settles_of_recurs`).
* **Within finitely many configurations, recurring change is a change within a loop.** Along a run
  a list holds, a change that recurs is a change within a loop (`Settling.loop_of_recurs`): among
  more changing steps than the list is long, two are at one configuration.
* **Exactly, on the process.** A change within a loop is a reachable step to another
  configuration from which the first can be reached again (`Settling.undoable_of_loop`), and such a
  step gives a run that keeps changing (`Settling.recurs_of_undoable`). So in a world a list holds, some
  run from a configuration keeps changing exactly where some run from it changes within a loop
  (`Settling.keeps_changing_iff_loop`), exactly where a configuration reachable from it has a step
  to another configuration from which it can be reached again (`Settling.keeps_changing_iff`).
  Where every run from a configuration settles, and so where assured enough holds, no reachable
  step to another configuration can be undone (`Settling.settles_no_undoable`,
  `Settling.assured_no_undoable`).
* **Not changing for ever is not settling.** In `Settling.OneWay`, two configurations with no step
  from the second back to the first, no run keeps changing (`Settling.OneWay.never_keeps_changing`),
  and every run from the first configuration settling is the limited principle of omniscience
  (`Settling.OneWay.lpo_of_settles`): a run that changes once, at the first `true` of a sequence,
  settles at a step only if it can be said by then whether the sequence has a `true`.

So in a world a list holds, whether some run of a process keeps changing is a property of the
process: a reachable change that can be undone. That no run keeps changing does not give a step from which each run is
settled; that needs, already in a process of two configurations, the limited principle of
omniscience, which the core does not assume. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

open Generative

universe u v

namespace Settling

section AnyProcess

variable {S : Type u} {A : Type v} {P : Process S A}

/-- The run keeps changing: at arbitrarily late steps its configuration changes across a step. -/
def ChangeRecurs (r : Run P) : Prop := ∀ T, ∃ k, T ≤ k ∧ r.state (k + 1) ≠ r.state k

/-- The run changes within a loop: its configuration at `i` is its configuration at
`i + (p + 1)`, and at `i + c`, with `c ≤ p`, it changes across a step. -/
def ChangesInLoop (r : Run P) : Prop :=
  ∃ i p c, r.state (i + (p + 1)) = r.state i ∧ c ≤ p ∧ r.state (i + c + 1) ≠ r.state (i + c)

/-- **A run that keeps changing does not settle.** -/
theorem not_settles_of_recurs {r : Run P} (recurs : ChangeRecurs r) : ¬ Enough.Settles r :=
  fun ⟨T, stays⟩ => match recurs T with
    | ⟨k, late, changes⟩ => changes (stays k late)

/-! ### Going round a loop -/

/-- The index that runs from `0` to `i + p` and then from `i` to `i + p` again and again. -/
def roundIndex (i p : Nat) : Nat → Nat
  | 0 => 0
  | n + 1 => if roundIndex i p n < i + p then roundIndex i p n + 1 else i

theorem roundIndex_lt {i p n : Nat} (lt : roundIndex i p n < i + p) :
    roundIndex i p (n + 1) = roundIndex i p n + 1 :=
  if_pos lt

theorem roundIndex_last {i p n : Nat} (last : ¬ roundIndex i p n < i + p) :
    roundIndex i p (n + 1) = i :=
  if_neg last

theorem roundIndex_le (i p : Nat) : ∀ n, roundIndex i p n ≤ i + p
  | 0 => Nat.zero_le _
  | n + 1 =>
    match Decidable.em (roundIndex i p n < i + p) with
    | .inl lt => Eq.subst (motive := fun x => x ≤ i + p) (roundIndex_lt lt).symm (Nat.succ_le_of_lt lt)
    | .inr last => Eq.subst (motive := fun x => x ≤ i + p) (roundIndex_last last).symm
        (Nat.le_add_right i p)

/-- From `e` steps before the end of the loop, the index is back at `i` one step after it. -/
theorem roundIndex_back {i p : Nat} : ∀ e n, roundIndex i p n + e = i + p →
    roundIndex i p (n + (e + 1)) = i
  | 0, _, at_last => roundIndex_last fun lt =>
      Nat.lt_irrefl _ (Eq.subst (motive := fun x => x < i + p) at_last lt)
  | e + 1, n, before =>
    have lt : roundIndex i p n < i + p :=
      Nat.lt_of_lt_of_le (Nat.lt_succ_self _)
        (Nat.le_trans (Nat.add_le_add_left (Nat.succ_le_succ (Nat.zero_le e)) _) (Nat.le_of_eq before))
    have next : roundIndex i p (n + 1) + e = i + p :=
      (congrArg (· + e) (roundIndex_lt lt)).trans ((Nat.succ_add _ e).trans before)
    (congrArg (roundIndex i p) (Nat.succ_add n (e + 1))).symm.trans (roundIndex_back e (n + 1) next)

/-- From `i`, the index is at `i + c` after `c` steps, for `c ≤ p`. -/
theorem roundIndex_from {i p : Nat} : ∀ c n, c ≤ p → roundIndex i p n = i →
    roundIndex i p (n + c) = i + c
  | 0, _, _, at_i => at_i
  | c + 1, n, le, at_i =>
    have here : roundIndex i p (n + c) = i + c := roundIndex_from c n (Nat.le_of_succ_le le) at_i
    have lt : roundIndex i p (n + c) < i + p :=
      Eq.subst (motive := fun x => x < i + p) here.symm (Nat.add_lt_add_left (Nat.lt_of_succ_le le) i)
    (roundIndex_lt lt).trans (congrArg (· + 1) here)

/-- From every step on, the index is at `i + c` at some step, for `c ≤ p`. -/
theorem roundIndex_hits {i p c : Nat} (le : c ≤ p) (T : Nat) :
    ∃ n, T ≤ n ∧ roundIndex i p n = i + c :=
  match le_dest (roundIndex_le i p T) with
  | ⟨e, gap⟩ => ⟨T + (e + 1) + c, Nat.le_trans (Nat.le_add_right T (e + 1)) (Nat.le_add_right _ c),
      roundIndex_from c _ le (roundIndex_back e T gap.symm)⟩

/-- The run along configurations `g` and actions `h`, admissible up to the end of a loop at
`i + p` that closes at `i`, going round the loop again and again. -/
def round (g : Nat → S) (h : Nat → A) {i p : Nat}
    (steps : ∀ k, k ≤ i + p → P.step (g k) (h k) (g (k + 1))) (back : g (i + (p + 1)) = g i) :
    Run P :=
  ⟨fun n => g (roundIndex i p n), fun n => h (roundIndex i p n), fun n =>
    match Decidable.em (roundIndex i p n < i + p) with
    | .inl lt => Eq.subst (motive := fun k => P.step (g (roundIndex i p n)) (h (roundIndex i p n)) (g k))
        (roundIndex_lt lt).symm (steps _ (Nat.le_of_lt lt))
    | .inr last =>
      have at_last : roundIndex i p n = i + p := Nat.le_antisymm (roundIndex_le i p n) (Nat.ge_of_not_lt last)
      Eq.subst (motive := fun y => P.step (g (roundIndex i p n)) (h (roundIndex i p n)) y)
        ((congrArg (fun x => g (x + 1)) at_last).trans (back.trans (congrArg g (roundIndex_last last)).symm))
        (steps _ (roundIndex_le i p n))⟩

/-- **Going round a loop with a change in it, the change recurs.** -/
theorem round_recurs {g : Nat → S} {h : Nat → A} {i p c : Nat}
    (steps : ∀ k, k ≤ i + p → P.step (g k) (h k) (g (k + 1))) (back : g (i + (p + 1)) = g i)
    (le : c ≤ p) (changes : g (i + c + 1) ≠ g (i + c)) : ChangeRecurs (round g h steps back) :=
  fun T => match roundIndex_hits (i := i) le T with
    | ⟨n, late, at_c⟩ => ⟨n, late, fun same =>
      match Decidable.em (c < p) with
      | .inl lt =>
        have next : roundIndex i p (n + 1) = i + c + 1 :=
          (roundIndex_lt (Eq.subst (motive := fun x => x < i + p) at_c.symm
            (Nat.add_lt_add_left lt i))).trans (congrArg (· + 1) at_c)
        changes ((congrArg g next).symm.trans (same.trans (congrArg g at_c)))
      | .inr not_lt =>
        have eq : c = p := Nat.le_antisymm le (Nat.ge_of_not_lt not_lt)
        have at_p : roundIndex i p n = i + p := at_c.trans (congrArg (i + ·) eq)
        have next : roundIndex i p (n + 1) = i := roundIndex_last fun lt =>
          Nat.lt_irrefl _ (Eq.subst (motive := fun x => x < i + p) at_p lt)
        changes (((congrArg (fun x => g (i + x + 1)) eq).trans back).trans
          ((congrArg g next).symm.trans (same.trans (congrArg g at_c))))⟩

/-- **A change within a loop keeps recurring.** A run that changes within a loop gives a run from
the same configuration whose change recurs: it follows the run to the end of the loop and goes
round it again and again. -/
theorem recurs_of_loop {r : Run P} (loop : ChangesInLoop r) :
    ∃ r' : Run P, r'.state 0 = r.state 0 ∧ ChangeRecurs r' :=
  match loop with
  | ⟨_, _, _, back, le, changes⟩ =>
    ⟨round r.state r.act (fun k _ => r.step k) back, rfl, round_recurs _ back le changes⟩

/-! ### Within finitely many configurations -/

/-- A sequence of positions kept up to `m` and `k` after it. -/
def extend (f : Nat → Nat) (m k : Nat) (n : Nat) : Nat := if n ≤ m then f n else k

theorem extend_le {f : Nat → Nat} {m k n : Nat} (le : n ≤ m) : extend f m k n = f n := if_pos le

theorem extend_gt {f : Nat → Nat} {m k n : Nat} (gt : ¬ n ≤ m) : extend f m k n = k := if_neg gt

/-- Rising at each step up to `m`, positions rise between any two up to `m`. -/
theorem rising {f : Nat → Nat} {m : Nat} (inc : ∀ n, n < m → f n < f (n + 1)) :
    ∀ i j, i < j → j ≤ m → f i < f j
  | _, 0, lt, _ => absurd lt (Nat.not_lt_zero _)
  | i, j + 1, lt, le =>
    match Decidable.em (i < j) with
    | .inl lt' => Nat.lt_trans (rising inc i j lt' (Nat.le_of_succ_le le)) (inc j le)
    | .inr nlt => Eq.subst (motive := fun x => f x < f (j + 1))
        (Nat.le_antisymm (Nat.ge_of_not_lt nlt) (Nat.le_of_lt_succ lt)) (inc j le)

/-- Where change recurs, there are rising positions of `m + 1` changes, for every `m`. -/
theorem changes_at {r : Run P} (recurs : ChangeRecurs r) : ∀ m, ∃ f : Nat → Nat,
    (∀ n, n < m → f n < f (n + 1)) ∧ ∀ n, n ≤ m → r.state (f n + 1) ≠ r.state (f n)
  | 0 => match recurs 0 with
    | ⟨k, _, changes⟩ => ⟨fun _ => k, fun _ lt => absurd lt (Nat.not_lt_zero _), fun _ _ => changes⟩
  | m + 1 => match changes_at recurs m with
    | ⟨f, inc, ch⟩ => match recurs (f m + 1) with
      | ⟨k, late, changes⟩ => ⟨extend f m k,
        fun n lt => match Decidable.em (n < m) with
          | .inl lt' => Eq.subst (motive := fun x => x < extend f m k (n + 1)) (extend_le (Nat.le_of_lt lt')).symm
              (Eq.subst (motive := fun y => f n < y) (extend_le (Nat.succ_le_of_lt lt')).symm (inc n lt'))
          | .inr nlt =>
            have at_m : m = n := Nat.le_antisymm (Nat.ge_of_not_lt nlt) (Nat.le_of_lt_succ lt)
            Eq.subst (motive := fun x => extend f m k x < extend f m k (x + 1)) at_m
              (Eq.subst (motive := fun x => x < extend f m k (m + 1)) (extend_le (Nat.le_refl m)).symm
                (Eq.subst (motive := fun y => f m < y) (extend_gt (Nat.not_succ_le_self m)).symm late)),
        fun n _ => match Decidable.em (n ≤ m) with
          | .inl le => Eq.subst (motive := fun x => r.state (x + 1) ≠ r.state x) (extend_le le).symm (ch n le)
          | .inr gt => Eq.subst (motive := fun x => r.state (x + 1) ≠ r.state x) (extend_gt gt).symm changes⟩

/-- **Within finitely many configurations, recurring change is a change within a loop.** Along a
run whose configurations a list holds, a change that recurs is a change within a loop: among more
changing steps than the list is long, two are at one configuration. -/
theorem loop_of_recurs {r : Run P} {l : List S} (held : ∀ n, r.state n ∈ l) (recurs : ChangeRecurs r) :
    ChangesInLoop r :=
  match changes_at recurs l.length with
  | ⟨f, inc, ch⟩ =>
    match revisits_within l (fun n => r.state (f n)) (fun n _ => held (f n)) with
    | ⟨i, j, lt, le, same⟩ =>
      match gap_of_lt (rising inc i j lt le) with
      | ⟨d, gap⟩ => ⟨f i, d, 0, (congrArg r.state gap).symm.trans same.symm, Nat.zero_le d,
          ch i (Nat.le_trans (Nat.le_of_lt lt) le)⟩

/-! ### On the process -/

/-- **A change within a loop is a reachable step that can be undone.** Where a run changes within
a loop, a configuration reachable from where it begins has a step to another configuration from
which it can be reached again. -/
theorem undoable_of_loop {r : Run P} (loop : ChangesInLoop r) :
    ∃ x a y, Reach P (r.state 0) x ∧ P.step x a y ∧ y ≠ x ∧ Reach P y x :=
  match loop with
  | ⟨i, p, c, back, le, changes⟩ =>
    match le_dest le with
    | ⟨e, gap⟩ =>
      have ends : i + c + 1 + e = i + (p + 1) :=
        (Nat.add_right_comm (i + c) 1 e).trans
          (congrArg (· + 1) ((Nat.add_assoc i c e).trans (congrArg (i + ·) gap.symm)))
      ⟨r.state (i + c), r.act (i + c), r.state (i + c + 1),
       Eq.subst (motive := fun k => Reach P (r.state 0) (r.state k)) (Nat.zero_add (i + c)) (r.reach 0 (i + c)),
       r.step (i + c), changes,
       Reach.trans
         (Eq.subst (motive := fun k => Reach P (r.state (i + c + 1)) (r.state k)) (ends.trans rfl)
           (r.reach (i + c + 1) e))
         (Eq.subst (motive := fun x => Reach P x (r.state (i + c))) back.symm (r.reach i c))⟩

/-- A path prefixed by a step. -/
def consSeq {α : Type u} (x : α) (g : Nat → α) : Nat → α
  | 0 => x
  | k + 1 => g k

/-- A finite path prefixed to configurations and actions admissible for `N` steps. -/
theorem path_then {x y : S} {as : List A} (path : Trace P x as y) {N : Nat} {g : Nat → S}
    {h : Nat → A} (start : g 0 = y) (steps : ∀ k, k < N → P.step (g k) (h k) (g (k + 1))) :
    ∃ g' : Nat → S, ∃ h' : Nat → A, g' 0 = x ∧ (∀ k, g' (as.length + k) = g k) ∧
      ∀ k, k < as.length + N → P.step (g' k) (h' k) (g' (k + 1)) := by
  induction path with
  | nil _ => exact ⟨g, h, start, fun k => congrArg g (Nat.zero_add k), fun k lt =>
      steps k (Eq.subst (motive := fun n => k < n) (Nat.zero_add N) lt)⟩
  | @cons s m _ a bs step _ ih =>
    exact match ih start with
    | ⟨g', h', start', along, steps'⟩ => ⟨consSeq s g', consAct a h', rfl,
        fun k => (congrArg (consSeq s g') (Nat.succ_add bs.length k)).trans (along k), fun
        | 0, _ => Eq.subst (motive := fun z => P.step s a z) start'.symm step
        | k + 1, lt => steps' k (Nat.lt_of_succ_lt_succ
            (Eq.subst (motive := fun n => k + 1 < n) (Nat.succ_add bs.length N) lt))⟩

/-- **A reachable step that can be undone gives a run that keeps changing.** Where a
configuration reachable from `s` has a step to another configuration from which it can be reached
again, some run from `s` keeps changing: it goes to the configuration and round the way back again
and again. -/
theorem recurs_of_undoable {s x y : S} {a : A} (reach : Reach P s x) (step : P.step x a y)
    (moves : y ≠ x) (undo : Reach P y x) :
    ∃ r : Run P, r.state 0 = s ∧ ChangeRecurs r :=
  match reach, undo with
  | ⟨as, path⟩, ⟨bs, back⟩ =>
    match Branching.trace_positions a back with
    | ⟨g, h, start, finish, steps⟩ =>
      have steps₁ : ∀ k, k < bs.length + 1 →
          P.step (consSeq x g k) (consAct a h k) (consSeq x g (k + 1)) := fun
        | 0, _ => Eq.subst (motive := fun z => P.step x a z) start.symm step
        | k + 1, lt => steps k (Nat.lt_of_succ_lt_succ lt)
      match path_then path (g := consSeq x g) rfl steps₁ with
      | ⟨g', h', start', along, steps'⟩ =>
        have closes : g' (as.length + (bs.length + 1)) = g' as.length :=
          (along _).trans (finish.trans (along 0).symm)
        have changes : g' (as.length + 0 + 1) ≠ g' (as.length + 0) := fun same =>
          moves (start.symm.trans ((along 1).symm.trans (same.trans (along 0))))
        ⟨round g' h' (fun k le => steps' k (Nat.lt_succ_of_le le)) closes, start',
          round_recurs _ closes (Nat.zero_le _) changes⟩

end AnyProcess

/-! ### Exactly, in a world a list holds -/

section Exactly

variable {S : Type u} {A : Type v} {P : Process S A}

/-- **Keeping changing is changing within a loop.** In a world a list holds, some run from `s`
keeps changing exactly where some run from `s` changes within a loop. The second direction needs
no list. -/
theorem keeps_changing_iff_loop {s : S} {l : List S} (world : ∀ x, x ∈ l) :
    (∃ r : Run P, r.state 0 = s ∧ ChangeRecurs r) ↔ ∃ r : Run P, r.state 0 = s ∧ ChangesInLoop r :=
  ⟨fun ⟨r, start, recurs⟩ => ⟨r, start, loop_of_recurs (fun _ => world _) recurs⟩,
   fun ⟨_, start, loop⟩ => match recurs_of_loop loop with
    | ⟨r', start', recurs⟩ => ⟨r', start'.trans start, recurs⟩⟩

/-- **Keeping changing is a reachable change that can be undone.** In a world a list holds, some
run from `s` keeps changing exactly where a configuration reachable from `s` has a step to another
configuration from which it can be reached again. The second direction needs no list. -/
theorem keeps_changing_iff {s : S} {l : List S} (world : ∀ x, x ∈ l) :
    (∃ r : Run P, r.state 0 = s ∧ ChangeRecurs r) ↔
      ∃ x a y, Reach P s x ∧ P.step x a y ∧ y ≠ x ∧ Reach P y x :=
  ⟨fun ⟨_, start, recurs⟩ =>
    Eq.subst (motive := fun z => ∃ x a y, Reach P z x ∧ P.step x a y ∧ y ≠ x ∧ Reach P y x)
      start (undoable_of_loop (loop_of_recurs (fun _ => world _) recurs)),
   fun ⟨_, _, _, reach, step, moves, undo⟩ => recurs_of_undoable reach step moves undo⟩

/-- **Where every run settles, no reachable change can be undone.** Where every run from `s`
settles, no configuration reachable from `s` has a step to another configuration from which it can
be reached again. No list is needed. -/
theorem settles_no_undoable {s : S} (settle : ∀ r : Run P, r.state 0 = s → Enough.Settles r) :
    ¬ ∃ x a y, Reach P s x ∧ P.step x a y ∧ y ≠ x ∧ Reach P y x :=
  fun ⟨_, _, _, reach, step, moves, undo⟩ =>
    match recurs_of_undoable reach step moves undo with
    | ⟨r, start, recurs⟩ => not_settles_of_recurs recurs (settle r start)

/-- **Where assured enough holds, no reachable change can be undone.** Where every run from `s`
comes to rest with its target met, no configuration reachable from `s` has a step to another
configuration from which it can be reached again. -/
theorem assured_no_undoable {s : S} {target : S → Prop}
    (assured : ∀ r : Run P, r.state 0 = s → Enough.Rests target r) :
    ¬ ∃ x a y, Reach P s x ∧ P.step x a y ∧ y ≠ x ∧ Reach P y x :=
  settles_no_undoable (Enough.assured_iff.mp assured).2

end Exactly

/-! ## Not changing for ever is not settling -/

namespace OneWay

/-- Two configurations; from `true` every step stays at `true`. -/
def process : Process Bool Unit := ⟨fun x _ y => x = true → y = true⟩

/-- Whether a sequence has had a `true` before `n`. -/
def seen (f : Nat → Bool) : Nat → Bool
  | 0 => false
  | n + 1 => seen f n || f n

/-- The run that changes once, at the first `true` of `f`. -/
def run (f : Nat → Bool) : Run process :=
  ⟨seen f, fun _ => (), fun n before => Eq.subst (motive := fun b => (b || f n) = true) before.symm rfl⟩

theorem seen_stays (f : Nat → Bool) {m : Nat} (yes : seen f m = true) : ∀ k, seen f (m + k) = true
  | 0 => yes
  | k + 1 => (run f).step (m + k) (seen_stays f yes k)

theorem seen_witness (f : Nat → Bool) : ∀ n, seen f n = true → ∃ k, f k = true
  | 0, yes => Bool.noConfusion yes
  | n + 1, yes =>
    match hf : f n with
    | true => ⟨n, hf⟩
    | false => seen_witness f n ((Bool.or_false _).symm.trans
        (Eq.subst (motive := fun b => (seen f n || b) = true) hf yes))

/-- No configuration has a step to another configuration from which it can be reached again: from
`true` every step stays, and from `true` `false` cannot be reached. -/
theorem no_undoable : ¬ ∃ x a y, Reach process x x ∧ process.step x a y ∧ y ≠ x ∧ Reach process y x
  | ⟨x, _, y, _, step, moves, undo⟩ =>
    match x, y with
    | true, true => moves rfl
    | false, false => moves rfl
    | true, false => Bool.noConfusion (step rfl)
    | false, true => Bool.noConfusion
        (Invariant.reach (P := process) (I := fun z => z = true) (fun _ _ _ step held => step held) undo rfl)

/-- **No run keeps changing.** -/
theorem never_keeps_changing (s : Bool) : ¬ ∃ r : Run process, r.state 0 = s ∧ ChangeRecurs r :=
  fun keeps => match (keeps_changing_iff (l := [false, true])
      (fun x => match x with
        | false => List.Mem.head _
        | true => List.Mem.tail _ (List.Mem.head _))).mp keeps with
    | ⟨x, a, y, _, step, moves, undo⟩ => no_undoable ⟨x, a, y, Reach.refl process x, step, moves, undo⟩

/-- **Every run from `false` settling is the limited principle of omniscience.** -/
theorem lpo_of_settles (settle : ∀ r : Run process, r.state 0 = false → Enough.Settles r) : LPO :=
  fun f => match settle (run f) rfl with
    | ⟨T, stays⟩ =>
      match hT : seen f T with
      | true => .inl (seen_witness f T hT)
      | false => .inr fun k =>
        have later : seen f (k + 1) = false :=
          match Decidable.em (k + 1 ≤ T) with
          | .inl le =>
            match hk : seen f (k + 1) with
            | false => rfl
            | true => match le_dest le with
              | ⟨e, gap⟩ => Bool.noConfusion (((congrArg (seen f) gap).trans (seen_stays f hk e)).symm.trans hT)
          | .inr gt => match le_dest (Nat.le_of_lt (Nat.gt_of_not_le gt)) with
            | ⟨d, gap⟩ => (congrArg (seen f) gap).trans
                ((Enough.settled_at (r := run f) stays d).trans hT)
        match hf : f k with
        | false => rfl
        | true => Bool.noConfusion ((Bool.or_true _).symm.trans
            (Eq.subst (motive := fun b => (seen f k || b) = false) hf later))

end OneWay

end Settling

end Becoming
