/**
 * A deterministic robot projection of the serial beam trace.  The domain event
 * stream remains authoritative for the beam and custody.  These states are a
 * separate, explicitly scoped mechanism study until robot poses and check IDs
 * are persisted by the domain reducer.
 *
 * Coordinates are metres, time is seconds, and Z is up.  A `pass` in
 * `localGeometry` is limited to sampled IK, the supplied box obstacles, and the
 * robotics module's assumed quasi-static capacities.  `transaction` never
 * claims that the beam, connector, host frame, or tool identity was qualified.
 */
import { assessStance, beginMotion, advanceMotion, createRobotState, planBodyMove, planStep, planToolExchange, toolDockPosition } from '../robotics';
import { add, length, mix, rotateZ, sub } from '../robotics/math';
import type { Anchor, CheckResult, MotionPlan, Obstacle, RobotConfig, RobotState, Vec3 } from '../robotics';
import type { EventAction, ExecutionEvent, SimulationTrace } from '../domain/types';

export type Fixture = 'A' | 'B';
export type RobotDeployment = 'two-robot' | 'four-robot-bench';
export type RobotMotionKind = 'grip-step' | 'body-shift' | 'tool-pick' | 'tool-park' | 'work-approach' | 'work-retract';

export interface RobotTaskOptions {
  /** Two-robot study omits B work; the four-robot bench uses a staged pair there. */
  deployment?: RobotDeployment;
  /** Applied to all machines. Null ratings correctly make a motion unverified. */
  config?: Partial<RobotConfig>;
  /** Additional measured or modeled exclusions in world coordinates. */
  obstacles?: Obstacle[];
}

export interface RobotMotionWindow {
  robotId: string;
  eventId: string;
  kind: RobotMotionKind;
  start: number;
  end: number;
  /** This check covers only the named robot primitive and supplied obstacles. */
  localGeometry: CheckResult;
}

export interface RobotTaskEvent {
  eventId: string;
  action: EventAction;
  fixture: Fixture | null;
  start: number;
  end: number;
  robotIds: string[];
  motions: RobotMotionWindow[];
  localGeometry: CheckResult;
  /** Full beam/robot transaction gate. It is unverified until domain integration. */
  transaction: CheckResult;
}

export interface RequiredRail {
  id: string;
  fixture: Fixture;
  x: number;
  y: number;
  zMin: number;
  zMax: number;
  purpose: string;
}

export interface RobotTaskTrace {
  scenarioId: string;
  deployment: RobotDeployment;
  initialStates: Record<string, RobotState>;
  finalStates: Record<string, RobotState>;
  events: RobotTaskEvent[];
  motions: RobotMotionWindow[];
  /** Missing robots here are simulated bench additions, not domain inventory. */
  supplementalRobotIds: string[];
  requiredRails: RequiredRail[];
  limitations: string[];
  /** Internal replay records; use robotTaskAtTime rather than mutating these. */
  replay: RobotMotionReplay[];
}

export interface RobotTaskSnapshot {
  time: number;
  states: Record<string, RobotState>;
  activeEvent: RobotTaskEvent | null;
  activeMotions: RobotMotionWindow[];
}

interface RobotMotionReplay extends RobotMotionWindow {
  before: RobotState;
  after: RobotState;
  plan?: MotionPlan;
  samples?: Vec3[];
}

interface Draft {
  state: RobotState;
  windows: RobotMotionReplay[];
  cursor: number;
}

const ROBOTS: Record<Fixture, readonly [string, string]> = {
  A: ['climber-1', 'climber-2'],
  B: ['climber-3', 'climber-4'],
};
const WORK_HEIGHT = 2.25;
const WORK_FACE_OFFSET = 0.68;
const WORK_STANDOFF = 0.25;
const WORK_Z = 3.0;
const EPS = 1e-8;

const clone = <T>(value: T): T => structuredClone(value);
const result = (status: CheckResult['status'], scope: string, reasons: string[] = []): CheckResult => ({ status, scope, reasons });
const unique = (items: string[]): string[] => [...new Set(items)];
const smooth = (t: number): number => t * t * (3 - 2 * t);
const fixtureY = (fixture: Fixture): number => fixture === 'A' ? 0 : 3;
const yawFor = (fixture: Fixture): number => fixture === 'A' ? 0 : Math.PI;
const xFor = (index: number): number => index === 0 ? 0 : 3;

