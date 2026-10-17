import Becoming.Mechanism
import Becoming.Space

/-!
# One unfolding and its readings

Ren asked of the core's first two layers, `Process S A` and `Frame`, on 12 October 2026: "is
this dualistic?" They posit no subject and object, but their form takes four splits as given:
a configuration and a move drawn from an alphabet of its own; a law supplied before the history
it governs; claims read off a configuration; and configurations given before the relation among
them. `World` (`Becoming.Space`) takes none of them: one kind of relatum, with what each takes,
gives, stands at, needs and draws at each step. This module states the four splits from the
world's side, with no premise beyond what each theorem names, so that the labelled process and
the frame are readings of one unfolding rather than its ground.

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
  does not (`Twins.naming_not_identifiesAlike`). For a determined law read through a registration
  (`Law.registered`), configurations are alike exactly where their registered futures are the
  same (`Law.SameFuture`, `Law.alike_iff_sameFuture`), so there a description makes sense where
  it identifies exactly the same registered futures, and it carries a law
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
-/

namespace Becoming

open Generative

universe u v w u' u''

/-! ## The move within the configuration -/

section Move

variable {S : Type u} {A : Type v}

/-- The move read within the configuration: what the unfolding is at a step includes the move
made there, and the law relates such configurations. -/
def withMove (P : Process S A) : Process (S × A) Unit :=
  ⟨fun x _ y => P.step x.1 x.2 y.1⟩

variable {P : Process S A}

/-- A run read with its moves inside its configurations. -/
def Run.toWithMove (r : Run P) : Run (withMove P) :=
  ⟨fun n => (r.state n, r.act n), fun _ => (), fun n => r.step n⟩

/-- A run of the law with moves inside, read with its moves as labels. -/
def Run.ofWithMove (r : Run (withMove P)) : Run P :=
  ⟨fun n => (r.state n).1, fun n => (r.state n).2, fun n => r.step n⟩

/-- **One run, read two ways.** Reading the moves inside and back gives the same run. -/
theorem Run.ofWithMove_toWithMove (r : Run P) (n : Nat) :
    r.toWithMove.ofWithMove.state n = r.state n ∧ r.toWithMove.ofWithMove.act n = r.act n :=
  ⟨rfl, rfl⟩

/-- And reading the moves as labels and back. -/
theorem Run.toWithMove_ofWithMove (r : Run (withMove P)) (n : Nat) :
    r.ofWithMove.toWithMove.state n = r.state n :=
  rfl

/-- **The law leaves the move open.** A step to a configuration admits every next move. -/
theorem withMove_open {x : S × A} {i : Unit} {t : S} {b : A}
    (step : (withMove P).step x i (t, b)) (b' : A) : (withMove P).step x i (t, b') :=
  step

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

/-- The move formed within the unfolding: the next move is what a policy makes of the next
configuration. -/
def closedBy (P : Process S A) (policy : S → A) : Process (S × A) Unit :=
  ⟨fun x _ y => P.step x.1 x.2 y.1 ∧ y.2 = policy y.1⟩

/-- Forming the move within narrows the law with the move left open. -/
theorem closedBy_withMove {policy : S → A} {x : S × A} {i : Unit} {y : S × A}
    (step : (closedBy P policy).step x i y) : (withMove P).step x i y :=
  step.1

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

/-- A process with its moves forgotten: a configuration goes to another by some move. -/
def unlabelled (P : Process S A) : Process S Unit :=
  ⟨fun s _ t => ∃ a, P.step s a t⟩

/-- Forgetting the move of a joint step leaves a step of each part with its move forgotten. -/
theorem unlabelled_product_le {T : Type w} {Q : Process T A} {x : S × T} {i : Unit} {y : S × T}
    (step : (unlabelled (productProcess P Q)).step x i y) :
    (productProcess (unlabelled P) (unlabelled Q)).step x i y :=
  match step with
  | ⟨a, here, there⟩ => ⟨⟨a, here⟩, ⟨a, there⟩⟩

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

