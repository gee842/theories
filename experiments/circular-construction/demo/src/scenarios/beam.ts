import type { EventAction, EventData, ExecutionEvent, PartInstance, Scenario, Vec3, WorldState } from '../domain/types';

export type BeamFailure = 'none' | 'mis-seat' | 'grip-unavailable' | 'delivery-delay';
export interface BeamScenarioOptions { seed?: number; failure?: BeamFailure; }
export const BEAM_ID = 'steel-beam-001';
export const BEAM_POSITIONS = {
  stock: [-5, -4, 0.7] as Vec3,
  delivery: [-1, -3, 0.7] as Vec3,
  liftedA: [1.5, 0, 3.777] as Vec3,
  installedA: [1.5, 0, 3.327] as Vec3,
  clearA: [1.5, 0, 3.777] as Vec3,
  inspection: [-4, 3, 0.7] as Vec3,
  liftedB: [1.5, 3, 3.777] as Vec3,
  installedB: [1.5, 3, 3.327] as Vec3,
};
export const HOIST_SLING_HEIGHT = 0.65;
export const CARRIER_DECK_HEIGHT = 0.7;
export function hookAbove(position: Vec3): Vec3 { return [position[0], position[1], position[2] + HOIST_SLING_HEIGHT]; }
export function carrierBelow(position: Vec3): Vec3 { return [position[0], position[1], position[2] - CARRIER_DECK_HEIGHT]; }

function part(id: string, typeId: string, position: Vec3, fixture = false): PartInstance {
  return {
    id, typeId, condition: 'qualified', location: fixture ? 'workfront' : 'stock',
    position, yaw: 0, supports: [{ kind: fixture ? 'ground-anchor' : 'stock-rack', id: fixture ? `anchor-${id}` : 'new-stock-rack' }],
    connections: {
      A: { id: `${id}:A`, end: 'A', targetId: '', phase: 'absent', verifiedAt: null },
      B: { id: `${id}:B`, end: 'B', targetId: '', phase: 'absent', verifiedAt: null },
    },
    useCount: 0, assignedTarget: null, reserved: false,
  };
}

export function createInitialWorld(): WorldState {
  const parts = {
    [BEAM_ID]: part(BEAM_ID, 'beam-3m', BEAM_POSITIONS.stock),
    'fixture-A-left': part('fixture-A-left', 'anchor-fixture', [0, 0, 1.5], true),
    'fixture-A-right': part('fixture-A-right', 'anchor-fixture', [3, 0, 1.5], true),
    'fixture-B-left': part('fixture-B-left', 'anchor-fixture', [0, 3, 1.5], true),
    'fixture-B-right': part('fixture-B-right', 'anchor-fixture', [3, 3, 1.5], true),
  };
  return {
    schemaVersion: 1, time: 0, revision: 0,
    partTypes: {
      'beam-3m': { id: 'beam-3m', label: '3 m reusable steel beam', kind: 'beam', dimensions: [3, 0.146, 0.254], massKg: 93.3, material: 'steel', interfaceFamily: 'capture-bolt-v1' },
      'anchor-fixture': { id: 'anchor-fixture', label: 'Anchored test fixture', kind: 'fixture', dimensions: [0.28, 0.28, 3], massKg: 120, material: 'steel', interfaceFamily: 'capture-bolt-v1' },
    },
    parts,
    robots: {
      'climber-1': { id: 'climber-1', position: [0, -0.45, 2.55], lockedGrips: 4, tool: 'parked', mode: 'travel' },
      'climber-2': { id: 'climber-2', position: [3, -0.45, 2.55], lockedGrips: 4, tool: 'parked', mode: 'travel' },
      'climber-3': { id: 'climber-3', position: [0, 3.68, 2.25], lockedGrips: 4, tool: 'parked', mode: 'travel' },
      'climber-4': { id: 'climber-4', position: [3, 3.68, 2.25], lockedGrips: 4, tool: 'parked', mode: 'travel' },
    },
    equipment: {
      hoistId: 'hoist-1', hoistBusy: false, carrierId: 'carrier-1', carrierBusy: false,
      carrierPosition: carrierBelow(BEAM_POSITIONS.stock), carrierDeckHeight: CARRIER_DECK_HEIGHT,
      hoistHookPosition: [-1, -3, 4.5], hoistSlingHeight: HOIST_SLING_HEIGHT,
      hoistEnvelope: { min: [-6.25, -5.5, 1.0], max: [4.25, 5.6, 5.18] },
    },
    activeFaults: {},
    material: { initialMassKg: 573.3, addedMassKg: 0, lostMassKg: 0 },
    status: 'running',
  };
}

