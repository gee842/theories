# From formed parts to a revisable response module

6 October 2026. AI-assisted mathematical companion for the continuing generative-foundation research. This study advances the named connection **formed response parts → paid construction of a response-selection module → consequence-dependent maintenance and replacement**, under an explicit staged law. It joins the preceding [formed-variant process](../../../../experiments/shared-renewal-capability/regulation/retention/formation/formal/FormedSelection.lean) to [costed selector revision](../../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/formal/SelectorRevision.lean).

The new law supplies the component recipes and the relation between successful use and maintenance. Those mechanisms are not inferred from the resource ledger. The result is a finite construction and an accounting-preserving composition; the origin of the whole sensing and updating architecture remains a further derivation.

## 1. The gap being closed

The earlier formation process starts with neither response type present. Its events form A and H, associate a resident, repair an access site, capture support and make additional copies. The selector process instead begins with a supplied mapping apparatus that can be assembled, used, maintained or replaced. Matching the names of these two studies does not join their actual states.

There are two immediate obstacles. First, the original formation-to-copy witness has spent its entire support stock at its terminal state. It cannot fund even the next positive-cost assembly. Second, the formation process counts each remaining source unit as one unit of support, while the selector example counts each packet as four. Mapping a source count directly to a packet count would silently quadruple the resource.

The present construction addresses both obstacles. It uses a funded preparation history of the existing formation law, carries its actual successor into the operational phase, represents the remaining source in the new denomination with a retained remainder, and consumes actual A or H parts for each new response module.

## 2. One staged state space

The composed process has a preparation phase and an operational phase.

In preparation, its material state is exactly a `FormedSelection.State`; a regime bit is retained separately and is unchanged by preparation. Every preparation event follows the original `FormedSelection.Step`. The material bound is a fixed natural number $M$. No A or H part is supplied merely by entering the composed model.

An operational state retains:

- the selector state: fuel, source packets, current mapping orientation, remaining lease and hidden regime;
- the remaining free A and H, resident, access-site condition and local support;
- the source remainder and the number of A and H parts already incorporated or spent on modules.

The incorporated counters are cumulative. Parts belonging to an expired module remain counted; reconstruction consumes further free parts. The counters are not a claim that every former module remains active. The current orientation and lease describe the operative mapping.

Only preparation events run before handoff, and only operational events run after it. This is a declared staged law. It does not preserve all former preparation reactions as concurrently available reactions, nor show that a real chemical system would freeze those reactions at the boundary. In particular, there is no claim of an exact kinetic quotient from the formation chemistry to the selector kinetics.

## 3. Exact resources at handoff

Let the prepared state have common fuel $f$, source $s$, and local-fuel indicator $\ell\in\{0,1\}$. Let the selector packet size be $p>0$. Handoff requires an intact access site, retains $f$ and $\ell$, and represents the source by

\[
s = p q + r,\qquad 0\le r<p.
\]

Here $q$ is the packet count and $r$ is retained source that does not form a full packet. This is a change of accounting denomination. It neither credits additional fuel nor claims that packet fabrication is a cost-free physical operation. The operational law is separately supplied with access to a packet of that size.

The closed support quantity is

\[
E_{\rm pre}=f+s+\ell,
\qquad
E_{\rm run}=f+p q+r+\ell.
\]

They are equal at handoff. The dormant selector begins with lease zero; its initial orientation is bookkeeping, and no trial is enabled before an actual assembly. The regime is inherited unchanged. All free and resident parts are retained, while both incorporated counters initially equal zero.

If an episode later uses a packet unsuccessfully, that packet is charged as waste rather than disappearing from the ledger. A successful use pays the trial and maintenance costs and transfers the remaining packet support into fuel. Source remainders and the retained local store are included in total support even where this operational repertoire cannot spend them. Equality of total support does not imply immediate spendability through every route.

## 4. Parts needed to construct a mapping

The supplied recipe for orientation `false` requires two free A parts. Orientation `true` requires two free H parts. Assembly requires an expired or absent module and enough common fuel to pay the selector assembly cost, in addition to the appropriate parts. It reduces the selected free-part count by two and increases its incorporated counter by two.

If $a,h$ denote free parts, $o$ the resident occupancy, and $b_A,b_H$ the incorporated counters, the operational material count is

\[
N=a+h+o+b_A+b_H.
\]

Every operational event preserves $N$. In particular, reconstruction cannot turn previously spent parts back into free precursor. With precursor $M-N$, a valid state satisfies

\[
N+(M-N)=M.
\]

The module changes the existing signal-to-response rule $b\mapsto b\mathbin{\rm xor}m$. Which orientation succeeds depends on the hidden regime through the supplied physical consequences of the response. Neither assembly eligibility nor its choice of component recipe reads that regime. Both useful and unhelpful modules are constructible when the relevant parts and fuel are present.

Deleting the retained component fields projects each operational event to an event of the existing selector law. This is a forward simulation. Trial, reversal and source expiry have the old operational transition exactly. Lifting an old selector assembly back to this process additionally requires the selected part type in sufficient quantity. Consequently, the complete sets of feasible histories are not unconditionally equivalent: the component law introduces real assembly obstructions.

The stronger trace statement identifies those obstructions exactly. For any old selector history containing $n_A$ false-orientation assemblies and $n_H$ true-orientation assemblies, a component-level lift from inherited free inventories $a_0,h_0$ exists if and only if the old history is feasible and

