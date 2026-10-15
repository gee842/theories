import Becoming.Context
import Becoming.Population

/-!
# Gluing: when readings in context glue, for parity

`Becoming.Context` showed that a frame of context-free claims fits a world exactly where its
registrations glue, with Specker's three boxes and the Mermin–Peres square as possibilities no
context-free reading fits. This module gives the exact law for claims constrained by parity in
each context, with no premise beyond the listed claims and contexts: the next step of P72's
record, “the general parity obstruction; probabilistic contextuality” (Ren, 15 October 2026:
“please make best of your judgement, and push the frontier of completeness”).

A parity system (`ParitySystem`) lists claims and gives each context the claims it counts and the
parity it requires. An assignment of values to the claims meets a context where the parity of its
values on the counted claims is the required one (`ParitySystem.support`). A contradiction
(`ParitySystem.Contradicts`) is a selection of contexts, repetition allowed, counting every listed
claim an even number of times while the parities it requires add up to odd: its constraints,
added together, say that nothing has odd parity.

* **The obstruction.** Every context-free assignment fails an odd number of the contexts of a
  contradiction (`ParitySystem.unmet_odd`), so at least one, found by checking each
  (`ParitySystem.unmet_of_contradicts`), and none lies within every context's possibilities
  (`ParitySystem.contradicts_noGlobal`).
* **It is the only obstruction.** With equality of claims decided and the claims listed without
  repetition, for every list of contexts either a context-free assignment meets each of them or a
  selection of them contradicts (`ParitySystem.global_or_contradicts`). The proof eliminates the
  listed claims one at a time, as in solving linear equations over two values, and carries a
  contradiction found after an elimination back to the contexts it came from
  (`ParityConstraint.met_or_contradicts`). So with the contexts listed, no context-free reading
  lies within every context's possibilities exactly where a selection contradicts
  (`ParitySystem.noGlobal_iff`), and some world respecting the possibilities glues exactly where
  none does (`ParitySystem.glues_iff`).
* **A Bell-type bound.** A context-free assignment meets at most `m − 1` of the `m` contexts of a
  contradiction (`ParitySystem.met_le`), and so does a mixture of them on average, a mixture being
  a list of assignments counted with repetition (`ParitySystem.mixture_le`). Readings indexed by
  their context meet all `m` wherever each context can be met alone (`ParitySystem.indexed_met`):
  the difference between `m − 1` and `m` is what the context carries.
* **Instances.** Specker's three boxes are a parity system whose three openings contradict
  (`Specker.openings_contradict`): every mixture of placements meets at most two of the three on
  average (`Specker.mixture_le`), each opening's own placement meets all three
  (`Specker.indexed_met`), and P72's `Specker.noGlobal` follows (`Specker.noGlobal_of_contradiction`).
  The CHSH game (Clauser, Horne, Shimony and Holt, 1969), two stations each with two settings,
  whose outcomes must differ exactly where both settings are the second: its four pairs of
  settings contradict, so every mixture of context-free outcomes wins at most three of the four
  on average (`CHSH.mixture_le`), the classical bound, while outcomes in context win all four
  (`CHSH.indexed_met`). The Mermin–Peres square's six lines contradict
  (`Square.lines_contradict`): at most five of the six on average (`Square.mixture_le`), all six
  in context (`Square.indexed_met`), and `Square.noGlobal` follows (`Square.noGlobal_of_contradiction`).

What is not derived: the quantum values, which need real amplitudes (Tsirelson's bound for CHSH is
not stated here; `Becoming.Quantum` realizes the square with integer matrices); contextuality
beyond parity constraints; and which registrations of an actual unfolding are of this kind. No
ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

/-! ## Parity on a list -/

/-- Parities added: `addParity a b` is odd exactly where one of the two is. -/
def addParity : Bool → Bool → Bool
  | false, b => b
  | true, b => !b

/-- The parity of a quantity's values over a list. -/
def oddOver {α : Type} : List α → (α → Bool) → Bool
  | [], _ => false
  | a :: as, q => addParity (q a) (oddOver as q)

theorem addParity_false : ∀ b, addParity b false = b := by decide
theorem addParity_self : ∀ b, addParity b b = false := by decide
theorem addParity_assoc : ∀ a b c, addParity (addParity a b) c = addParity a (addParity b c) := by
  decide
theorem addParity_swap : ∀ a b c d,
    addParity (addParity a b) (addParity c d) = addParity (addParity a c) (addParity b d) := by
  decide
theorem addParity_and : ∀ a b c, (addParity a b && c) = addParity (a && c) (b && c) := by decide
theorem addParity_solve : ∀ a b c, addParity a b = c → a = addParity c b := by decide
theorem addParity_cancel : ∀ a b c, addParity (addParity b c) (addParity (addParity a b) c) = a := by
  decide
theorem true_of_ne_false : ∀ b : Bool, ¬ b = false → b = true := by decide
theorem cond_le_one : ∀ b : Bool, cond b 1 0 ≤ 1 := by decide

