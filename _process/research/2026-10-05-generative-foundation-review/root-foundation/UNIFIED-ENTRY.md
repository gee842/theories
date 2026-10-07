# One process: which packages are connected

7 October 2026. This is the working table for Ren's goal of formal unification: one Lean entry in which the process law, contact formation and acquisition, the three-phase cycle, U1/U2, renewal–closure, valuation development and the alignment modules all apply to the same generative process. Each connection must be a proof that a package's notions are realized by that process, not a restatement.

The process is the packet port as the core derives it ([process-law derivation](PROCESS-LAW-DERIVATION.md)), extended by recovery and formation ([contact-formation study](CONTACT-FORMATION-LAW.md)) and by the reading it retains (the revising port). All modules listed as connected audit completely empty: no `propext`, no `Quot.sound`, no other axiom. The [contact-formation checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/check_contact_formation.py) builds them together with the 32-module core: 46 modules, 801 audits, all empty.

## Packages

| Package | Status | The proof that connects it | What still separates it, and the next step |
|---|---|---|---|
| Process law and native port (32-module core) | **Base** | `GenerativeDerivedProcessLawModel`; every core declaration audits empty (GenerativeCore 28/28, Depletion 5/5) | None for this table. Remaining inputs (gate formula, rates) are tracked in the dependency map's §7 ledger |
| Three-phase cycle | **Connected** | `PhaseCycleDerivation` is stated on the port's own `Phase`, `nextPhase` and `execute` (`native_advance_represented`, `phase_recurs_whole_does_not`); the revising port's inquiry uses the cycle and needs its two rotations (`other_output_after_two_rotations`) | Period selection and the cycle's requirements are being grounded in a separate thread |
| Contact formation and acquisition | **Connected** | The extended port is the native process extended by recovery and formation; the inquiry is a native trace (`Inquiry.trace`, `inquiry_port_trace`) | The formation event is proved necessary and minimal (`change_requires_formation`, `unconsumed_formation_unbacked`); its draw is not yet derived; the recovery rate is with the grounding thread |
| Valuation development | **Connected** | In the revising port one history is both the valuation organization's run and an actual port history (`memory_trace`, `port_trace`); every organization embeds in the core (`ValuationInCore.trace_iff_run`) | Only the deterministic package is connected; the probabilistic and lineage results are not yet instantiated on the port |
| Alignment (`InquiryRelevance`, `InquiryWarrant`) | **Connected on its definitions** | `PortAlignment`: the port's response table is the package's `Pair Bool`; the inquiry is its faithful test (`inquiry_reads_table`); relevance and transfer adequacy hold on the port's family (`port_query_sufficient_iff`, `transfer_adequate_iff`) | Located mismatches, proved: the port realizes three tables, not four (`table_never_both`), and there an arrival settles the whole table (`arrival_settles_table`); the decision to form lies outside the package's one-entry continuations (`formation_outside_continuations`). The package's own theorems still use `propext`/`Quot.sound`, so they are restated, not imported |
| U1/U2 (sustain law) | **Partly connected, not on main** | The native port is a U1 instance on the rename branch (`NativePortContinuation.port_sustain_law`, `port_cannot_continue_indefinitely`) | After the rename merges: show recovery and formation are also supported stages, so the whole revising port satisfies U1 and its potential falls on every step |
| Renewal–closure | **Separate** | No instance yet | The port is one organization drawing on a finite source; renewal concerns populations of kinds with finite spans. Candidate bridge: show the formed contact opens more than its formation draws, so the port's deadline comes from its finite source and not from shortfall |
| Ethical naturalism | **Separate** | No instance yet | Candidate bridge: evaluate the revising and unrevised histories (`revision_changes_continuation`) under the whole-history property |

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
| Decision rule, two probes at different outputs, intact reset, reading after acting | **Proved necessary** (`decision_rule_unique`, `one_output_cannot_decide`, `broken_reset_cannot_decide`, `disposition_stale_then_recovers`) |
| A non-native formation event; consuming a recovered pair | **Proved necessary** (`change_requires_formation`, `unconsumed_formation_unbacked`) |
| Formation draws the native interface demand | Still assumed. No current result needs it. It should be settled with U1 for the whole port: either a result needs it there, or it is dropped |
| Formation as one event, rather than a rearrangement of the port's own material | Put to Ren as a decision; work proceeds on keeping it as one event, proved minimal |
| Recovery rate of ten wasted units per pair | Still assumed; being grounded in a separate thread |
