import { test, assert } from 'vitest';
import { assertWorldInvariants, materialLedger } from '../src/domain/invariants';
import { createBeamScenario, BEAM_ID } from '../src/scenarios/beam';
import { applyEvent, runScenario, worldAtTime, partPoseAtTime, equipmentPoseAtTime } from '../src/simulation/engine';
import type { ExecutionEvent } from '../src/domain/types';

test('the same identified beam stays supported through two configurations and stock reconciles', () => {
  const trace = runScenario(createBeamScenario());
  assert.equal(trace.finalWorld.status, 'complete');
  assert.equal(trace.finalWorld.parts[BEAM_ID].useCount, 2);
  assert.equal(trace.finalWorld.parts[BEAM_ID].assignedTarget, 'configuration-B');
  for (const checkpoint of trace.checkpoints) {
    assertWorldInvariants(checkpoint.world);
    assert.equal(Object.keys(checkpoint.world.parts).length, 5);
    assert.ok(Math.abs(materialLedger(checkpoint.world).residualKg) < 1e-8);
  }
  assert.equal(materialLedger(trace.finalWorld).reusedMassKg, 93.3);
});

test('hoist custody cannot be detached before both end connections pass inspection', () => {
  const scenario = createBeamScenario();
  const trace = runScenario(scenario);
  const afterFastening = trace.checkpoints.find(checkpoint => trace.events.find(event => event.id === checkpoint.eventId)?.action === 'fasten')!.world;
  const invalid: ExecutionEvent = { id: 'invalid-release', sequence: afterFastening.revision + 1, time: afterFastening.time + 1, duration: 1, action: 'detach-hoist', partId: BEAM_ID, label: 'Premature release', data: {} };
  const unchanged = structuredClone(afterFastening);
  assert.throws(() => applyEvent(afterFastening, invalid), /cannot release/);
  assert.deepEqual(afterFastening, unchanged);
});

test('final fastening cannot bypass temporary capture', () => {
  const scenario = createBeamScenario();
  const trace = runScenario(scenario);
  const guided = trace.checkpoints.find(checkpoint => trace.events.find(event => event.id === checkpoint.eventId)?.action === 'guide')!.world;
  const invalid: ExecutionEvent = { id: 'skip-capture', sequence: guided.revision + 1, time: guided.time + 1, duration: 1, action: 'fasten', partId: BEAM_ID, label: 'Skip capture', data: {} };
  assert.throws(() => applyEvent(guided, invalid), /expected captured/);
});

test('replay is deterministic and returned snapshots cannot corrupt the recorded world', () => {
  const trace = runScenario(createBeamScenario({ seed: 13, failure: 'mis-seat' }));
  assert.deepEqual(trace, runScenario(createBeamScenario({ seed: 13, failure: 'mis-seat' })));
  for (const checkpoint of trace.checkpoints) assert.deepEqual(worldAtTime(trace, checkpoint.time), checkpoint.world);
  const snapshot = worldAtTime(trace, trace.finalWorld.time);
  delete snapshot.parts[BEAM_ID];
  assert.ok(trace.finalWorld.parts[BEAM_ID]);
});

test('each modeled failure retains custody and recovers by explicit operations', () => {
  for (const failure of ['mis-seat', 'grip-unavailable', 'delivery-delay'] as const) {
    const trace = runScenario(createBeamScenario({ seed: 19, failure }));
    const faultEvent = trace.events.find(event => event.action === 'fault')!;
    const held = worldAtTime(trace, faultEvent.time).parts[BEAM_ID];
    assert.ok(held.supports.some(support => support.kind === (failure === 'delivery-delay' ? 'carrier' : 'hoist')));
    assert.ok(trace.events.some(event => event.action === 'recover' && event.data.fault === failure));
    assert.equal(trace.finalWorld.parts[BEAM_ID].useCount, 2);
    assert.ok(trace.finalWorld.time > runScenario(createBeamScenario()).finalWorld.time);
  }
});

test('display interpolation preserves the committed simulation state', () => {
  const trace = runScenario(createBeamScenario());
  const lift = trace.events.find(event => event.action === 'lift')!;
  const halfTime = lift.time - lift.duration / 2;
  const pose = partPoseAtTime(trace, BEAM_ID, halfTime);
  assert.ok(Math.abs(pose[2] - (lift.poseFrom![2] + lift.poseTo![2]) / 2) < 1e-10);
  assert.deepEqual(worldAtTime(trace, halfTime).parts[BEAM_ID].position, lift.poseFrom);
});

test('removed stock cannot bypass condition inspection before second use', () => {
  const trace = runScenario(createBeamScenario());
  const returned = trace.checkpoints.find(checkpoint => trace.events.find(event => event.id === checkpoint.eventId)?.action === 'return')!.world;
  const invalid: ExecutionEvent = { id: 'skip-inspection', sequence: returned.revision + 1, time: returned.time + 1, duration: 1, action: 'qualify-reuse', partId: BEAM_ID, label: 'Skip inspection', data: {} };
  assert.throws(() => applyEvent(returned, invalid), /passing inspection/);
});

test('a detected mis-seat blocks capture until a matching recovery resets the approach', () => {
  const trace = runScenario(createBeamScenario({ failure: 'mis-seat' }));
  const fault = trace.events.find(event => event.action === 'fault')!;
  const held = worldAtTime(trace, fault.time);
  const invalid: ExecutionEvent = { id: 'ignore-fault', sequence: held.revision + 1, time: held.time + 1, duration: 1, action: 'capture', partId: BEAM_ID, label: 'Ignore failed alignment', data: {} };
  assert.throws(() => applyEvent(held, invalid), /explicit recovery/);
  assert.throws(() => applyEvent(held, { ...invalid, action: 'recover', data: { fault: 'grip-unavailable' } }), /match an active fault/);
});

