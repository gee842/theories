# Independent review of source scope and the constitutive bridge

5 October 2026. Review status: passed after two precision repairs to the bridge. No reference source was edited, imported, or built.

## Material examined

I read `source-manifest.json`, `axiom-source-excerpts.md`, `verify_root_scope.py`, and `constitutive-bridge.md`; then read the relevant original definitions directly. The original repository instructions were read, including the prohibition on subagent builds. All 11 source-file SHA-256 values in the manifest match the files currently present.

Original source inspection included:

- `formal/SSBX/Foundation/Wen/Kernel.lean`, its aliases at lines 124–129, and its concrete field and motion definitions at lines 143–157.
- `formal/SSBX/Foundation/Atlas/Yi/Classical/Cells/R7.lean`, especially the direct Yao XOR table, componentwise hexagram XOR, R7 product XOR, and origin.
- `formal/SSBX/Foundation/Atlas/Yi/Classical/Core/Yi.lean`, the Yao aliases.
- The quoted root-DAG and FullGUT passages in the source excerpt bundle.
- `/Users/ren/theories/sources/06-zhishan/shengsheng/生生不息论v2/PLAN-v2.md`, sections 2 through 7, directly rather than relying only on its English summary.

The last source has SHA-256 `e5499c4dfbb387f65bab53a465ff953631d35c997995d3efc4615f7d0a0bf94d`. It expressly describes a normative process–relation philosophy and middle-range theory; disclaims a complete physical ontology and uniquely deduced morality; declares its public commitment; distinguishes six protection functions; and states the totalizing mechanism and downgrade conditions. The bridge accurately reports those passages. The term "canonical" here identifies this chosen v2 formulation, not a claim that every historical manuscript or every formal module makes identical claims.

## Wen motion: the period-two conclusion is exact

The alias `cell128Xor` resolves directly to `SSBX.Foundation.Bagua.R7.R7.xor`. That function performs componentwise XOR on six Yao components and the final Boolean trace component. The field is the product of these seven binary coordinates. The concrete `c_motion` changes the first Yao from yang to yin and leaves the other six coordinates at their identity values. Hence it is nonzero.

For every field state \(s\), let \(c=c_{\mathrm{motion}}\). Then

\[
\mathrm{motion}(\mathrm{motion}(s))
=(s\oplus c)\oplus c
=s\oplus(c\oplus c)=s.
\]

Since \(c\ne0\), \(\mathrm{motion}(s)\ne s\). Every orbit therefore has **exact period two**, not merely period dividing two.

Every `ZhongOrbit` in this module obeys its stated `step` field, so

\[
o.\mathrm{states}(n+2)=o.\mathrm{states}(n),
\qquad o.\mathrm{states}(n+1)\ne o.\mathrm{states}(n).
\]

Such an orbit has exactly two distinct field configurations. The 128 field states partition into 64 two-cycles.

The external verifier's mask `(1,0,0,0,0,0,0)` matches the inspected source coordinate order. Its extra exhaustive check of all 127 nonzero seven-bit masks is valid. As an independent encoding, I enumerated source-level `yang`/`yin` six-tuples and the Boolean trace, directly toggled the first Yao, and confirmed all 128 states return on the second step, with 64 distinct two-cycles.

This is a genuine counterexample to reading this particular `motion_self_consistent`/`shengsheng_buxi` result as proving infinitely many distinct field configurations. It is **not a contradiction of the actual Lean statements**, which assert adjacent change and repeated non-extremity. It does not refute infinite event occurrence, potentially growing history records, other dynamics on other carriers, the broader R-family representation results, or the whole philosophical corpus. No fresh Lean compilation or kernel trust audit is claimed.

The source's own comments at lines 214–219 explicitly limit the post-Cayley conclusion to the algebraic collapse of the fixed-point dichotomy. The result should be presented as an interpretation boundary, not as discovery that the whole project is a two-state system.

## Deletion-test quantifiers

The bridge correctly separates

\[
\forall i\,\exists M_i:
G(M_i)\land\neg G(\mathrm{del}_i(M_i))
\]

from the stronger universal necessity claim

\[
\forall M:\ G(M)\Rightarrow\text{all named functions are present}.
\]

The first can show that no named function is uniformly dispensable. It cannot show that every successful case requires all functions. The distinction between a function and one redundant implementation of it is also necessary and correctly stated.

One repair was needed and has been adopted: before describing

\[
W_G\cap\Pi_{\neg i}=\varnothing
\]

as a **loss** caused by deletion, assume \(W_G\ne\varnothing\) before deletion. Otherwise an originally impossible objective satisfies the empty-intersection condition too. The unchanged-law condition is essential: if deletion changes transition laws, observations, timing, or disturbances, a new model and controller interpretation are required. The revised bridge states this.

## Public commitment and conditional restriction law

The public protection commitment is faithfully attributed to the source as an explicit normative premise. The source itself allows that a consistent dominator may reject its initial moral commitment and does not claim to force concern by logic. Thus the bridge correctly avoids presenting the six protections as universal physical ingredients of any process whatsoever.

The conditional monotonicity claim is sound under a shared objective and comparison contract: removing admissible protected-controller strategies, removing information without compensation, or enlarging the adversarial outcome set cannot enlarge the protected controller's winning possibilities. A strict loss requires removal of all substitutes for at least one formerly attainable objective. Power concentration alone does not meet that stronger condition.

A second clarification has been adopted: removing **adversarial harmful actions** may help the protected controller, whereas removing that controller's optional actions cannot improve its existential winning set under unchanged outcome laws. These changes have opposite directions and must not both be described merely as "restriction." The revised bridge distinguishes them.

The causal arrows from local success to rule power, from rule power to restriction, and from restriction to irreplaceable loss require their own substantive evidence. The mathematics establishes the last implication under the specified restriction contract; it does not establish the prevalence or inevitability of the whole institutional chain.

## Review result

The source finding and revised bridge are sound at the stated scope. They support an exact boundary between recurring modeled motion and novelty, between distinct protection concerns and universally necessary ingredients, and between a conditional restriction theorem and an empirically confirmed universal social law. No result here establishes a complete physical ontology or an assumption-free normative foundation.