/-- What the relata present take and give across a step, read as a move. -/
structure Exchange (R : Type) where
  present : List R
  take : R → R → Nat
  give : R → R → Nat

/-- What the relata present take from `c`. -/
def Exchange.taken (m : Exchange R) (c : R) : Nat :=
  total m.present fun f => m.take f c

/-- What the relata present give to `c`. -/
def Exchange.given (m : Exchange R) (c : R) : Nat :=
  total m.present fun f => m.give f c

/-- The law of exchange: across a step, each relatum's standing after it, with what is taken
from it, is its standing before, with what is given to it. -/
def exchange (R : Type) : Process (R → Nat) (Exchange R) :=
  ⟨fun level m level' => ∀ c, level' c + m.taken c = level c + m.given c⟩

/-- The world's move across the step from `t`: its relata's exchange. -/
def World.move (w : World) (t : Nat) : Exchange w.Relatum :=
  ⟨w.flow.present t, w.flow.take t, w.flow.give t⟩

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

namespace Circulation

/-- One relatum standing at one. -/
def one : Unit → Nat := fun _ => 1

/-- It takes one from itself and gives one to itself. -/
def round : Exchange Unit := ⟨[()], fun _ _ => 1, fun _ _ => 1⟩

/-- Nothing is exchanged. -/
def idle : Exchange Unit := ⟨[], fun _ _ => 0, fun _ _ => 0⟩

/-- **The standings do not fix the exchange.** A circulation and no exchange at all leave the
same standings. -/
theorem standings_leave_exchange :
    (exchange Unit).step one round one ∧ (exchange Unit).step one idle one ∧
      round.present ≠ idle.present :=
  ⟨fun _ => rfl, fun _ => rfl, fun same => nomatch same⟩

/-- **Passing fixes standing only from a beginning.** With nothing exchanged, standing at zero
throughout and standing at one throughout are runs with the same moves. -/
theorem start_needed :
    ∃ r r' : Run (exchange Unit), (∀ n, r.act n = r'.act n) ∧ ∀ n, r.state n () ≠ r'.state n () :=
  ⟨⟨fun _ _ => 0, fun _ => idle, fun _ _ => rfl⟩, ⟨fun _ _ => 1, fun _ => idle, fun _ _ => rfl⟩,
   fun _ => rfl, fun _ same => absurd (show (0 : Nat) = 1 from same) (by decide)⟩

end Circulation

end Exchange

/-! ## A history and the law it shows -/

section Law

variable {S : Type u} {A : Type v}

/-- The law a history shows: the steps it takes. -/
def Shown (g : Nat → S) (m : Nat → A) : Process S A :=
  ⟨fun s a t => ∃ n, g n = s ∧ m n = a ∧ g (n + 1) = t⟩

/-- **Every history is a run of the law it shows**, with no premise. -/
def Shown.run (g : Nat → S) (m : Nat → A) : Run (Shown g m) :=
  ⟨g, m, fun n => ⟨n, rfl, rfl, rfl⟩⟩

/-- **The law a history shows is the least law it is a run of.** -/
theorem shown_le_iff {g : Nat → S} {m : Nat → A} {Q : Process S A} :
    (∀ s a t, (Shown g m).step s a t → Q.step s a t) ↔ ∀ n, Q.step (g n) (m n) (g (n + 1)) :=
  ⟨fun le n => le _ _ _ ⟨n, rfl, rfl, rfl⟩,
   fun steps _ _ _ ⟨n, at_s, by_a, to_t⟩ => at_s ▸ by_a ▸ to_t ▸ steps n⟩

