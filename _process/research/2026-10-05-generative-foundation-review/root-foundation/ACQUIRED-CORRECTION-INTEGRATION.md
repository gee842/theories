# 取得纠正路线，而非预先给定 / Acquiring correction routes

8 October 2026, Asia/Bangkok. AI-authored continuation of Ren's “continue” following the [four completed alignment contributions](ALIGNMENT-CONTINUITY-INTEGRATION.md). This round adds **24 Lean theorems, 45 explicit-declaration audits and 25,284 matched executable records**. Twenty-one declaration audits have empty axiom lists; the remaining lists contain only standard `propext`, `Quot.sound` and/or `Classical.choice`. This is a conditional theoretical construction with author counterreview, not independent acceptance or deployed-AI validation.

**中文结论。** 纠正不必总从一个预先列出的成功路线菜单开始。一个逐项实际读取的程序可以形成新的地址，区分“已找到”“给定可达范围已穷尽”与“预算不足、尚未查完”，并将搜索、复查和实际执行的消耗接成同一账目。取得的路线须按当前配置复查，当前权限也须重新核验。成功的局部见证不必覆盖未知全体；否定性的穷尽结论有更强范围条件。忠实读取、扫描期间固定的有限可达结构、事先允许的检查和原子执行仍为前提；制度俘获不由凭据匹配解决。

## The connection and prior results

The previous package selected inquiry and responses from supplied alternatives and executed correction. Its remaining question concerned acquisition of warranted new evidence and response options. This study closes a narrower, useful part: **inspection-driven formation of a previously unlisted correction address, with charged search and present-tense execution checks**. It does not claim to have completed every part of that remaining question.

The [model-revision cycle](MODEL-REVISION-INTEGRATION.md) already generates competing repairs from acquired residuals under a declared grammar; it is not being rediscovered. The [handoff result](CORRECTION-HANDOFF-INTEGRATION.md) already acquires and renews records while maintaining an active route. The [review-coverage result](SELECTOR-REVIEW-COVERAGE-INTEGRATION.md) distinguishes finite audit success from warranted generalization. Here the new join is discovery → a concrete route witness → resource-accounted revalidation → the inherited actual command protocol. Search and response do not inhabit separate realities: inspecting the installation changes available records and consumes the very capacity later needed to correct it.

## Operational representation and supplied premises

The substrate is an arbitrary finite binary tree. A node is closed, a command endpoint with a Boolean delivery key, or a fork with two child handles. The binary form is a declared local interface, not a foundational account of organizations. An address is an arbitrarily long finite Boolean path. The learner starts with the root handle and a query allowance. It is not handed a successful address, an uncertainty set covering all possible installations, or a list of every endpoint.

The executable `scan` maintains a frontier of address/handle pairs. It inspects only the next handle, charges one unit, removes a closed node, returns an endpoint, or puts the newly obtained children on the frontier. Child addresses arise by extending the observed path. `nodes`, the size of the complete tree, is used for a proof bound; the search procedure does not evaluate it. A symbolic subtree in Lean represents a handle whose contents become available when inspected. This is a specified read interface, not an implementation of physical sensing or an opaque-pointer security proof.

Three return values remain distinct:

- `found(ticket)`: an address and delivery key have been acquired.
- `exhausted`: the reachable frontier is empty.
- `pending`: work remains but the query allowance is spent.

The discovery theorem assumes faithful, nondestructive, atomic reads and a fixed topology during that scan. The inspection interface is assumed to be permitted; the command credential does not itself authorize every possible investigation. Acyclicity and finiteness are supplied. There is no theorem about discovery in arbitrary cyclic graphs, a topology changing during traversal, noisy sensing or unrestricted invention of new kinds of operation.

`acquire` first checks that its query allowance fits both remaining work and time, then charges the number of nodes actually inspected. It conservatively declines an allowance it cannot fund, even if that particular tree might yield a cheaper result. The accounting charges inspections; it is **not a bound on CPU instructions, allocation, path copying or all physical costs**. The formal work and time units need a deployment correspondence.

