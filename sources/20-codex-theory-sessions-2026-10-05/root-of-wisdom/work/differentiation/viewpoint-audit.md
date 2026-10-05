# Differentiated functional viewpoints inside one process

Constructed for the new differentiation branch, 5 October 2026. This note reads the retained `nonseparation-and-selfhood.md` and `next-root-joint-organization.md` as constraints. It preserves them unchanged. The mathematics below is a deliberately small original construction; it does not claim historical novelty for finite controllers, state estimation, or sufficient statistics. No external literature claim is needed for its proofs.

## The positive explanatory mechanism

A functional viewpoint can arise through a concrete chain:

**different causal contact → differently written internal records → retained differences after contact ends → different conditional predictions → actions that regulate a continuing organization.**

The mechanism is physical copying, retention, and controlled compensation. Its effects are calculated below. We do not begin with a subject possessing a private view and simply rename its perspective. We do supply a sensor–memory–actuator circuit, a criterion of continued functioning, and an asymmetric input field. Thus this explains how differentiated functional viewpoints are produced *given those mechanisms*. Their evolutionary or physical genesis and phenomenal experience are separate burdens. Another part of this investigation must address how the supporting organized units form.

## One finite global dynamics

There are two sites, indexed A and B, with identical local circuitry. The shared field has two disturbance bits \(h=(h_A,h_B)\). A three-phase clock \(\phi\in\{0,1,2\}\), itself a state variable, controls sensing, retention/message exchange, and response. The disturbances remain fixed during a cycle. Each site has a stored bit \(r_i\), a message register \(q_i\), a viability bit \(v_i\), and a body-error bit \(b_i\). A nonviable circuit remains nonviable. A mode bit \(\gamma\) specifies whether the disturbance entering a body depends on its local field bit alone or also on the other field bit.

The updates are:

1. **Sense, phase 0:** a viable site copies its actual local field input, \(r_i\leftarrow h_i\). This overwrites whatever was previously in that register. A nonviable site cannot perform the copy.
2. **Hold/communicate, phase 1:** the current sensor input is a common blank zero, while the stored record persists. If a physical link is enabled and both circuits remain viable, \(q_i\leftarrow r_j\). Otherwise it holds its previous value.
3. **Respond, phase 2:** the circuit produces \(a_i=v_i[r_i\mathbin\oplus(\gamma q_i)]\), the body error becomes

\[
b_i'=a_i\mathbin\oplus h_i\mathbin\oplus(\gamma h_j),
\qquad
v_i'=v_i(1-b_i').
\tag{V1}
\]

The phase advances modulo three. Registers not mentioned at a phase hold their values. All variables and both controllers belong to one deterministic state transition. There is no outside agent selecting the actual response; an intervention used for analysis is distinct from the implemented update. The supplies that physically realize reliable copying, retention, and timing remain premises of this ideal model.

Swapping A and B commutes with the full transition. Thus the laws do not assign one circuit a special perspective or privileged capacity. Different inputs or histories can nevertheless produce different internal states. If the inputs and complete histories are symmetric, the model does not spontaneously force their records to differ. The asymmetry has a specified source rather than arising from a label.

There are 6,144 possible global states in the supplied Boolean model, before choosing whether the message link is enabled. Exact enumeration verifies interchange symmetry for every state and both link settings: 12,288 checks. This is verification of a finite construction, not evidence that every actual being has this architecture.

## The records are different information partitions

Start both circuits viable, with arbitrary old records and body errors. After sensing, \(R_A=h_A\) and \(R_B=h_B\). Their records therefore identify different sets of still-possible field configurations:

| Retained record | Field states compatible with that record |
|---|---|
| A records 0 | 00, 01 |
| A records 1 | 10, 11 |
| B records 0 | 00, 10 |
| B records 1 | 01, 11 |

The partitions result from which field bit was physically copied. They are not independent realities. They are different losses of detail about one field. In a uniform preparation over the four field states, each local record carries one bit about the field and leaves one bit unresolved. These numerical uncertainty statements depend on that declared preparation; the compatibility partitions do not.

At the subsequent hold phase, both current sensor inputs are zero. Their records can still differ because of earlier contact. For example, in field 01, their records are 0 and 1 despite equal current inputs. Present input alone therefore cannot reconstruct the state that determines the coming response. This is a minimal exact role for history in a standpoint.

## Why these records matter to a continuing system

