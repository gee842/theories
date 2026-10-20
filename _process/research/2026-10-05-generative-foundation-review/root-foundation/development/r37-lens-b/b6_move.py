#!/usr/bin/env python3
"""R37 B6, stage 1: the definition twins and the copies resting on them, each stated once.

usage: python3 -B b6_move.py            (moves; writes b6-removals.json for R32's remove.py)

1. Cuts these declarations from their modules and states them again, under the same full name:
   * in `Becoming.Prelude` (they read nothing but Lean's types): `Distinct` (Population; now in every
     universe, as `CrossSituational.Distinct` was), `total` (World), `steps` (Flow), `nonzero`
     (Weighted), `Undecided.upto`, `DistinctUnder` (Refinement), `Copying.nth`, `Settling.consAct`,
     `Law.memberAt` (Identification), and the statements on them kept from the copy groups:
     `not_mem_of_middle` (Listing), `distinct_append` (OneStep; now in every universe, as
     `SituationTraces.distinct_append` was), `distinct_map_on` (Counting), `total_steps_succ`
     (OneStep), `total_steps_add` (Stuttering), `between_of_mem_steps` (Sampling),
     `RouteTraces.nonzero_of_le`;
   * `Flow.excess_zero_of_le` (Entropy) in `Becoming.Change`, beside `excess`, with OneStep's direct
     proof; `Situations.sum_one` in `Becoming.Weighted`, beside `counting`; `Shuttle.next_off`
     (Persistence) in `Becoming.Roles`, beside the shuttle.
2. Makes three witnesses one-line instances: `Hexagram.nth` and `OneStep.Witness.pick` read
   `Law.memberAt` with their default, `Race.present` is `Exceeding.present`.
3. Writes the removal table: each twin and copy with the name it takes (`remove.py` cuts them and
   points their uses there)."""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / 'r31-support'))
import decltext  # noqa: E402

B = decltext.dups.ROOT

PRELUDE_MOVED = ['Becoming.Distinct', 'Becoming.total', 'Becoming.steps', 'Becoming.nonzero',
                 'Becoming.Undecided.upto', 'Becoming.DistinctUnder', 'Becoming.Copying.nth',
                 'Becoming.Settling.consAct', 'Becoming.Law.memberAt', 'Becoming.not_mem_of_middle',
                 'Becoming.distinct_append', 'Becoming.distinct_map_on', 'Becoming.total_steps_succ',
                 'Becoming.total_steps_add', 'Becoming.between_of_mem_steps',
                 'Becoming.RouteTraces.nonzero_of_le']
OTHER_MOVED = ['Becoming.Flow.excess_zero_of_le', 'Becoming.Situations.sum_one', 'Becoming.Shuttle.next_off']

