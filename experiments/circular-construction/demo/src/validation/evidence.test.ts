import { describe, expect, it } from 'vitest';
import { createBeamScenario } from '../scenarios/beam';
import { applyEvent } from '../simulation/engine';
import type { ExecutionEvent, WorldState } from '../domain/types';
import { createBeamHandoffGates } from './beamHandoff';
import { EvidenceRegistry, evaluateEventGate } from './evidence';
import type { EngineeringInputs, EvidenceSubmission, GateDefinition, GateRequirement } from './evidence';

const models = {
  connectorMotion: { id: 'connector-sweep', version: '2' },
  robotBeamContact: { id: 'beam-contact', version: '1' },
  hoistLoad: { id: 'hoist-load', version: '1' },
  beamFrame: { id: 'beam-frame', version: '3' },
  jointStrength: { id: 'joint-strength', version: '2' },
  hostFrame: { id: 'host-frame', version: '1' },
} as const;
const gates = createBeamHandoffGates(models);

function before(action: ExecutionEvent['action'], occurrence = 0,
  failure: 'none' | 'mis-seat' = 'none'): { world: WorldState; event: ExecutionEvent } {
  const scenario = createBeamScenario({ failure });
  let world = scenario.initialWorld;
  let found = 0;
  for (const event of scenario.events) {
    if (event.action === action && found++ === occurrence) return { world, event };
    world = applyEvent(world, event);
  }
  throw new Error(`No ${action} event ${occurrence}`);
}

function inputs(capacityBasis: 'measured' | 'assumed' = 'measured'): EngineeringInputs {
  return {
    geometry: { beamSection: 'synthetic measured 3 m section', seatProfile: 'synthetic two-end fixture' },
    supports: { fixtureStiffness: 'synthetic measured', proposedUnassistedState: true },
    loads: { selfWeightN: 915.273, imposedN: 1200, gravityMS2: 9.81 },
    capacities: Object.fromEntries(['beam', 'joint-A', 'joint-B', 'host', 'robot', 'hoist'].map(id => [id, {
      value: { designLimitN: 5000 }, units: 'N', basis: capacityBasis, reference: `synthetic-${capacityBasis}-${id}`,
    }])),
  };
}

function capacityId(requirement: GateRequirement): string[] {
  if (requirement.acceptedCapacityBases.includes('none')) return [];
  if (requirement.checkId === 'joint-strength') return [requirement.connection === 'A' ? 'joint-A' : 'joint-B'];
  if (requirement.checkId === 'robot-beam-contact') return ['robot'];
  if (requirement.checkId === 'hoist-load') return ['hoist'];
  return [requirement.checkId === 'host-frame' ? 'host' : 'beam'];
}

function submit(registry: EvidenceRegistry, world: WorldState, event: ExecutionEvent,
  engineeringInputs: EngineeringInputs, requirement: GateRequirement, overrides: Partial<EvidenceSubmission> = {}) {
  const connectionId = requirement.connection === 'part' ? null : world.parts[event.partId].connections[requirement.connection].id;
  const submission: EvidenceSubmission = {
    id: `${event.id}:${requirement.id}`, checkId: requirement.checkId,
    connectionId, model: requirement.model, status: 'passed',
    provenance: { basis: 'calculated', reference: 'synthetic test calculation' },
    capacityIds: capacityId(requirement), dependencies: [], detail: 'Synthetic test result only',
    ...overrides,
  };
  return registry.register(world, event, engineeringInputs, submission);
}

