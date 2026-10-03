# Engineering evidence gate

`EvidenceRegistry` holds immutable check results. `evaluateEventGate` evaluates a named gate against the **world immediately before** an event. A result is usable only for the same world revision, event ID and action, part and connection, full input fingerprint, check ID, model ID/version/scope, and accepted provenance. A failed or unverified exact result holds the gate. Every named requirement must be satisfied; a passing beam check cannot conceal a missing joint or host check.

The fingerprint is exact canonical JSON of the complete `WorldState` and the supplied `EngineeringInputs`. It includes four explicit external domains: geometry, supports, loads, and capacities. The caller must populate these with the full physical model used by the check: path and seat/obstacle geometry; current and proposed support state; self-weight and imposed/load-case data; and every capacity with its measured or assumed basis and reference. The API rejects absent domains and non-JSON values. It cannot infer an omitted physical load or certify a source document; a solver or reviewer must establish the result and its provenance.

Each submission names the capacity IDs it used. The registry derives `provenance.capacityBasis`: `measured` only if every named capacity is measured, `assumed` if any is assumed, and `none` if no capacity was used. An assumed result needs an explicit assumption. A calculation can therefore be `passed` as a conditional screen while the strict handoff still holds on `capacity-basis-mismatch`. `dependencies` are evidence IDs; each dependency must itself be passed for the same event, revision, part, and fingerprint. Missing, failed, stale, assumed-capacity, or cyclic dependencies hold the parent result.

`createBeamHandoffGates(models)` supplies strict `guide`, `transferLoad`, and `detachHoist` policies. `guide` requires the beam-end connector path, robot-to-beam load contact, and supported hoist load. `transferLoad` requires a beam-frame analysis, strength at each separate end joint, and supporting-frame response. `detachHoist` requires fresh results for the proposed state after hoist release. The policy fixes the required scopes, so the existing axial-truss screen and connector motion screen cannot satisfy beam-frame or joint-strength requirements. Robot contact and mechanical capacities based on assumptions cannot satisfy its measured-capacity requirements. The present demonstration has no measured joint/host qualification and therefore remains held in strict mode.

With an empty registry, strict execution holds at the first `guide` event with three `missing` reasons. An independent frame study at revision 10 has its own event, model scope, geometry, loads, supports, and capacities. Its original result cannot qualify a visible transfer event at another revision or fingerprint. Re-registering that old calculation under the visible event would falsely claim it was checked against the visible inputs and violates this API's provenance contract.

For a strict simulation path, construct `EngineeringInputs` from the current world and the engineering model, register finished results using that same world/event/inputs tuple, then check inside `applyEvent` before cloning or changing custody:

```ts
const gate = strict?.gates[event.action];
if (gate) {
  const inputs = strict.inputsFor(previous, event); // fresh, complete input snapshot
  const decision = evaluateEventGate(strict.registry, previous, event, inputs, gate);
  requireState(decision.allowed, formatGateHolds(decision));
}
```

Keep the reducer's existing state prerequisites and invariant checks. If an asynchronous check finishes after another event commits, registering its original world/event snapshot is safe: the next gate rejects it as stale. Recompute against the new world before attempting another event. Do not stamp an old calculation with the new revision.

For a passing synthetic test result, the call shape is:

```ts
registry.register(worldBeforeEvent, event, inputs, {
  id: 'qualification-001', checkId: 'joint-strength',
  connectionId: worldBeforeEvent.parts[event.partId].connections.A.id,
  model: gates.transferLoad.requirements[1].model,
  status: 'passed',
  provenance: { basis: 'measured', reference: 'test-report-id' },
  capacityIds: ['joint-A'], dependencies: [], detail: 'Measured joint qualification',
});
```

Registration records provenance; it does not perform the underlying joint test. A production caller must only submit `passed` after independently verifying the named model's actual result, and must preserve the report or measurement referenced by the record.
