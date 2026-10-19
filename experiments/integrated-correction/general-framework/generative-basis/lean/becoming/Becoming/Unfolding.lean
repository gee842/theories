import Becoming.Labelled
import Becoming.Mechanism
import Becoming.Space

/-!
# One unfolding and its readings

Ren asked of the core's first two layers, `Process S A` and `Frame`, on 12 October 2026: "is
this dualistic?" They posit no subject and object, but their form takes four splits as given:
a configuration and a move drawn from an alphabet of its own; a law supplied before the history
it governs; claims read off a configuration; and configurations given before the relation among
them. `World` (`Becoming.World`) takes none of them: one kind of relatum, with what each takes,
gives, stands at, needs and draws at each step. This module states the four splits from the
world's side, with no premise beyond what each theorem names, so that the labelled process and
the frame are readings of one unfolding rather than its ground.

The readings that need only the frame and the world (`withMove` and its round trips, `Shown`,
`Shown.run`, `shown_le_iff`, `Consistent`, `DeadEnd`, `Splice`, `exchange`, `Frame.world`,
`Frame.world_fixes_run`, `Bisimulation`, `Alike`, `IdentifiesAlike`, `Circulation` and the rest)
are stated in `Becoming.Labelled`, which this module imports, and `Exchange` and `World.move` in
`Becoming.World`; their names are unchanged. This module states the readings that also need laws
of the world (`Flow.Balances`, `Web.Arises`, `coming_recurs_iff`) or of the process
(`Determined`, `GoAlike`, `carries_law_iff`, `keepHistory`, `Law.orbit`), and the list below
covers both.

* **The move is part of what the unfolding is.** Read with the move inside the configuration
  (`withMove`), a process has the same runs, read two ways (`Run.toWithMove`, `Run.ofWithMove`).
  The law then leaves the next move open (`withMove_open`), and it is determined exactly where
  it is determined with moves as labels and, wherever it takes a step, only one move exists
  (`withMove_determined_iff`). Where the move is formed within the unfolding by a policy of the
  configuration (`closedBy`), a determined law stays determined (`closedBy_determined`) and two
  runs from one configuration agree at every step (`closedBy_runs_agree`, through
  `GoAlike.runs_agree` of `Becoming.Mechanism`). Between parts, a shared move is a relation:
  in the synchronized product two forking parts cannot go different ways at once, while with
  the move forgotten in each part first they can (`unlabelled_product_le`,
  `Fork.label_couples`). In a world the move is the relata's own exchange (`Exchange`,
  `World.move`): a world balances exactly where its standings run by the law of exchange
  (`World.balances_iff_exchange`), across one step exactly where it balances on every family
  there (`World.exchange_step_iff`), and is then a run of that law (`World.exchangeRun`). The
  exchange fixes the standings after it (`exchange_agrees`) and, from a beginning, at every
  step (`exchange_runs_agree`); without the beginning it does not, and the standings do not fix
  the exchange (`Circulation.start_needed`, `Circulation.standings_leave_exchange`).
* **A history fixes the law it shows.** Every sequence of configurations and moves is a run of
  the law it shows (`Shown`, `Shown.run`), the least law it is a run of (`shown_le_iff`); two
  laws take the same steps exactly when they have the same traces (`same_steps_iff_traces`). That
  law is determined exactly where the history never takes one move at one configuration to two
  outcomes (`Consistent`, `shown_determined_iff`), and so some determined law admits the history
  exactly then (`exists_law_iff`, through `carries_law_iff` of `Becoming.Mechanism`). Every
  determined law of the history repeats what it shows (`Shown.agrees`). The correspondence is
  not an identity. A law can have a step and no history (`DeadEnd.no_history`); where a history
  revisits a configuration, the law it shows admits a history it never took
  (`Splice.spliced`); where it never revisits, the law admits only the history
  (`Shown.runs_of_new`), so the law a kept history shows admits only it
  (`Run.keepHistory_shown`), at the price `Becoming.Recurrence` states: a kept history never
  returns. What a law supplied before the history adds is its moves not taken, which the
  record does not fix (`Run.not_fixes_of_untaken` of `Becoming.Experiment`); a law that changes
  is a law on the configuration with its rule (`adaptive` of `Becoming.Mechanism`).
