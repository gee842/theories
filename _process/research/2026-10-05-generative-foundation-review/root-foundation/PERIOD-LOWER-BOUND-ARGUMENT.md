# A period-independent bound from bounded inquiry strategies

**Subsequent formal continuation:** [the composed proof](PERIOD-GENERAL-PROOF.md) records the implementation and current verification of the original-game correspondence left open below. It uses certified covering families and deletion routes; exact maximal-language completeness is unnecessary. This note preserves the earlier reduction and its narrower receipt.

7 October 2026. AI-authored continuation of [phase-period selection](PHASE-PERIOD-SELECTION.md). This takes up the separate arbitrary-period obligation left there. It does not extend the period cutoff of the old enumeration. It proposes a reduction of **every strategy with at most seven commands, on a cycle of any positive length**, to a fixed language of seven-bit windows.

**Historical status of the argument recorded below:** this is a reviewed mathematical argument with an **incomplete end-to-end Lean proof**. The original Boolean game’s bounded-policy semantics, general preservation under pruning, and exact finite language certificates have been checked separately. The original-game-to-concrete-window/mask correspondence remains unformalized. Under Ren’s requirement that new proof claims be checked in Lean, the proposed arbitrary-period lower bound and selection extension are not yet completed formal results. This concerns local inquiry and conditional selection, not ethical warrant or a derivation of the entire native law.

The [checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/check_period_general.py) freshly builds 12 modules with Lean 4.29.1, with **77 new audited declarations and 387 total audits, all empty and no warnings**. It exactly matches six complete mask sets between the arithmetic Lean implementation and a separate Python implementation using bit operations. The [receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/period-general-verification.json) and [immutable run](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/period-general-runs/20261007T104916.419891Z/verification.json) preserve sources, hashes, compiler identity, raw logs and correspondence output. The [portable exact tables](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/period-general-languages.json) include all 201 seven-command and 44 six-command residual languages and their pruned tables.

The [independent review](PERIOD-REDUCTION-REVIEW.md) also checks the written reduction and [1,020 original-game comparisons](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/period-reduction-review.json), with no mismatch. Those comparisons cover periods one through eight, both targets and constant patterns; they are supplemental checks against the supplied 201-language fixture, not a separate enumeration proving the general claim. That review receipt was regenerated after the final language artifact was written.

**Checked continuation:** the missing original-game correspondence is now completed in [the composed general proof](PERIOD-GENERAL-PROOF.md), with an [independent composition review](PERIOD-GENERAL-PROOF-REVIEW.md). The fresh 21-module Lean 4.29.1 build has 1,183 empty axiom audits. The continuation proves policy coverage using certified covering families rather than assuming exact maximal-language enumeration, and checks the concrete cyclic pruning and period-divisibility bridges. The earlier argument and its narrower receipt are preserved below as the preceding stage.

## Claim and fixed scope

Let a nonempty binary cycle have arbitrary carrier size n. The initial possibilities contain every phase and both values of a fixed, unknown reading inversion. One command either advances by one phase or reads the current bit through that inversion. A strategy may stop early and may choose subsequent commands from its observations. To succeed for a requested bit v, every still-possible start must finish at an actual bit v. The two requested bits may use different strategies. These are the choices represented by `knowsWithin` and `bothKnowableWithin`; no reliable reset is available in this game.

The reviewed written reduction supports the following proposed conclusions. Under Ren’s requirement that new proof claims be checked in Lean, these are **not yet completed general proof results**: the end-to-end original-game/window/mask correspondence remains unformalized.

1. Both requested bits cannot be guaranteed with six commands, at any cycle length.
2. If both can be guaranteed with seven commands, the cycle repeats a two-valued three-bit pattern. Its factor language is that of `001` or its complement, allowing every rotation. Consequently n is divisible by three.
3. A cycle not of that form requires at least eight commands if it can guarantee both requested bits at all. The conclusion includes unidentifiable cycles without assigning them a finite minimum.

The native `001` cycle already has the checked seven-command strategy. Repeating that pattern on a larger carrier gives the same observed bit histories; it need not identify the distinct underlying carrier phases. Thus period-six repetitions remain genuine seven-command examples, as the earlier study required.

## 1. From the knowing-arrival game to a bounded policy

A bounded policy has three forms: stop; advance followed by a policy with one fewer command; or read followed by one policy for each possible observed bit, again with one fewer command. Its success on a particular start is defined by following the actual observations and checking the actual bit when it stops. A policy wins a belief if it succeeds on every candidate in that belief.

Induction on the command bound identifies the Boolean `knowsWithin` recurrence with existence of a winning bounded policy:

