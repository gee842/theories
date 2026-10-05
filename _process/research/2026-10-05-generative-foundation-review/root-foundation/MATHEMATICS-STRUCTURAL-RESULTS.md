# Mathematical structure, acquired abstraction and finite certificates

6 October 2026. AI-authored mathematical development under Ren's request to investigate how far the relation between the theory and mathematics can be claimed. The named connection is **acquired prediction → reusable abstraction → warranted inference** within the [generative-grounding programme](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/GENERATIVE-GROUNDING.md). These are self-contained reconstructions of standard mathematical arguments, plus finite executable checks. No mathematical priority, new physical law, empirical acquisition result, or new Lean verification is claimed.

The strongest result here is conditional and constructive: a deterministic process has a canonical coarsest exact abstraction relative to its specified observable questions. When a finite state bound, a known finite action alphabet and an adequate exact testing interface are supplied, finitely many observations can identify its behavior on every finite continuation. Finite compositional syntax then supports interpretations and inference whose correctness is proved by induction. This provides precise interfaces through which an actually formed learner could acquire and reuse a mathematical structure. It does not derive the testing interface, the choice of relevant questions, mathematical truth in general, or a uniquely necessary ontology.

The [common premise ledger](../../../../theories/shengsheng-buxi-generative-existence/unified-2026-10-05/FOUNDATION-PREMISES.md) and [inquiry conditions](SCIENTIFIC-INQUIRY-CONDITIONS.md) remain in force. A semantic structure, its physical acquisition, and justified confidence that an application instantiates it are different achievements.

## 1. A fixed, explicit process and question interface

Let a deterministic observed process be

\[
M=(S,A,O,\delta,o),\qquad
\delta:S\times A\to S,\quad o:S\to O.
\tag{M1}
\]

Here states retain all conditions needed by the claim; action labels describe the permitted experimental alphabet; and outputs are the questions whose answers must be preserved. A tuple of outputs may retain multiple questions. The transition function is **total and time independent** on this declared state. Time, memory, resource stocks and environmental conditions must be included when they affect later answers. Partial actions can instead be totalized with an explicit denial/failure outcome whose significance is preserved; totalization does not make a denied action physically available.

This is a narrower class than the repository's general nondeterministic relation `State → Action → State → Prop`. It is a deliberate local premise. Stochastic kernels, continuous time, interacting agents and unavailable interventions require their own corresponding preservation contracts.

For a finite action word \(w\in A^*\), define

\[
\delta^*(s,\epsilon)=s,\qquad
\delta^*(s,aw)=\delta^*(\delta(s,a),w),\qquad
\beta_s(w)=o(\delta^*(s,w)).
\tag{M2}
\]

Induction gives \(\delta^*(s,uv)=\delta^*(\delta^*(s,u),v)\). Thus an actual prefix supplies the starting state for its suffix. In particular, this notation does not permit a later calculation to restore depleted resources or reset a changed mechanism without an event that does so.

The entire finite output trace along an action word is determined by the endpoint outputs for each of its prefixes. Preserving \(\beta_s\) therefore preserves all such output traces. It need not preserve an omitted expense, historical identity, another center's condition, or a newly introduced question.

## 2. The canonical exact abstraction

Define behavioral equivalence by

\[
s\sim t\quad\Longleftrightarrow\quad
\forall w\in A^*,\ \beta_s(w)=\beta_t(w).
\tag{M3}
\]

An output-respecting transition congruence is an equivalence relation \(R\) on \(S\) satisfying

\[
sRt\ \Longrightarrow\ o(s)=o(t)
\quad\text{and}\quad
\forall a\in A,\ \delta(s,a)R\delta(t,a).
\tag{M4}
\]

### Proposition M1 — Coarsest exact recursive quotient

Relation \(\sim\) is the unique coarsest output-respecting transition congruence. The quotient has well-defined operations

\[
\bar o([s])=o(s),\qquad
\bar\delta([s],a)=[\delta(s,a)],
\tag{M5}
\]

and exactly reproduces every \(\beta_s(w)\).

**Proof.** Equality of functions \(\beta_s\) makes \(\sim\) an equivalence relation. The empty word gives output equality. If \(s\sim t\), for every \(a,w\), the equality \(\beta_s(aw)=\beta_t(aw)\) says that \(\beta_{\delta(s,a)}(w)=\beta_{\delta(t,a)}(w)\). Hence successors are equivalent. These two properties make (M5) independent of the representative. Induction on word length proves equality of the quotient and original responses. Conversely, for any \(R\) satisfying (M4), induction carries \(sRt\) along every word; output preservation at its endpoint gives \(s\sim t\). Thus every such \(R\) is contained in \(\sim\), which proves coarseness and uniqueness. ∎