/-- **A law is fixed by its traces.** Two laws on the same configurations and moves take the
same steps exactly when they have the same traces with both ends kept; traces of one move
suffice. -/
theorem same_steps_iff_traces {P Q : Process S A} :
    (∀ s a t, P.step s a t ↔ Q.step s a t) ↔ ∀ s as t, Trace P s as t ↔ Trace Q s as t :=
  ⟨fun same _ _ _ => ⟨trace_map (f := fun x => x) fun s a t => (same s a t).mp,
     trace_map (f := fun x => x) fun s a t => (same s a t).mpr⟩,
   fun same s a t => ⟨fun h => trace_singleton_iff.mp ((same s [a] t).mp (trace_singleton_iff.mpr h)),
     fun h => trace_singleton_iff.mp ((same s [a] t).mpr (trace_singleton_iff.mpr h))⟩⟩

/-- A history is consistent where it never takes one move at one configuration to two
outcomes. -/
def Consistent (g : Nat → S) (m : Nat → A) : Prop :=
  ∀ i j, g i = g j → m i = m j → g (i + 1) = g (j + 1)

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

/-- A run of a law is a run of the law it shows, which the law contains. -/
theorem Run.shown_le {P : Process S A} (r : Run P) :
    ∀ s a t, (Shown r.state r.act).step s a t → P.step s a t :=
  shown_le_iff.mpr r.step

end Law

/-! ## How far a history and its law correspond -/

section Correspondence

variable {S : Type u} {A : Type v}

/-- A history new at every step meets no configuration twice. -/
theorem eq_of_new {g : Nat → S} (new : ∀ i j, i < j → g i ≠ g j) {i j : Nat} (same : g i = g j) :
    i = j :=
  match Nat.lt_or_ge i j with
  | .inl lt => absurd same (new i j lt)
  | .inr ge => match Nat.lt_or_eq_of_le ge with
    | .inl lt => absurd same.symm (new j i lt)
    | .inr eq => eq.symm

/-- **Where a history never revisits a configuration, the law it shows admits only the history.**
Every run of that law from a configuration of the history is the history from there on. -/
theorem Shown.runs_of_new {g : Nat → S} {m : Nat → A} (new : ∀ i j, i < j → g i ≠ g j)
    (r : Run (Shown g m)) {k : Nat} (start : r.state 0 = g k) : ∀ n, r.state n = g (k + n)
  | 0 => start
  | n + 1 => match r.step n with
    | ⟨_, at_s, _, to_t⟩ => by
      cases eq_of_new new (at_s.trans (Shown.runs_of_new new r start n))
      exact to_t.symm

/-- **The law a kept history shows admits only that history.** Along a run keeping its history
(`keepHistory` of `Becoming.Experiment`), every run of the law the history shows, from one of its
configurations, is the run from there on. -/
theorem Run.keepHistory_shown {P : Process S A} (r : Run (keepHistory P))
    (r' : Run (Shown r.state r.act)) {k : Nat} (start : r'.state 0 = r.state k) :
    ∀ n, r'.state n = r.state (k + n) :=
  Shown.runs_of_new (keepHistory_new r) r' start

namespace Splice

/-- A history that returns once to where it began and then goes elsewhere for good. -/
def history : Nat → Nat
  | 0 => 0
  | 1 => 1
  | 2 => 0
  | _ + 3 => 2

/-- Going back and forth between the first two configurations, as the history never did. -/
def loop : Nat → Nat
  | 0 => 0
  | 1 => 1
  | n + 2 => loop n

/-- The loop's steps are steps the history took. -/
theorem loop_step : ∀ n, (Shown history fun _ => ()).step (loop n) () (loop (n + 1))
  | 0 => ⟨0, rfl, rfl, rfl⟩
  | 1 => ⟨1, rfl, rfl, rfl⟩
  | n + 2 => loop_step n

