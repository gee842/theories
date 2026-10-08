# Deriving the packet process law from its native activity

6 October 2026. AI-assisted continuation of Ren's request to derive the process law, after the [inquiry-premise discharge](DERIVED-INQUIRY-PREMISES.md). This follows the [nondual method](../../../../theories/becoming/chapters/NONDUAL-METHOD.md): examine how a particular organization of activity produces its effective possibilities, retaining the relations that the coarse description omitted. A locally supplied law is not thereby external to generative reality.

The concrete target is the previously stipulated one-packet inquiry law. Its three represented targets, probe table and depletion are derived from the pre-existing executable apparatus's source conversion, contact gate and subsequent receipt acquisition. This is a derivation of an effective law from an independently implemented finer mechanism. The primitive cycle, gate and accounting rules of that mechanism remain inherited inputs; the origin of every fundamental law is not declared solved.

The named connection is **organized native activity → conditions of completion and actual effects → effective inquiry law**. The original source already specifies more than the desired macro table: it includes capacity failure, interface charges, source exhaustion, actual arrival, receipt inversion and failure after conversion. Those consequences constrain the derivation and prevent an arbitrary favorable table from being substituted.

## The independent source and its order

The source is [the existing diagnosis port](../../../../experiments/integrated-correction/general-framework/generative-basis/mathematical-abstraction/acquisition/access/diagnosis.py), with its retained three-phase cycle and default tariff. The old inquiry graph and criterion checks used this source's permissive informational comparison; they did not yet prove that their macro transition table followed from native command execution. The earlier [prediction protocol bridge](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/learning/PredictionProtocolBridge.lean) already demonstrates a different native-to-macro derivation and is preserved as prior work.

[NativePacketProcess.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/NativePacketProcess.lean) reconstructs the port call without importing the one-packet target classes or table. Its source, fuel, retained accounting totals, phase and fault coordinates remain in one configuration. It distinguishes a completed call from an interrupted call and retains the configuration actually reached by interruption.

The native probe proceeds in this order:

1. Check capacity and fund the interface operation.
2. Check whether at least ten source units remain.
3. Consume ten units and determine actual arrival from the current contact configuration.
4. Credit the actual arrival or retain the failed conversion's waste.
5. Check and fund the separate acquisition of the receipt.
6. Return the receipt, including any existing inversion fault.

No anticipated arrival funds the first interface operation. An actual arrival can fund its later receipt. Failure to acquire a receipt does not restore the source or reverse an arrival that already occurred. A depleted probe can incur its interface charge before reporting unavailable source. These are effects of the inherited code, not newly inserted exceptions.

## The completion law follows from that sequence

The exact default scale-one tariff has an integer representation: 65,536 fuel ticks per unit. If the call retains `live` cells and `workspace` temporary work cells, its capacity demand and each interface/receipt bill are

\[
p=\mathrm{live}+\mathrm{workspace}+2,
\qquad c=16{,}384+p.
\]

Let \(F\) be starting fuel, \(S\) source, and \(g\) the credit from the actual arrival: 655,360 ticks on arrival, zero otherwise. The probe's completed-command guard is

\[
p\leq\mathrm{capacity},\qquad c\leq F,\qquad 10\leq S,
\qquad c\leq F-c+g.
\]

Its completed source and fuel are \(S-10\) and \(F-c+g-c\). The guard must be established before reading these natural-number subtractions as an executable operation. The native execution derives the condition and the endpoint together; a promised successful macro action is not an input.

The `Process` in this native module represents **completed commands**. Failed attempts remain in the executor's explicit stopped results and their separate theorems. Omitting them from completed-command edges is not a claim that they produced no effects. Diagnostic preparation, belief commitment and later retention outside the port call are separate operations in the source; the present extraction does not fund or implement them automatically.

## Deriving the three classes and two probes

[PacketLawDerivation.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/PacketLawDerivation.lean) begins with the native gate

