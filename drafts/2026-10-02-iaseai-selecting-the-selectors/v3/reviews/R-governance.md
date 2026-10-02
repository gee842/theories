# Review R-governance: "No Viable Winner: Competitive Selection, Captured Correction, and the Necessity of Cooperation in AI Development"

*IASEAI'27, archival track, double-blind. Reviewer profile: AI governance and AI safety, trained in philosophy of science. Inputs: `v3/main.tex` (all 395 lines, including appendices), the text of `v3/review-draft.pdf` (11 pages; main text ends about a third of the way down page 7), `v3/checks.log` and `v3/figures_v3.py`. Citations rendered "??" were ignored as instructed. Written 2026-10-02 by Claude Opus 5.5 at the request of the drafting session. No paper file was edited. Section 14 holds notes for the authors that a real reviewer would not have.*

---

## 0. Verdict in brief

**Score: borderline, leaning weak reject (4/10).** **Probability of archival acceptance as is: about 20% (range 15–25%).** With the three changes in Section 13: about 35–40%.

The paper asks the right question for this venue, and its second-order core is new and useful. That core is: control over correctors is selected in large carriers; correction of correctors is selected against; and the independent correction required rises as AI lowers the cost of control. The headline claims are another matter. "No viable winner", "each remedy now relied on" fails, "the conditions of any viable trajectory", and "cooperation is … a necessity" all go beyond the theorems. Each rests on one of three things:
- a premise the paper itself calls the least established (C0);
- modelling choices that are not listed among the conditions;
- a list of remedies chosen in their weakest versions.

A careful reader can therefore refute the headline without touching a single proof. That defeats the paper's stated aim. The aim is reachable: the second-order results support a narrower, harder claim, and the paper has about three unused pages in which to make it.

---

## 1. Summary of the submission

The paper builds a model of a "field" of developers inside a "host": a shared condition V with logistic regeneration, depleted by the field's activity and viable only above a floor V_min.

**First order.**
- Lemma 1: any relative selection rule is blind to terms common to all payoffs, including G(V).
- Proposition 1: the race strategy takes over under payoff-monotone selection. Under C0 (hē > ρ(1 − V_min/K)) the host falls below its floor.
- Proposition 2 (a static n-player game with weight λ on winning): depletion is dominant once λ > (θ − n)/(n − 1), and every player is worse off than under joint restraint when θ > 1.

**Second order.** Correctors (evaluation E, rules and liability S) are domains of a cooperative threshold system into which success converts.
- Proposition 3: control capacity is selected only above a size threshold, with a return quadratic in own share.
- Proposition 4: correction is a second-order public good, selected against inside the field.
- Proposition 5: the independent correction rate d* that keeps evaluation uncaptured rises as AI lowers the cost of control γ. If γ falls at rate g, correction growing slower than g/2 is eventually overtaken.
- Proposition 6: evaluator masking m delays or suppresses the alarm, including permanent silence of moderate harm.

**Synthesis.**
- Theorem 1 (C0–C4 plus an order-of-events condition): the host crosses its floor before any alarm.
- Table 1 maps seven remedies to unmet conditions.
- Theorem 2 gives invariants I1–I4, sufficient and each "indispensable".
- Corollary 1 concludes that cooperation binding all carriers, including states, is necessary.
- Table 2 pairs C0–C4 with indicators, evidence and falsifiers.

---

## 2. Strengths

1. **The right question, posed structurally.** "Who guards the guardians when the guardians are selected by the race they guard" is central to frontier AI governance. It is rarely formalised, and the paper does so without attributing motives to anyone. The sentence "What carriers value decides which strategies they try, not which ones grow" is a good one.
2. **The second-order results are the paper's real contribution, and they are useful.**
   - Control pays only above a size threshold, so it amplifies dominance rather than creating it.
   - Fragmentation divides cultivated conversion by k, while it raises the first-order commons problem through n. That trade-off between concentration and fragmentation is not obvious, and practitioners will find it informative.
   - The required correction rate d* is a calculable, policy-relevant quantity.
   - Proposition 9 says a pause that freezes shares completes capture unless rule-making is insulated. This is a crisp, non-obvious result, and it fits a common informal critique of pauses.
