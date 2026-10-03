import { describe, it, expect } from 'vitest';
import { BEAM, seatHardware, INSTALLED_CENTER } from '../connectors/bench';
import { fixtureObstacles } from '../integration/robotTask';
import { createRobotState, toolDockPosition } from './controller';
import { add, scale, sub, cross, length } from './math';
import { screenBeamInteraction, wristForBeamContact, guideContactWrenches } from './beamInteraction';
import type { BeamInteractionInput } from './beamInteraction';
import type { Vec3 } from './types';

function candidate(): BeamInteractionInput {
  const robot = createRobotState({ position: [0, -0.68, 2.25] });
  robot.limbs[1] = { ...robot.limbs[1], position: [0.25, -0.45, 3.36], anchor: null, mode: 'tooling', tool: true };
  robot.toolDocked = false;
  const contact = { solidId: 'beam-body', point: [-1.25, -0.073, 0.033] as Vec3, side: -1 as const };
  const tool = { id: 'spherical-side-guide', axis: [0, 1, 0] as Vec3, extension: 0.13, shaftRadius: 0.012, padRadius: 0.025 };
  const beamCenter: Vec3 = [...INSTALLED_CENTER];
  const wrist = wristForBeamContact(beamCenter, contact, tool);
  return { robot, limbIndex: 1, beam: BEAM, tool, contact,
    waypoints: [
      { wrist: [...robot.limbs[1].position], beamCenter, contactRequired: false },
      { wrist, beamCenter, contactRequired: true },
    ], obstacles: [...fixtureObstacles(), ...seatHardware().map(s => ({ id: s.id, min: [...s.min] as Vec3, max: [...s.max] as Vec3 }))], normalForceN: 80 };
}