\[
\mathrm{arrival}(x,\tau,b)=(x\mathbin{\mathrm{xor}}\tau)\land\neg b,
\]

where \(x\) is the current learned phase output, \(\tau\) readiness reversal and \(b\) blocked contact. The possible pairs of responses at \(x=0\) and \(x=1\) are derived:

| Native configuration | Response at 0 | Response at 1 | Derived class |
|---|---:|---:|---|
| Open, no reversal | 0 | 1 | A |
| Open, reversed | 1 | 0 | B |
| Blocked, either reversal | 0 | 0 | C |

Equality of these response profiles is proved equivalent to equality of the A/B/C class. Both blocked configurations remain represented. Thus the three transfer-response classes and their probe table follow from the native gate; they are not three primitive kinds added to the native executor.

These are transfer-response classes, not unconditionally complete observational classes of the whole apparatus. Ordinary readings also involve sensor parity. The proof identifies that parity explicitly; equal phase and equal parity give equal ordinary readings. A receipt equals actual arrival exactly when its inversion flag is absent. Calibration has not been obtained merely by renaming the receipt as evidence.

The native cycle reaches either requested learned output after at most two `a` commands. A usable alignment must execute those commands with their actual charges; specifying a phase in a proof is not permission to reset or teleport to it. The macro comparison retains its declared zero-or-ten source domain. A completed probe from twenty source units leaves ten; another completion still requires funding. That source cannot be silently treated as a one-packet configuration.

For the selected alignment schedule, let \(n\leq2\) be its number of rotations and \(g\) the actual arrival credit at the aligned probe phase. The direct guard is

\[
p\leq\mathrm{capacity},\qquad (n+1)c\leq F,\qquad 10\leq S,
\qquad c\leq F-(n+1)c+g.
\]

The first \(n\) charges fund the actual rotations; the next funds probe dispatch. Only then can arrival credit fund receipt acquisition. `alignment_guard_iff_native_guards` proves the direct guard equivalent to the sequential rotation and probe guards. The proof constructs a native `Trace` through each paid rotation and the completed probe. It tracks the initial representative's actual phase and resource changes while retaining its fault coordinates; it does not substitute a favorable configuration.

This schedule is calculated from the native phase. It realizes either requested output from a known common phase; it does not establish that a learner has acquired that phase. The guard can also depend on hidden arrival conditions. An exact mathematical feasibility criterion is not an installed observable admission policy, and its funding threshold concerns this particular command schedule rather than every possible protocol.

## Which effective law is derived

Within the calibrated, admitted one-packet protocol, the completed probe retains the original target class, consumes the packet and returns the corresponding macro response. The endpoint and observation are derived from native execution. The protocol tracks each native representative's actual phase and resource changes and retains its fault coordinates; a favorable representative cannot replace a failed starting configuration.

The central results are `profile_equal_iff_target_equal`, `probe_complete_iff`, `probeReady_exact`, `completed_probe_projects` and `aligned_probe_realizes_macro`. The first derives the transfer-response classes; the next two characterize actual completion and its ordered resource conditions; the last two establish the completed-call projection and the paid alignment implementation. Source amount, receipt calibration and starting phase describe the regime being compared. They have not been erased from the theorem statements or proved necessary properties of every generative process.

The old comparison also grants common denial after depletion and arbitrary common-control observations. Those grants are a permissive abstraction. The original native code raises source unavailability and can already have spent interface resources. Its different completed control commands change phase or acquire a reading while retaining source; they must not all be represented as physically free actions. Consequently the derivation does not claim unrestricted equality between every permissive macro transition and a native event.

This distinction retains the old impossibility proofs. Extra noninformative macro permissions made those negative results stronger, but do not by themselves prove positive native implementation. The new derivation identifies the actual successful interface and its real failure branches.

## The remaining foundation

The independent native mechanism is still an executable study model. Exact correspondence with its Python source is not empirical identification of a physical system. Its three-phase cycle, contact gate, source conversion unit, tariffs, fixed fault coordinates and receipt mechanism remain to be related to formation and maintenance within a broader realization. No added Lean axiom justifies those choices.