After acquisition, the topology and authority may have changed arbitrarily. `dispatch` re-reads the proposed address in the **current** topology. It allocates and charges `path length + 1` inspection units, retaining this charge even on a mismatch or revoked authority. This is a conservative path-check charge; an early failure can require fewer actual reads. If that allocation cannot be funded, dispatch does not start. It checks that the current key matches the ticket, the request is signed, its credential matches current authority, and three command units and steps remain. Then it invokes the unchanged `EffectiveCommand` issue/deliver/enact protocol.

The actual endpoint supplies the backend's `openRoute` field; the proposed key remains the ticket's key. Thus the connection describes delivery through the currently inspected endpoint, not a mutation that makes an incorrect ticket correct. Update, replacement and shutdown retain their inherited effects. Revalidation and subsequent command execution form one transaction with respect to further topology/authority changes. No concurrent physical race or queued-request fairness is proved. Existing overlap-handoff results retain their separate scope.

## Checked implications

The [Lean module](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/AcquiredCorrection.lean) proves the following principal connections.

| Result | Exact reach |
|---|---|
| `scan_budget`, `acquired_accounting` | Search uses at most its allowance; actual inspection charges are retained in reserve, expenditure and time. |
| `discovered_route_is_real` | A ticket produced from the faithful fixed root locates an actual endpoint with that key. No complete uncertainty family is supplied. |
| `exhausted_is_scoped_absence` | Genuine frontier exhaustion implies no endpoint in that frontier's reachable subtrees. Budget exhaustion does not have that implication. |
| `sufficient_budget_finishes`, `reachable_route_is_found` | An allowance at least the number of nodes finishes; if an endpoint exists, some real ticket is returned. No adequate-allowance selection algorithm is thereby supplied. |
| `positive_witness_needs_no_complete_map` | Two reads find the left endpoint of a fork for **every** possible finite right subtree, which is never read. |
| `successful_dispatch_is_current` | Any successful dispatch has a matching endpoint in the current topology, a signed request and current credentials, even if its ticket was generated incorrectly. |
| `dispatch_completes`, `acquired_execution` | A real current ticket, current signed authority and sufficient remaining capacity produce actual completion with exact successful accounting. |
| `complete_finite_discovery_and_execution` | For a reachable tree of size `N`, work and remaining time at least `2N+3` suffice for search with allowance `N`, current path inspection and actual command completion. |

The last bound follows from at most `N` discovery reads, at most `N` reads on a real endpoint path, and three inherited command steps. It is sufficient, generally loose, and not an optimality theorem. `N` is a condition in the completeness theorem, not information inferred by the program before searching. Operational runs may use any affordable finite allowance and keep `pending` if it is insufficient.

The partial-map theorem supplies a positive witness, not coverage of all possible consequences of using it. Command behavior and the endpoint interface remain supplied. Nor does an exhausted reachable tree establish that no route exists outside its accessible root, or that future construction cannot make one.

## Constructed successes and failures

The worked tree has a closed left child and a right fork whose left child is the endpoint. The address `[true,false]` is formed after four reads; no path is supplied to the search. Three units recheck it and three execute shutdown, giving total expenditure ten and `running = false`.

With only nine units, discovery still succeeds. After rechecking, only two remain, so command execution is refused; the seven consumed units remain visible. This is a concrete reason to reserve response capacity when planning inquiry. In this model, knowing a route and being able to use it differ.

Revoking authority between discovery and dispatch refuses execution while retaining seven units of discovery and recheck expense. Flipping the endpoint key rejects the stale ticket. With newly valid authority and a fresh observation of the changed key, correction succeeds. These are explicit construction checks; the model does not itself decide or create the institution's rightful renewal.

The final countermodel replaces authority and credential together with a new accepted epoch and retains the represented signature. The technical gate accepts the request. **If capture obtains what the gate accepts as current credentials, epoch equality supplies no further protection.** This is not a model of how capture occurs or a cryptographic exploit. It isolates exactly what authentication fails to establish: whether the authority is justified.

## Verification and source assessment