/** A bounded first mechanism experiment, with explicit modeled controller durations. */
export function createBeamScenario(options: BeamScenarioOptions = {}): Scenario {
  const seed = options.seed ?? 42;
  const failure = options.failure ?? 'none';
  const events: ExecutionEvent[] = [];
  let time = 0;
  let position = BEAM_POSITIONS.stock;
  let carrierPosition = carrierBelow(BEAM_POSITIONS.stock);
  let hookPosition: Vec3 = [-1, -3, 4.5];
  const add = (action: EventAction, duration: number, label: string, data: EventData = {}, poseTo?: Vec3, equipmentTo?: { carrier?: Vec3; hoistHook?: Vec3 }) => {
    time += duration;
    const sequence = events.length + 1;
    const targets = { ...equipmentTo };
    if (poseTo) {
      if (action === 'deliver') targets.carrier = carrierBelow(poseTo);
      else targets.hoistHook = hookAbove(poseTo);
    }
    const equipmentMotion: NonNullable<ExecutionEvent['equipmentMotion']> = {};
    if (targets.carrier) equipmentMotion.carrier = { from: carrierPosition, to: targets.carrier };
    if (targets.hoistHook) equipmentMotion.hoistHook = { from: hookPosition, to: targets.hoistHook };
    events.push({ id: `beam-${sequence.toString().padStart(3, '0')}`, sequence, time, duration, action, partId: BEAM_ID, label, data,
      ...(poseTo ? { poseFrom: position, poseTo } : {}),
      ...(Object.keys(equipmentMotion).length ? { equipmentMotion } : {}),
    });
    if (poseTo) position = poseTo;
    if (targets.carrier) carrierPosition = targets.carrier;
    if (targets.hoistHook) hookPosition = targets.hoistHook;
  };
  const install = (target: 'A' | 'B', fault: BeamFailure) => {
    const lifted = target === 'A' ? BEAM_POSITIONS.liftedA : BEAM_POSITIONS.liftedB;
    const installed = target === 'A' ? BEAM_POSITIONS.installedA : BEAM_POSITIONS.installedB;
    add('reserve', 2, `Allocate ${BEAM_ID} to configuration ${target}`, { targetId: `configuration-${target}` });
    add('receive', 8, 'Carrier receives beam on restrained cradle');
    if (fault === 'delivery-delay') {
      const delay = 30 + (Math.abs(Math.trunc(seed)) % 21);
      add('fault', delay, 'Delivery queue holds carrier with supported beam', { fault, message: 'Hoist approach lane occupied; carrier remains in its cradle.' });
      add('recover', 3, 'Approach lane released; resume delivery', { fault });
    }
    add('deliver', 18, `Carrier delivers to workfront ${target}`, {}, BEAM_POSITIONS.delivery);
    add('move-hook', 12, 'Move trolley above the delivery cradle at clear height', {}, undefined, { hoistHook: [-1, -3, 4.5] });
    add('move-hook', 10, 'Lower detached hook to the delivery sling', {}, undefined, { hoistHook: hookAbove(BEAM_POSITIONS.delivery) });
    add('attach-hoist', 7, 'Connect lifting sling while carrier retains support');
    add('release-carrier', 3, 'Tension hoist cradle and release carrier restraints before movement');
    add('lift', 14, 'Raise beam vertically above neighboring fixtures', {}, [-1, -3, 3.777]);
    add('move-hoist', 15, `Traverse supported beam to workfront ${target}`, {}, lifted);
    if (fault === 'grip-unavailable') {
      add('fault', 5, 'Dock unavailable: robots and hoist hold position', { fault, message: 'Planned rail docking socket unavailable; choose adjacent socket.' });
      add('recover', 14, 'Regrasp available socket; retain three attached limbs', { fault, robotId: 'climber-1' });
    }
    add('guide', 12, 'Two anchored climbers guide beam ends', {}, installed);
    if (fault === 'mis-seat') {
      add('fault', 5, 'Latch misalignment detected before capture', { fault, message: 'Hoist keeps the entire beam supported; capture has not passed.' });
      add('recover', 10, 'Retract beam from lead-in and reset alignment', { fault }, lifted);
      add('guide', 16, 'Repeat approach with corrected alignment', {}, installed);
    }
    add('capture', 8, 'Engage temporary positive capture at both ends');
    add('fasten', 24, 'Climbers exchange guide tool for fastening driver');
    add('verify', 12, 'Inspect both reversible end connections');
    add('transfer-load', 6, 'Transfer beam custody to verified end joints');
    add('detach-hoist', 6, 'Release hoist after verified load transfer');
    add('move-hook', 8, 'Raise detached hook clear of completed member', {}, undefined, { hoistHook: [installed[0], installed[1], 4.5] });
    add('park-tools', 5, 'Park tools and attach the free limb');
    add('retreat', 10, 'Climbers return to prepared rail stances');
  };
  install('A', failure);
  add('move-hook', 8, 'Lower detached hook to the installed beam sling', {}, undefined, { hoistHook: hookAbove(BEAM_POSITIONS.installedA) });
  add('attach-hoist', 8, 'Reconnect hoist before dismantling');
  add('begin-removal', 6, 'Retake beam load; temporary latches retain alignment');
  add('unfasten', 24, 'Remove reversible fasteners under hoist support');
  add('release-capture', 8, 'Release latches while hoist retains beam');
  add('lower', 22, 'Lift beam vertically clear of both open seats', {}, BEAM_POSITIONS.clearA);
  add('move-hoist', 20, 'Traverse recovered beam to inspection yard above fixtures', {}, [-4, 3, 3.777]);
  add('return', 15, 'Lower recovered beam vertically onto inspection rack', {}, BEAM_POSITIONS.inspection);
  add('move-hook', 10, 'Raise detached hook above inspection rack', {}, undefined, { hoistHook: [-4, 3, 4.5] });
  add('park-tools', 5, 'Park tools after removal');
  add('retreat', 8, 'Return robots to travel mode');
  add('inspect-part', 18, 'Dimensional and condition inspection of recovered member', { condition: 'qualified' });
  add('qualify-reuse', 3, 'Return the same identified beam to qualified stock');
  add('move-carrier', 20, 'Empty carrier travels from delivery station to inspection rack', {}, undefined, { carrier: carrierBelow(BEAM_POSITIONS.inspection) });
  install('B', 'none');
  add('complete', 2, 'Same beam completes second useful configuration');
  return {
    id: `reversible-beam-${failure}`, seed, initialWorld: createInitialWorld(), events,
    assumptions: [
      'SI units and Z-up coordinates. The 3 m beam uses the researched 31.1 kg/m handling example, not a sized structural member.',
      'Anchored fixture pair A and pair B are supplied laboratory supports. Their fabrication and foundation installation are outside this mechanism experiment.',
      'Controller task times are declared illustrative inputs, not measured robot performance.',
      'Connection observations are idealized; capture, fastening and inspection remain different recorded operations.',
      'Custody and transition checks run here. Grip count is a sequencing constraint, not a proof of contact or structural adequacy.',
      'The cradle, hoist, fixtures and robot motions require independent numerical geometry and load checks before engineering acceptance.',
      'This first experiment preserves the beam and fixtures without remanufacturing, consumables or losses; it makes no whole-building circularity claim.',
    ],
  };
}