/-- Conjunctions with one value agree where the other two do whenever the first is `true`. -/
theorem and_congr_of : ∀ (b x y : Bool), (b = true → x = y) → (b && x) = (b && y)
  | true, _, _, same => same rfl
  | false, _, _, _ => rfl

section Lists

variable {α β : Type}

theorem oddOver_add (q r : α → Bool) : ∀ l : List α,
    oddOver l (fun a => addParity (q a) (r a)) = addParity (oddOver l q) (oddOver l r)
  | [] => rfl
  | a :: l => (congrArg (addParity (addParity (q a) (r a))) (oddOver_add q r l)).trans
      (addParity_swap (q a) (r a) (oddOver l q) (oddOver l r))

theorem oddOver_and (q : α → Bool) (b : Bool) : ∀ l : List α,
    oddOver l (fun a => q a && b) = (oddOver l q && b)
  | [] => rfl
  | a :: l => (congrArg (addParity (q a && b)) (oddOver_and q b l)).trans
      (addParity_and (q a) (oddOver l q) b).symm

theorem oddOver_congr {q r : α → Bool} :
    ∀ {l : List α}, (∀ a, a ∈ l → q a = r a) → oddOver l q = oddOver l r
  | [], _ => rfl
  | a :: l, same => show addParity (q a) (oddOver l q) = addParity (r a) (oddOver l r) from
      congr (congrArg addParity (same a (.head l))) (oddOver_congr fun b mem => same b (.tail a mem))

theorem oddOver_false {q : α → Bool} :
    ∀ {l : List α}, (∀ a, a ∈ l → q a = false) → oddOver l q = false
  | [], _ => rfl
  | a :: l, zero => show addParity (q a) (oddOver l q) = addParity false false from
      congr (congrArg addParity (zero a (.head l))) (oddOver_false fun b mem => zero b (.tail a mem))

/-- Parities over two lists may be taken in either order. -/
theorem oddOver_swap (q : α → β → Bool) (m : List β) : ∀ l : List α,
    oddOver l (fun a => oddOver m (q a)) = oddOver m (fun b => oddOver l fun a => q a b)
  | [] => (oddOver_false (l := m) fun _ _ => rfl).symm
  | a :: l => (congrArg (addParity (oddOver m (q a))) (oddOver_swap q m l)).trans
      (oddOver_add (q a) (fun b => oddOver l fun a' => q a' b) m).symm

theorem oddOver_map (g : α → β) (q : β → Bool) : ∀ l : List α,
    oddOver (l.map g) q = oddOver l (fun a => q (g a))
  | [] => rfl
  | a :: l => congrArg (addParity (q (g a))) (oddOver_map g q l)

/-- A member of a mapped list is the image of a member. -/
theorem image_of_mem_map {g : α → β} {b : β} : ∀ {l : List α}, b ∈ l.map g → ∃ a, a ∈ l ∧ g a = b
  | [], mem => nomatch mem
  | a :: _, mem => match mem_cons_cases mem with
    | .inl same => ⟨a, .head _, same.symm⟩
    | .inr mem => match image_of_mem_map mem with
      | ⟨a', found, same⟩ => ⟨a', .tail a found, same⟩

/-! ### Counting what is odd -/

theorem count_le_length (q : α → Bool) : ∀ l : List α, total l (fun a => cond (q a) 1 0) ≤ l.length
  | [] => Nat.le_refl 0
  | a :: l => Nat.le_trans (Nat.add_le_add (cond_le_one (q a)) (count_le_length q l))
      (Nat.le_of_eq (Nat.add_comm 1 l.length))

theorem count_all {q : α → Bool} :
    ∀ {l : List α}, (∀ a, a ∈ l → q a = true) → total l (fun a => cond (q a) 1 0) = l.length
  | [], _ => rfl
  | a :: l, all => show cond (q a) 1 0 + total l (fun a => cond (q a) 1 0) = l.length + 1 from
      (congr (congrArg Nat.add (congrArg (cond · 1 0) (all a (.head l))))
        (count_all fun b mem => all b (.tail a mem))).trans (Nat.add_comm 1 l.length)

theorem met_step : ∀ (b x : Bool) (n y : Nat), y ≤ n → (x = true → y + 1 ≤ n) →
    addParity b x = true → cond (!b) 1 0 + y + 1 ≤ n + 1
  | true, _, _, y, le, _, _ => Nat.succ_le_succ (Nat.le_trans (Nat.le_of_eq (Nat.zero_add y)) le)
  | false, _, _, y, _, odd, holds =>
    Nat.succ_le_succ (Nat.le_trans (Nat.le_of_eq (Nat.add_comm 1 y)) (odd holds))

/-- Where the parity of a quantity's values over a list is odd, the members at which it is even
number at most one fewer than the list. -/
theorem even_le_of_odd {q : α → Bool} :
    ∀ {l : List α}, oddOver l q = true → total l (fun a => cond (!(q a)) 1 0) + 1 ≤ l.length
  | [], odd => Bool.noConfusion odd
  | a :: l, odd => met_step (q a) (oddOver l q) l.length _ (count_le_length (fun a => !(q a)) l)
      even_le_of_odd odd

