import { assertWorldInvariants } from '../domain/invariants';
import type { ConnectionPhase, ExecutionEvent, PartInstance, Scenario, SimulationTrace, Vec3, WorldState } from '../domain/types';

function requireState(condition: boolean, message: string): asserts condition {
  if (!condition) throw new Error(message);
}
function phases(part: PartInstance, phase: ConnectionPhase) {
  return Object.values(part.connections).every(connection => connection.phase === phase);
}
function changePhase(part: PartInstance, from: ConnectionPhase, to: ConnectionPhase, event: ExecutionEvent) {
  const ends = event.data.end ? [event.data.end] : ['A', 'B'] as const;
  for (const end of ends) {
    const connection = part.connections[end];
    requireState(connection.phase === from, `${event.action}: ${connection.id} expected ${from}, found ${connection.phase}`);
    connection.phase = to;
    connection.verifiedAt = to === 'verified' ? event.time : null;
  }
}
function hasHoist(part: PartInstance) { return part.supports.some(s => s.kind === 'hoist'); }
function poseMatches(a: Vec3, b: Vec3) { return a.every((value, i) => Math.abs(value - b[i]) < 1e-8); }

/** Transactional reducer. Invalid events leave the input world untouched. */
export function applyEvent(previous: WorldState, event: ExecutionEvent): WorldState {
  requireState(event.sequence === previous.revision + 1, 'Event sequence is not contiguous');
  requireState(event.time >= previous.time && event.duration >= 0 && Number.isFinite(event.duration), 'Event clock runs backwards or duration is invalid');
  requireState(event.time - event.duration >= previous.time - 1e-8, 'Serial operation starts before the previous transaction committed');
  requireState(previous.status !== 'complete', 'Cannot mutate a completed scenario');
  const world: WorldState = structuredClone(previous);
  const part = world.parts[event.partId];
  requireState(!!part, `Unknown part: ${event.partId}`);
  requireState(!world.activeFaults[event.partId] || event.action === 'recover', 'Active fault requires explicit recovery before new work');
  if (event.poseFrom) requireState(poseMatches(part.position, event.poseFrom), `Motion source disagrees with world: ${event.id}`);
  const carrierMotion = event.equipmentMotion?.carrier;
  const hookMotion = event.equipmentMotion?.hoistHook;
  if (carrierMotion) requireState(poseMatches(world.equipment.carrierPosition, carrierMotion.from), 'Carrier motion source disagrees with world');
  if (hookMotion) requireState(poseMatches(world.equipment.hoistHookPosition, hookMotion.from), 'Hook motion source disagrees with world');
  const robotIds = part.assignedTarget === 'configuration-B'
    ? ['climber-3', 'climber-4'] : ['climber-1', 'climber-2'];
  const robots = robotIds.map(id => world.robots[id]);
  requireState(robots.every(Boolean), 'The assigned fixture needs two available robots');
  switch (event.action) {
    case 'reserve':
      requireState(part.location === 'stock' && part.condition === 'qualified' && !part.reserved, 'Only available qualified stock can be reserved');
      requireState(!!event.data.targetId, 'Reservation requires a target');
      part.reserved = true;
      part.assignedTarget = event.data.targetId!;
      for (const connection of Object.values(part.connections)) connection.targetId = part.assignedTarget;
      break;
    case 'receive':
      requireState(part.reserved && part.location === 'stock' && !world.equipment.carrierBusy, 'Carrier pickup prerequisites failed');
      requireState(poseMatches(part.position, [world.equipment.carrierPosition[0], world.equipment.carrierPosition[1], world.equipment.carrierPosition[2] + world.equipment.carrierDeckHeight]), 'Carrier must reach the actual stock location before pickup');
      part.location = 'carrier';
      part.supports = [{ kind: 'carrier', id: world.equipment.carrierId }];
      world.equipment.carrierBusy = true;
      break;
    case 'deliver':
      requireState(part.location === 'carrier', 'Delivery requires carrier custody');
      break;
    case 'attach-hoist':
      requireState(!world.equipment.hoistBusy && ['carrier', 'installed'].includes(part.location), 'Hoist attachment prerequisites failed');
      requireState(poseMatches(world.equipment.hoistHookPosition, [part.position[0], part.position[1], part.position[2] + world.equipment.hoistSlingHeight]), 'Hook must reach sling apex before attachment');
      part.supports.push({ kind: 'hoist', id: world.equipment.hoistId });
      world.equipment.hoistBusy = true;
      break;
    case 'release-carrier':
      requireState(hasHoist(part) && part.location === 'carrier' && !event.poseTo, 'Carrier handoff requires attached hoist before any lift motion');
      part.supports = part.supports.filter(s => s.kind !== 'carrier');
      world.equipment.carrierBusy = false;
      part.location = 'workfront';
      break;
    case 'lift':
      requireState(hasHoist(part) && part.location === 'workfront' && !part.supports.some(s => s.kind === 'carrier'), 'Lift motion requires completed carrier-to-hoist handoff');
      break;
    case 'move-carrier':
      requireState(!world.equipment.carrierBusy && !!carrierMotion && !event.poseTo, 'Empty carrier movement requires a free carrier and no part displacement');
      break;
    case 'move-hook':
      requireState(!world.equipment.hoistBusy && !!hookMotion && !event.poseTo, 'Detached hook movement requires a free hoist');
      break;
    case 'move-hoist':
      requireState(hasHoist(part) && part.location === 'workfront' && !!hookMotion && !!event.poseTo, 'Loaded hoist traversal requires continuous sling and part motion');
      break;
    case 'guide':
      requireState(hasHoist(part) && part.location === 'workfront', 'Guiding requires a hoist supported workfront');
      requireState(robots.every(robot => robot.lockedGrips >= 3), 'Guiding requires anchored robots');
      changePhase(part, 'absent', 'aligned', event);
      robots.forEach(robot => { robot.mode = 'work'; robot.tool = 'guide'; });
      break;
    case 'capture':
      requireState(hasHoist(part), 'Hoist must remain attached during capture');
      changePhase(part, 'aligned', 'captured', event);
      for (const connection of Object.values(part.connections)) {
        if (connection.phase === 'captured' && !part.supports.some(s => s.id === connection.id)) part.supports.push({ kind: 'capture-seat', id: connection.id });
      }
      break;
    case 'fasten':
      requireState(hasHoist(part) && robots.every(robot => robot.lockedGrips >= 3), 'Fastening requires supported part and anchored robots');
      changePhase(part, 'captured', 'final', event);
      robots.forEach(robot => { robot.tool = 'driver'; robot.mode = 'work'; });
      break;
    case 'verify':
      changePhase(part, 'final', 'verified', event);
      robots.forEach(robot => { robot.tool = 'inspection'; robot.mode = 'work'; });
      break;
    case 'transfer-load':
      requireState(phases(part, 'verified') && hasHoist(part), 'Load transfer requires both verified joints and hoist custody');
      part.supports = part.supports.filter(s => s.kind !== 'capture-seat');
      part.supports.push({ kind: 'installed-joint', id: part.assignedTarget! });
      part.location = 'installed';
      part.useCount += 1;
      part.reserved = false;
      break;
    case 'detach-hoist':
      requireState(part.location === 'installed' && phases(part, 'verified') && part.supports.some(s => s.kind === 'installed-joint') && hasHoist(part), 'Hoist cannot release before verified load handoff');
      part.supports = part.supports.filter(s => s.kind !== 'hoist');
      world.equipment.hoistBusy = false;
      break;
    case 'park-tools':
      robots.forEach(robot => { robot.tool = 'parked'; robot.lockedGrips = 4; });
      break;
    case 'retreat':
      requireState(robots.every(robot => robot.tool === 'parked'), 'Tools must be parked before retreat');
      robots.forEach(robot => { robot.mode = 'travel'; });
      break;
    case 'begin-removal':
      requireState(hasHoist(part) && part.location === 'installed' && phases(part, 'verified'), 'Removal requires hoist attached to installed member');
      part.supports = part.supports.filter(s => s.kind !== 'installed-joint');
      part.location = 'workfront';
      part.condition = 'inspection-required';
      for (const connection of Object.values(part.connections)) part.supports.push({ kind: 'capture-seat', id: connection.id });
      robots.forEach(robot => { robot.tool = 'driver'; robot.mode = 'work'; });
      changePhase(part, 'verified', 'final', event);
      break;
    case 'unfasten':
      requireState(hasHoist(part), 'Unfastening requires hoist support');
      changePhase(part, 'final', 'captured', event);
      break;
    case 'release-capture':
      requireState(hasHoist(part), 'Capture release requires hoist support');
      changePhase(part, 'captured', 'absent', event);
      part.supports = part.supports.filter(s => s.kind !== 'capture-seat');
      break;
    case 'lower':
      requireState(hasHoist(part) && phases(part, 'absent'), 'Lowering requires extracted member supported by hoist');
      break;
    case 'return':
      requireState(hasHoist(part) && phases(part, 'absent'), 'Return requires safely extracted member');
      part.location = 'inspection-yard';
      part.supports = [{ kind: 'stock-rack', id: 'inspection-rack' }];
      part.assignedTarget = null;
      world.equipment.hoistBusy = false;
      break;
    case 'inspect-part':
      requireState(part.location === 'inspection-yard' && part.condition === 'inspection-required', 'Inspection requires returned part');
      part.condition = event.data.condition ?? 'qualified';
      break;
    case 'qualify-reuse':
      requireState(part.location === 'inspection-yard' && part.condition === 'qualified', 'Reuse qualification requires a passing inspection');
      part.location = 'stock';
      part.supports = [{ kind: 'stock-rack', id: 'reuse-rack' }];
      break;
    case 'fault':
      requireState(!!event.data.fault, 'Fault kind required');
      world.activeFaults[event.partId] = { kind: event.data.fault!, detectedAt: event.time, message: event.data.message ?? event.label };
      if (event.data.fault !== 'delivery-delay') {
        requireState(hasHoist(part), 'Assembly failure requires retained hoist support');
        robots.forEach(robot => { robot.mode = 'hold'; robot.tool = 'parked'; });
      }
      break;
    case 'recover':
      requireState(!!event.data.fault, 'Recovery kind required');
      requireState(world.activeFaults[event.partId]?.kind === event.data.fault, 'Recovery must match an active fault');
      if (event.data.fault === 'mis-seat') changePhase(part, 'aligned', 'absent', event);
      robots.forEach(robot => { robot.lockedGrips = 4; robot.tool = 'parked'; robot.mode = 'travel'; });
      delete world.activeFaults[event.partId];
      break;
    case 'complete':
      requireState(part.useCount >= 2 && part.location === 'installed' && !world.equipment.hoistBusy, 'Scenario requires completed second use');
      world.status = 'complete';
      break;
  }
  if (event.poseTo) part.position = [...event.poseTo] as Vec3;
  if (carrierMotion) world.equipment.carrierPosition = [...carrierMotion.to] as Vec3;
  if (hookMotion) world.equipment.hoistHookPosition = [...hookMotion.to] as Vec3;
  if (event.data.yaw !== undefined) part.yaw = event.data.yaw;
  world.time = event.time;
  world.revision = event.sequence;
  assertWorldInvariants(world);
  return world;
}