* **A claim is a relatum; being realized is its activity.** A frame along a run is a world whose
  relata are its claims, each active exactly where it is realized (`Frame.world`,
  `Frame.world_active`). A claim realized anew is a relatum arising (`Frame.arises_iff`,
  `Frame.novel_iff_arises`), so the laws of activity hold of claims: in a finite family of
  decided claims, coming to be realized recurs exactly where ceasing to be realized recurs
  (`Frame.claims_recur_iff`). With configurations as claims (`Frame.configurations`) every run
  is a world, and the world fixes the run (`Frame.world_fixes_run`).
* **A configuration is how it relates.** Configurations are alike (`Alike`) where some
  bisimulation relates them (`Bisimulation`): they realize the same claims and match each
  other's steps by the same moves into alike configurations. Likeness is an equivalence
  (`Alike.refl`, `Alike.symm`, `Alike.trans`), stated as a relation since a quotient needs
  `Quot.sound`. Alike configurations admit the same courses of moves into alike configurations
  (`Alike.trace`) and pass the same tests, a course of moves followed by a claim
  (`Alike.tests`). This brings into the core the periphery's relational identity of
  configurations (`RelationalDynamics`, 6 October 2026, and the branching tests of
  `ExplanatoryBranching`), which `Becoming.Bridge` shows to be this one. There a step that
  leaves the configuration unchanged was found to read the carrier's equality
  (`unchanged_reads_carrier_identity`); so does determinacy as equality: the twins have two
  successors alike in every relation, are alike to a determined frame, and are not determined
  (`Twins.not_determined`, `Twins.alike_one`, `Twins.left_alike_right`). Determinacy
  up to likeness (`DeterminedAt`) passes along likeness (`DeterminedAt.transfer`), and alike
  configurations go alike under it (`DeterminedAt.goAlike`). Under the law of exchange,
  standings are alike exactly where they agree at every relatum (`exchange_alike_iff`), and the
  law is determined up to likeness (`exchange_determinedAt`). A description of configurations
  makes sense where it identifies exactly the alike ones (`IdentifiesAlike`): exactly where what it
  identifies relate alike and it identifies whatever is alike (`identifiesAlike_iff`). Descriptions
  that make sense identify the same configurations (`IdentifiesAlike.unique`) and, where the frame is
  determined up to likeness, carry a law (`IdentifiesAlike.carries`); naming the configurations makes
  sense exactly where alike configurations are one (`identifiesAlike_id_iff`), and the twins' naming
  does not (`Twins.naming_not_identifiesAlike`). For a determined law read through a map
  (`Law.frameBy`), configurations are alike exactly where their futures through the map are the
  same (`Law.SameFuture`, `Law.alike_iff_sameFuture`), so there a description makes sense where
  it identifies exactly the same futures through the map, and it carries a law
  (`Law.IdentifiesAlike.carries`).

The results on dead ends, splicing, kept history, coupling and standing and passing restate on
these definitions theorems checked on the branch "Current math core (fork 2)" of the same
conversation, 12 October 2026, and those on descriptions that make sense restate, for frames
that branch and carry claims, the `IdentifiesAlike` checked on the branch "Current math core (fork)"
for one determined law.

**Readings.** Ren, 12 October 2026, of the reading that law and history are one unfolding read
two ways, the law read off the unfolding rather than set over it: "yes, i do agree with your
reading, there are no two realities". The rest are the AI's, adopted on Ren's delegation of 15
October 2026 (DELEGATED-CHOICES D23).
- (Superseded: on 14 October 2026 Ren asked “why do we need "World"?” and approved the readings in
  context as the general case, `World` being the case where they glue, `Becoming.Readings`;
  DELEGATED-CHOICES D23.) `World` is where the core begins; a labelled process is a world read with
  its configuration split into what the law fixes and what it leaves open, and a frame is a world
  read through its claims. The two directions are both proved: every run with its claims is a world
  that fixes it, and every world is a run of the law it shows, and of the law of exchange where it
  balances. Neither reading is the ground of the other; the world is stated first because its
  relations are among relata of one kind.
