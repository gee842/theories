#!/usr/bin/env python3
"""One checker for the Becoming package: the formal core and its bridge.

The package names modules by path (`Becoming/Frame.lean` is `Becoming.Frame`); other
modules are found by file name under the Lean root. The checker resolves the import
closure, requires every inherited module's current bytes to match a passed receipt,
compiles the closure in dependency order with Lean 4.29.1 and audits the axioms of
every source declaration. Inherited reports are recorded, not changed.

The core is pure: its import closure is exactly the foundation and the core modules,
every source declaration in that closure has an empty axiom report, and the closure
compiles from Lean's prelude alone (the foundation's `import Std` line is removed for
that run). The constants Lean generates in the closure are audited as well: the only
ones depending on an axiom are the injectivity lemmas of constructors with fields
(`injEq`), on `propext`, which no source declaration uses; the receipt lists them.
The bridge imports existing modules to show that their interfaces are the core's;
nothing in the core imports it, and its declarations also have empty axiom reports.
"""
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
LEAN_ROOT = HERE.parent
sys.path.insert(0, str(LEAN_ROOT / "universal-ethics" / "generative-capacity"))
import check as audit_support  # noqa: E402

# The foundation the core builds on (L0 and its two direct companions).
FOUNDATION = ["GenerativeCore", "InquirySufficiency", "RelationalRenewal"]
# The package, in layer order: the four core layers and their root, then the bridge.
CORE = ["Becoming.Frame", "Becoming.Inquiry", "Becoming.Renewal", "Becoming.Dependence",
        "Becoming.Return", "Becoming.Horizon", "Becoming.Joint", "Becoming.Substitution",
        "Becoming.Generation", "Becoming.Flow", "Becoming.Change", "Becoming.Population",
        "Becoming.Identity", "Becoming.Wholes", "Becoming.Dissipation", "Becoming.Roles",
        "Becoming.Reserve", "Becoming.Evolution", "Becoming.Space", "Becoming.Premises",
        "Becoming.Openness", "Becoming.Metaethics", "Becoming.Ranking", "Becoming.Correspondence", "Becoming.Descent",
        "Becoming"]
BRIDGE = ["Becoming.Bridge"]
SPINE = CORE + BRIDGE
PURE = FOUNDATION + CORE
RECEIPT = HERE / "becoming-verification.json"
RETAINED = HERE / "becoming-checks"