/-- **Where a history revisits, the law it shows admits a history it never took.** -/
theorem spliced :
    (∃ r : Run (Shown history fun _ => ()), ∀ n, r.state n = loop n) ∧
      ∀ k, ∃ n, loop n ≠ history (k + n) :=
  ⟨⟨⟨loop, fun _ => (), loop_step⟩, fun _ => rfl⟩,
   fun _ => ⟨3, fun same => absurd (show (1 : Nat) = 2 from same) (by decide)⟩⟩

end Splice

namespace DeadEnd

/-- One step, into a configuration with no continuation. -/
def law : Process Bool Unit :=
  ⟨fun s _ t => s = false ∧ t = true⟩

/-- **A law can have a step and no history.** No history shows it. -/
theorem no_history : law.step false () true ∧ (Run law → False) :=
  ⟨⟨rfl, rfl⟩, fun r => nomatch (r.step 0).2.symm.trans (r.step 1).1⟩

end DeadEnd

end Correspondence

/-! ## Claims as relata -/

section Claims

variable {S : Type u} {A : Type v} {C : Type}

/-- A frame along a run read as a world: its relata are its claims, each active exactly where
it is realized; nothing stands, depends, draws or is exchanged. -/
def Frame.world (F : Frame S A C) (r : Run F.P) : World :=
  ⟨C, ⟨fun _ => [], fun _ _ _ => 0, fun _ _ _ => 0⟩,
    ⟨fun _ _ => 0, fun t c => F.realized (r.state t) c, fun _ _ _ => False, fun _ _ _ => 0,
      fun _ _ _ => False⟩⟩

variable {F : Frame S A C} {r : Run F.P}

/-- **A claim's activity is its being realized.** -/
theorem Frame.world_active {t : Nat} {c : C} :
    (F.world r).web.active t c ↔ F.realized (r.state t) c :=
  Iff.rfl

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

/-- A process read through the claims that the configuration is this or that one. -/
def Frame.configurations {S : Type} (P : Process S A) : Frame S A S :=
  ⟨P, fun s c => s = c⟩