PRELUDE_BLOCK = '''
/-! ## Definitions stated once (R37)

Each of these was defined with the same body in two or more modules of the run, or is a definition
the statements stated once below name; it is stated here once, under the name kept (twentieth
review, B6). `Distinct` and `distinct_append` are stated in every universe, as the copies they
replace (`CrossSituational.Distinct`, `SituationTraces.distinct_append`) were. -/

section Once

variable {α : Type u} {β : Type v}

/-- A list in which no member occurs twice. -/
def Distinct : List α → Prop
  | [] => True
  | a :: as => ¬ a ∈ as ∧ Distinct as

/-- Two lists without repetition and with no member in common join without repetition. -/
theorem distinct_append : ∀ {l m : List α}, Distinct l → Distinct m →
    (∀ a, a ∈ l → ¬ a ∈ m) → Distinct (l ++ m)
  | [], _, _, distinct, _ => distinct
  | a :: l, _, ⟨fresh, distinctL⟩, distinctM, apart =>
    ⟨fun mem => match ListTests.mem_append_iff.mp mem with
      | .inl inside => fresh inside
      | .inr outside => apart a (.head l) outside,
     distinct_append distinctL distinctM fun b mem => apart b (.tail a mem)⟩

/-- Members of a list pairwise apart under a relation: no member is related to a later one. -/
def DistinctUnder (R : α → α → Prop) : List α → Prop
  | [] => True
  | x :: s => (∀ y, y ∈ s → ¬ R x y) ∧ DistinctUnder R s

namespace Copying

/-- The member at index `i`, if any. -/
def nth : List β → Nat → Option β
  | [], _ => none
  | x :: _, 0 => some x
  | _ :: xs, i + 1 => nth xs i

end Copying

namespace Law

/-- The member at index `i`, `d` past the end. -/
def memberAt (d : α) : List α → Nat → α
  | [], _ => d
  | x :: _, 0 => x
  | _ :: r, i + 1 => memberAt d r i

end Law

namespace Settling

/-- The sequence that starts with `a` and continues as `h`. -/
def consAct (a : α) (h : Nat → α) : Nat → α
  | 0 => a
  | k + 1 => h k

end Settling

end Once

/-- The total of a quantity over a finite list. -/
def total {α : Type} : List α → (α → Nat) → Nat
  | [], _ => 0
  | a :: as, q => q a + total as q

/-- The steps `T`, `T + 1`, …, `T + N - 1`. -/
def steps : Nat → Nat → List Nat
  | _, 0 => []
  | T, N + 1 => T :: steps (T + 1) N

/-- Whether a count is not zero. -/
def nonzero : Nat → Bool
  | 0 => false
  | _ + 1 => true

namespace Undecided

/-- The numbers below `n`, from `n - 1` down. -/
def upto : Nat → List Nat
  | 0 => []
  | n + 1 => n :: upto n

end Undecided

section OnceLists

variable {α β : Type}

/-- In a list without repetition, a member standing in the middle stands nowhere else. -/
theorem not_mem_of_middle {a : α} : ∀ {p q : List α}, Distinct (p ++ a :: q) → ¬ a ∈ p ++ q
  | [], _, ⟨fresh, _⟩, mem => fresh mem
  | _ :: p, q, ⟨fresh, distinct⟩, mem => match mem_cons_cases mem with
    | .inl ax => fresh (Eq.subst (motive := fun y => y ∈ p ++ a :: q) ax (mem_middle p))
    | .inr mem => not_mem_of_middle distinct mem

/-- Mapping a list one to one on its members keeps it without repetition. -/
theorem distinct_map_on {β : Type} {g : α → β} :
    ∀ {l : List α}, (∀ a b, a ∈ l → b ∈ l → g a = g b → a = b) → Distinct l →
      Distinct (l.map g)
  | [], _, _ => trivial
  | a :: l, inj, ⟨fresh, distinct⟩ =>
    ⟨fun mem => match preimage_of_mem_map mem with
      | ⟨b, listed, same⟩ => fresh (Eq.subst (motive := (· ∈ l))
          (inj b a (.tail a listed) (.head l) same) listed),
     distinct_map_on (fun x y first second => inj x y (.tail a first) (.tail a second))
       distinct⟩

end OnceLists

/-- Shifting a stretch of steps by one is shifting the quantity. -/
theorem total_steps_succ (q : Nat → Nat) :
    ∀ T n, total (steps (T + 1) n) q = total (steps T n) fun i => q (i + 1)
  | _, 0 => rfl
  | T, n + 1 => congrArg (q (T + 1) + ·) (total_steps_succ q (T + 1) n)

/-- The total over a stretch of `a + b` steps is the total over its first `a` steps with the
total over the `b` after them. -/
theorem total_steps_add (q : Nat → Nat) : ∀ (S a b : Nat),
    total (steps S (a + b)) q = total (steps S a) q + total (steps (S + a) b) q
  | S, 0, b => (congrArg (fun k => total (steps S k) q) (Nat.zero_add b)).trans
      (Nat.zero_add _).symm
  | S, a + 1, b =>
    (congrArg (fun k => total (steps S k) q) (Nat.succ_add a b)).trans
      ((congrArg (q S + ·) (total_steps_add q (S + 1) a b)).trans
        ((Nat.add_assoc _ _ _).symm.trans
          (congrArg (fun k => total (steps S (a + 1)) q + total (steps k b) q)
            (Nat.add_right_comm S 1 a))))

/-- A member of a stretch of steps lies between its ends. -/
theorem between_of_mem_steps : ∀ {T N j : Nat}, j ∈ steps T N → T ≤ j ∧ j < T + N
  | _, 0, _, mem => nomatch mem
  | T, N + 1, _, mem => match mem_cons_cases mem with
    | .inl same => ⟨Nat.le_of_eq same.symm,
        Eq.subst (motive := fun x => x < T + (N + 1)) same.symm
          (Nat.lt_add_of_pos_right (Nat.succ_pos N))⟩
    | .inr mem => match between_of_mem_steps mem with
      | ⟨le, lt⟩ => ⟨Nat.le_of_succ_le le,
          Nat.lt_of_lt_of_le lt (Nat.le_of_eq (Nat.add_right_comm T 1 N))⟩

namespace RouteTraces

/-- A count at most another that is not zero leaves the other not zero. -/
theorem nonzero_of_le : ∀ {a b : Nat}, a ≤ b → nonzero a = true → nonzero b = true
  | 0, _, _, pos => Bool.noConfusion pos
  | _ + 1, 0, le, _ => absurd le (Nat.not_succ_le_zero _)
  | _ + 1, _ + 1, _, _ => rfl

end RouteTraces
'''

CHANGE_BLOCK = '''
/-- An amount at most another leaves no excess over it. -/
theorem Flow.excess_zero_of_le : ∀ {a b : Nat}, a ≤ b → excess a b = 0
  | 0, _, _ => rfl
  | _ + 1, 0, le => absurd le (Nat.not_succ_le_zero _)
  | a + 1, b + 1, le => Flow.excess_zero_of_le (a := a) (b := b) (Nat.le_of_succ_le_succ le)
'''

WEIGHTED_BLOCK = '''
/-- Counting one for each member of a list counts its length. -/
theorem Situations.sum_one {α : Type u} : ∀ l : List α, counting.sum l (fun _ => 1) = l.length
  | [] => rfl
  | _ :: l => (Nat.add_comm 1 _).trans (congrArg (· + 1) (Situations.sum_one l))
'''

