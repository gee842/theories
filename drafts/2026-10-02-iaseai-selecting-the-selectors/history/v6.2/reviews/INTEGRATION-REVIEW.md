# V6.2 integration and verification review

Reviewed on 4 October 2026. This report covers the argument's status across documents, the empirical test programme, preservation of the author's directions, and what the automated checks establish. It supplements the separate formal, systems and alignment, and evidence and governance reviews. The review does not change the manuscript.

## Main assessment

V6.2 is a substantial improvement in the discipline with which the project distinguishes results, premises, conjectures, numerical examples and values. Its strongest contribution is a connected set of conditional mechanisms and a programme for testing whether their interfaces matter in the world. Neither a unified model of the whole argument nor an empirical demonstration of the present trajectory has been supplied. The text often says this clearly. Its weakest passages temporarily drop these distinctions, especially when moving from mechanisms into the conclusion and activation or release rules.

The appropriate revision is targeted. Preserve the corrected price-of-standing distinction, channel-specific levers, the conjectural status of C0, the separation of E2 and E3, and the explicit accounting of a cooperative arrangement's own hazards. Repair the few mathematical and logical bridges that still carry more weight than their support.

## I1 The test runner does not fail on all reported numerical failures

**Priority P2. Confidence high. Category verification.**

Locations: `checks_v62.py:65–78`, the main execution and final assertion counter at the end of the script, and `SUPPLEMENT.md:1282–1284,1290–1329,1347–1349`.

The reported 188 assertions are actual checks, but they are not a blanket regression gate for every computation printed by the 40 blocks. Twenty-three original `check_*` function bodies contain neither `expect` nor an `assert`. Nine receive additional asserting extensions later; several of their original comparisons remain print-only. Fourteen block names have no such asserting extension: FB, TC, TH, CB, RH, FS, BI, WG, PE, FD, LG, T3, AC and FA. This does not mean all fourteen contain a failed comparison, or that all should be turned into tests without deciding what counts as success. It means exit status does not certify all their displayed results.

A minimal fault-injection experiment confirms the distinction. In memory only, the review replaced FB's agreement increment with `agree += False`, and ran only FB. The output was:

```text
agreement 0/200000
=== assertions: 0 passed, 0 failed (default sizes)
```

The process exited 0. The experiment changed neither the manuscript nor its checker. Its log and exact mutation are in `harness-audit/injected-failure.log` and `harness-audit/audit.json`.

**Impact.** A later regression in an inherited block can leave the aggregate success message intact. A reviewer should not interpret the 188 count as 188 independently proved claims, 40 fully guarded blocks, or a complete certification of all computed examples. The Supplement already disclaims proof and empirical certification; that disclaimer is correct and should be retained.

**Repair.** Add an `expect` for each comparison intended to gate the build, starting with `agree == N` in FB, zero mismatch counts in TC and LG, and the explicit truth conditions of other print-only comparisons. Leave exploratory tables labelled diagnostic. Add a small harness self-test that injects a known false result and requires nonzero exit. The purpose is to verify failure reporting, not to duplicate the mathematics.

## I2 The necessity of shared understanding is a thesis beyond Lemma 3.11

**Priority P2. Confidence high about the logical scope, not a rejection of the author's philosophy. Category argument.**

Locations: `THEORY.md:281–285,293–300,1185–1187,1223`; proof at `SUPPLEMENT.md:302–304`; provenance at `CLAIMS.md:426` and the entry D36 in that table.

Lemma 3.11 proves a useful selection result for a costly trait whose benefit is equally distributed. It also explicitly permits transmission and rules that change relative payoffs. From this, the manuscript moves to a stronger statement: because a global irreversible failure cannot teach its survivors, anticipation on an accurate model is the only timely route, and shared understanding that we are one is a long-term requirement when growth and change are favoured.

The first implication is valid in its narrow sense: learning *from that terminal failure after it occurs* cannot prevent it. The stronger necessity does not follow. Rules can be learned from reversible precursors, local experiments, historical analogies or simulation; they can be maintained by sanctions and individually advantageous service arrangements. Actors can comply with a useful safety rule without sharing a comprehensive understanding of the whole system. A rule that changes relative payoffs is expressly outside the lemma's adverse-selection premise. The lemma contains no theorem that all such rules require common adoption of the proposed understanding.

