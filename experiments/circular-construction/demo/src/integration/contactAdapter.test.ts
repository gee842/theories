import { describe, expect, it } from 'vitest';
import { contactBridgeCases } from '../../scripts/contactBridgeCases';
import { assessContactResult, createContactRequest } from './contactAdapter';
import { createRobotState, solveRobotPose } from '../robotics';
import type { Vec3 } from '../robotics';
import incompleteGuideResult from '../../numerical/fixtures/robot-task-actual-guiding-incomplete.result.json';
import guideResult from '../../numerical/fixtures/robot-task-guide-three-grip.result.json';
import collinearResult from '../../numerical/fixtures/robot-three-collinear-point-grips.result.json';
import relaxedResult from '../../numerical/fixtures/robot-three-collinear-unbounded-point-grips.result.json';

describe('fixed robot pose contact bridge', () => {
  it('binds a real beam guide three-grip pose to complete self-weight loads and checks conservative actuator rows conditionally', async () => {
    const [candidate] = await contactBridgeCases();
    const request = candidate.request;
    expect(request.schema_version).toBe(1);
    expect(request.world_revision).toBeGreaterThan(0);
    expect(request.input_fingerprint).toMatch(/^sha256:[a-f0-9]{64}$/);
    expect(request.loads).toHaveLength(14); // body + 4 × (upper, fore, clamp) + tool
    expect(request.loads.reduce((sum, load) => sum + (load.mass_kg ?? 0), 0)).toBe(102);
    expect(request.contacts).toHaveLength(3);
    expect(request.contacts.every(contact => contact.kind === 'keyed')).toBe(true);
    expect(request.adapter_context.source_geometry?.status).toBe('pass');
    expect(request.require_actuator_limits).toBe(true);
    expect(request.actuator_constraints).toHaveLength(24);
    expect(request.adapter_context.actuator_rows).toBe('self-weight-resultant-box');
    const result = guideResult;
    const assessment = await assessContactResult(request, result, request);
    expect(result.status).toBe('passed');
    expect(result.actuator_status).toBe('included');
    expect(assessment.status).toBe('pass');
    expect(assessment.stale).toBe(false);
    expect(assessment.reasons.join(' ')).toMatch(/no beam-guiding or hardware approval/);
  });

  it('keeps actual beam guiding unverified despite a feasible self-weight subset', async () => {
    const cases = await contactBridgeCases();
    const request = cases[3].request;
    const result = await assessContactResult(request, incompleteGuideResult, request);
    expect(incompleteGuideResult.status).toBe('passed');
    expect(result.status).toBe('unverified');
    expect(result.stale).toBe(false);
    expect(result.reasons.join(' ')).toMatch(/external loads are not fully specified/);
  });

  it('derives coefficients and distal gravity from moment balance at each joint', async () => {
    const state = createRobotState({ position: [2, -1, 3], yaw: 0.37 });
    state.toolDocked = false;
    state.limbs[1].tool = true; // Tool on a supporting limb is included too.
    state.limbs[3].mode = 'free';
    state.limbs[3].anchor = null;
    const pose = solveRobotPose(state);
    const request = await createContactRequest(state, { requestId: 'analytical', worldRevision: 0,
      externalLoadsComplete: true, loadScope: 'self-weight' });
    const f: Vec3 = [37, -19, 83], m: Vec3 = [7, 11, -5];
    // Independent, expanded moment balance; no production cross/dot helper.
    const moment = (point: Vec3, origin: Vec3, force: Vec3): Vec3 => {
      const x = point[0] - origin[0], y = point[1] - origin[1], z = point[2] - origin[2];
      return [y * force[2] - z * force[1], z * force[0] - x * force[2], x * force[1] - y * force[0]];
    };
    for (const limb of state.limbs) for (const joint of ['shoulder', 'elbow'] as const) {
      const p = pose.limbs[limb.index], origin = p[joint];
      const massPoints: [Vec3, number][] = [[p.wrist, state.config.clampMass + (limb.tool ? state.config.toolMass : 0)],
        [p.elbow.map((v, i) => (v + p.wrist[i]) / 2) as Vec3, state.config.foreMass]];
      if (joint === 'shoulder') massPoints.push([p.shoulder.map((v, i) => (v + p.elbow[i]) / 2) as Vec3, state.config.upperMass]);
      const gravity = massPoints.reduce((sum, [point, mass]) => {
        const value = moment(point, origin, [0, 0, -9.81 * mass]);
        return sum.map((v, axis) => v + value[axis]) as Vec3;
      }, [0, 0, 0] as Vec3);
      const expectedContact = limb.anchor ? moment(p.wrist, origin, f).map((v, i) => v + m[i]) : [0, 0, 0];
      for (let axis = 0; axis < 3; axis++) {
        const row = request.actuator_constraints.find(row => row.id.endsWith(`limb-${limb.index}:${joint}:${'xyz'[axis]}`))!;
        expect(row.gravity_torque_Nm).toBeCloseTo(gravity[axis], 10);
        const contactTorque = row.wrench_coefficients.reduce((sum, c) => sum +
          c.force_to_torque_m.reduce((value, x, i) => value + x * f[i], 0) +
          c.moment_to_torque.reduce((value, x, i) => value + x * m[i], 0), 0);
        expect(contactTorque + row.gravity_torque_Nm).toBeCloseTo(expectedContact[axis] + gravity[axis], 10);
        expect(row.wrench_coefficients).toHaveLength(limb.anchor ? 1 : 0);
        expect(row.upper_Nm).toBeCloseTo((joint === 'shoulder' ? 520 : 360) / Math.sqrt(3), 10);
      }
    }
  });

  it('keeps docked mass upstream and accounts for a carried tool on the free arm', async () => {
    const state = createRobotState({ position: [0, 0, 2] });
    const options = { requestId: 'custody', worldRevision: 0, externalLoadsComplete: true, loadScope: 'self-weight' };
    const docked = await createContactRequest(state, options);
    const heavy = structuredClone(state);
    heavy.config.bodyMass *= 2;
    heavy.config.toolMass *= 2;
    expect((await createContactRequest(heavy, options)).actuator_constraints).toEqual(docked.actuator_constraints);
    state.toolDocked = false;
    state.limbs[1].tool = true;
    state.limbs[1].anchor = null;
    state.limbs[1].mode = 'tooling';
    const carried = await createContactRequest(state, options);
    const p = solveRobotPose(state).limbs[1];
    for (const joint of ['shoulder', 'elbow'] as const) {
      const before = docked.actuator_constraints.find(row => row.id.endsWith(`limb-1:${joint}:x`))!;
      const after = carried.actuator_constraints.find(row => row.id === before.id)!;
      expect(after.wrench_coefficients).toEqual([]);
      expect(after.gravity_torque_Nm - before.gravity_torque_Nm).toBeCloseTo(
        -(p.wrist[1] - p[joint][1]) * 9.81 * state.config.toolMass, 10);
    }
  });

  it('does not invent joint ownership for external loads and preserves missing actuator capacities', async () => {
    const state = createRobotState({ position: [0, 0, 2] });
    const options = { requestId: 'external', worldRevision: 0, externalLoadsComplete: true, loadScope: 'test load' };
    const external = await createContactRequest(state, { ...options,
      externalLoads: [{ id: 'beam-force', position_m: [0, 0, 2], force_N: [0, 0, -100] }] });
    expect(external.actuator_constraints).toEqual([]);
    expect(external.adapter_context.actuator_rows).toBe('missing-external-load-attachment');
    state.config.shoulderTorqueLimit = null;
    const unknown = await createContactRequest(state, options);
    expect(unknown.actuator_constraints.filter(row => row.id.includes(':shoulder:')).every(row =>
      row.lower_Nm === null && row.upper_Nm === null)).toBe(true);
    state.config.elbowTorqueLimit = -1;
    await expect(createContactRequest(state, options)).rejects.toThrow(/capacity/);
  });

  it('rejects incomplete or inconsistent positive numerical evidence', async () => {
    const [{ request }] = await contactBridgeCases();
    for (const change of [{ actuator_status: 'unverified' }, { max_bound_violation: 1 },
      { equilibrium_residual: { max_abs: 1 } }, { missing_capacities: ['unknown'] },
      { solver: { status: 'numerical_error' } }]) {
      expect((await assessContactResult(request, { ...guideResult, ...change }, request)).status).toBe('unverified');
    }
  });

  it('finds the roll mechanism in a fixed three-grip collinear point-contact pose', async () => {
    const [, mechanism, relaxed] = await contactBridgeCases();
    const request = mechanism.request;
    expect(request.contacts).toHaveLength(3);
    expect(request.contacts.every(contact => contact.kind === 'point')).toBe(true);
    expect(new Set(request.contacts.map(contact => `${contact.position_m[1]},${contact.position_m[2]}`)).size).toBe(1);
    const result = collinearResult;
    const assessment = await assessContactResult(request, result, request);
    expect(result.status).toBe('failed');
    expect(assessment.status).toBe('fail');
    expect(relaxed.request.contacts.every(contact => contact.force_bounds_N.lower.every(value => value === null))).toBe(true);
    expect(relaxedResult.status).toBe('failed');
    expect((await assessContactResult(relaxed.request, relaxedResult, relaxed.request)).status).toBe('fail');
  });

  it('invalidates numerical evidence after rebuilding changed mass, geometry or torque capacity', async () => {
    const state = createRobotState({ position: [0, 0, 2] });
    const options = { requestId: 'stale-rebuild', worldRevision: 1, externalLoadsComplete: true, loadScope: 'self-weight' };
    const issued = await createContactRequest(state, options);
    expect((await createContactRequest(structuredClone(state), options)).input_fingerprint).toBe(issued.input_fingerprint);
    for (const change of ['mass', 'geometry', 'capacity'] as const) {
      const changed = structuredClone(state);
      if (change === 'mass') changed.config.foreMass += 1;
      if (change === 'geometry') changed.config.upperLength += 0.01;
      if (change === 'capacity') changed.config.elbowTorqueLimit = 300;
      const current = await createContactRequest(changed, options);
      expect(current.input_fingerprint).not.toBe(issued.input_fingerprint);
      expect((await assessContactResult(issued, guideResult, current)).stale).toBe(true);
    }
    const shuffled = structuredClone(state);
    [shuffled.limbs[0], shuffled.limbs[1]] = [shuffled.limbs[1], shuffled.limbs[0]];
    await expect(createContactRequest(shuffled, options)).rejects.toThrow(/array order/);
  });

  it('rejects an old world revision, a changed pose fingerprint, and a mismatched solver response', async () => {
    const [candidate] = await contactBridgeCases();
    const issued = candidate.request;
    const result = guideResult;
    const revised = structuredClone(issued);
    revised.world_revision += 1;
    expect((await assessContactResult(issued, result, revised)).stale).toBe(true);
    const moved = structuredClone(issued);
    moved.loads[0].position_m[0] += 0.01;
    expect((await assessContactResult(issued, result, moved)).stale).toBe(true);
    const changedActuator = structuredClone(issued);
    changedActuator.actuator_constraints[0].gravity_torque_Nm += 1;
    expect((await assessContactResult(issued, result, changedActuator)).stale).toBe(true);
    const changedBound = structuredClone(issued);
    changedBound.actuator_constraints[0].upper_Nm = 999;
    expect((await assessContactResult(issued, result, changedBound)).stale).toBe(true);
    const wrongReply = { ...result, input_fingerprint: 'wrong' };
    expect((await assessContactResult(issued, wrongReply, issued)).stale).toBe(true);
    const oldRevisionReply = { ...result, world_revision: issued.world_revision - 1 };
    expect((await assessContactResult(issued, oldRevisionReply, issued)).stale).toBe(true);
    const wrongHashReply = { ...result, request_sha256: '0'.repeat(64) };
    expect((await assessContactResult(issued, wrongHashReply, issued)).stale).toBe(true);
  });
});
