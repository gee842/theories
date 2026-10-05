# Recipient evidence, distinguishable targets and paid correction

6 October 2026. AI-authored mathematical companion to the [recipient-correction protocol](../../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/PROTOCOL.md). The named connection is **another center's actual consequence → paid correction of its action correspondence while preserving the actor's acquired correspondence**. This is a supporting interface for the parallel concern study, not a derivation of concern's valuation.

The independent [Lean interface](../../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/formal/RecipientCorrection.lean) checks 36 declarations. The finite stochastic producer, its actual inherited prefix and its full resource account have separate executable checks. The Lean package imports only `Std`; it neither imports nor changes the concurrently developed coupling or prediction APIs.

## 1. What information must survive

Let the two deterministic target laws be

\[
z=(z_A,z_P)\in\{0,1\}^2,
\]

where an action supports the chosen target exactly when it equals that target's law. The actor and recipient laws may vary independently. Let \(S\) contain **all persistent state accessible to the controller**, let \(e:\{0,1\}^2\to S\) encode its acquired information, and let

\[
\pi:S\times\{A,P\}\to\{0,1\}
\]

issue the action when a target query arrives. There is no fresh target-outcome probe between that query and the required action. Assume exact correctness for every pair and either possible target:

\[
\pi(e(z),t)=z_t.
\]

**Distinguishability theorem.** The encoding \(e\) is injective, and two different law pairs produce different behavior on at least one target query. Consequently the controller has at least four distinguishable accessible states.

