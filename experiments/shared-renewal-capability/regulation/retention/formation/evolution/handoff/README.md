# Finite support handoff, actual failure and completion

7 October 2026, Asia/Bangkok. AI-authored supporting construction for the [practical Liangzhi investigation](../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/LIANGZHI-PRACTICAL-ARGUMENT.md), following [Ren's positive 生生 direction](../../../../../../../sources/15-codex-theory-conversations/2026-10-07-shengsheng-ethical-direction.md). [Mathematical scope and correspondence](../../../../../../../_process/research/2026-10-05-generative-foundation-review/history/root-foundation/LIANGZHI-PRACTICAL-MATH.md).

This local process forms an activity and its support relationship from initially unassembled material. A second support assembly is then built, connected and actually used before the first is dismantled; a later operation through the second completes the same activity. The first support can end while work remains, and the finite activity later genuinely completes and ends. The work produces three material products, rather than merely clearing a pending flag.

The process contains six material units and finite operational support. Each support assembly and the work assembly occupies one unit; each successful operation turns a loose unit into a product. Dismantling returns assembly material. Every actual event consumes one operational-support unit. [SupportHandoff.lean](SupportHandoff.lean) proves material conservation and exact support consumption for all admitted finite histories, alongside the complete finite witnesses.

Four comparisons remain explicit:

- **Replacement tested before removal:** actual replacement work precedes removal; further replacement work completes the activity with no failed attempt.
- **An actual attempt after early removal:** using the removed connection produces no product, consumes support and increments `failedAttempts`. A later replacement can recover completion; the earlier failed occurrence remains in that same history.
- **Replacement after removal, before another attempt:** this also completes without failure. The law has no clock or continuous-demand event, so an unsupported interval alone does not create a failed operation. Replacement before removal is not necessary in this model.
- **Finite completion without replacement:** all three products can be formed through the original support, followed by completion and dismantling. With seven support units this route is feasible while the declared ten-event handoff word is not. That bound concerns the stated word, not every possible handoff.

[SEMANTICS.md](SEMANTICS.md) fixed the meaning before the first Lean check and records the review-added comparison. Assembly recipes, operation laws, connections, quota and numerical costs remain supplied local inputs. This is a new finite process using the established generative and occurrence interfaces; it is not a refinement of `FormedSelection`, a biological implementation or a controller for the four ethical cases. First/second mark formation order and interface positions within one process. No theorem derives a moral obligation from dependence, equates a failed operation with experienced harm, ranks overall generativity, or makes producing the quota necessary for every justified cancellation or ending.

[verification.json](verification.json) records a fresh Lean 4.29.1 build of four modules and **65 audited declarations**, including **20 new declarations**. Ten new declarations have empty named-axiom reports; the others use only standard `propext` and, for the arithmetic results, `Quot.sound`. No custom axioms, placeholders or unchecked native evaluation are used. [check.py](check.py) binds the compiler, unchanged inherited sources, new source, semantic contract, checker and logs by SHA-256.

```sh
python3 experiments/shared-renewal-capability/regulation/retention/formation/evolution/handoff/check.py
```

The passed attempt is [1791378712930201000](checks/1791378712930201000/receipt.json). Preserved failures include [a checker preflight error](checks/1791378482224854000/receipt.json), [the first Lean elaboration attempt](checks/1791378482401590000/receipt.json), and [a case-binder error in the support proof](checks/1791378575636007000/receipt.json). The preflight scanned an inherited comment as code; it did not invoke Lean. The later repairs changed proof implementation and names, preserving the stated event laws. The additional delayed-replacement comparison was requested by review and checked under those same laws.
