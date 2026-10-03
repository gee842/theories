import { assert, test } from 'vitest';
import { createBeamScenario, BEAM_ID } from '../scenarios/beam';
import { createBeamHandoffGates, EvidenceRegistry, type EngineeringInputs } from '../validation';
import { applyEvent } from './engine';
import { runGatedScenario } from './gated';

const models = {
  connectorMotion: { id: 'sampled-connector-path', version: '1' },
  robotBeamContact: { id: 'robot-beam-contact', version: '1' },
  hoistLoad: { id: 'hoist-load', version: '1' },
  beamFrame: { id: 'linear-frame', version: '1' },
  jointStrength: { id: 'reversible-joint', version: '1' },
  hostFrame: { id: 'supporting-frame', version: '1' },
} as const;
const policy = createBeamHandoffGates(models);
const gates = { guide: policy.guide, 'transfer-load': policy.transferLoad,
  'detach-hoist': policy.detachHoist };
const inputs: EngineeringInputs = {
  geometry: { fixture: 'synthetic gate test' },
  supports: { hoistRetained: true },
  loads: { beamWeightN: 93.3 * 9.81 },
  capacities: { synthetic: { value: 1, units: 'N', basis: 'measured', reference: 'synthetic test only' } },
};

test('missing guide evidence holds the real beam trace before changing connection state', () => {
  const scenario = createBeamScenario();
  const initial = structuredClone(scenario.initialWorld);
  const result = runGatedScenario(scenario, new EvidenceRegistry(), () => inputs, gates);
  assert.equal(result.status, 'held');
  assert.equal(result.hold?.event.action, 'guide');
  assert.equal(result.hold?.decision.allowed, false);
  assert.equal(result.world.parts[BEAM_ID].connections.A.phase, 'absent');
  assert.ok(result.world.parts[BEAM_ID].supports.some(support => support.kind === 'hoist'));
  assert.deepEqual(scenario.initialWorld, initial);
});

test('a synthetic guide pass reaches load transfer, then holds the hoist and both seats', () => {
  const scenario = createBeamScenario();
  const registry = new EvidenceRegistry();
  let world = structuredClone(scenario.initialWorld);
  for (const event of scenario.events) {
    if (event.action === 'guide') {
      for (const requirement of policy.guide.requirements) {
        registry.register(world, event, inputs, {
          id: `synthetic:${event.id}:${requirement.id}`,
          checkId: requirement.checkId,
          connectionId: null,
          model: requirement.model,
          status: 'passed',
          provenance: { basis: 'calculated', reference: 'synthetic runner test only' },
          capacityIds: requirement.acceptedCapacityBases.includes('none') ? [] : ['synthetic'],
          dependencies: [],
          detail: 'Synthetic result used only to test event gating',
        });
      }
      break;
    }
    world = applyEvent(world, event);
  }
  const result = runGatedScenario(scenario, registry, () => inputs, gates);
  assert.equal(result.status, 'held');
  assert.equal(result.hold?.event.action, 'transfer-load');
  assert.deepEqual(result.hold?.decision.holds.map(hold => hold.code),
    ['missing', 'missing', 'missing', 'missing']);
  const beam = result.world.parts[BEAM_ID];
  assert.equal(beam.useCount, 0);
  assert.equal(beam.location, 'workfront');
  assert.ok(beam.supports.some(support => support.kind === 'hoist'));
  assert.ok(beam.supports.some(support => support.kind === 'capture-seat'));
  assert.ok(!beam.supports.some(support => support.kind === 'installed-joint'));
  assert.ok(result.commits.some(commit => commit.event.action === 'guide' && commit.gateDecision?.allowed));
});