The [checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/check_acquired_correction.py) builds a fresh temporary closure under Lean 4.29.1, compiling unchanged `AlignmentInquiry` and `EffectiveCommand` before the new module. It audits all 45 explicitly named declarations and stores theorem signatures, axiom reports, source snapshots, compiler hash and log hashes in the [receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/universal-ethics/generative-capacity/acquired-correction-verification.json). The 24 theorems are new; inherited theorems are not recounted. No custom axiom, `sorry`, `admit`, `native_decide` or skipped kernel check is used. Definitions and interface interpretation still carry substantive premises.

The executable companion enumerates all 147 binary substrates of depth at most two with closed/false-key/true-key leaves. Ten allowances yield 1,470 search records. Three commands, six work/time profiles, three topology continuations and three signing/authority states yield 23,814 acquisition/dispatch records. A separately written **iterative stack** reference checks the recursive Lean search, and explicit arithmetic checks every emitted execution result, running/completed flags, remaining work, expenditure, time and update/replacement counts. All **25,284** records match. These are same-author finite implementation comparisons, not independent research, empirical measurements or substitutes for the general proofs.

Ordinary depth-first search and runtime revalidation deserve full credit; no new search algorithm or performance advantage is claimed. Necula and Lee's primary [proof-carrying-code account](https://www.usenix.org/legacy/publications/library/proceedings/osdi96/full_papers/necula/html/node2.html) and [safety-policy specification](https://www.usenix.org/legacy/publications/library/proceedings/osdi96/full_papers/necula/html/node3.html) were read in full for these two web sections. They already distinguish supplied operational policy, certification and checking before use. Our ticket is an observed address, **not proof-carrying machine code**; the comparison credits the established validation strategy and its declared semantic premises. The previous study's primary [human-control comparison](ALIGNMENT-CONTINUITY-INTEGRATION.md#primary-comparisons-and-read-scope) remains applicable. This is targeted comparison, not an exhaustive novelty search.

## Ethical connection, substantive counterreview and closure

Under the already completed G0/J account, justified correction concerns consequences for living and further formation, with legitimate participation and bounded responsibility. An institution's inability to name a route today does not itself show no corrective action is possible. Acquiring an actual alternative can change practical feasibility. Conversely, investigation that consumes the last capacity needed for an already justified response can worsen the practical situation. This is an application of the completed practical account, not a new axiom saying that every search or every authenticated command is good.

**The strongest objection is that the trusted inspection law does much of the epistemic work.** Correct. What has been derived is the route address, the scope of its evidential consequence, and the coupled accounting/execution result. The law's actual reliability is still supplied. Revalidation protects a positive execution against a stale or spurious ticket under the current read law; it does not make a corrupted sensor trustworthy or prevent false-negative reporting from hiding a route. Normative evaluation also requires a faithful account of consequences beyond successful command delivery.

**“The model knows the whole tree.”** The semantic description supplies a complete finite substrate so the theorem has a target. The search operationally examines only reached handles, and the arbitrary-unread-subtree theorem verifies one limit on what it consults. This is a meaningful distinction within the model, but no claim that the physical installation has been inferred from nothing. Cycles and unknown future operation types require another interface and proof.

**“You solved changing authority.”** Only the boundary between current accepted credentials and stale credentials is mechanized. Legitimacy, renewal and capture remain substantive institutional questions evaluated under G0/J. The capture countermodel prevents a stronger conclusion.

**Closed scope:** acquired route formation and affordable execution on the stated interface are now reusable results. The next unresolved connection is **warrant for the real inspection-and-enforcement relation when sensing or authority issuance can be manipulated**. It requires a concrete fault/intervention model and evidence or institutional argument; adding a predicate called “trustworthy” would repeat the premise. General repertoire expansion, adversarial synchronization and captured-authority resistance remain open, while earlier ethical grounding and successful local mechanisms stay completed.

**Further continuation, 8 October 2026.** [Correction under partial compromise](FAULT-TOLERANT-CORRECTION-INTEGRATION.md) now supplies a concrete bounded-fault extension: 37 additional Lean theorems / 68 audits and 85,680 matched records. It tolerates covered deviations in readers and issuers while retaining current route and delegated-command guarantees, with exact availability and explicit correlated-capture failures. Real fault coverage, a protected monitor and legitimate mandate formation/revision remain the unclosed correspondence and governance questions. The 24 / 45 acquired-route result is unchanged.
