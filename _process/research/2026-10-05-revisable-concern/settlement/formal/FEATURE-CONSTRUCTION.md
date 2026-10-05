# A bounded construction of a new discriminating feature

5 October 2026. A separately scoped refinement of the finite audit in [the integrated process](REPORT.md). This constructs a feature unavailable among the initial primitives. Its grammar, finite domain and independently labeled relevance test remain supplied. It does not derive ethical significance or unrestricted novelty.

## The finite problem

The initial representation has three binary measurements x,y,z. The finite domain contains all eight possible input rows. The model posits a noninjurious assay for a contextual relevance label l: whether the specified condition for one declared reason is present. In this authored specimen, its supplied table is l=x XOR y. The learner receives these supplied assay-table labels, not an XOR feature primitive or the expression generating them. No physical assay has been performed and these are not empirical observations.

The representation grammar allows a disjunction of at most two conjunctions, each using at most two literals from x,not-x,y,not-y,z,not-z. The learner constructs the syntactic candidates from those six literals. Its complexity measure is the total number of literal occurrences. Candidates are filtered first against the four discovery rows on which z=l, then against the four held-out validation rows on which z differs from l. Here independent validation means disjoint from discovery and not used to fit the first-stage candidates; it does not mean independently observed empirical evidence. The second set covers the entire remaining finite domain; it is not a small held-out sample claimed to establish unbounded generalization.

On the discovery rows alone, the one-literal identity proxy z fits perfectly. It fails every validation row. No primitive measurement or its negation fits all eight labels. A minimum-complexity surviving expression has four literals and computes

\[
(x\land\neg y)\lor(\neg x\land y).
\]

The finite checker constructs this expression class by enumeration, verifies the minimal literal count, and verifies all eight outputs. Thus the new feature is assembled from the supplied grammar and supplied assay-table labels in this authored example; the procedure is more than adding an already supplied transfer edge. The resulting classifier can identify a new case with z=0 as satisfying the same declared condition as an anchor with z=1. The label's normative relevance still comes from the independently defended reason specification.

## Cost and interface with the same selected process

There are finitely many syntactic candidates and eight assay labels. Let actual assembly cost be kappa>0 per candidate, evaluation cost epsilon>0 per candidate-row evaluation, label cost gamma>0 per assay, and replay cost rho>0 per declared graph-rule check. The exact construction-and-replay bill is

\[
u_{feature}=8\gamma+\kappa N_{candidate}+\epsilon N_{eval}+\rho N_{replay}.
\]

Charge this to u in a=a_0+u+h, before the commercial receipt. For the three-node, three-rule witness, two parallel closure rounds require six rule checks. The numerical refinement has gamma=1/32, kappa=1/(4N_candidate), epsilon=1/(4N_eval), and rho=1/24. Each of the four components costs 1/4, so u_feature=1 including assembly and replay. These positive technology prices are assumptions, not empirical estimates. They are chosen to fit the already explicit u=1 audit allowance. The refinement therefore preserves the same a=3, receipt comparisons, protection prices, and reserve invariant. If a real construction exceeds the allowance, the theorem must be rechecked using its larger actual a; no claim of free representation learning is made.

Once the verified expression determines which finite cases meet the declared reason condition, the current certificates and rooted closure are computed as before. A contradiction in the independently validated condition defeats affected certificates and triggers the same selective retraction. Validation of a descriptive label is not proof that the chosen condition exhausts the relevant ethical facts.

This refinement settles a limited representation-construction question: a process can build and validate a useful composite feature that was absent as a primitive and then pay for its consequences in the same economy. It does not establish discovery outside this finite grammar, reliable learning from biased or sparse labels, creation of a new ethical reason, or independent empirical support for the commercial prices.

The [feature checker](check_feature.py) records the candidate count, actual evaluation count, exact costs, selected feature and all eight predictions in [feature-results.json](feature-results.json). The main game checker does not silently include this refinement; its interface is the stated unchanged audit bill and outputs.
