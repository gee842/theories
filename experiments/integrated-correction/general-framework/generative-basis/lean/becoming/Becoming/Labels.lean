import Becoming.Unrolling

/-!
# Labels: what finitely many labelled names fix

`Becoming.Unrolling` states that in a world a list holds, a prefix, given nothing, fixes the whole
future through the map (`Learnable.ahead_fixes`), and that a feature is learnable exactly where it is,
from some step on, a reading of that future (`Learnable.learnable_iff_reading`). The reading of the
first direction is a function on whole futures. This module states that a finite part of it is
enough, and what labels of the feature along the course give, with no premise beyond a list.

* **A table of labelled names.** A name is a finite future through the map, latest first, as
  `Law.name` writes it, and a label is a value of the feature. The extrapolation given a table
  unrolls the extrapolation by elimination over the lasso candidates on its own proposals and
  claims the label of the first entry whose name the proposed future begins with
  (`Learnable.byTable`). It is given neither the configurations, nor how many there are, nor the
  law, nor any value of the feature beyond the table's labels; how far to read is the length of
  each name.
* **`N` names of `N - 1` values are enough.** In a world a list of `N` holds, where configurations
  with the same future through the map have features agreeing from some step on, the extrapolation
  given the table of the `N` configurations as many steps on as the list is long, each named by
  its first `N - 1` values through the map, from itself on (Moore's bound,
  `Law.sameFuture_iff_within`), and labelled with its feature, rests in accord with the feature
  along every orbit, from the bound of the extrapolation given nothing on
  (`Learnable.table_predicts`). So a feature is learnable exactly where the extrapolation given some
  table of at most `N` labelled names of `N - 1` values learns it (`Learnable.learnable_iff_table`).
* **The labels needed.** Every value the feature takes from the step an extrapolation given a
  table rests on is a label of the table (`Learnable.label_of_predicts`); where the law leaves every
  configuration unchanged, every value the feature takes is (`Learnable.labels_of_still`).
* **Labels along the course.** Where the map also carries the feature, every feature is
  learned by the extrapolation given nothing, from the bound on (`Learnable.predicts_with_labels`, an
  instance of `Learnable.predicts_through`), and, unrolled, it proposes the feature at every step ahead
  (`Learnable.ahead_with_labels`, an instance of `Learnable.ahead_fixes`): in a world a list holds,
  the labels before the bound fix every later one. Over every course no prefix fixes the next
  value (`Learning.no_prefix_fixes_next`); here a list holds the world.
* **Along runs** (`LearnableRuns.table_predicts`, `LearnableRuns.learnable_iff_table`,
  `LearnableRuns.labels_of_still`, `LearnableRuns.predicts_with_labels`,
  `LearnableRuns.ahead_with_labels`), through `Becoming.LearnableRuns`.

So what a learnable feature adds to the prefix is a finite object: at most `N` labelled names of
`N - 1` values. No ethical predicate, ranking or axiom occurs.
-/

namespace Becoming

universe u v w

namespace Learning

