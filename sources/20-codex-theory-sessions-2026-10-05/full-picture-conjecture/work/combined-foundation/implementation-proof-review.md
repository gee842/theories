# Independent implementation and proof review

5 October 2026. Reviewed `implementation/model.py`, `verify.py`, `MODEL.md`, `RESULTS.md`, `results.json`, and all eight graph exports. The baseline combined-process certificate is valid for the declared finite process. No blocking implementation error was found. This review does not promote its supplied clock, calibration apparatus, finite grammar, or productive technology into proved universal mechanisms.

## Independent execution

`implementation-review-check.py` imports only the model, not the author's verifier. It independently traverses every reachable state from the two declared initial states, compares the actual resulting transitions and initial states with each exported graph, and checks payment prefixes, event meanings, payload transmission, hidden-field noninterference, baseline phase assertions, and all six progress ranks. It writes `implementation-review-check.json`; that file records the reviewed source hashes. It does not modify the implementation or any reference repository.

The independent replay exactly matches all eight exports. The baseline has **486 states and 506 edges**, no reachable public violation, no false strict certificate, minimum stored balance **2**, and minimum balance immediately after the debit and before any receipt **1**. Every baseline non-event edge strictly decreases the corresponding phase rank for all six required events. The parent separately checks event-deleted graph acyclicity; this review does not rely on that separate result.

The replay includes unsafe states in the adverse models rather than stopping at the first violation. It finds **122 reachable false strict-certificate states** in the misleading-calibration control. These are distinct graph states carrying a false certificate, not 122 independent experimental observations or distinct episodes.

## Why the six actual events recur

The event phases are declared at `model.py:16`. Every funded microstep advances its phase modulo 23 (`model.py:191`), and the baseline never reaches the resource-stop case (`model.py:135`, `model.py:185`). For an event assigned source phase p, set

`rho_p(s) = (p - s.phase) mod 23`.

Every non-event baseline edge lowers that rank by one. At the corresponding phase, the physical event occurs and the rank resets from 0 to 22. Consequently each event occurs within at most 23 further microsteps from every reachable state, and repeatedly thereafter. Because the declared physical duration is one per paid microstep, the baseline also excludes Zeno accumulation. The clock and duration contract are supplied assumptions, not inferred from an unlabelled graph.

| Event | Actual implementation condition | Why it holds throughout baseline |
|---|---|---|
| `corrective_install` | Phase 15 actually installs a program equal to physical truth, different from the previous installed program, with the strict certificate (`model.py:220`) | The first truth is 1 or 2 while the old program is 0. Later the retained program equals the preceding period's truth, and every boundary chooses a different truth. Exact records and the revised evaluator reconstruct the new truth before admission. |
| `delivered_x0` | Phase 16 actually executes the installed program on context 0 and its result matches the physical law (`model.py:227`) | Fresh exhaustive checking plus within-period stability makes the installed program correct; the execution-block control is absent. |
| `delivered_x1` | The corresponding delivered execution on context 1, at phase 17 | The same correct program remains installed and the law remains stable. |
| `maintained_archive` | Phase 18 writes the actual installed program, evaluator, guard and linked records into a payload (`model.py:234`) | The baseline retains skill, lease, and strict guard, and pays the charge. |
| `trained_successor` | Phase 19 copies the maintained archive into the actual trainee payload (`model.py:239`) | The paid archive exists; training is enabled and its result contains that archive. |
| `competent_handoff` | Phase 20 loads the trainee's payload into the successor's operating fields and changes its carrier label (`model.py:244`) | The trainee equals the retained archive, its guard is strict, and the lease remains active. |

The first event's recurrence genuinely uses the **different-law boundary premise** (`model.py:258`). If that premise were weakened to permit indefinitely unchanged laws, correct service and the other duties could continue while changes to the installed program ceased. That would defeat recurring *correction*, not safe operation. The report correctly states this premise; it must remain attached to the correction claim.

## Formation, evaluation, evidence, and admission

`Observation` omits both the hidden law and the irreversible assessment flag (`model.py:53`). The installed action selector and its helper routines read only that interface (`model.py:107`, `model.py:126`, `model.py:133`). Perturbing the hidden fields while holding the interface fixed leaves its choice unchanged. The transition model's use of physical truth to produce sensor outputs or assess recipient outcomes therefore does not grant that truth directly to the actor.

The generator really constructs a candidate from acquired context-linked bits: `data0 | (data1 << 1)` (`model.py:118`). Without both bits it has only constant candidates. This is bounded program formation under a supplied expression grammar. It is neither an injected answer from the analyst nor invention of an unrestricted grammar. The record-loss control removes the data before selection and consequently produces no conditional-candidate event.

