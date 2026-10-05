# What the existing root actually entails

Read-only source audit, 2026-10-05. This memo audits the bridge from the canonical root to indefinite generation. It does not edit or rebuild either source repository. Source paths, exact excerpts, and SHA-256 values accompany it in `axiom-source-excerpts.md` and `source-manifest.json`.

## Determination

The corpus contains three different root claims, with different proof obligations. They should not be merged.

1. **An articulation root:** distinctions and compositional structures support formal representation. Substantial finite and encodable representation theorems exist. The latest formal claim ledger explicitly leaves the unrestricted semantic claim open.
2. **A generative structure:** a situation has structurally constrained legal transformations, with situated criteria for openness, closure, response, revision, and protection. This can support universal constraints and conditional characterizations. It does not by itself assert that the conditions for continued generation always obtain.
3. **A global inexhaustibility claim:** the universe's unfolding does not cease. A canonical primary text asserts this explicitly and distinguishes it from destructible local openness. The assertion is not derived there from the articulation or transition structure; calling unfolding the name of the process does not supply a nontermination proof.

These are compatible research directions, but neither the first nor the second currently discharges the third. This is a precise missing inference, not a dismissal of the theory because it does not fix every physical detail. A genuinely universal constraint theory can leave many mechanisms unspecified.

## Strongest faithful core, with claim types retained

The following is an audit reconstruction, not a replacement axiom system secretly attributed to the author.

| Core commitment | Source | What it gives | What it does not give |
|---|---|---|---|
| An assertion or articulated distinction distinguishes something. 間 is the name given to this relational opening. | Primary `03_一、间.md:3–11`; canonical README:53–55,362–365 | A constitutive description of articulation, if this usage of 間 is accepted. | Existence of a later event, indefinite activity, or inexhaustible physically realizable novelty. |
| Continuation has the form `x ⊕ i`, with a legal `i` constrained by the state's structure, accumulation, situation, and relations. | Primary `03_一、间.md:13–25`; README:57–65 | An interface for describing transformations and rules of admissibility; arbitrary imagined changes need not be admitted. | A specified law determining which transformations exist, their probabilities, their costs, or which ones occur. |
| Transformations can be partial and order-sensitive; exhausted local states can have no continuation; rest need not be closure. | README:59,369–374 | Important distinctions among unavailable actions, identity actions, order, and exhaustion. | A theorem that the whole process can never exhaust. The empty-interval and empty-set notions also need distinct types in an exact formalization. |
| Openness combines 未, 可, 应, 转, and distinguishes protective from destructive closure. | Primary `06_四、开闭.md:3–26`; README:79–97,406–421 | A richer object of protection than option count, activity, or monotone complexity. | Sufficiency of separately available capacities for one joint indefinitely executable policy; a measurement-free empirical theorem. |
| Calibration must confront consequences, other agents, alternatives, and revision. | README:115–119,294–297 | Conditions for responsible situated diagnosis and correction; the corpus explicitly admits calibration failure. | Guaranteed convergence of calibration or access to a complete model. |
| The six public protection functions and anti-domination commitments apply to affected centres. | README:303–315 | A declared normative programme with mechanisms and falsifiers. | Derivation of public care from nontermination alone. The v2 text explicitly refuses that derivation. |

The phrase “structurally constrained” is not empty, but it is a schema until the constraints are independently specified. Merely relabelling a successor relation as the set of legal intervals is representationally possible for every transition system; therefore additional substantive content must do the work of excluding cases or predicting different outcomes. That content can be a constraint rather than a unique equation of motion.

## The global assertion and its exact gap

Primary text: `/Users/ren/repos/生生不息/史料/生生不息论_三本文完整版/04_补篇二_间生论_主篇/15_十三、行仁要善_alignment_之真义.md`.

- Lines 30–32 assert that 間生 is not a thing and cannot perish as a thing does; the universe's unfolding is not ended by one thing's destruction; 間生不息 is described as the name of process itself, rather than a closable system.
- Line 34 explicitly grants that particular openings, situations, species, civilizations, and persons' capacities can be destroyed.
- Lines 36–39 explain why this global assurance does not make local protection unnecessary.

