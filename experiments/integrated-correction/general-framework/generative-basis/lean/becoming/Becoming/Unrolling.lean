import Becoming.LearnableRuns

/-!
# Unrolling: what an extrapolation given nothing fixes

`Becoming.Learnable` states what an extrapolation from prefixes through a map `reg : S → R` can
come to rest in accord with: a feature `val : S → V` is learnable in a world a list holds exactly
where configurations with the same future through the map have features agreeing from some step
on (`Learnable.learnable_iff`), the extrapolation of the second direction being built from the
law, the configurations and the feature (`Learnable.fromLaw`). Given nothing, the extrapolation by
elimination over the lasso candidates proposes the next value through the map
(`Identification.held_byElimination_rests`). This module states what that extrapolation fixes and
what it needs to be given, with no premise.

* **Unrolling.** An extrapolation can be unrolled on its own proposals: each proposed value is put
  at the front of the prefix, latest first, as `Learning.prefixOf` keeps it
  (`Learning.unroll`), and what it proposes `k` steps ahead is read off the unrolled prefix
  (`Learning.ahead`). Where it proposes the course's value at every step from some step on, the
  prefix unrolled from any later step is the course's prefix (`Learning.unroll_prefix`), and it
  proposes the course's value at every step ahead (`Learning.ahead_accords`).
* **Given nothing, the whole future through the map is fixed.** In every world a list holds, from
  `Becoming.Identification`'s bound on, the extrapolation by elimination over the lasso candidates,
  unrolled, proposes at every step ahead the value through the map that many steps on
  (`Learnable.ahead_fixes`). It is given neither the configurations, nor how many there are, nor
  the law, nor any feature. Over every course no prefix fixes the next value
  (`Learning.no_prefix_fixes_next`); what fixes it here is that a list holds the world.
* **A feature needs its reading.** Where a feature is a reading of the future through the map
  (`Learnable.ReadOff`: `val s` is `G` of the values through the map along the orbit from `s`), the
  extrapolation given only that reading rests in accord with the feature from the same bound on
  (`Learnable.reading_predicts`), for a reading respecting values at each step (no function
  extensionality is assumed). This extends `Learnable.predicts_through`, where the feature is read off
  the present value only.
* **Given nothing, not every learnable feature.** With one configuration and one value through the
  map, the feature `true` and the feature `false` are each learned by the extrapolation given its
  reading, and no single extrapolation rests in accord with both (`Learnable.given_nothing_not_every`):
  the prefixes are the same in both, so what an extrapolation proposes is the same.

* **Learnable exactly where a reading of the future.** In a world a list holds, a feature is
  learnable through the map exactly where some reading of futures, respecting values at each step,
  is the feature from some step on along every orbit (`Learnable.learnable_iff_reading`). The
  reading of the first direction is built from the list, the law and the feature
  (`Learnable.fromWorld`):
  configurations as many steps on as the list is long return (`Law.returns_of_reachable`), and
  returning configurations whose features agree from some step on have equal features
  (`Learnable.eq_of_returns`), so on them the feature is fixed by the future
  (`Learnable.reads_of_agree`). Then the extrapolation given the reading learns the feature
  (`Learnable.reading_predicts_from`).

* **Along runs.** A determined law is a process of the spine whose runs are its orbits; the
  whole future fixed given nothing, the exact reading and the witness hold along its runs
  (`LearnableRuns.ahead_fixes`, `LearnableRuns.learnable_iff_reading`,
  `LearnableRuns.given_nothing_not_every`), proved through the laws above and
  `Becoming.LearnableRuns`.

So the prefix alone fixes the future through the map; what a learnable feature adds to it is
exactly a reading of that future, which an extrapolation given nothing does not have. No ethical
predicate, ranking or axiom occurs.
-/

namespace Becoming

universe u v w

namespace Learning

variable {O : Type u}