describe('versioned engineering evidence gate', () => {
  it('holds the first guide with an empty strict registry', () => {
    const { world, event } = before('guide');
    const decision = evaluateEventGate(new EvidenceRegistry(), world, event, inputs(), gates.guide);
    expect(decision.allowed).toBe(false);
    expect(decision.holds.map(item => [item.requirementId, item.code])).toEqual([
      ['connector-path', 'missing'], ['beam-contact', 'missing'], ['hoist-supported-guide', 'missing'],
    ]);
  });

  it('holds a real beam transfer until every named beam, two-joint, and host check exists', () => {
    const { world, event } = before('transfer-load');
    const engineeringInputs = inputs();
    const registry = new EvidenceRegistry();
    for (const requirement of gates.transferLoad.requirements.slice(0, 3))
      submit(registry, world, event, engineeringInputs, requirement);

    const held = evaluateEventGate(registry, world, event, engineeringInputs, gates.transferLoad);
    expect(held.allowed).toBe(false);
    expect(held.holds).toEqual([expect.objectContaining({ requirementId: 'host-frame', code: 'missing' })]);

    submit(registry, world, event, engineeringInputs, gates.transferLoad.requirements[3]);
    const passed = evaluateEventGate(registry, world, event, engineeringInputs, gates.transferLoad);
    expect(passed.allowed).toBe(true);
    expect(passed.acceptedEvidenceIds).toHaveLength(4);
  });

  it('keeps an assumed-capacity calculation conditional and never treats it as measured qualification', () => {
    const { world, event } = before('transfer-load');
    const engineeringInputs = inputs('assumed');
    const registry = new EvidenceRegistry();
    const requirement = gates.transferLoad.requirements[0];
    const result = submit(registry, world, event, engineeringInputs, requirement, {
      provenance: { basis: 'calculated', reference: 'synthetic assumed-capacity screen',
        assumptions: ['Beam resistance declared for exploration, not measured'] },
    });
    expect(result.status).toBe('passed');
    expect(result.provenance.capacityBasis).toBe('assumed');

    const conditionalGate: GateDefinition = { id: 'conditional-screen', version: '1', action: event.action,
      requirements: [{ ...requirement, acceptedCapacityBases: ['assumed'] }] };
    expect(evaluateEventGate(registry, world, event, engineeringInputs, conditionalGate).allowed).toBe(true);
    const handoff = evaluateEventGate(registry, world, event, engineeringInputs, gates.transferLoad);
    expect(handoff.allowed).toBe(false);
    expect(handoff.holds).toContainEqual(expect.objectContaining({
      requirementId: 'beam-frame', code: 'capacity-basis-mismatch',
    }));
    expect(handoff.holds).toContainEqual(expect.objectContaining({ requirementId: 'joint-A', code: 'missing' }));
    expect(handoff.holds).toContainEqual(expect.objectContaining({ requirementId: 'host-frame', code: 'missing' }));
  });

  it('rejects a late async result from the earlier guide revision', async () => {
    const first = before('guide', 0, 'mis-seat');
    const second = before('guide', 1, 'mis-seat');
    const engineeringInputs = inputs();
    const registry = new EvidenceRegistry();
    const requirement = gates.guide.requirements[0];
    const delayed = Promise.resolve().then(() => submit(registry, first.world, first.event, engineeringInputs, requirement));
    await delayed; // The result arrives after the caller has advanced to the second guide.
    const decision = evaluateEventGate(registry, second.world, second.event, engineeringInputs, gates.guide);
    expect(decision.allowed).toBe(false);
    expect(decision.holds).toContainEqual(expect.objectContaining({
      requirementId: 'connector-path', code: 'stale-revision',
    }));
  });

  it.each(['failed', 'unverified'] as const)('holds an exact %s result', status => {
    const { world, event } = before('transfer-load');
    const engineeringInputs = inputs();
    const registry = new EvidenceRegistry();
    const requirement = gates.transferLoad.requirements[0];
    submit(registry, world, event, engineeringInputs, requirement, { status });
    const gate: GateDefinition = { id: 'beam-only', version: '1', action: event.action,
      requirements: [requirement] };
    const decision = evaluateEventGate(registry, world, event, engineeringInputs, gate);
    expect(decision.holds).toContainEqual(expect.objectContaining({ code: status, requirementId: 'beam-frame' }));
  });

  it.each([
    { name: 'truss scope', change: { model: { id: models.beamFrame.id, version: models.beamFrame.version,
      scope: 'axial-truss-screening-only' } }, code: 'scope-mismatch' },
    { name: 'wrong model version', change: { model: { id: models.beamFrame.id, version: 'old',
      scope: 'installed-beam-frame' } }, code: 'model-mismatch' },
    { name: 'wrong connection', change: { connectionId: 'will-replace' }, code: 'connection-mismatch' },
  ])('rejects $name', ({ change, code }) => {
    const { world, event } = before('transfer-load');
    const engineeringInputs = inputs();
    const registry = new EvidenceRegistry();
    const requirement = code === 'connection-mismatch'
      ? gates.transferLoad.requirements[1] : gates.transferLoad.requirements[0];
    const overrides = code === 'connection-mismatch'
      ? { connectionId: world.parts[event.partId].connections.B.id }
      : change;
    submit(registry, world, event, engineeringInputs, requirement, overrides);
    const gate: GateDefinition = { id: 'single', version: '1', action: event.action,
      requirements: [requirement] };
    expect(evaluateEventGate(registry, world, event, engineeringInputs, gate).holds)
      .toContainEqual(expect.objectContaining({ code }));
  });

  it('rejects a connector screen submitted in place of a beam-frame result', () => {
    const { world, event } = before('transfer-load');
    const engineeringInputs = inputs();
    const registry = new EvidenceRegistry();
    const requirement = gates.transferLoad.requirements[0];
    submit(registry, world, event, engineeringInputs, requirement, {
      checkId: 'connector-motion', model: { id: models.connectorMotion.id, version: models.connectorMotion.version,
        scope: 'beam-end-guide-path' }, capacityIds: [],
    });
    const gate: GateDefinition = { id: 'beam-only', version: '1', action: event.action,
      requirements: [requirement] };
    expect(evaluateEventGate(registry, world, event, engineeringInputs, gate).holds)
      .toContainEqual(expect.objectContaining({ requirementId: 'beam-frame', code: 'missing' }));
  });

  it('rejects a result registered for a different part', () => {
    const { world, event } = before('transfer-load');
    const engineeringInputs = inputs();
    const registry = new EvidenceRegistry();
    const requirement = gates.transferLoad.requirements[0];
    const fixtureEvent = { ...event, partId: 'fixture-A-left' };
    submit(registry, world, fixtureEvent, engineeringInputs, requirement);
    const gate: GateDefinition = { id: 'beam-only', version: '1', action: event.action,
      requirements: [requirement] };
    expect(evaluateEventGate(registry, world, event, engineeringInputs, gate).holds)
      .toContainEqual(expect.objectContaining({ code: 'part-mismatch' }));
  });

  it('rejects an independent revision-10 result for the visible transfer', () => {
    const scenario = createBeamScenario();
    let studyWorld = scenario.initialWorld;
    for (const event of scenario.events.slice(0, 10)) studyWorld = applyEvent(studyWorld, event);
    const studyEvent = { ...scenario.events[10], action: 'transfer-load' as const };
    const visible = before('transfer-load');
    const engineeringInputs = inputs();
    const registry = new EvidenceRegistry();
    const requirement = gates.transferLoad.requirements[0];
    submit(registry, studyWorld, studyEvent, engineeringInputs, requirement);
    const gate: GateDefinition = { id: 'beam-only', version: '1', action: 'transfer-load',
      requirements: [requirement] };
    expect(evaluateEventGate(registry, visible.world, visible.event, engineeringInputs, gate).holds)
      .toContainEqual(expect.objectContaining({ code: 'stale-revision' }));
  });

  it('checks exact fingerprints, dependencies, and immutable stored results', () => {
    const { world, event } = before('transfer-load');
    const engineeringInputs = inputs();
    const registry = new EvidenceRegistry();
    const requirement = gates.transferLoad.requirements[0];
    const mutableModel = { ...requirement.model };
    const saved = submit(registry, world, event, engineeringInputs, requirement, {
      model: mutableModel, dependencies: ['missing-joint-check'],
    });
    mutableModel.scope = 'changed-after-registration';
    expect(saved.model.scope).toBe('installed-beam-frame');
    expect(Object.isFrozen(saved.model)).toBe(true);
    expect(Object.isFrozen(saved.dependencies)).toBe(true);
    const gate: GateDefinition = { id: 'beam-only', version: '1', action: event.action,
      requirements: [requirement] };
    expect(evaluateEventGate(registry, world, event, engineeringInputs, gate).holds)
      .toContainEqual(expect.objectContaining({ code: 'dependency-missing' }));

    for (const changed of [
      { ...engineeringInputs, geometry: { ...engineeringInputs.geometry, seatProfile: 'changed' } },
      { ...engineeringInputs, supports: { ...engineeringInputs.supports, proposedUnassistedState: false } },
      { ...engineeringInputs, loads: { ...engineeringInputs.loads, imposedN: 1201 } },
      { ...engineeringInputs, capacities: { ...engineeringInputs.capacities,
        beam: { ...engineeringInputs.capacities.beam, value: { designLimitN: 4999 } } } },
    ] as EngineeringInputs[]) {
      expect(evaluateEventGate(registry, world, event, changed, gate).holds)
        .toContainEqual(expect.objectContaining({ code: 'fingerprint-mismatch' }));
    }
  });

  it('rejects a failed dependency even when its parent calculation says passed', () => {
    const { world, event } = before('transfer-load');
    const engineeringInputs = inputs();
    const registry = new EvidenceRegistry();
    const requirement = gates.transferLoad.requirements[0];
    const dependency = submit(registry, world, event, engineeringInputs, requirement, {
      id: 'fixture-qualification', checkId: 'fixture-qualification', status: 'failed',
    });
    submit(registry, world, event, engineeringInputs, requirement, {
      id: 'beam-frame-with-dependency', dependencies: [dependency.id],
    });
    const gate: GateDefinition = { id: 'beam-only', version: '1', action: event.action,
      requirements: [requirement] };
    expect(evaluateEventGate(registry, world, event, engineeringInputs, gate).holds)
      .toContainEqual(expect.objectContaining({ code: 'dependency-invalid' }));
  });
});