The modest claim, “the destruction of one local form need not end all unfolding,” is readily compatible with transition systems containing other continuing processes. The stronger claim, “the whole process necessarily remains generative forever,” needs a global extension law. The first is not the second. In particular, “not a persisting object” does not entail “cannot terminate”: an event or process can have finite duration without being a persisting object of the kind rejected by the ontology.

There are two readings of the stronger sentence:

- If “process” is **defined** to mean indefinitely continuing process, the conclusion follows definitionally for that concept. The proposition that actual reality is such a process remains a substantive premise.
- If “process” includes finite processes, the conclusion does not follow from being a process, being relational, or being internally generated.

The same scope issue appears within the primary openness chapter: `06_四、开闭.md:38` uses an all-places/all-times/all-foci formulation, while lines 21–22 and the later global/local passage allow real closures. A faithful formalization must make the protected or global field explicit. It should not silently choose the strongest quantifier and then call allowed local collapse a refutation.

Two useful logical separations are rigorous:

**Finite-past separation.** For any finite eventful record `0,1,…,H`, a successor structure can agree on every observed step and stop at H, or agree and continue `H+1,H+2,…`. Each has distinctions, internal state-dependent transitions, and a consistent causal record. Therefore a finite record plus that bare interface does not logically entail indefinite continuation. This does not claim that the stopping structure is physically realized or that it satisfies the separate global-inexhaustibility postulate.

**Continuation/novelty separation.** A two-state alternation continues forever but visits only two states; `n ↦ n+1` continues forever and visits infinitely many states. Both have distinctions, definite endogenous successor laws, and no terminal transition state. Thus serial continuation does not entail infinitely many distinct configurations. An independently meaningful notion of novelty can be still stronger than distinct state labels.

These separations leave open genuine universal laws restricting both systems. They establish only that the specific stronger conclusion needs an additional bridge.

## A concrete reach check on the inspected Wen Kernel theorem

This is a finding about a specific existing formal witness, **not** about every module of the latest R-family doctrine. The repository's `AGENTS.md` points to `wen-substrate/00-README.md`, `08-obligations.md`, and the claim-status ledger as latest doctrine. It treats older foundations as historical layers. The present canonical theory summary nevertheless cites a Lean no-telos result in its account of continued generation, making its exact conclusion relevant.

In `/Users/ren/repos/生生不息/formal/SSBX/Foundation/Wen/Kernel.lean`:

- Lines 143–157 define `Field = R7 = (Z/2)^7` and `motion(s) = s XOR c_motion`.
- Lines 152–153 give the exact cell `(Hexagram.mk yin yang yang yang yang yang, false)`. The coordinate vector is `(1,0,0,0,0,0,0)` in the order `(y1,…,y6,past_trace)`.
- Lines 206–237 define a terminus as a fixed point and prove there are no such fixed points under this motion.
- Lines 270–276 define a `ZhongOrbit` as a Nat-indexed sequence that follows motion and remains nonfixed.
- Lines 283–284 return its nonfixed property as `shengsheng_buxi`.
- Lines 330–335 prove `momentumDirection_no_telos`: the orbit cannot eventually equal one fixed target forever.

The definitions imply the stronger, exact identity

\[
\operatorname{motion}(\operatorname{motion}(s))
  =(s\mathbin{\mathrm{XOR}}c)\mathbin{\mathrm{XOR}}c
  =s\mathbin{\mathrm{XOR}}(c\mathbin{\mathrm{XOR}}c)=s.
\]

Because `c ≠ 0`, the orbit's least period is exactly two. For every `ZhongOrbit`, its step law therefore gives `states(n+2)=states(n)` and `states(n+1)≠states(n)`.

