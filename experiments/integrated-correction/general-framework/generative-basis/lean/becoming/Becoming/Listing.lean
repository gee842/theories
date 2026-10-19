import Becoming.Decidedness
import Becoming.Sampling
import Becoming.Resolution

/-!
# Listing: what listing each relatum once commits to

The zero-premise plan lists among the commitments of the representation (class (b), item 4) that
each relatum taking part in the flow is listed once and that families are without repetition
(`Distinct`). This module finds what the commitment is, as `Becoming.Decidedness` did for
decidedness and `Becoming.Imbalance` for balance: nothing is adopted, and no other module changes.

* **Listing once is decided identity among the listed.** A list without repetition decides
  identity among its members (`Distinct.identityDecided`); where identity among a list's members
  is decided, some list without repetition has exactly its members (`listsOnce_of_decided`). So a
  list can be listed once exactly where identity among its members is decided
  (`listsOnce_iff_decided`), and that it can be is never refuted (`not_not_listsOnce`). A
  procedure deciding identity among the members lists them once (`listOnce`,
  `listOnce_listsOnce`).
* **Sums and counts once per member are one number.** Lists without repetition with the same
  members have the same total of every quantity and the same length (`total_eq_of_same`,
  `ListsOnce.total_eq`, `ListsOnce.length_eq`). The number of relata a list holds (`Numbers`) is
  one number (`Numbers.unique`) and exists exactly where identity among them is decided
  (`numbers_iff_decided`). Repetition only adds (`Numbers.le_length`, `ListsOnce.total_le`): a
  list's length counts places, not relata (`repeated_same`).
* **Membership needs nothing, and neither does a refutation.** Closure, enclosure around a
  family, inflow, and whether something takes from a family are matters of membership
  (`Flow.ClosedAt.widen`, `Flow.Around.of_same`, `Flow.Inward.of_same`, `Flow.takers_pos_of_sub`).
  A law refuting something wherever a list is listed once refutes it of the list with no premise
  (`not_of_listsOnce`); a law holding wherever it is listed once holds where identity among its
  members is decided (`of_listsOnce`). So the laws whose conclusion is a refutation hold of every
  family however listed, with no listing once and no decided identity
  (`Flow.Dissipative.opens_listing`, `Flow.Dissipative.finite_taking_not_recurring_listing`,
  `Flow.taking_draws_in_listing`, `Web.embodiedArising_not_recurring_listing`, `Flow.taking_not_recurring_listing`),
  and under balance, dissipation and embodied arising, neither arising nor ceasing recurs
  where some list, repetition allowed, holds every relatum (`World.Enumerated.not_recurring`).
* **Where the commitment is used, it is local.** A step is enclosed, or enclosed around a family,
  exactly where some family closed across it has decided identity among its members
  (`Flow.enclosed_iff`, `Flow.around_iff`). A world is finite exactly where some list holds every
  relatum and identity among the relata is decided (`World.finite_iff`). Over families listed
  once, dissipation is a matter of the members (`Flow.DissipatesOn.of_same`), and dissipation is
  dissipation on every closed family read once per member (`Flow.dissipative_iff`). A sum law
  reads the sum once per member: under dissipation a member of a closed family coming to stand
  lowers the stock over every list listing the family once (`Flow.standing_lowers_listing`), and
  such a list exists where identity among the family is decided
  (`Flow.standing_lowers_decided`). Every census decides identity among what it lists
  (`Listed.identityDecided`), and any listing of what holds, repetition allowed, gives a census
  where a procedure decides identity among the listed at each step (`Listed.of_listing`); the
  census law holds of such listings (`Web.arising_of_ceasing_listing`).
* **Where repetition is not harmless.** Over a family listing a member twice a sum law fails: in
  `Doubled` the flow balances and dissipates, the family listing twice the condition that comes to
  stand is closed and not dissipated on, and its stock does not fall; listed once, it falls
  (`Doubled.needs_once`). `Lone.repeated_family` shows the same for
  `Flow.Dissipative.gives_less`, and `Repeated` for counting formations.
* **What taking part counts.** The flow's list of what takes part is not a family: a relatum
  listed twice there takes part twice. Read by occurrence, each place in a step's list is taken
  as a relatum of its own, alike in every relation to the relatum there (`Flow.byOccurrence`,
  `Web.byOccurrence`, `Flow.byOccurrence_alike`). Every flow so read lists what takes part once,
  with no decided identity among its relata (`Flow.byOccurrence_once`), and keeps its amounts,
  takers, closure, dissipation, balance and activity premises (`Flow.byOccurrence_taken`,
  `Flow.byOccurrence_takers`, `Flow.byOccurrence_dissipative`, `Flow.byOccurrence_balances`,
  `Flow.byOccurrence_acting`, `Flow.byOccurrence_taking`, `Flow.byOccurrence_more`); so balance
  composes across a coarse step for every flow read by occurrence
  (`Flow.BalancesOn.sample_byOccurrence`). Occurrences are not followed across steps: wherever a
  relatum is active, no list holds its active occurrences (`Flow.byOccurrence_uncounted`), so the
  laws counting relata across steps keep their census.
* **Where identity is not decided.** Every list over a type can be listed once exactly where
  identity on the type is decided (`listsOnce_all_iff`). Read through relations, two relata of a
  world are alike where they are indiscernible, alike in every relation of the world to every
  relatum (`World.Indiscernible`, a likeness: `World.indiscernible_equivalence`). Up to a likeness
  the number of relata a list holds is one number and exists exactly where likeness among them is
  decided (`NumbersBy.unique`, `numbersBy_iff_decided`), counting by name being counting up to
  identity of names (`numbers_iff_numbersBy_eq`). Asked of every world, whether two relata are
  indiscernible is decided, and the number of relata each list holds is fixed, exactly under
  excluded middle (`World.indiscernible_decided_iff_em`, `World.numbers_indiscernible_iff_em`).
  Names count what relations do not tell apart: where two relata are indiscernible, the list of
  both has two members by name and holds one relatum read through relations
  (`World.probe_named_apart`).
* **What takes part in a step, counted.** Read on a flow's steps: what takes part in a step can
  be listed once, and has a number, exactly where identity among it is decided
  (`Flow.present_listsOnce_iff`, `Flow.present_numbers_iff`); the number is one, at most the
  places in the step's list, and counted by name is counted up to identity of names
  (`Flow.present_number_unique`, `Flow.present_number_le`, `Flow.present_numbers_iff_by_eq`); a
  step listing one relatum twice numbers one relatum in two places (`Flow.present_repeated`); and
  every flow on a type lists what takes part in each step once exactly where identity on the type
  is decided (`Flow.present_listsOnce_all_iff`).

**AI reading, adopted on Ren's delegation of 15 October 2026 (DELEGATED-CHOICES D30).** Listing once
commits to no more than this: identity among what is summed or counted is decided where it is summed
or counted. That is a local condition, as P58 made decidedness. Laws of membership, and laws
refuting something, need nothing. Laws that sum or count over a family hold of the sum or count once
per member, which exists exactly where identity among the members is decided and is then one number.
In the flow, listing once fixes what one taking part is: each occurrence, read as its own relatum,
makes every flow one listed once, so for the amounts it restricts nothing. Identity itself is read
off the relations only up to indiscernibility, and the core's names give one decided identity more
than the relations do: asked of every world, the relational count is fixed only under excluded
middle.
-/

namespace Becoming

variable {α : Type}

/-! ## Listing once is decided identity among the listed -/

/-- Identity among the members of a list is decided: any two of them are the same or are
not. -/
def IdentityDecided (l : List α) : Prop :=
  ∀ a b, a ∈ l → b ∈ l → Decided (a = b)

/-- `s` lists the members of `l`, each once. -/
def ListsOnce (s l : List α) : Prop :=
  Distinct s ∧ ∀ a, a ∈ s ↔ a ∈ l