This advances the existing explanation because the macro law is constrained by an independently specified mechanism with additional testable effects, rather than being redefined in another notation. It locally discharges the macro table's status as an independent input. It does not discharge all upstream explanatory content or establish a unique universal dynamics. The earlier carrier-underdetermination results retain their limited scope; they do not refute the richer activity-first account.

The next derivation is **formation and revision of the contact, access and retained-evidence organization → changed effective inquiry law**, joining the existing construction/applicability histories where their interfaces actually match. That inquiry must retain the acquired organization, its actual conditions and failures. Whole-process significance remains governed by the current generative grounding programme, rather than by a favorable outcome or private return in this packet model.

## Verification and integration

The public [GenerativeDerivedProcessLawModel.lean](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/GenerativeDerivedProcessLawModel.lean) imports the previous derived-inquiry model and the native law, macro derivation and correspondence cases. A fresh isolated build with pinned Lean 4.29.1 passes **32 modules and 599 audits, all with empty axiom dependencies**. All 409 earlier audited declarations and their source bytes are retained. The 190 additions comprise:

| Module | Audited declarations | What is checked |
|---|---:|---|
| `NativePacketProcess` | 45 | Independent native executor, completion/failure conditions and effects |
| `PacketLawDerivation` | 51 | Derived response classes, exact chosen-schedule guards, paid trace and macro correspondence |
| `NativePacketCases` | 94 | 93 grouped closed certificates covering 5,928 original-command cases, plus their common case predicate |

The additions include 146 theorems, of which 93 are generated case groups, 36 definitions, one abbreviation, six inductive types and one structure. Audit counts describe declarations, not independent empirical findings. Every new named declaration has an explicit audit; the import-only public entry introduces none. The checker rejects undeclared dependencies, warnings, proof placeholders and nonempty axiom reports.

The [correspondence checker](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/check_native_packet_correspondence.py) executes fresh instances of the original `Port.command` and emits its results as closed Lean cases. Its independent Python reconstruction compares all represented coordinates plus the original logs and historical peak. It uses the saved learned machine from the original handoff rather than rerunning its learning. The [saved report](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/native-packet-correspondence.json) includes all phases and fault combinations, source amounts zero through twenty, capacity boundaries and chronological funding boundaries. It retains 318 receipt-funding failures after conversion and 1,416 source-unavailability failures. This finite source correspondence is separate from the universal statements proved about the Lean reconstruction and from physical empirical validation.

The [immutable combined receipt](../../../../experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/process-law-runs/1791291483950888000/receipt.json) has SHA256 `2dd47104443f4eb3495f6336438a3ca8a3171eab5c67a69379588a1d581a37a0`. It binds all 32 source snapshots, compilation logs, compiler, both checkers, the 12 original native evidence files and the 16 preserved earlier evidence files. It uses a fresh temporary build without local precompiled imports. Original scientific producers and their saved results remain unchanged; only new port-call fixtures were executed. The [independent review](PROCESS-LAW-DERIVATION-REVIEW.md) checks the mathematical scope and the evidence chain.

Reproduce from the repository root:

```sh
python3 experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/check_native_packet_correspondence.py
python3 experiments/integrated-correction/general-framework/generative-basis/lean/inquiry-root/sufficiency/check_process_law.py
```

The first regenerates the current correspondence report and closed cases from unchanged original sources. The second preserves earlier contracts and creates another immutable fresh-build receipt. The [owned integration edits](PROCESS-LAW-DERIVATION-EDITS.json) identify this round's insertions into shared documents. [Documentation and evidence checks](PROCESS-LAW-DERIVATION-CHECKS.json), produced by [the reconciliation checker](PROCESS-LAW-DERIVATION-CHECK.py), verify those fragments, links and accepted hashes without repeating the scientific or Lean runs.
