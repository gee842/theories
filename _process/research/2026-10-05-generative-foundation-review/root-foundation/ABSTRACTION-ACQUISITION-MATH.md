# Acquiring a compositional abstraction from paid endpoint observations

6 October 2026. AI-authored mechanism and hand-proof contribution to the connection **acquired prediction → reusable abstraction → warranted inference**. This develops the acquisition interface left by [mathematical structural results](MATHEMATICS-STRUCTURAL-RESULTS.md), following Ren's approval to pursue the operational bridge. The executable continuation has its own [declared protocol](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/PROTOCOL.md); numerical outcomes and independent validation belong to that package.

**The result:** an installed learner can acquire action histories and distinguishing suffixes from its own endpoint experiments, construct a composition-preserving Moore abstraction, and certify its response to every finite continuation under a supplied state bound. Neither the correct quotient nor counterexample labels are given to the learner. Its own predicted-versus-observed disagreements drive refinement. All observations, symbolic work, memory and retained use require an explicit affordable implementation.

This is conventional observation-table learning with an exhaustive bounded test replacing an equivalence-query teacher. The mathematical ancestry is Angluin's \(L^*\): finite prefix and suffix tables, closure, consistency and counterexample refinement are established methods. The original algorithm assumes a teacher able to answer membership and equivalence queries; the present interface obtains counterexamples by executing its own finite tests under a known bound. This is an adaptation and conditional operational join, not a new learning algorithm or evidence of theoretical distinctiveness. [Angluin, 1987, §§1.1 and 2.1–2.3](https://homepages.math.uic.edu/~lreyzin/papers/angluin87.pdf).

The proofs below are hand proofs in ordinary discrete mathematics. They do not constitute new Lean verification or empirical calibration of the supplied resource tariffs.

## 1. What is supplied, and what is acquired

Let the target have a fixed initial state \(x_0\), a known finite nonempty action alphabet \(A\), a known finite output alphabet \(O\) with decidable equality, a total stationary deterministic transition law \(\delta\), and output map \(o\). Write

\[
F(w)=o(\delta^*(x_0,w)),\qquad w\in A^*.
\tag{A1}
\]

The learner can request an endpoint experiment: reset the target to \(x_0\), execute \(w\), and read \(F(w)\). Resets restore this target condition only. They do not restore laboratory fuel, clear the learner's expenses or create new source packets. An experiment must either return an exact observed output with its payment completed, or report failure; a failure is not silently interpreted as an output.

Supply an integer \(N\ge1\) that is a valid upper bound on the target's reachable states. The learner is not given those states, their transition table, their behavioral equivalence, or a test telling it which hypothesis is correct. It receives no counterexample word except one identified by comparing its own prediction to its own endpoint observation.

The supplied conditions include the controller algorithm, a faithful action and output interface, reset fidelity, stationarity, the state bound, memory encoding, equality and string operations, a clock/order for finite work, and a resource law. These are consequential local inputs. The proof does not infer them from the existence of an acquired prediction.

The learned content consists of:

- a cache of actual endpoint answers, indexed by executed words;
- selected histories used as state representatives;
- experimentally acquired suffix distinctions;
- an output and transition table composed from those rows;
- a completed finite test record supporting the conditional all-word claim.

