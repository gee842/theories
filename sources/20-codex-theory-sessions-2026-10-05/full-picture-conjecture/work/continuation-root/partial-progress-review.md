# Independent review: hidden-progress obligation reduction

5 October 2026. Read-only audit of `partial_progress_verify.py`, its imported `progress-check.py`, saved results, and the proposed breakpoint interpretation. I did not rerun the 4,608-case enumeration. The new main report was not yet present when this initial review was written; a later addendum can review its phrasing.

## Verdict

**No mathematical or implementation defect found in the inspected reduction.** For a finite known plant with deterministic observations, common finite action labels, adversarial successor choice, and sure safety plus physical-state Büchi recurrence, the belief/obligation construction is sound and complete with the proof below. It must not be presented as ordinary belief-target substitution, probability-one synthesis, or proof of unbounded novelty.

This review verifies source logic and the general correspondence. The saved enumeration checks the constructed game against a separate positional-strategy/cycle oracle and checks extracted policies on concrete plant/controller paths. It does not enumerate arbitrary-history observation policies directly; the correspondence proof and the perfect-information Büchi theorem are what justify that wider quantifier.

## 1. Correct state meaning and initialization

`B` is the exact nonempty information set given the action/observation history. The allowed states have one common observation and lie entirely in the safe set. `O⊆B\P` tracks current states of compatible histories that have **not yet visited progress P during the current obligation phase**.

Initialization at `(B0,B0\P)` is correct: initial physical states already in P have met this first phase's obligation; the other possible initial states have not. This does not reveal the true hidden state. The controller can compute the subsets using the known model and observation history.

An empty O does not claim every current physical state lies in P. Different possible paths may have visited P at different times. This is why the construction accepts the hidden deterministic alternation that an ordinary target `B⊆P` incorrectly rejects.

## 2. Correct update and failure handling

For action a and observed next symbol y, write `B′=Post_a(B)∩h⁻¹(y)`.

- If O is nonempty, `O′=(Post_a(O)∩h⁻¹(y))\P` keeps exactly the still-unfulfilled histories.
- If O is empty, `O′=B′\P` starts a fresh phase at the successor.

The implementation matches these equations. Merging an already-fulfilled and an unfulfilled history at the same physical state correctly keeps that state in O until the still-unfulfilled history reaches P; the shared state cannot justify forgetting that obligation.

If an action is unavailable at **any** state in B, the constructed action goes to an unsafe sink. This correctly makes the action unusable for a sure guarantee. It is not allowed merely because it works in the actual but hidden state. An empty plant successor is treated as unavailable, not as vacuous universal safety.

Every nonempty observation branch is included. If a branch's updated belief contains any unsafe state, it goes to the sink. Unsafe successors are not silently deleted. Empty observation updates are impossible branches and are correctly omitted. The sink is nonprogress and unsafe with a self-loop, so it cannot accidentally satisfy recurrence.

## 3. Why the Büchi objective on empty obligations is equivalent

**From the product to the plant.** An observation controller can implement the product state and its chosen action without knowing the actual hidden state. If O becomes empty infinitely often, then each concrete path visits physical P during every completed phase (apart from any harmless initialization convention for the first phase). Otherwise that path's current state would remain represented in O. Thus all concrete paths are safe and visit P infinitely often.

**From the plant to the product.** Lift any sure-winning observation-history policy to histories of the constructed game. Suppose an allowed infinite product history eventually never empties O. From the last reset (or initialization), every later nonempty obligation contains the endpoint of a compatible path that has avoided P throughout that phase. These finite avoidance paths form a finitely branching tree with arbitrarily long branches. König's lemma supplies an infinite compatible physical path avoiding P thereafter. That contradicts the original policy's sure recurrence. Therefore the lifted policy visits empty O infinitely often.

