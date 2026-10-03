import { describe, expect, it } from 'vitest';
import { createBeamScenario } from '../scenarios/beam';
import { runScenario } from '../simulation/engine';
import { assessStance, solveRobotPose } from '../robotics';
import { createRobotTaskTrace, robotTaskAtTime } from './robotTask';

const beam = (failure: 'none' | 'mis-seat' | 'grip-unavailable' | 'delivery-delay' = 'none') =>
  runScenario(createBeamScenario({ failure }));

describe('beam-coupled robot task projection', () => {
  it('regrips from the domain initial pose and reaches A with controller-checked fixed supports', () => {
    const task = createRobotTaskTrace(beam());
    const delivery = task.events.find(event => event.fixture === 'A' && event.action === 'deliver')!;
    expect(delivery.localGeometry.status).toBe('pass');
    expect(delivery.motions.map(motion => motion.kind)).toEqual([
      'grip-step', 'grip-step', 'grip-step', 'grip-step', 'body-shift',
      'grip-step', 'grip-step', 'grip-step', 'grip-step', 'body-shift',
    ]);
    expect(robotTaskAtTime(task, 0).states['climber-1'].position).toEqual(beam().initialWorld.robots['climber-1'].position);
    const atDeliveryEnd = robotTaskAtTime(task, delivery.end).states['climber-1'];
    expect(atDeliveryEnd.position).toEqual([0, -0.68, 2.25]);
    expect(atDeliveryEnd.limbs.map(limb => limb.anchor?.position[1])).toEqual([0, 0, 0, 0]);
    const body = delivery.motions.find(motion => motion.robotId === 'climber-1' && motion.kind === 'body-shift')!;
    const start = robotTaskAtTime(task, body.start).states['climber-1'];
    const middle = robotTaskAtTime(task, (body.start + body.end) / 2).states['climber-1'];
    expect(middle.limbs.map(limb => limb.position)).toEqual(start.limbs.map(limb => limb.position));
    expect(middle.position).not.toEqual(start.position);
    expect(solveRobotPose(middle).check.status).toBe('pass');
    expect(assessStance(middle).anchorCount).toBe(4);
  });

  it('samples guide, exchange, inspection, and recapture without moving three support anchors', () => {
    const task = createRobotTaskTrace(beam());
    const guide = task.events.find(event => event.fixture === 'A' && event.action === 'guide')!;
    const fasten = task.events.find(event => event.fixture === 'A' && event.action === 'fasten')!;
    const verify = task.events.find(event => event.fixture === 'A' && event.action === 'verify')!;
    const park = task.events.find(event => event.fixture === 'A' && event.action === 'park-tools')!;
    const retreat = task.events.find(event => event.fixture === 'A' && event.action === 'retreat')!;
    expect(guide.localGeometry.status).toBe('pass');
    expect(guide.transaction.status).toBe('unverified');
    expect(guide.motions.map(motion => motion.kind)).toContain('work-approach');
    expect(fasten.motions.map(motion => motion.kind)).toEqual(expect.arrayContaining(['tool-park', 'grip-step', 'tool-pick', 'work-approach']));
    expect(verify.motions.map(motion => motion.kind)).toEqual(expect.arrayContaining(['tool-park', 'grip-step', 'tool-pick', 'work-approach']));
    const approach = guide.motions.find(motion => motion.robotId === 'climber-1' && motion.kind === 'work-approach')!;
    const atStart = robotTaskAtTime(task, approach.start).states['climber-1'];
    const midway = robotTaskAtTime(task, (approach.start + approach.end) / 2).states['climber-1'];
    expect(midway.limbs[1].position).not.toEqual(atStart.limbs[1].position);
    for (const index of [0, 2, 3]) expect(midway.limbs[index].position).toEqual(atStart.limbs[index].position);
    expect(assessStance(midway).anchorCount).toBe(3);
    expect(park.motions.map(motion => motion.kind)).toContain('tool-park');
    expect(assessStance(robotTaskAtTime(task, park.end).states['climber-1']).anchorCount).toBe(3);
    expect(retreat.motions.map(motion => motion.kind)).toContain('grip-step');
    expect(assessStance(robotTaskAtTime(task, retreat.end).states['climber-1']).anchorCount).toBe(4);
    const earlier = robotTaskAtTime(task, approach.start);
    robotTaskAtTime(task, retreat.end);
    expect(robotTaskAtTime(task, approach.start)).toEqual(earlier);
    expect(task.initialStates['climber-1'].position).toEqual([0, -0.45, 2.55]);
  });

  it('holds a two-robot deployment at A when an unplanned B transfer would otherwise teleport them', () => {
    const task = createRobotTaskTrace(beam());
    const bGuide = task.events.find(event => event.fixture === 'B' && event.action === 'guide')!;
    expect(bGuide.localGeometry.status).toBe('unverified');
    expect(bGuide.localGeometry.reasons).toEqual(expect.arrayContaining([expect.stringMatching(/No checked A-to-B route/)]));
    expect(bGuide.robotIds).toEqual([]);
    expect(bGuide.motions).toEqual([]);
    expect(robotTaskAtTime(task, bGuide.end).states['climber-1'].position).toEqual([0, -0.68, 2.25]);
    expect(task.finalStates['climber-1'].position[1]).toBeLessThan(0);
  });

  it('checks both local fixture B stances in a four-robot bench while leaving the transaction unverified', () => {
    const task = createRobotTaskTrace(beam(), { deployment: 'four-robot-bench' });
    const bGuide = task.events.find(event => event.fixture === 'B' && event.action === 'guide')!;
    expect(task.supplementalRobotIds).toEqual([]);
    expect(bGuide.localGeometry.status).toBe('pass');
    expect(bGuide.transaction.status).toBe('unverified');
    expect(bGuide.transaction.reasons).toEqual(expect.arrayContaining([expect.stringMatching(/Mechanical robot states/)]));
    expect(bGuide.motions.filter(motion => motion.kind === 'work-approach')).toHaveLength(2);
    const bPose = robotTaskAtTime(task, bGuide.end).states['climber-3'];
    expect(bPose.position).toEqual([0, 3.68, 2.25]);
    expect(assessStance(bPose).anchorCount).toBe(3);
    expect(solveRobotPose(bPose).check.status).toBe('pass');
    expect(task.events.every(event => event.transaction.status !== 'pass')).toBe(true);
  });

  it('uses a supplied B domain pose and blocks B work if it is not the checked bench stance', () => {
    const source = beam();
    source.initialWorld.robots['climber-3'] = { id: 'climber-3', position: [0, 3.40, 2.25], lockedGrips: 4, tool: 'parked', mode: 'travel' };
    source.initialWorld.robots['climber-4'] = { id: 'climber-4', position: [3, 3.68, 2.25], lockedGrips: 4, tool: 'parked', mode: 'travel' };
    const task = createRobotTaskTrace(source, { deployment: 'four-robot-bench' });
    const bGuide = task.events.find(event => event.fixture === 'B' && event.action === 'guide')!;
    expect(task.supplementalRobotIds).toEqual([]);
    expect(task.initialStates['climber-3'].position).toEqual([0, 3.40, 2.25]);
    expect(bGuide.localGeometry.status).toBe('unverified');
    expect(bGuide.motions).toEqual([]);
  });

  it('models a mis-seat retraction but refuses to invent a replacement for an unavailable grip', () => {
    const misSeat = createRobotTaskTrace(beam('mis-seat'));
    const recovery = misSeat.events.find(event => event.action === 'recover' && event.fixture === 'A')!;
    expect(recovery.motions.filter(motion => motion.kind === 'work-retract')).toHaveLength(2);
    expect(recovery.localGeometry.status).toBe('pass');
    expect(recovery.transaction.status).toBe('unverified');
    const unavailable = createRobotTaskTrace(beam('grip-unavailable'));
    const gripRecovery = unavailable.events.find(event => event.action === 'recover' && event.fixture === 'A')!;
    const nextGuide = unavailable.events.find(event => event.action === 'guide' && event.fixture === 'A')!;
    expect(gripRecovery.localGeometry.status).toBe('unverified');
    expect(gripRecovery.motions).toEqual([]);
    expect(nextGuide.localGeometry.status).toBe('unverified');
    expect(nextGuide.motions).toEqual([]);
    expect(robotTaskAtTime(unavailable, nextGuide.end).states['climber-1'].limbs.filter(limb => limb.mode === 'load_verified')).toHaveLength(4);
  });

  it('rejects unknown capacities and an obstructed work corridor without committing partial motion', () => {
    const unknown = createRobotTaskTrace(beam(), { config: { gripForceLimit: null } });
    const delivery = unknown.events.find(event => event.fixture === 'A' && event.action === 'deliver')!;
    expect(delivery.localGeometry.status).toBe('unverified');
    expect(delivery.motions).toEqual([]);
    expect(robotTaskAtTime(unknown, delivery.end).states['climber-1'].position).toEqual(unknown.initialStates['climber-1'].position);
    const blocked = createRobotTaskTrace(beam(), { obstacles: [{ id: 'blocked guide corridor', min: [-0.20, -0.42, 2.78], max: [0.20, -0.18, 3.24] }] });
    const blockedGuide = blocked.events.find(event => event.fixture === 'A' && event.action === 'guide')!;
    expect(blockedGuide.localGeometry.status).toBe('fail');
    expect(blockedGuide.localGeometry.reasons.join(' ')).toMatch(/blocked guide corridor/);
    expect(blockedGuide.motions).toEqual([]);
    expect(robotTaskAtTime(blocked, blockedGuide.end).states['climber-1'].limbs[1].tool).toBe(false);
  });
});
