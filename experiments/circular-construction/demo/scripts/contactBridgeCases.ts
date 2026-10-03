import { createBeamScenario } from '../src/scenarios/beam';
import { runScenario, worldAtTime } from '../src/simulation/engine';
import { createRobotState } from '../src/robotics';
import { createRobotTaskTrace, robotTaskAtTime } from '../src/integration/robotTask';
import { assessContactResult, createContactRequest } from '../src/integration/contactAdapter';
import type { ContactRequest } from '../src/integration/contactAdapter';
import type { Vec3 } from '../src/robotics';

export interface BridgeCase { name: string; request: ContactRequest; expected: 'passed' | 'failed' | 'unverified'; expectedAssessment?: 'pass' | 'fail' | 'unverified'; }
export { assessContactResult };

export async function contactBridgeCases(): Promise<BridgeCase[]> {
  const beam = runScenario(createBeamScenario());
  const task = createRobotTaskTrace(beam);
  const guide = task.events.find(event => event.fixture === 'A' && event.action === 'guide');
  if (!guide || guide.localGeometry.status !== 'pass') throw new Error('Beam guide pose is not checked locally');
  const candidate = robotTaskAtTime(task, guide.end).states['climber-1'];
  const real = await createContactRequest(candidate, {
    requestId: `beam-A-guide-${candidate.id}`,
    worldRevision: worldAtTime(beam, guide.end).revision,
    externalLoadsComplete: true,
    loadScope: 'Robot self-weight at checked beam-end standoff; no beam or tool contact force',
    sourceGeometry: guide.localGeometry,
  });

  const incompleteGuiding = await createContactRequest(candidate, {
    requestId: `beam-A-guiding-incomplete-${candidate.id}`,
    worldRevision: worldAtTime(beam, guide.end).revision,
    externalLoadsComplete: false,
    loadScope: 'Actual beam guiding is unverified: pose stops at standoff and beam/tool interaction loads are unspecified',
    sourceGeometry: guide.localGeometry,
  });

  // A fixed three-grip robot pose with point contacts on one horizontal line.
  // The body is 0.68 m away from that line, so self-weight demands roll moment.
  const collinear = createRobotState({ id: 'collinear-climber', position: [0, -0.68, 2.25] });
  const anchors: [number, Vec3][] = [[0, [-0.58, 0, 2.25]], [2, [0, 0, 2.25]], [3, [0.58, 0, 2.25]]];
  for (const [index, point] of anchors) {
    const limb = collinear.limbs[index];
    limb.position = [...point];
    limb.anchor = { id: `point-${index}`, position: [...point], normal: [0, -1, 0], available: true };
  }
  collinear.limbs[1].anchor = null;
  collinear.limbs[1].mode = 'tooling';
  collinear.limbs[1].tool = true;
  collinear.toolDocked = false;
  const mechanism = await createContactRequest(collinear, {
    requestId: 'collinear-three-grip-roll', worldRevision: 0, contactKind: 'point',
    externalLoadsComplete: true, loadScope: 'Isolated robot self-weight; three collinear point grips',
  });
  const relaxedState = structuredClone(collinear);
  relaxedState.config.gripForceLimit = null;
  const relaxedMechanism = await createContactRequest(relaxedState, {
    requestId: 'collinear-three-grip-roll-unknown-force-capacity', worldRevision: 0, contactKind: 'point',
    externalLoadsComplete: true, loadScope: 'Isolated robot self-weight; collinear point grips with relaxed force limits',
  });
  return [
    { name: 'robot-task-guide-three-grip', request: real, expected: 'passed' },
    { name: 'robot-three-collinear-point-grips', request: mechanism, expected: 'failed' },
    { name: 'robot-three-collinear-unbounded-point-grips', request: relaxedMechanism, expected: 'failed' },
    { name: 'robot-task-actual-guiding-incomplete', request: incompleteGuiding, expected: 'passed', expectedAssessment: 'unverified' },
  ];
}