/-- A prefix extended by an extrapolation's proposal: the proposed value is put at the front,
latest first; where the extrapolation stays silent the prefix is kept. -/
def extendBy (pred : List O → Option O) (l : List O) : List O :=
  match pred l with
  | some v => v :: l
  | none => l

theorem extendBy_of {pred : List O → Option O} {l : List O} {v : O} (proposes : pred l = some v) :
    extendBy pred l = v :: l := by
  unfold extendBy
  rw [proposes]

/-- A prefix unrolled `k` steps on an extrapolation's own proposals. -/
def unroll (pred : List O → Option O) (l : List O) : Nat → List O
  | 0 => l
  | k + 1 => extendBy pred (unroll pred l k)

/-- What an extrapolation proposes `k` steps ahead of a prefix, unrolling its own proposals. -/
def ahead (pred : List O → Option O) (l : List O) (k : Nat) : Option O :=
  pred (unroll pred l k)

/-- **Unrolled where it accords, the prefix is the course's.** Where an extrapolation proposes the
course's value at every step from `N` on, the prefix before any step `t` from `N` on, unrolled `k`
steps, is the prefix before `t + k`. -/
theorem unroll_prefix {pred : List O → Option O} {o : Nat → O} {N : Nat}
    (accords : ∀ u, N ≤ u → pred (prefixOf o u) = some (o u)) {t : Nat} (late : N ≤ t) :
    ∀ k, unroll pred (prefixOf o t) k = prefixOf o (t + k)
  | 0 => rfl
  | k + 1 => (congrArg (extendBy pred) (unroll_prefix accords late k)).trans
      (extendBy_of (accords (t + k) (Nat.le_trans late (Nat.le_add_right t k))))

/-- **Unrolled where it accords, it proposes the course ahead.** -/
theorem ahead_accords {pred : List O → Option O} {o : Nat → O} {N : Nat}
    (accords : ∀ u, N ≤ u → pred (prefixOf o u) = some (o u)) {t : Nat} (late : N ≤ t) (k : Nat) :
    ahead pred (prefixOf o t) k = some (o (t + k)) :=
  (congrArg pred (unroll_prefix accords late k)).trans
    (accords (t + k) (Nat.le_trans late (Nat.le_add_right t k)))

end Learning

namespace Learnable

section GivenNothing

variable {S : Type u} {R : Type v} {V : Type w} [DecidableEq R]

/-- **Given nothing, the whole future through the map is fixed.** In a world a list holds, from
`Becoming.Identification`'s bound on, the extrapolation by elimination over the lasso candidates,
unrolled on its own proposals, proposes `k` steps ahead the value through the map `k` steps on,
for every `k`. -/
theorem ahead_fixes {next : S → S} {s : S} {l : List S} (held : ∀ n, Law.orbit next s n ∈ l)
    (reg : S → R) :
    ∀ t, l.length + (l.length + l.length - 1) * Learning.tri l.length ≤ t → ∀ k,
      Learning.ahead (Learning.byElimination Learning.lassos)
          (Learning.prefixOf (course next reg s) t) k =
        some (reg (Law.orbit next s (t + k))) :=
  fun _ late k => Learning.ahead_accords (Identification.held_byElimination_rests held reg) late k

/-- A feature is read off the future through the map by `G`: at every configuration, it is `G` of
the values through the map along the orbit from there. -/
def ReadOff (next : S → S) (reg : S → R) (val : S → V) (G : (Nat → Option R) → V) : Prop :=
  ∀ s, val s = G fun k => some (reg (Law.orbit next s k))

/-- The extrapolation given a reading of futures: it unrolls the extrapolation by elimination over
the lasso candidates and proposes the reading of what that proposes ahead. -/
def reading (G : (Nat → Option R) → V) (r : List R) : Option V :=
  some (G (Learning.ahead (Learning.byElimination Learning.lassos) r))