- At zero commands, stopping wins exactly when `contactKnown` holds.
- The first disjunct is early stopping.
- The second is an advance and a policy for the mapped belief.
- The last conjunction supplies separate policies for the two filtered reading branches, joined into a read policy.
- An empty belief admits any policy vacuously. This is exactly the empty `allOf` case; neither a nonempty observation branch nor an available actual start is inserted.

The reverse direction follows the same three policy constructors. `knows_iff_policy` in [PeriodStrategySemantics.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/PeriodStrategySemantics.lean) checks this equivalence for every original pattern, period, budget and belief, with 11 empty axiom audits in that module. This is an existence claim about policies, rather than an additional assumption that the controller already knows the true phase.

## 2. Removing leading advances and choosing the first reading branch

Handle constant patterns first: a constant cycle cannot reach the other requested value under any command history, so it never guarantees both values. Now assume both values occur.

No policy that stops without reading can win: advancing only permutes the full set of possible phases, which still contains both output values. Therefore each winning policy has an initial finite sequence of advances followed by its first reading. Before that reading it has no observations on which to branch. An advance maps the full phase/inversion set bijectively to itself. Delete the leading advances and start directly with that reading; the same suffix still has a guarantee over all starts and has at least as much remaining budget.

Choose the suffix reached when the first reading is **zero**. This does not assume the actual first reading is always zero. For every phase i, the candidate with inversion equal to the actual initial bit x_i produces zero, so this one branch must already succeed for a candidate at **every phase**. The policy used after a first reading of one may be completely different; nothing in the proof assumes symmetric first-reading branches.

Write the local actual word as w_j = x_(i+j), with cyclic indices. In this zero-reading branch, every later observation at offset j is w_j XOR w_0. At most six commands remain after the first reading in a seven-command policy, so the position never exceeds six. The seven actual bits w_0,...,w_6 determine the entire residual execution, including any early stop. Repeated readings and advances that skip an intermediate reading are both retained.

For six total commands there are at most five residual commands; retaining seven-bit words simply includes an unused coordinate. No lower bound on n is needed: when n is small, the window wraps around the cycle repeatedly.

## 3. Complete enumeration of residual success languages

There are 128 seven-bit words. For target value one, represent a policy's success set as a subset of these words. At current offset p and residual bound d, let F(d,p) retain the **inclusion-maximal** success languages of every policy. This statement is proved by induction using the following exact recurrence, for p+d≤6.

Let B_p be the set of words whose p-th actual bit is one, and O_p the set whose normalized reading w_p XOR w_0 is one.

- F(0,p) = {B_p}.
- For d+1, form all of the following languages, then discard languages contained in another candidate:
  - B_p, corresponding to stopping;
  - every member of F(d,p+1), corresponding to advancing;
  - (L_0 intersect complement(O_p)) union (L_1 intersect O_p), for independently chosen L_0,L_1 from F(d,p), corresponding to reading and branching.

The implementation also discards dominated languages separately after restriction to each reading branch. This preserves completeness: if A is contained in B, then A intersect C is contained in B intersect C, and replacing either argument of a union by a superset preserves containment. Every policy language is therefore contained in at least one retained candidate. Conversely, every retained candidate is the exact success language of a policy constructed from the same stop, advance and read operations. Discarding dominated candidates changes neither existence of a cover for any belief nor the validity of the retained candidate.

No discarded policy needs to be reconstructed to use the lower bound: the proof only needs the forward coverage implication. Empty restricted languages are retained or dominated under exactly the same inclusion rule, so impossible observation branches do not become obligations.

The resulting counts are:

| Total command bound | Residual bound after first reading | Maximal success languages |
|---|---:|---:|
| 6 | 5 | 44 |
| 7 | 6 | 201 |

A target-zero policy is handled by complementing every actual word bit. Normalized observations are unchanged because complementing both w_p and w_0 preserves their XOR. The same policy then succeeds for target one on the complemented word. Hence target-zero languages are exactly bitwise word-complements of the target-one languages, with no assumption relating the policies chosen for the two targets.

## 4. Cyclic consistency, with arbitrary period

Let W be the nonempty set of length-seven windows occurring around the actual cycle. Every word in W has an allowed successor and an allowed predecessor in W. Encoding chronological bits from least to most significant, the two possible successors of word w are floor(w/2) and floor(w/2)+64. The two possible predecessors are (2w mod 128) and (2w mod 128)+1.

For a candidate language L, one pruning round keeps only words in L with at least one successor in L and at least one predecessor in L. If W is contained in L, then W is contained in the pruned language: use each actual window's actual next and preceding windows as witnesses. Induction preserves this inclusion through any number of rounds. Early exit when the language stops changing also preserves it.