The observation history used for lifting is recoverable from the product history because every nonempty B has one observation label; the actions are retained in the history as well. The construction does not grant hidden information to the lifted policy. A deterministic memoryless strategy suffices in the resulting finite perfect-information Büchi game, producing a finite-memory observation controller for the plant. The finite-state/finite-branching premise is doing real work here.

Sure winning is the intended quantifier: every successor path is admitted, without environmental fairness. A path that forever postpones progress is a counterexample even if a separate probabilistic interpretation would assign it probability zero. Private randomization does not rescue a sure guarantee against every compatible outcome of that randomization.

## 4. Extracted physical certificate

The imported fixed-point solver rejects empty actions. Its rank certificate selects actions that remain in the winning set at progress states and descend through finite reachability ranks otherwise. The separate cycle oracle enumerates positional choices, checks reachable unsafe/deadlocked nodes, and rejects any reachable cycle wholly outside progress.

The partial-observation checker goes further than checking the product's empty-O objective. It constructs nodes `(actual physical state x, controller memory m)` for every x compatible with a winning memory state. Each edge uses the selected controller action, an actual allowed plant successor, and the corresponding observed-memory update. It verifies that the successor lies in the same certified product and then applies the cycle oracle with the **physical** progress predicate `x∈P`.

This supplies the requested certificate against all concrete environmental paths. The physical graph may include more memory/state pairs than are reached from one chosen initial information set; checking all of them is conservative and not a hidden-information shortcut. The selected policy never needs the physical x coordinate that the audit uses to check it.

## 5. Exact scope of the reported counts

The saved result records:

- 256 two-state/two-action plants, allowing empty successor masks;
- two observation partitions;
- nine progress/safety pairs `P⊆K⊆S`;
- hence **4,608 exhaustive plant/observation/predicate cases**;
- **11,520** constructed belief/obligation states and **3,962** certified physical/controller states accumulated over those exhaustive cases.

Two additional named examples run afterward: hidden alternating recurrence succeeds, while a hidden adversarial stuttering option defeats the guarantee. Thus **4,610 total calls** is accurate if explicitly described as 4,608 exhaustive cases plus two examples. The state/certificate totals exclude those two extra calls because the script does not add their returned counts to the accumulators.

All saved checks pass. The review did not independently rerun these totals, and no claim of proof-assistant validation or empirical replication follows.

## 6. Required interpretation guard

The theorem characterizes safe recurrence of an independently declared finite-state progress predicate. It can model repeatedly successful repair, service, revision or challenge response when those events are faithfully specified. It does not establish infinitely many distinct achievements, new concepts, changing semantics, ethical improvement, or universal applicability to all real systems.

With a fixed finite novelty-label set, there can be only finitely many first occurrences. A finite controller can nevertheless generate unbounded artifacts or nonperiodic outputs when the output/history space is unbounded; that possibility is not refuted by a finite-label result. Neither direction should be collapsed into the recurrence theorem.

A claim about worthwhile ongoing generation therefore needs both the proved strategy characterization and a separately supported interpretation of P, the protected set, controller resources and environmental model. This qualification preserves the positive theorem: it now covers hidden progress under partial observation, rather than promising semantic novelty by renaming recurrent visits.

## Files inspected

- `/Users/ren/Documents/Codex/2026-10-05/full-picture-conjecture/work/continuation-root/partial_progress_verify.py`
- `/Users/ren/Documents/Codex/2026-10-05/full-picture-conjecture/work/continuation-root/progress-check.py`
- `/Users/ren/Documents/Codex/2026-10-05/full-picture-conjecture/work/continuation-root/partial-progress-results.json`
- `/Users/ren/Documents/Codex/2026-10-05/full-picture-conjecture/work/continuation-root/progress-and-sources.md`
- `/Users/ren/Documents/Codex/2026-10-05/full-picture-conjecture/work/continuation-root/formal-continuation.md` (relevant safety/hidden-progress boundaries)

Only this review file was added by this audit; all inspected sources and saved results were read only.