- An agent's choice is not a second kind of cause beside the unfolding. What an outside mover
  supplies is what the law leaves open; once the move's forming is represented, it is part of
  what the configuration is, and varying one's own act is varying what the configuration is.
- A law is not prior to what it governs (the reading Ren agreed with): the law a history shows
  is the history read as a relation, a world's sequence of cross-sections included; a law with
  more steps is a model of moves not taken. The gap between a law and its histories is memory:
  a law answers from where one is, not from how one came there.
- Knowing is within the unfolding: a claim comes to be and ceases to be under the same laws
  as anything else.
- The names of configurations, like those of relata (`Becoming.Identity`), carry nothing;
  what can be found out is the same for alike configurations. For standings under the law of
  exchange, agreeing at every relatum is being alike, so the zero-premise plan's commitment to
  pointwise properties in place of function extensionality (§1.2, b(5)) states the relational
  identity of standings; function extensionality would add only that alike standings are one
  and the same.

What is not derived: the shared index of steps (a commitment of the representation; see
`Becoming.Sampling` and `Becoming.Tower`); that a move is formed within the unfolding, or by
what; which law a formation takes its history to show; that configurations passing the same
tests are alike, which needs a condition on branching; that a description making sense exists
(describing each configuration by what it is alike to makes sense given function and
propositional extensionality, and the quotient by likeness needs `Quot.sound`); that the theory without axiom's
theorems stated with `Determined` hold up to likeness. No ethical predicate, ranking or axiom
occurs.

`Law.SameFuture` is stated in `Becoming.Recurrence`, so the modules using it do not import the frame
(board item W).
-/

namespace Becoming

open Generative

universe u v w u' u''

/-! ## The move within the configuration -/

section Move

variable {S : Type u} {A : Type v}

variable {P : Process S A}