describe('finite beam-side guidance contact', () => {
  it('reaches a real side face above/inboard of the open seat with three unchanged supports', () => {
    const input = candidate(), before = structuredClone(input.robot);
    const result = screenBeamInteraction(input);
    expect(result.localGeometry, result.localGeometry.reasons.join('\n')).toMatchObject({ status: 'pass' });
    expect(result.finalContact).toEqual([0.25, -0.073, 3.36]);
    expect(result.finalWrist![0]).toBeCloseTo(0.25);
    expect(result.finalWrist![1]).toBeCloseTo(-0.228);
    expect(result.finalWrist![2]).toBeCloseTo(3.36);
    expect(result.finalGap).toBeCloseTo(0, 9);
    expect(result.sampleCount).toBeGreaterThan(20);
    expect(result.forceAndHost.status).toBe('unverified');
    expect(input.robot).toEqual(before);
    expect(result.contactWrenches!.onBeam.force).toEqual([-0, 80, -0]);
  });
  it('checks the right-end robot independently', () => {
    const input = candidate();
    input.robot.position[0] = 3;
    for (const limb of input.robot.limbs) {
      if (limb.index !== 1) {
        limb.position[0] += 3;
        limb.anchor!.position[0] += 3;
      }
    }
    input.contact.point[0] = 1.25;
    input.robot.limbs[1].position[0] = 2.75;
    input.waypoints[0].wrist[0] = 2.75;
    input.waypoints[1].wrist = wristForBeamContact([...INSTALLED_CENTER], input.contact, input.tool);
    const result = screenBeamInteraction(input);
    expect(result.localGeometry, result.localGeometry.reasons.join('\n')).toMatchObject({ status: 'pass' });
  });
  it('transfers the same contact screen to a raised active floor without changing its local geometry', () => {
    const input = candidate(), offset: Vec3 = [12, -5, 54];
    input.robot.position = add(input.robot.position, offset);
    for (const limb of input.robot.limbs) {
      limb.position = add(limb.position, offset);
      if (limb.anchor) limb.anchor.position = add(limb.anchor.position, offset);
    }
    input.obstacles = input.obstacles.map(b => ({ ...b, min: add(b.min, offset), max: add(b.max, offset) }));
    input.waypoints = input.waypoints.map(p => ({ ...p, wrist: add(p.wrist, offset), beamCenter: add(p.beamCenter, offset) }));
    const result = screenBeamInteraction(input);
    expect(result.localGeometry, result.localGeometry.reasons.join('\n')).toMatchObject({ status: 'pass' });
    expect(result.finalContact![2]).toBeCloseTo(57.36);
    expect(result.forceAndHost.status).toBe('unverified');
  });
  it('follows the last 120 mm of hoist lowering while staying in actual side contact', () => {
    const input = candidate(), startCenter = add([...INSTALLED_CENTER], [0, 0, 0.12]);
    const startWrist = wristForBeamContact(startCenter, input.contact, input.tool);
    input.waypoints[0].beamCenter = startCenter;
    input.waypoints.splice(1, 0, { wrist: startWrist, beamCenter: startCenter, contactRequired: true });
    const result = screenBeamInteraction(input);
    expect(result.localGeometry, result.localGeometry.reasons.join('\n')).toMatchObject({ status: 'pass' });
  });
  it('rejects fixed-orientation departure from the generic body dock because the tool strikes its forearm', () => {
    const input = candidate();
    input.robot.limbs[1].position = toolDockPosition(input.robot);
    input.waypoints[0].wrist = [...input.robot.limbs[1].position];
    const result = screenBeamInteraction(input);
    expect(result.localGeometry.status).toBe('fail');
    expect(result.localGeometry.reasons.join(' ')).toContain('tool intersects limb 2');
  });
  it('rejects the old z=3.0 standoff as physical contact', () => {
    const input = candidate();
    input.waypoints[1].wrist = [0, -0.25, 3];
    const result = screenBeamInteraction(input);
    expect(result.localGeometry.status).toBe('fail');
    expect(result.localGeometry.reasons.join(' ')).toContain('pad misses');
    expect(result.contactWrenches).toBeNull();
  });
  it('fails the full 450 mm lowering with the low work stance instead of inventing reach', () => {
    const input = candidate(), high = add([...INSTALLED_CENTER], [0, 0, 0.45]);
    input.waypoints[0].beamCenter = high;
    input.waypoints.splice(1, 0, { wrist: wristForBeamContact(high, input.contact, input.tool), beamCenter: high, contactRequired: true });
    const result = screenBeamInteraction(input);
    expect(result.localGeometry.status).toBe('fail');
    expect(result.localGeometry.reasons.join(' ')).toContain('outside reach/joint envelope');
  });
  it('retains fixture cheeks as obstacles and rejects an end-shoe side contact through a cheek', () => {
    const input = candidate();
    input.contact = { solidId: 'left-shoe', point: [-1.41, -0.065, -0.082], side: -1 };
    input.waypoints[1].wrist = wristForBeamContact([...INSTALLED_CENTER], input.contact, input.tool);
    const result = screenBeamInteraction(input);
    expect(result.localGeometry.status).toBe('fail');
    expect(result.localGeometry.reasons.join(' ')).toMatch(/tool intersects left-open-seat-front-cheek/);
  });
  it('rejects missing contact, beam penetration, teleport, nonexistent surfaces and unavailable supports', () => {
    for (const edit of [
      (i: BeamInteractionInput) => { i.waypoints[1].wrist[1] -= 0.02; },
      (i: BeamInteractionInput) => { i.waypoints[1].wrist[1] += 0.02; },
      (i: BeamInteractionInput) => { i.waypoints[0].wrist[0] += 0.1; },
      (i: BeamInteractionInput) => { i.contact.solidId = 'imaginary'; },
      (i: BeamInteractionInput) => { i.robot.limbs[0].anchor!.available = false; },
      (i: BeamInteractionInput) => { i.normalForceN = -80; },
      (i: BeamInteractionInput) => { i.tool.extension = NaN; },
    ]) {
      const input = candidate(); edit(input);
      const result = screenBeamInteraction(input);
      expect(result.localGeometry.status).toBe('fail');
      expect(result.contactWrenches).toBeNull();
    }
  });
  it('catches a supplied obstruction in the approach corridor', () => {
    const input = candidate();
    input.obstacles.push({ id: 'approach obstruction', min: [0.235, -0.26, 3.345], max: [0.265, -0.25, 3.375] });
    const result = screenBeamInteraction(input);
    expect(result.localGeometry.status).toBe('fail');
    expect(result.localGeometry.reasons.join(' ')).toContain('approach obstruction');
  });
  it('places equal/opposite forces at one physical point and transfers the correct moment to the wrist', () => {
    const point: Vec3 = [0.25, -0.073, 3.36], wrist: Vec3 = [0.3, -0.228, 3.31];
    const pair = guideContactWrenches(point, wrist, [0, -1, 0], 80);
    expect(length(add(pair.onBeam.force, pair.onTool.force))).toBe(0);
    expect(pair.onTool.point).toEqual(pair.onBeam.point);
    expect(pair.atWrist.moment).toEqual(cross(sub(point, wrist), pair.onTool.force));
    const worldMoment = add(cross(pair.onBeam.point, pair.onBeam.force), add(cross(wrist, pair.atWrist.force), pair.atWrist.moment));
    expect(length(worldMoment)).toBeLessThan(1e-10);
    expect(pair.onTool.force).toEqual(scale(pair.onBeam.force, -1));
  });
});