test('empty carrier travels to recovered stock before its second pickup', () => {
  const trace = runScenario(createBeamScenario());
  const pickups = trace.events.filter(event => event.action === 'receive');
  assert.equal(pickups.length, 2);
  const travel = trace.events.find(event => event.action === 'move-carrier')!;
  assert.ok(travel.time < pickups[1].time);
  assert.ok(travel.duration > 0);
  const before = worldAtTime(trace, travel.time - travel.duration);
  assert.equal(before.equipment.carrierBusy, false);
  assert.equal(before.parts[BEAM_ID].location, 'stock');
  const halfway = equipmentPoseAtTime(trace, 'carrier', travel.time - travel.duration / 2);
  assert.ok(Math.abs(halfway[0] - (travel.equipmentMotion!.carrier!.from[0] + travel.equipmentMotion!.carrier!.to[0]) / 2) < 1e-10);
  const pickupWorld = worldAtTime(trace, pickups[1].time);
  assert.deepEqual(pickupWorld.equipment.carrierPosition.slice(0, 2), pickupWorld.parts[BEAM_ID].position.slice(0, 2));
});

test('loaded equipment motion has continuous poses and matching support geometry', () => {
  const trace = runScenario(createBeamScenario({ failure: 'mis-seat' }));
  let carrier = trace.initialWorld.equipment.carrierPosition;
  let hook = trace.initialWorld.equipment.hoistHookPosition;
  for (const event of trace.events) {
    if (event.equipmentMotion?.carrier) {
      assert.deepEqual(event.equipmentMotion.carrier.from, carrier);
      carrier = event.equipmentMotion.carrier.to;
    }
    if (event.equipmentMotion?.hoistHook) {
      assert.deepEqual(event.equipmentMotion.hoistHook.from, hook);
      hook = event.equipmentMotion.hoistHook.to;
    }
    if (event.poseTo) {
      const midpoint = event.time - event.duration / 2;
      const pose = partPoseAtTime(trace, BEAM_ID, midpoint);
      const motionWorld = worldAtTime(trace, midpoint);
      if (event.action === 'deliver') {
        const cart = equipmentPoseAtTime(trace, 'carrier', midpoint);
        assert.ok(pose.every((value, axis) => Math.abs(value - cart[axis] - (axis === 2 ? motionWorld.equipment.carrierDeckHeight : 0)) < 1e-8));
        assert.ok(motionWorld.parts[BEAM_ID].supports.some(support => support.kind === 'carrier'));
      } else {
        const apex = equipmentPoseAtTime(trace, 'hoistHook', midpoint);
        assert.ok(pose.every((value, axis) => Math.abs(value - apex[axis] + (axis === 2 ? motionWorld.equipment.hoistSlingHeight : 0)) < 1e-8));
        assert.ok(motionWorld.parts[BEAM_ID].supports.some(support => support.kind === 'hoist'));
        assert.ok(!motionWorld.parts[BEAM_ID].supports.some(support => support.kind === 'carrier'));
      }
    }
  }
});

test('pickup and sling attachment cannot occur at remote equipment positions', () => {
  const trace = runScenario(createBeamScenario());
  const reserve = trace.events.find(event => event.action === 'reserve')!;
  const world = worldAtTime(trace, reserve.time);
  world.equipment.carrierPosition = [100, 100, 0];
  const pickup = trace.events.find(event => event.action === 'receive')!;
  assert.throws(() => applyEvent(world, pickup), /actual stock location/);
  const approach = trace.events.find(event => event.action === 'attach-hoist')!;
  const beforeApproach = worldAtTime(trace, approach.time - approach.duration);
  beforeApproach.equipment.hoistHookPosition = [100, 100, 4];
  assert.throws(() => applyEvent(beforeApproach, approach), /sling apex/);
});

test('loaded-site hook motions cannot leave the finite gantry envelope', () => {
  const world = createBeamScenario().initialWorld;
  const unchanged = structuredClone(world);
  const motion: ExecutionEvent = {
    id: 'out-of-reach', sequence: 1, time: 2, duration: 2,
    action: 'move-hook', partId: BEAM_ID, label: 'Attempt unreachable lift', data: {},
    equipmentMotion: { hoistHook: { from: world.equipment.hoistHookPosition, to: [100, -3, 4.5] } },
  };
  assert.throws(() => applyEvent(world, motion), /outside gantry envelope/);
  assert.deepEqual(world, unchanged);
});

test('robot task modes change only at the assigned fixture', () => {
  const trace = runScenario(createBeamScenario());
  const guided = trace.checkpoints.filter(checkpoint => trace.events.find(event => event.id === checkpoint.eventId)?.action === 'guide');
  assert.equal(guided.length, 2);
  assert.equal(guided[0].world.robots['climber-1'].tool, 'guide');
  assert.equal(guided[0].world.robots['climber-2'].tool, 'guide');
  assert.equal(guided[0].world.robots['climber-3'].tool, 'parked');
  assert.equal(guided[0].world.robots['climber-4'].tool, 'parked');
  assert.equal(guided[1].world.robots['climber-1'].tool, 'parked');
  assert.equal(guided[1].world.robots['climber-2'].tool, 'parked');
  assert.equal(guided[1].world.robots['climber-3'].tool, 'guide');
  assert.equal(guided[1].world.robots['climber-4'].tool, 'guide');
});