ROLES_BLOCK = '''
namespace Shuttle

/-- The holder stands at nothing after its step. -/
theorem next_off : ∀ t, stands (holder t) (t + 1) = 0
  | 0 => rfl
  | 1 => rfl
  | t + 2 => (stands_two (holder t) (t + 1)).trans (next_off t)

end Shuttle
'''

REMOVALS = [
    ('Becoming.CrossSituational.Distinct', 'Becoming.Distinct'),
    ('Becoming.Typicality.total', 'Becoming.total'),
    ('Becoming.Tail.nonzero', 'Becoming.nonzero'),
    ('Becoming.Situations.upto', 'Becoming.Undecided.upto'),
    ('Becoming.skip', 'Becoming.skipAt'),
    ('Becoming.DistinctBy', 'Becoming.DistinctUnder'),
    ('Becoming.Hexagram.memberAt', 'Becoming.Law.memberAt'),
    ('Becoming.Joining.slot', 'Becoming.Copying.nth'),
    ('Becoming.Learning.back', 'Becoming.Copying.nth'),
    ('Becoming.Shifts.half', 'Becoming.Pulse.half'),
    ('Becoming.CouplingTraces.consSeq', 'Becoming.Settling.consAct'),
    ('Becoming.Lasting.prepend', 'Becoming.Settling.consAct'),
    ('Becoming.Frequency.SelfLoop.onset_amount', 'Becoming.Closing.Onset.amount_after'),
    ('Becoming.TypicalRuns.sum_one', 'Becoming.Situations.sum_one'),
    ('Becoming.Courses.counting_sum_one', 'Becoming.Situations.sum_one'),
    ('Becoming.Exposed.holder_after', 'Becoming.Shuttle.next_off'),
    ('Becoming.OneStep.Chain.excess_of_le', 'Becoming.Flow.excess_zero_of_le'),
    ('Becoming.HistorySums.nonzero_of_le', 'Becoming.RouteTraces.nonzero_of_le'),
    ('Becoming.Loops.total_steps_shift', 'Becoming.total_steps_succ'),
    ('Becoming.total_steps_split', 'Becoming.total_steps_add'),
    ('Becoming.LossMatching.distinct_map_on', 'Becoming.distinct_map_on'),
    ('Becoming.LossMatching.not_mem_middle', 'Becoming.not_mem_of_middle'),
    ('Becoming.distinct_append_apart', 'Becoming.distinct_append'),
    ("Becoming.Net.distinct_append'", 'Becoming.distinct_append'),
    ('Becoming.SituationTraces.distinct_append', 'Becoming.distinct_append'),
]


def cut(names):
    ds = decltext.decls(refresh=True)
    spans = {}
    for n in names:
        path, a, b = decltext.span(n, ds)
        spans.setdefault(path, []).append((a, b))
    for path, ss in spans.items():
        lines = path.read_text().split('\n')
        gone = set()
        for a, b in ss:
            gone.update(range(a - 1, b))
            if b < len(lines) and lines[b].strip() == '':
                gone.add(b)
        path.write_text('\n'.join(l for i, l in enumerate(lines) if i not in gone))
        print('cut', path.name, len(ss))


def before_end(path, block):
    s = path.read_text().rstrip('\n')
    assert s.endswith('end Becoming'), path
    s = s[:-len('end Becoming')].rstrip('\n') + '\n' + block + '\nend Becoming\n'
    path.write_text(s)


def replace(mod, old, new):
    p = B / f'{mod}.lean'
    s = p.read_text()
    assert s.count(old) == 1, (mod, old)
    p.write_text(s.replace(old, new))


cut(PRELUDE_MOVED + OTHER_MOVED)
before_end(B / 'Prelude.lean', PRELUDE_BLOCK)
before_end(B / 'Change.lean', CHANGE_BLOCK)
before_end(B / 'Weighted.lean', WEIGHTED_BLOCK)
before_end(B / 'Roles.lean', ROLES_BLOCK)
replace('HexagramPlaces', '''def nth : List Hexagram → Nat → Hexagram
  | [], _ => allBroken
  | s :: _, 0 => s
  | _ :: l, n + 1 => nth l n''', 'def nth : List Hexagram → Nat → Hexagram := Law.memberAt allBroken')
replace('OneStep', '''def pick : List Passage → Nat → Passage
  | [], _ => Passage.idle
  | p :: _, 0 => p
  | _ :: P, i + 1 => pick P i''', 'def pick : List Passage → Nat → Passage := Law.memberAt Passage.idle')
replace('RelativePosition', '''def present : Nat → List Member
  | 0 => [.renewer, .first, .second]
  | 1 => [.renewer, .first, .second]
  | _ + 2 => []''', 'def present : Nat → List Member := Exceeding.present')
json.dump({'rows': [{'old': o, 'new': n, 'why': 'R37 B6: the same definition or statement, one name'} for o, n in REMOVALS]},
          open(HERE / 'b6-removals.json', 'w'), indent=1, ensure_ascii=False)
print(len(REMOVALS), 'removal rows')