end Lists

/-! ## Parity constraints -/

/-- A parity constraint on claims: which claims it counts, and whether their parity must be odd. -/
structure ParityConstraint (C : Type) where
  counts : C → Bool
  odd : Bool

namespace ParityConstraint

variable {C : Type}

/-- The parity, over listed claims, of an assignment's values on the claims the constraint
counts. -/
def value (xs : List C) (r : ParityConstraint C) (v : C → Bool) : Bool :=
  oddOver xs fun c => r.counts c && v c

/-- Two constraints added. -/
def add (r p : ParityConstraint C) : ParityConstraint C :=
  ⟨fun c => addParity (r.counts c) (p.counts c), addParity r.odd p.odd⟩

theorem value_add (xs : List C) (r p : ParityConstraint C) (v : C → Bool) :
    (r.add p).value xs v = addParity (r.value xs v) (p.value xs v) :=
  (oddOver_congr fun c _ => addParity_and (r.counts c) (p.counts c) (v c)).trans
    (oddOver_add (fun c => r.counts c && v c) (fun c => p.counts c && v c) xs)

/-- Added together, the constraints `ks` count no listed claim and require odd parity. -/
def Contradicts (xs : List C) (ks : List (ParityConstraint C)) : Prop :=
  (∀ c, c ∈ xs → oddOver ks (fun r => r.counts c) = false) ∧ oddOver ks (fun r => r.odd) = true

/-- Constraints that together count no listed claim have even parity together at every
assignment. -/
theorem value_even {xs : List C} {ks : List (ParityConstraint C)}
    (even : ∀ c, c ∈ xs → oddOver ks (fun r => r.counts c) = false) (v : C → Bool) :
    oddOver ks (fun r => r.value xs v) = false :=
  (oddOver_swap (fun (r : ParityConstraint C) (c : C) => r.counts c && v c) xs ks).trans
    ((oddOver_congr fun c _ => oddOver_and (fun r => r.counts c) (v c) ks).trans
      (oddOver_false fun c mem => congrArg (· && v c) (even c mem)))

/-- **Every assignment fails an odd number of the constraints of a contradiction.** -/
theorem unmet_odd {xs : List C} {ks : List (ParityConstraint C)} (contra : Contradicts xs ks)
    (v : C → Bool) : oddOver ks (fun r => addParity (r.value xs v) r.odd) = true :=
  (oddOver_add (fun r => r.value xs v) (fun r => r.odd) ks).trans
    ((congrArg (addParity · (oddOver ks fun r => r.odd)) (value_even contra.1 v)).trans contra.2)

/-- Eliminating `x` with the pivot `p`: a constraint counting `x` has `p` added to it. -/
def eliminate (x : C) (p r : ParityConstraint C) : ParityConstraint C :=
  cond (r.counts x) (r.add p) r

theorem counts_after {x : C} {p r : ParityConstraint C} (pivot : p.counts x = true) :
    ∀ b, r.counts x = b → (cond b (r.add p) r).counts x = false
  | false, counted => counted
  | true, counted => (congr (congrArg addParity counted) pivot : _ = addParity true true)

/-- After eliminating `x` with a pivot counting it, no constraint counts `x`. -/
theorem eliminate_counts {x : C} {p : ParityConstraint C} (pivot : p.counts x = true)
    (r : ParityConstraint C) : (eliminate x p r).counts x = false :=
  counts_after pivot (r.counts x) rfl

