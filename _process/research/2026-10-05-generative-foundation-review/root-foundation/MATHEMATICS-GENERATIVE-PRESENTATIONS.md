# Generative presentations and the reach of mathematical claims

6 October 2026. AI-authored mathematical and conceptual development for the [mathematics exploration](../../../../theories/becoming/chapters/MATHEMATICS-AND-GENERATIVITY.md), following Ren's request to investigate how far its claims can extend. The results below are standard elementary constructions and self-contained hand arguments, not claims of new mathematics. Their contribution is a precise interface between the generative research programme and mathematical foundations.

The named connection is **generated operations → structural interpretation → warranted consequences**. Logic, recursion, the operation signature, admissible equations and interpretation remain explicit inputs. The mechanism by which a learner acquires them is a separate connection.

## A universal structure for iteration

Given a set \(X\), a chosen start \(x_0\in X\), and a total function \(f:X\to X\), there is exactly one function \(r:\mathbb N\to X\) satisfying

\[
r(0)=x_0,\qquad r(n+1)=f(r(n)).
\]

**Proof.** Define \(r\) by recursion. Any two functions satisfying the equations agree at zero. If they agree at \(n\), applying the same \(f\) makes them agree at \(n+1\). Induction proves equality everywhere.

This gives natural numbers a precise universal role: zero and successor organize arbitrary finite iteration from a specified start. The uniqueness concerns the interpretation of iteration into each supplied system. It does not require \(r\) to be injective. A one-state system, a toggle and an unbounded counter all admit such a map; only the last of these examples distinguishes all iteration counts in its physical state.

The theorem uses natural numbers and recursion in its mathematical background. It is a characterization of their role, not a proof deriving the existence of natural numbers from physical observations without using mathematics. Nor does it certify that a real system can execute every iteration forever.

