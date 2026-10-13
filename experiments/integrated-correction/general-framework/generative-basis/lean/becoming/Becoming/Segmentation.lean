/-!
# Segmentation: grouping a sequence by a learned relation of adjacency

A sequence is grouped by a relation `r` between adjacent elements: reading from the right, an
element joins the group that follows it where `r` links it to that group's first element, and
opens a new group otherwise (`chunks`). This is the grouping of the inquiry-root acquisition
histories, stated for every alphabet and every relation.

* **Grouping is exact.** Grouping by `r` returns a list of groups exactly when every group is
  nonempty and linked by `r` inside, and no group is linked by `r` to the next
  (`chunks_eq_iff`). That partition is the only one with this property (`chunks_unique`), and
  grouping never changes the sequence (`join_chunks`).
* **Encoded words.** For a vocabulary of nonempty words, grouping recovers the words of every
  encoded sequence exactly when each word is linked inside and the last element of any word is
  not linked to the first element of any word (`encode_iff`). Both conditions are local: they
  concern single adjacent pairs.
* **Majority bonds are functional.** Where the relation is learned as the strict majority of
  observed transitions (`bond`), each element is linked to at most one successor
  (`bond_unique`). So where two words continue one element differently inside, no record of
  transitions groups both (`no_record_groups`).
* **Reading.** Where grouping recovers the words, reading every encoded sequence word by word
  gives the meanings of its words exactly when each word is read as its meaning
  (`reads_every_iff`).

No premise is added; the module imports nothing and every declaration has an empty axiom
report.
-/

namespace Becoming.Segmentation

universe u v w

variable {α : Type u}

/-! ## Grouping -/

/-- An element joins the group that follows it where `r` links them. -/
def glue (r : α → α → Bool) (x : α) : List (List α) → List (List α)
  | [] => [[x]]
  | [] :: rest => [x] :: rest
  | (y :: ys) :: rest => if r x y = true then (x :: y :: ys) :: rest else [x] :: (y :: ys) :: rest

/-- Group a sequence by the relation `r` between adjacent elements. -/
def chunks (r : α → α → Bool) : List α → List (List α)
  | [] => []
  | x :: xs => glue r x (chunks r xs)

/-- The group `x :: xs` is linked by `r` at each adjacent pair. -/
def LinkedFrom (r : α → α → Bool) : α → List α → Prop
  | _, [] => True
  | x, y :: ys => r x y = true ∧ LinkedFrom r y ys

/-- The last element of `x :: xs`. -/
def lastOf : α → List α → α
  | x, [] => x
  | _, y :: ys => lastOf y ys

/-- The group after an element `z`, if any, is not linked from it. -/
def Opens (r : α → α → Bool) (z : α) : List (List α) → Prop
  | [] => True
  | [] :: _ => True
  | (y :: _) :: _ => r z y = false

/-- Every group is nonempty and linked inside, and no group is linked to the next. -/
def Grouped (r : α → α → Bool) : List (List α) → Prop
  | [] => True
  | [] :: _ => False
  | (x :: xs) :: rest => LinkedFrom r x xs ∧ Opens r (lastOf x xs) rest ∧ Grouped r rest

/-- Joining a sequence of groups. -/
def join : List (List α) → List α
  | [] => []
  | g :: gs => g ++ join gs

theorem join_glue (r : α → α → Bool) (x : α) :
    ∀ L : List (List α), join (glue r x L) = x :: join L
  | [] => rfl
  | [] :: _ => rfl
  | (y :: ys) :: rest => by
    show join (if r x y = true then (x :: y :: ys) :: rest else [x] :: (y :: ys) :: rest) = _
    cases r x y with
    | true => rfl
    | false => rfl

/-- **Grouping never changes the sequence.** -/
theorem join_chunks (r : α → α → Bool) : ∀ xs : List α, join (chunks r xs) = xs
  | [] => rfl
  | x :: xs => (join_glue r x (chunks r xs)).trans (congrArg (List.cons x) (join_chunks r xs))

theorem grouped_glue (r : α → α → Bool) (x : α) :
    ∀ L : List (List α), Grouped r L → Grouped r (glue r x L)
  | [], _ => ⟨trivial, trivial, trivial⟩
  | [] :: _, absurd => absurd.elim
  | (y :: ys) :: rest, ⟨linked, opens, grouped⟩ => by
    show Grouped r (if r x y = true then (x :: y :: ys) :: rest else [x] :: (y :: ys) :: rest)
    cases link : r x y with
    | true => exact ⟨⟨link, linked⟩, opens, grouped⟩
    | false => exact ⟨trivial, link, linked, opens, grouped⟩