First take local mode \(\gamma=0\). The implemented controller sets \(a_i=r_i=h_i\), so \(b_i'=0\) and both viable states persist for every one of the four field states. The record supports regulation across counterfactual disturbances. The maintained viable state in turn enables sensing and response in later cycles. This supplies an explicit functional loop, albeit with ideal memory and supplied energy/timing rather than a complete organism.

If the entire allowed decision statistic is independent of \(h_i\), no policy can guarantee this compensation. Under the uniform field preparation every deterministic constant action succeeds in exactly half the states. Randomization is a mixture of such policies and cannot improve the average beyond 1/2. This is a statement about a specified information restriction, not a claim that physically deleting one register prevents all imaginable alternate encodings.

We can also intervene on the actual retained record immediately before response. Flipping \(r_i\) while keeping the field and all other states fixed makes that circuit fail and leaves the other viable in local mode. Thus the recorded correlation is used causally for continuation. Merely being correlated with the surroundings is not sufficient for the sense of agency used here. This circuit satisfies the additional operational conditions of retained discrimination, action selection, regulation under varying disturbances, and dependence of future functioning on the regulated state. We do not assert that these conditions are sufficient for consciousness or for every richer concept of a self.

What is relevant differs by site because its maintained state has a different disturbance channel. The local field bit is useful to its own compensation task; the other bit alone is useless for that task under the uniform independent preparation. This is a concrete way in which a shared field acquires different action significance at different organized locations. The local viability condition is supplied by the model, not derived as a universal moral value.

## Exact criterion: when a viewpoint contains the needed distinction

Let \(\Omega\) be a finite set of possible field states, \(R:\Omega\to\mathcal R\) the record actually produced, and \(T:\Omega\to\{0,1\}\) the compensation required. A deterministic policy based only on the record can succeed for every field state exactly when

\[
\boxed{R(\omega)=R(\omega')\ \Longrightarrow\ T(\omega)=T(\omega').}
\tag{V2}
\]

Necessity follows because equal records require the same chosen action. If those states require different actions, at least one fails. For sufficiency, choose the common required action on each record class. With arbitrary preparation probabilities the optimal average accuracy is

\[
\sum_r\max_{t\in\{0,1\}}\Pr(R=r,T=t).
\tag{V3}
\]

The record partition therefore has to preserve the distinctions demanded by the consequence under consideration. This is a consequence-relative adequacy criterion, not a declaration that all retained distinctions are equally important.

For local mode, each record meets the criterion for its own body's continuation. In coupled mode \(\gamma=1\), both bodies instead require \(T=h_A\oplus h_B\). The required classes are \(\{00,11\}\) and \(\{01,10\}\). Neither local record preserves this distinction: for example, 00 and 01 look identical to A but require opposite actions. Every one of the four deterministic one-bit policies has accuracy exactly 1/2; randomization cannot improve it. Failure arises from the missing consequence-relevant distinction, despite a perfectly accurate local record.

This is also a constructive answer to noticing an omitted possibility: **seek two allowed situations that leave the recorded state unchanged but alter the required or predicted consequence.** Finding such a pair proves an omission. It does not supply a guaranteed procedure for finding every unknown pair in the actual world.

## Communication changes which viewpoint is possible

Enable the message link during the hold phase. The other record is physically copied into \(q_i\). The pair \((r_i,q_i)\) now determines the two-bit field, up to the known ordering at each site. The implemented coupled-mode controller sets \(a_i=r_i\oplus q_i\), so both bodies remain viable for every field state. A one-bit message to each site repairs this particular missing distinction.

No omniscient external observer is inserted. Two situated circuits have acquired broader knowledge through a new causal channel. Under the uniform preparation each augmented record carries two bits about the supplied field. Unlimited access is not implied beyond those modeled variables. Conversely, differentiated viewpoints are not necessarily condemned to disagree forever: sufficiently informative interaction can make their relevant predictions agree.

The coupled mode makes this more than two unrelated local examples pasted into a single notation: each body's condition depends on both disturbance ports, and a message carrying the other circuit's acquired record affects its continuation. The distinction between adequate local control and the need for exchange is calculated by the same equations with a declared coupling parameter.

## A restricted operational meaning of self/other

The model distinguishes three relations that ordinary talk about self can conflate:

- **What informs this circuit:** the field bit written into its record and any messages later received.
- **What this circuit directly controls:** varying \(a_i\) at fixed disturbances changes \(b_i'\), while varying \(a_j\) does not. The actuator-to-body intervention matrix is diagonal in this construction, including in coupled mode.
- **What enables its continuation:** the condition \(v_i=1\), maintained through compensation, permits its own later sensing and response.

These relations can be established by the specified transition and counterfactual intervention; an irreducible owner is not among the model variables. They need not coincide in richer systems: a tool can enlarge causal reach, communication can enlarge information, and resource dependence can extend much farther than either. Causal controllability alone therefore does not define an organism or establish moral ownership. The model explains a functional indexical—this record regulates this continuing circuit—conditional on its physical implementation. It does not explain why anything feels like being that circuit.

## Status and exact verification

The script `check_viewpoints.py` and result `viewpoint-checks.json` record:

- 12,288 global site-swap symmetry checks on 6,144 states and two link settings.
- 64 local-mode all-field/old-record/body-state regulation trials.
- 64 coupled-mode communication regulation trials over the same preparations.
- Eight record-flip intervention checks.
- All four local deterministic policies, for both sites and both modes.
- The sufficiency criterion for every one of the 16 binary target functions on the four field states and both local record maps: 32 checks.

The general claims have short proofs above. No physical, biological, human, or artificial consciousness experiment was performed. The result establishes that different functional viewpoints can be generated and used within one explicitly specified process. It neither proves metaphysical monism nor reduces phenomenal first-person experience to information partitions.