SCOPE = (
    "Spine: a Frame is the core Process with realized claims; runs, reachability, invariants and new "
    "realization are defined through the core Trace; the visible scope of an inquiry is the set of "
    "configurations its actual executions reach, and a sound policy secures its goal there. "
    "Renewal: a run read through observables of conditions is one relational unfolding; an observable "
    "that never rises from some step on falls only finitely often, with depletion, recurrent renewal "
    "under a natural-number rank and unrenewed drawdown as its cases; in one process from one "
    "configuration one run renews and another consumes. "
    "Dependence: which conditions a formation depends on, at what level, and which it draws on may "
    "change from step to step; constant dependence recovers the static reading exactly; every met "
    "dependence is kept or broken across each step; consumption as inherited admits a requirement "
    "never met, which consumes its condition with no break; where activity needs current support, a "
    "formation still active after a loss without return has weakened or dissolved its dependence, and "
    "with fixed dependence it is no longer active, both contrapositives of that premise; these "
    "outcomes are neither exhaustive nor exclusive, and in one process from one configuration a break "
    "of the same dependence, read at the start of its step, is followed by an ending, a transformation "
    "and a restoration; an event is within renewal when its step keeps every dependence on the "
    "conditions it participates in, breaking when it draws on a condition at a step that breaks a "
    "dependence on it, and undermining when it draws on a condition at a step after which the "
    "condition is below both the present need of a dependence on it and a need of that dependence "
    "met at some step of its tenure, so that a level from before the dependence held and a "
    "dependence never met at its own need do not count, falling short only of a need grown beyond "
    "what was met is not undermining, a draw below a need that was met undermines after the need "
    "has grown, and a dependence that lapses for one step starts a new tenure; breaking is "
    "undermining, drawing after a loss can undermine without breaking, and "
    "drawing that changes no level can undermine; the stepwise and whole-run readings credit "
    "different events in both directions. "
    "Return: a dependence returns within p steps when it is met at one of the next p; renewal, "
    "renewal within one step, within p, return and non-consumption are ordered, and consumption is "
    "exactly a dependence that never returns; renewal within one step does not imply renewal, and "
    "cycles of length zero are degenerate; a seasonal condition is renewed within two steps and "
    "not one; a recovery can slow without bound, returning always while no cycle bounds it; over "
    "cycles of two a dip is credited, and an escalation undermines for every cycle. "
    "Horizon: for every horizon two runs of one process agree up to it, drawing beyond renewal with "
    "every event within renewal, and afterwards one renews and the other consumes; a reading decided "
    "by a finite prefix that credits every renewing run credits a consuming one; the renewing run "
    "itself draws beyond renewal before the horizon and the whole-run reading credits it; a reading "
    "of amounts per step is fixed by the history through the step and withholds every such draw; "
    "the formation-level cycle readings are not fixed by any finite prefix; and the same holds in "
    "the support-gated law, whose renewal stops below support. "
    "Joint activity: withholding a formation's part with the same move taken, which must still be "
    "available, the loss is kept or broken; when with any single part withheld the same move still breaks, no part alone makes the "
    "difference; from one configuration a lone drawer's part makes the difference under a calm move "
    "and the loss is overdetermined under a shock; with the shock written into the step relation "
    "of one move the move does not determine the step and the loss is overdetermined though the "
    "calm outcome would keep the dependence, and a move no withheld configuration can take makes "
    "no part decisive; when the move determines the step and can be taken with a part withheld, "
    "and the dependence still holds and is met there, either the part makes the difference or the "
    "same move still breaks the dependence; in one process a drawer's part makes the "
    "difference with one other drawer and not with two, while the relational reading counts it "
    "consuming in both; a drawer taking exactly the renewal makes no difference and still "
    "undermines; drawing beyond renewal at every step consumes the condition, the first event "
    "undermines for no positive cycle, with every draw before any step withheld the condition is "
    "still consumed, and at the breaking step drawing nothing keeps the dependence. "
    "Substitution: in the support-gated law, a focal formation that can substitute an alternative "
    "condition stays active, transforms its dependence at a step that can be found, and consumes, "
    "while the sustaining formation ends; a concrete law meets the premises, and there the stepwise "
    "reading credits the focal formation at every step but the one at which the sustaining "
    "formation loses support; in another law of the family it is withheld at two steps, until it "
    "switches. "
    "Generation: a formation arises when it is inactive before a step and active after it, and "
    "generation is unceasing when some formation arises at arbitrarily late steps; an event "
    "depletes a finite family when at each of its steps at which no condition of the family rises "
    "one of them falls, which says only that some condition of the family changes at each of its "
    "steps; a finite family none of whose conditions rises from some step on is depleted by only "
    "finitely many events; so where arising depletes such a family, unceasing generation makes "
    "some condition of it rise at arbitrarily late steps, and, every rise being made by a "
    "formation renewing it, renewing activity recurs; a formation lowering such a family at each "
    "active step is active only finitely often however it substitutes; if a quantity never rises "
    "and every arising lowers it, generation is not unceasing, while a closed cycle whose total "
    "stays constant sustains unceasing generation; a flicker depending and drawing on nothing "
    "arises unceasingly, each arising depleting an unrelated tide; a tide renewed by the moon "
    "rises at arbitrarily late steps while nothing arises, and drawing what is renewed keeps every "
    "dependence while nothing arises; arising on a consumed condition ceases; and a formation "
    "arising again and again on a renewed condition meets every premise, each arising coming at a "
    "rise, while the stepwise reading withholds each of its blooms and the reading over cycles of "
    "two credits it. "
    "Flow: when every change of a condition's level is what the formations taking part take and "
    "give, the family's total plus its uptake equals its total before plus its replenishment, over "
    "a step and over any stretch, every rise is made by an active renewer, and every fall is "
    "taken from, by an active formation drawing on it where only active formations take; "
    "positive uptake at "
    "arbitrarily late steps needs replenishment at arbitrarily late steps, so when formations "
    "taking from the family at their first active step arise at arbitrarily late steps, formations "
    "replenish the family at arbitrarily late steps, and so they do for a constant consumer with "
    "nothing arising; over any stretch from which at least K formations take, the family is "
    "replenished by at least K per step less its stock at the start, and with each formation "
    "giving at most a fixed amount the renewers grow in the same averaged sense; so generation that is more without end, with ever more formations taking "
    "from a finite family from some step on, needs replenishment that no eventual bound bounds "
    "and, each formation giving at most a fixed amount, renewers that no eventual bound bounds, "
    "who can still be absent at infinitely many steps; renewers and growers arising at every step "
    "meet these premises with a level that never rises, so that arising there does not deplete "
    "the family in the net sense; the unceasing bloom is not more without end; and in a closed "
    "cycle each formation gives back what it takes, the total never changes, and generation is "
    "more without end with as many renewers as takers; every rise of a condition is given to, "
    "so a rising condition replenishes every family containing it, and where members of a "
    "family rise at arbitrarily late steps its replenishment recurs, whatever is taken; a "
    "condition coming to stand, its level zero before a step and positive after, rises and is "
    "given at least its new standing, and a condition can rise at every step without coming "
    "to stand. "
    "Change: with no premise about an unfolding, a determination comes to be across a step where "
    "it fails before and holds after, and ceases to be where it holds before and fails after; a "
    "formation arising and ceasing, a dependence forming and dissolving and a condition coming to "
    "stand and ceasing to stand are this one change; a decidable determination that ceases at no "
    "step from some step on holds on; a formation stays supported where each dependence it has it "
    "had before, at no greater need, on a condition standing no lower; over any stretch an amount "
    "at the end with everything it fell is the amount at the start with everything it rose, and "
    "so for the total of a finite family with the rises and falls of its members; since no amount "
    "falls below zero, a finite family falls over any stretch by at most its total at the start "
    "more than it rises, so members falling at arbitrarily late steps rise at arbitrarily late "
    "steps, which for one amount is the law that an observable never rising from some step on "
    "falls only finitely often, and with the amounts bounded the family rises by at most its "
    "bound per member more than it falls, so rising at arbitrarily late steps needs falling at "
    "arbitrarily late steps; so in a finite family of decidable determinations the members "
    "holding at the end with those that ceased to be are those holding at the start with those "
    "that came to be, comings and ceasings over any stretch differ by at most the number of "
    "members, and coming to be recurs exactly when ceasing to be recurs: given decidable "
    "activity, the members of a finite family of formations active at the end with those that "
    "ceased are those active at the start with those that arose, they arise at arbitrarily late "
    "steps exactly when they cease at arbitrarily late steps, and with finitely many formations "
    "generation is unceasing exactly when some formation ceases at arbitrarily late steps; with "
    "no premise at all, conditions of a finite family come to stand "
    "at arbitrarily late steps exactly when they cease to stand at arbitrarily late steps; ever "
    "new formations can arise with none ceasing while a level rises at every step and never "
    "falls, and formations all active at the start can cease one after another with nothing "
    "arising. "
    "Population: a census lists the formations active at each step, each once; if more are active "
    "after a step than before, one arises across it, and a census growing without bound makes "
    "generation unceasing; under a census, with each formation taking part in a flow listed once "
    "and only active formations taking, more without end makes the active formations grow without "
    "bound and generation unceasing, and the garden and the cycle meet all these premises; the "
    "unceasing bloom meets these premises and is not more; without a census every formation of an "
    "infinite family can be active from the start and more without end comes with nothing "
    "arising, with takers that are never active the same holds under a census, and so it does "
    "with one formation listed many times in the flow; ever more formations can draw on a "
    "condition while the flow records no taking. "
    "Identity: re-identifying formations one to one at each step leaves every step's levels, "
    "activity, dependences and drawing unchanged; a renaming preserves the readings that follow "
    "a formation, and every re-identification preserves support, keeping and breaking, the class "
    "of every condition, whether activity needs support, being within renewal and breaking at "
    "each event, what a flow takes and gives, the counts of takers and renewers, so more without "
    "end, a census of the active formations and that only active formations take, so that under "
    "a census more without end makes generation unceasing under every re-identification, as in "
    "the garden; exchanging names at odd steps turns a renewing and a consuming formation into two "
    "consuming, removes undermining after the first step and makes formations arise without end, "
    "and arisings made by naming alone can meet every premise of the recurrence of renewal; "
    "keeping the names of continuing activity makes no arising and keeping those of continuing "
    "dependences removes no undermining, while succession, joining a formation that ends with one "
    "that begins then or later, can hide arising in a lineage and make drawing after an elder's "
    "loss undermine a living heir, both namings keeping continuity only one way; kept both ways, "
    "continuity preserves arising and undermining exactly and excludes a join at a single step, "
    "and joining across a dormant step still changes which formation renews and which consumes; "
    "under a census, with each formation taking part listed once and only active formations "
    "taking, under every continuation in which no formation continues as two, every "
    "re-identification and a continuation with merges among them, more without end makes "
    "formations arise at arbitrarily late steps, a decidable continuation giving the "
    "decidability this asks; on the garden, whose formations never end, a merge comes with a "
    "persisting formation re-read as arising at every step, while where the merged formation "
    "ends what arises under a merge is exactly what is new; without a census it does not, with "
    "new formations budding from one "
    "already there it forces no arising, and a single split need not defeat arising, so no split "
    "is sufficient, not necessary; a lineage named beside its members is active at every step "
    "while they arise without end. "
    "Wholes: a formation is the whole of some parts when it is active exactly while some part is, "
    "a coincidence of activity by which every formation is the whole of itself and two formations "
    "always active are each the whole of the other; a whole arises only as some part arises; "
    "parts covering every step from some step on, none active at two steps d apart, have a part "
    "arising within every d consecutive steps, a bound attained by members working in shifts and "
    "met by two members arising again and again, and parts covering every step from some step "
    "on, each of whose activity ends, with the active ones listed, arise at arbitrarily late "
    "steps outside every finite list of parts; a whole active at every step from some step on is "
    "covered by its parts; "
    "with a part that never ends, or infinitely many parts active at once, it persists while "
    "nothing arises, and parts arising without end may leave the whole inactive between them. "
    "Dissipation: a family is closed across a step when no formation taking part exchanges with "
    "a condition outside it, and is dissipated on when every formation taking part gives it no "
    "more than it takes from it and less when it takes; in a balanced flow a family dissipated on "
    "falls across a step by at least its number of takers, its takers over all later steps number "
    "at most its stock, and taking from it does not recur; so under dissipation on every closed "
    "family without repetition, a finite family from which formations take at arbitrarily late "
    "steps, and every finite family without repetition containing it, is open at arbitrarily late "
    "steps, more without end, the unceasing arising of takers and one eater kept up with nothing "
    "arising being such taking, and with finitely many conditions in all taking does not recur; "
    "a step is enclosed when some finite family without repetition is closed across it, as when "
    "finitely many conditions are all there is, and under dissipation a formation that gives "
    "takes more than it gives over every closed family without repetition, so across an enclosed "
    "step giving needs uptake, while where no step is enclosed dissipation holds vacuously and a "
    "renewer can give taking nothing; a step is enclosed around a family when a finite family "
    "without repetition containing it is closed across it, as every enclosed step is when "
    "equality is decidable, and under dissipation a finite family from which taking recurs and "
    "which is enclosed around from some step on draws in: at arbitrarily late steps a formation "
    "gives to it and takes from beyond it; a sun burning a fresh fuel at every step and giving a "
    "pool less than it "
    "burns, while ever more growers take from the pool, meets these premises, with the growers "
    "depending on the pool under a census as well, every step being enclosed and the pool drawing "
    "in the fuel; the flows of the earlier witnesses in which "
    "taking recurs on one condition are not dissipative; a member of a family dissipated on "
    "rising, as in coming to stand, lowers its stock, so members of a family dissipated on from "
    "some step on neither rise nor come to stand at arbitrarily late steps; under dissipation a finite family without "
    "repetition whose members rise, as in coming to stand, at arbitrarily late steps is open at "
    "arbitrarily late steps and, enclosed around from some step on, draws in, and with finitely "
    "many conditions in all none rises at arbitrarily late steps; across a step dissipated on, "
    "a family's members fall by at least as much as they rise and by one more for each formation "
    "taking from it, so a formation taking from it makes a member fall whether or not another "
    "rises, an event at whose steps the family is dissipated on and taken from depletes it, and a "
    "member rising comes with another member falling across the same step, so that under "
    "dissipation a member of a family without repetition rising while none falls shows the "
    "family open across that step, an active formation "
    "giving to the one and taking from the family and an active formation drawing on the other "
    "taking from it where only active formations give and take. "
    "Roles: a web or flow read with one kind of relatum, in which no formation is a condition, keeps "
    "support, dependence, renewal, consumption, the classes of formations, undermining, living "
    "events, arising, unceasing generation and a census, and what is taken and given, balance, "
    "that only active formations give and take, a present without repetition, takers, renewers, "
    "more without end and dissipation, and in it no active formation stands as a condition "
    "exactly while it is active or depends on itself; relabelling the conditions of a one-kind "
    "web onto themselves keeps dependence and undermining and changes which relata are embodied "
    "and which depend on themselves, so that identification is supplied by the shared index; "
    "where a relatum is so embodied and activity needs "
    "support, a formation depending on it at a positive need is active only while it is, activity "
    "passes along every chain of such dependence so that a relatum not active ends every formation "
    "whose chain reaches it, consuming it at a need of one ends it, a dependence on itself is met "
    "exactly while it is active, drawing on it across the step at which it ends breaks that "
    "dependence whatever ends it, even for a drawer that takes nothing and for its own last event, "
    "and in a balanced flow in which only active formations give it arises only as another active "
    "formation gives to it, a formation that need not be embodied, and that is embodied where "
    "only embodied relata give, as a sun depending on nothing can be; a "
    "bee and a flower renew each other, a fox ends with the hare it draws on, and generations arise "
    "without end each given by the one before; an embodied relatum comes to stand as it arises, "
    "so it is given at least the standing it arises with, its arising replenishes every family "
    "containing it and embodied "
    "generation recurring in a family needs its replenishment to recur whatever is taken; "
    "whatever gives to a family dissipated on takes from it, so the arising of an embodied member "
    "of a family dissipated on lowers its stock and embodied members of a family dissipated on "
    "from some step on do not arise at arbitrarily late steps; under dissipation a finite family "
    "without repetition in which embodied members arise at arbitrarily late steps is open at "
    "arbitrarily late steps, and enclosed around from some step on it draws in, and with "
    "finitely many relata in all embodied arising does not recur; the arising of an embodied "
    "member of a family dissipated on comes with another member falling across the same step, "
    "while each generation of the brood arises in a closed family of it and the one before with "
    "nothing falling, so that family is not dissipated on; two sides handing one "
    "standing back and forth bear unceasing generation in a closed world without dissipation, "
    "burning a fresh fuel they bear it under dissipation while every finite family containing a "
    "side opens and the family of the sides draws in the fuel, with a sink exchanging with ever "
    "new relata instead dissipation holds vacuously and the sink opens the family of the sides "
    "while nothing flows into it, and a relatum whose activity is not its standing arises again "
    "and again with nothing given to it. "
    "Reserve: a reserve does not rise across a step at which its formation is unsupported and "
    "falls across each such step at which the formation is active; the zero reserve is exactly "
    "the premise that activity needs support, a condition in a balanced flow given nothing while "
    "its holder is unsupported and taken from, by whatever takes part, while the holder is active "
    "there is a reserve, as it is where the holder itself takes part and takes from it, while "
    "the supplied reserves of the dormant seeds are held by no condition of their webs, and an "
    "active formation whose dependences fail has a positive reserve, so where a held condition "
    "carries the formations, moving each unsupported dependence onto it at need one keeps "
    "levels, activity and drawing and meets the premise that activity needs support by "
    "construction; a formation unsupported from "
    "some step on is active only finitely often, over any stretch at most as often as its "
    "reserve at the start, and arises only finitely often, so after a loss without return, and "
    "after the end of an embodied relatum it depends on at a positive need, it is active beyond "
    "its support at most as often as its reserve; a reserve that also falls across every "
    "unsupported step at which it is positive bounds the time as well, the formation being "
    "inactive once as many steps have passed as its reserve; a relatum standing as a condition "
    "while active, absent at some step and active later, came to stand across some step in "
    "between; a seed waking twice in the dark on "
    "its reserve, a seed waking once before its viability is spent and a fox outliving the hare "
    "by its fat attain these bounds, and the fox read with its dependence "
    "moved onto its fat meets the premise that activity needs support, its event at step one "
    "then not undermining, as it is under the published reading; a seed given its "
    "standing while dormant arises later with nothing given to it, and a relatum standing "
    "throughout wakes without end with nothing given to it, nothing taking part in its flow. "
    "Metaethical core: on a connected whole with some living claim, significance of every living claim "
    "from every standpoint (G0 at claim level) is equivalent to a seed together with relational and "
    "standpoint neutrality; the positioned articulation D follows from the articulation premise A; a "
    "sound inquiry for new living content gives every position with access a contributory reason; "
    "G0, C, D and the secured positive ground are stated in the core, which imports no ethics module. "
    "Each of seed, relational neutrality, standpoint neutrality, connection and A has a consistent "
    "countermodel, and each rival satisfies the same rule inside a formed boundary. The lifting rule L "
    "is transitive only through a live middle response. No premise is proved, no rejecting position is "
    "bound, and no duty, ranking, recognition or compliance is inferred. On a run read relationally, "
    "a condition in which every living formation participates discharges connection, and without one "
    "connection can fail; a consuming formation and one losing its support co-participate in the "
    "drawn condition, so under N_rel valuing the consumer's activity reaches the living events of the "
    "formation losing support. Read stepwise, an event is living when active and not undermining; the "
    "same discharge holds, an event drawing at a step that breaks a dependence is related to the "
    "broken formation, so under N_rel valuing it reaches that formation's living events, and both "
    "readings credit the broken formation's own event. Read through relations, the stepwise reading "
    "of an event is the conjunction of the reading of its relations, and one event can have a living "
    "relation and an undermining one. "
    "Ranking: C over courses is stated through a frame whose realized claims are the events a "
    "reading credits; the course without a formation extends the course with it only if the reading "
    "withholds every event of that formation; under the whole-run reading, for every law of the "
    "support-gated family in which the focal formation draws beyond renewal, the course without it "
    "extends the course with it, so every comparison satisfying C ranks it higher; under the stepwise "
    "reading an event of the formation whose step leaves every need met is credited, neither course "
    "extends the other, and an irreflexive, transitive comparison satisfying C prefers the course with "
    "the formation, malignant growth and winning by consumption being instances, while with no "
    "credited event of the formation the stepwise reading too ranks its absence higher; under the "
    "stepwise "
    "reading sharing still extends winning by consumption; under either reading a course in which "
    "every need stays met extends a course of the family in which overdraw ends the sustaining "
    "formation's support, malignant growth being ranked below the same formation stopping before "
    "the threshold, while with a third formation sharing the condition neither course extends the "
    "other under the stepwise reading. "
    "Correspondence: under the discipline that two events are related through a condition only "
    "when one draws on it and the other depends on it at a positive level, a condition nothing draws "
    "on or no dependence on which can fail relates nothing and undermines nothing, and adjoining one "
    "leaves living, the relation and connection unchanged, while under co-participation adjoining a "
    "condition every formation requires at level zero connects every web; every undermining relation "
    "is an interaction, though interaction orders no steps and does not ask whether the drawing "
    "changes the level, and under N_rel valuing any drawing event reaches every living dependent "
    "at a positive level; a condition on which every living event bears, with a living drawer and a "
    "living dependent, connects the whole; in one example two dependents are connected through a "
    "living use of their condition and not when its only use undermines them, while co-participation "
    "connects them in both; adjoining a renewed condition every formation depends on at a positive "
    "level, drawn on by one living event, still connects every web without changing living; read "
    "with one kind of relatum a web keeps the connection of co-participation and of interaction, "
    "drawing on a relatum that depends on itself interacts with each of its active events, so a bee "
    "and a flower each depending on itself and on the other are connected with no third condition "
    "and G0 there is exactly a seed with both neutralities, while where each depends only on the "
    "other neither co-participation nor interaction relates the bee to the flower, though both "
    "are embodied; relabelling the conditions of a one-kind web onto themselves keeps the "
    "connection of both valuations. "
    "Evolution: a relatum descends from a formation across a step when the formation takes part "
    "in the step and gives to it and the relatum comes to stand across it; over any finite family "
    "of parents, each with finitely many offspring, and any amounts read of them, the offspring's "
    "total with what transmission lowered equals the parents' amounts, each counted once for every "
    "offspring, with what transmission raised, Price's equation in additive form with no premise; "
    "where only active formations give and activity needs support, a formation a relatum descends "
    "from across a step is supported there, so one unsupported at a step leaves no descendant "
    "across it and one never supported leaves none, and read of needs on a condition every parent "
    "depends on, the selection term is at most the level counted once for every offspring; where "
    "a flow transmits a dependence within a bound, a descendant depending on the condition at its "
    "first standing step descending only from formations depending on it and needing it at most "
    "the bound more, a descendant's need is at most the condition's level at the giving step plus "
    "the bound, and in a balanced flow its need with everything taken from the condition since an "
    "earlier step is at most the level then with everything given since, plus the bound; a parent "
    "taking from a pool and giving to two descendants leaves the one inheriting its need "
    "unsupported from its first standing step on, while the one needing less is supported, active "
    "and takes in turn, and without the premise that activity needs support a formation active "
    "beyond its support transmits a need above the level at its giving step. "
    "Space: a world is relata read with one kind, the flow among them and their web, and the "
    "space is every world; the laws stated with no premise hold of each; in a finite world whose "
    "activity is decided, generation recurs exactly when degeneration does, while with infinitely "
    "many relata either recurs without the other; activity needing support, balance, only active "
    "formations giving, only active formations taking what they draw on, dissipation, embodiment "
    "and a reserve carrying activity are each met by some worlds and not by others; among finite "
    "worlds generation recurring or not occurs both with every event living and with some event "
    "not living; in a finite, balanced, dissipative world in which whatever arises is embodied, "
    "neither generation nor degeneration recurs, and without finiteness, dissipation, balance or "
    "embodiment generation can recur. "
    "Premises: a census and bounded transmission are premises of worlds too; activity needing "
    "support makes activity carried, embodiment makes whatever arises embodied, a finite world "
    "whose activity is decided has a census, and where only active relata take and the flow "
    "dissipates only active relata give across every enclosed step, as every step of a finite "
    "world is; activity needing support, balance, only active relata giving, only active relata "
    "taking what they draw on, dissipation, embodiment, a census and bounded transmission are "
    "independent, each failed by a world meeting the other seven, the worlds failing a census or "
    "only active relata giving being infinite; mutualists active throughout meet all eight, and "
    "in a finite world the eight together bring generation and degeneration to an end. "
    "Openness: under balance and dissipation, across a step enclosed around what stands, the "
    "total standing does not rise and any condition's standing rising or falling lowers it, so "
    "where what stands is listed and every step from some step on is enclosed around it, "
    "standing stops changing; a world with a census whose relata are embodied, balanced and "
    "dissipative, enclosed from some step on, comes to rest without being finite, so its "
    "generation without end needs steps not enclosed; the sides of Handing exchanging with an "
    "unbounded ground meet all eight premises, no step enclosed, and generate without end. "
    "Descent: read with one kind of relatum, an event living on a relatum, drawing on it and "
    "depending on it at a positive need, is related to that relatum's events, and an event is "
    "related to the events of the relata it descends from and that descend from it, descent "
    "relating every event of the two, while a gift entry "
    "of a formation taking no part makes no descent; living on, like interaction, needs a "
    "dependence that can fail, so under the premise that activity needs support the relatum an "
    "active formation lives on stands at that step and, if embodied, is active there, while a "
    "dormant relatum standing while asleep can be lived on; under N_rel valuing an "
    "event that lives on a relatum reaches that relatum's living events and conversely, and "
    "valuing any event of a formation reaches the living events of the relata descending from "
    "it and conversely; in a balanced flow in which only active formations give, an embodied "
    "relatum that arises descends from another formation active at that step; generations "
    "each given by the one before are connected by descent and by neither co-participation "
    "nor interaction, and G0 there is exactly a seed with N_rel and N_std; a bee and a flower "
    "depending only on each other are connected by living on, and relabelling their "
    "conditions each onto the other keeps co-participation and interaction and removes that "
    "connection; a seed descends from the parent that provisioned it while dormant, and "
    "waking from dormancy descends from nothing. "
    "Instances: the core's G0, C, D, secured ground and relational living are by definition those of "
    "the existing modules, the core's whole-run reading of courses is the relational inventory of "
    "RenewalComparison with the same undisturbed levels, and J1/J2 on configurations is "
    "PracticalJudgment.Better; "
    "seed-edge closures and evaluator chains are reachability on the edge process; a "
    "frame's reachable configurations form a joint-continuation space whose bundles step-preserving "
    "maps carry and lifting summaries reflect; robust responses, guarantees, live steps and evidence "
    "narrowing by a rule list are common responses, one-step completion, enabledness and After on a "
    "pure observation; the functional articulation of a situation is exactly the deterministic case "
    "of the articulation under L, and the lifted comparison, reason, survival and continual-improvement "
    "results hold on every frame. A countermodel shows that L is substantive: a response with one "
    "better and one worse outcome is comparable in neither direction."
)