/-- **Grouping returns a grouped partition.** -/
theorem grouped_chunks (r : α → α → Bool) : ∀ xs : List α, Grouped r (chunks r xs)
  | [] => trivial
  | x :: xs => grouped_glue r x (chunks r xs) (grouped_chunks r xs)

/-- A group linked inside, followed by a grouped rest it is not linked to, is regrouped as it
stands. -/
theorem chunks_group (r : α → α → Bool) {rest : List (List α)} (grouped : Grouped r rest)
    (again : chunks r (join rest) = rest) :
    ∀ (x : α) (xs : List α), LinkedFrom r x xs → Opens r (lastOf x xs) rest →
      chunks r ((x :: xs) ++ join rest) = (x :: xs) :: rest
  | x, [], _, opens => by
    show glue r x (chunks r (join rest)) = [x] :: rest
    rw [again]
    cases rest with
    | nil => rfl
    | cons g gs =>
      cases g with
      | nil => exact grouped.elim
      | cons y ys =>
        show (if r x y = true then (x :: y :: ys) :: gs else [x] :: (y :: ys) :: gs) = _
        have unlinked : r x y = false := opens
        rw [unlinked]
        rfl
  | x, y :: ys, ⟨link, linked⟩, opens => by
    show glue r x (chunks r ((y :: ys) ++ join rest)) = (x :: y :: ys) :: rest
    rw [chunks_group r grouped again y ys linked opens]
    show (if r x y = true then (x :: y :: ys) :: rest else [x] :: (y :: ys) :: rest) = _
    rw [link]
    rfl

/-- A grouped partition is regrouped as it stands. -/
theorem chunks_of_grouped (r : α → α → Bool) :
    ∀ L : List (List α), Grouped r L → chunks r (join L) = L
  | [], _ => rfl
  | [] :: _, absurd => absurd.elim
  | (x :: xs) :: rest, ⟨linked, opens, grouped⟩ =>
    chunks_group r grouped (chunks_of_grouped r rest grouped) x xs linked opens

/-- **Grouping is exact.** Grouping by `r` returns the partition `L` of its join exactly when
every group of `L` is nonempty and linked inside and no group is linked to the next. -/
theorem chunks_eq_iff (r : α → α → Bool) (L : List (List α)) :
    chunks r (join L) = L ↔ Grouped r L :=
  ⟨fun same => same ▸ grouped_chunks r (join L), chunks_of_grouped r L⟩

/-- **The grouped partition is unique.** -/
theorem chunks_unique (r : α → α → Bool) {L : List (List α)} {xs : List α}
    (grouped : Grouped r L) (joined : join L = xs) : chunks r xs = L :=
  joined ▸ chunks_of_grouped r L grouped

/-! ## Encoded words -/

variable {W : Type v}

/-- A sequence of words, written out. -/
def encode (word : W → List α) (ws : List W) : List α := join (ws.map word)

/-- Each word read as a nonempty group: `word w = first w :: rest w`. -/
def Spelled (word : W → List α) (first : W → α) (rest : W → List α) : Prop :=
  ∀ w, word w = first w :: rest w

theorem grouped_words (r : α → α → Bool) {word : W → List α} {first : W → α}
    {rest : W → List α} (spelled : Spelled word first rest)
    (inside : ∀ w, LinkedFrom r (first w) (rest w))
    (between : ∀ w v, r (lastOf (first w) (rest w)) (first v) = false) :
    ∀ ws : List W, Grouped r (ws.map word)
  | [] => trivial
  | [w] => by
    show Grouped r [word w]
    rw [spelled w]
    exact ⟨inside w, trivial, trivial⟩
  | w :: v :: ws => by
    show Grouped r (word w :: word v :: ws.map word)
    have onward : Grouped r (word v :: ws.map word) := grouped_words r spelled inside between (v :: ws)
    rw [spelled w]
    refine ⟨inside w, ?_, onward⟩
    show Opens r (lastOf (first w) (rest w)) (word v :: ws.map word)
    rw [spelled v]
    exact between w v

