# Review of the proposed finite-block extension bridge

2026-10-05. This is a sufficient-condition theorem identifying the missing generativity bridge. It is not a newly justified universal premise or a novel-method claim.

## Correct statement

Let a controller's information history include its available observations and executable internal memory. Let W be an independently specified nonempty class of certified information histories, with initial history h0 in W. Each history has an associated finite set L(h) of previously certified novelty labels. Labels and their equivalence criterion must be fixed independently of the conclusion: appending a timestamp alone should not count as substantive novelty unless that is explicitly the chosen target.

Suppose a **single observation-consistent selector** B assigns an executable block policy to every h in W. Its choice cannot depend on hidden physical differences that the actor cannot distinguish. For every allowed hidden state compatible with h and every admitted environment branch under B(h):

1. The whole block remains within the protected conditions, including intermediate states.
2. The block terminates after a positive finite number of steps at a controller-recognizable completion event.
3. The resulting information history h' belongs to W.
4. L(h) is contained in L(h'), and L(h') contains at least one certified label absent from L(h).
5. Block selection, execution, completion recognition, label certification, and memory updates meet all modeled resource and authority constraints.

Then recursively running B at each completion yields a controller that stays protected and produces infinitely many distinct certified labels on every admitted branch, in discrete step time.

If the conclusion concerns unbounded physical time rather than infinitely many discrete steps, also require non-Zeno behavior: cumulative elapsed time diverges. A positive lower bound on block duration is sufficient but not necessary.

## Proof

Induct on completed blocks. h0 is in W by assumption. If hn is in W, the selected policy block terminates on the actual admitted branch at hn+1 in W, protects every intermediate state, and adds a new label. Thus the recursive policy remains defined after every finite number n of completions. Its first n blocks certify at least |L(h0)|+n distinct labels. Each block has positive finite step length, so their cumulative discrete length is at least n and cannot accumulate at a finite discrete index. The concatenated policy therefore has an infinite protected discrete execution with unboundedly many certified labels. The selector and recognizable stopping events make the concatenation an implementable information-respecting controller rather than an omniscient sequence of choices. Non-Zeno behavior supplies the corresponding physical-time statement.

## Essential review points

**The selector condition is load-bearing.** Merely asserting “for every hidden physical history there exists an information-admissible successful block” is insufficient. Different hidden histories may require different first actions while presenting the same observations. Each separately successful policy can be information-admissible; selecting the right one may still be impossible. W should be built on information histories/compatible supports, or the selector must be required to agree across indistinguishable physical histories.

**Every-branch finite completion is stronger than possible completion.** A branch that delays completion forever breaks the induction along that branch. Replacing robust completion by almost-sure completion is a different theorem requiring a probabilistic formulation.

**Observable completion is needed for this implementation.** An external proof that progress happened does not automatically let the controller know when to switch to the next policy block. A controller-recognizable stopping rule or equivalent executable schedule must be supplied.

**This is sufficient, not yet a necessary-and-sufficient characterization.** A successful controller may generate novel but unobservable changes without ever certifying them, or may not admit the stipulated block interface. A converse needs the success target and observations to guarantee the required certification/stopping structure. Avoid importing that converse silently.

**The certificate does not verify reality's membership in W.** Establishing the extension property for a substantive physical or social system remains the substantive work. If W is just defined as all histories admitting the conclusion, the theorem is mathematically valid but supplies no independent model membership test.

**Protection remains a supplied criterion.** The theorem can prove that certified public protections are preserved; it cannot establish the worth of those protections or the physical truth of the transition law by composition alone.