/-- A constraint is met at the assignment built after an elimination. -/
theorem met_after {xs : List C} {x : C} {p r : ParityConstraint C} {v v' : C → Bool}
    (vx : v x = addParity p.odd (p.value xs v')) (rest : r.value xs v = r.value xs v') :
    ∀ b, r.counts x = b → (cond b (r.add p) r).value xs v' = (cond b (r.add p) r).odd →
      addParity (r.counts x && v x) (r.value xs v) = r.odd
  | false, counted, met =>
    (congrArg (fun b => addParity (b && v x) (r.value xs v)) counted).trans (rest.trans met)
  | true, counted, met =>
    (congrArg (fun b => addParity (b && v x) (r.value xs v)) counted).trans
      ((congr (congrArg addParity vx)
        (rest.trans (addParity_solve _ _ _ ((value_add xs r p v').symm.trans met)))).trans
        (addParity_cancel r.odd p.odd (p.value xs v')))

/-- A selection after an elimination comes from a selection before it, with the same counts and
parities together. -/
theorem pulled {rs : List (ParityConstraint C)} {p r : ParityConstraint C}
    (pmem : p ∈ rs) (rmem : r ∈ rs) {rest ks : List (ParityConstraint C)}
    (ksub : ∀ k, k ∈ ks → k ∈ rs)
    (counts : ∀ c, oddOver ks (fun r => r.counts c) = oddOver rest (fun r => r.counts c))
    (odd : oddOver ks (fun r => r.odd) = oddOver rest (fun r => r.odd)) :
    ∀ b, ∃ ks₀, (∀ k, k ∈ ks₀ → k ∈ rs) ∧
      (∀ c, oddOver ks₀ (fun r => r.counts c) = oddOver (cond b (r.add p) r :: rest) (fun r => r.counts c)) ∧
        oddOver ks₀ (fun r => r.odd) = oddOver (cond b (r.add p) r :: rest) (fun r => r.odd)
  | false => ⟨r :: ks, (fun k mem => match k, mem with
      | _, .head _ => rmem
      | k, .tail _ mem => ksub k mem),
    fun c => congrArg (addParity (r.counts c)) (counts c), congrArg (addParity r.odd) odd⟩
  | true => ⟨r :: p :: ks, (fun k mem => match k, mem with
      | _, .head _ => rmem
      | _, .tail _ (.head _) => pmem
      | k, .tail _ (.tail _ mem) => ksub k mem),
    fun c => (addParity_assoc (r.counts c) (p.counts c) (oddOver ks fun r => r.counts c)).symm.trans
      (congrArg (addParity (addParity (r.counts c) (p.counts c))) (counts c)),
    (addParity_assoc r.odd p.odd (oddOver ks fun r => r.odd)).symm.trans
      (congrArg (addParity (addParity r.odd p.odd)) odd)⟩

theorem pull_back {rs : List (ParityConstraint C)} {x : C} {p : ParityConstraint C} (pmem : p ∈ rs) :
    ∀ ks' : List (ParityConstraint C), (∀ k, k ∈ ks' → k ∈ rs.map (eliminate x p)) →
      ∃ ks, (∀ k, k ∈ ks → k ∈ rs) ∧
        (∀ c, oddOver ks (fun r => r.counts c) = oddOver ks' (fun r => r.counts c)) ∧
          oddOver ks (fun r => r.odd) = oddOver ks' (fun r => r.odd)
  | [], _ => ⟨[], (fun _ mem => nomatch mem), (fun _ => rfl), rfl⟩
  | k' :: rest, sub =>
    match pull_back pmem rest (fun k mem => sub k (.tail k' mem)) with
    | ⟨_, ksub, counts, odd⟩ => match image_of_mem_map (sub k' (.head rest)) with
      | ⟨r, rmem, same⟩ =>
        Eq.subst (motive := fun k => ∃ ks₀, (∀ k, k ∈ ks₀ → k ∈ rs) ∧
            (∀ c, oddOver ks₀ (fun r => r.counts c) = oddOver (k :: rest) (fun r => r.counts c)) ∧
              oddOver ks₀ (fun r => r.odd) = oddOver (k :: rest) (fun r => r.odd))
          same (pulled pmem rmem ksub counts odd (r.counts x))

/-- **One of the two, by elimination.** With equality of claims decided and the claims listed
without repetition, for every list of constraints either one assignment meets each of them, or a
selection of them, repetition allowed, contradicts. -/
theorem met_or_contradicts [DecidableEq C] : ∀ (xs : List C), Distinct xs →
    ∀ rs : List (ParityConstraint C),
      (∃ v : C → Bool, ∀ r, r ∈ rs → r.value xs v = r.odd) ∨
        ∃ ks, (∀ k, k ∈ ks → k ∈ rs) ∧ Contradicts xs ks
  | [], _, rs => match search (p := fun r : ParityConstraint C => r.odd = false) rs with
    | .inl ⟨r, mem, odd⟩ => .inr ⟨[r], (fun k found => match k, found with
        | _, .head _ => mem
        | _, .tail _ found => nomatch found),
      (fun _ found => nomatch found), (addParity_false r.odd).trans (true_of_ne_false r.odd odd)⟩
    | .inr even => .inl ⟨fun _ => false, fun r mem => (even r mem).symm⟩
  | x :: xs, ⟨fresh, distinct⟩, rs =>
    match search (p := fun r : ParityConstraint C => r.counts x = false) rs with
    | .inr uncounted => match met_or_contradicts xs distinct rs with
      | .inl ⟨v, met⟩ => .inl ⟨v, fun r mem =>
          show addParity (r.counts x && v x) (r.value xs v) = r.odd from
            Eq.subst (motive := fun b => addParity (b && v x) (r.value xs v) = r.odd)
              (uncounted r mem).symm (met r mem)⟩
      | .inr ⟨ks, sub, even, odd⟩ => .inr ⟨ks, sub, (fun c mem => match c, mem with
          | _, .head _ => oddOver_false fun k found => uncounted k (sub k found)
          | c, .tail _ mem => even c mem), odd⟩
    | .inl ⟨p, pmem, counted⟩ =>
      have pivot : p.counts x = true := true_of_ne_false _ counted
      match met_or_contradicts xs distinct (rs.map (eliminate x p)) with
      | .inl ⟨v', met⟩ =>
        let v : C → Bool := fun c => if c = x then addParity p.odd (p.value xs v') else v' c
        have vx : v x = addParity p.odd (p.value xs v') := if_pos rfl
        have rest : ∀ r : ParityConstraint C, r.value xs v = r.value xs v' := fun r =>
          oddOver_congr fun (c : C) found => congrArg (r.counts c && ·)
            (if_neg fun same => fresh (Eq.subst (motive := fun d => d ∈ xs) same found))
        .inl ⟨v, fun r mem => met_after vx (rest r) (r.counts x) rfl (met _ (mem_map_of mem))⟩
      | .inr ⟨ks', sub', even', odd'⟩ => match pull_back pmem ks' sub' with
        | ⟨ks, sub, counts, odd⟩ => .inr ⟨ks, sub, (fun c mem => match c, mem with
            | _, .head _ => (counts x).trans (oddOver_false fun k found =>
                match image_of_mem_map (sub' k found) with
                | ⟨r, _, same⟩ => Eq.subst (motive := fun k => k.counts x = false) same
                    (eliminate_counts pivot r))
            | c, .tail _ mem => (counts c).trans (even' c mem)),
          odd.trans odd'⟩

end ParityConstraint

/-! ## Parity systems -/

/-- Claims constrained by parity in contexts: the listed claims, the claims each context counts,
and the parity each context requires. -/
structure ParitySystem (K C : Type) where
  claims : List C
  counts : K → C → Bool
  odd : K → Bool

namespace ParitySystem

variable {K C : Type} (S : ParitySystem K C)

/-- The constraint of a context. -/
def constraint (k : K) : ParityConstraint C := ⟨S.counts k, S.odd k⟩

/-- A context registers the claims it counts. -/
def within (k : K) (c : C) : Prop := S.counts k c = true

/-- The parity of an assignment's values on the listed claims a context counts. -/
def value (k : K) (v : C → Bool) : Bool := (S.constraint k).value S.claims v

/-- An assignment lies within a context's possibilities where its parity there is the required
one. -/
def support (k : K) (v : C → Bool) : Prop := S.value k v = S.odd k

instance (k : K) (v : C → Bool) : Decidable (S.support k v) := instDecidableEqBool _ _

/-- Whether an assignment meets a context. -/
def met (k : K) (v : C → Bool) : Bool := !(addParity (S.value k v) (S.odd k))

/-- A selection of contexts, repetition allowed, counting every listed claim an even number of
times while the parities it requires add up to odd. -/
def Contradicts (ks : List K) : Prop :=
  (∀ c, c ∈ S.claims → oddOver ks (fun k => S.counts k c) = false) ∧ oddOver ks S.odd = true

/-- What a context can show depends only on the claims it registers. -/
theorem local_ : Local S.within S.support :=
  fun k v v' same met =>
    (oddOver_congr fun c _ => and_congr_of (S.counts k c) (v c) (v' c) (same c)).symm.trans met

theorem contradicts_iff (ks : List K) :
    S.Contradicts ks ↔ ParityConstraint.Contradicts S.claims (ks.map S.constraint) :=
  ⟨fun ⟨even, odd⟩ => ⟨fun c mem => (oddOver_map S.constraint (fun r => r.counts c) ks).trans
      (even c mem), (oddOver_map S.constraint (fun r => r.odd) ks).trans odd⟩,
   fun ⟨even, odd⟩ => ⟨fun c mem => (oddOver_map S.constraint (fun r => r.counts c) ks).symm.trans
      (even c mem), (oddOver_map S.constraint (fun r => r.odd) ks).symm.trans odd⟩⟩

variable {S}

/-- **Every context-free assignment fails an odd number of the contexts of a contradiction.** -/
theorem unmet_odd {ks : List K} (contra : S.Contradicts ks) (v : C → Bool) :
    oddOver ks (fun k => addParity (S.value k v) (S.odd k)) = true :=
  (oddOver_map S.constraint (fun r => addParity (r.value S.claims v) r.odd) ks).symm.trans
    (ParityConstraint.unmet_odd ((S.contradicts_iff ks).mp contra) v)

/-- So it fails at least one, found by checking each. -/
theorem unmet_of_contradicts {ks : List K} (contra : S.Contradicts ks) (v : C → Bool) :
    ∃ k, k ∈ ks ∧ ¬ S.support k v :=
  match search (p := fun k => S.support k v) ks with
  | .inl found => found
  | .inr all => Bool.noConfusion ((oddOver_false fun k mem =>
      (congrArg (addParity · (S.odd k)) (all k mem)).trans (addParity_self (S.odd k))).symm.trans
        (unmet_odd contra v))

/-- **No context-free reading lies within the possibilities of every context of a
contradiction.** -/
theorem contradicts_noGlobal {ks : List K} (contra : S.Contradicts ks) : NoGlobal S.support :=
  fun ⟨v, all⟩ => match unmet_of_contradicts contra v with
    | ⟨k, _, unmet⟩ => unmet (all k)

/-- **A Bell-type bound.** A context-free assignment meets at most `m − 1` of the `m` contexts of
a contradiction. -/
theorem met_le {ks : List K} (contra : S.Contradicts ks) (v : C → Bool) :
    total ks (fun k => cond (S.met k v) 1 0) + 1 ≤ ks.length :=
  even_le_of_odd (unmet_odd contra v)

/-- **So does every mixture, on average.** Over a list of context-free assignments counted with
repetition, the contexts met, together with the number of assignments, are at most `m` for each
assignment. -/
theorem mixture_le {ks : List K} (contra : S.Contradicts ks) (mix : List (C → Bool)) :
    total mix (fun v => total ks (fun k => cond (S.met k v) 1 0)) + mix.length ≤
      total mix (fun _ => ks.length) :=
  Nat.le_trans (Nat.le_of_eq ((congrArg (total mix (fun v => total ks fun k => cond (S.met k v) 1 0) + ·)
      (total_ones mix).symm).trans (total_add _ (fun _ => 1) mix).symm))
    (total_le mix fun v _ => met_le contra v)

/-- **Readings in context meet every context that can be met alone.** Where each context of a
selection is given an assignment within its possibilities, reading each context by its own
assignment meets all `m` of them. -/
theorem indexed_met {ks : List K} (choose : K → C → Bool)
    (each : ∀ k, k ∈ ks → S.support k (choose k)) :
    total ks (fun k => cond (S.met k (choose k)) 1 0) = ks.length :=
  count_all fun k mem =>
    (congrArg (fun b => !(addParity b (S.odd k))) (each k mem)).trans
      (congrArg (!·) (addParity_self (S.odd k)))

variable (S)

/-- A selection of constraints of listed contexts is the constraints of a selection of them. -/
theorem lift_selection {all : List K} : ∀ rs : List (ParityConstraint C),
    (∀ r, r ∈ rs → r ∈ all.map S.constraint) →
      ∃ ks : List K, (∀ k, k ∈ ks → k ∈ all) ∧ ks.map S.constraint = rs
  | [], _ => ⟨[], (fun _ mem => nomatch mem), rfl⟩
  | r :: rest, sub => match lift_selection rest (fun r' mem => sub r' (.tail r mem)) with
    | ⟨ks, ksub, same⟩ => match image_of_mem_map (sub r (.head rest)) with
      | ⟨k, kmem, image⟩ => ⟨k :: ks, (fun k' mem => match k', mem with
          | _, .head _ => kmem
          | k', .tail _ mem => ksub k' mem),
        show S.constraint k :: ks.map S.constraint = r :: rest from
          congr (congrArg List.cons image) same⟩

/-- **The parity law: a context-free reading or a contradiction.** With equality of claims
decided and the claims listed without repetition, for every list of contexts either a
context-free assignment meets every context in it, or a selection of its contexts contradicts. -/
theorem global_or_contradicts [DecidableEq C] (distinct : Distinct S.claims) (all : List K) :
    (∃ v : C → Bool, ∀ k, k ∈ all → S.support k v) ∨
      ∃ ks, (∀ k, k ∈ ks → k ∈ all) ∧ S.Contradicts ks :=
  match ParityConstraint.met_or_contradicts S.claims distinct (all.map S.constraint) with
  | .inl ⟨v, met⟩ => .inl ⟨v, fun _ mem => met _ (mem_map_of mem)⟩
  | .inr ⟨rs, sub, contra⟩ => match S.lift_selection rs sub with
    | ⟨ks, ksub, same⟩ => .inr ⟨ks, ksub, (S.contradicts_iff ks).mpr
        (Eq.subst (motive := fun l => ParityConstraint.Contradicts S.claims l) same.symm contra)⟩

/-- So, with the contexts listed, no context-free reading lies within every context's
possibilities exactly where a selection of contexts contradicts. -/
theorem noGlobal_iff [DecidableEq C] (distinct : Distinct S.claims) {all : List K}
    (every : ∀ k, k ∈ all) : NoGlobal S.support ↔ ∃ ks, S.Contradicts ks :=
  ⟨fun none => match S.global_or_contradicts distinct all with
    | .inl ⟨v, met⟩ => absurd ⟨v, fun k => met k (every k)⟩ none
    | .inr ⟨ks, _, contra⟩ => ⟨ks, contra⟩,
   fun ⟨_, contra⟩ => contradicts_noGlobal contra⟩

/-- **Readings in context glue exactly where no selection of contexts contradicts.** With the
contexts listed, some world registering what each context counts, respecting the possibilities,
glues at its configuration exactly where no selection contradicts. -/
theorem glues_iff [DecidableEq C] (distinct : Distinct S.claims) {all : List K}
    (every : ∀ k, k ∈ all) :
    (∃ X : Contextual Unit K C Bool, X.within = S.within ∧ X.Respects S.support () ∧ X.Glues ()) ↔
      ¬ ∃ ks, S.Contradicts ks :=
  ⟨fun ⟨X, same, respects, glues⟩ ⟨_, contra⟩ =>
     X.not_glues (Eq.subst (motive := fun w => Local w S.support) same.symm S.local_)
       (contradicts_noGlobal contra) respects glues,
   fun none => match S.global_or_contradicts distinct all with
    | .inl ⟨v, met⟩ => ⟨⟨S.within, fun _ _ => v⟩, rfl, fun k => met k (every k),
        ⟨v, fun _ _ _ => rfl⟩⟩
    | .inr ⟨ks, _, contra⟩ => absurd ⟨ks, contra⟩ none⟩

end ParitySystem

/-! ## Specker's three boxes -/

namespace Specker

/-- An opening counts its two boxes and requires odd parity: exactly one of them holds the gem. -/
def paritySystem : ParitySystem Opening Box :=
  ⟨[.a, .b, .c], fun k x => marks (first k) x || marks (second k) x, fun _ => true⟩

theorem two_iff : ∀ x y : Bool, (addParity x (addParity y false) = true) ↔ x ≠ y := by decide
theorem two_iff_swap : ∀ x y : Bool, (addParity x (addParity y false) = true) ↔ y ≠ x := by decide

/-- The parity system's possibilities are the openings' possibilities. -/
theorem support_iff : ∀ (k : Opening) (v : Box → Bool), paritySystem.support k v ↔ support k v
  | .ab, v => two_iff (v .a) (v .b)
  | .bc, v => two_iff (v .b) (v .c)
  | .ca, v => two_iff_swap (v .a) (v .c)

/-- The three openings. -/
def openings : List Opening := [.ab, .bc, .ca]

/-- **The three openings contradict**: each box is opened twice, and three odd parities add up to
odd. -/
theorem openings_contradict : paritySystem.Contradicts openings :=
  ⟨fun x _ => match x with
    | .a => rfl
    | .b => rfl
    | .c => rfl, rfl⟩

/-- P72's `noGlobal`, from the contradiction. -/
theorem noGlobal_of_contradiction : NoGlobal support :=
  fun ⟨v, all⟩ => ParitySystem.contradicts_noGlobal openings_contradict
    ⟨v, fun k => (support_iff k v).mpr (all k)⟩

/-- **Every mixture of placements meets at most two of the three openings on average.** -/
theorem mixture_le (mix : List (Box → Bool)) :
    total mix (fun v => total openings (fun k => cond (paritySystem.met k v) 1 0)) + mix.length ≤
      total mix (fun _ => 3) :=
  ParitySystem.mixture_le openings_contradict mix

/-- **Each opening read by its own placement meets all three**: in `world`, each opening shows
the gem in its first box. -/
theorem indexed_met :
    total openings (fun k => cond (paritySystem.met k (world.shows () k)) 1 0) = 3 :=
  ParitySystem.indexed_met (fun k => world.shows () k) fun k _ => (support_iff k _).mpr (respects k)

end Specker

/-! ## The CHSH game -/

namespace CHSH

/-- The outcomes: `left x` at the first station under setting `x`, `right y` at the second under
setting `y`. -/
inductive Outcome where
  | left (x : Bool)
  | right (y : Bool)

/-- The four outcomes. -/
def outcomes : List Outcome := [.left false, .left true, .right false, .right true]

/-- Whether two settings are the same. -/
def same (x y : Bool) : Bool := !(addParity x y)

/-- A pair of settings registers the outcome at each station under its setting, and requires
the two to differ exactly where both settings are `true`. -/
def paritySystem : ParitySystem (Bool × Bool) Outcome :=
  ⟨outcomes, fun k o => match o with
    | .left x => same x k.1
    | .right y => same y k.2, fun k => k.1 && k.2⟩

theorem two_iff : ∀ x y b : Bool, (addParity x (addParity y false) = b) ↔ addParity x y = b := by
  decide

/-- **The winning condition.** The pair `(x, y)` is met exactly where the two outcomes differ
exactly when both settings are `true`. -/
theorem support_iff : ∀ (x y : Bool) (v : Outcome → Bool),
    paritySystem.support (x, y) v ↔ addParity (v (.left x)) (v (.right y)) = (x && y)
  | false, false, v => two_iff (v (.left false)) (v (.right false)) false
  | false, true, v => two_iff (v (.left false)) (v (.right true)) false
  | true, false, v => two_iff (v (.left true)) (v (.right false)) false
  | true, true, v => two_iff (v (.left true)) (v (.right true)) true

/-- The four pairs of settings. -/
def pairs : List (Bool × Bool) := [(false, false), (false, true), (true, false), (true, true)]

/-- **The four pairs contradict**: each outcome is registered twice, and only one pair requires
the outcomes to differ. -/
theorem pairs_contradict : paritySystem.Contradicts pairs :=
  ⟨fun o _ => match o with
    | .left false => rfl
    | .left true => rfl
    | .right false => rfl
    | .right true => rfl, rfl⟩

/-- **The classical bound.** Every mixture of context-free outcomes wins at most three of the four
pairs on average. -/
theorem mixture_le (mix : List (Outcome → Bool)) :
    total mix (fun v => total pairs (fun k => cond (paritySystem.met k v) 1 0)) + mix.length ≤
      total mix (fun _ => 4) :=
  ParitySystem.mixture_le pairs_contradict mix

/-- Outcomes read in their pair: both `false`, except that the second station's is `true` where
both settings are. -/
def inPair (k : Bool × Bool) : Outcome → Bool
  | .left _ => false
  | .right _ => k.1 && k.2

theorem inPair_support : ∀ k, paritySystem.support k (inPair k)
  | (false, false) => rfl
  | (false, true) => rfl
  | (true, false) => rfl
  | (true, true) => rfl

/-- **Outcomes in context win all four.** -/
theorem indexed_met : total pairs (fun k => cond (paritySystem.met k (inPair k)) 1 0) = 4 :=
  ParitySystem.indexed_met inPair fun k _ => inPair_support k

end CHSH

/-! ## The Mermin–Peres square -/

namespace Square

/-- The nine cells, row by row. -/
def cells : List Cell :=
  [(i0, i0), (i0, i1), (i0, i2), (i1, i0), (i1, i1), (i1, i2), (i2, i0), (i2, i1), (i2, i2)]

/-- A line counts its three cells. -/
def counts : Line → Cell → Bool
  | .row i, p => Nat.beq p.1.val i.val
  | .column j, p => Nat.beq p.2.val j.val

/-- The square's parity system: a line counts its cells and requires the parity `odd`. -/
def paritySystem : ParitySystem Line Cell := ⟨cells, counts, odd⟩

/-- The six lines. -/
def lines : List Line := [.row i0, .row i1, .row i2, .column i0, .column i1, .column i2]

theorem three_iff : ∀ x y z b : Bool,
    (addParity x (addParity y (addParity z false)) = b) ↔ (x ^^ (y ^^ z)) = b := by decide

theorem not_beyond {n : Nat} (lt : n + 3 < 3) : False :=
  Nat.not_lt_of_le (Nat.le_add_left 3 n) lt

/-- The parity system's possibilities are the lines' possibilities. -/
theorem support_iff : ∀ (l : Line) (v : Cell → Bool), paritySystem.support l v ↔ support l v
  | .row ⟨0, _⟩, v => three_iff (v (i0, i0)) (v (i0, i1)) (v (i0, i2)) false
  | .row ⟨1, _⟩, v => three_iff (v (i1, i0)) (v (i1, i1)) (v (i1, i2)) false
  | .row ⟨2, _⟩, v => three_iff (v (i2, i0)) (v (i2, i1)) (v (i2, i2)) false
  | .row ⟨_ + 3, lt⟩, _ => (not_beyond lt).elim
  | .column ⟨0, _⟩, v => three_iff (v (i0, i0)) (v (i1, i0)) (v (i2, i0)) false
  | .column ⟨1, _⟩, v => three_iff (v (i0, i1)) (v (i1, i1)) (v (i2, i1)) false
  | .column ⟨2, _⟩, v => three_iff (v (i0, i2)) (v (i1, i2)) (v (i2, i2)) true
  | .column ⟨_ + 3, lt⟩, _ => (not_beyond lt).elim

theorem cells_even : ∀ p, p ∈ cells → oddOver lines (fun l => counts l p) = false
  | _, .head _ => rfl
  | _, .tail _ (.head _) => rfl
  | _, .tail _ (.tail _ (.head _)) => rfl
  | _, .tail _ (.tail _ (.tail _ (.head _))) => rfl
  | _, .tail _ (.tail _ (.tail _ (.tail _ (.head _)))) => rfl
  | _, .tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _))))) => rfl
  | _, .tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _)))))) => rfl
  | _, .tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _))))))) => rfl
  | _, .tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.tail _ (.head _)))))))) => rfl

