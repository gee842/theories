# V7 editorial and synthesis review

V7 is suitable for private specialist criticism with its open questions and known findings attached. It is not ready to be presented as a finished public theory until its formal requirements, decision branches and comparison of alternatives agree. This review concerns the current text, not the merits of Ren's normative commitments.

## Concentration and narrower objectives are different claims

The parenthetical in `src/core/10_s01.md:7` identifies a game that concentrates with one in which reinvestment's relative return exceeds its common return. Those are different conditions in the paper's own models. With a fixed prize, beta = 0.5, r = 1, d = 0.2 and discount = 0.9, the structural gain is 0.5, the gap shrinks by a factor 0.9 each period, and the relative continuation price is about 0.474 while the common price is zero. Equal standing is stable despite the objective becoming narrower. The fresh mathematics reviewer independently checked this example and the formal distinction.

This matters because the definition is used to decide which games fall under broad E1. The author can prefer excluding AI from concentrating contests without identifying every positive relative continuation return with concentration. Use separate operational conditions, and say when the proportional-prize special case makes them coincide. Severity P2; a correctable statement of scope, not a failure of the narrowed continuation proposition.

## The zero tax withdrawal row contradicts the main recommendation

At `src/core/c0_s12.md:25`, item 7 correctly distinguishes a negative safeguard tax from a zero one: a negative tax selects for the safeguard; zero makes it neutral, so withdrawal at zero also needs evidence that the safeguard persists. But the C9a row at line 68 says zero or negative tax withdraws item 7 without that additional condition. `src/core/60_s6.md:101` similarly says admission constraints last until the tax is zero or negative.

At zero payoff difference, replicator selection leaves an existing unsafe share unchanged. For example, an unsafe share of 0.2 remains 0.2 once sanctions are withdrawn if the two variants have equal baseline payoffs. There is no automatic repair. The main text already supplies the appropriate rule; propagate it into the operational summaries. Severity P2.

## Reader readiness and the status of the evidence

The new entry, claim tags, source dates and counterexample catalogue are substantial improvements. The strongest repairs explain what would defeat the argument, and the manuscript distinguishes its empirical diagnosis from theorems in specified models. Its length is appropriate to assess as a research manuscript, not as a short article; a specific publication target would need a separate editorial decision.

The remaining readiness problem is not that all empirical cruxes must be resolved before a conditional working paper can circulate. It is that some downstream sentences still state necessities, exclusions or safety properties that the models do not establish. A reader should not have to locate a contradictory qualification in another volume to know which claim is intended.

## Audit basis

The 50 source and checking inputs in V7's saved input manifest match the final build. Its recorded numerical suite passed 231 counted checks across 43 blocks; this review does not treat those checks as certification of all theorem scopes. The team wrote fresh counterexamples rather than rerunning the unchanged full suite for reassurance. Manuscript changes are outside this review request; all feedback is saved separately.
