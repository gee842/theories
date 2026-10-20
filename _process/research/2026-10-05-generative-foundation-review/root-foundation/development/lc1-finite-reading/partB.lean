
/-! ## A part's merge, paid by the rest -/

namespace Law

variable {S : Type} {P : Type} {E : Type}

/-- Every pair of a member of `ps` and a member of `es`. -/
def pairs : List P → List E → List (P × E)
  | [], _ => []
  | p :: ps, es => es.map (fun e => (p, e)) ++ pairs ps es

theorem mem_row {p : P} : ∀ {es : List E} {e : E}, e ∈ es → (p, e) ∈ es.map (fun e => (p, e))
  | _ :: _, _, .head _ => .head _
  | _ :: _, _, .tail _ mem => .tail _ (mem_row mem)

theorem mem_pairs {p : P} {e : E} : ∀ {ps : List P} {es : List E}, p ∈ ps → e ∈ es →
    (p, e) ∈ pairs ps es
  | _ :: _, es, .head _, mem => mem_append_of_left _ (mem_row mem)
  | q :: _, es, .tail _ mem, mem' => mem_append_of_right (es.map (fun e => (q, e)))
      (mem_pairs mem mem')

theorem length_join {α : Type} : ∀ (a b : List α), (a ++ b).length = a.length + b.length
  | [], b => (Nat.zero_add _).symm
  | _ :: a, b => (congrArg Nat.succ (length_join a b)).trans (Nat.succ_add _ _).symm

theorem length_pairs : ∀ (ps : List P) (es : List E), (pairs ps es).length = ps.length * es.length
  | [], _ => (Nat.zero_mul _).symm
  | p :: ps, es => (length_join _ _).trans
      ((congrArg (· + (pairs ps es).length) (length_map (fun e => (p, e)) es)).trans
        ((congrArg (es.length + ·) (length_pairs ps es)).trans
          ((Nat.add_comm _ _).trans (Nat.succ_mul _ _).symm)))

/-- **Distinct configurations need room in their readings.** Where two readings, a part `part`
and a rest `rest`, together tell every configuration apart, `k` configurations no two of which
coincide, with their parts held by `ps` and their rests by `es`, number at most
`ps.length * es.length`. -/
theorem distinct_within {part : S → P} {rest : S → E}
    (tells : ∀ x y, part x = part y → rest x = rest y → x = y)
    {h : Nat → S} {k : Nat} (distinct : ∀ i j, i < j → j < k → h i ≠ h j)
    {ps : List P} {es : List E} (inP : ∀ i, i < k → part (h i) ∈ ps)
    (inE : ∀ i, i < k → rest (h i) ∈ es) : ¬ ps.length * es.length < k := fun beyond =>
  have room : ∀ n, n ≤ (pairs ps es).length → (part (h n), rest (h n)) ∈ pairs ps es :=
    fun n le =>
      have below : n < k := Nat.lt_of_le_of_lt
        (Nat.le_trans le (Nat.le_of_eq (length_pairs ps es))) beyond
      mem_pairs (inP n below) (inE n below)
  match revisits_within (pairs ps es) (fun n => (part (h n), rest (h n))) room with
  | ⟨i, j, lt, le, same⟩ =>
    distinct i j lt
      (Nat.lt_of_le_of_lt (Nat.le_trans le (Nat.le_of_eq (length_pairs ps es))) beyond)
      (tells _ _ (congrArg Prod.fst same) (congrArg Prod.snd same))

/-- **Merging nothing, a law keeps the possibilities apart.** Under a law that merges nothing,
configurations no two of which coincide are, any number of steps on, still no two alike. -/
theorem Lossless.keeps_apart {next : S → S} (lossless : Lossless next) {h : Nat → S} {k : Nat}
    (distinct : ∀ i j, i < j → j < k → h i ≠ h j) (n : Nat) :
    ∀ i j, i < j → j < k → orbit next (h i) n ≠ orbit next (h j) n :=
  fun i j lt below same => distinct i j lt below (lossless.cancel n same)

/-- **A part's narrowing is paid by the rest.** Under a law that merges nothing, read every
configuration by a part and a rest that together tell configurations apart. Of `k` possibilities
no two alike, if `n` steps on their parts are held by `ps` and their rests by `es`, then `k` is at
most `ps.length * es.length`: the possibilities are conserved, so where the part is narrowed to
fewer configurations the rest must hold correspondingly more. Erasing a part of two
configurations into one, from every rest of `e`, needs the rest to hold at least `2 e`: Landauer's
count, with no energy, temperature or probability, from the law's merging nothing alone. -/
theorem Lossless.narrowing_paid {next : S → S} (lossless : Lossless next) {part : S → P}
    {rest : S → E} (tells : ∀ x y, part x = part y → rest x = rest y → x = y)
    {h : Nat → S} {k : Nat} (distinct : ∀ i j, i < j → j < k → h i ≠ h j) (n : Nat)
    {ps : List P} {es : List E} (inP : ∀ i, i < k → part (orbit next (h i) n) ∈ ps)
    (inE : ∀ i, i < k → rest (orbit next (h i) n) ∈ es) : ¬ ps.length * es.length < k :=
  distinct_within tells (lossless.keeps_apart distinct n) inP inE

/-- **A rest with room for `N` bounds every narrowing.** Where every rest lies in a list of `N`,
the parts of `k` possibilities, at every step under a law that merges nothing, need a list of at
least `k / N`: in a finite rest a part can be narrowed only so far. -/
theorem Lossless.narrowing_floor {next : S → S} (lossless : Lossless next) {part : S → P}
    {rest : S → E} (tells : ∀ x y, part x = part y → rest x = rest y → x = y)
    {room : List E} (finite : ∀ x, rest x ∈ room)
    {h : Nat → S} {k : Nat} (distinct : ∀ i j, i < j → j < k → h i ≠ h j) (n : Nat)
    {ps : List P} (inP : ∀ i, i < k → part (orbit next (h i) n) ∈ ps) :
    ¬ ps.length * room.length < k :=
  lossless.narrowing_paid tells distinct n inP (fun _ _ => finite _)

/-- **Resetting a part at every step needs an unbounded whole.** Where a law merges nothing and,
after every step, a part reads one configuration `p`, then if any configuration has another part,
no list holds every configuration: within finitely many configurations the law would return every
configuration (`Law.Lossless.returns`), each would come after a step, and its part would be `p`.
A part whose reading merges at every step, inside a whole that merges nothing, passes what it
loses into a rest that grows without bound. -/
theorem Lossless.reset_unlisted {next : S → S} (lossless : Lossless next) {part : S → P} {p : P}
    (reset : ∀ x, part (next x) = p) {y : S} (other : part y ≠ p) :
    ¬ ∃ all : List S, ∀ s, s ∈ all := fun ⟨_, every⟩ =>
  match returns_iff.mp (lossless.returns every y) with
  | ⟨0, pos, _⟩ => absurd pos (Nat.lt_irrefl 0)
  | ⟨k + 1, _, back⟩ =>
    other (Eq.subst (motive := fun x => part x = p) back (reset (orbit next y k)))

end Law

/-! ## Reset: a part merged at every step, a whole that merges nothing -/

namespace Reset

/-- The part, one bit, is set to `false` at every step, and the bit it held passes onto the rest,
a list kept: the history of what the part held. -/
def next (x : Bool × List Bool) : Bool × List Bool := (false, x.1 :: x.2)

/-- The whole merges nothing. -/
theorem lossless : Law.Lossless next := Law.lossless_iff.mpr fun x y same => by
  cases x with
  | mk a h =>
    cases y with
    | mk b h' =>
      injection same with _ rest
      injection rest with bit hist
      subst bit
      subst hist
      rfl

/-- The part merges at every step: whatever it held, it reads `false` after the step. -/
theorem part_merges (x : Bool × List Bool) : (next x).1 = false := rfl

/-- The rest grows by one at every step. -/
theorem rest_length (x : Bool × List Bool) : ∀ n, (Law.orbit next x n).2.length = x.2.length + n
  | 0 => rfl
  | n + 1 => congrArg Nat.succ (rest_length x n)

/-- **The part's merges paid by the rest.** The part merges at every step and the whole merges
nothing; the rest of every run never repeats, so no list holds it, as `Law.Lossless.reset_unlisted`
requires of every such law. -/
theorem paid_by_rest :
    Law.Lossless next ∧ (∀ x, (next x).1 = false) ∧ (next (true, [])).1 = (next (false, [])).1 ∧
    (∀ x, ¬ ∃ l : List (List Bool), ∀ n, (Law.orbit next x n).2 ∈ l) ∧
    ¬ ∃ all : List (Bool × List Bool), ∀ s, s ∈ all :=
  ⟨lossless, part_merges, rfl,
   fun x => unlisted_of_new (g := fun n => (Law.orbit next x n).2) fun i j lt same =>
     Nat.ne_of_lt lt (Nat.add_left_cancel ((rest_length x i).symm.trans
       ((congrArg List.length same).trans (rest_length x j)))),
   lossless.reset_unlisted part_merges (y := (true, [])) Bool.noConfusion⟩

end Reset