/** Boxes for visible rigid fixture posts, heads, and top longitudinal members. */
export function fixtureObstacles(): Obstacle[] {
  const boxes: Obstacle[] = [];
  for (const x of [0, 3]) {
    for (const y of [0, 3]) {
      boxes.push({ id: `fixture post ${x},${y}`, min: [x - 0.09, y - 0.09, 0], max: [x + 0.09, y + 0.09, 3] });
      boxes.push({ id: `fixture head ${x},${y}`, min: [x - 0.15, y - 0.15, 2.85], max: [x + 0.15, y + 0.15, 3.15] });
    }
    boxes.push({ id: `top longitudinal member ${x}`, min: [x - 0.075, 0, 2.915], max: [x + 0.075, 3, 3.085] });
  }
  return boxes;
}

/** These socket rails are required by the candidate poses and must be built/qualified. */
export function requiredRobotRails(): RequiredRail[] {
  const rails: RequiredRail[] = [];
  for (const fixture of ['A', 'B'] as const) {
    for (const xCenter of [0, 3]) {
      for (const side of [-1, 1]) {
        rails.push({ id: `${fixture}-${xCenter}-${side}-work`, fixture, x: xCenter + side * 0.58,
          y: fixtureY(fixture), zMin: 1.65, zMax: 2.85, purpose: 'Four verified work and tool-exchange grips' });
        if (fixture === 'A') rails.push({ id: `A-${xCenter}-${side}-staging`, fixture,
          x: xCenter + side * 0.58, y: 0.23, zMin: 1.95, zMax: 3.15,
          purpose: 'Initial domain pose and checked transition to work rails' });
      }
    }
  }
  return rails;
}

function robotAtFixture(id: string, fixture: Fixture, x: number, config: Partial<RobotConfig>,
  suppliedPosition?: readonly [number, number, number]): RobotState {
  const y = fixtureY(fixture), yaw = yawFor(fixture);
  const position: Vec3 = suppliedPosition ? [...suppliedPosition]
    : [x, y + (fixture === 'A' ? -WORK_FACE_OFFSET : WORK_FACE_OFFSET), WORK_HEIGHT];
  const state = createRobotState({ id, position, yaw, config });
  state.limbs.forEach(limb => {
    limb.anchor = { id: `rail-${fixture}-${id}-${limb.index}`, position: [...limb.position], normal: rotateZ([0, -1, 0], yaw), available: true };
  });
  return state;
}

function seedA(id: string, position: readonly [number, number, number], config: Partial<RobotConfig>): RobotState {
  const state = createRobotState({ id, position: [...position], yaw: 0, config });
  state.limbs.forEach(limb => {
    limb.anchor = { id: `rail-A-${id}-staging-${limb.index}`, position: [...limb.position], normal: [0, -1, 0], available: true };
  });
  return state;
}

function localHold(states: RobotState[], obstacles: Obstacle[]): CheckResult {
  const checks = states.map(state => assessStance(state, obstacles));
  const reasons = unique(checks.flatMap(check => check.reasons));
  const status = checks.some(check => check.status === 'fail') ? 'fail'
    : checks.some(check => check.status === 'unverified') ? 'unverified' : 'pass';
  return result(status, 'fixed robot pose, supplied fixture boxes, and assumed keyed-grip allocation', reasons);
}

/** The controller maps missing ratings to a rejected motion. Preserve the distinction. */
function controllerCheck(plan: MotionPlan): CheckResult {
  const unknown = plan.reasons.some(reason => /missing declared capacity/i.test(reason));
  return result(unknown ? 'unverified' : plan.status, plan.scope, plan.reasons);
}

