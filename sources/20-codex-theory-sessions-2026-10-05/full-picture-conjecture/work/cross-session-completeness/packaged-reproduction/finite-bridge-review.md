# Review of the finite completeness bridge

5 October 2026. Reviewed `completeness-target.md` and the sibling `generative-basis/formal/STRUCTURAL-CLOSURE.md` by proof inspection. No Lean compilation or independent rerun is claimed here.

The two-policy-contract theorem is correct: inclusions of allowed trace sets in both policy-transfer directions preserve every sure objective. The stated converse is correct when the objective family consists of all subsets of the semantic trace space; choosing a policy's own trace set as the objective supplies the required opposite-model policy. For a restricted objective family, the note correctly withholds necessity.

The finite binary encoding is an independent explicit construction. Because state, observation, and action alphabets are encoded separately and model carriers are restricted to code images, it preserves hidden information rather than revealing the encoded hidden state to the actor. The policy decoder/encoder gives a bijection of admissible abstract policies and a correspondence of legal histories and maximal plays. Composition with a valid finite partial-observation safety/recurring-progress decision theorem therefore establishes relative completeness for that exact declared finite class.

This does not establish that the existing R-family FullGUT implementation supplies that policy correspondence. A representation-preservation theorem for objects and operations has different obligations. The note explicitly states that connecting the R-family implementation to these contracts remains separate; that qualification must survive the final synthesis.

The structural-closure theorem is a complementary positive result. Least closure under all declared old-state read dependencies yields an exact coordinate quotient because every retained update sees equal retained arguments and the same joint noise. The source properly includes guards, old-value preservation branches, action permissions, observations, and state-dependent noise selectors. It allows shared correlated noise, preserves joint events, and does not infer a small global closure merely from bounded local parent counts.

When integrating the structural quotient with the finite controller theorem, retain three conditions:

1. The actor still observes its original permitted observation map. The solver must not expose the entire retained coordinate vector merely because that vector is the mathematical state of the quotient.
2. Environment input selection must use retained information or be explicitly prescribed; omitted interacting environment dependence cannot be declared harmless.
3. For sure winning, establish the support/possible-successor and policy correspondence, not merely equality of an optimized expectation or almost-sure event probability. Exact finite kernel equality and retained permission/observation maps permit this support correspondence, but the step should be stated. For expected/chance objectives, keep full probability laws instead.

The composed finite result is a substantive completion of a declared mathematical task: exact representation, admissible strategy transfer, and exact attainability/failure characterization. It does not require every process to continue, physical universality, a morally mandatory objective, or a total solver for arbitrary unbounded programs. Those are different targets.