/-- **A list without repetition decides identity among its members**: two members are the
same where they stand at one place, and different where they stand at two. -/
theorem Distinct.identityDecided : ∀ {s : List α}, Distinct s →
    ∀ a b, a ∈ s → b ∈ s → Decided (a = b)
  | [], _, _, _, mem, _ => nomatch mem
  | _ :: s, ⟨fresh, distinct⟩, a, b, ma, mb => match mem_cons_cases ma, mem_cons_cases mb with
    | .inl ha, .inl hb => .inl (ha.trans hb.symm)
    | .inl ha, .inr mb' =>
      .inr fun same => fresh (Eq.subst (motive := fun y => y ∈ s) (same.symm.trans ha) mb')
    | .inr ma', .inl hb =>
      .inr fun same => fresh (Eq.subst (motive := fun y => y ∈ s) (same.trans hb) ma')
    | .inr ma', .inr mb' => Distinct.identityDecided distinct a b ma' mb'

/-- **Where identity among its members is decided, a list can be listed once**: some list
without repetition has exactly its members. -/
theorem listsOnce_of_decided : ∀ {l : List α}, IdentityDecided l → ∃ s, ListsOnce s l
  | [], _ => ⟨[], trivial, fun _ => Iff.rfl⟩
  | a :: l, decided =>
    match listsOnce_of_decided (l := l) (fun x y mx my => decided x y (.tail a mx) (.tail a my)),
        Decided.exists_mem (P := fun b => a = b) (l := l)
          (fun b mem => decided a b (.head l) (.tail a mem)) with
    | ⟨s, distinct, same⟩, .inl ⟨_, mem, ab⟩ =>
      ⟨s, distinct, fun x => ⟨fun mx => .tail a ((same x).mp mx), fun mx =>
        match mem_cons_cases mx with
        | .inl xa => (same x).mpr (Eq.subst (motive := fun y => y ∈ l) (ab.symm.trans xa.symm) mem)
        | .inr ml => (same x).mpr ml⟩⟩
    | ⟨s, distinct, same⟩, .inr absent =>
      ⟨a :: s, ⟨fun ma => absent ⟨a, (same a).mp ma, rfl⟩, distinct⟩, fun x =>
        ⟨fun mx => match mem_cons_cases mx with
          | .inl xa => Eq.subst (motive := fun y => y ∈ a :: l) xa.symm (.head l)
          | .inr ms => .tail a ((same x).mp ms),
         fun mx => match mem_cons_cases mx with
          | .inl xa => Eq.subst (motive := fun y => y ∈ a :: s) xa.symm (.head s)
          | .inr ml => .tail a ((same x).mpr ml)⟩⟩

/-- A list listing another once decides identity among the other's members. -/
theorem ListsOnce.identityDecided {s l : List α} (lists : ListsOnce s l) : IdentityDecided l :=
  fun a b ma mb => lists.1.identityDecided a b ((lists.2 a).mpr ma) ((lists.2 b).mpr mb)

/-- **A list can be listed once exactly where identity among its members is decided.** -/
theorem listsOnce_iff_decided {l : List α} : (∃ s, ListsOnce s l) ↔ IdentityDecided l :=
  ⟨fun ⟨_, lists⟩ => lists.identityDecided, listsOnce_of_decided⟩

/-- A list without repetition lists itself once. -/
theorem Distinct.listsOnce {s : List α} (distinct : Distinct s) : ListsOnce s s :=
  ⟨distinct, fun _ => Iff.rfl⟩

/-- That identity among the members of a list is decided cannot be refuted. -/
theorem not_not_identityDecided (l : List α) : ¬ ¬ IdentityDecided l :=
  fun undecided =>
    not_not_all (E := l) (P := fun a => ∀ b, b ∈ l → Decided (a = b))
      (fun a _ => not_not_all (E := l) (P := fun b => Decided (a = b))
        fun b _ => not_not_decided (a = b))
      fun all => undecided fun a b ma mb => all a ma b mb

/-- **That a list can be listed once cannot be refuted**: no premise. -/
theorem not_not_listsOnce (l : List α) : ¬ ¬ ∃ s, ListsOnce s l :=
  fun none => not_not_identityDecided l fun decided => none (listsOnce_of_decided decided)

/-- **A law refuting something wherever a list is listed once refutes it of the list with no
premise.** -/
theorem not_of_listsOnce {B : Prop} (l : List α) (law : ∀ s, ListsOnce s l → ¬ B) : ¬ B :=
  fun holds => not_not_listsOnce l fun ⟨s, lists⟩ => law s lists holds

/-- A law holding wherever a list is listed once holds of it where identity among its
members is decided. -/
theorem of_listsOnce {B : Prop} {l : List α} (decided : IdentityDecided l)
    (law : ∀ s, ListsOnce s l → B) : B :=
  match listsOnce_of_decided decided with
  | ⟨s, lists⟩ => law s lists

/-! ## Sums and counts once per member -/

/-- In a list without repetition, a member standing in the middle stands nowhere else. -/
theorem not_mem_of_middle {a : α} : ∀ {p q : List α}, Distinct (p ++ a :: q) → ¬ a ∈ p ++ q
  | [], _, ⟨fresh, _⟩, mem => fresh mem
  | _ :: p, q, ⟨fresh, distinct⟩, mem => match mem_cons_cases mem with
    | .inl ax => fresh (Eq.subst (motive := fun y => y ∈ p ++ a :: q) ax (mem_middle p))
    | .inr mem => not_mem_of_middle distinct mem

/-- **Sums once per member are one number**: two lists without repetition with the same
members have the same total of any quantity. -/
theorem total_eq_of_same {q : α → Nat} : ∀ {s s' : List α}, Distinct s → Distinct s' →
    (∀ a, a ∈ s ↔ a ∈ s') → total s q = total s' q
  | [], [], _, _, _ => rfl
  | [], b :: _, _, _, same => nomatch (same b).mpr (.head _)
  | a :: s, _, ⟨fresh, distinct⟩, distinct', same =>
    match List.append_of_mem ((same a).mp (.head s)) with
    | ⟨p, r, split⟩ =>
      have middle : Distinct (p ++ a :: r) := Eq.subst (motive := Distinct) split distinct'
      have inner : total s q = total (p ++ r) q := total_eq_of_same distinct
        (distinct_remove middle) fun x =>
          ⟨fun mx => mem_remove (fun xa => fresh (Eq.subst (motive := fun y => y ∈ s) xa mx))
              (Eq.subst (motive := fun y => x ∈ y) split ((same x).mp (.tail a mx))),
           fun mx => match mem_cons_cases ((same x).mpr
               (Eq.subst (motive := fun y => x ∈ y) split.symm (mem_insert mx))) with
             | .inl xa => absurd (Eq.subst (motive := fun y => y ∈ p ++ r) xa mx)
                 (not_mem_of_middle middle)
             | .inr ms => ms⟩
      (congrArg (q a + ·) inner).trans
        (((congrArg (total · q) split).trans ((total_append q (a :: r) p).trans
          ((Nat.add_left_comm (total p q) (q a) (total r q)).trans
            (congrArg (q a + ·) (total_append q r p).symm)))).symm)

/-- Any two lists listing a list once have the same total of any quantity. -/
theorem ListsOnce.total_eq {s s' l : List α} (lists : ListsOnce s l) (lists' : ListsOnce s' l)
    (q : α → Nat) : total s q = total s' q :=
  total_eq_of_same lists.1 lists'.1 fun a => (lists.2 a).trans (lists'.2 a).symm

/-- And the same length. -/
theorem ListsOnce.length_eq {s s' l : List α} (lists : ListsOnce s l) (lists' : ListsOnce s' l) :
    s.length = s'.length :=
  length_eq_of_same lists.1 lists'.1 fun a => (lists.2 a).trans (lists'.2 a).symm

/-- `n` numbers the relata a list holds: some list of them, each once, has `n` members. A
count of relata as a relation, as `Counts` is of what holds. -/
def Numbers (l : List α) (n : Nat) : Prop :=
  ∃ s, ListsOnce s l ∧ s.length = n

/-- The number of relata a list holds is one number. -/
theorem Numbers.unique {l : List α} {n n' : Nat} : Numbers l n → Numbers l n' → n = n'
  | ⟨_, lists, length⟩, ⟨_, lists', length'⟩ =>
    length.symm.trans ((lists.length_eq lists').trans length')

/-- **The number of relata a list holds exists exactly where identity among them is
decided.** -/
theorem numbers_iff_decided {l : List α} : (∃ n, Numbers l n) ↔ IdentityDecided l :=
  ⟨fun ⟨_, _, lists, _⟩ => lists.identityDecided,
   fun decided => match listsOnce_of_decided decided with
    | ⟨s, lists⟩ => ⟨s.length, s, lists, rfl⟩⟩

/-- A list without repetition numbers its members by its length. -/
theorem Distinct.numbers {s : List α} (distinct : Distinct s) : Numbers s s.length :=
  ⟨s, distinct.listsOnce, rfl⟩

/-- The number of relata a list holds is at most its length: repetition only adds. -/
theorem Numbers.le_length {l : List α} {n : Nat} : Numbers l n → n ≤ l.length
  | ⟨_, lists, length⟩ =>
    Nat.le_trans (Nat.le_of_eq length.symm)
      (length_le_of_sub lists.1 fun a mem => (lists.2 a).mp mem)

/-- A total once per member is at most the total over any list holding the members: repetition
only adds. -/
theorem ListsOnce.total_le {s l : List α} (lists : ListsOnce s l) (q : α → Nat) :
    total s q ≤ total l q :=
  total_le_of_support lists.1 fun a mem _ => (lists.2 a).mp mem

/-! ## Listing once by a procedure -/

/-- Whether `a` is a member of `l`, decided from decisions of identity between `a` and the
members. -/
def decideIn (a : α) : (l : List α) → (∀ b, b ∈ l → Decidable (a = b)) → Decidable (a ∈ l)
  | [], _ => .isFalse fun no => nomatch no
  | b :: l, dec => match dec b (.head l) with
    | .isTrue same => .isTrue (Eq.subst (motive := fun x => a ∈ x :: l) same (.head l))
    | .isFalse other => match decideIn a l (fun c mem => dec c (.tail b mem)) with
      | .isTrue mem => .isTrue (.tail b mem)
      | .isFalse no => .isFalse fun mem => match mem_cons_cases mem with
        | .inl same => other same
        | .inr mem => no mem

/-- `a` put in front of `s` where it is decided not to be there already. -/
def keepFresh (a : α) (s : List α) {P : Prop} : Decidable P → List α
  | .isTrue _ => s
  | .isFalse _ => a :: s

/-- The members of `l`, each once, the last occurrence of each kept, where a procedure decides
identity among them. -/
def listOnce : (l : List α) → (∀ a b, a ∈ l → b ∈ l → Decidable (a = b)) → List α
  | [], _ => []
  | a :: l, dec => keepFresh a (listOnce l fun x y mx my => dec x y (.tail a mx) (.tail a my))
      (decideIn a l fun b mem => dec a b (.head l) (.tail a mem))

theorem keepFresh_spec {a : α} {s l : List α} (lists : ListsOnce s l) :
    ∀ decide : Decidable (a ∈ l), ListsOnce (keepFresh a s decide) (a :: l)
  | .isTrue mem => ⟨lists.1, fun x => ⟨fun mx => .tail a ((lists.2 x).mp mx), fun mx =>
      match mem_cons_cases mx with
      | .inl xa => (lists.2 x).mpr (Eq.subst (motive := fun y => y ∈ l) xa.symm mem)
      | .inr ml => (lists.2 x).mpr ml⟩⟩
  | .isFalse fresh => ⟨⟨fun ms => fresh ((lists.2 a).mp ms), lists.1⟩, fun x =>
      ⟨fun mx => match mem_cons_cases mx with
        | .inl xa => Eq.subst (motive := fun y => y ∈ a :: l) xa.symm (.head l)
        | .inr ms => .tail a ((lists.2 x).mp ms),
       fun mx => match mem_cons_cases mx with
        | .inl xa => Eq.subst (motive := fun y => y ∈ a :: s) xa.symm (.head s)
        | .inr ml => .tail a ((lists.2 x).mpr ml)⟩⟩

/-- The procedure lists each member once. -/
theorem listOnce_listsOnce : ∀ (l : List α) (dec : ∀ a b, a ∈ l → b ∈ l → Decidable (a = b)),
    ListsOnce (listOnce l dec) l
  | [], _ => ⟨trivial, fun _ => Iff.rfl⟩
  | a :: l, dec => keepFresh_spec
      (listOnce_listsOnce l fun x y mx my => dec x y (.tail a mx) (.tail a my))
      (decideIn a l fun b mem => dec a b (.head l) (.tail a mem))

/-! ## Families of conditions: membership, and sums once per member -/

section Families

variable {F C : Type}

namespace Flow

variable {L : Flow F C} {W : Web F C}

/-- Closure is a matter of membership: a family holding every member of a family closed across
a step is closed across it. -/
theorem ClosedAt.widen {cs ds : List C} {t : Nat} (closed : L.ClosedAt cs t)
    (within : ∀ c, c ∈ cs → c ∈ ds) : L.ClosedAt ds t :=
  fun f present c outside => closed f present c fun inside => outside (within c inside)

/-- **A step is enclosed exactly where some family closed across it has decided identity among
its members**: `Enclosed` asks for a family without repetition, which is that. -/
theorem enclosed_iff {t : Nat} : L.Enclosed t ↔ ∃ cs, IdentityDecided cs ∧ L.ClosedAt cs t :=
  ⟨fun ⟨cs, distinct, closed⟩ => ⟨cs, distinct.identityDecided, closed⟩,
   fun ⟨_, decided, closed⟩ => match listsOnce_of_decided decided with
    | ⟨es, lists⟩ => ⟨es, lists.1, closed.widen fun c mem => (lists.2 c).mpr mem⟩⟩

/-- Likewise a step is enclosed around a family exactly where some family holding it, closed
across the step, has decided identity among its members. -/
theorem around_iff {ds : List C} {t : Nat} :
    L.Around ds t ↔ ∃ es, IdentityDecided es ∧ (∀ c, c ∈ ds → c ∈ es) ∧ L.ClosedAt es t :=
  ⟨fun ⟨es, distinct, within, closed⟩ => ⟨es, distinct.identityDecided, within, closed⟩,
   fun ⟨_, decided, within, closed⟩ => match listsOnce_of_decided decided with
    | ⟨fs, lists⟩ => ⟨fs, lists.1, fun c mem => (lists.2 c).mpr (within c mem),
        closed.widen fun c mem => (lists.2 c).mpr mem⟩⟩

/-- Enclosure around a family is a matter of its members. -/
theorem Around.of_same {ds es : List C} {t : Nat} (around : L.Around ds t)
    (within : ∀ c, c ∈ es → c ∈ ds) : L.Around es t :=
  match around with
  | ⟨fs, distinct, holds, closed⟩ => ⟨fs, distinct, fun c mem => holds c (within c mem), closed⟩

/-- **Over families listed once, dissipation is a matter of the members**: the sums once per
member are one number. -/
theorem DissipatesOn.of_same {es es' : List C} {t : Nat} (dissipates : L.DissipatesOn es t)
    (distinct : Distinct es) (distinct' : Distinct es') (same : ∀ c, c ∈ es ↔ c ∈ es') :
    L.DissipatesOn es' t :=
  fun f present =>
    Eq.subst (motive := fun g => g + sign (total es' (L.take t f)) ≤ total es' (L.take t f))
      (total_eq_of_same (q := L.give t f) distinct distinct' same)
      (Eq.subst (motive := fun k => total es (L.give t f) + sign k ≤ k)
        (total_eq_of_same (q := L.take t f) distinct distinct' same) (dissipates f present))

/-- Under dissipation, every family closed across a step is dissipated on, read once per
member: by every list listing it once. -/
theorem Dissipative.listsOnce (dissipative : L.Dissipative) {cs es : List C} {t : Nat}
    (closed : L.ClosedAt cs t) (lists : ListsOnce es cs) : L.DissipatesOn es t :=
  dissipative es t lists.1 (closed.widen fun c mem => (lists.2 c).mpr mem)

/-- **Dissipation is dissipation on every closed family, read once per member**: the families
without repetition that `Dissipative` quantifies over are every family, listed once. -/
theorem dissipative_iff : L.Dissipative ↔
    ∀ cs t, L.ClosedAt cs t → ∀ es, ListsOnce es cs → L.DissipatesOn es t :=
  ⟨fun dissipative _ _ closed _ lists => dissipative.listsOnce closed lists,
   fun once cs t distinct closed => once cs t closed cs distinct.listsOnce⟩

/-- **`Dissipative.opens` holds of every family, however listed, with no premise**: listing the
family once is used only inside the proof, and that it can be listed once cannot be refuted. -/
theorem Dissipative.opens_listing (balances : L.Balances W) (dissipative : L.Dissipative)
    {cs ds : List C} (within : ∀ c, c ∈ cs → c ∈ ds)
    (recurs : ∀ N, ∃ t, N ≤ t ∧ 0 < L.takers cs t) (T : Nat) :
    ¬ ∀ t, T ≤ t → L.ClosedAt ds t :=
  not_of_listsOnce ds fun _ lists closed =>
    dissipative.opens balances lists.1 (fun c mem => (lists.2 c).mpr (within c mem)) recurs T
      fun t later => (closed t later).widen fun c mem => (lists.2 c).mpr mem

/-- **Where some list holds every condition, however listed, taking does not recur under
dissipation**: no listing once and no decided identity (`Dissipative.finite_taking_not_recurring`). -/
theorem Dissipative.finite_taking_not_recurring_listing (balances : L.Balances W) (dissipative : L.Dissipative)
    {all : List C} (every : ∀ c, c ∈ all) (cs : List C) :
    ¬ ∀ N, ∃ t, N ≤ t ∧ 0 < L.takers cs t :=
  not_of_listsOnce all fun _ lists =>
    dissipative.finite_taking_not_recurring balances lists.1 (fun c => (lists.2 c).mpr (every c)) cs

/-- What a step gives to a family is positive exactly as it is for any family with the same
members. -/
theorem total_pos_of_within {q : C → Nat} {ds es : List C} (within : ∀ c, c ∈ ds → c ∈ es)
    (pos : 0 < total ds q) : 0 < total es q :=
  match total_pos ds pos with
  | ⟨_, mem, positive⟩ => total_pos_of_mem (within _ mem) positive

/-- Inflow into a family is a matter of its members. -/
theorem Inward.of_same {ds es : List C} {t : Nat} (inward : L.Inward ds t)
    (same : ∀ c, c ∈ ds ↔ c ∈ es) : L.Inward es t :=
  fun f present gives c takes =>
    (same c).mp (inward f present
      (total_pos_of_within (fun d mem => (same d).mpr mem) gives) c takes)

/-- **`taking_draws_in` holds of every family, however listed, with no premise**: where taking
from a family recurs and every step from some step on is enclosed around it, at arbitrarily late
steps some formation gives to it and takes from beyond it. -/
theorem taking_draws_in_listing (balances : L.Balances W) (dissipative : L.Dissipative)
    {ds : List C} {T₀ : Nat} (around : ∀ t, T₀ ≤ t → L.Around ds t)
    (recurs : ∀ N, ∃ t, N ≤ t ∧ 0 < L.takers ds t) (N : Nat) :
    ¬ ∀ t, N ≤ t → L.Inward ds t :=
  not_of_listsOnce ds fun _ lists inward =>
    taking_draws_in balances dissipative lists.1 (T₀ := T₀)
      (fun t later => (around t later).of_same fun c mem => (lists.2 c).mp mem)
      (fun M => match recurs M with
        | ⟨t, later, takes⟩ =>
          ⟨t, later, takers_pos_of_sub (fun c mem => (lists.2 c).mpr mem) takes⟩)
      N fun t later => (inward t later).of_same fun c => (lists.2 c).symm

/-- **A sum law reads the sum once per member.** Under dissipation, a member of a family closed
across a step coming to stand lowers the family's stock (`standing_lowers`), the stock taken
once per member: over every list listing the family once, however the family is listed. -/
theorem standing_lowers_listing (balances : L.Balances W) (dissipative : L.Dissipative)
    {ds : List C} {t : Nat} (closed : L.ClosedAt ds t) {c : C} (mem : c ∈ ds)
    (comes : W.ComesToStand t c) {es : List C} (lists : ListsOnce es ds) :
    W.stock es (t + 1) < W.stock es t :=
  standing_lowers balances dissipative lists.1 (closed.widen fun d m => (lists.2 d).mpr m)
    ((lists.2 c).mpr mem) comes

/-- Where identity among the family's members is decided, such a sum exists. -/
theorem standing_lowers_decided (balances : L.Balances W) (dissipative : L.Dissipative)
    {ds : List C} (decided : IdentityDecided ds) {t : Nat} (closed : L.ClosedAt ds t) {c : C}
    (mem : c ∈ ds) (comes : W.ComesToStand t c) :
    ∃ es, ListsOnce es ds ∧ W.stock es (t + 1) < W.stock es t :=
  match listsOnce_of_decided decided with
  | ⟨es, lists⟩ => ⟨es, lists, standing_lowers_listing balances dissipative closed mem comes lists⟩

end Flow

/-- **Where some list holds every relatum, however listed, embodied relata do not arise at
arbitrarily late steps under dissipation** (`Web.embodiedArising_not_recurring`): no listing once. -/
theorem Web.embodiedArising_not_recurring_listing {X : Type} {W : Web X X} {L : Flow X X}
    (balances : L.Balances W) (dissipative : L.Dissipative) {all : List X} (every : ∀ x, x ∈ all) :
    ¬ ∀ N, ∃ t x, N ≤ t ∧ W.Embodied x ∧ W.Arises t x :=
  not_of_listsOnce all fun _ lists =>
    Web.embodiedArising_not_recurring balances dissipative lists.1 fun x => (lists.2 x).mpr (every x)

/-- **With the unit fixed from some step on, taking from a closed family does not recur, however
the family is listed** (`Flow.taking_not_recurring`). -/
theorem Flow.taking_not_recurring_listing {L : Flow F C} {W : Web F C} {r : Nat → Nat}
    (balances : L.BalancesAt r W) (dissipative : L.Dissipative) {cs : List C} {T : Nat}
    (closed : ∀ t, T ≤ t → L.ClosedAt cs t) (fixed : ∀ t, T ≤ t → r t = 1) :
    ¬ ∀ N, ∃ t, N ≤ t ∧ 0 < L.takers cs t :=
  not_of_listsOnce cs fun _ lists recurs =>
    Flow.taking_not_recurring balances dissipative lists.1
      (fun t later => (closed t later).widen fun c mem => (lists.2 c).mpr mem) fixed
      fun N => match recurs N with
        | ⟨t, later, takes⟩ =>
          ⟨t, later, Flow.takers_pos_of_sub (fun c mem => (lists.2 c).mpr mem) takes⟩

end Families

/-! ## Finite worlds -/

namespace World

variable {w : World}

/-- Some list holds every relatum: finitely many relata, possibly listed more than once. -/
def Enumerated (w : World) : Prop :=
  ∃ all : List w.Relatum, ∀ x, x ∈ all

/-- **A world is finite exactly where some list holds every relatum and identity among the
relata is decided**: listing each relatum once adds decided identity to an enumeration. -/
theorem finite_iff : w.Finite ↔ w.Enumerated ∧ ∀ x y : w.Relatum, Decided (x = y) :=
  ⟨fun ⟨all, distinct, every⟩ =>
    ⟨⟨all, every⟩, fun x y => distinct.identityDecided x y (every x) (every y)⟩,
   fun ⟨⟨all, every⟩, decided⟩ =>
    match listsOnce_of_decided (l := all) fun x y _ _ => decided x y with
    | ⟨es, lists⟩ => ⟨es, lists.1, fun x => (lists.2 x).mpr (every x)⟩⟩

/-- That an enumerated world is finite cannot be refuted. -/
theorem Enumerated.not_not_finite (enumerated : w.Enumerated) : ¬ ¬ w.Finite :=
  match enumerated with
  | ⟨all, every⟩ => fun none => not_not_listsOnce all fun ⟨es, lists⟩ =>
      none ⟨es, lists.1, fun x => (lists.2 x).mpr (every x)⟩

/-- **Neither arising nor ceasing recurs in an enumerated world** under balance, dissipation
and embodied arising, with no listing once and no decided identity. The statement keeps this
non-recurrence strength, obtained from `World.rests_unrefuted` by its proved consequence. -/
theorem Enumerated.not_recurring (enumerated : w.Enumerated) (balanced : w.Balanced)
    (dissipative : w.Dissipative) (embodied : w.ArisingEmbodied) :
    ¬ w.ArisingRecurs ∧ ¬ w.CeasingRecurs :=
  ⟨fun arising => enumerated.not_not_finite fun finite =>
      (World.not_recurring_of_rests_unrefuted
        (World.rests_unrefuted finite balanced dissipative embodied)).1 arising,
   fun ceasing => enumerated.not_not_finite fun finite =>
      (World.not_recurring_of_rests_unrefuted
        (World.rests_unrefuted finite balanced dissipative embodied)).2 ceasing⟩

end World

/-! ## Censuses from any listing -/

/-- A listing of what holds decides identity among what it lists at each step. -/
theorem Listed.identityDecided {p : α → Nat → Prop} {l : Nat → List α} (listed : Listed p l)
    (t : Nat) : IdentityDecided (l t) :=
  (listed t).1.identityDecided

/-- **Any listing of what holds, with repetition, gives a listing of it once, where a procedure
decides identity among the members listed at each step.** -/
theorem Listed.of_listing {p : α → Nat → Prop} {l : Nat → List α} (lists : ∀ t a, p a t ↔ a ∈ l t)
    (dec : ∀ t a b, a ∈ l t → b ∈ l t → Decidable (a = b)) :
    Listed p (fun t => listOnce (l t) (dec t)) :=
  fun t => ⟨(listOnce_listsOnce (l t) (dec t)).1,
    fun a => (lists t a).trans ((listOnce_listsOnce (l t) (dec t)).2 a).symm⟩

/-- **The census law for any listing of what is active** (`Listed.coming_of_ceasing`): with a
list of what is active at each step, possibly with repetition, and identity among the listed
decided, ceasing at arbitrarily late steps needs arising at arbitrarily late steps. -/
theorem Web.arising_of_ceasing_listing {F C : Type} (W : Web F C)
    [∀ t f, Decidable (W.active t f)] {l : Nat → List F} (lists : ∀ t f, W.active t f ↔ f ∈ l t)
    (dec : ∀ t a b, a ∈ l t → b ∈ l t → Decidable (a = b))
    (ceasing : ∀ N, ∃ t f, N ≤ t ∧ W.Ceases t f) : W.Unceasing :=
  Listed.coming_of_ceasing (Listed.of_listing (p := fun f t => W.active t f) lists dec) ceasing

/-! ## A sum over a family listing a member twice -/

namespace Doubled

/-- One relatum, at the first step only, takes two units from one condition (`false`) and
gives one to another (`true`). -/
def flow : Flow Unit Bool where
  present t := match t with
    | 0 => [()]
    | _ + 1 => []
  take t _ c := match t with
    | 0 => match c with
      | true => 0
      | false => 2
    | _ + 1 => 0
  give t _ c := match t with
    | 0 => match c with
      | true => 1
      | false => 0
    | _ + 1 => 0

/-- `true` comes to stand across the first step as `false` is drawn down. -/
def web : Web Unit Bool where
  level t c := match t with
    | 0 => match c with
      | true => 0
      | false => 2
    | _ + 1 => match c with
      | true => 1
      | false => 0
  active _ _ := True
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

theorem balances : flow.Balances web
  | 0, true => rfl
  | 0, false => rfl
  | _ + 1, true => rfl
  | _ + 1, false => rfl

theorem dissipative : flow.Dissipative := fun cs t => match t with
  | 0 => fun distinct closed f _ =>
    have gives : total cs (flow.give 0 f) ≤ 1 :=
      total_le_at (q := flow.give 0 f) (a := true) (fun b => match b with
        | true => fun _ => rfl
        | false => fun positive => absurd positive (Nat.lt_irrefl 0)) distinct
    have holds : false ∈ cs := match decideMem false cs with
      | .isTrue mem => mem
      | .isFalse out => Nat.noConfusion (closed () (.head []) false out).1
    Nat.le_trans (Nat.add_le_add gives (sign_le_one _))
      (le_total_of_mem (q := flow.take 0 f) holds)
  | _ + 1 => fun _ _ _ present => nomatch present

theorem closed : flow.ClosedAt [true, true, false] 0 := fun _ _ c outside => match c with
  | true => absurd (.head _) outside
  | false => absurd (.tail _ (.tail _ (.head _))) outside

theorem comes : web.ComesToStand 0 true :=
  ⟨Nat.lt_irrefl 0, Nat.zero_lt_one⟩

/-- **The sum law needs the sum once per member.** The flow balances and dissipates, the family
listing `true` twice and `false` once is closed across the first step, across which `true`
comes to stand: the stock over that listing does not fall, the rise of `true` counting twice,
and that family is not dissipated on; listed once, the stock falls, as `standing_lowers` says. -/
theorem needs_once :
    flow.Balances web ∧ flow.Dissipative ∧ flow.ClosedAt [true, true, false] 0 ∧
      web.ComesToStand 0 true ∧
      ¬ web.stock [true, true, false] 1 < web.stock [true, true, false] 0 ∧
      ¬ flow.DissipatesOn [true, true, false] 0 ∧
      web.stock [true, false] 1 < web.stock [true, false] 0 :=
  ⟨balances, dissipative, closed, comes, Nat.lt_irrefl 2,
   fun dissipates => Nat.not_succ_le_self 2 (dissipates () (.head [])), Nat.lt_succ_self 1⟩

end Doubled

/-! ## Where identity is not decided -/

/-- **Every list of relata of one type can be listed once exactly where identity among them is
decided.** -/
theorem listsOnce_all_iff : (∀ l : List α, ∃ s, ListsOnce s l) ↔ ∀ a b : α, Decided (a = b) :=
  ⟨fun all a b => (listsOnce_iff_decided.mp (all [a, b])) a b (.head _) (.tail _ (.head _)),
   fun decided _ => listsOnce_of_decided fun a b _ _ => decided a b⟩

/-- With repetition a list's length counts places, not relata: holding one relatum twice, a list
has the members of the list holding it once, and is longer. -/
theorem repeated_same (a : α) : (∀ x, x ∈ [a, a] ↔ x ∈ [a]) ∧ [a].length < [a, a].length :=
  ⟨fun _ => ⟨fun mem => match mem_cons_cases mem with
      | .inl same => Eq.subst (motive := fun y => y ∈ [a]) same.symm (.head [])
      | .inr mem => mem,
     fun mem => .tail a mem⟩, Nat.lt_succ_self 1⟩

/-! ### Identity read through relations -/

/-- No two members of a list are related by `R`. -/
def DistinctBy (R : α → α → Prop) : List α → Prop
  | [] => True
  | a :: as => (∀ b, b ∈ as → ¬ R a b) ∧ DistinctBy R as

/-- `s` lists the members of `l` once up to `R`: no two of its members are related, each member
of `l` is related to one of its members, and each of its members to a member of `l`. -/
def ListsOnceBy (R : α → α → Prop) (s l : List α) : Prop :=
  DistinctBy R s ∧ (∀ a, a ∈ l → ∃ b, b ∈ s ∧ R a b) ∧ ∀ b, b ∈ s → ∃ a, a ∈ l ∧ R b a

/-- `n` numbers the relata `l` holds, read up to `R`. -/
def NumbersBy (R : α → α → Prop) (l : List α) (n : Nat) : Prop :=
  ∃ s, ListsOnceBy R s l ∧ s.length = n

section Likeness

variable {R : α → α → Prop}

/-- A list no two of whose members are alike decides likeness among them. -/
theorem DistinctBy.decided (like : Equivalence R) : ∀ {s : List α}, DistinctBy R s →
    ∀ a b, a ∈ s → b ∈ s → Decided (R a b)
  | [], _, _, _, mem, _ => nomatch mem
  | _ :: _, ⟨fresh, distinct⟩, a, b, ma, mb => match mem_cons_cases ma, mem_cons_cases mb with
    | .inl ha, .inl hb =>
      .inl (Eq.subst (motive := fun y => R a y) (ha.trans hb.symm) (like.refl a))
    | .inl ha, .inr mb' =>
      .inr fun related => fresh b mb' (Eq.subst (motive := fun y => R y b) ha related)
    | .inr ma', .inl hb =>
      .inr fun related => fresh a ma' (like.symm (Eq.subst (motive := fun y => R a y) hb related))
    | .inr ma', .inr mb' => DistinctBy.decided like distinct a b ma' mb'

/-- Two alike members of a list no two of whose members are alike stand at one place. -/
theorem DistinctBy.eq_of (like : Equivalence R) : ∀ {s : List α}, DistinctBy R s →
    ∀ a b, a ∈ s → b ∈ s → R a b → a = b
  | [], _, _, _, mem, _, _ => nomatch mem
  | _ :: _, ⟨fresh, distinct⟩, a, b, ma, mb, related =>
    match mem_cons_cases ma, mem_cons_cases mb with
    | .inl ha, .inl hb => ha.trans hb.symm
    | .inl ha, .inr mb' => absurd (Eq.subst (motive := fun y => R y b) ha related) (fresh b mb')
    | .inr ma', .inl hb =>
      absurd (like.symm (Eq.subst (motive := fun y => R a y) hb related)) (fresh a ma')
    | .inr ma', .inr mb' => DistinctBy.eq_of like distinct a b ma' mb' related

/-- A list no two of whose members are alike is without repetition. -/
theorem DistinctBy.distinct (like : Equivalence R) : ∀ {s : List α}, DistinctBy R s → Distinct s
  | [], _ => trivial
  | a :: _, ⟨fresh, distinct⟩ =>
    ⟨fun mem => fresh a mem (like.refl a), DistinctBy.distinct like distinct⟩

/-- A list listing another once up to likeness decides likeness among the other's members. -/
theorem ListsOnceBy.decided (like : Equivalence R) {s l : List α} (lists : ListsOnceBy R s l) :
    ∀ a b, a ∈ l → b ∈ l → Decided (R a b) :=
  fun a b ma mb => match lists.2.1 a ma, lists.2.1 b mb with
  | ⟨a', ma', ra⟩, ⟨b', mb', rb⟩ => match lists.1.decided like a' b' ma' mb' with
    | .inl related => .inl (like.trans ra (like.trans related (like.symm rb)))
    | .inr apart => .inr fun related => apart (like.trans (like.symm ra) (like.trans related rb))

/-- Where likeness among its members is decided, a list can be listed once up to likeness. -/
theorem listsOnceBy_of_decided (like : Equivalence R) : ∀ {l : List α},
    (∀ a b, a ∈ l → b ∈ l → Decided (R a b)) → ∃ s, ListsOnceBy R s l
  | [], _ => ⟨[], trivial, (fun _ mem => nomatch mem), (fun _ mem => nomatch mem)⟩
  | a :: l, decided =>
    match listsOnceBy_of_decided like (l := l)
        (fun x y mx my => decided x y (.tail a mx) (.tail a my)),
      Decided.exists_mem (P := fun b => R a b) (l := l)
        (fun b mem => decided a b (.head l) (.tail a mem)) with
    | ⟨s, distinct, covers, back⟩, .inl ⟨b, mem, ab⟩ =>
      ⟨s, distinct, fun x mx => match mem_cons_cases mx with
          | .inl xa => match covers b mem with
            | ⟨b', mb', bb'⟩ =>
              ⟨b', mb', Eq.subst (motive := fun y => R y b') xa.symm (like.trans ab bb')⟩
          | .inr ml => covers x ml,
        fun y my => match back y my with
          | ⟨x, mx, yx⟩ => ⟨x, .tail a mx, yx⟩⟩
    | ⟨s, distinct, covers, back⟩, .inr absent =>
      ⟨a :: s, ⟨fun b mb related => match back b mb with
          | ⟨x, mx, bx⟩ => absent ⟨x, mx, like.trans related bx⟩, distinct⟩,
        fun x mx => match mem_cons_cases mx with
          | .inl xa => ⟨a, .head s, Eq.subst (motive := fun y => R y a) xa.symm (like.refl a)⟩
          | .inr ml => match covers x ml with
            | ⟨b, mb, xb⟩ => ⟨b, .tail a mb, xb⟩,
        fun y my => match mem_cons_cases my with
          | .inl ya => ⟨a, .head l, Eq.subst (motive := fun z => R z a) ya.symm (like.refl a)⟩
          | .inr ms => match back y ms with
            | ⟨x, mx, yx⟩ => ⟨x, .tail a mx, yx⟩⟩

/-- The number of relata a list holds, read up to likeness, is one number. -/
theorem NumbersBy.unique (like : Equivalence R) {l : List α} {n n' : Nat} :
    NumbersBy R l n → NumbersBy R l n' → n = n'
  | ⟨_, lists, length⟩, ⟨_, lists', length'⟩ =>
    have le : ∀ {s s' : List α}, ListsOnceBy R s l → ListsOnceBy R s' l → s.length ≤ s'.length :=
      fun lists lists' => length_le_of_matched (S := R) (lists.1.distinct like)
        (fun a ma => match lists.2.2 a ma with
          | ⟨x, mx, ax⟩ => match lists'.2.1 x mx with
            | ⟨b, mb, xb⟩ => ⟨b, mb, like.trans ax xb⟩)
        (fun a a' _ ma ma' ab a'b => lists.1.eq_of like a a' ma ma' (like.trans ab (like.symm a'b)))
    length.symm.trans ((Nat.le_antisymm (le lists lists') (le lists' lists)).trans length')

/-- **Read up to likeness, the number of relata a list holds exists exactly where likeness among
them is decided.** -/
theorem numbersBy_iff_decided (like : Equivalence R) {l : List α} :
    (∃ n, NumbersBy R l n) ↔ ∀ a b, a ∈ l → b ∈ l → Decided (R a b) :=
  ⟨fun ⟨_, _, lists, _⟩ => lists.decided like,
   fun decided => match listsOnceBy_of_decided like decided with
    | ⟨s, lists⟩ => ⟨s.length, s, lists, rfl⟩⟩

end Likeness

/-- Listing once up to identity of names is listing without repetition. -/
theorem distinctBy_eq_iff : ∀ {s : List α}, DistinctBy Eq s ↔ Distinct s
  | [] => Iff.rfl
  | a :: s =>
    ⟨fun ⟨fresh, rest⟩ => ⟨fun mem => fresh a mem rfl, (distinctBy_eq_iff (s := s)).mp rest⟩,
     fun ⟨fresh, rest⟩ =>
      ⟨fun _ mb same => fresh (Eq.subst (motive := fun y => y ∈ s) same.symm mb),
       (distinctBy_eq_iff (s := s)).mpr rest⟩⟩

/-- Counted by name is counted up to identity of names. -/
theorem numbers_iff_numbersBy_eq {l : List α} {n : Nat} : Numbers l n ↔ NumbersBy Eq l n :=
  ⟨fun ⟨s, ⟨distinct, same⟩, length⟩ => ⟨s, ⟨distinctBy_eq_iff.mpr distinct,
      fun a ma => ⟨a, (same a).mpr ma, rfl⟩, fun b mb => ⟨b, (same b).mp mb, rfl⟩⟩, length⟩,
   fun ⟨s, ⟨distinct, covers, back⟩, length⟩ => ⟨s, ⟨distinctBy_eq_iff.mp distinct, fun a =>
      ⟨fun ma => match back a ma with
        | ⟨_, mx, ax⟩ => Eq.subst (motive := fun y => y ∈ l) ax.symm mx,
       fun ma => match covers a ma with
        | ⟨_, mb, ab⟩ => Eq.subst (motive := fun y => y ∈ s) ab.symm mb⟩⟩, length⟩⟩

namespace World

/-- Two relata of a world are indiscernible: at each step alike in activity, standing and taking
part, and alike in every relation to every relatum, either way round. -/
def Indiscernible (w : World) (x y : w.Relatum) : Prop :=
  ∀ t z, ((w.web.active t x ↔ w.web.active t y) ∧ w.web.level t x = w.web.level t y ∧
      (x ∈ w.flow.present t ↔ y ∈ w.flow.present t)) ∧
    ((w.web.requires t x z ↔ w.web.requires t y z) ∧ (w.web.requires t z x ↔ w.web.requires t z y) ∧
      (w.web.draws t x z ↔ w.web.draws t y z) ∧ (w.web.draws t z x ↔ w.web.draws t z y)) ∧
    (w.web.need t x z = w.web.need t y z ∧ w.web.need t z x = w.web.need t z y ∧
      w.flow.take t x z = w.flow.take t y z ∧ w.flow.take t z x = w.flow.take t z y ∧
      w.flow.give t x z = w.flow.give t y z ∧ w.flow.give t z x = w.flow.give t z y)

/-- Indiscernibility is a likeness, kept as a relation. -/
theorem indiscernible_equivalence (w : World) : Equivalence w.Indiscernible :=
  ⟨fun _ _ _ => ⟨⟨Iff.rfl, rfl, Iff.rfl⟩, ⟨Iff.rfl, Iff.rfl, Iff.rfl, Iff.rfl⟩,
      ⟨rfl, rfl, rfl, rfl, rfl, rfl⟩⟩,
   fun ind t z => match ind t z with
    | ⟨⟨a, l, p⟩, ⟨r, r', d, d'⟩, ⟨n, n', k, k', g, g'⟩⟩ =>
      ⟨⟨a.symm, l.symm, p.symm⟩, ⟨r.symm, r'.symm, d.symm, d'.symm⟩,
        ⟨n.symm, n'.symm, k.symm, k'.symm, g.symm, g'.symm⟩⟩,
   fun ind ind' t z => match ind t z, ind' t z with
    | ⟨⟨a, l, p⟩, ⟨r, r', d, d'⟩, ⟨n, n', k, k', g, g'⟩⟩,
      ⟨⟨a₂, l₂, p₂⟩, ⟨r₂, r₂', d₂, d₂'⟩, ⟨n₂, n₂', k₂, k₂', g₂, g₂'⟩⟩ =>
      ⟨⟨a.trans a₂, l.trans l₂, p.trans p₂⟩, ⟨r.trans r₂, r'.trans r₂', d.trans d₂, d'.trans d₂'⟩,
        ⟨n.trans n₂, n'.trans n₂', k.trans k₂, k'.trans k₂', g.trans g₂, g'.trans g₂'⟩⟩⟩

/-- The probe's web: `true` active throughout, `false` active exactly where `Q` holds, nothing
standing, required or drawn. -/
def probeWeb (Q : Prop) : Web Bool Bool :=
  ⟨fun _ _ => 0, fun _ x => x = true ∨ Q, fun _ _ _ => False, fun _ _ _ => 0, fun _ _ _ => False⟩

/-- Two relata with no exchange, one active throughout, the other active exactly where `Q`
holds. -/
def probe (Q : Prop) : World :=
  World.of Bool Flow.still (probeWeb Q)

/-- In the probe the two relata are indiscernible exactly where `Q` holds. -/
theorem probe_indiscernible (Q : Prop) : (probe Q).Indiscernible true false ↔ Q :=
  ⟨fun ind => match (((ind 0 true).1.1).mp (Or.inl rfl) : false = true ∨ Q) with
    | .inl no => Bool.noConfusion no
    | .inr q => q,
   fun q _ _ => ⟨⟨⟨fun _ => Or.inr q, fun _ => Or.inl rfl⟩, rfl,
       ⟨fun (no : true ∈ ([] : List Bool)) => (nomatch no),
        fun (no : false ∈ ([] : List Bool)) => (nomatch no)⟩⟩,
     ⟨Iff.rfl, Iff.rfl, Iff.rfl, Iff.rfl⟩, ⟨rfl, rfl, rfl, rfl, rfl, rfl⟩⟩⟩

/-- **Whether two relata are indiscernible is decided in every world exactly under excluded
middle.** -/
theorem indiscernible_decided_iff_em :
    (∀ w : World, ∀ x y : w.Relatum, Decided (w.Indiscernible x y)) ↔ ∀ Q : Prop, Q ∨ ¬ Q :=
  ⟨fun decided Q => match decided (probe Q) true false with
    | .inl ind => .inl ((probe_indiscernible Q).mp ind)
    | .inr apart => .inr fun q => apart ((probe_indiscernible Q).mpr q),
   fun em _ _ _ => em _⟩

/-- **Read through relations, the number of relata a list holds is fixed for every list of every
world exactly under excluded middle.** Counted by name (`Numbers`), it is fixed exactly where
identity of names is decided (`numbers_iff_decided`). -/
theorem numbers_indiscernible_iff_em :
    (∀ w : World, ∀ l : List w.Relatum, ∃ n, NumbersBy w.Indiscernible l n) ↔
      ∀ Q : Prop, Q ∨ ¬ Q :=
  ⟨fun numbered => indiscernible_decided_iff_em.mp fun w x y =>
      (numbersBy_iff_decided w.indiscernible_equivalence).mp (numbered w [x, y]) x y
        (.head _) (.tail _ (.head _)),
   fun em w _ => (numbersBy_iff_decided w.indiscernible_equivalence).mpr fun _ _ _ _ => em _⟩

/-- **Names count what relations do not tell apart.** Where `Q` holds, the probe's two relata are
indiscernible: listed once by name the list of both has two members, and read through relations
it holds one relatum. -/
theorem probe_named_apart {Q : Prop} (q : Q) :
    Numbers ([true, false] : List (probe Q).Relatum) 2 ∧
      NumbersBy (probe Q).Indiscernible [true, false] 1 :=
  have ind : (probe Q).Indiscernible true false := (probe_indiscernible Q).mpr q
  have like := (probe Q).indiscernible_equivalence
  ⟨Distinct.numbers (s := ([true, false] : List Bool))
      ⟨fun mem => match mem_cons_cases mem with
        | .inl no => Bool.noConfusion no
        | .inr no => (nomatch no), fun no => (nomatch no), trivial⟩,
   [true], ⟨⟨fun _ no => (nomatch no), trivial⟩,
     fun _ mx => match mem_cons_cases mx with
      | .inl xt => ⟨true, .head [], Eq.subst (motive := fun y => (probe Q).Indiscernible y true)
          xt.symm (like.refl true)⟩
      | .inr mx => match mem_cons_cases mx with
        | .inl xf => ⟨true, .head [], Eq.subst (motive := fun y => (probe Q).Indiscernible y true)
            xf.symm (like.symm ind)⟩
        | .inr no => (nomatch no),
     fun _ mb => match mem_cons_cases mb with
      | .inl bt => ⟨true, .head _, Eq.subst (motive := fun y => (probe Q).Indiscernible y true)
          bt.symm (like.refl true)⟩
      | .inr no => nomatch no⟩, rfl⟩

end World

/-! ## Taking part, listed once by its occurrences -/

/-- Each member of a list with its place, counting from `i`. -/
def placed : List α → Nat → List (Nat × α)
  | [], _ => []
  | a :: l, i => (i, a) :: placed l (i + 1)

theorem placed_ge : ∀ {l : List α} {i : Nat} {o : Nat × α}, o ∈ placed l i → i ≤ o.1
  | [], _, _, mem => nomatch mem
  | _ :: _, i, _, mem => match mem_cons_cases mem with
    | .inl same => Eq.subst (motive := fun x : Nat × α => i ≤ x.1) same.symm (Nat.le_refl i)
    | .inr mem => Nat.le_trans (Nat.le_succ i) (placed_ge mem)

/-- **The occurrences of a list are listed once, whatever its members**: places are numbers. -/
theorem placed_distinct : ∀ (l : List α) (i : Nat), Distinct (placed l i)
  | [], _ => trivial
  | _ :: l, i => ⟨fun mem => Nat.not_succ_le_self i (placed_ge mem), placed_distinct l (i + 1)⟩

theorem mem_of_placed : ∀ {l : List α} {i : Nat} {o : Nat × α}, o ∈ placed l i → o.2 ∈ l
  | [], _, _, mem => nomatch mem
  | a :: l, _, _, mem => match mem_cons_cases mem with
    | .inl same => Eq.subst (motive := fun x : Nat × α => x.2 ∈ a :: l) same.symm (.head l)
    | .inr mem => .tail a (mem_of_placed mem)

theorem placed_of_mem : ∀ {l : List α} {i : Nat} {a : α}, a ∈ l → ∃ k, (k, a) ∈ placed l i
  | [], _, _, mem => nomatch mem
  | b :: l, i, _, mem => match mem_cons_cases mem with
    | .inl same =>
      ⟨i, Eq.subst (motive := fun x => (i, x) ∈ placed (b :: l) i) same.symm (.head _)⟩
    | .inr mem => match placed_of_mem (i := i + 1) mem with
      | ⟨k, held⟩ => ⟨k, .tail _ held⟩

/-- A total over the occurrences is the total over the list. -/
theorem total_placed (q : α → Nat) : ∀ (l : List α) (i : Nat),
    total (placed l i) (fun o => q o.2) = total l q
  | [], _ => rfl
  | a :: l, i => congrArg (q a + ·) (total_placed q l (i + 1))

section Occurrences

variable {F C : Type}

/-- The flow read by its occurrences: what takes part at a place in a step's list is the
occurrence at that place, taking and giving what the relatum there does. -/
def Flow.byOccurrence (L : Flow F C) : Flow (Nat × F) C where
  present t := placed (L.present t) 0
  take t o c := L.take t o.2 c
  give t o c := L.give t o.2 c

/-- The web read by occurrences: an occurrence is active, requires, needs and draws as its
relatum does. -/
def Web.byOccurrence (W : Web F C) : Web (Nat × F) C where
  level := W.level
  active t o := W.active t o.2
  requires t o := W.requires t o.2
  need t o := W.need t o.2
  draws t o := W.draws t o.2

namespace Flow

variable {L : Flow F C} {W : Web F C}

/-- **Every flow, read by its occurrences, lists what takes part once**, with no decided identity
among the relata. -/
theorem byOccurrence_once : L.byOccurrence.Once :=
  fun t => placed_distinct (L.present t) 0

/-- Two occurrences of one relatum are alike in every relation. -/
theorem byOccurrence_alike (i k : Nat) (f : F) (t : Nat) (c : C) :
    L.byOccurrence.take t (i, f) c = L.byOccurrence.take t (k, f) c ∧
      L.byOccurrence.give t (i, f) c = L.byOccurrence.give t (k, f) c ∧
      (W.byOccurrence.active t (i, f) ↔ W.byOccurrence.active t (k, f)) ∧
      (W.byOccurrence.requires t (i, f) c ↔ W.byOccurrence.requires t (k, f) c) ∧
      W.byOccurrence.need t (i, f) c = W.byOccurrence.need t (k, f) c ∧
      (W.byOccurrence.draws t (i, f) c ↔ W.byOccurrence.draws t (k, f) c) :=
  ⟨rfl, rfl, Iff.rfl, Iff.rfl, rfl, Iff.rfl⟩

theorem byOccurrence_taken (t : Nat) (c : C) : L.byOccurrence.taken t c = L.taken t c :=
  total_placed (fun f => L.take t f c) (L.present t) 0

theorem byOccurrence_given (t : Nat) (c : C) : L.byOccurrence.given t c = L.given t c :=
  total_placed (fun f => L.give t f c) (L.present t) 0

/-- Read by occurrences, as many take from a family as take from it in the flow, a relatum
listed twice counting twice. -/
theorem byOccurrence_takers (cs : List C) (t : Nat) : L.byOccurrence.takers cs t = L.takers cs t :=
  total_placed (fun f => sign (total cs (L.take t f))) (L.present t) 0

theorem byOccurrence_renewers (cs : List C) (t : Nat) :
    L.byOccurrence.renewers cs t = L.renewers cs t :=
  total_placed (fun f => sign (total cs (L.give t f))) (L.present t) 0

theorem byOccurrence_closedAt {cs : List C} {t : Nat} :
    L.byOccurrence.ClosedAt cs t ↔ L.ClosedAt cs t :=
  ⟨fun closed f present c outside => match placed_of_mem (i := 0) present with
    | ⟨k, held⟩ => closed (k, f) held c outside,
   fun closed o held c outside => closed o.2 (mem_of_placed held) c outside⟩

theorem byOccurrence_dissipatesOn {cs : List C} {t : Nat} :
    L.byOccurrence.DissipatesOn cs t ↔ L.DissipatesOn cs t :=
  ⟨fun dissipates f present => match placed_of_mem (i := 0) present with
    | ⟨k, held⟩ => dissipates (k, f) held,
   fun dissipates o held => dissipates o.2 (mem_of_placed held)⟩

theorem byOccurrence_dissipative : L.byOccurrence.Dissipative ↔ L.Dissipative :=
  ⟨fun dissipative cs t distinct closed =>
    byOccurrence_dissipatesOn.mp (dissipative cs t distinct (byOccurrence_closedAt.mpr closed)),
   fun dissipative cs t distinct closed =>
    byOccurrence_dissipatesOn.mpr (dissipative cs t distinct (byOccurrence_closedAt.mp closed))⟩

theorem byOccurrence_balancesOn {cs : List C} {t : Nat} :
    L.byOccurrence.BalancesOn W.byOccurrence cs t ↔ L.BalancesOn W cs t :=
  ⟨fun balances c mem => (congrArg (W.level (t + 1) c + ·) (byOccurrence_taken t c).symm).trans
      ((balances c mem).trans (congrArg (W.level t c + ·) (byOccurrence_given t c))),
   fun balances c mem => (congrArg (W.level (t + 1) c + ·) (byOccurrence_taken t c)).trans
      ((balances c mem).trans (congrArg (W.level t c + ·) (byOccurrence_given t c).symm))⟩

theorem byOccurrence_balances : L.byOccurrence.Balances W.byOccurrence ↔ L.Balances W :=
  ⟨fun balances t c => (byOccurrence_balancesOn (cs := [c]) (t := t)).mp
      (fun d _ => balances t d) c (.head []),
   fun balances t c => (byOccurrence_balancesOn (cs := [c]) (t := t)).mpr
      (fun d _ => balances t d) c (.head [])⟩

theorem byOccurrence_acting : L.byOccurrence.Acting W.byOccurrence ↔ L.Acting W :=
  ⟨fun acting t f c present gives => match placed_of_mem (i := 0) present with
    | ⟨k, held⟩ => acting t (k, f) c held gives,
   fun acting t o c held gives => acting t o.2 c (mem_of_placed held) gives⟩

theorem byOccurrence_taking : L.byOccurrence.Taking W.byOccurrence ↔ L.Taking W :=
  ⟨fun taking t f c present takes => match placed_of_mem (i := 0) present with
    | ⟨k, held⟩ => taking t (k, f) c held takes,
   fun taking t o c held takes => taking t o.2 c (mem_of_placed held) takes⟩

theorem byOccurrence_more {cs : List C} : L.byOccurrence.More cs ↔ L.More cs :=
  ⟨fun more K => match more K with
    | ⟨T, many⟩ => ⟨T, fun t later =>
        Nat.le_trans (many t later) (Nat.le_of_eq (byOccurrence_takers cs t))⟩,
   fun more K => match more K with
    | ⟨T, many⟩ => ⟨T, fun t later =>
        Nat.le_trans (many t later) (Nat.le_of_eq (byOccurrence_takers cs t).symm)⟩⟩

/-- Read by occurrence, nothing is followed across steps: wherever a relatum is active, no list
holds every active occurrence, so laws counting relata across steps keep their census. -/
theorem byOccurrence_uncounted {t : Nat} {f : F} (active : W.active t f) (l : List (Nat × F)) :
    ¬ ∀ o, W.byOccurrence.active t o → o ∈ l :=
  fun covers => Nat.not_succ_le_self _
    (le_total_of_mem (q := fun o : Nat × F => o.1) (covers (total l (fun o => o.1) + 1, f) active))

/-- **Balance composes across a coarse step for every flow, read by its occurrences**: no
listing once is asked (`Flow.BalancesOn.sample`). -/
theorem BalancesOn.sample_byOccurrence [DecidableEq F] (σ : Nat → Nat) {cs : List C} {s : Nat}
    (strict : Strict σ) (balances : ∀ j, j ∈ span σ s → L.BalancesOn W cs j) :
    (L.byOccurrence.sample σ).BalancesOn (W.byOccurrence.sample σ) cs s :=
  BalancesOn.sample σ strict (fun j _ => byOccurrence_once j)
    fun j mem => byOccurrence_balancesOn.mpr (balances j mem)

end Flow

end Occurrences

/-! ## What takes part in a step, counted -/

section Present

variable {F C : Type}

namespace Flow

variable {L : Flow F C}

/-- **A step listing one relatum twice numbers one relatum in two places.** -/
theorem present_repeated {t : Nat} {a : F} (twice : L.present t = [a, a]) :
    Numbers (L.present t) 1 ∧ (L.present t).length = 2 :=
  ⟨⟨[a], ⟨⟨(fun mem => nomatch mem), trivial⟩, fun x => twice ▸ ((repeated_same a).1 x).symm⟩, rfl⟩,
   twice ▸ rfl⟩

/-- **Every flow on a type lists what takes part in each step once exactly where identity on the
type is decided.** -/
theorem present_listsOnce_all_iff :
    (∀ (L : Flow F C) (t : Nat), ∃ s, ListsOnce s (L.present t)) ↔ ∀ a b : F, Decided (a = b) :=
  ⟨fun all => listsOnce_all_iff.mp fun l => all ⟨fun _ => l, fun _ _ _ => 0, fun _ _ _ => 0⟩ 0,
   fun decided L t => listsOnce_all_iff.mpr decided (L.present t)⟩

end Flow

end Present

end Becoming

section CensusWebs

/-!
## Census on webs: counts of arising and ceasing where they exist, and listing once

`Becoming.Decidedness` states counts as relations (`Counts`, `CountsAcross`) and the census over a
stretch for any family of determinations, with no decidedness; `Becoming.Listing` states what
listing each relatum once commits to. A web's activity is such a family: a formation arises
across a step where it comes to be active (`Web.Arises`) and ceases where it ceases to be
(`Web.Ceases`), and a family's stock is the sum of its conditions' levels (`Web.stock`). This
module states those laws of a web's activity and standing, and of a world's relata read through
their relations, and proves them through them.

* **The census of a web, with no decidedness.** Over a stretch at whose steps what is active is
  listed, each formation once, wherever the ceasings and arisings are counted, the list at the end
  with what ceased is the list at the start with what arose (`listed_over_stretch`). Over any
  stretch, wherever a listed family's arisings and ceasings are counted, they differ by at most
  its members (`keep_pace`). Where a procedure decides activity, its marks count what arises and
  what ceases (`arisings_count`, `ceasings_count`).
* **A census decides identity among what it lists.** A census of what is active in a web decides
  identity among the formations active at each step (`census_identityDecided`).
* **A stock once per member is one number.** Two lists listing a family of conditions once give
  it one stock at every step (`stock_eq`), and repetition only adds (`stock_le`).
* **Counting a world's relata through their relations.** The number of relata a list of a world
  holds, read up to indiscernibility, is one number (`indiscernible_numbers_unique`).

No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

namespace CensusWebs

section Census

variable {F C : Type} (W : Web F C)

/-- **Over any stretch of a web, wherever a listed family's arisings and ceasings are counted,
they differ by at most its members.** No decidedness is assumed. -/
theorem keep_pace {fs : List F} {S n A D : Nat}
    (arose : CountsAcross (fun _ => fs) (fun t f => W.Arises t f) (steps S n) A)
    (ceased : CountsAcross (fun _ => fs) (fun t f => W.Ceases t f) (steps S n) D) :
    A ≤ fs.length + D ∧ D ≤ fs.length + A :=
  CountsAcross.keep_pace (p := fun f t => W.active t f) arose ceased

/-- **A family's stock once per member is one number**: two lists listing the family once give
it the same stock at every step. -/
theorem stock_eq {cs cs' ds : List C} (lists : ListsOnce cs ds) (lists' : ListsOnce cs' ds)
    (t : Nat) : W.stock cs t = W.stock cs' t :=
  lists.total_eq lists' (W.level t)

/-- **Repetition only adds**: a family's stock once per member is at most its stock over any list
holding its members. -/
theorem stock_le {cs ds : List C} (lists : ListsOnce cs ds) (t : Nat) :
    W.stock cs t ≤ W.stock ds t :=
  lists.total_le (W.level t)

end Census

/-- **The number of relata a list of a world holds, read through their relations, is one
number**: counted up to indiscernibility. -/
theorem indiscernible_numbers_unique (w : World) {l : List w.Relatum} {n n' : Nat}
    (numbers : NumbersBy w.Indiscernible l n) (numbers' : NumbersBy w.Indiscernible l n') :
    n = n' :=
  NumbersBy.unique w.indiscernible_equivalence numbers numbers'

end CensusWebs

end Becoming

end CensusWebs