/-- **Grouping recovers the words of every encoded sequence exactly when each word is linked
inside and no word's last element is linked to any word's first.** -/
theorem encode_iff (r : α → α → Bool) {word : W → List α} {first : W → α} {rest : W → List α}
    (spelled : Spelled word first rest) :
    (∀ ws, chunks r (encode word ws) = ws.map word) ↔
      (∀ w, LinkedFrom r (first w) (rest w)) ∧
        ∀ w v, r (lastOf (first w) (rest w)) (first v) = false :=
  ⟨fun every =>
    ⟨fun w =>
      have grouped : Grouped r [word w] := (chunks_eq_iff r [word w]).mp (every [w])
      have shaped : Grouped r [first w :: rest w] := spelled w ▸ grouped
      shaped.1,
     fun w v =>
      have grouped : Grouped r [word w, word v] := (chunks_eq_iff r [word w, word v]).mp (every [w, v])
      have shaped : Grouped r [first w :: rest w, first v :: rest v] :=
        spelled v ▸ spelled w ▸ grouped
      shaped.2.1⟩,
   fun ⟨inside, between⟩ ws => chunks_of_grouped r (ws.map word) (grouped_words r spelled inside between ws)⟩

/-! ## Majority bonds -/

/-- Count the elements of a list that satisfy `p`. -/
def countIf {β : Type w} (p : β → Bool) : List β → Nat
  | [] => 0
  | b :: bs => if p b = true then countIf p bs + 1 else countIf p bs

/-- Observed transitions between adjacent observed elements; a gap (`none`) breaks adjacency. -/
def edges : List (Option α) → List (α × α)
  | [] => []
  | x :: rest => edgesFrom x rest
where
  edgesFrom : Option α → List (Option α) → List (α × α)
    | _, [] => []
    | none, y :: rest => edgesFrom y rest
    | some _, none :: rest => edgesFrom none rest
    | some u, some v :: rest => (u, v) :: edgesFrom (some v) rest

section Majority

variable [DecidableEq α]

/-- Transitions observed from `x`. -/
def departures (log : List (Option α)) (x : α) : Nat :=
  countIf (fun e => decide (e.1 = x)) (edges log)

/-- Transitions observed from `x` to `y`. -/
def transitions (log : List (Option α)) (x y : α) : Nat :=
  countIf (fun e => decide (e = (x, y))) (edges log)

/-- `x` is bonded to `y` where more than half the transitions from `x` go to `y`. -/
def bond (log : List (Option α)) (x y : α) : Bool :=
  decide (departures log x < 2 * transitions log x y)

theorem countIf_disjoint {β : Type w} (p q s : β → Bool)
    (apart : ∀ b, p b = true → q b = true → False)
    (underP : ∀ b, p b = true → s b = true) (underQ : ∀ b, q b = true → s b = true) :
    ∀ l : List β, countIf p l + countIf q l ≤ countIf s l
  | [] => Nat.le_refl 0
  | b :: bs => by
    have ih := countIf_disjoint p q s apart underP underQ bs
    show (if p b = true then countIf p bs + 1 else countIf p bs) +
        (if q b = true then countIf q bs + 1 else countIf q bs) ≤
      (if s b = true then countIf s bs + 1 else countIf s bs)
    cases hp : p b with
    | true =>
      cases hq : q b with
      | true => exact (apart b hp hq).elim
      | false =>
        rw [underP b hp]
        show countIf p bs + 1 + countIf q bs ≤ countIf s bs + 1
        rw [Nat.add_right_comm]
        exact Nat.succ_le_succ ih
    | false =>
      cases hq : q b with
      | true =>
        rw [underQ b hq]
        show countIf p bs + (countIf q bs + 1) ≤ countIf s bs + 1
        exact Nat.succ_le_succ ih
      | false =>
        show countIf p bs + countIf q bs ≤ (if s b = true then countIf s bs + 1 else countIf s bs)
        cases s b with
        | true => exact Nat.le_succ_of_le ih
        | false => exact ih

theorem transitions_le (log : List (Option α)) {x y z : α} (different : y ≠ z) :
    transitions log x y + transitions log x z ≤ departures log x :=
  countIf_disjoint (fun e => decide (e = (x, y))) (fun e => decide (e = (x, z)))
    (fun e => decide (e.1 = x))
    (fun _ hy hz => different (congrArg Prod.snd ((of_decide_eq_true hy).symm.trans (of_decide_eq_true hz))))
    (fun _ hy => decide_eq_true (congrArg Prod.fst (of_decide_eq_true hy)))
    (fun _ hz => decide_eq_true (congrArg Prod.fst (of_decide_eq_true hz)))
    (edges log)

