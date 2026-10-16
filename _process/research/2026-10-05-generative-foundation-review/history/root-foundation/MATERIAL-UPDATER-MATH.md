# Typed material constraints on updater formation

6 October 2026. AI-assisted mathematical companion to [material updater composition](../../../../theories/becoming/history/MATERIAL-UPDATER-COMPOSITION.md). The named transition is **actual formation of constituents → construction and replacement of response selectors and their updating modules using the same constituents and support history**. This extends a declared local model; it does not derive physical wiring, sensory transduction or a meta-selection mechanism from the root alone.

## 1. Which process is being refined

The operational predecessor is `UpdaterFormation`, including its paid `formModule` events. Its state contains the full selector state, updater kind, updater lease, whether a selector has previously been assembled, source remainder and coarse material total. A module formation spends two fuel units in the primary parameters even though it has no corresponding selector event. Erasing it would not preserve the paid state sequence. The present refinement keeps every updater event and its complete updater-state successor.

The [original updater interface](../../../../theories/becoming/history/UPDATER-FORMATION.md) uses reusable material slots. Here each new construction additionally binds previously free typed components, with no reclamation. Thus a trace projects to the coarse updater law, but an arbitrary coarse trace need not lift. The two material laws are not identified or assigned equal probabilities.

Let an operational state be

\[
r=(x,A,H,\rho,i,B_A,B_H,P),
\]

where \(x\) is the complete updater state, \(A,H\) are free stocks, \(\rho\) is the resident, \(i\) the site condition, \(B_A,B_H\) incorporated/spent stocks, and \(P\) retained precursor. The incorporated counters include the adapter, live structures and spent structures; they do not label which bound components are currently functional.

Declare the event cost vector

\[
c(\operatorname{formModule}(u))=(1,1),\quad
c(\operatorname{formSelector}(\mathrm{false}))=(2,0),\quad
c(\operatorname{formSelector}(\mathrm{true}))=(0,2),
\]

with zero component cost for trial, reversal and packet expiry. Different updater kinds use the same component quantities; the correspondence between the event's Boolean configuration and its functional arrangement is a supplied recipe. Counts alone do not explain that arrangement.

An event is enabled exactly when the old updater guard is true and both component costs fit the free stocks. Its successor has the old updater successor, subtracts the two component costs from free inventories and adds them to the bound inventories. It retains resident, site and precursor. No old operational fuel, packet, mapping, lease, retained information or regime field is replaced by a fresh initial value.

## 2. Exact operational lift criterion

For a finite word \(w\), write

\[
D_A(w)=U(w)+2S_A(w),\qquad D_H(w)=U(w)+2S_H(w),
\]

where \(U\) counts both updater kinds and \(S_A,S_H\) count the two selector configurations. For an inherited material state \(r\) and a proposed coarse endpoint \(y\),

\[
\begin{aligned}
&\exists t:\ \operatorname{TypedTrace}(r,w,t)\land t.x=y\\
&\quad\Longleftrightarrow\quad
\operatorname{UpdaterTrace}(r.x,w,y)
\land D_A(w)\le r.A\land D_H(w)\le r.H.
\end{aligned}
\]

The necessity direction projects each event and sums the exact inventory decrements. For sufficiency, induct on the old updater trace. The full-word inequalities imply that the first cost fits and that the tail costs fit the remaining stock. Since the operational phase contains no replenishment, other material sink or change of type, there are no additional material prefix conditions. The old updater feasibility premise still retains **all** actual fuel prepayments, source constraints, leases, consequence returns and permitted-reconstruction conditions at every prefix. Replacing it with a final energy inequality would be invalid.

The lifted endpoint, when it exists, has free stocks \(A-D_A(w),H-D_H(w)\) and bound stocks \(B_A+D_A(w),B_H+D_H(w)\). This also gives the component invariants

\[
A+B_A=\text{constant},\qquad H+B_H=\text{constant}.
\]

The material account adds the resident occupancy and retained precursor:

\[
A+H+B_A+B_H+\operatorname{occupied}(\rho)+P=M.
\]

Consequently \(U(w)\le\min(A_0,H_0)\). This limits **new updater constructions** under this law. It is not a bound on persistence or learning performed by an already formed structure, and zero-cost reversal events can still form cycles. Repeated reconstruction without bound would require production or reclamation laws and their support accounts.

## 3. Actual preparation and paid adapter

Preparation uses the unchanged `FormedSelection` law. A typed handoff requires its validity bound, an intact site, a captured local unit, adapter prepayment and at least one free A and free H. This is stronger than the coarse updater bridge, which merely requires positive total A and H counts, including a resident. Reusing the resident both in the retained compartment and as a free adapter part would double-count it.

The adapter binds one free A and H, retains resident and site, and sets precursor to \(M-\operatorname{population}(s)\). Its complete coarse state is **exactly** `UpdaterFormation.entrance p M s z`. For packet size six this state contains

\[
F'=F-\text{adapter}+\operatorname{bit}(\text{localFuel}),\quad
Q'=\lfloor\text{source}/6\rfloor,\quad
R'=\text{source}\bmod6.
\]

The captured local unit is converted to common fuel and is not also retained in a side store. The source remainder is retained. Thus coarse energy after entrance plus adapter expenditure equals actual formation energy before entrance. Quotient/remainder arithmetic does not derive the supplied physical access protocol or a packetizer.

The old two-material preparation has no free A: its sole A is the active resident. It therefore passes its original coarse bridge while failing this typed bridge. This is a new implementation obligation, not a refutation of the old law. Formation chemistry is suspended after entrance; no concurrent kinetic equivalence or continued component production is claimed.

## 4. The full typed witness

Declare at the beginning \(M=13\), common fuel 29, source 97, no A or H, no resident and a damaged site. The actual formation word is