Coarser means more states are identified. The quotient is canonical **relative to the specified law, action alphabet and outputs**. It is not the uniquely correct description of the world independently of questions. Even within this question, it need not minimize bit-level implementation cost, energy, computation, or inference time.

### Proposition M2 — Every exact representation factors onto this quotient

Suppose a representation \(q:S\to Z\) admits a response decoder \(d:Z\times A^*\to O\) with

\[
d(q(s),w)=\beta_s(w)
\quad\text{for all }s,w.
\tag{M6}
\]

There is a unique surjection

\[
f:q(S)\to S/{\sim},\qquad f(q(s))=[s].
\tag{M7}
\]

If the representation has an output map \(g\) and update law \(\rho\) satisfying

\[
g(q(s))=o(s),\qquad
\rho(q(s),a)=q(\delta(s,a)),
\tag{M8}
\]

then \(q(S)\) is closed under \(\rho\), and \(f\) preserves outputs and transitions. When \(q(s)=q(t)\) iff \(s\sim t\), it is an isomorphism.

**Proof.** If \(q(s)=q(t)\), (M6) implies equality of all responses, so \([s]=[t]\); thus \(f\) is well defined. Every class has a representative, so \(f\) is onto. Its prescribed values on every element of \(q(S)\) force uniqueness. Under (M8),

\[
f(\rho(q(s),a))=f(q(\delta(s,a)))
=[\delta(s,a)]=\bar\delta(f(q(s)),a),
\]

and similarly for outputs. Equality of the two kernels makes \(f\) injective, hence gives the claimed isomorphism. ∎

Only the image \(q(S)\) belongs in this result. Unreachable or unused states in a larger representation cannot be counted as indispensable. If only a fixed initial state is relevant, first restrict \(S\) to its action-reachable states. In the finite case every exact representation needs at least \(|S/{\sim}|\) used states, and every exact representation with that number is isomorphic to the quotient when it implements (M8). A merely response-exact decoder (M6) need not come with computable recursive updates or an affordable carrier.

### Proposition M3 — A finite local certificate gives all-word correctness

For any candidate map \(q\), the two conditions

\[
q(s)=q(t)\Longrightarrow o(s)=o(t),\qquad
q(s)=q(t)\Longrightarrow
q(\delta(s,a))=q(\delta(t,a))\ \ (a\in A)
\tag{M9}
\]

are necessary and sufficient for quotient output and update maps of the form (M8) to be well defined on \(q(S)\). When they hold, those maps reproduce all finite responses.

**Proof.** Necessity follows by applying \(g\) and \(\rho\) to equal representation values. Sufficiency defines their values using a representative; (M9) makes the choices unambiguous. Induction on the word supplies global correctness. ∎

If the complete finite transition/output tables and \(q\) are available, (M9) is a finite check. Its universal conclusion follows from the completeness of that local table and induction. It does not follow merely because the table matches the transitions so far sampled. A learner may propose \(q\); the certificate must still establish its adequacy on the declared process.

## 3. Finite distinguishing words and the refinement deadline

Assume now \(1\le n=|S|<\infty\). Define

\[
s\sim_k t\quad\Longleftrightarrow\quad
\forall |w|\le k,\ \beta_s(w)=\beta_t(w).
\tag{M10}
\]

Let \(k_0=|o(S)|\), the number of initial output classes. The exact recurrence is

\[
s\sim_{k+1}t\quad\Longleftrightarrow\quad
o(s)=o(t)\ \land\ \forall a,\ \delta(s,a)\sim_k\delta(t,a).
\tag{M11}
\]

### Proposition M4 — Finite refinement and short counterexamples

The relations refine monotonically and stabilize by \(\sim_{n-k_0}\). The stabilized relation equals \(\sim\). Every inequivalent pair has a distinguishing action word of length at most \(n-k_0\). For finite \(A\) with complete finite tables this yields a terminating partition-refinement algorithm.