/-- **Every run is a world, and the world fixes the run.** Two runs whose worlds of
configurations agree in activity agree at every step. -/
theorem Frame.world_fixes_run {S : Type} {P : Process S A}
    (r r' : Run (Frame.configurations P).P)
    (same : ∀ t c, ((Frame.configurations P).world r).web.active t c ↔
      ((Frame.configurations P).world r').web.active t c) :
    ∀ t, r.state t = r'.state t :=
  fun t => ((same t (r.state t)).mp rfl).symm

end Claims

/-! ## Configurations alike in their relations -/

section Likeness

variable {S : Type u} {S' : Type u'} {S'' : Type u''} {A : Type v} {C : Type w}

/-- A bisimulation between two frames: related configurations realize the same claims, and each
step of either is matched by a step of the other by the same move into related
configurations. -/
def Bisimulation (F : Frame S A C) (G : Frame S' A C) (B : S → S' → Prop) : Prop :=
  ∀ s s', B s s' →
    (∀ c, F.realized s c ↔ G.realized s' c) ∧
    (∀ a t, F.P.step s a t → ∃ t', G.P.step s' a t' ∧ B t t') ∧
    (∀ a t', G.P.step s' a t' → ∃ t, F.P.step s a t ∧ B t t')

/-- Two configurations are alike where some bisimulation relates them: they relate alike to
every continuation. `ReferencePlan.Alike` is another sense, two signals agreeing at the addresses
of a plan. -/
def Alike (F : Frame S A C) (G : Frame S' A C) (s : S) (s' : S') : Prop :=
  ∃ B, Bisimulation F G B ∧ B s s'

/-- Sameness is a bisimulation. -/
theorem Bisimulation.eq (F : Frame S A C) : Bisimulation F F fun s s' => s = s' :=
  fun s _ same => by
    cases same
    exact ⟨fun _ => Iff.rfl, fun _ t step => ⟨t, step, rfl⟩, fun _ t step => ⟨t, step, rfl⟩⟩

/-- The converse of a bisimulation is one. -/
theorem Bisimulation.converse {F : Frame S A C} {G : Frame S' A C} {B : S → S' → Prop}
    (bisim : Bisimulation F G B) : Bisimulation G F fun s' s => B s s' :=
  fun s' s related => match bisim s s' related with
    | ⟨claims, forth, back⟩ => ⟨fun c => (claims c).symm, back, forth⟩

/-- Bisimulations compose. -/
theorem Bisimulation.comp {F : Frame S A C} {G : Frame S' A C} {H : Frame S'' A C}
    {B : S → S' → Prop} {B' : S' → S'' → Prop}
    (bisim : Bisimulation F G B) (bisim' : Bisimulation G H B') :
    Bisimulation F H fun s s'' => ∃ s', B s s' ∧ B' s' s'' :=
  fun s s'' ⟨s', related, related'⟩ =>
    match bisim s s' related, bisim' s' s'' related' with
    | ⟨claims, forth, back⟩, ⟨claims', forth', back'⟩ =>
      ⟨fun c => (claims c).trans (claims' c),
       fun a t step => match forth a t step with
         | ⟨t', step', joined⟩ => match forth' a t' step' with
           | ⟨t'', step'', joined'⟩ => ⟨t'', step'', t', joined, joined'⟩,
       fun a t'' step'' => match back' a t'' step'' with
         | ⟨t', step', joined'⟩ => match back a t' step' with
           | ⟨t, step, joined⟩ => ⟨t, step, t', joined, joined'⟩⟩

/-- **Likeness is an equivalence:** every configuration is alike to itself, -/
theorem Alike.refl (F : Frame S A C) (s : S) : Alike F F s s :=
  ⟨_, Bisimulation.eq F, rfl⟩

/-- likeness runs both ways, -/
theorem Alike.symm {F : Frame S A C} {G : Frame S' A C} {s : S} {s' : S'} :
    Alike F G s s' → Alike G F s' s
  | ⟨_, bisim, related⟩ => ⟨_, bisim.converse, related⟩

/-- and passes along. -/
theorem Alike.trans {F : Frame S A C} {G : Frame S' A C} {H : Frame S'' A C} {s : S} {s' : S'}
    {s'' : S''} : Alike F G s s' → Alike G H s' s'' → Alike F H s s''
  | ⟨_, bisim, related⟩, ⟨_, bisim', related'⟩ => ⟨_, bisim.comp bisim', s', related, related'⟩

/-- Alike configurations realize the same claims. -/
theorem Alike.realized {F : Frame S A C} {G : Frame S' A C} {s : S} {s' : S'}
    (alike : Alike F G s s') (c : C) : F.realized s c ↔ G.realized s' c :=
  match alike with
  | ⟨_, bisim, related⟩ => (bisim s s' related).1 c

/-- A step of one is matched by a step of the other by the same move into alike
configurations. -/
theorem Alike.step {F : Frame S A C} {G : Frame S' A C} {s : S} {s' : S'}
    (alike : Alike F G s s') {a : A} {t : S} (step : F.P.step s a t) :
    ∃ t', G.P.step s' a t' ∧ Alike F G t t' :=
  match alike with
  | ⟨B, bisim, related⟩ => match (bisim s s' related).2.1 a t step with
    | ⟨t', step', joined⟩ => ⟨t', step', B, bisim, joined⟩

/-- Under a bisimulation every course of moves is matched by the same course into related
configurations. -/
theorem Bisimulation.trace {F : Frame S A C} {G : Frame S' A C} {B : S → S' → Prop}
    (bisim : Bisimulation F G B) {s t : S} {as : List A} (path : Trace F.P s as t) :
    ∀ {s'}, B s s' → ∃ t', Trace G.P s' as t' ∧ B t t' := by
  induction path with
  | nil =>
    intro s' related
    exact ⟨s', .nil s', related⟩
  | cons step _ ih =>
    intro s' related
    match (bisim _ s' related).2.1 _ _ step with
    | ⟨m', step', joined⟩ =>
      match ih joined with
      | ⟨t', path', joined'⟩ => exact ⟨t', .cons step' path', joined'⟩

/-- **Alike configurations admit the same courses of moves into alike configurations.** -/
theorem Alike.trace {F : Frame S A C} {G : Frame S' A C} {s : S} {s' : S'}
    (alike : Alike F G s s') {as : List A} {t : S} (path : Trace F.P s as t) :
    ∃ t', Trace G.P s' as t' ∧ Alike F G t t' :=
  match alike with
  | ⟨B, bisim, related⟩ => match bisim.trace path related with
    | ⟨t', path', joined⟩ => ⟨t', path', B, bisim, joined⟩

/-- **Alike configurations pass the same tests**: a course of moves followed by a claim. -/
theorem Alike.tests {F : Frame S A C} {G : Frame S' A C} {s : S} {s' : S'}
    (alike : Alike F G s s') (as : List A) (c : C) :
    (∃ t, Trace F.P s as t ∧ F.realized t c) ↔ (∃ t', Trace G.P s' as t' ∧ G.realized t' c) :=
  ⟨fun ⟨_, path, real⟩ => match alike.trace path with
    | ⟨t', path', joined⟩ => ⟨t', path', (joined.realized c).mp real⟩,
   fun ⟨_, path', real'⟩ => match alike.symm.trace path' with
    | ⟨t, path, joined⟩ => ⟨t, path, (joined.realized c).mp real'⟩⟩

/-- A frame is determined up to likeness at a configuration where any two outcomes of one move
there are alike. -/
def DeterminedAt (F : Frame S A C) (s : S) : Prop :=
  ∀ a t t', F.P.step s a t → F.P.step s a t' → Alike F F t t'

/-- A determined frame is determined up to likeness everywhere. -/
theorem Determined.at {F : Frame S A C} (determined : Determined F.P) (s : S) :
    DeterminedAt F s :=
  fun a t t' step step' => (determined s a t t' step step') ▸ Alike.refl F t

/-- **Determinacy up to likeness passes along likeness.** -/
theorem DeterminedAt.transfer {F : Frame S A C} {G : Frame S' A C} {s : S} {s' : S'}
    (alike : Alike F G s s') (determined : DeterminedAt F s) : DeterminedAt G s' :=
  fun a _ _ step₁ step₂ =>
    match alike.symm.step step₁, alike.symm.step step₂ with
    | ⟨u₁, back₁, joined₁⟩, ⟨u₂, back₂, joined₂⟩ =>
      joined₁.trans ((determined a u₁ u₂ back₁ back₂).trans joined₂.symm)

/-- **Alike configurations go alike.** Where a frame is determined up to likeness, the same move
takes alike configurations to alike ones. -/
theorem DeterminedAt.goAlike {F : Frame S A C} {s s' : S} (alike : Alike F F s s')
    (determined : DeterminedAt F s') {a : A} {t t' : S} (step : F.P.step s a t)
    (step' : F.P.step s' a t') : Alike F F t t' :=
  match alike.step step with
  | ⟨u, matched, joined⟩ => joined.trans (determined a u t' matched step')

/-! ### Descriptions that make sense -/

section Sense

variable {K : Type u'} {K' : Type u''}

/-- A description of configurations makes sense where it identifies exactly the alike ones. -/
def IdentifiesAlike (F : Frame S A C) (π : S → K) : Prop :=
  ∀ s s', π s = π s' ↔ Alike F F s s'

/-- **A description makes sense exactly where what it identifies relate alike and it identifies
whatever is alike.** -/
theorem identifiesAlike_iff {F : Frame S A C} {π : S → K} :
    IdentifiesAlike F π ↔
      Bisimulation F F (fun s s' => π s = π s') ∧ ∀ s s', Alike F F s s' → π s = π s' :=
  ⟨fun sense =>
    ⟨fun s s' same =>
      have alike := (sense s s').mp same
      ⟨alike.realized,
       fun _ _ step => match alike.step step with
         | ⟨t', step', joined⟩ => ⟨t', step', (sense _ t').mpr joined⟩,
       fun _ _ step' => match alike.symm.step step' with
         | ⟨t, step, joined⟩ => ⟨t, step, (sense t _).mpr joined.symm⟩⟩,
     fun s s' => (sense s s').mpr⟩,
   fun ⟨kernel, idle⟩ s s' => ⟨fun same => ⟨_, kernel, same⟩, idle s s'⟩⟩

/-- **Descriptions that make sense identify the same configurations.** -/
theorem IdentifiesAlike.unique {F : Frame S A C} {π : S → K} {ρ : S → K'} (sense : IdentifiesAlike F π)
    (sense' : IdentifiesAlike F ρ) (s s' : S) : π s = π s' ↔ ρ s = ρ s' :=
  (sense s s').trans (sense' s s').symm

/-- **Where the frame is determined up to likeness, a description that makes sense carries a
law** (`carries_law_iff` of `Becoming.Mechanism`). -/
theorem IdentifiesAlike.carries {F : Frame S A C} {π : S → K} (sense : IdentifiesAlike F π)
    (determined : ∀ s, DeterminedAt F s) :
    ∃ Q : Process K A, Determined Q ∧ FactorsThrough F.P π Q :=
  carries_law_iff.mpr fun s s' _ u u' same step step' =>
    (sense u u').mpr (DeterminedAt.goAlike ((sense s s').mp same) (determined s') step step')

/-- **Naming the configurations makes sense exactly where alike configurations are one.** -/
theorem identifiesAlike_id_iff {F : Frame S A C} :
    IdentifiesAlike F id ↔ ∀ s s', Alike F F s s' → s = s' :=
  ⟨fun sense s s' => (sense s s').mpr,
   fun one s s' =>
    ⟨fun same => Eq.subst (motive := fun x => Alike F F s x) same (Alike.refl F s), one s s'⟩⟩

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

/-- The same with one successor. -/
def one : Frame Bool Unit Unit :=
  ⟨⟨fun s _ t => s = false ∧ t = true⟩, fun _ _ => True⟩

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

/-! ### A determined law: likeness is the same registered future -/

section Registered

variable {R : Type w}

/-- A determined law read through a registration: what is registered is what is claimed. -/
def Law.registered (next : S → S) (o : S → R) : Frame S Unit R :=
  ⟨Law.process next, fun s r => o s = r⟩

/-- The law read through a registration is determined. -/
theorem Law.registered_determined (next : S → S) (o : S → R) :
    Determined (Law.registered next o).P :=
  fun _ _ _ _ to to' => to.trans to'.symm

/-- Two configurations have the same registered future under a law. -/
def Law.SameFuture (next : S → S) (o : S → R) (s s' : S) : Prop :=
  ∀ n, o (Law.orbit next s n) = o (Law.orbit next s' n)

/-- Alike configurations have the same registered future. -/
theorem Law.alike_future {next : S → S} {o : S → R} :
    ∀ n {s s' : S}, Alike (Law.registered next o) (Law.registered next o) s s' →
      o (Law.orbit next s n) = o (Law.orbit next s' n)
  | 0, s, _, alike => ((alike.realized (o s)).mp rfl).symm
  | n + 1, s, s', alike =>
    match alike.step (a := ()) (t := next s) rfl with
    | ⟨_, to, joined⟩ => by
      cases to
      exact (congrArg o (Law.orbit_shift next s n)).trans
        ((Law.alike_future n joined).trans (congrArg o (Law.orbit_shift next s' n)).symm)

/-- The same registered future is a bisimulation. -/
theorem Law.sameFuture_bisimulation {next : S → S} {o : S → R} :
    Bisimulation (Law.registered next o) (Law.registered next o) (Law.SameFuture next o) :=
  fun s s' same =>
    have ahead : Law.SameFuture next o (next s) (next s') := fun n =>
      (congrArg o (Law.orbit_shift next s n)).symm.trans
        ((same (n + 1)).trans (congrArg o (Law.orbit_shift next s' n)))
    ⟨fun _ => ⟨fun h => (same 0).symm.trans h, fun h => (same 0).trans h⟩,
     fun _ _ to => ⟨next s', rfl, by cases to; exact ahead⟩,
     fun _ _ to => ⟨next s, rfl, by cases to; exact ahead⟩⟩

/-- **Under a determined law, configurations are alike exactly where their registered futures are
the same.** -/
theorem Law.alike_iff_sameFuture {next : S → S} {o : S → R} {s s' : S} :
    Alike (Law.registered next o) (Law.registered next o) s s' ↔ Law.SameFuture next o s s' :=
  ⟨fun alike n => Law.alike_future n alike, fun same => ⟨_, Law.sameFuture_bisimulation, same⟩⟩

/-- **Under a determined law, a description that makes sense carries a law.** -/
theorem Law.IdentifiesAlike.carries {next : S → S} {o : S → R} {K : Type u'} {π : S → K}
    (sense : IdentifiesAlike (Law.registered next o) π) :
    ∃ Q : Process K Unit, Determined Q ∧ FactorsThrough (Law.process next) π Q :=
  sense.carries fun s => Determined.at (Law.registered_determined next o) s

end Registered

end Likeness

/-! ## Standings alike -/

section Standings

variable {R : Type}

/-- The law of exchange read through the claims that a relatum stands at an amount. -/
def exchangeFrame (R : Type) : Frame (R → Nat) (Exchange R) (R × Nat) :=
  ⟨exchange R, fun level x => level x.1 = x.2⟩

/-- Agreeing at every relatum is a bisimulation of the law of exchange. -/
theorem exchange_pointwise_bisimulation :
    Bisimulation (exchangeFrame R) (exchangeFrame R) fun level level' => ∀ c, level c = level' c :=
  fun _ _ same =>
    ⟨fun x => ⟨fun h => (same x.1).symm.trans h, fun h => (same x.1).trans h⟩,
     fun _ t step => ⟨t, fun c => (step c).trans (congrArg (· + _) (same c)), fun _ => rfl⟩,
     fun _ t step => ⟨t, fun c => (step c).trans (congrArg (· + _) (same c).symm), fun _ => rfl⟩⟩

/-- **Standings agreeing at every relatum are alike.** -/
theorem exchange_alike_of_pointwise {level level' : R → Nat} (same : ∀ c, level c = level' c) :
    Alike (exchangeFrame R) (exchangeFrame R) level level' :=
  ⟨_, exchange_pointwise_bisimulation, same⟩

/-- Alike standings agree at every relatum. -/
theorem exchange_pointwise_of_alike {level level' : R → Nat}
    (alike : Alike (exchangeFrame R) (exchangeFrame R) level level') : ∀ c, level c = level' c :=
  fun c => ((alike.realized (c, level c)).mp rfl).symm

/-- **Standings are alike exactly where they agree at every relatum.** -/
theorem exchange_alike_iff {level level' : R → Nat} :
    Alike (exchangeFrame R) (exchangeFrame R) level level' ↔ ∀ c, level c = level' c :=
  ⟨exchange_pointwise_of_alike, exchange_alike_of_pointwise⟩

/-- **The law of exchange is determined up to likeness.** -/
theorem exchange_determinedAt (level : R → Nat) : DeterminedAt (exchangeFrame R) level :=
  fun _ _ _ step step' => exchange_alike_of_pointwise (exchange_agrees step step')

end Standings

end Becoming