function planReach(state: RobotState, target: Vec3, obstacles: Obstacle[]): { check: CheckResult; samples: Vec3[] } {
  if (!state.limbs[1].tool || state.limbs[1].anchor || state.limbs[1].mode !== 'tooling')
    return { check: result('fail', 'tool-arm preconditions', ['Upper-right arm must carry a tool while three other grips are verified']), samples: [] };
  const from = state.limbs[1].position;
  // Smoothstep peaks at 1.5 times the average speed; keep spatial gaps <=20 mm.
  const count = Math.max(40, Math.ceil(length(sub(target, from)) * 1.5 / 0.02));
  const candidate = clone(state), samples: Vec3[] = [];
  for (let i = 0; i <= count; i++) {
    const position = mix(from, target, smooth(i / count));
    samples.push(position);
    candidate.limbs[1].position = position;
    const stance = assessStance(candidate, obstacles);
    if (stance.status !== 'pass') return { check: result(stance.status, 'sampled tool-arm IK, fixture-box clearance and three-grip allocation', stance.reasons), samples };
  }
  return { check: result('pass', 'sampled tool-arm IK, fixture-box clearance and three-grip allocation'), samples };
}

function addController(draft: Draft, event: ExecutionEvent, robotId: string, kind: RobotMotionKind, plan: MotionPlan): CheckResult {
  const check = controllerCheck(plan);
  if (check.status !== 'pass' || !plan.motion) return check;
  const start = draft.cursor, end = start + plan.motion.duration;
  if (end > event.time + EPS) return result('unverified', 'event time budget', [`${kind} requires ${plan.motion.duration.toFixed(2)} s beyond ${event.id}'s interval`]);
  const before = clone(draft.state);
  if (!beginMotion(draft.state, plan)) return result('fail', 'controller primitive', [`Controller refused ${kind}`]);
  advanceMotion(draft.state, plan.motion.duration);
  const after = clone(draft.state);
  draft.windows.push({ robotId, eventId: event.id, kind, start, end, localGeometry: check, before, after, plan: clone(plan) });
  draft.cursor = end;
  return check;
}

function addReach(draft: Draft, event: ExecutionEvent, robotId: string, kind: 'work-approach' | 'work-retract', target: Vec3,
  duration: number, obstacles: Obstacle[]): CheckResult {
  const start = draft.cursor, end = start + duration;
  if (end > event.time + EPS) return result('unverified', 'event time budget', [`${kind} requires ${duration.toFixed(2)} s beyond ${event.id}'s interval`]);
  const { check, samples } = planReach(draft.state, target, obstacles);
  if (check.status !== 'pass') return check;
  const before = clone(draft.state);
  draft.state.limbs[1].position = [...target];
  draft.state.elapsed += duration;
  draft.state.status = kind === 'work-approach' ? 'Tool held at checked beam-end standoff' : 'Tool retracted to body dock';
  const after = clone(draft.state);
  draft.windows.push({ robotId, eventId: event.id, kind, start, end, localGeometry: check, before, after, samples });
  draft.cursor = end;
  return check;
}

function workPoint(fixture: Fixture, index: number): Vec3 {
  return [xFor(index), fixtureY(fixture) + (fixture === 'A' ? -WORK_STANDOFF : WORK_STANDOFF), WORK_Z];
}

function parkAndRecapture(draft: Draft, event: ExecutionEvent, robotId: string, obstacles: Obstacle[]): CheckResult {
  if (draft.state.limbs[1].tool) {
    const check = addController(draft, event, robotId, 'tool-park', planToolExchange(draft.state, 1, 'park', obstacles));
    if (check.status !== 'pass') return check;
  }
  const home = draft.state.limbs[1].anchor ?? {
    id: `rail-home-${robotId}-1`, position: add(draft.state.position, rotateZ([0.58, 0.68, 0.54], draft.state.yaw)),
    normal: rotateZ([0, -1, 0], draft.state.yaw), available: true,
  } satisfies Anchor;
  if (draft.state.limbs[1].mode !== 'load_verified')
    return addController(draft, event, robotId, 'grip-step', planStep(draft.state, 1, home, obstacles));
  return result('pass', 'four-grip hold');
}