/-- **The six lines contradict**: each cell lies on one row and one column, and only the third
column requires odd parity. -/
theorem lines_contradict : paritySystem.Contradicts lines := ⟨cells_even, rfl⟩

/-- `noGlobal`, from the contradiction. -/
theorem noGlobal_of_contradiction : NoGlobal support :=
  fun ⟨v, all⟩ => ParitySystem.contradicts_noGlobal lines_contradict
    ⟨v, fun l => (support_iff l v).mpr (all l)⟩

/-- **Every mixture of context-free assignments meets at most five of the six lines on
average.** -/
theorem mixture_le (mix : List (Cell → Bool)) :
    total mix (fun v => total lines (fun l => cond (paritySystem.met l v) 1 0)) + mix.length ≤
      total mix (fun _ => 6) :=
  ParitySystem.mixture_le lines_contradict mix

/-- Values read in their line: `false` at its first two positions and the line's parity at the
third. -/
def inLine (l : Line) (y : Cell) : Bool := fill i0 false (odd l) (pos l y)

theorem inLine_support (l : Line) : support l (inLine l) :=
  show parity (fill i0 false (odd l) (pos l (at_ l i0))) (fill i0 false (odd l) (pos l (at_ l i1)))
      (fill i0 false (odd l) (pos l (at_ l i2))) = odd l by
    rw [pos_at, pos_at, pos_at]
    exact (fill_parity i0 false (odd l)).1

/-- **Values in context meet all six lines.** -/
theorem indexed_met : total lines (fun l => cond (paritySystem.met l (inLine l)) 1 0) = 6 :=
  ParitySystem.indexed_met inLine fun l _ => (support_iff l _).mpr (inLine_support l)

end Square

end Becoming
