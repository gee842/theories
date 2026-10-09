import Becoming.Change

/-!
# Population: counting the formations that take part

`Becoming.Generation` reads arising through the activity of formations across steps;
`Becoming.Flow` counts the formations that take from a family. This module reads how
many formations are active at each step, and ties the flow's count to the web's.

* A *census* lists the formations active at each step, each once (`Census`).
* If more formations are active after a step than before, some formation active after
  the step was not active before: it arises across the step (`arises_of_more`). A
  census that grows without bound makes generation unceasing (`unceasing_of_growth`).
* The census law: where the members of which a determination holds are listed at each
  step, each once (`Listed`), the list after a step with the members that ceased to be
  is the list before it with the members that came to be (`Listed.across`), and so over
  any stretch (`Listed.over_stretch`): ceasings are at most comings and the list at the
  start, comings at most ceasings and the list at the end (`Listed.ceasings_within`,
  `Listed.comings_within`). Read of recurrence, the balance is exact: ceasing to be
  recurs exactly when, from each step, the list at some later step is shorter than the
  list at the start with what came to be between, and coming to be recurs exactly when
  the list at the start is longer than some later list with what ceased to be between
  (`Listed.ceasing_iff_shortfall`, `Listed.coming_iff_excess`). Ceasings that recur
  accumulate past any list at the start, so ceasing to be at arbitrarily late steps needs
  coming to be at arbitrarily late steps (`Listed.coming_of_ceasing`). Not conversely:
  ever new formations can arise while none ceases (`Dawn`). Where at most `K` are listed
  at arbitrarily late steps, comings that recur accumulate past `K`, and the converse
  holds too (`Listed.ceasing_of_returning`); so where from some step on at most `B` are
  listed, the two recur together (`Listed.ceasing_of_coming`,
  `Listed.coming_iff_ceasing`). This needs only a list returning within a bound, not the
  finite family of `Becoming.Change` (`coming_recurs_iff`). Where the list grows without
  end, ceasing to be still recurs where, from each step, the comings over some stretch
  outnumber a bound on the list at its end (`Listed.ceasing_of_outpacing`). A census is
  the listing of activity: the formations active at the end with those that ceased are
  those active at the start with those that arose (`Web.Census.over_stretch`), ceasing
  recurring needs arising recurring (`Web.arising_of_ceasing`), and under a census
  bounded from some step on arising recurs exactly when ceasing recurs
  (`Web.unceasing_iff_bounded`). Read of dependence, forming and dissolving obey the
  same balance and laws (`Web.DependenceCensus.over_stretch`,
  `Web.DependenceCensus.forming_of_dissolving`,
  `Web.DependenceCensus.forming_iff_dissolving`); `Becoming.Openness` reads them of
  standing.
* Under a census, with each formation taking part in the flow listed once and only
  active formations taking (`Flow.Taking`, of which only the activity half is used),
  the active formations grow without bound (`Flow.More.grows`), and more without end
  makes generation unceasing (`Flow.More.unceasing`). The premises hold together in the
  garden and the cycle (`Garden.counted`, `Cycle.counted`). Not conversely: the bloom
  meets every one of these premises, arises again and again, and is not more
  (`Bloom.counted`). Under this correspondence, more without end is strictly stronger
  than unceasing generation.
* Each premise does work. Without a census, every formation of an infinite family can be
  active from the start, and more without end comes with nothing arising (`Dormant`).
  Without `Taking`, the flow's takers need not be active: one formation gives to ever
  more formations that take while never active, and nothing arises (`Inactive`). With a
  formation listed many times in a flow's `present`, one formation counts as many: more
  without end comes with one formation, always active, and nothing arising
  (`Repeated`).
* The converse of `Taking`, that every formation drawing on the family takes from it in
  the flow, is an application duty: ever more formations can be active, depend on a
  condition and draw on it while the flow records no taking (`Crowd`).

Activity at each step is supposed decidable where a theorem needs it; this is a
hypothesis of the theorem, not an axiom. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

variable {α β : Type}

/-! ## Lists without repetition -/

/-- A list in which no member occurs twice. -/
def Distinct : List α → Prop
  | [] => True
  | a :: as => ¬ a ∈ as ∧ Distinct as

theorem length_append : ∀ p q : List α, (p ++ q).length = p.length + q.length
  | [], _ => (Nat.zero_add _).symm
  | _ :: p, q => (congrArg Nat.succ (length_append p q)).trans (Nat.succ_add _ _).symm

theorem mem_cons_cases {a b : α} {q : List α} : b ∈ a :: q → b = a ∨ b ∈ q
  | .head _ => .inl rfl
  | .tail _ mem => .inr mem

theorem mem_map_of {g : α → β} {a : α} : ∀ {l : List α}, a ∈ l → g a ∈ l.map g
  | _ :: _, .head _ => .head _
  | _ :: _, .tail _ mem => .tail _ (mem_map_of mem)

theorem mem_of_map {g : α → β} (inj : ∀ a b, g a = g b → a = b) {a : α} :
    ∀ {l : List α}, g a ∈ l.map g → a ∈ l
  | [], mem => nomatch mem
  | b :: _, mem => match mem_cons_cases mem with
    | .inl same => Eq.subst (motive := fun x => x ∈ b :: _) (inj a b same).symm (.head _)
    | .inr mem => .tail b (mem_of_map inj mem)

/-- Mapping a list one to one keeps it without repetition. -/
theorem distinct_map {g : α → β} (inj : ∀ a b, g a = g b → a = b) :
    ∀ {l : List α}, Distinct l → Distinct (l.map g)
  | [], _ => trivial
  | _ :: _, ⟨fresh, distinct⟩ => ⟨fun mem => fresh (mem_of_map inj mem), distinct_map inj distinct⟩

/-- Removing one occurrence of `a` keeps every other member. -/
theorem mem_remove {a b : α} (other : ¬ b = a) : ∀ {p q : List α}, b ∈ p ++ a :: q → b ∈ p ++ q
  | [], _, mem => match mem_cons_cases mem with
    | .inl same => absurd same other
    | .inr mem => mem
  | c :: _, _, mem => match mem_cons_cases mem with
    | .inl same => Eq.subst (motive := fun x => x ∈ c :: _) same.symm (.head _)
    | .inr mem => .tail _ (mem_remove other mem)