\[
2n_A\le a_0,\qquad 2n_H\le h_0.
\]

At its actual successor the remaining free inventories are $a_0-2n_A$ and $h_0-2n_H$, and the corresponding incorporated counters have grown by those same amounts. No operation regenerates free parts in this repertoire, so satisfying the cumulative budgets also satisfies every earlier prefix's part demand. This is a quantified Lean result, `material_trace_lift_iff`. It makes the earlier selector's effective assembly permission depend on an independently constructed inventory, and bounds the number of replacements even when energy remains available.

## 5. One funded preparation, use and reversal history

The main fixture starts with material capacity five, common fuel twelve, source eighteen, no A or H, an empty resident site and a damaged capture site. The hidden regime is `false`.

The preparation word is

\[
[\operatorname{formH},\operatorname{formH},\operatorname{formA},
\operatorname{associateA},\operatorname{repair},
\operatorname{capture},\operatorname{localCopyA},
\operatorname{capture},\operatorname{localCopyA}].
\]

Both H formations precede repair because formation in this law requires a damaged site. The existing resident A restores capture, and two distinct capture events each fund one local A copy. Preparation therefore ends with two free A, two free H, one active resident, an intact site, no local fuel, common fuel seven and source sixteen. Five common-fuel expenditures and two locally funded copies have spent seven of the original thirty support units.

With packet size four, handoff gives four packets and remainder zero. Its selector projection is exactly the original selector example's initial state: fuel seven, four packets, dormant orientation `false`, lease zero and regime `false`.

The operational history is the existing reversal word:

| Event | Fuel after event | Packets | Orientation | Lease | Regime |
|---|---:|---:|---|---:|---|
| Assemble from two A | 6 | 4 | false | 2 | false |
| Matching trial | 7 | 3 | false | 2 | false |
| Reverse regime | 7 | 3 | false | 2 | true |
| Mismatching trial | 5 | 2 | false | 1 | true |
| Mismatching trial | 3 | 1 | false | 0 | true |
| Assemble from two H | 2 | 1 | true | 2 | true |
| Matching trial | 3 | 0 | true | 2 | true |

The first module is maintained after a successful use; its unchanged response mapping loses that maintenance after reversal and exhausts its lease. Replacement consumes a different pair of previously formed parts and one more unit of inherited fuel. The resulting mapping differs on the same signal. The history contains two successful trials, two unsuccessful trials and two assemblies. Its operational cost, including unsuccessful packet loss, is twenty support units; together with the seven-unit preparation cost and three final units this accounts for the original thirty.

The five material units remain one resident plus two incorporated A and two incorporated H. The example supplies neither new fuel nor new matter at reversal or replacement. It exhibits a feasible revision path; it does not assert that a scheduler inevitably chooses that path, or that random reconstruction has a particular probability of doing so.

## 6. Obstructions and the remaining premises

The original exhausted formation witness still fails to continue into paid operation. A larger initial source count alone does not substitute for the common fuel needed before the first assembly and trial. Component availability is another independent constraint: an energetically affordable assembly of an orientation remains impossible without its two required free parts. Total material without the required type is insufficient.

A second checked history first constructs the wrong H module, spends two trials without maintenance, and then constructs the matching A module. It ends with the correct response mapping and two full packets still present, but only one common-fuel unit. Since a trial requires two units paid before capture, this newly correct module cannot be used. The consequences of earlier unsuccessful construction therefore survive later correction. A matching representation, actual parts and a positive total support stock do not jointly guarantee an executable next use when the accessible payment route is blocked.

The successful history does not establish unrestricted renewal. Its initial source is finite, and every trial reduces that source whether useful or unsuccessful. Successful maintenance preserves the current module within this finite history; it does not create unlimited source or matter. The retained remainder and local store likewise do not create an unspecified conversion route.

The new premises are explicit: two-part recipes for the two response mappings; a phase boundary; the operational packet-access law; and the prior selector law's coupling from use consequences to lease maintenance. The earlier formation law still supplies its repair, capture and copying chemistry. These are legitimate local construction assumptions, but they are not consequences of difference, composition or accounting alone.

This round replaces a supplied stock of response-module parts with an actual prior formation history and replaces unrestricted paid assembly with a part-constrained construction. It leaves formation and variation of the transduction, maintenance and reconstruction rules themselves open. That further connection is required before calling the whole learning architecture derived; consequences for other centers remain an additional obligation on the path toward concern.

## 7. Verification scope

The Lean package records its quantified results in the package [README](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/README.md). The separately written [finite checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/check_model.py) passed 6,480 handoff cases and traversed the complete finite operational graph from the named fixture: 194 states and 510 enabled labelled edges, including reversal loops. Every checked event preserves matter, accounts for support and leaves no more than two two-part assemblies possible from the four initial free parts. Additional cases preserve a nonzero source remainder and isolate wrong part type at equal energy and total matter, unfunded assembly despite abundant source, an unhelpful constructible orientation, and a damaged-site handoff obstruction. The [machine-readable record](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/model-verification.json) includes input hashes.

The checker also evaluates the complete named preparation-and-reversal word over 456 initial stock pairs: common fuel zero through eighteen and unit source zero through twenty-three. Within that grid the word is executable exactly when common fuel is at least twelve and source at least eighteen. These are bounded exhaustive checks of a declared synthetic law. They are separate from the quantified Lean theorems and from any empirical identification of real material parts.