/-- **A feature read off the future is learned given its reading.** In a world a list holds,
where the feature is read off the future through the map by a reading respecting values at each
step, the extrapolation given that reading rests in accord with the feature from
`Becoming.Identification`'s bound on. It is given neither the configurations, nor how many there
are, nor the law, nor any value of the feature. -/
theorem reading_predicts {next : S → S} {s : S} {l : List S} (held : ∀ n, Law.orbit next s n ∈ l)
    {reg : S → R} {val : S → V} {G : (Nat → Option R) → V}
    (respects : ∀ f f' : Nat → Option R, (∀ k, f k = f' k) → G f = G f')
    (read : ReadOff next reg val G) :
    PredictsFrom next reg val (reading G) s
      (l.length + (l.length + l.length - 1) * Learning.tri l.length) :=
  fun t late => congrArg some ((respects _ _ fun k => (ahead_fixes held reg t late k).trans
      (congrArg (fun x => some (reg x)) (Law.orbit_add next s t k))).trans
    (read (Law.orbit next s t)).symm)

/-- **Given nothing, not every learnable feature.** With one configuration and one value through
the map, the feature `true` and the feature `false` are each learned by the extrapolation given its
reading (each a reading of the future, by a constant), and no single extrapolation rests in accord
with both: the prefixes are the same, so are its proposals. -/
theorem given_nothing_not_every :
    (∀ b : Bool, Predicts (fun _ : Unit => ()) (fun _ => ()) (fun _ => b)
      (reading fun _ => b) ()) ∧
    ¬ ∃ pred : List Unit → Option Bool, ∀ b : Bool,
      Predicts (fun _ : Unit => ()) (fun _ => ()) (fun _ => b) pred () :=
  ⟨fun _ => ⟨_, reading_predicts (l := [()]) (fun _ => List.Mem.head _) (fun _ _ _ => rfl)
      fun _ => rfl⟩,
   fun ⟨_, rests⟩ => match rests true, rests false with
    | ⟨T, yes⟩, ⟨T', no⟩ => Bool.noConfusion (Option.some.inj
        ((yes (T + T') (Nat.le_add_right T T')).symm.trans (no (T + T') (Nat.le_add_left T' T))))⟩

end GivenNothing

/-! ## Exactly a reading -/

section ExactlyReading

/-- **Returning configurations whose features agree from some step on have equal features.** -/
theorem eq_of_returns {S : Type u} {V : Type w} {next : S → S} {val : S → V} {x y : S}
    (back : Law.Returns next x) (back' : Law.Returns next y) {T : Nat}
    (agrees : ∀ t, T ≤ t → val (Law.orbit next x t) = val (Law.orbit next y t)) : val x = val y :=
  match Law.returns_iff.mp back, Law.returns_iff.mp back' with
  | ⟨p + 1, _, at_x⟩, ⟨q + 1, _, at_y⟩ =>
    have back_x : Law.orbit next x ((p + 1) * (q + 1)) = x := Law.orbit_mul at_x (q + 1)
    have back_y : Law.orbit next y ((p + 1) * (q + 1)) = y :=
      (congrArg (Law.orbit next y) (Nat.mul_comm (p + 1) (q + 1))).trans (Law.orbit_mul at_y (p + 1))
    have late : T ≤ (p + 1) * (q + 1) * T :=
      Nat.le_trans (Nat.le_add_left T ((p * (q + 1) + q) * T))
        (Nat.le_of_eq ((Nat.succ_mul (p * (q + 1) + q) T).symm.trans
          (congrArg (fun n => n * T) (Nat.succ_mul p (q + 1)).symm)))
    (congrArg val (Law.orbit_mul back_x T)).symm.trans
      ((agrees _ late).trans (congrArg val (Law.orbit_mul back_y T)))

variable {S : Type} {R : Type v} {V : Type w} [DecidableEq R]

/-- The configuration of `l` read for a future: the first whose configuration as many steps on as
the list is long has that future through the map before `2N - 1`. -/
def readAt (next : S → S) (reg : S → R) (l : List S) (f : Nat → Option R) : Option S :=
  Identification.firstFit
    (fun x => Learning.prefixOf f (l.length + l.length - 1) =
      Learning.prefixOf (fun n => some (reg (Law.orbit next (Law.orbit next x l.length) n)))
        (l.length + l.length - 1))
    (fun _ => decEq _ _) l

/-- **The reading built from the list** (with the law, the map and the feature): the feature of
the configuration read for a future, as many steps on as the list is long; `v₀` where no
configuration of the list is read. -/
def fromWorld (next : S → S) (reg : S → R) (val : S → V) (l : List S) (v₀ : V)
    (f : Nat → Option R) : V :=
  (readAt next reg l f).elim v₀ fun x => val (Law.orbit next x l.length)

theorem fromWorld_respects (next : S → S) (reg : S → R) (val : S → V) (l : List S) (v₀ : V) :
    ∀ f f' : Nat → Option R, (∀ k, f k = f' k) →
      fromWorld next reg val l v₀ f = fromWorld next reg val l v₀ f' :=
  fun _ _ same =>
    have prefixes := Identification.prefix_eq_iff.mpr fun n _ => same n
    congrArg (fun o => Option.elim o v₀ fun x => val (Law.orbit next x l.length))
      (Learnable.firstFit_congr fun _ _ => ⟨fun h => prefixes.symm.trans h, fun h => prefixes.trans h⟩)