This is not an objection to retaining Ren's words or to the pragmatic value of a shared model. It is an objection to calling that stronger necessity the lemma's formal content. If a system 'understands' solely by satisfying the institutional definition in §3.7, the claim instead risks becoming definitional. If cognitive understanding is also necessary, the required breadth and level of that understanding remain unspecified. The text need not, and does not explicitly, require every individual to comprehend the whole system. It already acknowledges local experimentation; what is missing is an argument that such routes cannot sustain the required institutions without the stronger shared understanding.

**Repair.** Preserve the author's statement as an explicit philosophical and institutional thesis. State separately the proved claim, the anticipation argument, and the conjecture that shared understanding is required to establish and sustain the relevant rules under open-ended change. Identify whose understanding, of what, and over which time horizon is required. A concise formulation is: 'The lemma explains why shared understanding and rules that change relative incentives are candidate routes; it does not establish that a shared global model is necessary for every viable arrangement.'

The provenance check found the 'favoured' formulation in the planning record as the author's stated choice, and CLAIMS correctly records that choice. A revision should correct its inferential status without silently replacing it with a different claim.

## I3 The test register is a research design outline rather than an operational preregistration

**Priority P2. Confidence high. Category empirical identification.**

Locations: `THEORY.md:775–780`; `TESTS.md:11,114–136,140–178,192–202`.

The register names promising observables and rival predictions. It also explicitly admits that loop gains are unestimated and readiness dimensions have not been measured. These admissions are strengths. Nevertheless, 'registered tests', 'registered indicators', 'certified row sums' and 'the dwell time' can sound like executable decision rules before the relevant estimands and measurement procedures exist.

For Test E in particular, an intervention having effects in more than one signature group does not uniquely identify the proposed interlock. A conventional causal network with several mechanisms and ordinary spillovers can also produce cross-effects. A disclosure duty can change reputation, financing, entry costs or selection, and thus need not be a clean intervention on conduct alone. Conversely, a true cross-effect can be small, delayed or masked by offsetting responses. A null estimate is not automatically the absence of the mechanism.

The same difficulty appears in the requirement that signatures persist 'unchanged over the dwell time'. The threshold model supplies a dwell time given its parameters and state. The empirical register has not supplied an independently estimated institutional dwell time, an equivalence margin for 'unchanged', or a rule for treating missing access as missing evidence rather than safety or capture.

**Repair.** Keep the present tables as a mechanism-testing agenda. For each first implemented test, register the following before observing its outcome:

1. The population, unit of observation, selection rule and observation horizon.
2. The intervention and the measured first-stage changes in the model parameters.
3. The primary outcome and its quantitative link to the model variable.
4. The rival causal model, including possible cross-effects and anticipation.
5. A minimum consequential effect, an equivalence margin for a null, and the uncertainty procedure.
6. The dwell horizon, fixed independently of the outcome being explained.
7. Treatment of strategic missingness, measurement changes, substitution and spillovers.
8. The precise inference to be withdrawn on a positive, negative or inconclusive result.

The first Test E should compare estimated cross-derivatives and their direction, lag and size under explicit rival models, rather than 'more than one group changes' against 'only one changes'. Do not require this entire programme before publishing the theoretical paper; require it before claiming that a pilot has confirmed or refuted C0, or using that result to activate a consequential policy.

## I4 The short reading path compresses conditions beyond safe readability

**Priority P3 advisory. Confidence high. Category presentation. This is optional entry-point advice, not a requirement to shorten the theory of record.**

Locations: `README.md` reading paths; `THEORY.md:5,17–31,57–69,1223–1227`; build report `reviews/xref-review.log`.

The assembled build counts 56,194 core words, 58,890 Supplement words and 20,573 Discussion words, excluding references and using the builder's formula-stripping convention. This is approximately 135,657 words before the registers. Length is not itself a defect: the recorded author direction explicitly says to complete the theory before compression and not let page limits govern it.