export function runScenario(scenario: Scenario): SimulationTrace {
  assertWorldInvariants(scenario.initialWorld);
  let world = structuredClone(scenario.initialWorld);
  const checkpoints = scenario.events.map(event => {
    world = applyEvent(world, event);
    return { eventId: event.id, time: event.time, world };
  });
  return {
    scenarioId: scenario.id, seed: scenario.seed,
    initialWorld: structuredClone(scenario.initialWorld), events: structuredClone(scenario.events),
    checkpoints, finalWorld: structuredClone(world), assumptions: [...scenario.assumptions],
  };
}

/** Returns a fresh snapshot; presentation never mutates the simulation's custody. */
export function worldAtTime(trace: SimulationTrace, time: number): WorldState {
  let low = 0;
  let high = trace.checkpoints.length;
  while (low < high) {
    const mid = Math.floor((low + high) / 2);
    if (trace.checkpoints[mid].time <= time) low = mid + 1;
    else high = mid;
  }
  return structuredClone(low ? trace.checkpoints[low - 1].world : trace.initialWorld);
}

/** Presentation interpolation only. Events commit complete motions at their end. */
export function partPoseAtTime(trace: SimulationTrace, partId: string, time: number): Vec3 {
  const next = trace.events.find(event => event.partId === partId && event.poseFrom && event.poseTo && time >= event.time - event.duration && time < event.time);
  if (next?.poseFrom && next.poseTo) {
    const fraction = next.duration === 0 ? 1 : Math.min(1, Math.max(0, (time - next.time + next.duration) / next.duration));
    return next.poseFrom.map((value, i) => value + (next.poseTo![i] - value) * fraction) as unknown as Vec3;
  }
  const part = worldAtTime(trace, time).parts[partId];
  if (!part) throw new Error(`Unknown part: ${partId}`);
  return part.position;
}

export function equipmentPoseAtTime(trace: SimulationTrace, equipment: 'carrier' | 'hoistHook', time: number): Vec3 {
  const next = trace.events.find(event => event.equipmentMotion?.[equipment] && time >= event.time - event.duration && time < event.time);
  const motion = next?.equipmentMotion?.[equipment];
  if (motion && next) {
    const fraction = next.duration === 0 ? 1 : Math.min(1, Math.max(0, (time - next.time + next.duration) / next.duration));
    return motion.from.map((value, i) => value + (motion.to[i] - value) * fraction) as unknown as Vec3;
  }
  const world = worldAtTime(trace, time);
  return equipment === 'carrier' ? world.equipment.carrierPosition : world.equipment.hoistHookPosition;
}