variable {O : Type u} {O' : Type v}

/-- A prefix read through a map is the prefix of the course read through it. -/
theorem prefix_map (g : O → O') (o : Nat → O) :
    ∀ t, (prefixOf o t).map g = prefixOf (fun n => g (o n)) t
  | 0 => rfl
  | t + 1 => congrArg (List.cons (g (o t))) (prefix_map g o t)

end Learning

namespace Identification

/-- The first member of a list meeting a decided condition is a member of the list. -/
theorem firstFit_mem {α : Type} {p : α → Prop} {dec : ∀ a, Decidable (p a)} :
    ∀ {l : List α} {a : α}, firstFit p dec l = some a → a ∈ l
  | [], _, found => nomatch found
  | b :: l, _, found =>
    match Decidable.em (p b) with
    | .inl pb => Eq.subst (motive := fun x => x ∈ b :: l) (Option.some.inj ((if_pos pb).symm.trans found))
        (List.Mem.head l)
    | .inr npb => List.Mem.tail b (firstFit_mem (l := l) ((if_neg npb).symm.trans found))

/-- The first member of a mapped list meeting a condition is the image of the first member meeting
the condition read through the map. -/
theorem firstFit_map {α β : Type} {p : β → Prop} {dec : ∀ b, Decidable (p b)} (g : α → β) :
    ∀ l : List α, firstFit p dec (l.map g) = (firstFit (fun a => p (g a)) (fun a => dec (g a)) l).map g
  | [] => rfl
  | a :: l =>
    match Decidable.em (p (g a)) with
    | .inl pa =>
      have lhs : firstFit p dec ((a :: l).map g) = some (g a) := if_pos pa
      have rhs : firstFit (fun a => p (g a)) (fun a => dec (g a)) (a :: l) = some a := if_pos pa
      lhs.trans (congrArg (Option.map g) rhs).symm
    | .inr npa =>
      have lhs : firstFit p dec ((a :: l).map g) = firstFit p dec (l.map g) := if_neg npa
      have rhs : firstFit (fun a => p (g a)) (fun a => dec (g a)) (a :: l) =
          firstFit (fun a => p (g a)) (fun a => dec (g a)) l := if_neg npa
      lhs.trans ((firstFit_map g l).trans (congrArg (Option.map g) rhs).symm)

end Identification

namespace Learnable

/-! ## A table of labelled names -/

section Table

variable {S : Type} {R : Type} {V : Type} [DecidableEq R]

/-- A proposed future begins with a name: its first values, as many as the name holds, are the
name's, latest first. -/
def Begins (f : Nat → Option R) (e : List R × V) : Prop :=
  Learning.prefixOf f e.1.length = e.1.map some

instance decBegins (f : Nat → Option R) (e : List R × V) : Decidable (Begins f e) :=
  decEq (Learning.prefixOf f e.1.length) (e.1.map some)

/-- **The extrapolation given a table of labelled names**: it unrolls the extrapolation by
elimination over the lasso candidates on its own proposals and claims the label of the first entry
whose name the proposed future begins with. -/
def byTable (tbl : List (List R × V)) (r : List R) : Option V :=
  (Identification.firstFit (Begins (Learning.ahead (Learning.byElimination Learning.lassos) r))
    (fun _ => inferInstance) tbl).map Prod.snd

/-- The entry of a configuration: the configuration as many steps on as the list is long, named
by its first `N - 1` values through the map, from itself on, and labelled with its feature. -/
def entryOf (next : S → S) (reg : S → R) (val : S → V) (l : List S) (x : S) : List R × V :=
  (Law.name next reg (l.length - 1) (Law.orbit next x l.length), val (Law.orbit next x l.length))

/-- The table of the world: an entry for each configuration of the list. -/
def tableOf (next : S → S) (reg : S → R) (val : S → V) (l : List S) : List (List R × V) :=
  l.map (entryOf next reg val l)

/-- A member of a mapped list is the image of a member. -/
theorem mem_map_of {α β : Type _} {g : α → β} : ∀ {l : List α} {b : β}, b ∈ l.map g → ∃ a, a ∈ l ∧ g a = b
  | [], _, mem => nomatch mem
  | a :: l, b, mem =>
    match b, (show b ∈ g a :: l.map g from mem) with
    | _, .head _ => ⟨a, .head l, rfl⟩
    | _, .tail _ mem' => match mem_map_of mem' with
      | ⟨x, inside, at_x⟩ => ⟨x, .tail a inside, at_x⟩

omit [DecidableEq R] in
/-- The table of the world has one entry for each configuration of the list. -/
theorem tableOf_length (next : S → S) (reg : S → R) (val : S → V) (l : List S) :
    (tableOf next reg val l).length = l.length :=
  length_map _ l

omit [DecidableEq R] in
/-- Each name of the table of the world holds `N - 1` values. -/
theorem entryOf_name_length (next : S → S) (reg : S → R) (val : S → V) (l : List S) (x : S) :
    (entryOf next reg val l x).1.length = l.length - 1 :=
  Learning.prefix_length _ _

omit [DecidableEq R] in
/-- Every name of the table of the world holds `N - 1` values. -/
theorem tableOf_names (next : S → S) (reg : S → R) (val : S → V) (l : List S) :
    ∀ e, e ∈ tableOf next reg val l → e.1.length = l.length - 1 :=
  fun _ mem => match mem_map_of mem with
    | ⟨x, _, at_x⟩ => (congrArg (fun e => e.1.length) at_x).symm.trans (entryOf_name_length next reg val l x)

omit [DecidableEq R] in
/-- A future begins with the name of a configuration exactly where its first `N - 1` values are
the configuration's next values through the map. -/
theorem begins_entryOf {next : S → S} {reg : S → R} {val : S → V} {l : List S} {f : Nat → Option R}
    {x : S} :
    Begins f (entryOf next reg val l x) ↔
      ∀ n, n < l.length - 1 → f n = some (reg (Law.orbit next (Law.orbit next x l.length) n)) :=
  have name : (entryOf next reg val l x).1.map some =
      Learning.prefixOf (fun n => some (reg (Law.orbit next (Law.orbit next x l.length) n))) (l.length - 1) :=
    Learning.prefix_map some _ _
  have len : (entryOf next reg val l x).1.length = l.length - 1 := entryOf_name_length next reg val l x
  ⟨fun begins => Identification.prefix_eq_iff.mp
      ((congrArg (Learning.prefixOf f) len).symm.trans (begins.trans name)),
   fun agree => (congrArg (Learning.prefixOf f) len).trans
      ((Identification.prefix_eq_iff.mpr agree).trans name.symm)⟩

/-- **`N` names of `N - 1` values are enough.** In a world a list holds, where configurations with
the same future through the map have features agreeing from some step on, the extrapolation given
the table of the world rests in accord with the feature along every orbit, from the bound of the
extrapolation given nothing on. -/
theorem table_predicts {next : S → S} {reg : S → R} {val : S → V} {l : List S} (world : ∀ s, s ∈ l)
    (agree : ∀ s s', Law.SameFuture next reg s s' →
      ∃ T, ∀ t, T ≤ t → val (Law.orbit next s t) = val (Law.orbit next s' t)) (s : S) :
    PredictsFrom next reg val (byTable (tableOf next reg val l)) s
      (l.length + (l.length + l.length - 1) * Learning.tri l.length) :=
  have closed : ∀ x, x ∈ l → next x ∈ l := fun x _ => world (next x)
  fun t late =>
    have proposed := Learnable.ahead_fixes (fun n => world (Law.orbit next s n)) reg t late
    match gap_of_le (Nat.le_trans (Nat.le_add_right l.length _) late) with
    | ⟨d, gap⟩ =>
      have at_t : Law.orbit next (Law.orbit next s d) l.length = Law.orbit next s t :=
        (Law.orbit_add next s d l.length).symm.trans
          (congrArg (Law.orbit next s) ((Nat.add_comm d l.length).trans gap.symm))
      have ahead_eq : ∀ k, Learning.ahead (Learning.byElimination Learning.lassos)
          (Learning.prefixOf (course next reg s) t) k = some (reg (Law.orbit next (Law.orbit next s t) k)) :=
        fun k => (proposed k).trans (congrArg (fun x => some (reg x)) (Law.orbit_add next s t k))
      have own : Begins (Learning.ahead (Learning.byElimination Learning.lassos)
          (Learning.prefixOf (course next reg s) t)) (entryOf next reg val l (Law.orbit next s d)) :=
        begins_entryOf.mpr fun n _ => (ahead_eq n).trans
          (congrArg (fun x => some (reg (Law.orbit next x n))) at_t.symm)
      have mapped := Identification.firstFit_map
        (p := Begins (Learning.ahead (Learning.byElimination Learning.lassos)
          (Learning.prefixOf (course next reg s) t))) (dec := fun _ => inferInstance)
        (entryOf next reg val l) l
      match Identification.firstFit_found
          (p := fun x => Begins (Learning.ahead (Learning.byElimination Learning.lassos)
            (Learning.prefixOf (course next reg s) t)) (entryOf next reg val l x))
          (dec := fun _ => inferInstance) (world (Law.orbit next s d)) own with
      | ⟨x, found⟩ =>
        have fits := Identification.firstFit_sound found
        have begins := begins_entryOf.mp fits
        have same : Law.SameFuture next reg (Law.orbit next (Law.orbit next s t) 0)
            (Law.orbit next (Law.orbit next x l.length) 0) :=
          (Law.sameFuture_iff_within closed (world _) (world _)).mpr fun n lt =>
            Option.some.inj ((ahead_eq n).symm.trans (begins n lt))
        match agree _ _ same with
        | ⟨_, agrees⟩ =>
          have equal : val (Law.orbit next s t) = val (Law.orbit next x l.length) :=
            eq_of_returns (Law.returns_of_reachable world (Law.reachable_iff.mpr ⟨Law.orbit next s d, at_t⟩))
              (Law.returns_of_reachable world (Law.reachable_iff.mpr ⟨x, rfl⟩)) agrees
          (congrArg (Option.map Prod.snd) (mapped.trans (congrArg (Option.map (entryOf next reg val l)) found))).trans
            (congrArg some equal.symm)

/-- **Learnable exactly where learned from at most `N` labelled names of `N - 1` values.** In a
world a list of `N` holds, a feature is learnable through the map exactly where the extrapolation
given some table of at most `N` labelled names, each of `N - 1` values, rests in accord with it at
every configuration; the table of the world is one where any is. -/
theorem learnable_iff_table {next : S → S} {reg : S → R} {val : S → V} {l : List S}
    (world : ∀ s, s ∈ l) :
    (∃ pred : List R → Option V, ∀ s, Predicts next reg val pred s) ↔
      ∃ tbl : List (List R × V), tbl.length ≤ l.length ∧ (∀ e, e ∈ tbl → e.1.length = l.length - 1) ∧
        ∀ s, Predicts next reg val (byTable tbl) s :=
  ⟨fun learnable => ⟨tableOf next reg val l, Nat.le_of_eq (tableOf_length next reg val l),
      tableOf_names next reg val l, fun s => ⟨_, table_predicts world ((learnable_iff world).mp learnable) s⟩⟩,
   fun ⟨tbl, _, _, rests⟩ => ⟨byTable tbl, rests⟩⟩

/-- **The labels needed.** Every value the feature takes from the step an extrapolation given a
table rests on is a label of an entry of the table. -/
theorem label_of_predicts {next : S → S} {reg : S → R} {val : S → V} {tbl : List (List R × V)}
    {s : S} {T : Nat} (rests : PredictsFrom next reg val (byTable tbl) s T) :
    ∀ t, T ≤ t → ∃ e, e ∈ tbl ∧ e.2 = val (Law.orbit next s t) :=
  fun t late =>
    match found : Identification.firstFit (Begins (Learning.ahead (Learning.byElimination Learning.lassos)
        (Learning.prefixOf (course next reg s) t))) (fun _ => inferInstance) tbl with
    | some e => ⟨e, Identification.firstFit_mem found,
        Option.some.inj ((congrArg (Option.map Prod.snd) found).symm.trans (rests t late))⟩
    | none => nomatch (congrArg (Option.map Prod.snd) found).symm.trans (rests t late)

/-- **Where the law leaves every configuration unchanged, every value the feature takes is a
label.** An extrapolation given a table resting in accord with the feature at every configuration
has every value of the feature among the table's labels. -/
theorem labels_of_still {next : S → S} (still : ∀ s, next s = s) {reg : S → R} {val : S → V}
    {tbl : List (List R × V)} (rests : ∀ s, Predicts next reg val (byTable tbl) s) (s : S) :
    ∃ e, e ∈ tbl ∧ e.2 = val s :=
  match rests s with
  | ⟨T, at_s⟩ => match label_of_predicts at_s T (Nat.le_refl T) with
    | ⟨e, mem, label⟩ => ⟨e, mem, label.trans (congrArg val (orbit_of_still (still s) T))⟩

end Table

/-! ## Labels along the course -/

section AlongTheCourse

variable {S : Type u} {R : Type v} {V : Type w} [DecidableEq R] [DecidableEq V]

/-- **With the feature carried by the map along the course, every feature is learned given
nothing.** In a world a list holds, the extrapolation by elimination over the lasso candidates,
reading the map paired with the feature, rests in accord with the feature from the bound on. An
instance of `predicts_through`. -/
theorem predicts_with_labels {next : S → S} {s : S} {l : List S} (held : ∀ n, Law.orbit next s n ∈ l)
    (reg : S → R) (val : S → V) :
    PredictsFrom next (fun x => (reg x, val x)) val
      (fun r => (Learning.byElimination Learning.lassos r).map Prod.snd) s
      (l.length + (l.length + l.length - 1) * Learning.tri l.length) :=
  predicts_through held (reg := fun x => (reg x, val x)) (g := Prod.snd) fun _ => rfl

/-- **The labels before the bound fix every later one.** In a world a list holds, from the bound
on, the extrapolation by elimination over the lasso candidates, reading the map paired with the
feature and unrolled on its own proposals, proposes the feature `k` steps ahead for every
`k`. An instance of `ahead_fixes`. -/
theorem ahead_with_labels {next : S → S} {s : S} {l : List S} (held : ∀ n, Law.orbit next s n ∈ l)
    (reg : S → R) (val : S → V) :
    ∀ t, l.length + (l.length + l.length - 1) * Learning.tri l.length ≤ t → ∀ k,
      (Learning.ahead (Learning.byElimination Learning.lassos)
          (Learning.prefixOf (course next (fun x => (reg x, val x)) s) t) k).map Prod.snd =
        some (val (Law.orbit next s (t + k))) :=
  fun t late k => congrArg (Option.map Prod.snd) (ahead_fixes held (fun x => (reg x, val x)) t late k)

end AlongTheCourse

end Learnable

/-! ## Along runs -/

namespace LearnableRuns

section Table

variable {S : Type} {R : Type} {V : Type} [DecidableEq R] {next : S → S}

/-- **`N` names of `N - 1` values are enough, along runs.** In a world a list holds, where runs
beginning alike in the frame have features agreeing from some step on, the extrapolation given the
table of the world rests in accord with the feature along every run of the law. -/
theorem table_predicts {reg : S → R} {val : S → V} {l : List S} (world : ∀ s, s ∈ l)
    (agree : ∀ r r' : Run (Law.process next),
      Alike (Law.frameBy next reg) (Law.frameBy next reg) (r.state 0) (r'.state 0) →
        ∃ T, ∀ t, T ≤ t → val (r.state t) = val (r'.state t))
    (r : Run (Law.process next)) :
    Predicts reg val (Learnable.byTable (Learnable.tableOf next reg val l)) r :=
  (predicts_iff r).mpr ⟨_, Learnable.table_predicts world
    (fun s s' same => match agree (Law.run next s) (Law.run next s') (Law.alike_iff_sameFuture.mpr same) with
      | ⟨T, agrees⟩ => ⟨T, fun t late =>
        (congrArg val (Branching.law_run_state (Law.run next s) t)).symm.trans
          ((agrees t late).trans (congrArg val (Branching.law_run_state (Law.run next s') t)))⟩)
    (r.state 0)⟩

/-- **Learnable along runs exactly where learned from at most `N` labelled names of `N - 1`
values.** -/
theorem learnable_iff_table {reg : S → R} {val : S → V} {l : List S} (world : ∀ s, s ∈ l) :
    (∃ pred : List R → Option V, ∀ r : Run (Law.process next), Predicts reg val pred r) ↔
      ∃ tbl : List (List R × V), tbl.length ≤ l.length ∧ (∀ e, e ∈ tbl → e.1.length = l.length - 1) ∧
        ∀ r : Run (Law.process next), Predicts reg val (Learnable.byTable tbl) r :=
  ⟨fun ⟨pred, rests⟩ =>
    match (Learnable.learnable_iff_table (next := next) (reg := reg) (val := val) world).mp
        ⟨pred, fun s => (predicts_iff (Law.run next s)).mp (rests (Law.run next s))⟩ with
    | ⟨tbl, few, names, rests'⟩ => ⟨tbl, few, names, fun r => (predicts_iff r).mpr (rests' (r.state 0))⟩,
   fun ⟨tbl, _, _, rests⟩ => ⟨Learnable.byTable tbl, rests⟩⟩

/-- **Where the law leaves every configuration unchanged, every value the feature takes is a
label**, of a table whose extrapolation rests in accord with the feature along every run. -/
theorem labels_of_still (still : ∀ s, next s = s) {reg : S → R} {val : S → V}
    {tbl : List (List R × V)}
    (rests : ∀ r : Run (Law.process next), Predicts reg val (Learnable.byTable tbl) r) (s : S) :
    ∃ e, e ∈ tbl ∧ e.2 = val s :=
  Learnable.labels_of_still still (fun s => (predicts_iff (Law.run next s)).mp (rests (Law.run next s))) s

end Table

section AlongTheCourse

variable {S : Type u} {R : Type v} {V : Type w} [DecidableEq R] [DecidableEq V] {next : S → S}

/-- **With the feature carried by the map along a run, every feature is learned given nothing**, along
every run of the law a list holds. -/
theorem predicts_with_labels (r : Run (Law.process next)) {l : List S} (held : ∀ n, r.state n ∈ l)
    (reg : S → R) (val : S → V) :
    PredictsFrom (fun x => (reg x, val x)) val
      (fun x => (Learning.byElimination Learning.lassos x).map Prod.snd) r
      (l.length + (l.length + l.length - 1) * Learning.tri l.length) :=
  (predictsFrom_iff r _).mpr
    (Learnable.predicts_with_labels
      (fun n => Eq.subst (motive := fun x => x ∈ l) (Branching.law_run_state r n) (held n)) reg val)

/-- **The labels before the bound fix every later one, along a run.** Along every run of the law a
list holds, from the bound on, the extrapolation by elimination over the lasso candidates, reading
the map paired with the feature and unrolled on its own proposals, proposes the feature `k` steps
ahead for every `k`. -/
theorem ahead_with_labels (r : Run (Law.process next)) {l : List S} (held : ∀ n, r.state n ∈ l)
    (reg : S → R) (val : S → V) :
    ∀ t, l.length + (l.length + l.length - 1) * Learning.tri l.length ≤ t → ∀ k,
      (Learning.ahead (Learning.byElimination Learning.lassos)
          (Learning.prefixOf (course (fun x => (reg x, val x)) r) t) k).map Prod.snd =
        some (val (r.state (t + k))) :=
  fun t late k =>
    (congrArg (fun x => (Learning.ahead (Learning.byElimination Learning.lassos) x k).map Prod.snd)
        (prefix_eq (fun x => (reg x, val x)) r t)).trans
      ((Learnable.ahead_with_labels
          (fun n => Eq.subst (motive := fun x => x ∈ l) (Branching.law_run_state r n) (held n))
          reg val t late k).trans
        (congrArg (fun x => some (val x)) (Branching.law_run_state r (t + k)).symm))

end AlongTheCourse

end LearnableRuns

end Becoming