The problem is the density of the advertised short route. The English abstract is one long paragraph combining local stability, common and relative continuation returns, correction rates, enforcement, asymptotic survival, masked divergence, ontology and three policy tiers. Readers must hold several distinct domains of validity in working memory before the definitions exist. The Chinese guide is substantially more natural than mechanically translated prose, and 母体 is consistent, but technical clauses such as '决定性增长不及存量比例者' still require the formal text to decode. A bilingual keyword score checks vocabulary, not equivalent qualifications or comprehensibility.

**Repair.** Keep the full files as the authoritative research dossier. Add a genuinely short entry point only after the substantive repairs: question, three main established results, three major open bridges, and what each tier recommends. In the abstract separate results from diagnosis and judgment into short paragraphs. Introduce 'won share' with one plain-language sentence before using it as the scissors' pivot. Preserve the author's expressions as quotations or declared commitments; distinguish their force from a theorem's force.

## Preservation and provenance sample

The review checked the fourteen-loss table in `LEDGER.md:312–333` against its stated homes and directly compared a targeted sample with the source records. This is a sample, not a fresh adjudication of all 1,060 sentences in the preservation ledger.

| Item | Source inspected | Assessment |
|---|---|---|
| Growth and the mind | `sources/16-claude-code-directions/2026-09-25-the-mind-not-the-approach.md` | The underlying ruling is present. 'Growth is not the danger; the mind is' is a rendering of a longer English statement, and CLAIMS D13 correctly marks that fact. |
| AI as planetary technology and broad E1 | `sources/16-claude-code-directions/2026-09-26-planetary-technology-and-the-literature.md` | The broad scope is the author's. The narrow list as an ordering of first steps originated as the assistant's reading; the register correctly distinguishes it. |
| Falling behind a cancer-like winner | `sources/16-claude-code-directions/2026-10-03-v4-direction-cooperation.md` | The Chinese ruling supports the restoration in §3.8; the English remains a rendering. |
| E2 and E3 remain distinct | Same 3 October record | Explicitly supported by the author's rejection of merging stop and slow. The review's recommendations preserve both. |
| Decay as growth | `drafts/2026-10-02-friend-conversation/transcript.md:483` | Speaker B explicitly states this. The manuscript discloses the provisional identification of Speaker B as Ren. |
| Identity with the process | Same transcript around `:557`, and `CLAIMS.md` D34 | The distinctive identity formulation is restored; removal of opening speech repetitions is recorded. |
| Favoured growth and change | `v6-planning/P5-ren-corpus-generators.md:137`, CLAIMS D36 | The wording choice is recorded. This review does not claim to have independently recovered the original audio or message behind that planning note. |

The register's distinctions between Ren's words, AI drafts he adopted, model renderings awaiting confirmation and literature are valuable. No sampled attribution defect justifies undoing these restorations. 'Restored in your words' should still be read with the register's own qualifications: many English and Chinese sentences are renderings, and some corpus phrases are explicitly not the author's original drafting.

## What the build checks establish

An isolated copy was assembled and checked to avoid overwriting the reviewed release. The assembly and xref checks passed, and every compared assembled file and keyed source was byte-identical to the reviewed input. The isolated xref initially failed because `refs_v62.py` imports the bibliography from the sibling `v6/THEORY.md`; supplying that repository dependency made the run pass. This was a limitation of the initial isolated copy, not a manuscript build failure. A standalone release should document or bundle that dependency.

The checker reported 93 core declarations and 35 Supplement declarations, 103 cited works in THEORY, 89 in SUPPLEMENT and 132 in DISCUSSION, with matching bibliography counts. It found all 32 required core items and nine Chinese guide items matching the nine English argument items under its vocabulary criterion.

The register-only citation warnings are informational under the current checker. Some entries are parser artefacts, while others are actual works absent from the three bibliographies. Their presence is not a contradiction of 'xref passes'; it is a limit of what that pass means. A public release should either give registers their own bibliography or make their references resolvable directly.

The source manifest, isolated-build comparison, main numerical log and fault-injection evidence are retained in this review directory. A clean build validates assembly, numbering and the implemented syntactic checks. It does not validate the semantic use of a cited source, equivalence of English and Chinese qualifications, completeness of a proof, or the policy applicability of a numerical example.
