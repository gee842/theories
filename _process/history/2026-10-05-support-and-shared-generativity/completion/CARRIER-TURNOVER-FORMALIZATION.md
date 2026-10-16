# From original-carrier loss to the turnover ledger

5 October 2026. AI-assisted Lean development for the unchanged 42-channel CF paid-access event vocabulary. Earlier proof sources and numerical experiments are preserved. This closes the original-loss-to-role-wear implication **inside an explicit carrier observer**, then composes it with the existing typed ledger theorem. Refining the complete material-slot implementation into this observer remains a separate obligation.

The main checked conclusion is:

\[
\boxed{\text{all four original carriers lost on a valid marked return}
\quad\Longrightarrow\quad K_{\rm capture}\ge 6+m'-m.}
\tag{1}
\]

The initial and final count states are any \(P_{ij}(m)\) and \(P_{i'j'}(m')\): one fabricator A, one charged capture carrier CF, one gate–Y complex, and the indicated free reserve. Successor types can change. Restoring or increasing reserve gives the six-capture lower bound; spending inherited reserve changes that requirement. The theorem no longer takes four role-wear lower bounds as independent hypotheses.

## 1. The new semantic layer

[CarrierTurnover.lean](../../../../experiments/shared-renewal-capability/formal/CarrierTurnover.lean) imports the frozen [reserve-sensitive source](../../../../experiments/shared-renewal-capability/formal/ReserveTurnover.lean), which imports the frozen [typed event table](../../../../experiments/shared-renewal-capability/formal/TypedRenewal.lean) and pooled ledger. It adds four original identities, named by their entry roles A, C, G and Y.

Each identity is either still present in a declared form, or permanently gone. Live forms are A of either type, C, CF, free Y, G of either type, GF of either type, and the **two separate constituent forms** G-in-YG and Y-in-YG. The distinction prevents a gate wear from being counted as loss of the bound Y, or conversely.

“Gone” describes an original carrier, not an empty material slot. Its material can continue through D, R and newly formed carriers. The observer has no transition that turns a gone original back into a live original. Births create new carriers, not new copies of the entry identity.

These are analyst observations defining a path event. They supply no physical sensor or control input. An experiment that reads carrier identity would need its own implemented and accounted readout.

The `Update` relation explicitly lists every change to a participating live original:

| Event family | Original-carrier change |
|---|---|
| Capture | C becomes CF, retaining identity. |
| CF leakage or any of the three CF paid-access families | CF becomes C, retaining identity. |
| Fuel binding/dissociation or GF leakage | G and GF interconvert, retaining gate identity and type. |
| Y binding/dissociation | Each participating G and Y enters or leaves its own constituent form. |
| Bound G wear | The gate original is lost; the original Y is released as the same Y. |
| Bound Y wear | The Y original is lost; the original gate is released as the same G. |
| Free A/G/C/Y wear or charged GF/CF wear | The affected original is lost. |
| Retained catalysts, newly produced carriers, recycling and nonparticipants | An existing original observation is unchanged. |

The table has no type-0 bound-reproduction event because the imported typed vocabulary has none. All free-F channels and exactly the three declared paid-access families remain present; optional bound copying, CF-catalyzed free-F recycling and added reverse chemistry remain absent.

An unchanged observation is permitted for every event. It covers retained catalysts and originals not selected by that reaction assignment. This is intentionally permissive: the observer does not choose particles or remember which particular G is bonded to which particular Y.

## 2. What a valid marked history means

`MarkedTrace` couples the concrete typed count history to the observer. Every step must satisfy the imported count-level enabledness condition and its actual stoichiometric update. Each original must make one of the listed observation updates. Every live original must be present in the corresponding count species at each state. Initially its observer form is the one specified by the organizational entry.

Role consistency is **derived**, not imposed as a conclusion at each later state. The event table preserves the original's functional role until loss. In particular, a live C original may alternate between C and CF, and a live G or Y may bind and dissociate, without becoming a different role. Permanent loss follows directly from the absence of any update out of “gone.”

This observer overapproximates the [material-slot semantics](CARRIER-SEMANTICS.md). Individual presence does not establish a globally consistent assignment to distinct material participants or the pairing of G/Y observations in complexes. For example, independently permitted observations can fail to record that two particular originals were bound to one another. The extra histories cannot invalidate a necessary accounting inequality proved for **every** observer history. They do prevent treating an observer history as a constructive physical path.

The new Lean file does not prove that Python's slot transitions refine `Update`, nor does it formalize Python execution. The earlier exact finite slot/rate check remains separate evidence for that implementation. The compositional statement is therefore precise: the original-carrier-to-ledger implication is now a machine theorem for the declared observer; its application to a physical or implemented labelled process still needs a sound refinement into that observer.

## 3. The checked induction

Let \(b_r\) be zero while original \(r\) remains live and one after its loss. Let \(w_r(e)\) indicate a wear of role \(r\) in the imported event table. Lean proves from the explicit `Update` constructors that

\[
b_r'\le b_r+w_r(e),
\qquad b_r=1\Longrightarrow b_r'=1.
\tag{2}
\]

The substantive case is the first change from live to gone. The only constructors that permit it are the matching free or bound wear reactions, and the affected live form has the corresponding role. Binding, reproduction, formation, recycling and capture cannot manufacture such a loss or resurrect the original.

Induction over an arbitrary finite enabled marked history gives

\[
b_r^{\rm final}\le b_r^{\rm initial}+\sum_e w_r(e).
\tag{3}
\]

All four initial bits are zero. If all four final originals are gone, (3) yields at least one A wear, one C wear, one G wear and one Y wear. This is the implication that the earlier ledger theorem required from outside Lean.

The marked history also projects to an enabled `TypedRenewal.Trace`. The imported accounting theorem then supplies

\[
K_{\rm capture}\ge 6+W_{\rm final}-W_{\rm initial}
\tag{4}
\]

whenever total A and total gate counts are restored. Since the work ledger at an organization is \(W(P_{ij}(m))=5+m\), (4) yields (1). This is the declared packet/work accounting quantity, not a calibrated thermodynamic free-energy lower bound.

The file additionally proves `all_gone_continuation`: after all originals have gone, **every later enabled typed history** lifts to an observer history with all four marks still gone. Later wear is permitted, and material reuse or type changes never clear an original-loss mark. Thus the bookkeeping does not impose a hidden rule rejecting repeated wear after a first successful replacement.

The theorem concerns finite histories. A stopped first-successor event is a subset of those histories and may use the same necessary bound, but the Lean file does not define a stopping time, a CTMC or an event probability.

## 4. Verification and preservation

The dedicated [checker](../../../../experiments/shared-renewal-capability/formal/carrier-check.py) verifies the three frozen dependency hashes, builds them into a temporary import directory, and compiles the new source with Lean 4.29.1 and its standard library. No dependency was installed. Dependency compilation was necessary for this new proof; no scientific experiment or probability propagation was rerun.

The [execution record](../../../../experiments/shared-renewal-capability/formal/carrier-lean-verification.json) saves source, checker, compiler, toolchain, dependency-object and output hashes. The [compiler output](../../../../experiments/shared-renewal-capability/formal/carrier-lean-output.txt) records successful compilation and the printed theorem dependencies. There are no `sorry` placeholders, custom axiom declarations or native evaluation shortcuts. The final accounting theorems use Lean's standard `propext`, `Quot.sound` and `Classical.choice` foundations; this is not an “axiom-free” claim.

To reproduce from the repository root:

```text
PYTHONDONTWRITEBYTECODE=1 python3 experiments/shared-renewal-capability/formal/carrier-check.py
```

That command replaces only the dedicated carrier execution records and removes its temporary imported objects. It preserves the earlier source and record files.

The completed formal layer establishes permanent original-loss semantics, the four wear implications and their reserve-sensitive ledger consequence. Material-slot refinement, exact labelled rates, truncation and probability certification, carrier identification in a molecular implementation, and any capability or universal-direction claim remain outside this proof.