Initially the simplicity-first evaluator selects a constant for either nonconstant initial law. Paid checks detect the mismatch; phase 8 records the mismatch, phase 9 changes the evaluator, and phase 10 then selects the exact record-supported rule. These are different actual state transitions (`model.py:206`–`model.py:217`), not retrospective changes to the analytical score. The mismatch-first evaluator subsequently remains installed and survives handoff. There are two evaluator-amendment edges in the reachable graph, one for each initial uncertainty branch; each baseline path performs the initial amendment once. Rewriting the evaluator infinitely often is neither required nor claimed.

The checks are **fresh paid queries to the same stipulated truthful calibration technology**. They are not independent instruments, independent random samples, or a proof that agreement between checks guarantees external truth in general. Since the law has only two contexts and is constant during the period, querying both contexts is exhaustive within this finite technology. The misleading-calibration control flips both discovery and checking values consistently. It then admits a rule that fits all acquired evidence and fails the unchanged physical criterion. That control correctly exposes the reliability premise rather than concealing it.

The safety envelope is independently assessed. An executed wrong response irreversibly sets `bad=True` (`model.py:232`); evaluator changes, handoff, and the next period do not erase it. The fixed protected predicate reads actual balance and this public flag (`model.py:263`). In the score-capture control, actual admission changes to a simplicity-based guard, so incorrect ordinary actions can occur despite internally favorable ranking. The implemented evaluator amendment concerns evidence-fit and simplicity. It is not moral learning or derivation of the public criterion.

## Paid local invariants and actual transmission

There is one resource ledger. Every executing microstep first debits one token. A work receipt arrives only after that debit; excess receipts are recorded as spill under capacity eight (`model.py:187`). Insufficient funds produces a zero-cost, no-event self-loop. No current action borrows against its own future receipt.

Baseline work at phases 0, 7, 14, and 21 restores the balance to eight; the six intervening charged steps take it to two before the next work phase. Its lowest debit prefix is therefore one, not a hidden negative transient. Generation, checking, amendment attempts, archive maintenance, training, and transfer all pay their specified charges. This establishes exact accounting for the supplied finite cost model. It does not establish realistic physical prices or constant costs for unbounded memory or arbitrary programs.

The successor contents do not come from a correct-answer reset. At phase 18 the archive is formed from current operating fields; at phase 19 the trainee obtains the archive; at phase 20 those trainee fields overwrite the operating program, evaluator, guard, and data. Missing archive or training clears the successor's relevant capabilities and guard instead of regenerating the original defaults (`model.py:252`). The no-maintenance and no-training controls consequently lose service and competent succession after the initial period. This is a real causal transfer dependency in the finite abstraction.

The ledger belongs to the modeled institution and persists across carrier replacement, paying a handoff charge. Separate predecessor/successor bank accounts and a resource-transfer protocol are not modeled. It is accurate to say that the successor operates with the continuing institutional ledger; it would be too strong to claim that a separate-account funding transfer has been checked.

## Supplied infrastructure versus maintained cognition

The fixed Python interpreter, phase-dispatch program, safe auxiliary-work apparatus, calibration response law, and availability of the next phase are supplied transition semantics. Archive preservation does not reproduce or validate all of that physical substrate. In particular auxiliary work and the clock can continue after the modeled cognitive skill becomes false; lease acquisition, record acquisition, candidate formation, strict validation, and mission execution then fail through their skill/lease conditions.

This separation is legitimate and now explicit in `MODEL.md`. The `no_maintenance` control deletes the maintained successor packet, not every form of infrastructure maintenance. The `skilled` bit and payload transfer are a finite abstraction of competence and instruction; they are not a psychological or biological learning theory. Carrier identifiers alternate between 0 and 1. Thus the model certifies indefinitely recurring turnover events, not infinitely many distinct people or newly generated agent identities.

Likewise `competent_handoff` denotes faithful transmission of the retained strict-checking program and modeled capability. It does not imply that a systematically corrupted calibration instrument becomes reliable. The event therefore still recurs in the misleading-calibration control even while physical safety fails. `maintained_archive` and `trained_successor` alone can also preserve bad contents. These facts are reasons to assess the **conjunction** of protection and all required outcomes, not to equate continuity of an institution with correctness.

The score-capture control can deliver correct service in each context infinitely often while also delivering wrong service at other times. Its recurrence entries do not establish safety. Conversely the record-loss, blocked-execution, no-renewal, no-maintenance, and no-training controls can preserve the no-harm criterion by withholding service while failing its continuing duties. The table's separate safety and recurrence columns are necessary and correct.

## Review conclusion

The construction is an actual installed finite controller with causally effective bounded formation, evaluator amendment, paid checks, guarded installation, execution, archive maintenance, instruction, and successor loading. Its successful combined certificate is stronger than separately showing that each ingredient could work or that some external optimizer could choose a successful policy. The explicit environmental and infrastructure assumptions remain premises. This is a valid finite constructive instance of the general combined-process theorem; it is not empirical closure of every biological, social, ethical, or recursively changing future setting.
