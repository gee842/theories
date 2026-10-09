import Becoming.Frame
import Becoming.Inquiry
import Becoming.Renewal
import Becoming.Dependence
import Becoming.Return
import Becoming.Horizon
import Becoming.Joint
import Becoming.Substitution
import Becoming.Generation
import Becoming.Flow
import Becoming.Change
import Becoming.Population
import Becoming.Identity
import Becoming.Wholes
import Becoming.Dissipation
import Becoming.Roles
import Becoming.Reserve
import Becoming.Metaethics
import Becoming.Ranking
import Becoming.Correspondence
import Becoming.Descent

/-!
# The Theory of Becoming: the formal core

One relational unfolding, stated once. The core is the foundation (`GenerativeCore`,
`InquirySufficiency`, `RelationalRenewal`) and four layers:

* `Becoming.Frame` (L1): a frame is a process with realized claims; runs,
  reachability, invariants and new realization.
* `Becoming.Inquiry` (L2): the visible scope of an inquiry is what its actual
  executions reach; a sound policy secures its goal there.
* `Becoming.Renewal` (L3): every run read through conditions is one relational
  unfolding; renewal and consumption belong to the run.
* `Becoming.Dependence` (L3): dependence forms, holds, breaks and dissolves across
  steps; the outcomes of a loss where activity needs support; stepwise readings of
  events and their relations.
* `Becoming.Return` (L3): renewal graded by the time to return; readings over cycles.
* `Becoming.Horizon` (L3): no finite stretch of a run decides whether its drawing
  renews or consumes in the whole-run sense, with or without feedback; a reading of
  amounts is decided step by step.
* `Becoming.Joint` (L3): difference-making, relative to a move that can still be taken
  once a part is withheld and read as intended when the move determines the step,
  belongs to the joint activity among formations; over a formation's events the run-level outcome is
  fixed by the tail, while the step-level test singles out the breaking event.
* `Becoming.Substitution` (L3): in the support-gated law, a consumer that substitutes
  a condition persists and still consumes on the whole-run reading, while the stepwise
  reading credits it until the sustaining formation loses support and withholds it from
  then until it switches.
* `Becoming.Generation` (L3): formations arise. Where arising depletes a finite family
  of conditions, unceasing generation needs their renewal to recur; renewal does not
  imply generation; substitution among unrenewed conditions defers the end; and
  dissipation ends generation, while a closed cycle need not.
* `Becoming.Flow` (L3): conditions as amounts that formations take and give. Uptake at
  arbitrarily late steps, as of formations that take arising without end, needs
  replenishment at arbitrarily late steps;
  more generation without end needs replenishment without bound and, with bounded
  capacity, renewers without bound; unceasing generation is not yet more. Every rise is
  given to, so where members of a family rise at arbitrarily late steps, as in coming to
  stand, the rise from nothing, its replenishment recurs.
* `Becoming.Change` (L3): what holds of every unfolding, with no premise about it.
  Arising, forming and coming to stand, with ceasing, dissolving and ceasing to stand,
  are one change, read of activity, dependence and standing. Over any stretch an amount
  at the end with its falls is the amount at the start with its rises. In a finite
  family coming to be and ceasing to be keep pace, differing over any stretch by at most
  the number of members, and each recurs exactly when the other does; so with finitely
  many formations generation is unceasing exactly when some formation ceases at
  arbitrarily late steps.
* `Becoming.Population` (L3): how many formations are active. Under a census of the
  active formations, with each formation taking part listed once and only active
  formations taking, more generation without end makes generation unceasing.
* `Becoming.Identity` (L3): which formation at one step continues which at the next.
  Labels carry nothing, while the pattern of names across steps carries identity; each
  step's relations, each condition's class and how many formations take and give do not
  depend on it, while a formation's class, the tenure of a dependence, undermining and
  arising do. Continuity read one way leaves succession open, read both ways it still
  leaves succession across dormancy. Under the premises of `Becoming.Population`, more
  without end makes generation unceasing under every one-to-one re-identification and
  makes formations arise under every continuation without splits.