/-- **Where features agree across the same future, each is a reading of the future.** In a world
a list holds, where configurations with the same future through the map have features agreeing
from some step on, the feature at every configuration as many steps on as the list is long is the
reading built from the list of its future. -/
theorem reads_of_agree {next : S → S} {reg : S → R} {val : S → V} {l : List S}
    (world : ∀ s, s ∈ l) (v₀ : V)
    (agree : ∀ s s', Law.SameFuture next reg s s' →
      ∃ T, ∀ t, T ≤ t → val (Law.orbit next s t) = val (Law.orbit next s' t)) (y : S) :
    val (Law.orbit next y l.length) =
      fromWorld next reg val l v₀ fun k => some (reg (Law.orbit next (Law.orbit next y l.length) k)) :=
  have closed : ∀ x, x ∈ l → next x ∈ l := fun x _ => world (next x)
  match Identification.firstFit_found
      (p := fun x => Learning.prefixOf
          (fun k => some (reg (Law.orbit next (Law.orbit next y l.length) k)))
          (l.length + l.length - 1) =
        Learning.prefixOf (fun n => some (reg (Law.orbit next (Law.orbit next x l.length) n)))
          (l.length + l.length - 1))
      (dec := fun _ => decEq _ _) (world y) rfl with
  | ⟨b, found⟩ =>
    have fits : Learning.prefixOf
          (fun k => some (reg (Law.orbit next (Law.orbit next y l.length) k)))
          (l.length + l.length - 1) =
        Learning.prefixOf (fun n => some (reg (Law.orbit next (Law.orbit next b l.length) n)))
          (l.length + l.length - 1) := Identification.firstFit_sound found
    have same : Law.SameFuture next reg (Law.orbit next b l.length) (Law.orbit next y l.length) :=
      (Law.sameFuture_iff_below closed (world _) (world _)).mpr fun n lt =>
        (Option.some.inj (Identification.prefix_eq_iff.mp fits n lt)).symm
    match agree _ _ same with
    | ⟨_, agrees⟩ =>
      (eq_of_returns (Law.returns_of_reachable world (Law.reachable_iff.mpr ⟨b, rfl⟩))
          (Law.returns_of_reachable world (Law.reachable_iff.mpr ⟨y, rfl⟩)) agrees).symm.trans
        (congrArg (fun o => Option.elim o v₀ fun x => val (Law.orbit next x l.length)) found).symm

/-- **A feature that is a reading of the future from some step on is learned given its reading.**
In a world a list holds, where from some step on along the orbit from `s` the feature is a reading
of the future through the map, respecting values at each step, the extrapolation given that
reading rests in accord with the feature. -/
theorem reading_predicts_from {next : S → S} {s : S} {l : List S} (held : ∀ n, Law.orbit next s n ∈ l)
    {reg : S → R} {val : S → V} {G : (Nat → Option R) → V}
    (respects : ∀ f f' : Nat → Option R, (∀ k, f k = f' k) → G f = G f') {T : Nat}
    (read : ∀ t, T ≤ t → val (Law.orbit next s t) =
      G fun k => some (reg (Law.orbit next (Law.orbit next s t) k))) :
    PredictsFrom next reg val (reading G) s
      (T + (l.length + (l.length + l.length - 1) * Learning.tri l.length)) :=
  fun t late => congrArg some ((respects _ _ fun k =>
      (ahead_fixes held reg t (Nat.le_trans (Nat.le_add_left _ T) late) k).trans
        (congrArg (fun x => some (reg x)) (Law.orbit_add next s t k))).trans
    (read t (Nat.le_trans (Nat.le_add_right T _) late)).symm)

/-- **Learnable exactly where a reading of the future.** In a world a list holds, a feature is
learnable through the map exactly where some reading of futures, respecting values at each step,
is the feature from some step on along every orbit. The reading of the first direction is given
the world, the law and the feature (`fromWorld`); in the second, the extrapolation given the
reading learns the feature (`reading`). -/
theorem learnable_iff_reading {next : S → S} {reg : S → R} {val : S → V} {l : List S}
    (world : ∀ s, s ∈ l) (v₀ : V) :
    (∃ pred : List R → Option V, ∀ s, Predicts next reg val pred s) ↔
      ∃ G : (Nat → Option R) → V, (∀ f f' : Nat → Option R, (∀ k, f k = f' k) → G f = G f') ∧
        ∀ s, ∃ T, ∀ t, T ≤ t → val (Law.orbit next s t) =
          G fun k => some (reg (Law.orbit next (Law.orbit next s t) k)) :=
  ⟨fun learnable => ⟨fromWorld next reg val l v₀, fromWorld_respects next reg val l v₀, fun s =>
      ⟨l.length, fun t late =>
        match le_dest late with
        | ⟨d, gap⟩ =>
          have at_t : Law.orbit next (Law.orbit next s d) l.length = Law.orbit next s t :=
            (Law.orbit_add next s d l.length).symm.trans
              (congrArg (Law.orbit next s) ((Nat.add_comm d l.length).trans gap.symm))
          (congrArg val at_t).symm.trans
            ((reads_of_agree world v₀ ((learnable_iff world).mp learnable) (Law.orbit next s d)).trans
              (congrArg (fun x => fromWorld next reg val l v₀ fun k => some (reg (Law.orbit next x k)))
                at_t))⟩⟩,
   fun ⟨_, respects, read⟩ => ⟨reading _, fun s =>
      match read s with
      | ⟨_, at_s⟩ => ⟨_, reading_predicts_from (fun _ => world _) respects at_s⟩⟩⟩

end ExactlyReading

end Learnable

/-! ## Along runs -/

namespace LearnableRuns

section GivenNothing

variable {S : Type u} {R : Type v} {V : Type w} [DecidableEq R] {next : S → S}

/-- **Given nothing, the whole future along a run is fixed.** Along every run of the law a list
holds, from `Becoming.Identification`'s bound on, the extrapolation by elimination over the lasso
candidates, unrolled on its own proposals, proposes `k` steps ahead the value through the map at
the run's configuration `k` steps on. -/
theorem ahead_fixes (r : Run (Law.process next)) {l : List S} (held : ∀ n, r.state n ∈ l)
    (reg : S → R) :
    ∀ t, l.length + (l.length + l.length - 1) * Learning.tri l.length ≤ t → ∀ k,
      Learning.ahead (Learning.byElimination Learning.lassos)
          (Learning.prefixOf (course reg r) t) k =
        some (reg (r.state (t + k))) :=
  fun t late k =>
    (congrArg (fun x => Learning.ahead (Learning.byElimination Learning.lassos) x k)
        (prefix_eq reg r t)).trans
      ((Learnable.ahead_fixes
          (fun n => Eq.subst (motive := fun x => x ∈ l) (Branching.law_run_state r n) (held n))
          reg t late k).trans
        (congrArg (fun x => some (reg x)) (Branching.law_run_state r (t + k)).symm))

/-- **Given nothing, not every feature learnable along runs.** Along the run of the law on one
configuration, the feature `true` and the feature `false` are each learned by the extrapolation
given its reading, and no single extrapolation rests in accord with both. -/
theorem given_nothing_not_every :
    (∀ b : Bool, ∀ r : Run (Law.process fun _ : Unit => ()),
      Predicts (fun _ => ()) (fun _ => b) (Learnable.reading fun _ => b) r) ∧
    ¬ ∃ pred : List Unit → Option Bool, ∀ b : Bool, ∀ r : Run (Law.process fun _ : Unit => ()),
      Predicts (fun _ => ()) (fun _ => b) pred r :=
  ⟨fun b r => (predicts_iff r).mpr (Learnable.given_nothing_not_every.1 b),
   fun ⟨pred, rests⟩ => Learnable.given_nothing_not_every.2
      ⟨pred, fun b => (predicts_iff (Law.run _ ())).mp (rests b (Law.run _ ()))⟩⟩

end GivenNothing

section ExactlyReading

variable {S : Type} {R : Type v} {V : Type w} [DecidableEq R] {next : S → S}

omit [DecidableEq R] in
/-- The future through the map along a run from step `t`, written along the orbit. -/
theorem future_eq (reg : S → R) (r : Run (Law.process next)) (t k : Nat) :
    some (reg (r.state (t + k))) = some (reg (Law.orbit next (Law.orbit next (r.state 0) t) k)) :=
  congrArg (fun x => some (reg x))
    ((Branching.law_run_state r (t + k)).trans (Law.orbit_add next (r.state 0) t k))

/-- **Learnable along runs exactly where a reading of the future.** In a world a list holds, a
feature is learnable along every run of the law exactly where some reading of futures, respecting
values at each step, is the feature from some step on along every run, read of the future along
the run. -/
theorem learnable_iff_reading {reg : S → R} {val : S → V} {l : List S} (world : ∀ s, s ∈ l)
    (v₀ : V) :
    (∃ pred : List R → Option V, ∀ r : Run (Law.process next), Predicts reg val pred r) ↔
      ∃ G : (Nat → Option R) → V, (∀ f f' : Nat → Option R, (∀ k, f k = f' k) → G f = G f') ∧
        ∀ r : Run (Law.process next), ∃ T, ∀ t, T ≤ t →
          val (r.state t) = G fun k => some (reg (r.state (t + k))) :=
  ⟨fun ⟨pred, rests⟩ =>
    match (Learnable.learnable_iff_reading (next := next) (reg := reg) (val := val) world v₀).mp
        ⟨pred, fun s => (predicts_iff (Law.run next s)).mp (rests (Law.run next s))⟩ with
    | ⟨G, respects, read⟩ => ⟨G, respects, fun r =>
      match read (r.state 0) with
      | ⟨T, at_s⟩ => ⟨T, fun t late =>
        (congrArg val (Branching.law_run_state r t)).trans
          ((at_s t late).trans (respects _ _ fun k => (future_eq reg r t k).symm))⟩⟩,
   fun ⟨G, respects, read⟩ =>
    match (Learnable.learnable_iff_reading (next := next) (reg := reg) (val := val) world v₀).mpr
        ⟨G, respects, fun s => match read (Law.run next s) with
          | ⟨T, at_r⟩ => ⟨T, fun t late =>
            (at_r t late).trans (respects _ _ fun k => future_eq reg (Law.run next s) t k)⟩⟩ with
    | ⟨pred, rests⟩ => ⟨pred, fun r => (predicts_iff r).mpr (rests (r.state 0))⟩⟩

end ExactlyReading

end LearnableRuns

end Becoming