# Every constant of the core closure, generated ones included, with the axioms it uses.
ENVIRONMENT_AUDIT = """import Lean
{imports}
open Lean Elab Command

#eval show CommandElabM Unit from do
  let env ← getEnv
  for m in [{modules}] do
    let some index := env.getModuleIdx? m | throwError m!"no module {{m}}"
    let mut count := 0
    for (n, _) in env.constants.map₁.toList do
      if env.getModuleIdxFor? n == some index then
        count := count + 1
        let axioms ← liftCoreM <| Lean.collectAxioms n
        if axioms.size > 0 then logInfo m!"AXIOMS {{n}} {{axioms.toList}}"
    logInfo m!"CONSTANTS {{m}} {{count}}"
"""


# Directories holding retained runs, frozen copies and development attempts.
ARCHIVE = re.compile(r"(-checks|-runs|-history|-development|verification.*)$"
                     r"|^(checks|runs|sources|revalidation|retained.*|history|archive.*)$")


def module_index():
    index = {}
    for path in LEAN_ROOT.rglob("*.lean"):
        if any(ARCHIVE.search(part) for part in path.relative_to(LEAN_ROOT).parts[:-1]):
            continue
        name = ".".join(path.relative_to(HERE).with_suffix("").parts) if HERE in path.parents else path.stem
        index.setdefault(name, []).append(path)
    return index


