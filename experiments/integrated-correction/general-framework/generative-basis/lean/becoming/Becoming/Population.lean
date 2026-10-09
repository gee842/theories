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
* Under a census, ceasing at arbitrarily late steps needs arising at arbitrarily late
  steps (`arising_of_ceasing`). A ceasing not preceded by an arising leaves fewer
  formations active than before (`arises_or_fewer`), and the count cannot fall forever.
  Not conversely: ever new formations can arise while none ceases (`Dawn`).
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

/-! ## Censuses -/

variable {F C : Type}

namespace Web

/-- The formations active at each step are listed, each once. -/
def Census (W : Web F C) (alive : Nat → List F) : Prop :=
  ∀ t, Distinct (alive t) ∧ ∀ f, W.active t f ↔ f ∈ alive t

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

/-- Under a census, either some formation arises from `N` on, or every formation active
at a later step was already active at `N`. -/
theorem arises_or_kept {alive : Nat → List F} (census : W.Census alive) {N : Nat} :
    ∀ {T}, N ≤ T → (∃ t f, N ≤ t ∧ W.Arises t f) ∨ ∀ f, W.active T f → W.active N f
  | _, .refl => .inr fun _ active => active
  | m + 1, .step within => match arises_or_kept census within with
    | .inl found => .inl found
    | .inr kept => match search (p := W.active m) (alive (m + 1)) with
      | .inl ⟨f, mem, inactive⟩ => .inl ⟨m, f, within, inactive, ((census (m + 1)).2 f).mpr mem⟩
      | .inr all => .inr fun f active => kept f (all f (((census (m + 1)).2 f).mp active))

/-- Under a census, a formation ceasing from `N` on comes after an arising from `N` on, or
leaves fewer formations active after its step than at `N`. -/
theorem arises_or_fewer {alive : Nat → List F} (census : W.Census alive) {N T : Nat}
    (later : N ≤ T) {f : F} (ceases : W.Ceases T f) :
    (∃ t g, N ≤ t ∧ W.Arises t g) ∨ (alive (T + 1)).length < (alive N).length :=
  match W.arises_or_kept census later with
  | .inl found => .inl found
  | .inr before => match W.arises_or_kept census (Nat.le_succ_of_le later) with
    | .inl found => .inl found
    | .inr after => .inr (length_le_of_sub (l := f :: alive (T + 1))
        ⟨fun mem => ceases.2 (((census (T + 1)).2 f).mpr mem), (census (T + 1)).1⟩
        fun g mem => match mem with
        | .head _ => ((census N).2 _).mp (before _ ceases.1)
        | .tail _ mem => ((census N).2 g).mp (after g (((census (T + 1)).2 g).mpr mem)))

/-- So where ceasing recurs, each ceasing not preceded by an arising lowers the count, and
the count cannot fall forever. -/
theorem arises_within {alive : Nat → List F} (census : W.Census alive)
    (ceasing : ∀ N, ∃ t f, N ≤ t ∧ W.Ceases t f) :
    ∀ k N, (alive N).length ≤ k → ∃ t f, N ≤ t ∧ W.Arises t f
  | 0, N, bound => match ceasing N with
    | ⟨_, _, later, ceases⟩ => match W.arises_or_fewer census later ceases with
      | .inl found => found
      | .inr fewer => absurd (Nat.le_trans fewer bound) (Nat.not_succ_le_zero _)
  | k + 1, N, bound => match ceasing N with
    | ⟨T, _, later, ceases⟩ => match W.arises_or_fewer census later ceases with
      | .inl found => found
      | .inr fewer =>
        match arises_within census ceasing k (T + 1)
          (Nat.le_of_succ_le_succ (Nat.le_trans fewer bound)) with
        | ⟨t, g, after, arises⟩ => ⟨t, g, Nat.le_trans (Nat.le_succ_of_le later) after, arises⟩

/-- Under a census, ceasing at arbitrarily late steps needs arising at arbitrarily late
steps: with finitely many formations active at each step, nothing keeps ceasing unless
something keeps arising. -/
theorem arising_of_ceasing {alive : Nat → List F} (census : W.Census alive)
    (ceasing : ∀ N, ∃ t f, N ≤ t ∧ W.Ceases t f) : W.Unceasing :=
  fun N => W.arises_within census ceasing _ N (Nat.le_refl _)

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