Riehl's *Category Theory in Context*, Example 2.1.1, gives precisely this universal-property interpretation of natural numbers. Her Example 4.1.13 constructs the free category on a directed graph from finite paths and concatenation. Both are established examples of generation characterized by an interpretation property. The word “universal” here quantifies over a specified category of structures; it does not assert that the actual universe has been derived. [Author's text, printed pp. 54 and 137](https://emilyriehl.github.io/files/context.pdf).

## The same generator supports different mathematics

Let the freely generated words on \(a\) be indexed by their lengths, with concatenation corresponding to addition. Additional identifications give different quotients.

1. Retain all lengths separately. The result is \((\mathbb N,+,0)\).
2. Identify lengths congruent modulo a specified \(k\ge2\). Addition descends because \(m\equiv m'\) and \(n\equiv n'\) imply \(m+n\equiv m'+n'\pmod k\). The result is the cyclic group of order \(k\), viewed also as a monoid.
3. Identify all positive lengths with each other, keeping zero separate. Positivity of a sum is the logical OR of positivity of its summands. The quotient is the two-element idempotent monoid: combining the nonidentity element with itself changes nothing.

These constructions all respect concatenation. They disagree about whether two repetitions cancel, accumulate or saturate. Thus a generator and composition alone do not select one particular arithmetic. The identifications carry substantive content.

For a finite alphabet \(A\), ignoring order while retaining the count of each symbol gives \(\mathbb N^A\) under coordinatewise addition. Each word determines its count vector; concatenation adds vectors; every nonnegative vector is represented by some word. This constructs a free commutative counting structure. It is appropriate only for questions invariant under the ignored reorderings. In an organization where repair-before-use differs from use-before-repair, that commutative abstraction would lose a consequential difference.

The positive lesson is plural: one compositional starting language supports several exact mathematical structures through different declared equivalences. The negative lesson concerns uniqueness: no preferred identification is selected merely by calling the starting language generative.

## Operations and equations give a general presentation

Choose a finitary signature \(\Sigma\): operation symbols with specified finite arities, including any constants. Choose variables \(V\). A term is either a variable or an operation symbol applied to an appropriately sized list of terms. This grammar inductively generates the term collection \(T_\Sigma(V)\). If there are neither variables nor constants, there are no terms; existence of a grammar is not automatically existence of an inhabitant. This construction permits empty algebras and subalgebras when there are no nullary operations. Under the convention that algebra carriers must be nonempty, assume instead that there is at least one variable or constant.

For any supplied \(\Sigma\)-algebra \(M\) and assignment \(v:V\to M\), there is a unique evaluation map

\[
\operatorname{ev}_v:T_\Sigma(V)\to M
\]

that agrees with \(v\) on variables and preserves every operation.

**Proof.** Recursively evaluate the immediate subterms and apply the corresponding operation of \(M\). This defines the map. Structural induction proves uniqueness: its value on each variable is fixed, and its value at an operation node is fixed once its values on the children are fixed.

The relation \(s\equiv_v t\) iff \(\operatorname{ev}_v(s)=\operatorname{ev}_v(t)\) is a congruence. Replacing arguments by equal interpreted values cannot change the result of a function. The quotient \(T_\Sigma(V)/{\equiv_v}\) is therefore isomorphic to the subalgebra generated by the assigned variables and constants: map a class to its interpreted value; the definition of the equivalence gives well-definedness and injectivity, and the image definition gives surjectivity.

For identities intended to hold under every assignment, a single assignment is insufficient. Instead choose a class \(K\) of algebras and identify terms only when every valuation in every member of \(K\) gives equal values. This is again a congruence, by the same argument at each valuation. If the relevant class is empty, the universal condition identifies everything vacuously; a substantive application must establish an intended model.

Alternatively, start from equations and close under the declared inference rules, including substitution where equations contain variables. The class of interpretations satisfying them, their consequences and the relationship between derivability and semantic validity require their own soundness/completeness results. The construction above does not assert that every true equation can be found by a terminating algorithm.

Free algebras and quotient algebras are established universal-algebra constructions. Burris and Sankappanavar's *A Course in Universal Algebra* treats them in Chapter II; the independent elementary argument above is used to expose our inputs and outputs. Their framework is a comparator to any claim that such generation is unique to this theory. [Author's edition and access page](https://www.math.uwaterloo.ca/~snburris/htdocs/ualg.html).

This supports a substantial claim: **a wide algebraic fragment of mathematics admits generative presentations whose interpretations are fixed by the images of the generators and preservation of operations.** It does not establish that all mathematics reduces to a finite algebraic presentation. Order, topology, infinite constructions, higher-order quantification and stronger set/type principles bring additional structure. Even within algebra, not every object has a finite presentation.

## Finitary deduction is a generative process

Let \(F\) be a set of formulas, \(B\subseteq F\) an axiom set, and \(R\) a collection of inference instances \((p_1,\ldots,p_k;q)\), with each \(k\) finite and possibly zero. A finite derivation tree has axiom leaves or rule nodes, each rule node having its listed premise trees as children. A zero-premise rule is itself a permitted leaf.

Define an abstract process whose state \(D\) is a finite set of available formulas. Begin at \(\varnothing\). An event adds either one axiom or the conclusion of a rule whose premises are already in \(D\).

**Proposition.** A formula \(q\) occurs in a state reachable by finitely many events exactly when it has a finite derivation tree from \(B,R\).

**Proof.** In the forward direction, induct over the event history. An added axiom is a one-node derivation; an applied rule combines the already available premise derivations into a derivation of its conclusion. In the reverse direction, induct on a derivation tree. Generate each premise tree in sequence and then append its conclusion. Earlier formulas remain available, so shared premises cause no obstruction.

The process is an instance of the repository's state/event/transition interface. This is an exact representation of finite derivability for the persistent-premise calculus defined here. Resource-sensitive logics need their contexts and permitted splits encoded in the judgments and rules; the accumulation of proved judgments does not authorize arbitrary reuse of resources inside a judgment. The process does not decide whether \(q\) is derivable, make the rules sound, or account for physical storage and work.

Suppose additionally that formulas and proposed rule instances have finite encodings, axiom membership and rule-instance validity are decidable, and each finite proof includes its premise references. A verifier can check a proposed proof by a finite scan. More generally, recursively enumerable axioms can carry finite certificates of their enumeration. These are the effectiveness assumptions needed to move from an abstract event relation to an effective checking procedure.

A rule allowing any false statement as a conclusion still generates a perfectly well-defined process. To obtain semantic soundness, supply an interpretation, require the axioms to hold, and require each inference instance to preserve truth. Induction over the derivation then proves the generated formulas true under those conditions. That induction is an argument in the surrounding mathematical framework, not evidence that causal production certifies itself.

The repository's [existing generative-closure package](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/README.md) already checks soundness and premise-preserving necessity transport for a selected eight-constructor calculus. Its formulas are semantic predicates. It explicitly does not supply effective syntax or a complete proof-search procedure. The general representation argument here neither changes those files nor upgrades their verification claim.

## Structural transport and its empirical boundary

Suppose a model \(M\) realizes the relevant operations and satisfies the premises of a soundly derived result. That result holds in \(M\). This is the exact source of substrate independence at the declared structural scope.

To apply the result to an actual system, one must identify its states, operations and observations with those of \(M\) sufficiently faithfully for the conclusion at issue. The relation between the physical and abstract accounts is itself an explanatory and empirical object. The theory should account for how the map is acquired, checked, maintained and revised.

The same inscription illustrates the boundary. The expression \(1+1=0\) holds in arithmetic modulo two and fails for ordinary natural numbers. The material production of the inscription alone does not select its domain and operation. Relevant surrounding practices or calibration may determine an interpretation; generative occurrence without that further content does not.

Similarly, a representation that preserves final answers might fail to preserve available choices, probabilities, intermediate costs or what a participant can observe. Which property is transported must be named. The current [process core](../../../../theories/becoming/chapters/GENERATIVE-CORE-LEAN.md) and [controlled-refinement study](../../../../theories/becoming/chapters/CONTROLLED-REFINEMENT.md) already separate these contracts.

## Strong claims and their remaining explanation

The following claims survive this development.

- Abstract iteration and finitary compositional construction have universal mathematical descriptions relative to specified structures and background logic.
- Generators, operations and declared identifications can produce exact algebraic structures with unique induced interpretations at the stated scope.
- Every finitary derivation system of the stated persistent-premise form has an exact finite-reachability presentation; resource-sensitive contexts require a faithful encoding, and effective proof checking requires additional encoding and computability assumptions.
- Soundness transports conclusions throughout an identified class of interpretations, while physical occurrence and applicability require further premises.

These claims justify treating generation as a mathematically serious organizing perspective on construction and reasoning. They do not establish that this vocabulary uniquely grounds mathematical truth, selects one logic, supplies actual infinity or explains how a learner acquires mathematical concepts.

The next connected task is to replace part of the supplied interpretation or abstraction with an acquired and corrected mechanism. The [structural-results study](MATHEMATICS-STRUCTURAL-RESULTS.md) examines a canonical exact abstraction and what finite evidence could identify it. The [foundation audit](MATHEMATICS-FOUNDATION-AUDIT.md) tests stronger necessity and ontology claims. The [learning evidence](MATHEMATICS-LEARNING-EVIDENCE.md) compares the acquisition proposal with existing research. These are distinct tests of one connection, not independent evidence for the entire theory.