function planRobotEvent(draft: Draft, event: ExecutionEvent, robotId: string, fixture: Fixture, index: number,
  obstacles: Obstacle[]): CheckResult {
  const run = (kind: RobotMotionKind, plan: MotionPlan): CheckResult => addController(draft, event, robotId, kind, plan);
  const approach = (duration = 2.4): CheckResult => addReach(draft, event, robotId, 'work-approach', workPoint(fixture, index), duration, obstacles);
  const good = (check: CheckResult): boolean => check.status === 'pass';
  switch (event.action) {
    case 'deliver': {
      if (fixture !== 'A') break;
      if (Math.abs(draft.state.position[1] + WORK_FACE_OFFSET) < 1e-6 &&
        Math.abs(draft.state.position[2] - WORK_HEIGHT) < 1e-6) break;
      if (Math.abs(draft.state.position[0] - xFor(index)) > 1e-6 ||
        Math.abs(draft.state.position[1] + 0.45) > 1e-6 ||
        Math.abs(draft.state.position[2] - 2.55) > 1e-6)
        return result('unverified', 'A rail preparation', ['No checked preparation path from this domain robot pose']);
      // Four controller-checked individual regrips precede a fixed-contact body shift.
      for (let limbIndex = 0; limbIndex < 4; limbIndex++) {
        const limb = draft.state.limbs[limbIndex];
        const target: Anchor = { id: `rail-A-${robotId}-work-${limbIndex}`,
          position: [limb.position[0], 0, limb.position[2] - 0.30], normal: [0, -1, 0], available: true };
        const check = run('grip-step', planStep(draft.state, limbIndex, target, obstacles));
        if (!good(check)) return check;
      }
      return run('body-shift', planBodyMove(draft.state, [xFor(index), -WORK_FACE_OFFSET, WORK_HEIGHT], obstacles));
    }
    case 'guide': {
      if (!draft.state.limbs[1].tool) {
        const check = run('tool-pick', planToolExchange(draft.state, 1, 'pick', obstacles));
        if (!good(check)) return check;
      }
      return approach();
    }
    case 'recover': {
      if (event.data.fault !== 'mis-seat' || !draft.state.limbs[1].tool) break;
      return addReach(draft, event, robotId, 'work-retract', toolDockPosition(draft.state), 2.4, obstacles);
    }
    case 'fasten': {
      let check = parkAndRecapture(draft, event, robotId, obstacles);
      if (!good(check)) return check;
      check = run('tool-pick', planToolExchange(draft.state, 1, 'pick', obstacles));
      return good(check) ? approach() : check;
    }
    case 'verify': {
      let check = parkAndRecapture(draft, event, robotId, obstacles);
      if (!good(check)) return check;
      check = run('tool-pick', planToolExchange(draft.state, 1, 'pick', obstacles));
      return good(check) ? approach(1.6) : check;
    }
    case 'begin-removal': {
      if (!draft.state.limbs[1].tool) {
        const check = run('tool-pick', planToolExchange(draft.state, 1, 'pick', obstacles));
        if (!good(check)) return check;
      }
      return approach();
    }
    case 'park-tools': {
      if (!draft.state.limbs[1].tool) break;
      return run('tool-park', planToolExchange(draft.state, 1, 'park', obstacles));
    }
    case 'retreat': {
      // The five-second park-tools event cannot also fit the controller's 3.6 s recapture.
      if (draft.state.limbs[1].mode !== 'load_verified') return parkAndRecapture(draft, event, robotId, obstacles);
      break;
    }
  }
  return localHold([draft.state], obstacles);
}

