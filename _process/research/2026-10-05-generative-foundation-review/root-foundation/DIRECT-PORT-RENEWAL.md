# Direct regeneration of a formation condition

7 October 2026. AI-authored continuation of the [exact port replenishment and mapping boundary](PORT-RENEWAL-LAW-CLOSURE.md), following [Ren's positive 生生 direction](../../../../sources/15-codex-theory-conversations/2026-10-07-shengsheng-ethical-direction.md). The question here is whether actual activity restores a condition of later formation in the same process. This supplies a concrete implementation relation for that direction. It does not establish ethical warrant, increasing diversity, or the formation of another organization.

**Result:** an actual productive inquiry followed by actual recovery creates one backed spare pair, while replenishing held support precisely when the arriving packet covers all eight supported stages. A genuine initial contact formation followed by that round restores the pair it consumed, at nine stages total. This is stronger than the earlier seven-stage held-only replenishment result: the restored coordinate is material required by the existing formation law. Source still declines by twenty units per round.

The proofs are in [PortDirectRenewal.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/PortDirectRenewal.lean). They retain the existing native executor, recovery, contact formation and full intermediate history. There is no new event law, source provider, or contact-aging convention.

## What the productive round actually regenerates

Use the already studied intact-reset inquiry `reset, probe, a, a, probe`. This schedule is one available inquiry; its intact-reset condition is not a claim that inquiry generally requires a reset. The independently checked adaptive [phase inquiry](PHASE-RECOVERED-CONTACT.md) remains a different schedule.

Let `d` be the existing native draw, in held ticks. A completed inquiry with an open contact transfers ten source units through one output and records ten failed units through the other. `inquiry_material` derives the latter relationship, and also proves that a blocked inquiry records twenty failed units and no transfer. The failed units are not inferred from a desired recovery outcome: they are the actual changes in the two probe records.

`inquiry_recovers_pair` then constructs the inquiry and a succeeding recovery event under these explicit hypotheses:

- the contact is open and the reset intact;
- the native capacity guard holds;
- source is at least twenty units;
- held support is at least `8d`, a sufficient transient bound;
- the existing recovery record is consistent: `10 × recovered ≤ dissipated`.

Neither an initial spare pair nor previously unclaimed failed conversion is required. The inquiry contributes ten newly recorded failed units, so the existing recovery rule can increment `recovered` and `spare` once without counting any recorded failure twice. If the old record was saturated, the new record is again saturated after this recovery.

The theorem retains a `FormationClosure.process` trace containing all five native commands and the recovery event. Its `Regenerates` conclusion gives the exact endpoint changes:

| Coordinate | Exact relationship |
|---|---|
| Source | `source' + 20 = source` |
| Held support | `held' + 8d = held + 655360` |
| Spare pairs | `spare' = spare + 1` |
| Recovered pairs | `recovered' = recovered + 1` |
| Recorded failed units | `dissipated' = dissipated + 10` |
| Transferred units | `transferred' = transferred + 10` |
| Accumulated arrivals | `arrived' = arrived + 655360` |
| Accumulated enactment | `enacted' = enacted + 8d` |

The draw, peak, capacity and intact reset remain unchanged; the contact remains open. Recovery supplies no held arrival. Its eighth draw is paid from the actually reached reserve. The conversion scale remains 65,536 held ticks per transferred source unit, so the ten-unit successful packet yields 655,360 ticks. Failed-conversion units, held ticks and spare-pair counts are separate coordinates related by the existing conversion and recovery rules, not interchangeable numerical units.

`regeneration_replenishes_iff` derives the exact local criterion:

\[
H'\ge H\quad\Longleftrightarrow\quad8d\le655360.
\]

No averaging or future arrival pays an earlier unfunded stage. The construction uses the sufficient initial reserve bound to discharge each actual executor guard. That bound is not claimed necessary.

## Restoring the pair consumed in actual formation

`formation_regenerates_its_pair` starts with a **blocked** contact, at least one spare pair, a backed recovery record, intact reset, native capacity, twenty source units and at least `9d` held. It constructs:

`formation → reset → probe → a → a → probe → recovery`.

Formation opens the blocked contact and consumes a pair. The inquiry operates through that reached open contact. Recovery replaces the pair from its new failed-conversion record. At the endpoint:

\[
\text{spare}'=\text{spare},\qquad
S'+20=S,\qquad
H'+9d=H+655360.
\]

The contact has actually changed from blocked to open, the recovered-pair count has increased by one, and the backing condition is retained. Held support is replenished if and only if `9d ≤ 655360`.

This restores a material condition of formation; it does not recreate the entire preceding state. Source was consumed, activity was enacted, the failure record increased, and the contact changed. The result is therefore not a loop returning all resources to their initial values.

Nor is repeatedly opening this same contact a demonstration of further organization. The native contact persists. Later formation on an already open contact consumes a pair and a draw without changing the contact, as the earlier `redundant_formation_draws` theorem proves. Newly available spares are a restored material prerequisite, not proof of a second contact, a maintenance requirement, or an expanding repertoire.

## Actual iteration, acquisition and the failure boundary

`finite_material_regeneration` composes productive inquiry-and-recovery rounds at their actual reached states. Under the productive conditions above, `8d ≤ 655360`, and initial source at least `20n`, it constructs `n` rounds with:

\[
S_n+20n=S_0,\quad
\text{spare}_n=\text{spare}_0+n,\quad
\text{recovered}_n=\text{recovered}_0+n,
\]

\[
\text{dissipated}_n=\text{dissipated}_0+10n,\qquad
H_n+n(8d)=H_0+n(655360),\qquad H_n\ge H_0.
\]

The `Ready` predicate retained at each endpoint includes actual capacity, sufficient held support, open contact, intact reset and material backing. It deliberately excludes the source guard: each next round must discharge that guard from its remaining source. This establishes finite repeatability of material regeneration, not indefinite renewal from one finite start. The earlier arbitrary-history source and strict-potential obstructions still apply.

The checked `acquired_condition_regeneration` witness extends the existing `acquiredHistory` by one actual recovery. It begins blocked, with forty source units, 400,000 held ticks, no spare pair, no recovered pair and no failed-conversion record. The first inquiry completes with both transfers blocked; recovery forms its spare; the contact is formed; the second inquiry transfers a packet; the new recovery leaves an additional spare. The endpoint has an open contact, one spare pair, two recovered pairs, thirty recorded failed units, ten transferred units, zero source, 278,562 enacted ticks and 776,798 held ticks. Thus neither the initial pair nor the final additional pair is provided silently. The choice of this history remains a supplied schedule; the earlier acquired-inquiry work supplies the relevant decision correspondence, not a new decision theorem here.

The successful cycle also has a checked failure boundary. `held_only_adequacy_does_not_cover_recovery` supplies a supported open port with draw 90,000. Seven draws cost 630,000, less than the arrival of 655,360; eight draws cost 720,000. The actual inquiry-and-recovery history creates a spare but lowers held support from 1,000,000 to 935,360. Merely importing the old seven-stage adequacy condition would incorrectly classify that material-regeneration round as replenishing. Higher overhead, inadequate initial funding and source exhaustion are not removed by an open contact or the existence of recoverable material.

## What relation to renewal has been established

This is a direct theorem about regeneration of a formation condition. It does not identify persistent contact with an aging `ChannelLaw` token. None of the old channel package's endless-renewal sufficiency theorems is transferred: their token lifetime, surviving support and realizability requirements are not established here. The earlier contact-only mapping obstructions are preserved.

The exact interface now available is stronger and more appropriate to this port: an actual history produces a new, consistently backed formation input while meeting its held costs, and finite repetition retains those enabling conditions subject to an explicitly decreasing source. The ten-failed-unit recovery rule, contact-opening rule, native draw/capacity law, conversion scale and inquiry schedule are still supplied model mechanisms or credited previous results. The new theorem derives their consequences together; it does not derive those mechanisms from no assumptions.

The accompanying, separately authored [GenerativePossibility.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/GenerativePossibility.lean) clarifies the relevant meaning of possibility. For a fixed process and fixed target, anything reachable after an actual prefix was already reachable through that prefix. Nevertheless actual resource-guarded formation changes whether an open contact is reachable using native activity alone. `NativeReachOpen` permits an empty trace, so it does not assert funded delivery. Possibility relative to the complete law, presently formed organization, and presently funded execution must not be conflated. Creating an actual condition within the process does not require importing it from outside the represented whole.

For Ren's criterion this gives a concrete instance of activity changing the conditions of further formation. It neither substitutes sustained operation for more 生 nor shows that one additional pair produces diversity, greater organizational complexity or ethical quality. The next substantive native extension would have to identify an actual additional formation that uses the regenerated material, with its organization, consequences and support costs. The present process has only the one persistent contact, so that stronger claim is unavailable in this model. Indefinite source regeneration additionally requires changing the source law; an improved description alone cannot supply it.

## Verification and review

The [independent mathematical and semantic review](DIRECT-PORT-RENEWAL-REVIEW.md) checked the executor, recovery backing, actual funding, finite iteration, acquisition witness and scope. It found no discrepancy; its wording clarification distinguishes blocked transfers from execution stopping.

The [checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/check_port_direct_renewal.py) compiles both new modules with Lean 4.29.1 in a fresh temporary directory. It snapshots their full nonstandard import closure and checker before compilation, records compiler identity, source hashes and raw output, checks that sources stayed unchanged, and audits every explicit new declaration. It rejects proof holes, custom axioms, `native_decide`, missing audits and unlisted logical dependencies. The allowed standard dependencies are `propext` and `Quot.sound`; neither choice nor no-assumptions completion is assumed by that allowance.

Fresh verification passed **27 modules and 647 audits**, recorded in the [source-bound receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/port-direct-renewal-verification.json). The fourteen new direct-renewal declarations have nine empty reports and five using only `propext` and `Quot.sound`. All seven declarations in the accompanying possibility module have empty reports. Thus the twenty-one new audits comprise sixteen empty reports and five with the named standard dependencies. The exact material and executed positive/counterexample histories have empty reports; the arithmetic construction and iteration use the named dependencies. No empirical evidence or independent ethical warrant is claimed. The counterexample above and the distinction between regenerated material and further organization are the substantive scope checks for this contribution.