theorem lt_of_twice {a b d : Nat} (over : d < 2 * a) (within : a + b ≤ d) : b < a :=
  Nat.lt_of_add_lt_add_left
    (Nat.lt_of_le_of_lt within (Nat.lt_of_lt_of_le over (Nat.le_of_eq (Nat.two_mul a))))

/-- **A majority bond is functional:** each element is bonded to at most one successor. -/
theorem bond_unique (log : List (Option α)) {x y z : α} (toY : bond log x y = true)
    (toZ : bond log x z = true) : y = z :=
  match decEq y z with
  | isTrue same => same
  | isFalse different =>
    have within := transitions_le log (x := x) different
    have within' : transitions log x z + transitions log x y ≤ departures log x :=
      (Nat.add_comm _ _).symm ▸ within
    absurd (lt_of_twice (of_decide_eq_true toY) within)
      (Nat.lt_asymm (lt_of_twice (of_decide_eq_true toZ) within'))

/-- **Where two words continue one element differently inside, no record of transitions groups
every encoded sequence.** -/
theorem no_record_groups {word : W → List α} {first : W → α} {rest : W → List α}
    (spelled : Spelled word first rest) {x y z : α} (different : y ≠ z)
    (hasY : ∀ log : List (Option α), (∀ w, LinkedFrom (bond log) (first w) (rest w)) →
      bond log x y = true)
    (hasZ : ∀ log : List (Option α), (∀ w, LinkedFrom (bond log) (first w) (rest w)) →
      bond log x z = true) (log : List (Option α)) :
    ¬ ∀ ws, chunks (bond log) (encode word ws) = ws.map word :=
  fun every =>
    have inside := ((encode_iff (bond log) spelled).mp every).1
    different (bond_unique log (hasY log inside) (hasZ log inside))

end Majority

/-! ## Reading grouped words -/

variable {M : Type w}

/-- Read each group; `none` where some group is not read. -/
def readAll (res : List α → Option M) : List (List α) → Option (List M)
  | [] => some []
  | g :: gs => (res g).bind fun m => (readAll res gs).bind fun ms => some (m :: ms)

theorem readAll_map_iff (res : List α → Option M) (word : W → List α) (meaning : W → M) :
    ∀ ws : List W, readAll res (ws.map word) = some (ws.map meaning) ↔
      ∀ w, w ∈ ws → res (word w) = some (meaning w)
  | [] => ⟨fun _ _ mem => (nomatch mem), fun _ => rfl⟩
  | w :: ws => by
    have ih := readAll_map_iff res word meaning ws
    constructor
    · intro read
      have read' : (res (word w)).bind (fun m => (readAll res (ws.map word)).bind
          fun ms => some (m :: ms)) = some (meaning w :: ws.map meaning) := read
      cases first : res (word w) with
      | none =>
        rw [first] at read'
        exact nomatch read'
      | some m =>
        rw [first] at read'
        cases others : readAll res (ws.map word) with
        | none =>
          rw [others] at read'
          exact nomatch read'
        | some ms =>
          rw [others] at read'
          have same : m :: ms = meaning w :: ws.map meaning := Option.some.inj read'
          have head : m = meaning w := List.head_eq_of_cons_eq same
          have tail : ms = ws.map meaning := List.tail_eq_of_cons_eq same
          intro v mem
          cases mem with
          | head => exact first.trans (congrArg some head)
          | tail _ mem' => exact (ih.mp (others.trans (congrArg some tail))) v mem'
    · intro every
      show (res (word w)).bind (fun m => (readAll res (ws.map word)).bind
          fun ms => some (m :: ms)) = some (meaning w :: ws.map meaning)
      rw [every w (.head ws), ih.mpr (fun v mem => every v (.tail w mem))]
      rfl

/-- **Where grouping recovers the words, every encoded sequence is read as the meanings of its
words exactly when each word is read as its meaning.** -/
theorem reads_every_iff (r : α → α → Bool) (word : W → List α) (res : List α → Option M)
    (meaning : W → M) (segments : ∀ ws, chunks r (encode word ws) = ws.map word) :
    (∀ ws, readAll res (chunks r (encode word ws)) = some (ws.map meaning)) ↔
      ∀ w, res (word w) = some (meaning w) :=
  ⟨fun every w =>
    have once : readAll res ([w].map word) = some ([w].map meaning) := segments [w] ▸ every [w]
    (readAll_map_iff res word meaning [w]).mp once w (.head []),
   fun each ws => (segments ws).symm ▸
    (readAll_map_iff res word meaning ws).mpr fun w _ => each w⟩

end Becoming.Segmentation