**Proof.** (M11) follows by splitting a nonempty word into its first action and suffix. Each \(\sim_k\) is an equivalence relation, and agreement through \(k+1\) implies agreement through \(k\). If two consecutive relations are equal, recurrence (M11) makes all subsequent ones equal. Every strict refinement increases the number of nonempty classes by at least one. Starting with \(k_0\) classes, at most \(n-k_0\) strict refinements can occur; if this maximum occurs the partition is discrete and already stable. At stabilization, (M11) gives an output-respecting congruence, so M1 identifies it with \(\sim\). An inequivalent pair is therefore separated by some word within the displayed horizon. Finite table signatures implement (M11) when \(A\) is finite. ∎

The integer bound remains a mathematical statement for an infinite action set; it is not then automatically an effective finite scan over actions. This is a bound on refinement rounds and distinguishing word length, not an optimal runtime or cost bound.

**Sharp family.** For \(n\ge2\), let \(S=\{0,\ldots,n-1\}\), \(A=\{a\}\), \(\delta(i,a)=\min(i+1,n-1)\), and \(o(i)=1\) exactly at \(i=n-1\). There are two initial output classes. States 0 and 1 first differ after \(n-2\) actions; successive refinements separate one more predecessor per round. Thus the \(n-k_0=n-2\) bound is attained. The two states already differ at length zero when \(n=2\).

## 4. When finite acquired evidence can identify the whole behavior

A known finite table and an unknown finite process are different cases. The following gives a sufficient interface for the second case without assuming access to a correct equivalence oracle.

Supply these premises:

1. The target is a time-independent total deterministic observed process over known finite \(A,O\), with a fixed initial state and **at most \(N\ge1\) reachable states**.
2. A test can faithfully reset to that same initial condition, execute any requested word, and return its exact endpoint output. Denials and test failures are not silently dropped. Trials do not change the target law or leave hidden state affecting later trials.
3. The claimed target really belongs to that class. The bound is a justified structural input, not estimated from the number of states discovered so far.
4. The actual protocol can pay its reset, action, reading, memory and computation requirements. The abstract theorem below first concerns information; supplying a mathematical enumeration does not itself construct this machinery.

### Proposition M5 — Exact bounded-state identification from finitely many tests

Let \(L=2N-2\). Query the endpoint output for every word of length at most \(L\). Every deterministic candidate with at most \(N\) states that agrees with these answers has the same output as the target on **every** finite word from the initial state.

**Proof.** Compare the target to any such candidate. Form their disjoint union, with each component retaining its own transitions and output map. It has \(n\le2N\) states. If the initial states differ behaviorally, M4 supplies a distinguishing word of length at most \(n-k_0\). An actual difference implies at least two output values somewhere in this union, so \(k_0\ge2\) and this length is at most \(2N-2=L\). That contradicts their test agreement. Therefore no finite word distinguishes their initial states. ∎

Because \(A,O,N\) are finite, there are finitely many labeled candidates to enumerate; at least one matches because the actual target satisfies the premises. Selecting a matching candidate and applying M1–M4 gives a minimal accessible abstraction of its initial behavior. The canonical reachable quotient is unique up to output/action-preserving renaming; the hidden physical realization need not be unique. Enumeration can be grossly inefficient. This is an existence and information-sufficiency result, not a recommendation for a practical discovery algorithm.

For the fixed protocol that resets and reads separately for each tested word, let \(m=|A|\ge1\) and suppose reset, endpoint read and each primitive action have actual constant charges \(c_r,c_o,c_a\ge0\). Its observation bill is exactly

\[
C_{\rm obs}=\sum_{k=0}^{2N-2}m^k(c_r+c_o+k c_a).
\tag{M12}
\]

This is the bill for this stipulated complete-word protocol, not a universal lower bound or an optimized protocol. Prefix reuse, other experiments and better identification methods can alter it. Computation, storage, retained representation, checking and later use require additional accounts. Every payment prefix must be feasible; an eventual total is insufficient. Resets to an abstract test condition do not restore spent laboratory fuel or replenish a learner's memory for free. With \(A=\varnothing\), the only word is empty and only its read/reset interface matters.

The finite evidence warrants the all-word conclusion **within the supplied class and exact interface**. It does not certify its own state bound, stationarity, calibration, completeness of outputs, or transfer into a different environment.

### Proposition M6 — Without the bound, bounded perfect tests cannot certify future agreement

For every finite horizon \(H\ge0\), two finite deterministic unary processes agree on all words of length at most \(H\) and differ at length \(H+1\).

**Proof.** One process has one state, output zero, and a self-loop. The other has states \(0,\ldots,H+1\), starts at zero, advances by \(i\mapsto\min(i+1,H+1)\), and outputs one only at \(H+1\). Its outputs through length \(H\) are zero and its next output is one. ∎