This is a valid witness of indefinitely recurring nonconstant motion. It is **not** a proof of aperiodicity, infinitely many distinct configurations, perpetually new causal dimensions, or protected public capabilities. The no-telos theorem does not mention rewards, optimization, target selection, or a shrinking set of alternatives. Its source cannot by itself support the broader statement in canonical README:71 that judging actions solely by target proximity necessarily shrinks the interval field. Additional hypotheses and a separate theorem would be required for that statement.

The current inspection is not a failed proof: the theorem has the narrower, valid conclusion that its statement says. Nor does periodicity refute the canonical philosophy: the primary text expressly permits simplicity, rest, recurrence, and transformation without monotone complexity. It establishes the precise semantic reach of the formal witness.

External check `verify_root_scope.py` used the source's exact cell and componentwise XOR definitions. All 128 source states have exact period two, forming 64 two-cycles. A separate integer encoding checked all 127 nonzero seven-bit masks over all 128 states, or 16,256 state-mask pairs. All checks passed. The algebraic derivation is the proof; the exhaustive calculation is an independent finite check. No Lean build was run, so this is not a fresh kernel check of the repository.

For portable evidence replay, the checker's default mode reads the bundled source manifest and repeats the frozen arithmetic without accessing the source repositories or rewriting excerpts. `--inspect-live-sources` refreshes hashes and excerpts by read-only access to the original paths. A fresh-copy default replay was run with an audit hook forbidding all opens under the two source repositories; it reproduced `root-scope-checks.json` byte for byte. Default replay is not fresh source verification or a Lean check.

## Current representation and single-root results

The `MonadRoot` result has exact, useful organizational content:

- `notes/monad-root-plan.md:34–38` says that every admitted formal item has a finite path to `一元`, explicitly denying that this is a premise-free proof of philosophical truth.
- `MonadRoot.lean:1120–1128` defines root-to-face edges and subsequent registry links.
- `MonadRoot.lean:1259–1292` proves uniqueness of the root in that registered graph.

Thus “all registered items trace back to one root” is proved at that graph's scope. It does not say that each registered proposition is logically deduced from the root alone or that all truths about the world are registered.

The latest `FullGUT` layer deserves a fairer reading than “everything is assumed”:

- `FullGUT.lean:1561–1639` constructs faithful R-family realizations for arbitrary finite presentations satisfying its D1 interface.
- Its encodable stream branch likewise has an actual construction (`:2233` onward).
- These are substantive representation theorems; they preserve the supplied presentation's operations, relations, and proof structure.
- At the unrestricted interface, `SemanticsPreservable` is defined as existence of a faithful realization (`:1084–1087`), and the generic theorem returns that supplied witness (`:2482–2505`).
- The current `claim-status-ledger.md:25–26,40` explicitly leaves unrestricted Claim Z/T0 and broader native semantics open. It separates the achieved coordinate/representation boundary from those claims.

Even completing the representation programme would show how laws and systems can be expressed and related. It would not, without an additional theorem, show that every expressible system is perpetually generative or that a particular public norm is uniquely obligatory. Conversely, leaving dynamics variable does not disqualify the programme from being fundamental as a theory of representation.

## What would close the precise inference

To derive indefinite existence of a generative path, define an independently recognizable class K and prove that every reachable member of K has an admissible continuation remaining in K. Under an appropriate choice/construction principle this yields an infinite path. Under hostile uncertainty, an implementable controller must keep **every permitted successor** within K; local existence of a helpful successor is insufficient. To derive repeatedly completed progress, add a recurrence argument. To derive inexhaustible novelty, establish an appropriate unboundedness or nonrecurrence property. Those are different conclusions.

Such theorems can close a mathematical characterization of continuation and its failure. Establishing that reality belongs to K requires independently justified constitutive/physical premises. Merely defining K as “systems that keep generating” would not accomplish this. Public protection additionally needs the declared normative and standing commitments already made explicit by v2.

The strongest defensible current determination is therefore: the root programme contains real structural and representation results, and its global continuation assertion is an additional commitment whose required bridge is now identifiable. The inspected formal witness demonstrates sustained alternation exactly; it does not discharge the stronger bridge. The task is not resolved by changing a status label or by importing global continuation into the definition of the root.