def source_file(name):
    """Where a module sits in the compile directory: `Becoming.Frame` → `Becoming/Frame.lean`."""
    return name.replace(".", "/") + ".lean"


def imports_of(data):
    code = audit_support.code_only(data.decode())
    return [m.strip() for m in re.findall(r"^import\s+(.+)$", code, re.M) if m.strip() != "Std"]


def closure(index, roots=SPINE):
    order, seen = [], set()

    def visit(name, stack):
        assert name not in stack, ("import cycle", stack + [name])
        if name in seen:
            return
        paths = index.get(name, [])
        assert len(paths) == 1, (name, [str(p) for p in paths])
        for dependency in imports_of(paths[0].read_bytes()):
            visit(dependency, stack + [name])
        seen.add(name)
        order.append(name)

    for name in roots:
        visit(name, [])
    return order


def passed_receipts():
    receipts = []
    for path in LEAN_ROOT.rglob("*.json"):
        if path == RECEIPT or RETAINED in path.parents:
            continue
        relative = path.relative_to(LEAN_ROOT)
        text = path.read_text(errors="replace")
        if '"passed"' in text:
            receipts.append((str(relative), text))
    return receipts


def declarations(data):
    # A root module only imports and documents; it declares nothing.
    if not re.sub(r"^import .+$", "", audit_support.code_only(data.decode()), flags=re.M).strip():
        return []
    # The inherited scanner accepts only Std/GenerativeCore imports; it reads a copy
    # with imports replaced. Compilation uses the unchanged bytes.
    return audit_support.declarations(re.sub(r"^import .+$", "import Std", data.decode(), flags=re.M))