The target's minimal reachable behavioral quotient has some size \(d\le N\). The number \(d\) is used in the proof, not supplied to the learner. Histories \(h,h'\) have the same full behavior when \(F(hv)=F(h'v)\) for every continuation \(v\). The learner initially has only finitely many tested suffixes and must not treat equality on that finite sample as established equality of full behavior.

If the action alphabet is empty, only the initial output is observable and the problem reduces to its paid acquisition. The remainder concerns \(|A|\ge1\).

## 2. The executable information algorithm

Maintain a finite prefix-closed set \(S\subseteq A^*\), a finite suffix-closed set \(E\subseteq A^*\), and a cache of exact endpoint answers. Initialize \(S=E=\{\epsilon\}\), with no cached outputs. Prefix closure means all prefixes of a member are members; suffix closure has the analogous meaning. Thus both sets contain the empty word.

For every \(s\in S\cup SA\) and \(e\in E\), obtain the cached or freshly observed value \(F(se)\). Define the row

\[
\operatorname{row}_E(s):E\to O,\qquad
\operatorname{row}_E(s)(e)=F(se).
\tag{A2}
\]

Cache reuse is permitted only under the stationary interface contract and requires the implementation's charged lookup and read. Distinct table cells can refer to the same word \(se\); this permits reuse of one observation rather than a new physical experiment.

The completed table is **closed** when every \(t\in SA\) has the same row as some \(s\in S\). It is **consistent** when

\[
s,t\in S,\quad \operatorname{row}_E(s)=\operatorname{row}_E(t)
\ \Longrightarrow\
\operatorname{row}_E(sa)=\operatorname{row}_E(ta)
\quad(a\in A).
\tag{A3}
\]

Use the following deterministic procedure, with any fixed, explicitly implemented finite ordering for selecting witnesses:

1. Complete all required table entries through cache reads or paid endpoint experiments.
2. If closure fails at \(sa\in SA\), add \(sa\) to \(S\), then return to step 1.
3. If consistency fails at \(s,t,a\), choose \(e\in E\) with \(F(sae)\ne F(tae)\), add \(ae\) to \(E\), then return to step 1.
4. Construct the candidate Moore machine \(H\) from the distinct rows of \(S\), as below.
5. In shortlex order, compare \(H\)'s predicted output with the observed \(F(w)\) for every \(|w|\le L=2N-2\). Simulation, cache use, new experiments and comparisons are paid.
6. At the first disagreement \(w\), add **all prefixes of \(w\)** to \(S\), then return to step 1. If all comparisons finish and agree, pay for retaining the model and completed certificate before declaring acquisition complete.

Any denied payment, capacity failure or unavailable experiment stops the affected operation and prevents successful certification. Earlier spent resources remain spent. An implementation may also halt with a class-assumption failure if more than \(N\) distinct rows are observed. Absence of that diagnostic does not certify the state bound.

Closure repair preserves prefix closure because \(sa\) extends a member \(s\), whose prefixes are already present. Consistency repair preserves suffix closure because every proper suffix of \(ae\) is a suffix of \(e\), hence already in \(E\). Counterexample repair preserves prefix closure by construction. All additions preserve \(\epsilon\).

### The candidate

For a closed consistent table, define

\[
\begin{aligned}
Q_H&=\{\operatorname{row}_E(s):s\in S\},&
q_0&=\operatorname{row}_E(\epsilon),\\
\delta_H(\operatorname{row}_E(s),a)&=\operatorname{row}_E(sa),&
o_H(\operatorname{row}_E(s))&=F(s).
\end{aligned}
\tag{A4}
\]

Closure ensures that successors belong to \(Q_H\). Consistency makes the successor independent of the chosen representative. Since \(\epsilon\in E\), equal rows have equal present outputs, so \(o_H\) is also well defined. A row can be implemented by its retained finite entries or a checked index into those entries; it is not a hidden target-state label.

## 3. Acquired distinctions and warranted composition

### Lemma A1 — Every row distinction has an observed witness

If \(\operatorname{row}_E(s)\ne\operatorname{row}_E(t)\), some retained \(e\in E\) satisfies \(F(se)\ne F(te)\). These histories reach different full behavioral classes. Hence

\[
k=|Q_H|\le d\le N.
\tag{A5}
\]

**Proof.** Inequality of finite functions supplies an unequal entry. Its two values were obtained by endpoint experiments or faithful reuse of those observations. Equal full behaviors would agree on this particular suffix, so the corresponding behaviors are distinct. Distinct rows therefore require distinct behavioral classes. ∎

In a consistency repair, the newly selected suffix \(ae\) has a concrete causal provenance: the two observed continuations \(sae\) and \(tae\) differ. The procedure does not receive a label saying “split these correct states.” It derives the split from a failure of a previously proposed identification to support one more action.

### Lemma A2 — The candidate reproduces its finite evidence compositionally

For every \(s\in S\cup SA\),

\[
\delta_H^*(q_0,s)=\operatorname{row}_E(s).
\tag{A6}
\]

For every \(s\in S\cup SA\) and \(e\in E\), the candidate's response after \(se\) is \(F(se)\).

**Proof of (A6).** Induct on the length of \(s\). The empty word is immediate. A nonempty word in \(S\cup SA\) has the form \(ta\) with \(t\in S\): for a word in \(S\), this uses prefix closure. Apply the induction hypothesis and the transition definition.

For the second assertion, prove by induction on the length of \(e\) that from any state \(\operatorname{row}_E(t)\), \(t\in S\), the response along \(e\) equals \(F(te)\). The empty suffix uses the output definition. If \(e=av\), suffix closure gives \(v\in E\). The first transition reaches \(\operatorname{row}_E(ta)\), equal by closure to \(\operatorname{row}_E(u)\) for some \(u\in S\). Row equality gives \(F(tav)=F(uv)\); the induction hypothesis evaluates the remaining suffix from \(u\). For a starting history \(s\in S\cup SA\), use (A6) and a representative in \(S\) with the same row; its entries agree for every \(e\in E\). ∎

Consequently every candidate state is accessible by a history in \(S\). Any two distinct candidate states are distinguished by a suffix in \(E\), because their row entries differ and the candidate realizes those entries. Thus each closed consistent candidate is minimal **for its own behavior**. This does not yet prove that its behavior equals the target's.

### Lemma A3 — Each table repair makes strict progress

The number of distinct rows on \(S\) never decreases. Each closure repair or consistency repair increases it strictly.

**Proof.** Enlarging \(S\) retains its old rows. Enlarging \(E\) retains all old coordinates, so previously distinct rows remain distinct. A closure repair promotes a row that matched none of the old representatives. A consistency repair starts with equal rows for \(s,t\) but adds the coordinate \(ae\) on which they differ. It therefore splits an old row class. ∎

The refinement concerns equality that supports composition. Current-output clustering alone need not support an action update; the new suffix records precisely why a proposed equality failed.

## 4. Self-discovered counterexamples force progress

### Lemma A4 — A failed hypothesis strictly increases the next hypothesis's state count

Let \(H\) be built from a closed consistent table \((S,E)\). Suppose the learner observes \(F(w)\ne H(w)\), adds all prefixes of \(w\) and completes repairs, obtaining a closed consistent table \((S',E')\) and candidate \(H'\). Then

\[
|Q_{H'}|>|Q_H|.
\tag{A7}
\]

**Proof.** Monotonicity already gives \(|Q_{H'}|\ge |Q_H|=k\). Suppose equality held. Choose one old history for each distinct old row. Their new rows are still distinct, so these \(k\) histories represent all new states.

Restriction of a new row to \(E\) is therefore a bijection from \(Q_{H'}\) to \(Q_H\), taking every chosen old representative's new row to its old row. It preserves the initial state and output because \(\epsilon\in E\). It also preserves transitions: for a chosen old history \(s\), the new successor is the row of \(sa\); its restriction is the old row of \(sa\), which is exactly the old successor in (A4). Thus this bijection is a Moore-machine isomorphism, and \(H'\) and \(H\) have identical initial behavior.

But \(w\in S'\). Lemma A2 makes \(H'(w)=F(w)\), while the acquired counterexample gives \(H(w)\ne F(w)\). This contradicts identical behavior. Therefore the next hypothesis has strictly more states. ∎

This argument is needed because merely adding prefixes need not immediately split a row. The subsequent closure or consistency repairs may produce the decisive distinction. The claim concerns the next completed hypothesis, not every individual new prefix.

### Theorem A5 — Finite acquisition and an all-word certificate

Under the supplied deterministic, stationary, exact reset/read interface and valid bound \(N\), and assuming the required finite operations remain feasible, the procedure terminates with a candidate \(H\) satisfying

\[
H(w)=F(w)\qquad\text{for every }w\in A^*.
\tag{A8}
\]

There are at most \(d-1\) failed hypotheses and at most \(d-1\) closure/consistency repairs in total. These two bounds count potentially overlapping progress and must not be added as a bound of \(d-1\) on their combined count.

**Proof of termination.** Initially there is one row on \(S=\{\epsilon\}\). Lemma A1 bounds the number of distinct rows by \(d\). Lemma A3 makes every table repair increase that number, so there can be at most \(d-1\) such repairs. Each currently finite table can be completed and scanned in finitely many operations. Lemma A4 makes each failed hypothesis increase the next completed hypothesis's state count, so there are at most \(d-1\) failures. Each exhaustive test set is finite. No loop can continue indefinitely under the declared feasibility assumptions.

**Proof of correctness.** The final candidate has at most \(N\) states and agrees with the target on every word of length at most \(2N-2\). The bounded distinguishing-word result [M4–M5](MATHEMATICS-STRUCTURAL-RESULTS.md#4-when-finite-acquired-evidence-can-identify-the-whole-behavior) gives (A8). Explicitly, the disjoint union of target and candidate has at most \(2N\) states. If their initial responses differed, finite partition refinement would find a distinguishing word of length at most the number of states minus the number of output classes. A difference entails at least two output classes, so the word would have length at most \(2N-2\), contradicting the completed test. ∎

The candidate is judged by actual tests performed by the learner. A product-graph search that an analyst later runs using the hidden target table is a separate validation; it neither supplies learner counterexamples nor pays for its certificate.

### Corollary A5a — The acquired object is the canonical reachable abstraction

The final \(H\) is isomorphic to the target's reachable behavioral quotient. In particular, there is a surjective output- and action-preserving map from reachable target states to \(Q_H\), whose kernel is exactly full behavioral equivalence.

**Proof.** Lemma A2 distinguishes every pair of candidate states by some suffix, so \(H\) is minimal. Equation (A8) makes its residual response after every history equal the target's residual response. If two histories reach the same target state, their residual responses are equal, so they must reach the same state of minimal \(H\). Sending a target state to the candidate state reached by any access history is therefore well defined. It is onto by accessibility and preserves outputs and transitions by concatenation. Equality of its values implies equality of every continuation response; conversely equal full behaviors cannot reach distinguishable candidate states. Its kernel is precisely the target's behavioral equivalence. ∎

The learner does not need to represent that map using physical state names. Its access histories and acquired transition table already implement the quotient. The map is the semantic proof that those learned operations preserve the specified questions.

## 5. Explicit finiteness bounds, without a claim of efficiency

Write \(m=|A|\ge1\) and \(L=2N-2\). Prefix additions from any counterexample add at most \(L\) nonempty words; there are at most \(d-1\) such counterexamples. Closure repairs add at most another \(d-1\) words. Consistency repairs add at most \(d-1\) suffixes. Consequently

\[
|S|\le 1+(d-1)(L+1),\qquad |E|\le d.
\tag{A9}
\]

Each acquired suffix extends an existing suffix by one letter, so its length is at most \(d-1\). A representative history is either a counterexample prefix of length at most \(L\), or extends an earlier history through one of at most \(d-1\) closure promotions. Thus

\[
\max_{s\in S}|s|\le L+d-1,\qquad
\max_{s\in S\cup SA,\ e\in E}|se|\le L+2d-1\le4N-3.
\tag{A10}
\]

These are coarse upper bounds, not exact query counts. They also cover \(N=1\): a table may inspect one-action words even though the final distinguishing horizon is zero.

Because \(S,E\) only grow, all table queries lie in the final \((S\cup SA)E\). With permanent faithful caching, the total number \(Q_{\rm new}\) of distinct newly executed words is bounded by

\[
Q_{\rm new}\le
(m+1)N\bigl[1+(N-1)(2N-1)\bigr]
+\sum_{k=0}^{2N-2}m^k.
\tag{A11}
\]

The first term bounds table cells and may count duplicate words; the second covers all certification words, which may themselves overlap the table. Later hypotheses can reuse their outputs, but each still needs fresh simulation and comparison work. At most \(d\) hypotheses are tested, giving at most \(d\sum_{k=0}^{L}m^k\) certification comparisons. These tests can be exponentially numerous in the supplied bound. No efficiency advantage over established active learning or conformance testing is claimed.

For a stipulated reset/execute/read protocol with constant nonnegative charges \(c_r,c_a,c_o\), its actual new-observation bill is

\[
C_{\rm observation}
=\sum_{w\ {\rm newly\ executed}}(c_r+|w|c_a+c_o)
\le Q_{\rm new}\bigl(c_r+(4N-3)c_a+c_o\bigr).
\tag{A12}
\]

This excludes symbolic work, cache reads, writes, capacity, retention, installation and later use. It does not replace their accounting. The information theorem only proves that an adequately provisioned finite implementation is possible under the supplied interface.

## 6. Prefix feasibility is part of the operational theorem

Model an implementation as an ordered sequence of declared events. An event may reset, act, read, access cached evidence, allocate or write memory, compare rows, construct a candidate, simulate it, retain a certificate or use the result. Each event has a supplied nonnegative charge \(c_t\), and any incoming resource \(u_t\) must actually become available before the event that uses it.

For initial liquid reserve \(R_0\), the exact scalar payment condition is

\[
R_0+\sum_{j=0}^{t}u_j-\sum_{j=0}^{t-1}c_j\ge c_t
\qquad\text{for every payment event }t.
\tag{A13}
\]

Resource types that cannot substitute for one another require their own componentwise conditions. Persistent and temporary memory also require a capacity invariant: live cells plus the current operation's required workspace must fit the installed capacity at each operation, not merely after the operation releases temporaries.

**Proof of the payment criterion.** Immediately before event \(t\), the left side before its comparison with \(c_t\) is precisely the initial stock plus credited arrivals minus already paid charges. It is sufficient exactly when that event can be prepaid. Induction yields the complete successful schedule if all inequalities hold; the first failure prevents its event. ∎

With no arrivals and nonnegative charges, enough initial reserve for the entire fixed trace is equivalent to all its scalar prefix checks. When receipts occur later, a favorable eventual net balance does not imply (A13). In particular, a later productive use cannot finance the earlier test that enabled it.

The mechanism needs these further implementation obligations:

- A new observation or durable update is committed only after its required payments and capacity checks; denial must not create a free answer or completed refinement.
- Reading previously acquired evidence, constructing row keys and comparing them still consume the declared computation and retention resources.
- Candidate construction and exhaustive testing need their own prepaid work and temporary space; paying only for target actions is insufficient.
- A test certificate is committed only after all required comparisons and its record are paid. Completion of retained acquisition additionally waits for the declared compaction and retention payments.
- A later invocation of \(\delta_H\), output decoding or external action is a new paid event. Mathematical reusability does not imply costless use.

The protocol's work envelopes are abstract machine tariffs, not measured processor instruction counts or joules. A correct implementation must conservatively account for its declared symbolic operations and storage. The theorem does not itself validate the numerical envelope sizes; that is an implementation and audit obligation. External analyst logs are not free memory available to the learner.

If funding or capacity runs out, already acquired information can remain valid, but the interrupted run has not established the remaining operational goal. Interruption before completing the tests and their certificate record gives no completed all-word certificate. A later failure to fund retention does not erase a previously completed certificate; it prevents the stronger claim that the learned result has been retained and made available for its intended later use. The implementation's separate certified, retained and overall status fields should preserve these distinctions.

## 7. A concrete acquired distinction

Consider the supplied three-phase target, starting at phase 0, with output pattern \((0,0,1)\). Action \(a\) moves cyclically through phases \(0\to1\to2\to0\). The learner receives neither phase names nor this table.

Initially \(S=E=\{\epsilon\}\). The endpoint observations for \(\epsilon\) and \(a\) are both zero. The table is closed and consistent, so its first hypothesis has one state and predicts zero forever.

The learner's own test of \(aa\) returns one, contradicting that prediction. It adds \(\epsilon,a,aa\) to \(S\). With only the empty suffix, \(\epsilon\) and \(a\) still have the same row. Their \(a\)-successors have different outputs: \(F(a)=0\), but \(F(aa)=1\). Consistency repair therefore adds the acquired suffix \(a\).

The three rows on \(E=\{\epsilon,a\}\) become

\[
\operatorname{row}(\epsilon)=(0,0),\qquad
\operatorname{row}(a)=(0,1),\qquad
\operatorname{row}(aa)=(1,0).
\tag{A14}
\]

The resulting candidate has three states, with its cyclic update inferred from the observed successor rows. Its longer continuation predictions follow by composing this update. Completed tests through \(2N-2=4\), with \(N=3\), license all-word correctness under the stated premises.

Adding a second action \(b\) that resets the target phase to zero gives the binary fixture in the protocol. Its initial observations for \(\epsilon,a,b\) remain zero; the mismatch \(aa\) and suffix \(a\) yield the same essential differentiation, while new row observations acquire the \(b\)-transition behavior.

The resource history must be described precisely. In the companion protocol, an actual earlier Fast prediction path provides the inherited reserve and remaining source packets. A newly supplied cartridge and installation law create the new learner and retire the earlier task. The earlier predictor's acquired state remains historical; it does not supply the new quotient or transfer its old semantic content into the new target. The semantic acquisition shown here occurs inside the installed learner, from its first predictions through their repair. The lineage/resource join and this new semantic acquisition are both concrete, but they are different achievements; the origin of the installed learning architecture remains supplied.

## 8. Counterexamples and exact scope

**Closed and consistent does not yet mean correct.** The first one-state candidate in section 7 satisfies both finite table conditions and nevertheless fails at \(aa\). Treating those conditions alone as an all-word certificate would be false.

**Present-output equality does not support an update.** Histories \(\epsilon\) and \(a\) initially both output zero in that example, yet the same next action gives different outputs. The acquired suffix distinguishes future behavior rather than merely naming a new current appearance.

**A false bound can produce an accepted wrong hypothesis.** Declare \(N=1\), but use a unary target whose successive outputs are \(0,0,1,1,\ldots\). Its initial table sees only \(\epsilon,a\), both zero, and builds the constant-zero candidate. The final horizon is \(2N-2=0\), so its test succeeds although it fails at \(aa\). The actual target has three reachable states and violates the declared bound. No theorem here licenses the unconditional conclusion outside that bound.

**No bound allows a delayed disagreement beyond every finite transcript.** For any finite set of endpoint tests, let \(H\) be their greatest word length. A zero-output self-loop and a unary chain first outputting one at length \(H+1\) give the same answers to those tests. A finite run cannot certify all future outputs over unrestricted finite targets on that transcript. The earlier [M6 proof](MATHEMATICS-STRUCTURAL-RESULTS.md#proposition-m6--without-the-bound-bounded-perfect-tests-cannot-certify-future-agreement) remains in force.

**A recoded sensor can preserve learning while changing meaning.** A fixed Boolean inversion still supplies a stationary finite Moore observation process. The learner can correctly acquire the inverted output function. A downstream use that treats sensor value 1 as physical readiness despite this inversion is a calibration error; it does not follow that the learned sensor model itself is wrong. The intended question and the decoder linking it to action need independent justification.

**An unreliable reset breaks the history function.** If repeated requests for one word can begin from different unrecorded target phases, cached values need not be values of one \(F:A^*\to O\). The deterministic reset theorem then does not apply. Successful finite comparisons cannot by themselves certify the omitted reset premise.

**Resource extraction changes the whole process.** The phase-readiness target may be stationary even though using a finite source packet depletes the larger environment. The three-state certificate concerns the phase observation law. It is not a certificate that the entire learner-plus-fuel-plus-source process has three states, nor that future extraction remains available forever.

**A cheaper frozen predictor is not an equal learning result.** A comparator that retains the first candidate can pay less by avoiding revision. Once it observes \(aa\), it has evidence that its model is wrong. Its saved expense and its failed continuation must both be reported; neither alone measures the success of acquisition.

**Standard learning is an exact comparator.** A conventional implementation of the same observation-table procedure, endpoint interface and event tariffs should match its learned behavior and its declared charges. Such equality confirms the specified mechanism and exposes its premises; it supplies no evidence that the generative philosophical account uniquely explains or improves on conventional learning.

## 9. Result and integration boundary

The mathematical connection is closed under the stated class and implementation contract: **paid prediction errors can generate new suffix distinctions; those distinctions determine a finite compositional hypothesis; further paid tests can certify its full continuation behavior under a valid finite bound.** The procedure acquires its representative histories and distinction coordinates rather than receiving a correct partition as an input.

The remaining supplied ingredients are concrete: a stationary resettable target, exact observations, the state bound, an installed conventional learning algorithm, workspace and work laws, calibrated meanings, and sufficient accessible resources. Neither the proof nor a successful finite assay establishes how those ingredients arise universally. In particular, a chosen observation and a later useful action do not derive concern for other centers, a general reward, favorable selection, or a unique mathematical foundation.

Acceptance of the executable continuation additionally requires independent checks of its actual observation trace, acquired suffix witness, product-graph equivalence after certification, minimal state count, resource and capacity prefixes, retained result, later paid use and failure cases. The hand proofs establish what a conforming implementation warrants; they do not predeclare that the particular run has passed those checks.

## 10. Implementation review checkpoint

The accompanying [implementation](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/model.py) was inspected against A1–A5. Its closure and consistency repairs, prefix addition, candidate construction, bound diagnostic and exhaustive tests implement the information algorithm above. Its separate endpoint callback is the learner's only target interface; hidden transition tables and external audit traces are not consulted by the learner. A separate internal review checked the suffix-induction and counterexample-progress arguments.

A read-only execution of the unary fixture with initial fuel 36 completed the exact trace in section 7: the observed mismatch at \(aa\) produced suffix \(a\), the retained model had the three cyclic states, and the later word \(aaaaa\) produced a successful use after the largest observed word length was four. The reported peak was 114 abstract cells. A separate run with the falsely supplied bound \(N=1\) returned the wrong one-state model with its conditional test-completion flag set, confirming the stated limitation. These runs start from the specified fuel value; they do not independently replay the earlier Fast history, which the package's broader integration check must establish.

The implementation retains table workspace across intervening endpoint experiments, checks capacity before its committed updates, and prepays its declared work. Its cells and work units are an abstract logical-machine accounting law. They are not a claim that every Python dictionary copy, interpreter allocation or external diagnostic log occupies the indicated number of literal RAM cells or instructions. Correct execution of that accounting law and justification of its chosen tariffs remain distinct from empirical hardware calibration.

This checkpoint supports the correspondence between the hand mechanism and the inspected implementation. The package's independent checker and recorded outcomes determine final assay acceptance; the illustrative executions here do not substitute for that audit.