The general preservation statement is checked in [PeriodWindowPruning.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/PeriodWindowPruning.lean), with nine empty axiom audits. Its concrete Nat-mask instantiation remains one of the correspondence obligations below. This is an overapproximation to edges belonging to strongly connected components. Paths joining different recurrent components can survive. No equality with an SCC computation is asserted or needed: retaining extra words makes the exclusion certificate harder to satisfy, not unsound. The argument applies to every cycle length and to all the possible components in a language.

Prune each candidate in F, then retain maximal results again. The 44 six-command candidates reduce to four maximal languages; the 201 seven-command candidates reduce to ten. If a cycle admits both requested-value strategies, its W must be contained in an intersection of a target-one candidate and the word-complement of a target-one candidate representing the target-zero strategy. Prune each such intersection and again retain maximal results. W still survives every step.

## 5. The finite certificates and their proposed general consequence

The six-command computation leaves only the empty mask. Since W is nonempty for every positive n, no cycle can admit both strategies within six commands.

The seven-command computation leaves exactly these two maximal languages, written in chronological bit order:

- {`0100100`, `0010010`, `1001001`};
- {`0110110`, `1101101`, `1011011`}.

The whole W is contained in **one** of these two languages, because each retained maximal language dominates a complete candidate intersection. We are not taking their union as if all words could be freely mixed. Every surviving window repeats after three positions, so x_i = x_(i+3) for every phase. Each consecutive triple contains exactly one one in the first language, or exactly one zero in the second. Summing that count over the n cyclic triple starts counts each one (respectively zero) exactly three times. Therefore n = 3k, where k is the total count of the minority bit. The cycle is a rotation of a repetition of `001` or its complement.

Taking the contrapositive gives the eight-command lower bound for every other cycle, whenever it is identifiable. If the remaining Lean correspondence is completed, this will generalize the old bounded pattern result through the bounded-policy/local-window reduction. Checking short cycles alone does not exhaust longer ones.

## Selection consequence and preserved premises

Extending the period-selection theorem would need only the weaker first conclusion. The following is a consequence of the written reduction, pending its remaining Lean correspondence. Every both-value guarantee has a worst-case requirement of at least seven native commands; for any period greater than three, the supplied retained-cycle representation `1 + 2n` occupies strictly more cells than at period three. With the same other live cells and workspace, the native per-command draw is therefore strictly larger. A favorable realized branch can stop earlier. Multiplying the worst-case command and per-command inequalities gives a strict worst-case draw advantage to the three-phase cycle over every larger carrier that guarantees both requested values. The three-phase native policy attains its seven-command bound. Periods one and two cannot meet the guarantee.

This proposed general selection conclusion still depends on the same command repertoire, unknown full-start belief, fixed inversion, worst-case guarantee, supplied retained-cell representation and draw schedule. Average known-phase alignment remains a different question; the earlier period-five advantage under that measure is preserved. The result does not derive a physical three-cycle from no premises, and it does not provide normative warrant for an objective merely because its implementation draws less material.

## Formal status and remaining Lean bridge

[PeriodLocalCertificate.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/PeriodLocalCertificate.lean) has 57 declarations with empty axiom audits. Twenty-eight DP-cell equalities are checked from their recurrence and earlier checked cells. The pruned-table equalities then check the four- and ten-language tables; the final certificates check the empty six-command joint mask and the two three-edge seven-command masks. The literal tables are proved results of these computations, not accepted inputs. The arithmetic mask operations use structural recursion, avoiding the propositional-extensionality dependency found in the exploratory implementation using standard Nat bit operations.

The receipt distinguishes exact finite evaluation, original-game bounded-policy semantics, and general pruning preservation. All three are separately kernel checked. The mathematical reduction connecting them is reviewed in this note, but its original-game-to-concrete-mask correspondence is not silently imported into the audits.

For a complete arbitrary-period Lean theorem, the following links must also be present: the chosen first-reading branch after removal of leading advances; its relative-reading correspondence with seven-bit window execution; completeness of maximal-language enumeration under domination; and correspondence between the concrete Nat mask operations and set membership, including the invariant that masks fit in 128 bits. The latter invariant follows mathematically from starting with subsets of 128 words and closing under restriction, union, word-complement and deletion. The fixed-width arithmetic routines rely on it when they return a nonzero operand early.

A reviewer should reject the general claim if any policy constructor, branch, admissible start or cyclic window is omitted by this reduction. A mismatch between the independent mask enumeration and the kernel certificate would invalidate the finite certification until repaired. No counterexample has been removed by assuming an intact reset, a known inversion, a primitive period equal to the carrier size, or a connected candidate graph.