CONTROLS = """import Becoming.Bridge
open Becoming Generative Generative.InquirySufficiency

-- The full premise set is consistent: the model satisfies seed, both neutralities and connection.
example : (Model.valuation Model.linked (fun _ _ => True)).Grounds :=
  ((Model.valuation Model.linked (fun _ _ => True)).significant_iff
    (Model.linked_connected _) .evaluator (c₀ := .self) trivial).mp (fun _ _ _ => trivial)

-- The headline theorem has a nonvacuous instance: one step forms a new living claim.
def grow : Frame Bool Unit Unit := ⟨⟨fun s _ t => s = false ∧ t = true⟩, fun s _ => s = true⟩
def everyone : Valuation Model.Who Unit :=
  ⟨fun _ => True, fun _ _ => True, fun _ _ => True, fun _ _ => True⟩
def zero : Fin 2 := ⟨0, Nat.zero_lt_succ 1⟩
def sense0 : Bool → Unit → Bool → Fin 2 := fun _ _ _ => zero
def respondOnce : Unit → List Unit := fun _ => [()]
def believed : Bool → Prop := fun s => s = false
def access : Model.Who → Policy Unit Unit 2 → Prop := fun _ _ => True
def nothingBefore : Bool → Unit → Prop := fun _ _ => False

/-- The least reason satisfying A. -/
def routeReason (p : Model.Who) (r : Policy Unit Unit 2) : Prop :=
  access p r ∧ SecuresPositiveGround (Scope grow.P sense0 respondOnce believed) nothingBefore
    (fun _ c => everyone.sig p c) r

theorem grow_sound :
    Sound grow.P (fun _ _ _ => True) (Novel grow everyone.living nothingBefore)
      sense0 respondOnce (.respond ()) believed :=
  ⟨⟨false, rfl⟩, fun s held => by
    cases held
    exact ⟨⟨true, rfl, rfl⟩, fun t step => ⟨trivial, by
      cases step.2
      exact ⟨(), trivial, rfl, id⟩⟩⟩⟩

theorem grow_reason : ∀ p, access p (.respond ()) → routeReason p (.respond ()) :=
  universal_reason grow everyone nothingBefore access routeReason
    ⟨⟨.evaluator, (), trivial, trivial⟩, fun ⟨_, _, _⟩ _ _ _ => trivial,
      fun ⟨_, _, _⟩ _ _ => trivial⟩
    (fun _ _ _ _ => Reach.refl _ _)
    (fun ⟨_, _⟩ available secured => ⟨available, secured⟩)
    (.respond ()) grow_sound

-- The continuation instance is nonvacuous: a reached configuration realizes the living claim.
example : JointContinuationClassification.Jointly (grow.continuations false) (fun _ => True) :=
  ⟨true, Reach.of_step (a := ()) ⟨rfl, rfl⟩, fun _ _ => rfl⟩

-- The common-condition discharge is nonvacuous: in the commons, every formation participates.
example : (Commons.conditions.valuation Commons.sharing (fun (_ : Unit) _ => True)
    (fun _ _ => True)).Connected :=
  Commons.conditions.connected_of_common Commons.sharing _ _ ()
    (fun e _ => match e with
      | (.focal, _) => Or.inr trivial
      | (.sustaining, _) => Or.inl trivial)

-- The stepwise discharge is nonvacuous: its first event is living in the escalating run.
example : ((Commons.conditions.dependence.along Commons.escalating).valuation
    (fun (_ : Unit) _ => True) (fun _ _ => True)).Connected ∧
    ((Commons.conditions.dependence.along Commons.escalating).valuation
      (fun (_ : Unit) _ => True) (fun _ _ => True)).living (.focal, 0) :=
  ⟨Web.connected_of_common _ _ _ ()
    (fun e _ => match e with
      | (.focal, _) => Or.inr trivial
      | (.sustaining, _) => Or.inl trivial),
   ⟨trivial, Commons.stepwise_credits_before_escalation.2.1.not_undermining⟩⟩
"""