function transactionCheck(event: ExecutionEvent, fixture: Fixture | null, deployment: RobotDeployment,
  supplementalRobotIds: string[], noRoute: boolean): CheckResult {
  const reasons = ['Mechanical robot states and check IDs are not committed to the authoritative WorldState'];
  if (supplementalRobotIds.length) reasons.push(`Bench adds ${supplementalRobotIds.length} robots absent from domain inventory`);
  if (noRoute) reasons.push('No checked A-to-B access route or time reservation for the original two robots');
  if (['guide', 'capture', 'fasten', 'verify', 'begin-removal', 'unfasten', 'release-capture', 'transfer-load', 'detach-hoist'].includes(event.action)) {
    reasons.push('Beam/tool contact, connector qualification, and host-frame reactions are not solved');
  }
  if (['guide', 'fasten', 'verify', 'begin-removal'].includes(event.action))
    reasons.push('Generic docked tool has no verified guide, driver, or inspection-tool identity');
  if (event.action === 'park-tools') reasons.push('Fourth grip is recaptured in retreat because the five-second event cannot fit both controller primitives');
  if (event.action === 'retreat') reasons.push('Return from work stance to another rail location has no checked access trajectory');
  if (event.data.fault === 'grip-unavailable') reasons.push('Unavailable socket and replacement socket have no qualified rail record');
  if (event.data.fault === 'mis-seat') reasons.push('Beam retraction and tool-arm clearance are not checked together');
  if (fixture === 'B' && deployment === 'two-robot') reasons.push('B operation has no robots at its fixture');
  return result('unverified', 'full beam/robot/fixture transaction', unique(reasons));
}

/** Compile a beam trace once. Later reads can seek to any timestamp without advancing a second clock. */
export function createRobotTaskTrace(trace: SimulationTrace, options: RobotTaskOptions = {}): RobotTaskTrace {
  const deployment = options.deployment ?? 'two-robot';
  const obstacles = [...fixtureObstacles(), ...(options.obstacles ?? [])];
  const initialStates: Record<string, RobotState> = {};
  for (const id of ROBOTS.A) {
    const domain = trace.initialWorld.robots[id];
    if (!domain) throw new Error(`Missing domain robot ${id}`);
    initialStates[id] = seedA(id, domain.position, options.config ?? {});
  }
  if (deployment === 'four-robot-bench') {
    ROBOTS.B.forEach((id, index) => {
      initialStates[id] = robotAtFixture(id, 'B', xFor(index), options.config ?? {}, trace.initialWorld.robots[id]?.position);
    });
  }
  const supplementalRobotIds = Object.keys(initialStates).filter(id => !trace.initialWorld.robots[id]);
  const current = clone(initialStates), motions: RobotMotionReplay[] = [], events: RobotTaskEvent[] = [];
  let activeFixture: Fixture | null = null;
  const blockedFixture: Partial<Record<Fixture, string>> = {};
  if (deployment === 'four-robot-bench') {
    for (const [index, id] of ROBOTS.B.entries()) {
      const expected: Vec3 = [xFor(index), 3 + WORK_FACE_OFFSET, WORK_HEIGHT];
      if (initialStates[id].position.some((value, axis) => Math.abs(value - expected[axis]) > 1e-6))
        blockedFixture.B = 'B domain robot pose differs from the proposed work stance; no checked approach route is supplied';
    }
  }
  for (const event of trace.events) {
    if (event.action === 'reserve') {
      if (event.data.targetId === 'configuration-A') activeFixture = 'A';
      else if (event.data.targetId === 'configuration-B') activeFixture = 'B';
    }
    // Removal remains at A; the second reservation changes the active fixture to B.
    const fixture = activeFixture;
    const ids = fixture ? [...ROBOTS[fixture]] : [];
    const missingRoute = fixture === 'B' && deployment === 'two-robot';
    const before = event.time - event.duration;
    let localGeometry: CheckResult;
    let committed: RobotMotionReplay[] = [];
    if (missingRoute) {
      localGeometry = result('unverified', 'fixture B robot access', ['No checked A-to-B route; the two domain robots hold their last verified A poses']);
    } else if (event.data.fault === 'grip-unavailable' && (event.action === 'fault' || event.action === 'recover')) {
      localGeometry = result('unverified', 'replacement rail grip',
        ['Unavailable socket and replacement socket are not specified or qualified; all robots hold their last checked supports']);
      if (fixture) blockedFixture[fixture] = 'Grip-unavailable recovery has no qualified replacement anchor';
    } else if (fixture && blockedFixture[fixture]) {
      localGeometry = result('unverified', 'blocked robot task', [blockedFixture[fixture]]);
    } else if (fixture) {
      const drafts = ids.map(id => ({ state: clone(current[id]), windows: [] as RobotMotionReplay[], cursor: before }));
      const checks = drafts.map((draft, index) => planRobotEvent(draft, event, ids[index], fixture, index, obstacles));
      const rejected = checks.find(check => check.status !== 'pass');
      if (rejected) {
        localGeometry = result(rejected.status, rejected.scope, unique(rejected.reasons));
        blockedFixture[fixture] = `Prior robot primitive could not be approved at ${event.id}: ${rejected.reasons.join('; ')}`;
      } else {
        const ending = localHold(drafts.map(draft => draft.state), obstacles);
        localGeometry = ending.status === 'pass' ? result('pass', 'sampled robot primitives and fixed-contact holds') : ending;
        if (localGeometry.status === 'pass') {
          drafts.forEach((draft, index) => { current[ids[index]] = draft.state; committed.push(...draft.windows); });
          motions.push(...committed);
        } else blockedFixture[fixture] = `Prior robot hold could not be approved at ${event.id}: ${ending.reasons.join('; ')}`;
      }
    } else {
      localGeometry = localHold(Object.values(current), obstacles);
    }
    events.push({ eventId: event.id, action: event.action, fixture, start: before, end: event.time,
      robotIds: missingRoute ? [] : ids, motions: committed.map(({ before: _before, after: _after, plan: _plan, samples: _samples, ...publicWindow }) => publicWindow),
      localGeometry, transaction: transactionCheck(event, fixture, deployment, supplementalRobotIds, missingRoute) });
  }
  const publicMotions = motions.map(({ before: _before, after: _after, plan: _plan, samples: _samples, ...publicWindow }) => publicWindow);
  return { scenarioId: trace.scenarioId, deployment, initialStates: clone(initialStates), finalStates: clone(current),
    events, motions: publicMotions, supplementalRobotIds, requiredRails: requiredRobotRails(), replay: motions,
    limitations: [
      'Rails and keyed sockets in requiredRails are proposed bench equipment; the rendered fixture pads do not supply them.',
      'Fixture boxes omit the diagonal braces, live beam swept volume, tool geometry, cable, and permitted contact region.',
      'The tool arm stops 0.25 m from the connection plane. Workpiece contact and forces are unverified.',
      'Quasi-static capacity values are assumed; wrist orientation, dynamics, host frame and connector stages remain unverified.',
      'WorldState currently persists only coarse robot mode, tool name and grip count, so this trace is a projection rather than a committed state.',
    ] };
}