Any finite collection of queried words has a maximum length. On the all-zero responses, an adaptive procedure that stops after finitely many queries cannot distinguish these two admitted targets if arbitrary finite state counts remain possible. The same transcript can therefore support only a conditional claim, a defeasible hypothesis, or a bounded-horizon conclusion. This does not rule out identification in the limit, informative inherited structure, active learning with stronger queries, or controlled-error learning.

Even under a known bound, shorter tests may fail: a two-state unary toggler and a two-state latch both start with output zero and output one after one action; the toggler outputs zero after two actions while the latch stays at one. Thus one-step fitting does not certify all continuations even for this tiny class.

## 5. Histories, acquired concepts and changed questions

Fix an initial state \(s_0\). Define the response function on histories by \(F(h)=o(\delta^*(s_0,h))\). Two action histories satisfy

\[
h\equiv h'\quad\Longleftrightarrow\quad
\forall v\in A^*,\ F(hv)=F(h'v).
\tag{M13}
\]

It follows directly from (M2) that \(h\equiv h'\) iff their reached states are equivalent by (M3). In particular \(h\equiv h'\) implies \(ha\equiv h'a\). This gives a history-based construction of the same reachable quotient even when internal physical names are unavailable. The familiar language case takes \(O=\{0,1\}\); the equivalence then records which continuations produce acceptance.

This construction is semantic. It does not say that a finite learner possesses all answers \(F(hv)\), has identified their equality, or can retain an unbounded history. Equal response rows for only a finite tested suffix set need not be equal full functions. If initial conditions are uncertain, the action word need not determine one physical state; the information-state or history interface must preserve that uncertainty. If the target law changes, the previous quotient may cease to be exact.

### Proposition M7 — Enlarging the question can force conceptual differentiation

Suppose a richer output \(o':S\to O'\) determines the old output through \(o=p\circ o'\). Let \(\sim'\) and \(\sim\) be the two behavioral equivalences. Then \(\sim'\subseteq\sim\), with a natural surjection \(S/{\sim'}\to S/{\sim}\). If some formerly equivalent states yield different new outputs after a word, no decoder using only their old common abstraction can answer that new question correctly in both.

**Proof.** Equality of richer responses implies equality after applying \(p\), which proves inclusion and makes the class map well defined and onto. For the final assertion, a deterministic decoder of the same stored value and same word must give the same answer, whereas the required answers differ. ∎

For example, a three-state cycle with a constant output has a one-state behavioral quotient. Asking additionally for its actual phase makes all three states distinguishable. Both abstractions are exact for their own questions. More retained distinction is required because the question changed, rather than because the earlier model was necessarily mistaken.

Conversely, current output equality alone is too weak for recursive prediction. In the three-state chain with outputs \((0,0,1)\), its first two states answer the present question identically but differ after one action. This is why the theory's significant learned object should be an update-compatible relation, not just a cluster of currently similar appearances.

These results offer a concrete interpretation of acquired mathematical concepts: equivalence classes that preserve specified inferential continuations and come with compositional update rules. They do not imply that every useful human concept is a finite deterministic behavioral quotient, or that such concepts are actually acquired by this algorithm. In particular, epistemic and ethical relevance remain supplied in the chosen question interface.

## 6. Finitary syntax, interpretation and valid reuse

The preceding results concern behavioral abstraction. Mathematical expressions require an additional generative interface: a declared signature \(\Sigma\) of operation symbols with finite arities and a set \(X\) of variables. Form finite terms inductively:

\[
x\in X\Rightarrow x\in T_\Sigma(X),\qquad
t_1,\ldots,t_k\in T_\Sigma(X)
\Rightarrow f(t_1,\ldots,t_k)\in T_\Sigma(X)
\quad(f\in\Sigma\text{ of arity }k).
\tag{M14}
\]

Zero-arity symbols are constants. Empty seeds with no constants need not produce any term; construction rules do not provide their own base cases. A signature gives syntax, not the truth of additional equations such as commutativity. Multiple sorts can be treated with separate carriers and arity-compatible constructors; only the single-sorted case is proved here.

### Proposition M8 — Unique compositional interpretation and transport

Given a \(\Sigma\)-algebra \(D\), which interprets every \(k\)-ary symbol as a total function \(f_D:D^k\to D\), and a variable assignment \(v:X\to D\), there is a unique evaluation satisfying

\[
\llbracket x\rrbracket_{D,v}=v(x),\qquad
\llbracket f(t_1,\ldots,t_k)\rrbracket_{D,v}
=f_D(\llbracket t_1\rrbracket_{D,v},\ldots,\llbracket t_k\rrbracket_{D,v}).
\tag{M15}
\]

If \(h:D\to E\) preserves every declared operation, then

\[
h(\llbracket t\rrbracket_{D,v})
=\llbracket t\rrbracket_{E,h\circ v}
\quad\text{for every finite term }t.
\tag{M16}
\]

**Proof.** Recursive evaluation along a finite term tree gives existence. For uniqueness, two evaluations agree at variable leaves; agreement at all children forces agreement at their parent by (M15), so induction covers every term. For transport, the variable case is the definition of \(h\circ v\). For a compound term, preservation of \(f\) moves \(h\) inside the operation; apply the induction hypotheses to each child. ∎

The theorem explains a precise form of reusability: a derivation built from declared constructors can be interpreted across different carriers while a structure-preserving map keeps its meaning aligned. It does not say that all carriers share the same operations, that every analogy is a homomorphism, or that a map preserving ordinary outputs also preserves resource costs or other centers' consequences.

### Proposition M9 — Finite equational derivation is sound under its premises

Let \(\Gamma\) be identities over \(\Sigma\), understood under every variable assignment. Allow finite derivations using identities from \(\Gamma\), reflexivity, symmetry, transitivity, replacement inside any operation, and substitution of terms for variables. If an algebra \(D\) satisfies every identity in \(\Gamma\), then every derived equation is valid in \(D\).

**Proof.** Induct on the finite derivation. The premise case is the hypothesis. Reflexivity, symmetry and transitivity preserve equality. Replacement inside an operation preserves equality because its interpretation is a function. For substitution \(\sigma:X\to T_\Sigma(X)\), structural induction gives the substitution identity

\[
\llbracket t\sigma\rrbracket_{D,v}
=\llbracket t\rrbracket_{D,v_\sigma},\qquad
v_\sigma(x)=\llbracket\sigma(x)\rrbracket_{D,v}.
\tag{M17}
\]

Applying the previously valid identity under assignment \(v_\sigma\) establishes the substituted identity under \(v\). Thus every derivation rule preserves validity. ∎

This is soundness, not a proof of completeness for every mathematical theory. The finite derivation may support an identity under infinitely many assignments, because local rules preserve a universally stated property. A learned equation is first a candidate premise. A sound calculus using a false candidate does not thereby make its physical application correct.

Bare binary composition does not imply \(f(x,y)=f(y,x)\): word concatenation interprets the same binary syntax with `ab` different from `ba`. Adding commutativity selects a restricted algebraic class. Neither the existence of the syntax nor the existence of such a class establishes that actual physical interactions are commutative. Similarly, choosing equational relations can define many distinct quotient structures; no theorem here selects all of mathematics or the actual universe from a single undifferentiated generator.

Finite symbolic configurations and rule applications can themselves be represented by a process in the repository's existing transition interface. Effective construction and checking additionally require explicit encodings and executable local rules. A proof tree is not required to have finitely many possible extensions merely because each existing proof is finite. The existing [inquiry-root Lean package](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/README.md) checks a semantic formation closure under supplied predicates; its report must not be promoted to a new executable syntax checker by association with the hand proofs here.

## 7. Boundaries that prevent stronger claims

**Nondeterminism changes the quotient question.** Equal sets of finite event words need not imply state-by-state branching equivalence. Consider a state whose `a` step chooses either a state permitting only `b` or one permitting only `c`; compare a state whose `a` step reaches one state permitting both `b` and `c`. Both admit the same complete words `ab` and `ac`, and the same prefixes, but the branch reached after the first step has different future alternatives. The deterministic congruence proof cannot simply be applied to their trace-language equality. The existing exact local-to-trace theorem has its own stronger lifting premise.

**Approximate similarity need not be an equivalence.** For outputs 0, 1 and 2, the relation “difference at most one” relates the first to the second and the second to the third, but not the first to the third. An exact quotient cannot be obtained merely by replacing equality with an error tolerance. Approximate abstractions need their own error and composition bounds.

**Separate summaries do not supply joint feasibility.** A common quotient exact for each deterministic readout under the same action histories also preserves their tuple and joint output traces. Separate abstractions or marginal summaries do not establish this common contract by themselves. Affordability, learning authority and simultaneous protection transfer only insofar as the relevant conditions and outcomes are included in the state, action and observation contract. No positive reward or ethical evaluation is inferred from minimal state count.

**Semantic existence is not acquired access.** The function \(s\mapsto\beta_s\) always exists in the declared mathematical model. Its entries, equality test, finite representation and causal interpretation are not thereby available to a learner. M4 and M5 explain two distinct sufficient interfaces; their premises cannot be omitted when describing an actual mechanism.

**Physical implementation is a further bridge.** Resettable experiments, exact output readers, complete action repertoires and finite state bounds are strong conditions. For a material implementation, calibration, irreversibility, hidden context, wear and support must be identified. Realizing a specific lawful learning procedure would be evidence for that realization; it would not establish a universal historical tendency toward discovering exact mathematics.

## 8. Verification, antecedents and next connection

The [owned executable package](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/README.md) independently compares partition refinement against shortest-witness searches in a product graph. It exhaustively enumerates all Boolean-output deterministic machines with one to three states and two actions, and all four-state unary machines. It also checks every equivalence partition of those carriers for the canonical-coarseness implication, the sharp chain family, delayed-disagreement counterexamples, bounded-query identification, and finite term-interpretation transport. The [receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/verification.json) records exact coverage and the checker hash. These tests check finite instances; M1–M9 remain hand proofs. Existing Lean checks are cited only at their own scopes.

The mathematical antecedents are established, and the paper-specific summaries below are deliberately limited:

- J. J. M. M. Rutten, [*A calculus of transition systems (towards universal coalgebra)*, 1995](https://ir.cwi.nl/pub/5060/5060D.pdf), develops transitions, structure-preserving maps, equivalence and quotient reasoning in a common framework. This is prior art for the structural perspective, not evidence that our philosophical theory originated it. The longer [2000 paper](https://ir.cwi.nl/pub/48/0048D.pdf) was found but the web fetch exceeded its size limit; no detailed claim here depends on that inaccessible full text.
- Dana Angluin, [*Learning Regular Sets from Queries and Counterexamples*, 1987](https://homepages.math.uic.edu/~lreyzin/papers/angluin87.pdf), explicitly separates examples from the stronger membership/equivalence-query interface and constructs closed, consistent observation tables. Its learning guarantee assumes the stated teacher interface. M5 here instead gives a simple exhaustive sufficient test under an explicit known state bound; no efficiency improvement over established learning methods is claimed.
- The free-term and homomorphism arguments in M8–M9 are standard universal algebra. See the author-hosted [Burris–Sankappanavar text](https://www.math.uwaterloo.ca/~snburris/htdocs/UALG/univ-algebra2012.pdf), Chapter II, and [Bergman's text page](https://math.berkeley.edu/~gbergman/245/). The present proofs state their complete local contracts; they do not invoke an unreviewed equivalence between alternative foundations. The first text's direct web fetch timed out during this strand; its cited chapter is an antecedent pointer, not an additional completed validation.

**What is now defensible:** within this explicitly identified deterministic class, there is a uniquely coarsest exact recursive abstraction for a specified question family; finite local certificates can warrant claims about all finite continuations; finite exact acquisition is possible under a finite bound and adequate experiments; compositional terms and sound rules support reuse across faithful interpretations. This is stronger than a loose analogy between generativity and mathematics, while remaining standard mathematics applied to a specific explanatory interface.

**What remains to derive:** an actual formed learner must acquire and retain the testing records, construct or justify its relevant question interface, establish adequate finite-state/context assumptions, pay for abstraction construction and checking, and use the retained quotient in later prediction or reason revision. Current paid prediction and recording studies supply candidate upstream interfaces but do not yet meet all these conditions. The next useful joint construction should compare an initially overmerged model with a counterexample-refined model on held-out continuation tasks, preserve the full costs and records, and explicitly separate a correct bounded-class certificate from unverified extrapolation. A simpler conventional learning implementation is a required comparator.

A demonstrated failure of a claimed exact quotient under its complete stated table would refute its certificate or proof. A real system departing from a passed finite test beyond the declared bound would require examining class membership, calibration or hidden state, rather than declaring all later outcomes compatible by renaming them. A system whose task genuinely requires unbounded memory would restrict this finite interface while leaving the wider generative programme open. None of these results entails that minimal abstraction is uniquely ethical, that all mathematics is finite-state, or that a formal foundation has completed the theory's derivation of concern and wisdom.