\[
\operatorname{formH}^{5};\operatorname{formA}^{8};
\operatorname{associateA};\operatorname{repair};\operatorname{capture}.
\]

It contains sixteen events and spends fifteen fuel units. All formation precedes repair, as the original guards require. Its endpoint is seven free A, five free H, one active resident, common fuel 14, source 96 and one local unit. The adapter spends one fuel unit while converting the local unit, leaving common fuel 14, sixteen packets, free stocks six A and four H, and one bound A and H.

The operational word is the existing `UpdaterFormation.updaterWitness`. Its complete coarse state uses material total 13. The predecessor's literal `primaryEntrance` and `finalWitness` use material total 2, so they must be retagged at that inert field; equality to those complete literal states without retagging would be false.

| Completed stage | Common fuel | Packets | Free A | Free H |
|---|---:|---:|---:|---:|
| Paid adapter | 14 | 16 | 6 | 4 |
| Form initial updater | 12 | 16 | 5 | 3 |
| Form initial A selector | 11 | 16 | 3 | 3 |
| Four productive trials | 19 | 12 | 3 | 3 |
| Reverse and fail twice | 15 | 10 | 3 | 3 |
| Old updater reconstructs A selector | 14 | 10 | 1 | 3 |
| Two more failed trials | 10 | 8 | 1 | 3 |
| Form changed updater | 8 | 8 | 0 | 2 |
| Construct H selector | 7 | 8 | 0 | 0 |
| Productive trial | 9 | 7 | 0 | 0 |

There are two updater formations, two A-selector constructions and one H-selector construction, with demand \((6,4)\). The final incorporated counts are seven A and five H, plus the one resident. All thirteen material units remain accounted for. Source, repair and formation are actual events in the same staged history, not initial values silently assigned at the learning boundary.

Support obeys

\[
126=15+1+59+51.
\]

The operational loss of 59 consists of four units for updater assembly, three for selector assembly, twenty for five successful trials including both renewal charges, and thirty-two for four failed trials including lost packets. The remaining 51 is nine common fuel plus seven packets of six. This is an existential event word. Neither the choice to replace the updater nor the particular replacement is generated by a derived meta-policy here.

## 5. Causal competition and separating histories

Both levels use the same free inventories, but their assembly guards are not simultaneously enabled: updater formation requires its lease to be zero, whereas selector construction requires a live updater. Competition is therefore across the actual sequence, not a simultaneous choice between two enabled events.

The independent checker validates two alternative actual preparation histories with the same 14 fuel and 16 packets at entrance:

- Start with \(M=12,F=28,\text{source}=97\), form seven A and five H, associate A, repair and capture. After the adapter there are five A and four H. The original operational word reaches the second updater formation with fuel 10, eight packets, free A zero and H three. The coarse formation guard is true, but the missing A blocks it. Earlier selector construction has consumed the A required for this later updater.
- Start with the same original support and capacity, form eight A and four H instead. After the adapter there are six A and three H. The changed updater can form, but the following H-selector construction has only one H left. Fuel eight and eight packets remain, and the coarse reconstruction guard is true. The earlier updater constructions have consumed H needed by the selector.

As an inventory comparison, the main word's updater demands \((2,2)\) and selector demands \((4,2)\) each fit the first example's \((5,4)\) stock, while their joint demand \((6,4)\) does not. This does **not** claim that either construction subword is independently executable without the intervening trials and lease changes. The full feasible prefixes above provide the causal witnesses.

There is also a separation from the fully successful main witness. Continue with reversal, two failed trials and an A-selector reconstruction. The coarse process admits all four events. The typed process admits the first three and reaches fuel five and five packets, but cannot assemble from its exhausted free A stock. Coarse affordability therefore cannot imply typed realizability even after a successful earlier updater change.

Conversely, one fuel unit with the original free stocks cannot pay a two-unit updater assembly. Component abundance does not imply payment. A state with the same funded coarse state but zero free A cannot form an updater. These isolate the component and support conditions instead of making both fail at once.

## 6. Independent finite verification and formal scope

The independent [checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/updater/check_model.py) implements the declared preparation events, complete operational event table and typed inventory layer without importing Lean conclusions or the other executable model. Its [result](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/updater/model-verification.json) records:

- 1,248 enabled and 15,600 disabled handoff cases, including resident types, local-store flags, source remainders and retained precursor;
- 299,584 lift-criterion cases over every operational word of length at most four, four coarse starts and sixteen inventory pairs, of which 4,194 are admitted;
- 48 stock pairs for the complete fifteen-event revision word, with exactly four admitted, plus 768 prefix/stock cases;
- a complete operational reachability graph from fuel eight, three packets and free stocks three A and three H: 200 states and 522 labelled edges, exhausted to a fixed point including reversal cycles, with no depth cutoff;
- seven boundary checks covering the coarse two-material bridge, separate fuel and part deficits, both actual preparation competition histories, the post-success coarse-only extension, and the updater kind's different reconstruction guard.

The graph is deliberately a smaller funded initial state; its 200-state result is not reported as the full graph from the main sixteen-packet witness. The full main witness and its alternatives are separately replayed with every intermediate account checked. Short-word finite checks do not replace the quantified Lean lift theorem. The [formal package](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/construction/updater/README.md) reports theorem verification separately; source hashes identify the code reviewed and replayed.

The result advances compatible construction, not the origin of the event laws. A formed controller acquiring a calibrated prediction and causally using it in paid action remains the next shared connection. Reusable slots, reclamation, concurrent chemistry, physical wiring, complete sensing, memory formation and choice of replacement remain explicit implementation or explanatory premises. This model supplies no empirical advantage, universal favorable direction or ethical conclusion.