* `Becoming.Wholes` (L3): a whole is active exactly while some part is, a coincidence of
  activity rather than constitution. A persisting whole of brief parts, or of parts that
  end with finitely many active at once, persists only through their generation: parts
  never active at two steps `d` apart arise within every `d` steps, possibly the same
  parts again, and parts whose activity ends arise at arbitrarily late steps when the
  active ones are listed, ever new ones.
* `Becoming.Dissipation` (L3): when every formation gives a closed family less than it
  takes from it, the family runs down and taking from it stops. A finite family from
  which taking recurs, whether of more, of generation or of maintenance, is open at
  arbitrarily late steps, though what opens it need not touch it; where each step's
  exchange around it lies within finitely many conditions, it draws in: at arbitrarily
  late steps some formation gives to it and takes from beyond it. With finitely many
  conditions in all, taking does not recur. Where the exchange of a step lies within
  finitely many conditions, giving needs uptake. Rising, as in coming to stand, falls
  under this with no taking of its own: where it recurs in a finite family, the family
  is open at arbitrarily late steps and, enclosed around, draws in.
* `Becoming.Roles` (L3): formations and conditions are roles of one relatum; the
  two-kind reading embeds as the one in which no formation is a condition, and which
  condition is which formation is supplied by the shared index. Where a relatum stands
  as a condition exactly while it is active, a formation depending on it lives only
  while it does, its ending ends every formation whose chain of dependence reaches it,
  and it arises only as another active formation gives to it. It comes to stand as it
  arises, so its arising is replenishment: under dissipation generation that recurs in a
  finite family leaves it open, draws in where each step's exchange around it lies within
  finitely many relata, and in a finite world ceases.
* `Becoming.Reserve` (L3): a reserve carries activity beyond support. `Dependent` is
  exactly the zero reserve; a reserve can be a held condition, and where none is
  represented it is supplied. Where a held condition carries the formations, moving
  their unsupported dependences onto it gives a `Dependent` reading by construction,
  which can differ in which events undermine. A formation unsupported
  from some step on is active at most as often as its reserve at the start, so a reserve
  defers the end after a loss and after coextinction and does not escape it, and a
  reserve decaying while dormant bounds the time as well. A relatum standing while active,
  absent earlier, came to stand before it was active: generation bears replenishment where
  standing rises, not where activity does.
* `Becoming.Metaethics` (L4): the Universal Metaethical Core: the premise card,
  G0's characterization, minimality, the universal reason, C and L, and the
  relational readings over a whole run, stepwise and through relations.
* `Becoming.Ranking` (L4): what C ranks under each reading. Both the whole-run and the
  stepwise reading rank sharing above winning by consumption and, in the two-part
  family, restraint above overdraw; for an overdrawing formation with an event that
  leaves every need met, only the whole-run reading ranks its absence above its
  occurrence.
* `Becoming.Correspondence` (L4): which conditions relate. Under the discipline that a
  condition relates two events only when one draws on it and the other depends on it
  at a positive level, at any steps, idle conditions connect nothing, and connection through a
  condition is made by its living use. Read with one kind of relatum, the valuations keep
  their connection, and formations bearing on themselves relate directly, with no third
  condition.
* `Becoming.Descent` (L4): relata related directly. Read with one kind of relatum, an
  event is related to the relatum it lives on, drawing on it and depending on it at a
  positive need, which under `Dependent` stands at that step; and a relatum given to as
  it comes to stand descends from the formation taking part that gives to it.
  An embodied relatum that arises descends from another active formation, so under N_rel
  valuing that formation reaches the arisen relatum's living events, and generations each
  given by the one before are connected by descent alone. Whether these readings count
  as formed relations is Ren's choice.

The core imports nothing else, every source declaration has an empty axiom report, and
it compiles from Lean's prelude alone. Of the constants Lean generates, only the
injectivity lemmas of constructors with fields depend on an axiom, `propext`; no source
declaration uses them. `Becoming.Bridge` lies outside the core: it shows
that existing modules' interfaces are these, so dependence runs toward the core.

The foundation keeps its historical namespace `Generative`. Its processes are any
becoming, including maintenance and degeneration, not only generative change.
-/
