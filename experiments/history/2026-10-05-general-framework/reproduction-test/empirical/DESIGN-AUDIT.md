# Assignment audit added after the frozen result

Date: 2026-10-05. This clarification changes interpretation, not the frozen endpoint, estimator, or numerical outcomes.

Before reading outcomes, the archive identifiers showed 31 actual sessions with a homogeneous treatment in each. The protocol therefore froze session-level aggregation and an explicitly conditional causal interpretation, despite the article's statement that groups were randomly assigned to treatments.

After completing the declared analysis, we inspected the authors' [S2 Protocol.doc](https://osf.io/download/p3bs7/) to clarify this mismatch. The experimenter setup section directs staff to check the **Treatment Order Log** and load the appropriate treatment for the day/session. The participant instructions explicitly describe random assignment into groups, whose members then remain together. This confirms session scheduling; it does not document how session treatments were assigned. Neither the actual order log nor its randomization procedure is verified here.

The distinction matters: random membership within a session does not make that session's treatment random. A causal reading requires that treatment order or participant assignment to session satisfies the appropriate exchangeability assumptions. The cluster-aware t interval only addresses within-session dependence. It does not remove temporal, recruiting, experimenter, or session-allocation confounding.

Accordingly, report the result as a **facilitation intervention contrast on retained sanction permission**, with a causal interpretation conditional on credible session allocation. Do not describe the reanalysis as having verified a randomized group-level causal effect. The result is not invalidated merely by common treatment within a session; cluster randomization could be valid, but it has not been established from the inspected records.

The downloaded source has SHA256 `0f7517a8739a54e62c919460043b389a0c262c6a6e810804edb5004a1138cca5`. `data/Protocol_author.txt` contains only two targeted design excerpts extracted from the binary document's text stream. An attempted automatic document conversion did not produce readable text and was replaced by these clearly labeled excerpts. No experiment setup commands embedded in the document were executed.