/-- **With the move inside, the law is determined exactly where it is determined with moves
as labels and, wherever it takes a step, only one move remains.** -/
theorem withMove_determined_iff :
    Determined (withMove P) ↔ Determined P ∧ ∀ s a t, P.step s a t → ∀ b b' : A, b = b' :=
  ⟨fun determined =>
    ⟨fun s a t t' step step' =>
      congrArg Prod.fst (determined (s, a) () (t, a) (t', a) step step'),
     fun s a t step b b' =>
      congrArg Prod.snd (determined (s, a) () (t, b) (t, b') step step)⟩,
   fun ⟨determined, one⟩ x _ y y' step step' =>
    match y, y', step, step' with
    | (t, b), (t', b'), step, step' => by
      cases determined x.1 x.2 t t' step step'
      cases one x.1 x.2 t step b b'
      rfl⟩

/-- With the move formed within, a determined law stays determined. -/
theorem closedBy_determined (determined : Determined P) (policy : S → A) :
    Determined (closedBy P policy) :=
  fun x _ y y' step step' =>
    match y, y', step, step' with
    | (t, b), (t', b'), ⟨step, formed⟩, ⟨step', formed'⟩ => by
      cases determined x.1 x.2 t t' step step'
      cases formed.trans formed'.symm
      rfl

/-- **A move formed within the unfolding varies only with the configuration.** Where the law
is determined and the move is formed within, two runs from one configuration agree at every
step: what one does otherwise is what one is otherwise. -/
theorem closedBy_runs_agree (determined : Determined P) {policy : S → A}
    (r r' : Run (closedBy P policy)) (start : r.state 0 = r'.state 0) :
    ∀ n, r.state n = r'.state n :=
  GoAlike.runs_agree (π := id) (goAlike_id_iff.mpr (closedBy_determined determined policy))
    r r' (fun _ => rfl) start

namespace Fork

/-- An origin and two ends. -/
inductive Pos where
  | origin
  | left
  | right

/-- Two ways. -/
inductive Way where
  | one
  | other

/-- From the origin one way leads left and the other right. -/
inductive Steps : Pos → Way → Pos → Prop where
  | toLeft : Steps .origin .one .left
  | toRight : Steps .origin .other .right

/-- The fork. -/
def law : Process Pos Way := ⟨Steps⟩

/-- **A shared move is a relation between the parts.** Two parts forking by one law, the move
shared, cannot go different ways at once; with the move forgotten in each part first, they can. -/
theorem label_couples :
    (¬ ∃ a, (productProcess law law).step (.origin, .origin) a (.left, .right)) ∧
      (productProcess (unlabelled law) (unlabelled law)).step (.origin, .origin) () (.left, .right) :=
  ⟨(fun ⟨a, here, there⟩ => match a, here, there with
    | .one, _, there => nomatch there
    | .other, here, _ => nomatch here),
   ⟨⟨.one, .toLeft⟩, ⟨.other, .toRight⟩⟩⟩

end Fork

end Move

/-! ## A world's moves are its relata's exchanges -/

section Exchange

variable {R : Type}

/-- **A world balances exactly where its standings run by its relata's exchanges.** -/
theorem World.balances_iff_exchange (w : World) :
    w.flow.Balances w.web ↔
      ∀ t, (exchange w.Relatum).step (w.web.level t) (w.move t) (w.web.level (t + 1)) :=
  Iff.rfl

/-- **Across one step, the world's standings run by its exchange exactly where it balances on
every family there.** -/
theorem World.exchange_step_iff (w : World) (t : Nat) :
    (exchange w.Relatum).step (w.web.level t) (w.move t) (w.web.level (t + 1)) ↔
      ∀ cs, w.flow.BalancesOn w.web cs t :=
  ⟨fun step _ c _ => step c, fun on c => on [c] c (.head [])⟩

/-- A balanced world is a run of the law of exchange, its moves its relata's exchanges. -/
def World.exchangeRun (w : World) (balances : w.flow.Balances w.web) :
    Run (exchange w.Relatum) :=
  ⟨w.web.level, w.move, (w.balances_iff_exchange.mp balances)⟩

/-- The law of exchange fixes each standing after the step. -/
theorem exchange_agrees {level level' level'' : R → Nat} {m : Exchange R}
    (step : (exchange R).step level m level') (step' : (exchange R).step level m level'') :
    ∀ c, level' c = level'' c :=
  fun c => add_right_cancel (m.taken c) ((step c).trans (step' c).symm)

/-- **Passing fixes standing from a beginning.** Two runs of the law of exchange with the same
moves, starting alike at every relatum, agree at every relatum at every step. -/
theorem exchange_runs_agree (r r' : Run (exchange R)) (moves : ∀ n, r.act n = r'.act n)
    (start : ∀ c, r.state 0 c = r'.state 0 c) : ∀ n c, r.state n c = r'.state n c
  | 0 => start
  | n + 1 => fun c =>
    have there : r'.state (n + 1) c + (r.act n).taken c = r'.state n c + (r.act n).given c :=
      moves n ▸ r'.step n c
    add_right_cancel _ ((r.step n c).trans ((congrArg (· + (r.act n).given c)
      (exchange_runs_agree r r' moves start n c)).trans there.symm))

end Exchange

/-! ## A history and the law it shows -/

section Law

variable {S : Type u} {A : Type v}

/-- **The law a history shows is determined exactly where the history is consistent.** -/
theorem shown_determined_iff {g : Nat → S} {m : Nat → A} :
    Determined (Shown g m) ↔ Consistent g m :=
  ⟨fun determined i j same same' =>
    determined (g i) (m i) (g (i + 1)) (g (j + 1)) ⟨i, rfl, rfl, rfl⟩
      ⟨j, same.symm, same'.symm, rfl⟩,
   fun consistent _ _ _ _ ⟨i, at_s, by_a, to_t⟩ ⟨j, at_s', by_a', to_t'⟩ =>
    to_t.symm.trans
      ((consistent i j (at_s.trans at_s'.symm) (by_a.trans by_a'.symm)).trans to_t')⟩

/-- **Some determined law admits a history exactly where the history is consistent.** -/
theorem exists_law_iff {g : Nat → S} {m : Nat → A} :
    (∃ Q : Process S A, Determined Q ∧ ∀ n, Q.step (g n) (m n) (g (n + 1))) ↔
      Consistent g m :=
  ⟨fun ⟨Q, determined, steps⟩ =>
    shown_determined_iff.mp (goAlike_id_iff.mp (carries_law_iff.mp
      ⟨Q, determined, fun s a t step => shown_le_iff.mpr steps s a t step⟩)),
   fun consistent =>
    ⟨Shown g m, shown_determined_iff.mpr consistent, fun n => ⟨n, rfl, rfl, rfl⟩⟩⟩

/-- **Every determined law of a history repeats what it shows.** -/
theorem Shown.agrees {g : Nat → S} {m : Nat → A} {Q : Process S A} (determined : Determined Q)
    (steps : ∀ n, Q.step (g n) (m n) (g (n + 1))) {s : S} {a : A} {t t' : S}
    (shown : (Shown g m).step s a t) (step : Q.step s a t') : t' = t :=
  determined s a t' t step (shown_le_iff.mpr steps s a t shown)

end Law

/-! ## How far a history and its law correspond -/

section Correspondence

variable {S : Type u} {A : Type v}

/-- **The law a kept history shows admits only that history.** Along a run keeping its history
(`keepHistory` of `Becoming.Experiment`), every run of the law the history shows, from one of its
configurations, is the run from there on. -/
theorem Run.keepHistory_shown {P : Process S A} (r : Run (keepHistory P))
    (r' : Run (Shown r.state r.act)) {k : Nat} (start : r'.state 0 = r.state k) :
    ∀ n, r'.state n = r.state (k + n) :=
  Shown.runs_of_new (keepHistory_new r) r' start

end Correspondence

/-! ## Claims as relata -/

section Claims

variable {S : Type u} {A : Type v} {C : Type}

variable {F : Frame S A C} {r : Run F.P}

/-- **A claim realized anew is a relatum arising.** -/
theorem Frame.arises_iff {t : Nat} {c : C} :
    (F.world r).web.Arises t c ↔ ComesToBe (fun n => F.realized (r.state n) c) t :=
  Iff.rfl

/-- **Novelty is arising.** Where the configuration after a step records what was realized
before it, a claim of the reading is new there exactly where one arises across the step. -/
theorem Frame.novel_iff_arises {reading : C → Prop} {before : S → C → Prop} {t : Nat}
    (records : ∀ c, before (r.state (t + 1)) c ↔ F.realized (r.state t) c) :
    Novel F reading before (r.state (t + 1)) ↔ ∃ c, reading c ∧ (F.world r).web.Arises t c :=
  ⟨fun ⟨c, read, real, fresh⟩ => ⟨c, read, fun was => fresh ((records c).mpr was), real⟩,
   fun ⟨c, read, was_not, real⟩ => ⟨c, read, real, fun was => was_not ((records c).mp was)⟩⟩

/-- **The laws of activity hold of claims.** In a finite family of claims, each decided at each
step, coming to be realized recurs exactly where ceasing to be realized recurs. -/
theorem Frame.claims_recur_iff {cs : List C} [∀ c t, Decidable (F.realized (r.state t) c)] :
    Recurs cs (fun c => ComesToBe (fun n => F.realized (r.state n) c)) ↔
      Recurs cs (fun c => CeasesToBe (fun n => F.realized (r.state n) c)) :=
  coming_recurs_iff (p := fun c n => F.realized (r.state n) c)

end Claims

/-! ## Configurations alike in their relations -/

section Likeness

variable {S : Type u} {S' : Type u'} {S'' : Type u''} {A : Type v} {C : Type w}

/-- A determined frame is determined up to likeness everywhere. -/
theorem Determined.at {F : Frame S A C} (determined : Determined F.P) (s : S) :
    DeterminedAt F s :=
  fun a t t' step step' => (determined s a t t' step step') ▸ Alike.refl F t

/-! ### Descriptions that make sense -/

section Sense

variable {K : Type u'} {K' : Type u''}

/-- **Where the frame is determined up to likeness, a description that makes sense carries a
law** (`carries_law_iff` of `Becoming.Mechanism`). -/
theorem IdentifiesAlike.carries {F : Frame S A C} {π : S → K} (sense : IdentifiesAlike F π)
    (determined : ∀ s, DeterminedAt F s) :
    ∃ Q : Process K A, Determined Q ∧ FactorsThrough F.P π Q :=
  carries_law_iff.mpr fun s s' _ u u' same step step' =>
    (sense u u').mpr (DeterminedAt.goAlike ((sense s s').mp same) (determined s') step step')

end Sense

/-! ### The twins: determinacy as equality depends on names -/

namespace Twins

/-- A start and two successors. -/
inductive Config where
  | start
  | left
  | right

/-- From the start one move leads to either successor; nothing is claimed. -/
def frame : Frame Config Unit Unit :=
  ⟨⟨fun s _ t => s = .start ∧ (t = .left ∨ t = .right)⟩, fun _ _ => True⟩

/-- The twins are not determined. -/
theorem not_determined : ¬ Determined frame.P :=
  fun determined =>
    nomatch determined .start () .left .right ⟨rfl, .inl rfl⟩ ⟨rfl, .inr rfl⟩

/-- The one successor is determined. -/
theorem one_determined : Determined one.P :=
  fun _ _ _ _ ⟨_, to⟩ ⟨_, to'⟩ => to.trans to'.symm

/-- Whether a configuration is the start is all the twins' relations tell. -/
theorem bisimulation : Bisimulation frame frame fun x y => (x = .start ↔ y = .start) :=
  fun _ _ same =>
    ⟨fun _ => Iff.rfl,
     fun _ t ⟨at_start, to⟩ => ⟨t, ⟨same.mp at_start, to⟩, Iff.rfl⟩,
     fun _ t ⟨at_start, to⟩ => ⟨t, ⟨same.mpr at_start, to⟩, Iff.rfl⟩⟩

/-- **The two successors are alike in every relation.** -/
theorem left_alike_right : Alike frame frame .left .right :=
  ⟨_, bisimulation, (fun h => nomatch h), (fun h => nomatch h)⟩

/-- A successor is not the start. -/
theorem successor_not_start {t : Config} (to : t = .left ∨ t = .right) : ¬ t = .start :=
  match to with
  | .inl h => fun s => nomatch h.symm.trans s
  | .inr h => fun s => nomatch h.symm.trans s

/-- The twins and the one successor relate alike. -/
theorem bisimulation_one : Bisimulation frame one fun x b => (x = .start ↔ b = false) :=
  fun _ _ same =>
    ⟨fun _ => Iff.rfl,
     fun _ _ ⟨at_start, to⟩ =>
      ⟨true, ⟨same.mp at_start, rfl⟩,
       (fun s => absurd s (successor_not_start to)), (fun h => nomatch h)⟩,
     fun _ _ ⟨at_false, to⟩ =>
      ⟨.left, ⟨same.mpr at_false, .inl rfl⟩,
       (fun h => nomatch h), (fun h => nomatch to.symm.trans h)⟩⟩

/-- **The twins are alike to a determined frame, and are not determined.** Determinacy as
equality depends on how configurations are named; up to likeness it holds at the start, as it
does of the one successor. -/
theorem alike_one :
    Alike frame one .start false ∧ Determined one.P ∧ ¬ Determined frame.P ∧
      DeterminedAt frame .start :=
  ⟨⟨_, bisimulation_one, fun _ => rfl, fun _ => rfl⟩, one_determined, not_determined,
   DeterminedAt.transfer (Alike.symm ⟨_, bisimulation_one, fun _ => rfl, fun _ => rfl⟩)
     (Determined.at one_determined false)⟩

/-- **Naming the twins does not make sense**: it tells apart two successors alike in every
relation. -/
theorem naming_not_identifiesAlike : ¬ IdentifiesAlike frame id :=
  fun sense => nomatch identifiesAlike_id_iff.mp sense .left .right left_alike_right

end Twins

/-! ### A determined law: likeness is the same future through the map -/

section Registered

variable {R : Type w}

/-- A determined law read through a map: the map's value is what is claimed. -/
def Law.frameBy (next : S → S) (o : S → R) : Frame S Unit R :=
  ⟨Law.process next, fun s r => o s = r⟩

/-- The law read through a map is determined. -/
theorem Law.frameBy_determined (next : S → S) (o : S → R) :
    Determined (Law.frameBy next o).P :=
  fun _ _ _ _ to to' => to.trans to'.symm

/-- Alike configurations have the same future through the map. -/
theorem Law.alike_future {next : S → S} {o : S → R} :
    ∀ n {s s' : S}, Alike (Law.frameBy next o) (Law.frameBy next o) s s' →
      o (Law.orbit next s n) = o (Law.orbit next s' n)
  | 0, s, _, alike => ((alike.realized (o s)).mp rfl).symm
  | n + 1, s, s', alike =>
    match alike.step (a := ()) (t := next s) rfl with
    | ⟨_, to, joined⟩ => by
      cases to
      exact (congrArg o (Law.orbit_shift next s n)).trans
        ((Law.alike_future n joined).trans (congrArg o (Law.orbit_shift next s' n)).symm)

/-- The same future through the map is a bisimulation. -/
theorem Law.sameFuture_bisimulation {next : S → S} {o : S → R} :
    Bisimulation (Law.frameBy next o) (Law.frameBy next o) (Law.SameFuture next o) :=
  fun s s' same =>
    have ahead : Law.SameFuture next o (next s) (next s') := fun n =>
      (congrArg o (Law.orbit_shift next s n)).symm.trans
        ((same (n + 1)).trans (congrArg o (Law.orbit_shift next s' n)))
    ⟨fun _ => ⟨fun h => (same 0).symm.trans h, fun h => (same 0).trans h⟩,
     fun _ _ to => ⟨next s', rfl, by cases to; exact ahead⟩,
     fun _ _ to => ⟨next s, rfl, by cases to; exact ahead⟩⟩

/-- **Under a determined law, configurations are alike exactly where their futures through the map are
the same.** -/
theorem Law.alike_iff_sameFuture {next : S → S} {o : S → R} {s s' : S} :
    Alike (Law.frameBy next o) (Law.frameBy next o) s s' ↔ Law.SameFuture next o s s' :=
  ⟨fun alike n => Law.alike_future n alike, fun same => ⟨_, Law.sameFuture_bisimulation, same⟩⟩

/-- **Under a determined law, a description that makes sense carries a law.** -/
theorem Law.IdentifiesAlike.carries {next : S → S} {o : S → R} {K : Type u'} {π : S → K}
    (sense : IdentifiesAlike (Law.frameBy next o) π) :
    ∃ Q : Process K Unit, Determined Q ∧ FactorsThrough (Law.process next) π Q :=
  sense.carries fun s => Determined.at (Law.frameBy_determined next o) s

end Registered

end Likeness

/-! ## Standings alike -/

section Standings

variable {R : Type}

/-- **The law of exchange is determined up to likeness.** -/
theorem exchange_determinedAt (level : R → Nat) : DeterminedAt (exchangeFrame R) level :=
  fun _ _ _ step step' => exchange_alike_of_pointwise (exchange_agrees step step')

end Standings

end Becoming