/** Pure random-access pose sampling for the renderer. No call depends on frame rate or read order. */
export function robotTaskAtTime(trace: RobotTaskTrace, time: number): RobotTaskSnapshot {
  if (!Number.isFinite(time)) throw new Error('Robot task time must be finite');
  const last = trace.events.at(-1)?.end ?? 0;
  const t = Math.max(0, Math.min(time, last));
  const states = clone(trace.initialStates), activeMotions: RobotMotionReplay[] = [];
  for (const replay of trace.replay) {
    if (t + EPS >= replay.end) {
      states[replay.robotId] = clone(replay.after);
    } else if (t >= replay.start) {
      const sampled = clone(replay.before);
      if (replay.plan) {
        beginMotion(sampled, clone(replay.plan));
        advanceMotion(sampled, t - replay.start);
      } else {
        const duration = replay.end - replay.start;
        const fraction = duration > 0 ? (t - replay.start) / duration : 1;
        const start = replay.before.limbs[1].position, end = replay.after.limbs[1].position;
        sampled.limbs[1].position = mix(start, end, smooth(fraction));
        sampled.limbs[1].mode = 'tooling';
        sampled.motion = { kind: 'tool', elapsed: t - replay.start, duration, limbIndex: 1,
          start: [...start], end: [...end], samples: clone(replay.samples ?? []) };
        sampled.status = replay.kind === 'work-approach' ? 'Approaching beam-end standoff' : 'Retracting from beam-end standoff';
      }
      states[replay.robotId] = sampled;
      activeMotions.push(replay);
    }
  }
  const activeEvent = trace.events.find(event => t >= event.start && t < event.end) ?? trace.events.at(-1) ?? null;
  return { time: t, states, activeEvent, activeMotions: activeMotions.map(({ before: _before, after: _after, plan: _plan, samples: _samples, ...publicWindow }) => publicWindow) };
}
