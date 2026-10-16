# One process: which packages are connected

7 October 2026. This is the working table for Ren's goal of formal unification: one Lean entry in which the process law, contact formation and acquisition, the three-phase cycle, U1/U2, renewal–closure, valuation development and the alignment modules all apply to the same generative process. Each connection must be a proof that a package's notions are realized by that process, not a restatement.

The process is the packet port as the core derives it ([process-law derivation](PROCESS-LAW-DERIVATION.md)), extended by recovery and formation ([contact-formation study](CONTACT-FORMATION-LAW.md)) and by the reading it retains (the revising port). The earlier [contact-formation checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/check_contact_formation.py) builds its connected packages together with the 32-module core: 46 modules, 801 audits, all empty. The separate [finite-renewal continuation](PORT-RENEWAL-LAW-CLOSURE.md) has 41 new audits: 21 empty and 20 using `propext` and `Quot.sound`, with no `Classical.choice` or custom axioms. Its arithmetic is not included in the earlier empty-dependency count.

## Packages

| Package | Status | The proof that connects it | What still separates it, and the next step |
|---|---|---|---|
| Process law and native port (32-module core) | **Base** | `GenerativeDerivedProcessLawModel`; every core declaration audits empty (GenerativeCore 28/28, Depletion 5/5) | None for this table. Remaining inputs (gate formula, rates) are tracked in the dependency map's §7 ledger |
| Three-phase cycle | **Connected; arbitrary-period inquiry bound checked** | `PhaseCycleDerivation` uses the port's own phase/execute law. `PeriodGeneralProof` proves the seven-command lower bound and three-periodicity consequence on the original game for every positive carrier | [PhaseRecoveredContact](PHASE-RECOVERED-CONTACT.md) acquires phase and composes contact inquiry without reset. The [completed period proof](PERIOD-GENERAL-PROOF.md) removes the old upper cutoff from conditional draw selection; the supplied advance/read game, retained-cell representation and worst-case criterion remain explicit |
| Contact formation and acquisition | **Connected** | The extended port is the native process extended by recovery and formation; the inquiry is a native trace (`Inquiry.trace`, `inquiry_port_trace`) | [Whole-port review](WHOLE-PORT-CONTINUATION.md) removes formation draw as a necessity for conservation/termination. Pair consumption and the local conversion/recovery rule remain explicit; minimality is relative to the tested target |
| Valuation development | **Connected** | In the revising port one history is both the valuation organization's run and an actual port history (`memory_trace`, `port_trace`); every organization embeds in the core (`ValuationInCore.trace_iff_run`) | Only the deterministic package is connected; the probabilistic and lineage results are not yet instantiated on the port |
| Alignment (`InquiryRelevance`, `InquiryWarrant`) | **Connected on its definitions** | `PortAlignment`: the port's response table is the package's `Pair Bool`; the inquiry is its faithful test (`inquiry_reads_table`); relevance and transfer adequacy hold on the port's family (`port_query_sufficient_iff`, `transfer_adequate_iff`) | Located mismatches, proved: the port realizes three tables, not four (`table_never_both`), and there an arrival settles the whole table (`arrival_settles_table`); the decision to form lies outside the package's one-entry continuations (`formation_outside_continuations`). The upstream axiom-removal work is now on main. This entry retains its proved table/continuation mismatches; axiom removal alone does not complete further composition |
| U1/U2 (sustain law) | **Connected through completed extended/revising histories** | `WholePortContinuation.extended_sustain_law`, `revising_sustain_law`, exact trace conservation and finite-source bounds | No intact-reset premise is needed. Completed-edge bounds do not cover infinite failed retries; the drawless rival also terminates. See [the continuation](WHOLE-PORT-CONTINUATION.md) |
| Renewal–closure | **Exact finite replenishment; direct contact-only identification fails** | `PortRenewalLawClosure.finite_encounter_horizon`: under its intact-open schedule and funding premises, exactly `n` completed encounters are possible iff `20n ≤ initial source`; source bounds also cover arbitrary completed histories | [The mapping audit](PORT-RENEWAL-LAW-CLOSURE.md) proves contact-only aging/support and full inverse obstructions. It states sufficient conditions for a richer forward correspondence; that correspondence is not yet instantiated. Indefinite encounters require a different source-support law |
| Ethical naturalism | **Actual-history representation connected; ethical order unresolved** | `IntegratedPortContinuation.acquired_loop_has_one_supported_history` places support and the `ActualRecovery` contact profile on the same adaptive run | Contact opening is not necessarily restoration after loss. Eventual possibilities alone omit actual interruption; neither profile counts nor successful inquiry establish ethical warrant |

**Merged continuation, 7 October 2026:** the [integration and reviewed limits](MERGED-OBLIGATIONS-INTEGRATION.md) supersede the earlier merge blockers and connect acquired phase, whole-port support and an actual contact profile on one history. Local connection completion does not establish renewal closure or ethical warrant.

**Latest continuation:** [the three-obligation report](OPEN-OBLIGATIONS-CONTINUATION.md) records the exact finite renewal result, completed arbitrary-period proof and unsuccessful universal-warrant shortcut. Neither the finite renewal theorem nor the period proof supplies ethical warrant.

## Splits

The dependency map's §8 checks splits against the one process. This entry settles these:

| Split | Status | Proof |
|---|---|---|
| Ordinary activity and formation | **Derived** for every process: a step either keeps a coordinate or changes it, and every history is a history of that cut | `RelationalCut.cut_trace_iff`, `change_needs_changing_step`; on the port, redundant formation keeps the contact (`redundant_formation_keeps`) |
| Deciding organization and mechanism | **Derived**: the decision is a step of the same process, and its rule is the unique one that works | `RevisingPort.memory_trace`, `decision_rule_unique` |
| Retained reading and the rest of the state | **Derived**: the reading is one more coordinate, set apart only because encounters alone change it | `reading_changes_only_at_encounters` |
| Organization and world (valuation package) | **Derived** on the port: the presented condition is the port's own contact coordinate and the consequence law is native execution | `encounter_effects`; see also the valuation thread's joint-process result |
| Test and tested table (alignment package) | **Derived** on the port: the table is the port's profile and the test is its own probe | `inquiry_reads_table` |

## Inputs of this entry

| Input | Status |
|---|---|
| Decision rule, two probes at different outputs, phase knowledge and reading after acting | Earlier necessity results retain their protocol scope. Intact reset is necessary for the old schedule, **not for inquiry generally**: `PhaseRecoveredContact` acquires phase from readings without reset. Its decoder and observation access remain supplied |
| A non-native formation event; consuming a recovered pair | **Proved necessary** (`change_requires_formation`, `unconsumed_formation_unbacked`) |
| Formation draws the native interface demand | Retained in the original local law; **not necessary for U1 or termination**, as the capacity-guarded pair-consuming drawless rival proves. A different material rank also bounds its revising histories |
| Formation as one event, rather than a rearrangement of the port's own material | Put to Ren as a decision; work proceeds on keeping it as one event, proved minimal |
| Recovery rate of ten dissipated units per pair | Still a supplied material conversion in this connected port. Current support/recognition results do not derive its unique necessity |