Proof: if \(e(z)=e(z')\), querying actor yields \(z_A=z'_A\), and querying recipient yields \(z_P=z'_P\), so \(z=z'\). Conversely, a coordinate on which the laws differ witnesses a behavioral difference. Lean proves injectivity, this behavioral distinction, the existence of four pairwise unequal encoded states, and the impossibility of an exact controller whose complete accessible state is one Boolean.

This is a zero-error, deterministic, zero-new-probe result with independently variable laws. A shared law, fresh informative observation, approximate objective, restricted query set or another persistent accessible variable changes its premises. In particular, the previous physical organization already has a five-valued register, a last-action field and other state. **The theorem is not a capacity impossibility for that organization.** Counting only one chosen variable while covertly using the others would invalidate the lower-bound application.

The opposite-laws fixture alone does not prove a two-bit requirement. If a controller is supplied the invariant \(z_P=1-z_A\), it can store one bit and invert it on recipient queries; Lean checks that counter-regime explicitly. The general theorem instead quantifies over all four law pairs without a supplied label identifying their relationship. The experiment's shared arm fails because its particular record/action rule overwrites one estimate and applies that same estimate to both targets.

## 2. A sufficient representation within existing abstract capacity

The new supplied recipe interprets four values of the existing register as

\[
q=z_A+2z_P\in\{0,1,2,3\}.
\]

The actor bit is the low bit; the recipient bit is the high bit. A target query selects its corresponding bit. Four codes fit the earlier five-code abstract register, leaving one value unused in this phase. The physical retooling is charged by the protocol. A state count and a fuel payment do not derive a real circuit capable of this reinterpretation.

Writing a recipient label replaces only the high bit. Writing an actor label replaces only the low bit. Lean proves that each write sets the queried cell, preserves the other cell, remains in the four-code range, and commutes with a write to the other target. The packed table gives exact actions for any stored law pair.

A single shared orientation estimate instead applies the same stored bit to both targets. If \(z_A\ne z_P\), it cannot be correct for both. Even under stable laws and perfect observations, overwriting it with the recipient law makes the next actor decision wrong; correcting that decision overwrites it with the actor law and makes the next recipient decision wrong. This is interference caused by the supplied representation, not changing reality or corrupted evidence.

The context labels must maintain distinct identities. A consistent bijective swap of actor and recipient labels, accompanied by the corresponding swap of table cells, preserves all commands and writes. Lean checks this relabeling identity. Reporting both physical targets as actor instead routes recipient evidence into the actor cell; with opposite laws that write damages actor behavior. The pertinent failure is losing distinction, not the spelling of the labels.

## 3. Which consequence supplies the correction

For actual action \(a\), target law \(z\) and source availability \(v\), define the target receipt

\[
c(a,z,v)=[a=z]\land v.
\]

Under the calibrated, noiseless complementary law \(v=1\), the action-tagged decoder

\[
D(a,c)=\begin{cases}a,&c=1,\\1-a,&c=0\end{cases}
\]

returns exactly \(z\). Lean proves this for every action and binary law. Applying that actual recipient label to its indexed cell repairs the recipient command while preserving the actor command.

Recipient capture credits the recipient's separate reserve. The actor receives zero whether the recipient succeeds or fails. Holding the actual action fixed, those two possibilities therefore have the same private credit. Lean gives the explicit alias and proves that no decoder of action plus private credit can recover every recipient law.

There is a sharper trap: the decoder applied to a fabricated zero receipt is correct **exactly when the recipient action fails**. Thus a first failed recipient attempt followed by apparently correct revision does not identify which evidence channel caused that revision. After a successful attempt, the same zero-private-credit proxy teaches the opposite of the correct law. This equivalence is checked in Lean and motivates the protocol's actual-channel provenance requirement for its strict witness; the weaker behavioral correction remains a separate observation.

Source outages also break identification. Action zero with law one and an available source produces no receipt; action zero with law zero and an unavailable source produces the same receipt. Their useful orientations differ. The decoder theorem must not be exported to that noisy fixture without a new identification argument.

## 4. Observation and writing are paid operations

The formal observation interface begins with actor reserve \(F\) **after preceding routing, retention, target sensing and work charges**. Recording the actual action-tagged recipient outcome costs \(o\). A subsequent register write costs \(w\). Recipient capture provides no fuel for either payment.

**Local payment theorem.** A completed observation-and-write pair is available exactly when

\[
F\ge o+w.
\]

When completed, its remaining reserve is \(F-o-w\). Under the noiseless law its recipient cell becomes the actual law and its actor cell is unchanged. These claims hold for every initial code, action and nonnegative price. If observation is affordable but writing is not, observation is still charged: the intermediate reserve is \(F-o\), and no completed write occurs.

The Lean `paidFeedback` function returns an optional **completed pair**. Its absent result does not mean an attempted observation was free; the separate `failed_write_retains_observation_charge` theorem exposes the paid intermediate state. This finite interface does not model the entire runtime abort state, rent destruction, missing-channel branch, setup or exposure clock. The full producer retains those stages and expenditures.

## 5. The four-phase correction route and its liquidity boundary

The protocol installs its target interface and indexed recoding for a total of four actor units. Both cells initially copy the actual acquired actor bit, without receiving the recipient's law. Consider a correctly calibrated admitted circuit with opposite target laws, no outages, actual recipient evidence and primary prices. Its four physical opportunities are recipient, actor, recipient, actor; the controller receives the target only through the paid identity input.

The first recipient action fails. Its paid actual receipt changes only the recipient cell. The actor action then succeeds using its preserved cell; the second recipient action succeeds using its corrected cell; the final actor action succeeds. The finite Lean witness checks the corresponding information path for actor law zero, recipient law one and initial code zero: the first recipient write produces code two, which then commands actor zero and recipient one. The complete inherited probabilistic history and its paid phases are executable claims, not that finite Lean witness.

Each completed exposure costs retention1 + target sensing1 + work3 + acquisition1 + writing1 = 7. Each successful actor exposure captures10 into the actor reserve, while successful recipient work captures10 into a separate recipient reserve. Let \(F\) be the actor reserve **after setup**. The actor balances after the four completed phases are

\[
F-7,\quad F-4,\quad F-11,\quad F-8.
\]

The final actor capture requires its retention, target identification and work to be prepaid. Its pre-return price is five. Therefore this specific complete route is possible exactly when

\[
F-11\ge5\quad\Longleftrightarrow\quad F\ge16.
\]

Earlier phases require at most this reserve. With setup included, the inherited reserve boundary is20. At19, the final actor phase can pay retention and target sensing but cannot pay work; its future packet cannot fund the missing work. This is a hand-derived protocol bound, separately checked by the executable boundary fixture, not a full-path Lean theorem.

At the boundary20 the suffix ends with actor8, recipient10, expenditures32 and inaccessible source10. With the original four packets of ten, the suffix account is

\[
20+40=8+10+32+10.
\]

No receipt from recipient welfare enters the actor account. The original preparation plus eight-exposure predecessor is carried by the producer into this suffix without resetting its reserve or excluding failures.

## 6. What this contributes, and what remains supplied

The result explains a precise limitation of transferring an acquired predictor to another center: if target laws can differ, reliable correction needs both actual target evidence and enough accessible distinction to preserve their separate correspondences. An existing abstract register can suffice, but the change in its operational interpretation must be physically supplied and paid. Learning another center's consequence need not overwrite the actor's own learned dependency.

This is not a private-payoff selection theorem for recipient evidence. In the primary indexed comparison, removing recipient outcome access can leave actor actions, charges and receipts identical while recipient support differs. Private retention alone therefore need not favor the more informative recipient channel. Moral standing, valence, selection of that channel, the origin of indexed circuitry, natural target identity and sustained robustness remain separate obligations.

The four-exposure stabilization recipe, calibrated identity input, complementary binary plant, supplied sensor/decoder, recoding operation and fixed policies are local inputs. Earlier component wear laws are explicitly suspended in this new phase; no unchanged kinetic refinement is claimed. The conventional indexed table is an exact comparator rather than a historical novelty claim. A cheaper available recipe or a different information channel can change the comparison.

## Verification scope

Run the [fresh-build checker](../../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/formal/check.py) with Python. It freezes the standalone source, invokes pinned Lean 4.29.1 in a temporary directory, requires an axiom audit for every theorem, and records compiler, toolchain, checker, source and output hashes in [verification.json](../../../../experiments/shared-renewal-capability/regulation/retention/formation/selectors/updaters/prediction/recipient-correction/formal/verification.json).

All 36 declarations pass without compiler warnings, custom unproved declarations or unchecked proof shortcuts. Some have empty dependency lists; the union across all declarations is the standard foundations `propext` and `Quot.sound`. No `Classical.choice` dependency occurs in this package. These are checked conditional mathematical results, not empirical validation, a proof of the full stochastic program, or completion of the unified generative foundation.
