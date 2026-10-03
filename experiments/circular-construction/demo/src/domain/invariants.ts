import type { WorldState } from './types';

export function materialLedger(world: WorldState) {
  const retainedMassKg = Object.values(world.parts).reduce((mass, part) => mass + world.partTypes[part.typeId].massKg, 0);
  return {
    retainedMassKg,
    inputMassKg: world.material.initialMassKg + world.material.addedMassKg,
    lostMassKg: world.material.lostMassKg,
    residualKg: world.material.initialMassKg + world.material.addedMassKg - retainedMassKg - world.material.lostMassKg,
    reusedMassKg: Object.values(world.parts).filter(part => part.useCount > 1).reduce((mass, part) => mass + world.partTypes[part.typeId].massKg, 0),
  };
}

export function assertWorldInvariants(world: WorldState): void {
  if (!Number.isFinite(world.time) || world.time < 0) throw new Error('Invalid simulation time');
  const gantry = world.equipment.hoistEnvelope;
  for (let axis = 0; axis < 3; axis++) {
    const { min, max } = gantry;
    const hook = world.equipment.hoistHookPosition[axis];
    if (!Number.isFinite(min[axis]) || !Number.isFinite(max[axis]) || min[axis] >= max[axis] ||
        !Number.isFinite(hook) || hook < min[axis] - 1e-8 || hook > max[axis] + 1e-8) {
      throw new Error(`Hoist hook outside gantry envelope on axis ${axis}`);
    }
  }
  for (const [id, part] of Object.entries(world.parts)) {
    if (id !== part.id) throw new Error(`Part identity mismatch: ${id}`);
    const type = world.partTypes[part.typeId];
    if (!type || !(type.massKg > 0)) throw new Error(`Unknown or invalid part type: ${part.typeId}`);
    if (part.supports.length === 0) throw new Error(`Unsupported part: ${id}`);
    if (!part.position.every(Number.isFinite)) throw new Error(`Invalid part position: ${id}`);
    const supportKeys = part.supports.map(support => `${support.kind}:${support.id}`);
    if (new Set(supportKeys).size !== supportKeys.length) throw new Error(`Duplicate custody: ${id}`);
    const installed = Object.values(part.connections).every(connection => connection.phase === 'verified');
    if (part.location === 'installed' && (!installed || !part.supports.some(support => support.kind === 'installed-joint'))) {
      throw new Error(`Installed part has no verified joint custody: ${id}`);
    }
    if (part.supports.some(support => support.kind === 'installed-joint') && !installed) throw new Error(`Unverified joint carries load: ${id}`);
    for (const connection of Object.values(part.connections)) {
      if (connection.phase === 'verified' && connection.verifiedAt === null) throw new Error(`Missing verification record: ${connection.id}`);
      if (part.supports.some(support => support.kind === 'capture-seat' && support.id === connection.id)
        && !['captured', 'final', 'verified'].includes(connection.phase)) throw new Error(`Absent latch carries load: ${connection.id}`);
    }
    if (part.location === 'stock' && part.condition !== 'qualified') throw new Error(`Unqualified part in available stock: ${id}`);
    if (part.supports.some(support => support.kind === 'carrier')) {
      const position = world.equipment.carrierPosition;
      if (part.position.some((value, axis) => Math.abs(value - position[axis] - (axis === 2 ? world.equipment.carrierDeckHeight : 0)) > 1e-8)) {
        throw new Error(`Carrier is not beneath its supported part: ${id}`);
      }
    }
    if (part.supports.some(support => support.kind === 'hoist')) {
      const hook = world.equipment.hoistHookPosition;
      if (part.position.some((value, axis) => Math.abs(value - hook[axis] + (axis === 2 ? world.equipment.hoistSlingHeight : 0)) > 1e-8)) {
        throw new Error(`Hoist hook is not at its supported part sling apex: ${id}`);
      }
    }
  }
  for (const robot of Object.values(world.robots)) {
    if (!Number.isInteger(robot.lockedGrips) || robot.lockedGrips < 3 || robot.lockedGrips > 4) throw new Error(`Robot lacks conservative grip count: ${robot.id}`);
    if (robot.mode === 'travel' && robot.tool !== 'parked') throw new Error(`Robot travels with working tool: ${robot.id}`);
  }
  if (Math.abs(materialLedger(world).residualKg) > 1e-8) throw new Error('Material account does not reconcile');
}