/-- A list without repetition, each member of which is matched to a member of another
list, no member of which is matched to two: the first list is no longer. -/
theorem length_le_of_matched {S : α → β → Prop} : ∀ {l : List α} {m : List β}, Distinct l →
    (∀ a, a ∈ l → ∃ b, b ∈ m ∧ S a b) →
    (∀ a a' b, a ∈ l → a' ∈ l → S a b → S a' b → a = a') → l.length ≤ m.length
  | [], _, _, _, _ => Nat.zero_le _
  | a :: l, m, ⟨fresh, distinct⟩, matched, once => match matched a (.head l) with
    | ⟨b, mem, paired⟩ => match List.append_of_mem mem with
      | ⟨p, q, split⟩ =>
        have inner : l.length ≤ (p ++ q).length :=
          length_le_of_matched distinct
            (fun a' mem' => match matched a' (.tail a mem') with
              | ⟨b', mem_b', paired'⟩ =>
                have other : ¬ b' = b := fun same =>
                  fresh (Eq.subst (motive := fun x => x ∈ l)
                    (once a' a b' (.tail a mem') (.head l) paired'
                      (Eq.subst (motive := fun x => S a x) same.symm paired)) mem')
                ⟨b', mem_remove other (split ▸ mem_b'), paired'⟩)
            (fun x y b' mx my => once x y b' (.tail a mx) (.tail a my))
        have whole : m.length = (p ++ q).length + 1 :=
          (congrArg List.length split).trans ((length_append p (b :: q)).trans
            ((Nat.add_succ _ _).trans (congrArg Nat.succ (length_append p q).symm)))
        whole ▸ Nat.succ_le_succ inner

/-- A list without repetition whose members all belong to another list is no longer. -/
theorem length_le_of_sub {l m : List α} (distinct : Distinct l) (sub : ∀ a, a ∈ l → a ∈ m) :
    l.length ≤ m.length :=
  length_le_of_matched (S := Eq) distinct (fun a mem => ⟨a, sub a mem, rfl⟩)
    fun _ _ _ _ _ same same' => same.trans same'.symm

/-- Counting the members a quantity is positive at, in a list without repetition: no more
than a list holding every such member. -/
theorem count_le_of_sub {q : α → Nat} : ∀ {l m : List α}, Distinct l →
    (∀ a, a ∈ l → 0 < q a → a ∈ m) → count l q ≤ m.length
  | [], _, _, _ => Nat.zero_le _
  | a :: l, m, ⟨fresh, distinct⟩, sub => match h : q a with
    | 0 =>
      have rest : count l q ≤ m.length :=
        count_le_of_sub distinct fun b mem => sub b (.tail a mem)
      show sign (q a) + count l q ≤ m.length from
        (congrArg (· + count l q) (congrArg sign h)).symm ▸ (Nat.zero_add _).symm ▸ rest
    | n + 1 => match List.append_of_mem (sub a (.head l) (h.symm ▸ Nat.zero_lt_succ n)) with
      | ⟨p, r, split⟩ =>
        have inner : count l q ≤ (p ++ r).length :=
          count_le_of_sub distinct fun b mem positive =>
            mem_remove (fun same => fresh (Eq.subst (motive := fun x => x ∈ l) same mem))
              (split ▸ sub b (.tail a mem) positive)
        have whole : m.length = (p ++ r).length + 1 :=
          (congrArg List.length split).trans ((length_append p (a :: r)).trans
            ((Nat.add_succ _ _).trans (congrArg Nat.succ (length_append p r).symm)))
        show sign (q a) + count l q ≤ m.length from
          (congrArg (· + count l q) (congrArg sign h)).symm ▸ whole ▸
            (Nat.add_comm (count l q) 1 ▸ Nat.succ_le_succ inner)

/-- Constructively, either some member of a list lacks a decidable property, or every
member has it. -/
theorem search {p : α → Prop} [decide : ∀ a, Decidable (p a)] :
    ∀ l : List α, (∃ a, a ∈ l ∧ ¬ p a) ∨ ∀ a, a ∈ l → p a
  | [] => .inr fun _ mem => nomatch mem
  | a :: l => match decide a with
    | isFalse lacks => .inl ⟨a, .head l, lacks⟩
    | isTrue has => match search l with
      | .inl ⟨b, mem, lacks⟩ => .inl ⟨b, .tail a mem, lacks⟩
      | .inr all => .inr fun b mem => match mem with
        | .head _ => has
        | .tail _ mem => all b mem

/-- Whether some member of a list has a decidable property is decidable. -/
def decideSome {p : α → Prop} [decide : ∀ a, Decidable (p a)] :
    ∀ l : List α, Decidable (∃ a, a ∈ l ∧ p a)
  | [] => isFalse fun ⟨_, mem, _⟩ => nomatch mem
  | a :: l => match decide a with
    | isTrue holds => isTrue ⟨a, .head l, holds⟩
    | isFalse lacks => match decideSome l with
      | isTrue found => isTrue (match found with | ⟨b, mem, holds⟩ => ⟨b, .tail a mem, holds⟩)
      | isFalse absent => isFalse fun ⟨b, mem, holds⟩ => match mem_cons_cases mem with
        | .inl same => lacks (Eq.subst (motive := p) same holds)
        | .inr mem => absent ⟨b, mem, holds⟩

/-- A quantity that ends higher than it starts rises across some step between. -/
theorem rises_between {q : Nat → Nat} {N : Nat} :
    ∀ {T}, N ≤ T → q N < q T → ∃ t, N ≤ t ∧ t < T ∧ q t < q (t + 1)
  | _, .refl, higher => absurd higher (Nat.lt_irrefl _)
  | m + 1, .step within, higher => match Nat.decLt (q m) (q (m + 1)) with
    | isTrue up => ⟨m, within, Nat.lt_succ_self m, up⟩
    | isFalse flat => match rises_between within
        (Nat.lt_of_lt_of_le higher (Nat.ge_of_not_lt flat)) with
      | ⟨t, from_, below, up⟩ => ⟨t, from_, Nat.lt_succ_of_lt below, up⟩

/-! ## Counting marks -/

theorem mark_one {p : Prop} [Decidable p] (holds : p) : mark p = 1 :=
  Nat.le_antisymm (mark_le_one p) (mark_pos.mpr holds)

theorem mark_zero {p : Prop} [Decidable p] (fails : ¬ p) : mark p = 0 :=
  eq_zero_of_not_pos fun pos => fails (mark_pos.mp pos)

/-- Of two decidable propositions, exactly one holding: their marks add to one. -/
theorem mark_add_not {q r : Prop} [Decidable q] [Decidable r] (one : q ∨ r)
    (not_both : ¬ (q ∧ r)) : mark q + mark r = 1 :=
  match one with
  | .inl hq => (congrArg (· + mark r) (mark_one hq)).trans
      (congrArg (1 + ·) (mark_zero fun hr => not_both ⟨hq, hr⟩))
  | .inr hr => (congrArg (mark q + ·) (mark_one hr)).trans
      (congrArg (· + 1) (mark_zero fun hq => not_both ⟨hq, hr⟩))

/-- Quantities that agree on the members of a list have the same total over it. -/
theorem total_congr_on {f g : α → Nat} :
    ∀ {as : List α}, (∀ a, a ∈ as → f a = g a) → total as f = total as g
  | [], _ => rfl
  | a :: _, same => (congrArg (· + _) (same a (.head _))).trans
      (congrArg (g a + ·) (total_congr_on fun b mem => same b (.tail a mem)))

/-- Inserting one member keeps every other. -/
theorem mem_insert {a b : α} : ∀ {p q : List α}, b ∈ p ++ q → b ∈ p ++ a :: q
  | [], _, mem => .tail a mem
  | c :: _, _, mem => match mem_cons_cases mem with
    | .inl same => Eq.subst (motive := fun x => x ∈ c :: _) same.symm (.head _)
    | .inr mem => .tail c (mem_insert mem)

/-- Removing one occurrence keeps a list without repetition. -/
theorem distinct_remove {a : α} : ∀ {p q : List α}, Distinct (p ++ a :: q) → Distinct (p ++ q)
  | [], _, ⟨_, distinct⟩ => distinct
  | _ :: _, _, ⟨fresh, distinct⟩ => ⟨fun mem => fresh (mem_insert mem), distinct_remove distinct⟩

/-- Over a list without repetition, the members at which a decidable property holds are no
more than the members of a second list without repetition at which another holds, where
each of the first is one of the second. -/
theorem marks_le_of_sub {q r : α → Prop} [∀ a, Decidable (q a)] [∀ a, Decidable (r a)] :
    ∀ {l m : List α}, Distinct l → Distinct m → (∀ a, a ∈ l → q a → a ∈ m ∧ r a) →
    total l (fun a => mark (q a)) ≤ total m (fun a => mark (r a))
  | [], _, _, _, _ => Nat.zero_le _
  | a :: l, m, ⟨fresh, distinct⟩, apart, sub =>
    if holds : q a then
      match sub a (.head l) holds with
      | ⟨mem, has⟩ => match List.append_of_mem mem with
        | ⟨p, s, split⟩ =>
          have inner : total l (fun b => mark (q b)) ≤ total (p ++ s) (fun b => mark (r b)) :=
            marks_le_of_sub distinct (distinct_remove (split ▸ apart)) fun b mem_b q_b =>
              match sub b (.tail a mem_b) q_b with
              | ⟨in_m, r_b⟩ => ⟨mem_remove (fun (same : b = a) =>
                  fresh (Eq.subst (motive := fun x => x ∈ l) same mem_b)) (split ▸ in_m), r_b⟩
          have whole : total m (fun b => mark (r b)) = total (p ++ s) (fun b => mark (r b)) + 1 :=
            calc total m (fun b => mark (r b))
                = total p (fun b => mark (r b)) + (mark (r a) + total s fun b => mark (r b)) :=
                  (congrArg (total · fun b => mark (r b)) split).trans (total_append _ (a :: s) p)
              _ = total p (fun b => mark (r b)) + (total s (fun b => mark (r b)) + 1) :=
                  congrArg (total p (fun b => mark (r b)) + ·)
                    ((congrArg (· + _) (mark_one has)).trans (Nat.add_comm 1 _))
              _ = total (p ++ s) (fun b => mark (r b)) + 1 :=
                  (Nat.add_assoc _ _ _).symm.trans (congrArg (· + 1) (total_append _ s p).symm)
          Nat.le_trans (Nat.le_of_eq ((congrArg (· + _) (mark_one holds)).trans (Nat.add_comm 1 _)))
            (Nat.le_trans (Nat.succ_le_succ inner) (Nat.le_of_eq whole.symm))
    else
      Nat.le_trans (Nat.le_of_eq ((congrArg (· + _) (mark_zero holds)).trans (Nat.zero_add _)))
        (marks_le_of_sub distinct apart fun b mem_b q_b => sub b (.tail a mem_b) q_b)

/-- A count balanced across each step, what it gains against what it loses, is balanced
over any stretch: at the end with everything lost, it is the count at the start with
everything gained. -/
theorem balance_over_stretch {q x y : Nat → Nat} (across : ∀ t, q (t + 1) + x t = q t + y t)
    (S : Nat) : ∀ n, q (S + n) + total (steps S n) x = q S + total (steps S n) y
  | 0 => rfl
  | n + 1 => calc
      q (S + (n + 1)) + (x S + total (steps (S + 1) n) x)
          = x S + (q (S + 1 + n) + total (steps (S + 1) n) x) :=
        (congrArg (· + _) (congrArg q (Nat.add_right_comm S 1 n).symm)).trans
          (Nat.add_left_comm _ _ _)
      _ = x S + (q (S + 1) + total (steps (S + 1) n) y) :=
        congrArg (x S + ·) (balance_over_stretch across (S + 1) n)
      _ = (q (S + 1) + x S) + total (steps (S + 1) n) y :=
        (Nat.add_left_comm _ _ _).trans (Nat.add_assoc _ _ _).symm
      _ = (q S + y S) + total (steps (S + 1) n) y := congrArg (· + _) (across S)
      _ = q S + (y S + total (steps (S + 1) n) y) := Nat.add_assoc _ _ _

/-! ## Listing what holds -/

/-- The members of which a determination holds at each step are listed, each once:
finitely many hold at each step, of possibly infinitely many in all. -/
def Listed (p : α → Nat → Prop) (l : Nat → List α) : Prop :=
  ∀ t, Distinct (l t) ∧ ∀ a, p a t ↔ a ∈ l t

namespace Listed

variable {p : α → Nat → Prop} [∀ a t, Decidable (p a t)] {l : Nat → List α}

/-- The census balance across a step: the list after it with the members that ceased to be
is the list before it with the members that came to be. The members kept across the step
are counted alike on both lists. -/
theorem across (listed : Listed p l) (t : Nat) :
    (l (t + 1)).length + ceasings (l t) p t = (l t).length + comings (l (t + 1)) p t :=
  have before : (l t).length = total (l t) (fun a => mark (p a (t + 1))) + ceasings (l t) p t :=
    (total_ones (l t)).symm.trans ((total_congr_on fun a mem =>
      have held : p a t := ((listed t).2 a).mpr mem
      Eq.symm (mark_add_not (q := p a (t + 1)) (r := CeasesToBe (p a) t)
        (if h : p a (t + 1) then .inl h else .inr ⟨held, h⟩)
        fun both => both.2.2 both.1)).trans (total_add _ _ (l t)))
  have after : (l (t + 1)).length =
      total (l (t + 1)) (fun a => mark (p a t)) + comings (l (t + 1)) p t :=
    (total_ones (l (t + 1))).symm.trans ((total_congr_on fun a mem =>
      have held : p a (t + 1) := ((listed (t + 1)).2 a).mpr mem
      Eq.symm (mark_add_not (q := p a t) (r := ComesToBe (p a) t)
        (if h : p a t then .inl h else .inr ⟨h, held⟩)
        fun both => both.2.1 both.1)).trans (total_add _ _ (l (t + 1))))
  have kept : total (l t) (fun a => mark (p a (t + 1))) =
      total (l (t + 1)) (fun a => mark (p a t)) :=
    Nat.le_antisymm
      (marks_le_of_sub (q := fun a => p a (t + 1)) (r := fun a => p a t) (listed t).1
        (listed (t + 1)).1 fun a mem h => ⟨((listed (t + 1)).2 a).mp h, ((listed t).2 a).mpr mem⟩)
      (marks_le_of_sub (q := fun a => p a t) (r := fun a => p a (t + 1)) (listed (t + 1)).1
        (listed t).1 fun a mem h => ⟨((listed t).2 a).mp h, ((listed (t + 1)).2 a).mpr mem⟩)
  calc (l (t + 1)).length + ceasings (l t) p t
      = (total (l (t + 1)) (fun a => mark (p a t)) + comings (l (t + 1)) p t) +
          ceasings (l t) p t := congrArg (· + _) after
    _ = (total (l t) (fun a => mark (p a (t + 1))) + ceasings (l t) p t) +
          comings (l (t + 1)) p t :=
        (congrArg (fun k => k + comings (l (t + 1)) p t + ceasings (l t) p t) kept.symm).trans
          (Nat.add_right_comm _ _ _)
    _ = (l t).length + comings (l (t + 1)) p t := congrArg (· + _) before.symm

/-- Over any stretch, the list at the end with the members that ceased to be is the list at
the start with the members that came to be. -/
theorem over_stretch (listed : Listed p l) (S n : Nat) :
    (l (S + n)).length + total (steps S n) (fun t => ceasings (l t) p t) =
      (l S).length + total (steps S n) (fun t => comings (l (t + 1)) p t) :=
  balance_over_stretch (q := fun t => (l t).length) (x := fun t => ceasings (l t) p t)
    (y := fun t => comings (l (t + 1)) p t) listed.across S n

/-- So over any stretch, the members ceasing to be are at most those coming to be and those
listed at the start: the census law counted. -/
theorem ceasings_within (listed : Listed p l) (S n : Nat) :
    total (steps S n) (fun t => ceasings (l t) p t) ≤
      (l S).length + total (steps S n) (fun t => comings (l (t + 1)) p t) :=
  Nat.le_trans (Nat.le_add_left _ _) (Nat.le_of_eq (listed.over_stretch S n))

/-- And the members coming to be are at most those ceasing to be and those listed at the
end: where at most `B` are listed, at most `B` more come to be than cease to be. -/
theorem comings_within (listed : Listed p l) (S n : Nat) :
    total (steps S n) (fun t => comings (l (t + 1)) p t) ≤
      (l (S + n)).length + total (steps S n) (fun t => ceasings (l t) p t) :=
  Nat.le_trans (Nat.le_add_left _ (l S).length) (Nat.le_of_eq (listed.over_stretch S n).symm)

/-- Read of recurrence, the balance is exact: ceasing to be recurs exactly when, from each
step, the list at some later step is shorter than the list at the start with the members
that came to be between. -/
theorem ceasing_iff_shortfall (listed : Listed p l) :
    (∀ N, ∃ t a, N ≤ t ∧ CeasesToBe (p a) t) ↔
      ∀ N, ∃ n, (l (N + n)).length <
        (l N).length + total (steps N n) fun t => comings (l (t + 1)) p t :=
  ⟨fun ceasing N => match ceasing N with
    | ⟨t, a, later, ceases⟩ => match le_dest later with
      | ⟨m, same⟩ =>
        have ceased : 0 < total (steps N (m + 1)) fun t => ceasings (l t) p t :=
          Nat.lt_of_lt_of_le
            (same ▸ total_pos_of_mem (((listed t).2 a).mp ceases.1) (mark_pos.mpr ceases))
            (Nat.le_trans (Nat.le_add_left _ _) (Nat.le_of_eq (steps_last _ N m).symm))
        ⟨m + 1, Nat.lt_of_lt_of_le (Nat.lt_add_of_pos_right ceased)
          (Nat.le_of_eq (listed.over_stretch N (m + 1)))⟩,
   fun shortfall N => match shortfall N with
    | ⟨n, short⟩ =>
      match total_pos (steps N n)
        (pos_of_exceeds short (Nat.le_of_eq (listed.over_stretch N n).symm)) with
      | ⟨t, mem, ceased⟩ => match total_pos (l t) ceased with
        | ⟨a, _, ceases⟩ => ⟨t, a, steps_mem mem, mark_pos.mp ceases⟩⟩

/-- And coming to be recurs exactly when, from each step, the list at some later step with
the members that ceased to be between is longer than the list at the start. -/
theorem coming_iff_excess (listed : Listed p l) :
    (∀ N, ∃ t a, N ≤ t ∧ ComesToBe (p a) t) ↔
      ∀ N, ∃ n, (l N).length <
        (l (N + n)).length + total (steps N n) fun t => ceasings (l t) p t :=
  ⟨fun coming N => match coming N with
    | ⟨t, a, later, comes⟩ => match le_dest later with
      | ⟨m, same⟩ =>
        have came : 0 < total (steps N (m + 1)) fun t => comings (l (t + 1)) p t :=
          Nat.lt_of_lt_of_le
            (same ▸ total_pos_of_mem (((listed (t + 1)).2 a).mp comes.2) (mark_pos.mpr comes))
            (Nat.le_trans (Nat.le_add_left _ _) (Nat.le_of_eq (steps_last _ N m).symm))
        ⟨m + 1, Nat.lt_of_lt_of_le (Nat.lt_add_of_pos_right came)
          (Nat.le_of_eq (listed.over_stretch N (m + 1)).symm)⟩,
   fun excess N => match excess N with
    | ⟨n, short⟩ =>
      match total_pos (steps N n)
        (pos_of_exceeds short (Nat.le_of_eq (listed.over_stretch N n))) with
      | ⟨t, mem, came⟩ => match total_pos (l (t + 1)) came with
        | ⟨a, _, comes⟩ => ⟨t, a, steps_mem mem, mark_pos.mp comes⟩⟩

/-- The census law: where what holds is listed at each step, ceasing to be at arbitrarily
late steps needs coming to be at arbitrarily late steps. Ceasings recurring accumulate past
any list at the start, and only comings make up the difference. -/
theorem coming_of_ceasing (listed : Listed p l)
    (ceasing : ∀ N, ∃ t a, N ≤ t ∧ CeasesToBe (p a) t) :
    ∀ N, ∃ t a, N ≤ t ∧ ComesToBe (p a) t :=
  listed.coming_iff_excess.mpr fun N =>
    match recurring_accumulates (q := fun t => ceasings (l t) p t) (fun M =>
        match ceasing M with
        | ⟨t, a, later, ceases⟩ =>
          ⟨t, later, total_pos_of_mem (((listed t).2 a).mp ceases.1) (mark_pos.mpr ceases)⟩)
        N ((l N).length + 1) with
    | ⟨n, many⟩ => ⟨n, Nat.lt_of_lt_of_le many (Nat.le_add_left _ _)⟩

/-- Where at most `K` are listed at arbitrarily late steps, coming to be at arbitrarily late
steps needs ceasing to be at arbitrarily late steps: comings recurring accumulate past `K`,
and the list returns to at most `K`. -/
theorem ceasing_of_returning (listed : Listed p l) {K : Nat}
    (returns : ∀ N, ∃ t, N ≤ t ∧ (l t).length ≤ K)
    (coming : ∀ N, ∃ t a, N ≤ t ∧ ComesToBe (p a) t) :
    ∀ N, ∃ t a, N ≤ t ∧ CeasesToBe (p a) t :=
  listed.ceasing_iff_shortfall.mpr fun N =>
    match recurring_accumulates (q := fun t => comings (l (t + 1)) p t) (fun M =>
        match coming M with
        | ⟨t, a, later, comes⟩ =>
          ⟨t, later, total_pos_of_mem (((listed (t + 1)).2 a).mp comes.2) (mark_pos.mpr comes)⟩)
        N (K + 1) with
    | ⟨m, many⟩ => match returns (N + m) with
      | ⟨_, later, few⟩ => match le_dest later with
        | ⟨k, same⟩ => ⟨m + k, Nat.lt_of_le_of_lt
            (Nat.le_trans (Nat.le_of_eq (congrArg (fun s => (l s).length)
              (same.trans (Nat.add_assoc N m k)).symm)) few)
            (Nat.lt_of_lt_of_le many (Nat.le_trans (steps_mono _ N m k) (Nat.le_add_left _ _)))⟩

/-- The bounded law: where from some step on at most `B` are listed, coming to be at
arbitrarily late steps needs ceasing to be at arbitrarily late steps. -/
theorem ceasing_of_coming (listed : Listed p l) {T B : Nat}
    (bounded : ∀ t, T ≤ t → (l t).length ≤ B) (coming : ∀ N, ∃ t a, N ≤ t ∧ ComesToBe (p a) t) :
    ∀ N, ∃ t a, N ≤ t ∧ CeasesToBe (p a) t :=
  listed.ceasing_of_returning
    (fun N => ⟨N + T, Nat.le_add_right N T, bounded _ (Nat.le_add_left T N)⟩) coming

/-- So where from some step on at most `B` are listed, coming to be recurs exactly when
ceasing to be does: the law of a finite family (`coming_recurs_iff`) needs only a list
bounded from some step on. -/
theorem coming_iff_ceasing (listed : Listed p l) {T B : Nat}
    (bounded : ∀ t, T ≤ t → (l t).length ≤ B) :
    (∀ N, ∃ t a, N ≤ t ∧ ComesToBe (p a) t) ↔ ∀ N, ∃ t a, N ≤ t ∧ CeasesToBe (p a) t :=
  ⟨listed.ceasing_of_coming bounded, listed.coming_of_ceasing⟩

/-- The rate law: where at most `B t` are listed at each step `t`, and from each step the
members coming to be over some stretch outnumber the bound at its end, ceasing to be
recurs. A bound however large is outnumbered by comings that outpace it; no bound growing
without end, however slowly, makes ceasing recur by itself (`World.slow_world`). -/
theorem ceasing_of_outpacing (listed : Listed p l) {B : Nat → Nat}
    (bounded : ∀ t, (l t).length ≤ B t)
    (outpacing : ∀ N, ∃ n, B (N + n) < total (steps N n) fun t => comings (l (t + 1)) p t) :
    ∀ N, ∃ t a, N ≤ t ∧ CeasesToBe (p a) t :=
  listed.ceasing_iff_shortfall.mpr fun N => match outpacing N with
    | ⟨n, more⟩ => ⟨n, Nat.lt_of_le_of_lt (bounded (N + n))
        (Nat.lt_of_lt_of_le more (Nat.le_add_left _ _))⟩

end Listed

/-! ## Censuses -/

variable {F C : Type}

namespace Web

/-- The formations active at each step are listed, each once. -/
def Census (W : Web F C) (alive : Nat → List F) : Prop :=
  Listed (fun f t => W.active t f) alive

/-- The dependences of each step, formation with condition, are listed, each once. -/
def DependenceCensus (W : Web F C) (deps : Nat → List (F × C)) : Prop :=
  Listed (fun d t => W.requires t d.1 d.2) deps

/-- The census law read of dependence: where the dependences of each step are listed,
dependences dissolving at arbitrarily late steps need dependences forming at arbitrarily
late steps (`Listed.coming_of_ceasing`). -/
theorem DependenceCensus.forming_of_dissolving {W : Web F C}
    [∀ t g c, Decidable (W.requires t g c)] {deps : Nat → List (F × C)}
    (census : W.DependenceCensus deps) (dissolving : ∀ N, ∃ t g c, N ≤ t ∧ W.Dissolves t g c) :
    ∀ N, ∃ t g c, N ≤ t ∧ W.Forms t g c :=
  fun N => match Listed.coming_of_ceasing census (fun N => match dissolving N with
      | ⟨t, g, c, later, dissolves⟩ => ⟨t, (g, c), later, dissolves⟩) N with
    | ⟨t, d, later, forms⟩ => ⟨t, d.1, d.2, later, forms⟩

/-- Where from some step on at most `B` dependences hold at each step, forming recurs
exactly when dissolving does (`Listed.coming_iff_ceasing`). -/
theorem DependenceCensus.forming_iff_dissolving {W : Web F C}
    [∀ t g c, Decidable (W.requires t g c)] {deps : Nat → List (F × C)}
    (census : W.DependenceCensus deps) {T B : Nat} (bounded : ∀ t, T ≤ t → (deps t).length ≤ B) :
    (∀ N, ∃ t g c, N ≤ t ∧ W.Forms t g c) ↔ ∀ N, ∃ t g c, N ≤ t ∧ W.Dissolves t g c :=
  ⟨fun forming N => match Listed.ceasing_of_coming census bounded (fun N => match forming N with
      | ⟨t, g, c, later, forms⟩ => ⟨t, (g, c), later, forms⟩) N with
    | ⟨t, d, later, dissolves⟩ => ⟨t, d.1, d.2, later, dissolves⟩,
   census.forming_of_dissolving⟩

instance decideForms (W : Web F C) [∀ t g c, Decidable (W.requires t g c)] (t : Nat) (g : F)
    (c : C) : Decidable (W.Forms t g c) :=
  instDecidableAnd

instance decideDissolves (W : Web F C) [∀ t g c, Decidable (W.requires t g c)] (t : Nat)
    (g : F) (c : C) : Decidable (W.Dissolves t g c) :=
  instDecidableAnd

/-- The census balance read of dependence: over any stretch, the dependences holding at the
end with those that dissolved are those holding at the start with those that formed
(`Listed.over_stretch`). -/
theorem DependenceCensus.over_stretch {W : Web F C} [∀ t g c, Decidable (W.requires t g c)]
    {deps : Nat → List (F × C)} (census : W.DependenceCensus deps) (S n : Nat) :
    (deps (S + n)).length + total (steps S n) (fun t => total (deps t) fun d =>
      mark (W.Dissolves t d.1 d.2)) =
      (deps S).length + total (steps S n) (fun t => total (deps (t + 1)) fun d =>
        mark (W.Forms t d.1 d.2)) :=
  Listed.over_stretch census S n

variable (W : Web F C) [∀ t f, Decidable (W.active t f)]

/-- If more formations are active after a step than before, one of them arises across
it. -/
theorem arises_of_more {t : Nat} {before after : List F}
    (listed : ∀ f, W.active t f → f ∈ before) (distinct : Distinct after)
    (now : ∀ f, f ∈ after → W.active (t + 1) f) (more : before.length < after.length) :
    ∃ f, f ∈ after ∧ W.Arises t f :=
  match search (p := W.active t) after with
  | .inl ⟨f, mem, inactive⟩ => ⟨f, mem, inactive, now f mem⟩
  | .inr all => absurd more (Nat.not_lt_of_ge
      (length_le_of_sub distinct fun f mem => listed f (all f mem)))

/-- A census that grows without bound makes generation unceasing. -/
theorem unceasing_of_growth {alive : Nat → List F} (census : W.Census alive)
    (grows : ∀ N K, ∃ t, N ≤ t ∧ K < (alive t).length) : W.Unceasing :=
  fun N => match grows N (alive N).length with
  | ⟨_, later, larger⟩ => match rises_between (q := fun t => (alive t).length) later larger with
    | ⟨t, from_, _, up⟩ =>
      match W.arises_of_more (fun f a => ((census t).2 f).mp a) ((census (t + 1)).1)
        (fun f mem => ((census (t + 1)).2 f).mpr mem) up with
      | ⟨f, _, arises⟩ => ⟨t, f, from_, arises⟩

/-- Under a census, ceasing at arbitrarily late steps needs arising at arbitrarily late
steps (`Listed.coming_of_ceasing`): with finitely many formations active at each step,
nothing keeps ceasing unless something keeps arising. -/
theorem arising_of_ceasing {alive : Nat → List F} (census : W.Census alive)
    (ceasing : ∀ N, ∃ t f, N ≤ t ∧ W.Ceases t f) : W.Unceasing :=
  Listed.coming_of_ceasing census ceasing

/-- With at most `B` formations active at each step from some step on, arising at
arbitrarily late steps needs ceasing at arbitrarily late steps
(`Listed.ceasing_of_coming`). -/
theorem ceasing_of_arising {alive : Nat → List F} (census : W.Census alive) {T B : Nat}
    (bounded : ∀ t, T ≤ t → (alive t).length ≤ B) (arising : W.Unceasing) :
    ∀ N, ∃ t f, N ≤ t ∧ W.Ceases t f :=
  Listed.ceasing_of_coming census bounded arising

/-- So with at most `B` formations active at each step from some step on, some formation
arises at arbitrarily late steps exactly when some formation ceases at arbitrarily late
steps: the law for finitely many formations (`unceasing_iff`) needs only a count bounded
from some step on. -/
theorem unceasing_iff_bounded {alive : Nat → List F} (census : W.Census alive) {T B : Nat}
    (bounded : ∀ t, T ≤ t → (alive t).length ≤ B) :
    W.Unceasing ↔ ∀ N, ∃ t f, N ≤ t ∧ W.Ceases t f :=
  Listed.coming_iff_ceasing census bounded

/-- The census balance read of activity: over any stretch, the formations active at the end
with those that ceased are those active at the start with those that arose
(`Listed.over_stretch`). -/
theorem Census.over_stretch {alive : Nat → List F} (census : W.Census alive) (S n : Nat) :
    (alive (S + n)).length + total (steps S n) (fun t => total (alive t) fun f =>
      mark (W.Ceases t f)) =
      (alive S).length + total (steps S n) (fun t => total (alive (t + 1)) fun f =>
        mark (W.Arises t f)) :=
  Listed.over_stretch census S n

end Web

/-- Under a census, with each formation taking part in the flow listed once and only
active formations taking, more without end makes the active formations grow without
bound. -/
theorem Flow.More.grows {W : Web F C} {L : Flow F C} {cs : List C} {alive : Nat → List F}
    (census : W.Census alive) (distinct : ∀ t, Distinct (L.present t)) (taking : L.Taking W)
    (more : L.More cs) : ∀ N K, ∃ t, N ≤ t ∧ K < (alive t).length :=
  have counted : ∀ t, L.takers cs t ≤ (alive t).length := fun t =>
    count_le_of_sub (distinct t) fun f mem takes => match total_pos cs takes with
    | ⟨c, _, positive⟩ => ((census t).2 f).mp (taking t f c mem positive).1
  fun N K => match more (K + 1) with
  | ⟨T, many⟩ => ⟨N + T, Nat.le_add_right N T,
      Nat.lt_of_lt_of_le (many (N + T) (Nat.le_add_left T N)) (counted (N + T))⟩

/-- More without end makes generation unceasing when a census lists the active
formations, each formation taking part in the flow is listed once, and only active
formations take. -/
theorem Flow.More.unceasing {W : Web F C} [∀ t f, Decidable (W.active t f)] {L : Flow F C}
    {cs : List C} {alive : Nat → List F} (census : W.Census alive)
    (distinct : ∀ t, Distinct (L.present t)) (taking : L.Taking W) (more : L.More cs) :
    W.Unceasing :=
  W.unceasing_of_growth census (more.grows census distinct taking)

/-! ## Every premise together -/

namespace Garden

theorem distinct : ∀ t, Distinct (present t)
  | 0 => trivial
  | n + 1 => ⟨fun mem => match mem_cons_cases mem with
      | .inl same => Kind.noConfusion (congrArg Prod.fst same)
      | .inr mem => Nat.lt_irrefl n (present_active n _ mem),
     fun mem => Nat.lt_irrefl n (present_active n _ mem), distinct n⟩

theorem listed : ∀ t (f : Kind × Nat), f.2 < t → f ∈ present t
  | 0, _, lt => absurd lt (Nat.not_lt_zero _)
  | n + 1, (k, i), lt => match Nat.lt_or_ge i n with
    | .inl below => .tail _ (.tail _ (listed n (k, i) below))
    | .inr above =>
      have same : n = i := Nat.le_antisymm above (Nat.le_of_lt_succ lt)
      match k with
      | .renewer => Eq.subst (motive := fun j => (Kind.renewer, j) ∈ present (n + 1))
          same (.head _)
      | .grower => Eq.subst (motive := fun j => (Kind.grower, j) ∈ present (n + 1))
          same (.tail _ (.head _))

/-- The garden's formations active at each step are those taking part, each listed once. -/
theorem census : web.Census present :=
  fun t => ⟨distinct t, fun f => ⟨listed t f, present_active t f⟩⟩

/-- Every premise of `Flow.More.unceasing` holds together in the garden. -/
theorem counted :
    web.Census present ∧ (∀ t, Distinct (flow.present t)) ∧ flow.Taking web ∧
    flow.More [()] :=
  ⟨census, distinct, growers_take.1, more.2.2.2.2.2.2⟩

end Garden

namespace Cycle

theorem distinct : ∀ t, Distinct (present t)
  | 0 => trivial
  | n + 1 => ⟨fun mem => Nat.lt_irrefl n (present_lt n n mem), distinct n⟩

theorem listed : ∀ t n, n < t → n ∈ present t
  | 0, _, lt => absurd lt (Nat.not_lt_zero _)
  | m + 1, n, lt => match Nat.lt_or_ge n m with
    | .inl below => .tail _ (listed m n below)
    | .inr above => Eq.subst (motive := fun j => j ∈ present (m + 1))
        (Nat.le_antisymm above (Nat.le_of_lt_succ lt)) (.head _)

/-- The cycle's formations active at each step are those taking part, each listed once. -/
theorem census : web.Census present :=
  fun t => ⟨distinct t, fun n => ⟨listed t n, present_lt t n⟩⟩

/-- Every premise of `Flow.More.unceasing` holds together in the cycle. -/
theorem counted :
    web.Census present ∧ (∀ t, Distinct (flow.present t)) ∧ flow.Taking web ∧
    flow.More [()] :=
  ⟨census, distinct, closed_more.2.2.1, closed_more.2.2.2.2.2.2.1⟩

end Cycle

/-! ## Under a census, unceasing generation is not yet more -/

namespace Bloom

/-- The sun at every step, and the bloom at even steps. -/
def alive : Nat → List Formation
  | 0 => [.sun, .bloom]
  | 1 => [.sun]
  | n + 2 => alive n

theorem pair : Distinct [Formation.sun, .bloom] :=
  ⟨fun mem => (match mem with | .tail _ mem => nomatch mem), fun mem => (nomatch mem), trivial⟩

theorem census : web.Census alive
  | 0 => ⟨pair, fun f => match f with
    | .sun => ⟨fun _ => .head _, fun _ => trivial⟩
    | .bloom => ⟨fun _ => .tail _ (.head _), fun _ => Nat.le_refl 2⟩⟩
  | 1 => ⟨⟨fun mem => (nomatch mem), trivial⟩, fun f => match f with
    | .sun => ⟨fun _ => .head _, fun _ => trivial⟩
    | .bloom => ⟨fun two => absurd two (Nat.not_succ_le_self 1),
        fun mem => match mem with | .tail _ mem => nomatch mem⟩⟩
  | n + 2 => census n

/-- The bloom meets every premise of `Flow.More.unceasing` except more without end: a
census lists the active formations, the sun and the bloom take part once each, and only
the active bloom takes. Generation is unceasing and not more. -/
theorem counted :
    web.Census alive ∧ (∀ t, Distinct (flow.present t)) ∧ flow.Taking web ∧
    web.Unceasing ∧ ¬ flow.More [()] :=
  ⟨census, fun _ => pair, takes.1, not_more.2.2.2.1, not_more.2.2.2.2⟩

end Bloom

/-! ## Without a census, more without end with nothing arising -/

namespace Dormant

/-- The garden's flow, with every formation active from the start. -/
def web : Web (Garden.Kind × Nat) Unit :=
  { Garden.web with active := fun _ _ => True }

/-- Every premise of `More.renewers_unbounded` holds, only active formations take, and
generation is more without end, yet nothing arises: infinitely many formations are
active at every step, so no census lists them. -/
theorem more_without_arising :
    Garden.flow.Balances web ∧ Garden.flow.Acting web ∧ Garden.flow.Taking web ∧
    Garden.flow.Capacity [()] 1 ∧ web.Dependent ∧ Garden.flow.More [()] ∧
    ∀ t f, ¬ web.Arises t f :=
  ⟨Garden.more.1, fun _ _ _ _ _ => trivial,
   fun t f _ mem takes => match f, mem, takes with
    | (.renewer, _), _, takes => absurd takes (Nat.lt_irrefl 0)
    | (.grower, _), mem, _ => ⟨trivial, rfl, Garden.present_active t _ mem⟩,
   Garden.more.2.2.1, fun _ _ _ _ _ => Nat.le_refl 1, Garden.more.2.2.2.2.2.2,
   fun _ _ ⟨inactive, _⟩ => inactive trivial⟩

end Dormant

/-! ## With a formation listed many times, more without end with nothing arising -/

namespace Repeated

/-- `n` entries, all the same formation. -/
def rep : Nat → List Unit
  | 0 => []
  | n + 1 => () :: rep n

/-- One formation, always active, drawing on the condition. -/
def web : Web Unit Unit where
  level _ _ := 1
  active _ _ := True
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := True

/-- The flow lists the one formation `t` times at step `t`, each entry taking one unit and
giving one back. -/
def flow : Flow Unit Unit := ⟨rep, fun _ _ _ => 1, fun _ _ _ => 1⟩

theorem ones : ∀ n, total (rep n) (fun _ => 1) = n
  | 0 => rfl
  | n + 1 => (congrArg (1 + ·) (ones n)).trans (Nat.add_comm 1 n)

theorem census : web.Census fun _ => [()] :=
  fun _ => ⟨⟨fun mem => (nomatch mem), trivial⟩,
    fun f => ⟨fun _ => match f with | () => .head [], fun _ => trivial⟩⟩

/-- A census lists the one active formation, the flow balances, only active formations
give and take, and only from what they draw on; generation is more without end, and
nothing ever arises. The one premise of `Flow.More.unceasing` that fails is that the
flow lists each formation once. -/
theorem more_without_arising :
    web.Census (fun _ => [()]) ∧ flow.Balances web ∧ flow.Acting web ∧ flow.Taking web ∧
    flow.More [()] ∧ ¬ (∀ t, Distinct (flow.present t)) ∧ ∀ t f, ¬ web.Arises t f :=
  ⟨census, fun _ _ => rfl, fun _ _ _ _ _ => trivial, fun _ _ _ _ _ => ⟨trivial, trivial⟩,
   fun K => ⟨K, fun t later => Nat.le_trans later (Nat.le_of_eq (ones t).symm)⟩,
   fun distinct => (distinct 2).1 (.head []),
   fun _ _ arises => arises.1 trivial⟩

end Repeated

/-! ## Without `Taking`, more without end with nothing arising -/

namespace Inactive

/-- Formation `0` and formations `1`, …, `t` take part in the step from `t`. -/
def present : Nat → List Nat
  | 0 => [0]
  | n + 1 => (n + 1) :: present n

/-- Formation `0` gives as much as the others take; each of the others takes one unit. -/
def flow : Flow Nat Unit where
  present := present
  take _ n _ := match n with
    | 0 => 0
    | _ + 1 => 1
  give t n _ := match n with
    | 0 => t
    | _ + 1 => 0

/-- Only formation `0` is active. -/
def web : Web Nat Unit where
  level _ _ := 1
  active _ n := n = 0
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False

/-- Formation `0` alone. -/
def alive (_ : Nat) : List Nat := [0]

theorem ones {q : Nat → Nat} (zero : q 0 = 0) (one : ∀ m, q (m + 1) = 1) :
    ∀ n, total (present n) q = n
  | 0 => congrArg (· + 0) zero
  | n + 1 => (congrArg (· + total (present n) q) (one n)).trans
      ((congrArg (1 + ·) (ones zero one n)).trans (Nat.add_comm 1 n))

theorem gives (t : Nat) : ∀ n, total (present n) (fun m => flow.give t m ()) = t
  | 0 => rfl
  | n + 1 => (Nat.zero_add _).trans (gives t n)

theorem present_le : ∀ n m, m ∈ present n → m ≤ n
  | 0, _, .head _ => Nat.le_refl 0
  | n + 1, _, .head _ => Nat.le_refl (n + 1)
  | n + 1, m, .tail _ mem => Nat.le_succ_of_le (present_le n m mem)

theorem distinct : ∀ n, Distinct (present n)
  | 0 => ⟨fun mem => (nomatch mem), trivial⟩
  | n + 1 => ⟨fun mem => Nat.not_succ_le_self n (present_le n (n + 1) mem), distinct n⟩

/-- The flow balances, only active formations give, a census lists the active
formations, each formation takes part once, and generation is more without end; yet the
takers are never active and nothing arises. -/
theorem more_without_arising :
    flow.Balances web ∧ flow.Acting web ∧ web.Census alive ∧
    (∀ t, Distinct (flow.present t)) ∧ flow.More [()] ∧ ¬ flow.Taking web ∧
    ∀ t f, ¬ web.Arises t f :=
  ⟨fun t _ => congrArg (1 + ·) ((ones rfl (fun _ => rfl) t).trans (gives t t).symm),
   fun _ n _ _ gives => match n, gives with
    | 0, _ => rfl
    | _ + 1, gives => absurd gives (Nat.lt_irrefl 0),
   fun _ => ⟨⟨fun mem => (nomatch mem), trivial⟩, fun n =>
     ⟨fun active => Eq.subst (motive := fun n => n ∈ [0]) active.symm (.head []),
      fun (mem : n ∈ [0]) => match n, mem with
        | _, .head _ => rfl
        | _, .tail _ mem => nomatch mem⟩⟩,
   distinct,
   fun K => ⟨K, fun t later => Nat.le_trans later (Nat.le_of_eq (ones rfl (fun _ => rfl) t).symm)⟩,
   fun taking => Nat.noConfusion (taking 1 1 () (.head _) Nat.zero_lt_one).1,
   fun _ _ ⟨inactive, active⟩ => inactive active⟩

end Inactive

/-! ## Drawing that the flow does not record -/

namespace Crowd

/-- The formations of the cycle, with no taking or giving recorded. -/
def flow : Flow Nat Unit := ⟨Cycle.present, fun _ _ _ => 0, fun _ _ _ => 0⟩

/-- The flow balances the web, and only active formations take and give; ever more
formations are active, depend on the condition and draw on it, yet no formation takes in
the flow and generation is not more without end. -/
theorem drawing_without_taking :
    flow.Balances Cycle.web ∧ flow.Acting Cycle.web ∧ flow.Taking Cycle.web ∧
    Cycle.web.Dependent ∧
    (∀ K, ∃ T, ∀ t, T ≤ t → ∀ n, n < K →
      Cycle.web.active t n ∧ Cycle.web.requires t n () ∧ Cycle.web.draws t n ()) ∧
    ¬ flow.More [()] :=
  have none : ∀ t, flow.takers [()] t = 0 := fun t => total_zero (Cycle.present t)
  ⟨fun _ _ => rfl,
   fun _ _ _ _ gives => absurd gives (Nat.lt_irrefl 0),
   fun _ _ _ _ takes => absurd takes (Nat.lt_irrefl 0),
   fun _ _ _ _ _ => Nat.le_refl 1,
   fun K => ⟨K, fun _ later _ below =>
     have active := Nat.lt_of_lt_of_le below later
     ⟨active, active, active⟩⟩,
   fun more => match more 1 with
    | ⟨T, many⟩ => Nat.not_succ_le_zero 0
        (Nat.le_trans (many T (Nat.le_refl T)) (Nat.le_of_eq (none T)))⟩

end Crowd

end Becoming