def main():
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
    retained = RETAINED / stamp
    retained.mkdir(parents=True, exist_ok=False)
    index = module_index()
    order = closure(index)
    core_closure = closure(index, CORE)
    paths = {name: index[name][0] for name in order}
    sources = {name: paths[name].read_bytes() for name in order}
    helpers = {p.name: p.read_bytes() for p in [Path(__file__), LEAN_ROOT / "universal-ethics" / "generative-capacity" / "check.py"]}
    for name, data in helpers.items():
        (retained / name).write_bytes(data)
    for name, data in sources.items():
        (retained / (name + ".lean")).write_bytes(data)
    receipt = {
        "status": "checking", "utc": stamp, "toolchain": audit_support.TOOLCHAIN,
        "retained_run": str(retained.relative_to(HERE)),
        "spine_modules": SPINE,
        "core_modules": CORE, "foundation_modules": FOUNDATION, "bridge_modules": BRIDGE,
        "core_closure": core_closure,
        "compile_order": order,
        "source_paths": {name: str(paths[name].relative_to(LEAN_ROOT)) for name in order},
        "source_sha256": {name: audit_support.digest(data) for name, data in sources.items()},
        "checker_sha256": {name: audit_support.digest(data) for name, data in helpers.items()},
        "scope": SCOPE,
    }
    try:
        assert sorted(core_closure) == sorted(PURE), ("core imports outside the core", core_closure)
        inherited = [name for name in order if name not in SPINE]
        receipts = passed_receipts()
        matches = {}
        for name in inherited:
            found = sorted(path for path, text in receipts if receipt["source_sha256"][name] in text)
            assert found, ("inherited module has no passed receipt for its current bytes", name)
            matches[name] = found
        receipt["inherited_receipts"] = matches
        registry = {name: declarations(data) for name, data in sources.items()}
        lean = Path.home() / ".elan/bin/lean"
        binary = Path.home() / ".elan/toolchains/leanprover--lean4---v4.29.1/bin/lean"
        receipt["lean_binary_sha256"] = audit_support.digest(binary.read_bytes())
        command = [str(lean), "+" + audit_support.TOOLCHAIN]
        records = []
        with tempfile.TemporaryDirectory(prefix="becoming-spine-lean-") as scratch:
            work = Path(scratch)

            def run(args, log, where=work):
                env = {**os.environ, "LEAN_PATH": str(where)}
                p = subprocess.run(command + args, cwd=where, env=env, text=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=600)
                (retained / log).write_text(p.stdout)
                assert p.returncode == 0, p.stdout
                assert not re.search(r"\b(?:error|warning):", p.stdout), p.stdout
                return p.stdout

            receipt["lean_version"] = run(["--version"], "version.log").strip()
            assert "version 4.29.1" in receipt["lean_version"]
            for name, data in sources.items():
                target = work / source_file(name)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
            for name in order:
                flat = name.replace(".", "")
                run(["-o", source_file(name)[:-5] + ".olean", source_file(name)], name + ".log")
                audit = "import " + name + "\n" + "\n".join(
                    "#print axioms " + item["name"] for item in registry[name]) + "\n"
                (work / (flat + "AxiomAudit.lean")).write_text(audit)
                (retained / (flat + "AxiomAudit.lean")).write_text(audit)
                output = run([flat + "AxiomAudit.lean"], flat + "AxiomAudit.log")
                dependencies = {}
                for item in registry[name]:
                    full = item["name"]
                    if "'" + full + "' does not depend on any axioms" in output:
                        axioms = []
                    else:
                        match = re.search(r"'" + re.escape(full) + r"' depends on axioms:\s*\[([^]]*)\]", output)
                        assert match, (full, output)
                        axioms = [a.strip() for a in match[1].split(",") if a.strip()]
                    assert set(axioms) <= {"propext", "Quot.sound", "Classical.choice"}, (full, axioms)
                    assert name not in SPINE + PURE or not axioms, (full, axioms)
                    dependencies[full] = axioms
                if name in SPINE:
                    signatures = "import " + name + "\n" + "\n".join(
                        "#check @" + item["name"] for item in registry[name] if item["kind"] == "theorem") + "\n"
                    (work / (flat + "Signatures.lean")).write_text(signatures)
                    (retained / (flat + "Signatures.lean")).write_text(signatures)
                    run([flat + "Signatures.lean"], flat + "Signatures.log")
                records.append({
                    "module": name, "spine": name in SPINE,
                    "layer": ("foundation" if name in FOUNDATION else "core" if name in CORE
                              else "bridge" if name in BRIDGE else "inherited"),
                    "theorems": sum(x["kind"] == "theorem" for x in registry[name]),
                    "declarations": registry[name], "axiom_dependencies": dependencies,
                    "kernel_checked": True,
                })
            # Constants Lean generates are not source declarations; audit them as well.
            environment = ENVIRONMENT_AUDIT.format(
                imports="\n".join("import " + name for name in core_closure),
                modules=", ".join("`" + name for name in core_closure))
            (work / "EnvironmentAudit.lean").write_text(environment)
            (retained / "EnvironmentAudit.lean").write_text(environment)
            output = run(["EnvironmentAudit.lean"], "EnvironmentAudit.log")
            constants = {m: int(n) for m, n in re.findall(r"CONSTANTS (\S+) (\d+)", output)}
            assert sorted(constants) == sorted(core_closure), (constants, core_closure)
            generated = {n: [a.strip() for a in axs.split(",") if a.strip()]
                         for n, axs in re.findall(r"AXIOMS (\S+) \[([^]]*)\]", output)}
            sources_named = {item["name"] for name in core_closure for item in registry[name]}
            for full, axioms in generated.items():
                assert full.endswith(".injEq") and axioms == ["propext"], (full, axioms)
                assert full not in sources_named, full
            receipt["core_closure_constants"] = constants
            receipt["generated_axiom_dependencies"] = generated
            (work / "Controls.lean").write_text(CONTROLS)
            (retained / "Controls.lean").write_text(CONTROLS)
            run(["Controls.lean"], "Controls.log")
            # The core needs nothing beyond Lean's prelude.
            bare = work / "prelude-only"
            bare.mkdir()
            for name in core_closure:
                target = bare / source_file(name)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(re.sub(r"^import Std\n", "", sources[name].decode(), flags=re.M))
                run(["-o", source_file(name)[:-5] + ".olean", source_file(name)], name + ".PreludeOnly.log", bare)
            receipt["core_compiles_from_prelude"] = True
            receipt["checked_application_examples"] = [
                {"claim": "the full premise set has a model", "kernel_checked": True, "counted_as_new_theorem": False},
                {"claim": "universal_reason has a nonvacuous instance on a one-step frame", "kernel_checked": True, "counted_as_new_theorem": False},
                {"claim": "a frame's continuation space has a reached configuration realizing a living claim", "kernel_checked": True, "counted_as_new_theorem": False},
                {"claim": "a run with a common condition is connected under the relational reading", "kernel_checked": True, "counted_as_new_theorem": False},
                {"claim": "the stepwise reading is connected by a common condition and credits a living event", "kernel_checked": True, "counted_as_new_theorem": False},
            ]
        receipt["source_unchanged_during_check"] = all(
            paths[name].read_bytes() == data for name, data in sources.items())
        assert receipt["source_unchanged_during_check"], "Source changed; only snapshot checked"
        assert all((retained / name).read_bytes() == data for name, data in helpers.items())
        receipt["modules"] = records
        receipt["artifact_sha256"] = {
            p.name: audit_support.digest(p.read_bytes()) for p in sorted(retained.iterdir()) if p.is_file()
        }
        receipt["status"] = "passed"
    except Exception as error:
        receipt["status"] = "failed"
        receipt["error"] = str(error)
        raise
    finally:
        serialized = json.dumps(receipt, indent=2, ensure_ascii=False) + "\n"
        (retained / "verification.json").write_text(serialized)
        RECEIPT.write_text(serialized)
    spine = [r for r in records if r["spine"]]
    print(json.dumps({
        "status": receipt["status"],
        "core_closure": core_closure,
        "core_axioms": sorted({a for r in records if r["layer"] in ("foundation", "core")
                               for aa in r["axiom_dependencies"].values() for a in aa}),
        "spine_theorems": {r["module"]: r["theorems"] for r in spine},
        "spine_declaration_audits": sum(len(r["declarations"]) for r in spine),
        "generated_with_axioms": len(receipt.get("generated_axiom_dependencies", {})),
        "inherited_modules": len(records) - len(spine),
        "inherited_axioms": sorted({a for r in records if not r["spine"]
                                    for aa in r["axiom_dependencies"].values() for a in aa}),
        "receipt": str(RECEIPT),
    }))


if __name__ == "__main__":
    main()