3. **A conditional, falsifiable style.** Pairing each condition with indicators and refuting observations (Table 2) is the right epistemic posture for a venue that mixes technical and policy reviewers. Admitting that C0 is "the least established condition" is honest.
4. **Even-handed in intent.** The paper criticises every camp: operator alignment, voluntary governance, open release, win-first, wait-for-evidence and pause. It does not single out a firm or a state. The race framing is cited for both the US and China. "Nothing in the result accuses anyone" is the right register.
5. **The proofs are short and, where I checked, correct.**
   - I re-derived Proposition 2. A brute-force best response at θ = 3 and θ = 8 for n ∈ {2, 3, 5, 10} matches the stated threshold (see Section 11 for why the paper's own check does not show this).
   - Proposition 5(i)–(iii): correct.
   - Proposition 6(ii): correct.
   - Lemma 1: correct.
6. **Compact.** The main text is about 6.4 pages. Note, though, that this leaves about 3.5 of the 10 allowed pages unused (Section 14).

---

## 3. Mapping to reality

### 3.1 Object-by-object

| Model object | Paper's reading | Closest real counterpart | Fit | Why |
|---|---|---|---|---|
| Host V, floor V_min | critical services, information environment, capacity for independent correction | Heterogeneous. Catastrophic-risk classes (bio, cyber, loss of control) are tail events, not regenerating stocks. The information environment and institutional capacity are stocks, but have no agreed floor. | **Poor to partial** | A logistic stock with a floor fits slow structural harms. Misuse and loss of control, the core concerns of most IASEAI attendees, are absent from the list. The floor is not absorbing (V regenerates from below V_min once E falls), so "floor" is a normative line, not a tipping point. "Capacity for independent correction" appears in V and again as d, a double role the model does not track. |
| e_k, ē, ν | fraction of activity that externalises load; private advantage | speed to deployment, omitted safeguards, release decisions | Partial | Real decisions bundle benefit and risk. Safety and capability are often complements (a negative "safety tax" on some margins). The model handles this only through the sign of ν. |
| Relative selection F | capital, compute and talent follow relative standing | Five to ten frontier firms and two or three frontier states; investment and talent do follow benchmark leadership | Partial | Replicator selection needs many carriers and time. For an oligopoly the defensible reading is imitation of practices (Schlag; Alchian), which the paper mentions but does not lean on. At state level, Proposition 1 does not apply, because states do not replicate; only Proposition 2 does. |
| τ (liability) | imposed by correctors | EU AI Act fines and GPAI obligations (Art. 55, 101); the revised EU Product Liability Directive (software); China's algorithm filing and security assessments for generative AI services; California SB 53 | Partial | τ > 0 already in several jurisdictions, so "τ = 0 unless an alarm fires" (C1) is false as stated. Ex post liability for diffuse harm to a shared host faces an attribution problem: I1 presupposes that each carrier's contribution e_k can be attributed. |
| Domain E, share x_E | evaluation "conducted within the practice's lineage" | Public institutes (UK AISI, US CAISI, EU AI Office), third-party evaluators (philanthropic or contract-funded), lab-authored benchmarks, LLM judges | Partial | Public institutes are *outside* the field on funding but *inside* on access (voluntary, time-limited, revocable) and on personnel. The model collapses funding, access, personnel and models into one b_ij. They differ in how reformable they are. |
| Domain S, share x_S | rule-making that accommodates the practice | standards bodies (CEN-CENELEC JTC 21, ISO/IEC JTC 1/SC 42, China's TC260), the GPAI Code of Practice drafting, legislatures | Partial to good | Industry participation in standards drafting is documented and fits b_ij. "One practice per domain" is a strong simplification of standards politics. |
| b_ij (conversion) | funding, personnel, authorship, data, access terms | documented in Wei et al. 2024 (AIES), Ahmed et al. 2023 (Science), Longpre et al. 2024, Whittaker 2021, Abdalla & Abdalla 2021 | **Good** | The best-supported mapping in the paper. Most of these sources are not cited in v3. |
| χ (appropriability) | support keyed to its producer: standards citing its interfaces, evaluations on its tooling | de facto API conventions and protocols set by one provider; lab-authored evaluation suites | Plausible, unmeasured | No indicator in Table 2 measures χ as distinct from b. |
| γ, g (cost of control falling with AI) | AI drafts standards and comments, writes evaluations, builds integrations | AI does lower drafting cost | **Poor to partial** | The binding inputs to control are access, credibility, relationships, money and legal standing, not drafting labour. AI also lowers the cost of correction. No evidence on g is offered (see O5). |
| d, α (independent correction) | rate at which rule support is corrected | public evaluation budgets, academic access, safe harbours, DSA Art. 40 researcher access | Partial | As a *rate*, d growing exponentially without bound is not a meaningful long-run object (see O5). |
| m, β_in, β_out (masking) | in-lineage and shared-material bias of evaluators | The real masking mechanisms in frontier evaluation: short pre-deployment access windows set by the developer; under-elicitation; evaluation awareness and sandbagging (van der Weij et al. 2024; Needham et al. 2025); loss of platform data access for researchers. | **Poor as stated, good if remapped** | Self-preference of LLM judges is a minor channel in dangerous-capability evaluations, which mostly use programmatic scoring, CTFs, expert grading and uplift trials. It is the main channel only for chat-quality leaderboards. |
| V_alarm, the alarm | alarm when the *reported host condition* falls to a level | If-then capability thresholds (leading indicators) in frontier safety frameworks, the GPAI Code and SB 53; serious-incident reporting (lagging) | **Poor** | Nobody "reports V". Correctors evaluate models, the inputs to harm, not the state of the host. |
| Scalable oversight, AI control | "AI in the evaluator's seat" | Debate, weak-to-strong, AI control | Partial, and mis-framed | These address the developer–model relation (can a developer catch its own model misbehaving?), not the society–developer relation the paper is about. AI control assumes worst-case adversarial masking and designs protocols against it, which is stronger than the paper's fixed, non-strategic β. |

### 3.2 Where the mapping is weakest (ranked)

1. **The alarm is on the wrong variable.** Real governance triggers on capability thresholds measured on models (if-then commitments), plus incident reports. The paper's alarm is on the host's state. The fix strengthens the paper. Split evidence into:
   - a *leading* channel: capability evaluations, masked by short access windows, under-elicitation and evaluation awareness;
   - a *lagging* channel: host indicators, masked by loss of independent data access.

   I4 ("fix thresholds before capture") then maps directly onto if-then commitments, and Section 6 becomes recognisable to evaluators.
2. **The host omits the risks the audience cares most about.** Misuse in bio and cyber and loss of control are tail events. A hazard version is easy and keeps Lemma 1 intact, because a catastrophe common to all is a common term: per-period catastrophe probability p(E), with viability as survival probability above a bound. One remark would bring these risks inside the model.
3. **Correctors are treated as uniformly "inside".** Public institutes are funded from outside but depend on access granted from inside. Separating funding, access, personnel and models as distinct b-channels would let the paper say which reform moves which term. For example, mandated access (EU AI Act Art. 92 evaluation powers) removes the access channel without touching personnel.
4. **γ is the paper's AI-specific lever, and it is the least evidenced.** See O5.

---

## 4. Strongest objections, ranked

### O1. The headline rests on C0, which the paper calls the least established condition, does not defend, and states in an untestable form. *(Critical for the headline; not for the core.)*

**Objection.**
- Theorem 1 ("no viable winner"), Theorem 2(b) (indispensability, constructed under C0), Corollary 1 (necessity) and the title all require C0: the race strategy can push the host below its floor.
- Table 2 calls C0 "contested and class-specific … the least established condition". Section 9 adds that "the theorem's other conclusions … do not depend on it". That is true, but the conclusions that do not depend on C0 are not the ones in the title.
- A sceptic in the "AI as normal technology" line (Narayanan & Kapoor 2025) denies C0, accepts every proof, and walks away with "competition causes a classical commons inefficiency and some evaluator capture, which ordinary regulation addresses".
- C0 is also untestable as stated. It concerns ē, the *maximum* depletion fraction, a counterfactual extreme. The listed falsifier ("shared conditions improve as deployment scales") tests current load, not capacity at ē.

**How damaging.** Fatal to the headline, harmless to the core. Survival table:

| Result | Needs C0? | What survives without C0 |
|---|---|---|
| Lemma 1; Prop. 1(i)–(ii) | No | Restraint is displaced, and V → V* > V_min: inefficiency, not failure |
| Prop. 1(iii); Prop. 2(iv) | Yes | — |
| Prop. 2(i)–(iii) | No | Pareto inefficiency when θ > 1 (classical) |
| Props. 3, 4, 5 | No | Intact: the whole novel core |
| Prop. 6(i), (iii), (v) | No | Delay; permanent silence of moderate harm (but moderate harm is viable by definition) |
| Theorem 1 | Yes | — |
| Theorem 2(a) / 2(b) | No / Yes | Sufficiency only |
| Corollary 1 (necessity for viability) | Yes | "Cooperation is Pareto-improving", which is classical |
| Title, last three sentences of the abstract, conclusion | Yes | — |

**Revision.**

(a) **Two tiers, stated as such.**
- Tier 1, C0-free: the competitive trajectory cannot keep its own correctors independent, and independent correction must be supplied from outside at a rate tied to AI's effect on the cost of control.
- Tier 2, under C0: no trajectory is viable without I1–I4.

The paper also already has a second, C0-free route to the cooperation conclusion. It is the normative premise stated in Limitations, that those affected should keep "a meaningful capacity to contest its direction". Combine that premise with Propositions 3–5 and with carriers that operate across jurisdictions: keeping correction independent then requires an arrangement covering those jurisdictions, with or without a floor. Make this route explicit. It trades an empirical premise that is contested for a normative one that almost no one at IASEAI will reject.

(b) **Anchor C0 in documents the modelled actors have adopted, symmetrically.** Replacement for the C0 row of Table 2 ("Present evidence"):

> "Developers' own frontier safety frameworks define capability thresholds beyond which deployment without further safeguards would be unacceptable, and national frameworks in the US, the EU and China name catastrophic and loss-of-control risks [Anthropic RSP; OpenAI Preparedness Framework; Google DeepMind Frontier Safety Framework; Seoul Frontier AI Safety Commitments 2024, whose signatories include US, European, Chinese and other firms; EU GPAI Code of Practice 2025; TC260 AI Safety Governance Framework 2024]. Whether any threshold is reached under the race strategy is contested [Bengio et al. 2025]. C0 is the least established condition."

This turns C0 from the authors' premise into a premise that the actors whose behaviour is modelled have already accepted.

(c) **Make C0 existential over harm classes, and give it a testable form.** Replacement for (C0) in Theorem 1:

> "(C0) for at least one class of shared condition, the race strategy can push the host below its floor, Eq. (3)."

Falsifier:

> "For every harm class with a posited threshold, independently measured capability with safeguards removed (the race strategy's ē) stays below the threshold."

Uplift studies on models with safeguards removed are the measurement.

(d) *Optional, high value.* Make C0 a rate condition parallel to C3. Harm potential per unit activity h·ē rises with capability, and safety research lowers it. C0 then holds eventually if and only if capability-driven harm potential grows faster than safeguards reduce it. This replaces an unfalsifiable level premise with a rate that existing evaluation series can track. It is the same comparison the paper already makes for correction.

(e) Make the floor dynamical. With an Allee-type host, V̇ = ρV(V/V_min − 1)(1 − V/K) − hEV, crossing the floor is irreversible, which is what "viability" usually means (Scheffer 2009 is already in the bibliography). That makes "silent crossing" a real loss, not a crossing of a line drawn on paper.

### O2. "Necessity of cooperation" does not follow as stated. *(Major.)*

Five distinct gaps.

**(a) Negated failure conditions are not necessary conditions.** "The conditions of Theorem 1 can be negated one by one. Their negations are the invariants a viable trajectory must respect." Theorem 1 has the form C0 ∧ … ∧ C4 ∧ order → failure. Negating its antecedent yields nothing about viable trajectories; that is denying the antecedent. Theorem 2(b) then proves something weaker than necessity: for each invariant, *there exist* parameters satisfying C0 and the other invariants under which the floor is crossed. That is non-redundancy in the worst case. It is a respectable notion (necessity for a *guarantee* that holds without knowing the parameters), but it is not "the conditions of any viable trajectory" (abstract). Within the model, viable trajectories exist without I1–I4: whenever C0 fails, and whenever θ > n + λ(n − 1).

*Replacement* for the sentence opening Section 8:

> "Negating the conditions of Theorem 1 yields conditions that suffice for viability. Theorem 2 shows that none of them can be dropped from a guarantee of viability that holds across the parameter range consistent with C0. This is the sense in which we call them necessary: necessary for robust viability, not for every viable path."

**(b) The model has no states, yet the corollary concludes that states must cooperate.**
- Corollary 1 shows only that no *carrier* (developer) can establish I1–I4 by choices that remain subject to selection. It then concludes "an arrangement that binds all of them, including the states in which they operate". The step from "no carrier can" to "only an arrangement among all states can" is not in the model.
- A rule-maker outside the field can set τ, d and χ for every carrier in its jurisdiction. That rule-maker could be a national regulator, or a large market regulating extraterritorially (the "Brussels effect" of the AI Act), or a compute chokepoint.
- So the necessity of *inter-state* cooperation rests only on the sentence "Proposition 2 applies with states as players". With two or three frontier states, Proposition 2 makes restraint dominant whenever θ > n + λ(n − 1); for two states, θ > 2 + λ. In the model, then, whether states need an agreement depends on how strongly rivalry weighs (λ) against how much they value the shared host (θ).
- That result is informative and should be stated. It implies two forms of cooperation short of a binding arrangement, which Section 8 never mentions:
  - shared scientific risk assessment, which raises the θ that states perceive (the International AI Safety Report; the UN scientific panel);
  - de-escalation of race framing, which lowers λ.
- The second-order apparatus (capture of correctors) is never developed for states. Yet that is where the paper's novelty would bite: international standards bodies and evaluators are also subject to conversion from the largest states.

*Replacement* for Corollary 1:

> "**Corollary 1 (What no participant can do alone).** (i) No carrier can establish (I1)–(I4) by choices that remain subject to selection: its unilateral restraint and its investment in correction are selected against (Propositions 1, 4), and a corrector it funds or forms belongs to its lineage. (ii) A rule-maker outside the field can establish them for the carriers in its jurisdiction, and is then itself subject to (I2)–(I4). (iii) Where carriers can grow in several jurisdictions, and the rule-makers are themselves players in a contest of relative standing (Proposition 2 with states as players), (I1)–(I4) hold only if every jurisdiction in which a carrier's share can grow is covered by rules that meet them and by correctors that no party controls. Among n states this is required whenever λ > (θ − n)/(n − 1). When θ > 1 and exposure to the host is shared, such an arrangement raises every party's absolute payoff (Proposition 2iii)."

**(c) "The arrangement enforces itself" contradicts the literature the paper cites.**
- Once I1 is in force, restraint is each *firm's* best response. But who imposes τ on *states*? Nothing in the model supplies inter-state enforcement.
- Barrett (1994; 2003), whom the paper cites for its precedents, is best known for showing that self-enforcing agreements on linear public goods sustain little cooperation when the gains from cooperation are large, unless they are backed by trade measures or minimum-participation clauses.
- The Montreal Protocol worked partly because substitutes were cheap (low ν) and trade with non-parties was restricted. AI's ν (economic and military advantage) looks more like greenhouse gases than CFCs.

*Replacement* for the corollary's last sentence:

> "Once (I1) is enforced, restraint is each carrier's best response. Between states, enforcement of (I1) is not supplied by the model. Agreements among states are self-enforcing only under restrictive conditions [Barrett 1994; Carraro & Siniscalco 1993], which is why coverage and verification (Section 8) are the hard parts of the arrangement."

**(d) "It does not require trust, because the corrector placed outside the competition verifies."** This assumes away the central open problem of international AI governance: verifying compliance with access to models, compute and training runs that states treat as sensitive (Shavit 2023; Baker 2023; Wasil et al. 2024). *Replacement:*

> "It does not require parties to trust one another's intentions. It requires that they accept verification by correctors none of them controls, with access that none of them can revoke. Designing verification that rival states accept is the hardest open part of the arrangement [Shavit 2023; Wasil et al. 2024]."

**(e) "Joint development" contradicts the paper's own regress.** The text says joint development "takes frontier development out of relative selection altogether", with correctors needed "only for harms to those not party to it". By the paper's own logic, though:
- allocation within a joint project is a new contest among its members (compare *juste retour* politics in CERN and ITER);
- the joint project is the largest possible carrier, so Proposition 3 gives it the largest return to controlling its correctors;
- the objection "Capture is not inevitable" itself says that the account "applies to every institution, including any that adopts it".

*Replacement:*

> "In the limit of joint development, in which the frontier's returns are shared, the first-order problem disappears (n = 1 in Proposition 2). The second-order problem does not: allocation within a joint project is itself a contest among its members, and the project, as the largest carrier, has the largest return to controlling its correctors (Proposition 3). Joint development needs independent correctors as much as competitive development does."

### O3. Table 1 fights the weakest version of each remedy and omits the remedies most relied on. *(Major.)*

**Objection.** The abstract says "each remedy now relied on leaves a necessary condition unmet". Table 1 has seven rows. Most describe the dependent or naive version of a remedy, and the "best version" of several rows *is* one of the paper's invariants. Missing entirely:
- **technical safety research and safeguards**, which lower h and ē and can negate C0 for a harm class;
- **societal resilience**, which raises ρ;
- **binding regulation with statutory evaluation powers** (EU AI Act GPAI obligations and AI Office powers; China's filing and security-assessment regime; California SB 53);
- **compute governance** (monitoring, licensing at chokepoints);
- **existing international institutions** (the network of AI safety institutes, the UN scientific panel);
- **deterrence among states** (Hendrycks, Schmidt & Wang 2025).

Practitioners in each camp will contest their row; Section 5 goes row by row. The result is that Table 1 reads as built to show that everything fails, which invites the reply "you chose weak versions".

**How damaging.** Major at this venue, because many reviewers *work* on these remedies. It is also the easiest objection to turn into a strength.

**Revision.** Reframe Table 1 from "why remedies fail" to "what each remedy supplies, what it leaves, and what only an arrangement across parties adds". New caption:

> "Table 1: What current remedies supply and leave. Each remedy, in its strongest current form, establishes some invariants of Theorem 2 for some carriers. None establishes coverage across jurisdictions together with independent correction that keeps pace with the falling cost of control. That is what an arrangement among parties adds."

New rows. The column "Supplies" is in the model's terms:

| Remedy (strongest current form) | Supplies | Leaves (model) | Missing piece |
|---|---|---|---|
| Technical safety research and safeguards | lowers h, ē; can negate C0 for a class | Supplied where privately valued (reliability, refusals customers want). Under-supplied where the benefit falls only on the host (the logic of Prop. 4). Knowledge is a best-shot good; adoption by every carrier is a coverage problem. | public funding of non-appropriable safety research; adoption across carriers (I1) |
| Frontier safety frameworks and if-then commitments | thresholds fixed in advance (I4); internal evaluation | Unilateral restraint is displaced unless codified (Prop. 1). Thresholds are set inside the field (C2). | codification with liability (I1); external verification (I3) |
| Binding regulation in a large market | I1 for carriers in that market; statutory access (I3) | Carriers grow elsewhere; national-security development is out of scope; the rule-maker is subject to C2–C3. | coverage across jurisdictions; correction that keeps pace (I2) |
| Public evaluation institutes under voluntary access | partial I3 | Access is revocable and time-limited; personnel and tooling come from the field (C2, C4). | mandated access; pooled funding indexed to capability (I2, I3) |
| Operator alignment, scalable oversight, AI control | the developer can detect its own model's misbehaviour | The society–developer relation is untouched. Capability lowers the cost of control *and* of correction (Prop. 5). | the same tools in independent correctors' hands |
| Open release and fragmentation | lowers concentration and χ; widens outside evaluation (raises d) | Raises n, lowering the λ at which depletion dominates (Prop. 2); removes safeguards against misuse (raises ē). | I1 for released capability classes |
| Win first, then govern (a lead as safety margin and bargaining leverage) | fewer contenders; slack to slow down | C1 holds during the race. The leader is the carrier selected for control (Prop. 3). Slack is spent on control unless the leader's correctors are independent. | I2–I4 bind the leader |
| Regulate once harm is evident (incident reporting) | correction triggered by evidence | Lagging evidence formed in the field is delayed or silenced (C4); decision and reversal must fit the window. | I3 with thresholds fixed in advance (I4) |
| Pause (international, verified) | halts depletion | Frozen shares convert into rule support unless rule-making is insulated (Prop. 9). | insulation and verification |
| Measures that change relative standing between states (controls on inputs, self-reliance programmes) | slows a rival | Changes standing, not the selection rule; raises the weight on winning λ. | — (chokepoints are useful as verification assets under an agreement) |

The last row must be worded symmetrically, as here, or omitted. See Section 8.

This framing is harder to refute, because each cell is a weaker and more accurate claim. It is also more persuasive, because it makes cooperation the *completion* of the portfolio IASEAI's members are building rather than a *replacement* for it.

### O4. The payoff accounting is chosen in a way that delivers "no viable winner". *(Major.)*

Four modelling choices, none listed among the conditions, carry the "winner is worse off" claim.

1. **No prize for winning.** π_k is a per-unit payoff. Under selection the winner's share goes to one, and in real races the prize *is* share: market, rents, decisive strategic advantage. Prop. 2(iii) compares per-unit payoffs in a *symmetric* equilibrium, which has no winner. The phrase "every developer, the eventual winner included" has no referent in the model.
2. **Control rents omitted.** Theorem 1 states that "every carrier ends with a lower absolute payoff than under joint restraint whenever θ > 1", and its proof imports this from Prop. 2(iii). Prop. 2 has no correctors. In Theorem 1's own dynamics the dominant carrier earns rule-support rents (W(q*) > 0 above the size threshold) and escapes τ through x_S. Its payoff is therefore not covered by the comparison. This is a checkable gap in the theorem itself.
3. **The floor is in the viability definition but not in payoffs.** G is linear, so crossing V_min costs a player nothing special, and carriers do not exit when V < V_min. "Every participant persists only while the host does" is asserted in prose, not modelled. With a G that is steep near the floor, rational players in Prop. 2 would restrain *near the floor if they could see it*. The failure then needs either selection (C1, which ignores values) or masking (C4, which hides proximity). That is the paper's real argument, and it is stronger than the linear-G version. Say it.
4. **Shared exposure.** Some components of the host, notably "capacity for independent correction", are depleted *to the benefit* of the dominant carrier: a captured corrector favours it. The paper lists "unequal exposure" as open, but it is central. If the winner is insulated, the winner may be viable while the host is not.

**How damaging.** Major. A political economist will see points 1 and 2 within minutes, and point 4 inverts the title.

**Revision.**

(a) Delete the payoff clause from Theorem 1, or qualify it:

> "… the host crosses its floor before any alarm. If, in addition, exposure to the host is shared and θ > 1, the race equilibrium of Proposition 2 leaves every carrier with a lower absolute payoff than joint restraint. Rents from control over correctors are not included in this comparison (Remark 2)."

(b) Delete "the eventual winner included" from Prop. 2(iii).

(c) Add a remark that turns unequal exposure into a dilemma:

> "**Remark 2 (Unequal exposure).** If a carrier's exposure to the host falls with its share, because it can buy private substitutes for shared conditions or because a captured corrector favours it, the host no longer cancels from comparisons involving that carrier, and selection favours insulation as well as depletion. Either exposure is shared, and no carrier's trajectory is viable once the host crosses its floor. Or it is not, and a carrier may remain viable while the host does not. That is the concentration of power that the contestability premise of Section 10 excludes. Neither branch yields a trajectory that those who depend on the host can accept."

This makes the headline robust to the strongest counter, "the winner survives", and connects the paper to the concentration-of-power literature (e.g., Davidson et al. 2025 on AI-enabled seizures of power; Kulveit et al. 2025).

(d) Add one sentence after Prop. 2:

> "With G steep near the floor, informed players restrain near it. The failure of Theorem 1 therefore requires either selection, which ignores values (Proposition 1), or masking, which hides proximity to the floor (Proposition 6)."

### O5. The AI-specific rate result, "half that rate", is a functional-form artifact, and the conclusion drawn from it is not derived. *(Major; checkable in ten minutes.)*

**Objection.**

(i) **The factor one half comes from the quadratic cost of control.** With C(q) = fq + γq^k/k, the selected capacity is q* = (χŶ/(γd))^{1/(k−1)}. The cultivated term in s_E then scales as γ^{−1/(k−1)} d^{−k/(k−1)}, so asymptotically d* ∝ γ^{−1/k} and d* grows at g/k. I checked this numerically with the paper's parameters:

| k | 1.5 | 2 | 3 | 4 |
|---|---|---|---|---|
| asymptotic growth rate of d* | 0.133 | 0.100 | 0.066 | 0.049 |
| g/k | 0.133 | 0.100 | 0.067 | 0.050 |

The abstract's "less than half that rate" therefore states a curvature parameter as if it were a finding.

(ii) **The rate race needs control capacity that grows without bound as γ → 0** (linear conversion, no saturation), and a correction *rate* d that grows exponentially forever. With any saturation of the return to control (a bounded number of standards seats or benchmarks that matter), d* is bounded, and a constant d eventually suffices.

(iii) **The pessimistic conclusion is not derived.** AI also lowers the cost of correction: AI-assisted evaluation, automated red-teaming, interpretability, regulatory analysis. Suppose the cost of correction falls at the same rate and with the same curvature as the cost of control, and budgets are fixed. Then d grows exactly as fast as d*, and the outcome is decided by budgets and adoption, not by AI. Yet the conclusion says "AI makes guarding harder faster than it makes it easier unless independent correction keeps pace". The "unless" clause makes this nearly tautological, and the rest is not shown.

(iv) **Table 2 offers no evidence on g.** The C3 row cites capability-horizon doubling (Kwa et al. 2025) and assurance lagging capability. Both concern capability growth, which does not enter Proposition 5 (see O7).

**How damaging.** Major. It is the paper's one AI-specific quantitative claim, and it appears in the abstract.

**Revision.**

(a) Generalise and sharpen Proposition 5. I verified that the sharper statement holds. With d = d₀e^{αt} and γ = γ₀e^{−gt}, both terms of s_E(t) are non-increasing when α ≥ g/2, so the certificate holds for all t if and only if it holds at t = 0. That is better than the paper's sufficient condition d₀ > A/c_E + S. Replace (iii)–(iv) with:

> "(iii) If AI lowers the cost of control as γ(t) = γ₀e^{−gt} and independent correction grows as d(t) = d₀e^{αt}, then for α ≥ g/2 the certificate holds for all t if and only if d₀ > d*(0); for α < g/2 it fails for all t > t*. (iv) With cost C(q) = fq + γq^k/k, k > 1, the threshold rate is g/k. Quadratic cost gives one half."

(b) Abstract:

> "… it rises as AI lowers the cost of control (as the square root of that fall, under quadratic cost)."

(c) Add a remark:

> "**Remark (Who adopts AI).** If AI lowers the cost of independent correction at rate g_c, with curvature k_c, the certificate is kept if and only if g_c/k_c ≥ g/k. With symmetric technology the result is decided by budgets and adoption, not by AI. Equipping independent correctors with the same AI the field uses is therefore a direct instrument for (I2)."

This turns a pessimistic, contestable claim into an actionable and robust one: fund AI-assisted independent evaluation, with budgets indexed to the field's capability.

(d) Replace "What AI changes", sentence 2:

> "Operator alignment does not change this: an assistant that faithfully serves its principal lowers that principal's cost of control as much as any capability does. Alignment to operators is therefore not sufficient. Whether AI favours control or correction depends on whether independent correctors adopt it as fast (Remark X)."

The current wording, "alignment to operators raises the correction the field needs", attributes to alignment what capability does. Alignment reviewers will reject it.

### O6. The masking and detection model does not match how frontier evaluation fails, and two of its choices carry the result. *(Major to moderate.)*

**Objection.**

(i) The required magnitude is large. In Fig. 2b the silent crossing needs β_in = 0.5 > m_fl ≈ 0.43: a captured evaluator reports the host halfway to full health. The cited evidence (self-preference in chat-quality judgments) is on a different scale and is small.

(ii) **Averaging is a structural choice that decides the result.** Reports are *averaged* over evaluators (Eq. 7). If the alarm fires when *any* credible evaluator reports below threshold, the silent crossing needs *every* evaluator masked (β_out > m_fl). Real systems include such a rule: whistleblowers, independent researchers publishing, safe harbours. Under a disjunctive rule, I3 reduces to "at least one independent evaluator with a hearing", which a single state or philanthropy can supply. The paper's defensible answer is that a captured rule-maker (x_S) does not act on dissent. That moves the problem from E to S, which is already in the model. Say so.

(iii) Masking is non-strategic (Limitations), while the alignment literature's central evaluation problem is strategic: evaluation awareness and sandbagging. The paper is weaker than its field here, not stronger.

(iv) The alarm variable is wrong (see 3.2, item 1).

**Revision.**

(a) In Section 6, add:

> "Reports are averaged because rule-makers act on the weight of evidence. If the alarm instead fires on any credible report, silent crossing requires β_out > m_fl, and (I3) can be met by a single independent channel. What then decides the outcome is whether a captured rule-making domain acts on that channel (x_S), which Theorem 1 already covers."

(b) Remap the masking parameters. β_in covers short access windows set by the evaluated developer, under-elicitation and evaluation awareness (van der Weij et al. 2024; Needham et al. 2025) for the leading channel; β_out covers shared training data and homogenised judges (Kleinberg & Raghavan 2021; Bommasani et al. 2022) and loss of researcher data access for the lagging channel.

(c) State in Table 2 that measured effects are far below m_fl (see O7), so the *silent crossing* is a possibility result. The *permanent silence of moderate harm* is the case the evidence supports.

### O7. Table 2: honest about C0, less honest elsewhere; and a risk of immunisation. *(Moderate to major.)*

**Row by row.**

- **C0.** The falsifier does not test the condition (see O1).
- **C1.** The condition includes "τ = 0 unless an alarm fires", which is already false. Its evidence ("development framed as a race by governments") is rhetoric, not selection. The listed indicator (capital, compute and talent following relative standing) is the right one, but no evidence is given for it. *Replacement condition:*

  > "C1: relative selection on margins where the effective liability τ(1 − x_S) is below the private advantage ν."

  *Evidence:*

  > "Liability and ex-ante conditions now exist in several jurisdictions [EU AI Act; China's generative-AI measures; California SB 53]; whether they exceed the private advantage on the relevant margins is open. Investment and talent concentrate in developers at the capability frontier [Ahmed et al. 2023; AI Index]."

- **C2.** The evidence supports b > 0 (dependence, gaming), not χ > 0 (appropriability), nor a carrier above the size threshold. The bibliography already contains stronger evidence (Wei et al. 2024 on capture mechanisms in AI policy; Ahmed et al. 2023; Whittaker 2021; Abdalla & Abdalla 2021). Add an appropriability indicator: the share of standards and evaluation suites that reference one provider's interfaces or tooling.
- **C3.** The evidence is mismatched. Capability horizons doubling and assurance lagging say nothing about α or g. *Replacement evidence:*

  > "No direct measurement. Proxies: growth of public budgets for independent evaluation against growth of developers' policy and standards engagement (lobbying disclosures, committee seats, lab-authored benchmarks). Capability growth [Kwa et al. 2025] bears on the difficulty of evaluation, not on g."

- **C4.** Existence is evidenced; magnitude is not. *Replacement evidence:*

  > "Self-preference and preference leakage in model judges [Panickssery et al. 2024; Li et al. 2026]; correlated errors across providers [Kim et al. 2025; Goel et al. 2025]. Recent measurements find small or undetectable own-model premia but shared preferences across families [preprints], which bears on β_out rather than β_in. Silent crossing requires masking above m_fl, far above any measured effect; permanent silence of moderate harm requires much less."

**Immunisation.** The paper makes two statements about evidence:
- "measurement of the indicators must be independent of the field (I3), or it inherits the masking it is meant to detect";
- "waiting for certainty is itself a choice of trajectory".

Together they let the paper discount any evidence that the host is healthy as possibly masked. This is a conventionalist stratagem in Popper's sense: it protects the theory from refutation by reinterpreting contrary evidence. A philosopher of science on the committee will name it. *Revision.* Name, now, the channels whose evidence the authors will accept as refuting. Add to Section 9:

> "We treat as independent, and accept as refuting, measurements by public statistical agencies, by researchers with mandated data access, and by evaluators with statutory access whose funding does not come from the evaluated firms."

### O8. "Cooperation" has no operational content: what, by whom, verified how. *(Moderate to major.)*

**Objection.** The paper says "cooperation among developers and states", "an arrangement that binds all of them", "joint development" and "cooperation on its conditions, not its spoils". Nowhere does it say:
- what must be agreed (which harm classes, which thresholds, what liability, what funding);
- who must be party (all states? frontier states? states controlling the compute supply chain?);
- how compliance is verified.

It also blurs three different things: coordination on standards, mutual restraint, and joint development. "Cooperation" also collides with "Cooperative AI" (Dafoe et al. 2020), which means cooperation *among AI systems*.

**How damaging.** Moderate to major. Policy reviewers will ask "cooperate on what?". The model can in fact answer, and the paper has the space to do so.

**Revision.** Add a definition, derived from the model, and one table.

> "**Definition (Cooperation on the conditions).** An arrangement is cooperative in our sense if it has three properties. (a) *Coverage*: it binds every carrier whose share can grow in the selection environment it governs, and the rule-makers of every jurisdiction in which such growth can occur. (b) *Content*: it enacts (I1)–(I3) with thresholds, triggers and the authority to act fixed in advance (I4). (c) *Verification*: compliance and the host's condition are assessed by correctors whose inbound conversion from every party is below one. The invariants constrain properties, not institutional form: they can be met by one institution or by mutually recognised national institutions."

| Invariant | What must be agreed | By whom | Verified how | Existing seeds |
|---|---|---|---|---|
| I1 consequences return | harm classes with floors; conditions on deployment or liability exceeding the private advantage on those margins | states hosting frontier developers or frontier compute | pre-deployment evaluation; incident reporting | EU AI Act Art. 55; China's filing and security assessment; California SB 53; frontier safety frameworks |
| I2 independent correction keeps pace | pooled funding at arm's length, indexed to the field's capability (for example a levy on frontier training compute), with AI tools for correctors | states and developers as payers, not controllers | public budgets; capacity audits | network of AI safety institutes; UN Independent International Scientific Panel on AI |
| I3 independent evidence | mandated, non-revocable access; safe harbours; whistleblower protection; evidence channels not formed on the field's outputs | the same parties | access logs; mutual inspection | AI Act Art. 92; DSA Art. 40; safe-harbour proposals [Longpre et al. 2024] |
| I4 before capture | thresholds and triggers fixed before evidence arrives; review clauses | the same parties | public registry of commitments | if-then commitments; Seoul commitments; IDAIS red lines |
| Verification across states | compute accounting; hardware-enabled mechanisms; mutual inspection | states controlling the compute supply chain | technical verification [Shavit 2023; Wasil et al. 2024] | none yet |

This gives the cooperation conclusion concrete content without proposing a world authority. That also protects the paper politically (Section 8).

### O9. Expertise versus independence: "evaluators that are neither funded nor formed by those they evaluate". *(Moderate.)*

**Objection.** Almost every evaluator competent at the frontier was trained in, or by, the field, and evaluation quality depends on access. In the model, every conversion channel b_ij is pure capture. In reality the same channels (access, personnel, tooling) carry *competence*. This trade-off is the central dilemma of the capture literature (Che 1995; Dal Bó 2006), and it is why safety institutes hire from labs and depend on lab access. Read literally, the instrument "neither funded nor formed" is infeasible. A regulator will ask: "Should institutes stop hiring former lab researchers?" The model cannot answer.

**Revision.** One paragraph in Section 8:

> "Independence does not require evaluators without access or expertise. It requires that access be mandated rather than granted, so that it cannot be withdrawn, and that expertise be acquired through channels that do not convert into rule support: cooling-off periods, rotation and disclosure. In the model, these remove the conversion b_Ej while keeping the competence that the same channels carry."

Ideally, add an evaluation-precision term that increases in access and show the frontier between precision and capture. If there is no time for that, state the trade-off in Limitations.

### O10. Related work is thin exactly where this audience lives. *(Moderate; easy to fix.)*

See Section 10 for the list. The most damaging omissions are four:
- **the closest formal prior work:** evolutionary-game models of AI races with safety and regulation (Han et al. 2020, JAIR; Han et al. 2021, PLOS ONE, already in the bibliography);
- **the race-rhetoric literature at AIES itself** (Cave & ÓhÉigeartaigh 2018);
- **international-institution proposals** (Ho et al. 2023; Maas & Villalobos 2023; Trager et al. 2023; Cihon, Maas & Kemp 2020);
- **third-party audit independence**, already in the bibliography but uncited (Raji et al. 2022; Costanza-Chock et al. 2022; Birhane et al. 2024).

---

## 5. Table 1 row by row: how practitioners would contest it

| Row as written | Who contests | Their best argument | Fair verdict |
|---|---|---|---|
| Align each system to its operator: "C1–C3 untouched; faithful assistance lowers γ" | Alignment researchers | Alignment is more than operator alignment. Model specifications impose platform-level rules operators cannot override. Honesty research lowers masking. Interpretability is an evidence channel that does not run through the model's self-report (I3). Capability, not alignment, lowers γ. | Unfair as worded. The fair claim is that operator alignment is *not sufficient* (O5d). |
| Voluntary self-governance: "restraint is displaced" | Lab policy teams; framework authors | Frameworks are coordination devices and templates for regulation (if-then commitments codified in the GPAI Code and SB 53), a "race to the top" on norms. | Partly fair. Unilateral restraint is displaced, but codification is the route to I1. The row should say so. |
| Evaluation dependent on developers, model judges | Safety-institute and third-party evaluators | Institutes are publicly funded. Dangerous-capability evaluations rarely rely on LLM judges. Statutory access powers now exist (AI Act Art. 92). | The weak version is described. The strong version (public funding plus mandated access) is the paper's own I2/I3. |
| Open release, fragmentation | Open-weights advocates | Openness lets independent researchers study weights, raising d, and lowers χ. | Missing their best point (d rises). The concern about misuse (ē rises) is also missing, which would make the row more balanced. |
| Win first, then govern | National-security and "lead as safety margin" proponents | A large lead buys time to slow down near dangerous thresholds and leverage to negotiate from strength. | The row does not engage "lead as margin". The model's answer (the leader is selected for control; slack is spent on control unless its correctors are independent) should be stated. |
| Regulate once harm is evident | Evidence-based-policy and "normal technology" scholars | Invest in early evidence: incident reporting, monitoring. Harms are gradual and visible. | The critique assumes C4. The best version (independent monitoring) *is* I3. The real disagreement is C0 and its timing. |
| Pause that freezes shares | Pause advocates | A real pause would be international, verified and conditional, with insulated rule-making. | Prop. 9 itself shows that an insulated pause works. Label the row "Pause without insulated rule-making". |

---

## 6. Falsifiability: summary judgement

- **C0** is not testable as stated (counterfactual ē). It becomes testable if made existential over harm classes and measured with safeguards removed (O1c), or if recast as a rate (O1d).
- **C1** is testable in principle (capital and talent flows by rank). As stated it includes a clause that is false (τ = 0).
- **C2** is testable for b (funding and access dependence); χ is untested and the size threshold s* is unmeasurable.
- **C3** is not tested by the evidence given. Its proxies exist (budgets, lobbying disclosures, committee composition) but are not offered.
- **C4** is testable and partly tested for existence; magnitude is untested and probably far below m_fl.
- **The identification paragraph** opens with "The conversion parameters can be identified" and then says "structural recoverability, not causal identification". Lead with the second: "Under the model, the conversion parameters can in principle be recovered: …".
- **A sharp prediction is missing.** Prop. 4(iv) predicts that incumbents support *appropriable* regulation, which installs their own rule support (for example licensing regimes keyed to their capabilities), and oppose *non-appropriable* correction (mandated independent access, arm's-length funding). The prediction is testable by coding public comments on AI rule-makings. It would answer the "unfalsifiable" charge, and it explains why some incumbents call for regulation, which otherwise looks like a counterexample.

---

## 7. Philosophy of science: does "reject a condition" work?

**The deduction is sound; the rhetorical claim is not.** "A reader who rejects a conclusion must therefore reject a condition" is false. Under the Duhem–Quine point, a reader can reject a *structural assumption* of the model, or the *mapping* of model objects to the world, without rejecting any of C0–C4. The paper's headline depends on at least eight structural assumptions that are not listed as conditions:

| Structural assumption | What changes if relaxed |
|---|---|
| A1 a scalar host with shared exposure (G common) | Under unequal exposure the winner may be viable (O4.4); the dilemma remark rescues the conclusion |
| A2 the floor is in the viability definition but not in payoffs (linear G); the floor is not absorbing | With steep G, informed players restrain near the floor, so failure needs selection or masking (O4.3) |
| A3 h, ρ, ē exogenous (no safety-R&D or resilience choice) | C0 becomes a choice variable; the technical-safety and resilience remedies appear (O3) |
| A4 per-unit payoffs, no prize for share | "Every carrier worse off" fails for the winner (O4.1) |
| A5 linear conversion, no saturation of control | d* bounded; no exponential race (O5.ii) |
| A6 quadratic cost of control; AI lowers only γ | "Half" becomes 1/k; symmetric adoption ties the race (O5) |
| A7 averaged, non-strategic reports; alarm on host state | A disjunctive alarm moves the problem to S; strategic masking is stronger (O6) |
| A8 no states as actors; τ imposed by an unspecified rule-maker | Corollary 1's step from "no carrier" to "all states" is not derived (O2b) |

**Is the model built to deliver its conclusion?** Partly. Two results follow by construction:
- First order: "selection does not see the host" holds because the host is *defined* as an unpriced common term. The paper admits this ("classical").
- Second order, step one: "correction must come from outside the field" holds because correctors are *defined* as inside (C3) and independent correction as outside.

That is acceptable if it is stated as framing. The non-trivial results are the size threshold, the quadratic return, the d* formula, the dependence on the order of events, the reform and re-absorption results, and the pause result. The headline ("no viable winner", "necessity") is delivered by A1–A8 plus C0, plus a table of weak remedies. That is what a hostile reader will attack.

**Is "necessity" warranted?** Three senses must be kept apart:
1. logical necessity within the model, given the conditions;
2. *robust* necessity: required for a guarantee of viability across all parameter values consistent with C0;
3. practical necessity in the world.

Theorem 2(b) establishes sense 2 at most, in its weak existential form. The abstract ("in this model") is close to sense 1. The introduction ("a necessity rather than a hope") and the conclusion ("the one course the analysis leaves open") slide to sense 3. Pick sense 2, name it, and say it in the abstract.

**Recommended methodological additions** (each about one paragraph):
1. List A1–A8 next to C0–C4, and say which conclusions survive relaxing each. This is derivational robustness analysis (Levins 1966; Weisberg 2006; Kuorikoski, Lehtinen & Marchionni 2010).
2. Classify every claim as *theorem*, *model-to-world mapping* or *normative*. Table 1 and the instrument bullets are mappings, not theorems.
3. Call the model a "credible world" (Sugden 2000) or a "how-possibly" model where that is what it is. Reserve "show" for the theorems.
4. Fix the immunisation risk (O7).

---

## 8. Political reception

**Overall.** The paper is even-handed in intent, and I found **no sentence that accuses a particular firm or state**. The risks lie in implicit readings by reviewers from each bloc.

| Passage | Risk | Who reads it that way | Fix |
|---|---|---|---|
| "described by governments as a race to be won [whitehouse2025, statecouncil2017]" plus the title "No Viable Winner" | Reads as a rebuttal of the 2025 US plan, whose title is literally about winning the race. The Chinese citation is eight years older, so the pairing is asymmetric in recency. | US reviewers | "Several governments describe frontier development as a contest for leadership [US 2025; China 2017 and the 2025 'AI+' opinions; EU AI Continent Action Plan 2025; UK AI Opportunities Action Plan 2025]." Three or more blocs, current documents. |
| "an arrangement that binds all of them, including the states in which they operate" | Reads as advocacy of supranational governance. The 2025 US position at the UN rejected centralised global AI governance (verify the source). China promotes UN-centred governance and a proposed world AI cooperation organisation. | US reviewers, and some Chinese reviewers wary of whose institution it would be | Add: "The invariants constrain properties, not institutional form; they can be met by mutually recognised national institutions" (O8). |
| Host examples: "a reliable information environment", "institutional … capacity for independent correction" | "Information environment" and "independent institutions" read as liberal-democratic categories in Beijing, and as content-control language in some US circles. | Chinese and US reviewers, in opposite directions | Lead with components on which there is cross-bloc consensus: critical infrastructure, biosecurity, cyber stability, human control over AI systems (Bletchley; IDAIS red lines). Add: "Independence here means independence from the evaluated field, not any particular political form; a state agency, an academic body or an international panel can each satisfy it." |
| "Change the game, not the players. Replacing leaders or developers leaves selected traits in place" | "Replacing leaders" can be read as political leadership or regime change. | Any | "Replacing executives or firms leaves selected traits in place." |
| "Rivals have kept shared conditions above a floor before"; "leading rival states" | Casts US–China as a new Cold War; Chinese official discourse rejects that framing. | Chinese reviewers | "States in strategic competition have …" Name the Bletchley signatories factually: "endorsed by the United States, China and the European Union among 28 countries". |
| Precedents limited to Bletchley 2023 | Looks cherry-picked; Paris 2025, where the US and UK did not sign, is known to everyone. | European and US reviewers | Use the replacement below, which includes both success and fragility, symmetrically. |
| "Captured correction" in the title; "captured" throughout | Safety-institute staff may read an accusation. | Institute staff on the PC | In Section 3, add: "Capture here is structural: a share of decisions follows the dominant practice through conversion channels, with or without intent [Kwak 2014]. We do not claim that any current institution is captured; the model states the conditions under which capture is selected." |
| "Cooperation among developers" | Inter-firm restraint agreements raise antitrust questions, especially in the US and EU. | Legal reviewers | One sentence and a citation: Hua & Belfield 2021 on antitrust and cooperative AI development. Restraint enacted through public rules (I1) avoids the problem. |
| Possible future edit toward "shared future for mankind" | "Community with a shared future for mankind" is a signature phrase of Chinese diplomacy and would read as partisan to Western reviewers. | US and European reviewers | Keep the current "common future" with the Brundtland citation. Do not change it. |
| No engagement with the EU AI Act | European reviewers will treat the omission as a sign the authors do not know the field. | European reviewers | Cite AI Act Art. 55, 68 and 92 and the GPAI Code in Table 1 and Section 8. The bibliography already has `euaiact2024`. |

**Replacement precedents paragraph:**

> "States in strategic competition have kept shared conditions above a floor before, when the arrangement covered everyone who could deplete them and its monitoring was controlled by none: the ozone regime, smallpox eradication and the Antarctic Treaty [Barrett 2003, 2007], and, with verification, parts of nuclear arms control. Failures are as instructive. Where the private advantage of depletion is large and verification weak, as for greenhouse gases and biological weapons, agreements have stayed weak. For AI, the United States, China and the European Union endorsed the 2023 Bletchley Declaration; the two 2024 General Assembly resolutions on AI, one led by each country, were adopted without a vote; and scientists from both countries have agreed on red lines [IDAIS 2024]. By 2025 these commitments had already proved fragile. They are seeds, not the arrangement: they do not yet fix thresholds, fund independent correction or provide verification."

Verify each fact before use. I am confident of the Bletchley endorsements, the Paris non-signatures and the two 2024 resolutions adopted without a vote; check the wording of the IDAIS statement.

---

## 9. Precision and overclaiming, sentence by sentence

| Location | Current text | Problem | Replacement |
|---|---|---|---|
| Title | "… and the Necessity of Cooperation …" | Necessity holds only in the robust sense and under C0 | "No Viable Winner: Competitive Selection, Captured Correction, and When Cooperation Becomes Necessary in AI Development". This keeps the thesis and states its condition. |
| Abstract | "show under explicit, testable conditions that it cannot correct itself" | C0 is not testable as stated; "cannot" is model-relative | "show, under explicit conditions paired with observable indicators, that within the model it cannot correct itself" |
| Abstract | "the more weight the contest places on winning, the sooner this holds" | Prop. 2 is static, so "sooner" is not temporal | "… the more readily this holds" |
| Abstract | "correction that grows at less than half that rate is overtaken" | Curvature artifact (O5) | "… it rises as AI lowers the cost of control (as the square root of that fall, under quadratic cost)" |
| Abstract | "Each remedy now relied on leaves a necessary condition unmet" | Seven weak versions; binding regulation, technical safety, compute governance and international institutions are omitted | "Each current remedy establishes some of the conditions for some participants; none establishes all of them across participants" |
| Abstract | "The conditions of any viable trajectory can be established only jointly" | False within the model (O2a) | "The conditions that guarantee viability across the model's parameter range can be established only jointly" |
| Abstract | "and they leave every participant better off" | Needs θ > 1, shared exposure and no prize for winning | "and, where exposure is shared, they leave every participant better off" |
| Intro, para. 2 | "cooperation follows as a necessity rather than a hope" | Slides to practical necessity | "so the model makes cooperation a condition of viability rather than a hope" |
| Method | "Every claim is a conditional statement proved …" | Table 1, the precedents, "enforces itself" and "does not require trust" are not proved | "Every formal claim …" |
| Method | "A reader who rejects a conclusion must therefore reject a condition." | Ignores structural assumptions and mapping (Section 7) | "A reader who rejects a conclusion must reject an empirical condition (C0–C4) or a structural assumption (A1–A8); we say which conclusions survive the rejection of each." |
| Prop. 2(ii) | "at every λ ≥ 0 when n ≥ θ" | At n = θ and λ = 0 players are indifferent | "when n > θ" |
| Prop. 2(iii) | "every developer, the eventual winner included" | The symmetric equilibrium has no winner | "every developer" |
| After Thm. 1 | "The order of events is not left to chance … Acceleration therefore favors capture before evidence." | Not derived: AI may also speed the spread of the race strategy and of h | "The order of events is not fixed by the model. Proposition 5 bounds the time to capture by t*, which shrinks as AI lowers the cost of control faster. The time for the host to reach the alarm level depends on h, ρ and the spread of the race strategy, which AI may also accelerate. Capture before evidence is a condition to be checked, not a consequence." |
| Sec. 8, opening | "Their negations are the invariants a viable trajectory must respect." | Denying the antecedent (O2a) | See O2a |
| Corollary 1 | "so the arrangement enforces itself as long as …" | Inter-state enforcement is not modelled (O2c) | See O2c |
| Sec. 8 | "It does not require trust …"; "correctors outside it are needed only for harms to those not party to it" | O2d, O2e | See O2d, O2e |
| Sec. 9 | "the theorem's other conclusions … do not depend on it" | True but hides which ones *do* | "The results on selection of control, starvation of correction, the required rate of independent correction and the silence of moderate harm do not depend on it. Theorem 1's conclusion that no trajectory is viable, and hence the necessity in Corollary 1, do." |
| Sec. 9 | "The conversion parameters can be identified." | Contradicted two sentences later | "Under the model, the conversion parameters can in principle be recovered." |
| Conclusion | "AI makes guarding harder faster than it makes it easier unless …"; "No winner of that race has a viable trajectory that the host does not also have"; "the one course the analysis leaves open" | Not derived (O5); false under unequal exposure (O4); the analysis leaves other courses open (negating C0, χ → 0, a regulator over one jurisdiction) | Full replacement below |

**Replacement conclusion:**

> "**Conclusion.** The developers of advanced AI, and the states in which they operate, share conditions that none of them prices. Selection on who is ahead does not register those conditions. The correctors meant to protect them are part of the environment the contest selects. The independent correction needed to keep them uncaptured must rise as AI lowers the cost of control, and it keeps pace only if independent correctors adopt AI as fast as the field does. These results hold whether or not any harm can cross a critical floor. If one can, a viable trajectory needs conditions that no participant can secure alone: consequences that return; correction that keeps pace and stays independent; evidence not formed inside the contest; and rules fixed before capture. Where exposure is shared, those conditions leave every participant better off. In this sense the future of AI development is a common future [WCED 1987]. What must be agreed is not who wins, but the conditions under which anyone's winning remains viable."

**Replacement abstract** (about 200 words):

> "Frontier AI is developed in a contest among firms and among states that all depend on shared conditions, such as secure critical infrastructure, a reliable information environment and the capacity to detect and correct error, and whose leaders help build the evaluations and rules that judge the next round. We ask what this arrangement selects for. Selection on relative performance does not register conditions that all participants share, so restraint that sustains them is displaced whatever participants intend; among strategic players the same holds once there are enough contenders or enough weight on winning. A corrector that makes costs return to their source is itself part of the selection environment: control over it pays only for the largest participants, and investment in correcting it is selected against. Accounting for this second-order selection, we derive the minimum rate of independent correction that keeps evaluation uncaptured. It rises as AI lowers the cost of control, as the square root of that fall under quadratic cost. Captured evaluation can then delay an alarm until harm has passed a critical level, and can hide moderate harm indefinitely. None of this requires that harm can cross a critical floor. If it can, guaranteeing viability requires four conditions that no participant can secure alone and that, under shared exposure, leave every participant better off. We specify what an agreement establishing them must cover and how it could be verified."

---

## 10. Missing related work reviewers will expect

**AI races (formal and conceptual).**
- Han, Pereira, Santos & Lenaerts 2020, "To Regulate or Not", *JAIR* 69. This is the closest formal precedent: evolutionary game theory of AI races with safety and regulation, with regime-dependent results.
- Han et al. 2021, *PLOS ONE* (already in the bibliography, uncited).
- Cave & ÓhÉigeartaigh 2018, "An AI Race for Strategic Advantage: Rhetoric and Risks" (AIES).
- Emery-Xu, Park & Trager 2024 (*J. Conflict Resolution*).
- Stafford, Trager & Dafoe 2022, "Safety Not Guaranteed".
- Naudé & Dimitri 2020.

The conceptual opponents the paper must answer:
- Narayanan & Kapoor 2025, "AI as Normal Technology" (denies C0);
- Hendrycks, Schmidt & Wang 2025, "Superintelligence Strategy" (stability through deterrence rather than agreement);
- the "lead as safety margin" and entente arguments, cited neutrally.

**International AI governance.**
- Proposals and models: Ho et al. 2023, "International Institutions for Advanced AI"; Maas & Villalobos 2023; Trager et al. 2023, "International Governance of Civilian AI: A Jurisdictional Certification Approach"; Cihon, Maas & Kemp 2020 (centralisation versus fragmentation); Hausenloy, Miotti & Dennis 2023 (MAGIC); Veale, Matus & Gorwa 2023.
- UN: High-level Advisory Body, *Governing AI for Humanity* (2024); the 2025 UN Independent International Scientific Panel on AI and the Global Dialogue on AI Governance.
- Council of Europe Framework Convention on AI (2024).
- China's Global AI Governance Initiative (2023) and Global AI Governance Action Plan (2025).
- IDAIS consensus statements (Beijing and Venice 2024).
- For balance from the Chinese side: Concordia AI's *State of AI Safety in China* reports and the TC260 framework.

**Self-enforcing agreements and public-good technologies.**
- Barrett 1994 and 2007 (*Why Cooperate?*); Carraro & Siniscalco 1993.
- Hirshleifer 1983, "From Weakest-Link to Best-Shot". This is essential for O2: knowledge from safety research is a best-shot good, while adoption and coverage are weakest-link, and that distinction locates exactly where cooperation is necessary.
- Ostrom's design principles (already cited) map closely onto I1–I3. Say so; the polycentric framing is palatable across blocs.

**Compute governance and verification.**
- Sastry et al. 2024, "Computing Power and the Governance of AI"; Heim et al. 2024, "Governing Through the Cloud".
- Shavit 2023, "What Does It Take to Catch a Chinchilla?"; Baker 2023, on lessons from nuclear verification; Wasil et al. 2024, on verification methods for international AI agreements.

**Frontier safety frameworks and regulation.**
- Anthropic RSP; OpenAI Preparedness Framework; Google DeepMind Frontier Safety Framework.
- Seoul Frontier AI Safety Commitments (2024).
- Karnofsky 2024 on if-then commitments; METR's "Common Elements of Frontier AI Safety Policies".
- Anderljung et al. 2023, "Frontier AI Regulation"; Shevlane et al. 2023, "Model Evaluation for Extreme Risks".
- EU AI Act (Art. 55, 68, 92) and the GPAI Code of Practice (2025); California SB 53 (2025).

**Audit independence and access.**
- Already in the bibliography but uncited: Raji et al. 2022, "Outsider Oversight" (AIES); Costanza-Chock, Raji & Buolamwini 2022, "Who Audits the Auditors?" (FAccT); Birhane et al. 2024.
- Not yet in the bibliography: Casper et al. 2024, "Black-Box Access is Insufficient for Rigorous AI Audits" (FAccT); Bucknall & Trager 2023 on structured access; Clark & Hadfield 2019 on regulatory markets.

**Evidence of conversion** (already in the bibliography, uncited in v3): Wei et al. 2024 (AIES; capture mechanisms in AI policy); Ahmed, Wahed & Thompson 2023 (*Science*); Whittaker 2021; Abdalla & Abdalla 2021; Büthe & Mattli 2011 on private power in international standard-setting.

**Masking in practice.** Van der Weij et al. 2024 (sandbagging); Needham et al. 2025 (evaluation awareness); Kleinberg & Raghavan 2021 and Bommasani et al. 2022 (monoculture; both in the bibliography, uncited).

**Philosophy of modelling.** Levins 1966; Weisberg 2006; Kuorikoski, Lehtinen & Marchionni 2010; Sugden 2000.

**Antitrust and cooperation.** Hua & Belfield 2021 (*Yale J.L. & Tech.*).

---

## 11. Smaller issues

1. **The brute-force check in Appendix C is vacuous.** `figures_v3.py` runs the brute-force best response only at θ = 0.5 (ν = ω = K = ρ = 1, h = 0.5). There depletion is always dominant, so the threshold is never tested. The θ = 3 and θ = 8 lines in `checks.log` evaluate the formula against itself. The formula is correct (I brute-forced θ ∈ {3, 8}, n ∈ {2, 3, 5, 10}, λ ∈ {0, 0.5, 1, 2, 6, 10}), but the appendix sentence "brute-force best responses … agree with the dominant-strategy thresholds" is not supported by the script. Run the brute force at θ ∈ {3, 8}.
2. **Figure 2 caption.** "overtaken at t* ≈ 6.8" uses t* for the actual crossing time. Proposition 5 defines t* as the bound (9.2 here). Use t_c for the crossing, or say "(bound t* = 9.2)".
3. **Proof of Theorem 2(a).** It uses the full row sum Σ_j R_Sj < 1 (Prop. 7b), but I2 as defined (d > d*) certifies only the inbound conversion from the captured set, s_S(C) < 1. Either define d* from the full row, or add "and no domain outside C is seeded".
4. **Proposition 5(iv)** can be sharpened to an iff (O5a): if α ≥ g/2 the certificate holds for all t iff d₀ > d*(0). The stated sufficient condition d₀ > A/c_E + S is stronger than needed.
5. **Notation overloads:** κ (the shift in Def. 2, and rates κ_i); τ (liability, and τ_d, τ_r); s (share in Prop. 3, s_i(C) inbound conversion, S in Prop. 5, 𝒮 a set of domains); d (correction rate), D (development), 𝒟 (all domains).
6. **"Invariants".** In dynamical systems an invariant is a conserved quantity or an invariant set. Theorem 2's I1–I4 are constraints maintained along a trajectory. Either say "conditions that must hold invariantly", or define the term once.
7. **The host's double role.** "Capacity for independent correction" is a component of V and is also d. Either drop it from V, or model d = d(V), which would add a reinforcing loop in the paper's favour: depletion lowers correction.
8. **The floor is not absorbing** (logistic regeneration from any V > 0). See O1e.
9. **Instruments are mis-mapped.** "Rotating held-out benchmarks" address contamination and Goodhart effects, not appropriability χ. "Conflict-of-interest rules for drafters" cut conversion b, not χ. Only "interface-neutral standards" lower χ directly.
10. **"Developers fund evaluators".** Precision: "Developers fund some evaluators, grant the access on which nearly all depend, author many benchmarks and standards contributions, and increasingly supply the models that judge."
11. **Selection in an oligopoly.** Say explicitly that for five to ten firms the operative reading is imitation of practices (Schlag 1998), and that at state level only Proposition 2 applies.
12. **Smallpox.** Barrett 2007 (*Why Cooperate?*) is the better source; it was a best-shot or weakest-link good, not a commons.
13. **Statement of Contributions** repeats the Contributions paragraph. Merge them, unless IASEAI requires both, in which case shorten one.
14. **Prop. 6(iii) "moderate harm".** Note in the text that harm settling above V_min is viable by definition, so this result supports the evidence argument, not the viability argument.

---

## 12. Score and probability

- **Recommendation:** borderline, leaning weak reject (4/10).
- **Confidence:** high on the governance, mapping and philosophy-of-science points; medium on venue calibration.
- **Probability of archival acceptance as submitted:** about 20% (15–25%).
  - Sympathetic reviewers (cooperation-minded, formal-model-friendly) will like the question, the conditional style and the second-order results.
  - Policy reviewers will find Table 1 unfair, cooperation unspecified and the EU AI Act absent.
  - A philosopher or economist will find the headline over-reaching (O1, O2, O4).
  - A technical reviewer will find the "half" claim to be a curvature artifact within minutes (O5).
  - Any one of these is enough for a reject at a roughly 19% acceptance rate.
- **After the three changes below:** about 35–40%.
- **After all ranked revisions:** perhaps 45%. The remaining risk is that the formal tools are standard and nothing is calibrated, which the paper can mitigate by positioning but not remove.

---

## 13. The three changes that would most increase resistance to refutation and persuasiveness

### 1. Restate what is proved: two tiers, robust necessity, and the conditions on the headline. *(O1, O2a, O4, Section 9.)*
- Put the C0-free second-order core first. It is novel, robust, and something a hostile reader cannot refute without rejecting standard tools.
- Make "no viable winner" a second tier conditional on C0. Anchor C0 in the frontier safety frameworks and national frameworks of all three blocs. Make it existential over harm classes, with a testable falsifier.
- Call the invariants necessary in the *robust* sense and say so.
- Add the unequal-exposure dilemma remark and qualify the payoff clause of Theorem 1.
- Add the C0-free route to the cooperation conclusion through the contestability premise.
- Rewrite the abstract, the introduction's last sentence, the method paragraph and the conclusion with the replacement texts above.

*Effect:* every remaining claim is either proved or explicitly conditional, and the cheapest refutation, denying C0, no longer reaches the paper's core or its cooperation conclusion.

### 2. Rebuild Table 1 around the strongest version of each remedy, and add the missing remedies. *(O3, O6, Section 5.)*
- Reframe Table 1 as "what each remedy supplies, what it leaves, what only an arrangement across parties adds".
- Add technical safety and resilience, binding regulation in a large market, public institutes with statutory access, compute governance, and existing international institutions, each mapped to invariants.
- Engage "lead as margin" and the "normal technology" view by name.
- Remap masking to the mechanisms evaluators recognise: access windows, under-elicitation, evaluation awareness, loss of data access. Justify the averaged alarm or move the problem to S.

*Effect:* reviewers who work on these remedies see their work as part of the solution the paper completes, not as a list of failures. The paper's thesis that cooperation is the missing piece becomes the conclusion of a fair comparison.

### 3. Give "cooperation" operational content and handle the state level honestly. *(O2b–e, O5, O8, Section 8.)*
- Add the definition (coverage, content, verification) and the five-row table (invariant → what must be agreed → by whom → verified how → existing seeds in the US, China and EU).
- Rewrite Corollary 1 to distinguish carriers, rule-makers and states. State the two-state condition λ > θ − 2, and name the forms of cooperation it implies: shared risk assessment and de-escalation.
- Replace "enforces itself", "does not require trust" and "only for harms to those not party to it" with the texts in O2.
- Generalise Proposition 5 to cost curvature k, and add the remark on who adopts AI. That turns the AI claim into a concrete instrument: fund AI-equipped independent evaluation, indexed to the field's capability.
- Use the balanced precedents paragraph and the political fixes in Section 8.

*Effect:* "cooperate on what?" gets an answer derived from the model. The paper stops reading as advocacy of a world authority, which matters to both US and Chinese reviewers, and the one AI-specific result becomes robust and actionable.

All three changes fit in the three or so unused pages and can be made before the 5 October deadline. Most of the text is supplied above; none of it requires new experiments.

---

## 14. Notes for the authors (outside the review)

- **Page budget.** The main text ends about a third of the way down page 7, so roughly 3.5 of the 10 pages are unused. That is enough for the cooperation definition and table (0.5 page), the expanded Table 1 (+0.3 page), a related-work paragraph on races and international institutions (0.4 page), the structural-assumptions list and robustness remarks (0.4 page), and the state-level paragraph (0.3 page).
- **The bibliography already holds verified, relevant entries that v3 no longer cites:** `wei2024`, `ahmed2023`, `raji2022`, `costanzachock2022`, `birhane2024`, `whittaker2021`, `abdalla2021`, `euaiact2024`, `han2021`, `narechania2024`, `kleinberg2021`, `bommasani2022`, `buthe2011`, `scheffer2009`, `li2026preference`, `awuni2026`, `zatuchin2026`. The last two are recent unreviewed preprints. They bear directly on C4, and v2 cited them. Dropping the one that finds no own-model premium, while keeping self-preference evidence, would look selective to a reviewer who knows that literature (O7).
- **Missing bibliography keys** in v3 (rendered "??"): `alchian1950`, `askell2019`, `aubin1991`, `barrett2003`, `bengio2025report`, `bletchley2023`, `bolton2012`, `espeland2007`, `frank1985`, `hardin1968`, `hirsch1976`, `hurwicz2008`, `krakauer2009`, `kwa2025`, `laffont1991`, `lehmann2008`, `lizzeri1999`, `olson1965`, `ostrom1990`, `panchanathan2004`, `rockstrom2009`, `schaffer1988`, `schlag1998`, `statecouncil2017`, `teece1986`, `vegaredondo1997`, `wced1987`, `whitehouse2025`, `yamagishi1986`.
- **Facts to verify before using the suggested texts:**
  - the wording and date of the 2025 US statement at the UN on global AI governance;
  - the 2025 UN resolution establishing the scientific panel;
  - the IDAIS statement wording;
  - China's December 2024 industry safety commitments, if cited;
  - the date of the DSA Art. 40 delegated act.

  I am confident of the Bletchley endorsements, the Paris 2025 non-signatures by the US and UK, the two 2024 General Assembly resolutions adopted without a vote, the EU AI Act articles cited, SB 53 (September 2025) and the GPAI Code (July 2025).
- **On Ren's aim** ("cannot be simply refuted by intellectuals"): what makes a conclusion hard to refute is not its strength but how exactly it matches what is proved. The v3 core is close to that standard; the headline is not. The changes above move the headline to the core rather than weakening the thesis. Cooperation remains the conclusion, now stated as what the model requires, under which conditions, and with what content.
