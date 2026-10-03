import { cataloguePart, catalogueRevision, constructionContract, defaultCatalogueId } from './catalogue';
import { composePose, interpolatePose, transformedAxis } from './transforms';
import type { CatalogueId, ConstructionMission, ConstructionPhase, ConstructionPlan, ConstructionSnapshot, PartDefinition, PartKind, PartState, Pose, RobotDefinition, RobotState, RobotTrack, Stage, TimedPose, Vec3 } from './types';

const H = constructionContract.building.storeyHeightM;
const FLOORS = constructionContract.building.storeys;
const AX = Array.from({ length: 4 }, (_, lane) => -constructionContract.building.widthM / 2 + lane * constructionContract.building.widthM / 3);
const clamp = (n: number, a = 0, b = 1) => Math.max(a, Math.min(b, n));
const pose = (position: Vec3, rotation: Vec3 = [0, 0, 0]): Pose => ({ position, rotation });
const mix = (a: Vec3, b: Vec3, u: number): Vec3 => a.map((v, i) => v + (b[i] - v) * u) as Vec3;
function route(start: number, points: Vec3[], speed = .7, initialYaw?: number): TimedPose[] {
  let time = start;
  const result: TimedPose[] = [];
  let incomingYaw = initialYaw ?? -Math.PI / 2;
  for (let i = 0; i < points.length; i++) {
    const point = points[i];
    if (i) {
      const previous = points[i - 1];
      const vertical = Math.abs(point[1] - previous[1]);
      const horizontal = Math.hypot(point[0] - previous[0], point[2] - previous[2]);
      time += vertical / .01174 + horizontal / speed;
    }
    const next = points[Math.min(i + 1, points.length - 1)];
    const dx = next[0] - point[0], dz = next[2] - point[2];
    const outgoingYaw = Math.abs(dx) + Math.abs(dz) > .001 ? -Math.atan2(dz, dx) : i + 1 < points.length && Math.abs(next[1] - point[1]) > .001 ? -Math.PI / 2 : incomingYaw;
    if (!i && initialYaw === undefined) incomingYaw = outgoingYaw;
    result.push({ time, pose: pose(point, [0, incomingYaw, 0]) });
    const turn = Math.atan2(Math.sin(outgoingYaw - incomingYaw), Math.cos(outgoingYaw - incomingYaw));
    if (Math.abs(turn) > .01) {
      time += Math.abs(turn) / .6;
      result.push({ time, pose: pose(point, [0, incomingYaw + turn, 0]) });
    }
    incomingYaw = outgoingYaw;
  }
  return result;
}
function finishFacing(waypoints: TimedPose[], yaw: number): void {
  const last = waypoints[waypoints.length - 1];
  const delta = Math.atan2(Math.sin(yaw - last.pose.rotation[1]), Math.cos(yaw - last.pose.rotation[1]));
  if (Math.abs(delta) > .001) waypoints.push({ time: last.time + Math.abs(delta) / .6, pose: pose([...last.pose.position], [0, last.pose.rotation[1] + delta, 0]) });
}
export function sampleRoute(waypoints: TimedPose[], time: number): Pose {
  if (!waypoints.length) return pose([0, 0, 0]);
  if (time <= waypoints[0].time) return structuredClone(waypoints[0].pose);
  for (let i = 1; i < waypoints.length; i++) {
    const a = waypoints[i - 1], b = waypoints[i];
    if (time <= b.time) {
      const u = clamp((time - a.time) / Math.max(.001, b.time - a.time));
      const yawDelta = Math.atan2(Math.sin(b.pose.rotation[1] - a.pose.rotation[1]), Math.cos(b.pose.rotation[1] - a.pose.rotation[1]));
      return { position: mix(a.pose.position, b.pose.position, u), rotation: [a.pose.rotation[0], a.pose.rotation[1] + yawDelta * u, a.pose.rotation[2]] };
    }
  }
  return structuredClone(waypoints[waypoints.length - 1].pose);
}
const rack = (lane: number): Vec3 => [-28 + lane * 4.5, .72, -15];
const groundHome = (lane: number): Vec3 => [-34, 0, -15 - lane * 7];
const boundary = (lane: number): Vec3 => [-50, 0, -15 - lane * 5];
const columnId = (floor: number, x: number, z: number) => `column-${floor}-${x}-${z}`;

/** Finite fleet schedule. Routes are authored supported planning motions, not dynamics evidence. */
export function buildConstructionPlan(): ConstructionPlan {
  const parts: PartDefinition[] = [], robots: RobotDefinition[] = [], missions: ConstructionMission[] = [], tracks: RobotTrack[] = [], stages: Stage[] = [];
  const dimensions = { width: constructionContract.building.widthM, depth: constructionContract.building.depthM, floors: FLOORS, storeyHeight: H, bay: constructionContract.building.bayM };
  function add(kind: PartKind, id: string, position: Vec3, floor: number, rotation: Vec3 = [0, 0, 0], temporary = false, catalogueId: CatalogueId = defaultCatalogueId(kind)) {
    const lane = Math.min(3, Math.max(0, Math.round((position[0] + dimensions.width / 2) / (dimensions.width / 3))));
    const material = cataloguePart(catalogueId);
    parts.push({ id, kind, catalogueId, asset: material.asset, assetScale: [1, 1, 1], dimensions: material.dimensionsM_YUp, massKg: material.massKg, floor, finalPose: pose(position, rotation), temporary, lane });
  }
  // Four delivered 2 m shaft sections per site-qualified pile group; no soil capacity claim.
  for (let x = 0; x <= 6; x++) for (let z = 0; z <= 4; z++) {
    for (let s = 0; s < 4; s++) add('pile', `pile-${x}-${z}-${s}`, [-9 + x * 3, -1 - s * 2, -6 + z * 3], -1);
    add('foundation', `foundation-${x}-${z}`, [-9 + x * 3, .13, -6 + z * 3], -1);
  }
  for (let lane = 0; lane < 4; lane++) {
    add('foundation', `supply-cradle-${lane}`, [rack(lane)[0], .13, rack(lane)[2]], -1, [0, 0, 0], true);
    parts[parts.length - 1].lane = lane;
  }
  add('temp_service', 'mobile-service-skid', [-36, .9, -8], -1, [Math.PI / 2, 0, 0], true);
  for (let lane = 0; lane < 4; lane++) add('temp_brace', `temporary-bootstrap-brace-${lane}`, [AX[lane], 1.6, -7.5], 0, [0, Math.PI / 2, 0], true);
  for (let f = 0; f < FLOORS; f++) {
    const bottom = f * H, top = bottom + H;
    for (let x = 0; x <= 6; x++) for (let z = 0; z <= 4; z++) add('column', columnId(f, x, z), [-9 + x * 3, bottom + H / 2, -6 + z * 3], f, [0, z === 0 ? Math.PI / 2 : z === 4 ? -Math.PI / 2 : x === 0 ? Math.PI : 0, 0]);
    for (let x = 0; x < 6; x++) for (let z = 0; z <= 4; z++) {
      if (f < FLOORS - 1 && x === 2 && (z === 2 || z === 3)) continue;
      add('beam', `beam-x-${f}-${x}-${z}`, [-7.5 + x * 3, top - .14, -6 + z * 3], f);
    }
    // Shaft headers/trimmers are actual delivered beams, including half-length trimmers.
    if (f < FLOORS - 1) {
      add('beam', `stair-header-full-${f}`, [-1.5, top - .09, -1.5], f);
      for (const z of [1.5, 3]) add('beam', `stair-header-mid-${f}-${z}`, [-1.5, bottom + 1.51, z], f);
      for (const x of [-3, 0]) add('beam', `stair-trimmer-mid-${f}-${x}`, [x, bottom + 1.51, 2.25], f, [0, Math.PI / 2, 0], false, 'beam_half');
    }
    for (let x = 0; x <= 6; x++) for (let z = 0; z < 4; z++) add('beam', `beam-z-${f}-${x}-${z}`, [-9 + x * 3, top - .14, -4.5 + z * 3], f, [0, Math.PI / 2, 0]);
    for (let x = 0; x < 6; x += 2) for (const z of [-6, 6]) add('brace', `brace-${f}-${x}-${z}`, [-7.5 + x * 3, bottom + 1.6, z], f);
    for (let x = 0; x < 6; x++) for (let z = 0; z < 12; z++) {
      if (f < FLOORS - 1 && x === 2 && z >= 3 && z <= 8) continue;
      add('floor', `floor-${f}-${x}-${z}`, [-7.5 + x * 3, top + .08, -5.5 + z], f);
    }
    if (f < FLOORS - 1) {
      add('landing', `landing-full-${f}`, [-1.5, top + .08, -2.25], f);
      add('landing', `landing-mid-${f}`, [-1.5, bottom + 1.68, 2.25], f);
    }
    // Segmented lightweight partitions and two reversible flights per storey.
    for (let i = 0; i < 3; i++) for (const z of [-3, 3]) {
      if (z === -3) {
        if (i === 1) {
          add('core', `core-entry-${f}`, [-1.5, bottom + 1.51, z], f, [0, 0, 0], false, 'entry');
        } else {
          add('core', `core-end-${f}-${i}-${z}`, [i === 0 ? -2.625 : -.375, bottom + 1.51, z], f, [0, 0, 0], false, 'core_half');
        }
      } else add('core', `core-end-${f}-${i}-${z}`, [-2.5 + i, bottom + 1.51, z], f);
    }
    for (let i = 0; i < 6; i++) for (const x of [-3, 0]) {
      // Leave the first end module open as the landing doorway.
      if (i === 0) continue;
      add('core', `core-side-${f}-${i}-${x}`, [x, bottom + 1.51, -2.5 + i], f, [0, Math.PI / 2, 0]);
    }
    if (f < FLOORS - 1) {
      add('stair', `stair-${f}-0`, [-2.15, bottom + .96, 0], f);
      add('stair', `stair-${f}-1`, [-.85, bottom + 2.56, 0], f, [0, Math.PI, 0]);
    }
    for (let i = 0; i < 4; i++) add('service', `service-${f}-${i}`, [i % 2 ? 6 : -6, bottom + 1.5, i < 2 ? -3 : 3], f);
    for (let x = 0; x < 12; x++) for (const z of [-6.12, 6.12]) {
      if (f === 0 && z < 0 && (x === 4 || x === 5)) continue;
      add('facade', `facade-x-${f}-${x}-${z}`, [-8.25 + x * 1.5, bottom + 1.51, z], f);
    }
    if (f === 0) {
      add('facade', 'building-entry', [-1.5, 1.51, -6.12], f, [0, 0, 0], false, 'entry');
      add('facade', 'building-entry-surround-left', [-2.625, 1.51, -6.12], f, [0, 0, 0], false, 'core_half');
      add('facade', 'building-entry-surround-right', [-.375, 1.51, -6.12], f, [0, 0, 0], false, 'core_half');
    }
    for (let z = 0; z < 8; z++) for (const x of [-9.12, 9.12]) add('facade', `facade-z-${f}-${x}-${z}`, [x, bottom + 1.51, -5.25 + z * 1.5], f, [0, Math.PI / 2, 0]);
    if (f % 4 === 3) for (const x of [-6, 6]) {
      add('terrace', `terrace-${f}-${x}`, [x, top + .08, 6.5], f);
      add('planter', `planter-${f}-${x}`, [x, top + .28, 6.6], f);
    }
  }
  for (let x = 0; x < 6; x++) for (let z = 0; z < 12; z++) add('floor', `ground-floor-${x}-${z}`, [-7.5 + x * 3, .08, -5.5 + z], -1);
  for (let x = 0; x < 6; x++) for (let z = 0; z < 12; z++) add('roof', `roof-${x}-${z}`, [-7.5 + x * 3, FLOORS * H + .26, -5.5 + z], FLOORS);
  for (let lane = 0; lane < 4; lane++) {
    for (let n = 0; n < 2; n++) robots.push({ id: `carrier-${lane * 2 + n}`, kind: 'carrier', lane, home: [rack(lane)[0], .72, -20 - n * 4.5] });
    robots.push({ id: `assembler-${lane}`, kind: 'assembler', lane, home: [rack(lane)[0], .72, -8] });
    robots.push({ id: `cargo-${lane}`, kind: 'cargo_rover', lane, home: [-43, 0, -15 - lane * 5] });
  }
  for (let i = 0; i < 2; i++) robots.push({ id: `builder-${i}`, kind: 'ground_builder', lane: i, home: groundHome(i) });
  const addTrack = (robotId: string, action: string, waypoints: TimedPose[], partId?: string, supportIds: string[] = ['terrain']) => {
    const r = robots.find(item => item.id === robotId)!;
    tracks.push({ robotId, start: waypoints[0].time, end: waypoints[waypoints.length - 1].time, action, partId, lane: r.lane, waypoints, supportIds });
  };
  stages.push({ phase: 'empty', start: 0, end: 20, label: 'Empty flat land · qualified-ground assumption declared' });
  for (const r of robots) {
    if (r.kind === 'cargo_rover') continue; // Cargo joins the opening convoy already loaded.
    const begin = 20 + robots.indexOf(r) * 2;
    addTrack(r.id, 'arrive with tools and empty cradle', route(begin, [boundary(r.lane), [-46, r.home[1], r.home[2]], r.home], 1));
  }
  const arrivalEnd = Math.max(...tracks.map(t => t.end));
  stages.push({ phase: 'arrival', start: 20, end: arrivalEnd, label: 'Fleet enters the site boundary' });
  const cargoFree = [arrivalEnd, arrivalEnd, arrivalEnd, arrivalEnd];
  const cargoDelivered = [false, false, false, false];
  const laneFree = [arrivalEnd + 15, arrivalEnd + 15, arrivalEnd + 15, arrivalEnd + 15];
  const builderFree = [arrivalEnd + 15, arrivalEnd + 15];
  const assemblerPosition = Array.from({ length: 4 }, (_, l) => robots.find(r => r.id === `assembler-${l}`)!.home);
  const builderPosition = [groundHome(0), groundHome(1)];
  const assemblerExit: Vec3[][] = AX.map(x => [[x, .72, -6.93]]);
  const uses = [0, 0, 0, 0];
  let groupStart = arrivalEnd;
  let accepted: string[] = [];
  function installGroup(group: PartDefinition[], phase: ConstructionPhase, label: string, ground = false) {
    if (!group.length) return;
    const phaseStart = groupStart;
    let groupEnd = groupStart;
    const previousAccepted = [...accepted];
    for (const p of group) {
      const l = p.lane, loadRack = rack(l);
      const rover = `cargo-${l}`;
      const builder = ground ? (p.id.length + uses[l]) % 2 : -1;
      // Dispatch just in time so a lane has one supplied payload instead of overlapping stock meshes.
      const openingDelivery = !cargoDelivered[l];
      const arrivalStart = openingDelivery ? 20 + robots.findIndex(r => r.id === rover) * 2 : Math.max(cargoFree[l], groupStart - 35, (ground ? builderFree[builder] : laneFree[l]) - 35);
      cargoDelivered[l] = true;
      const incoming = route(arrivalStart, [boundary(l), [loadRack[0], 0, boundary(l)[2]], [loadRack[0], 0, loadRack[2]]], 1.2);
      const arrived = incoming[incoming.length - 1].time;
      addTrack(rover, openingDelivery ? 'arrive carrying secured site equipment' : 'deliver secured factory cargo', incoming, p.id);
      const unloading = [{ time: arrived, pose: incoming[incoming.length - 1].pose }, { time: arrived + 12, pose: incoming[incoming.length - 1].pose }];
      addTrack(rover, 'unload to supported supply cradle', unloading, p.id);
      const cargoReturn = route(arrived + 12, [incoming[incoming.length - 1].pose.position, [loadRack[0], 0, boundary(l)[2]], boundary(l)], 1.2);
      addTrack(rover, 'return to supply boundary', cargoReturn);
      cargoFree[l] = cargoReturn[cargoReturn.length - 1].time + 5;
      const assemblerId = ground ? `builder-${builder}` : `assembler-${l}`;
      const carrierId = ground ? assemblerId : `carrier-${l * 2 + uses[l] % 2}`;
      uses[l]++;
      const begin = Math.max(groupStart, ground ? builderFree[builder] : laneFree[l], arrived + 18);
      let pickup = begin;
      let secured: number, attached: number, rendezvous: number, captured: number, installed: number, returned: number;
      let delivery: TimedPose[];
      const supportFloor = p.kind === 'column' ? p.floor - 1 : Math.min(FLOORS - 1, p.floor);
      const routeSupportIds = ground ? ['terrain'] : Array.from({ length: supportFloor + 1 }, (_, f) => columnId(f, (AX[l] + 9) / 3, 0));
      const prerequisites = ground ? previousAccepted.slice(-4) : [...routeSupportIds];
      if (ground) {
        const pickupApproach = route(begin, [builderPosition[builder], [loadRack[0], 0, loadRack[2]]], .8);
        pickup = pickupApproach[pickupApproach.length - 1].time;
        addTrack(carrierId, 'approach supplied material', pickupApproach);
        secured = pickup + 10;
        const at: Vec3 = [p.finalPose.position[0], 0, p.finalPose.position[2] - .8];
        delivery = route(secured, [[loadRack[0], 0, loadRack[2]], [at[0], 0, -10], at], .8, pickupApproach[pickupApproach.length - 1].pose.rotation[1]);
        addTrack(carrierId, 'capture and secure supplied material', [{ time: pickup, pose: pickupApproach[pickupApproach.length - 1].pose }, { time: secured, pose: delivery[0].pose }], p.id);
        attached = secured;
        rendezvous = delivery[delivery.length - 1].time;
        captured = rendezvous + 8;
        installed = captured + (p.kind === 'pile' ? 45 : 22);
        addTrack(carrierId, p.kind === 'pile' ? 'carry pile section and screw into ground' : 'carry and install from ground', [...delivery, { time: installed, pose: delivery[delivery.length - 1].pose }], p.id);
        const returnRoute = route(installed, [at, [at[0], 0, -10], [loadRack[0], 0, loadRack[2]]], .8);
        returned = returnRoute[returnRoute.length - 1].time;
        addTrack(carrierId, 'return for next material', returnRoute);
        builderPosition[builder] = returnRoute[returnRoute.length - 1].pose.position;
        builderFree[builder] = returned;
      } else {
        const y = (supportFloor + 1) * H - .8;
        let rx = Math.round(clamp(p.finalPose.position[0], -9, 9) / 3) * 3;
        if (rx === 0) rx = 3;
        if (['core', 'stair', 'landing'].includes(p.kind)) rx = p.finalPose.position[0] < -1 ? -6 : 3; // Keep through-traffic outside the reserved stair/core box.
        const rz = Math.round(clamp(p.finalPose.position[2], -6, 6) / 3) * 3;
        // Stand outside the member, with chassis .93 m from column centre and .75 m from rail.
        const railStance = (x: number, z: number): { position: Vec3; yaw: number } => z === -6 ? { position: [x, y, -6.93], yaw: -Math.PI / 2 } : z === 6 ? { position: [x, y, 6.93], yaw: Math.PI / 2 } : x === -9 ? { position: [-9.93, y, z], yaw: 0 } : { position: [x + .93, y, z], yaw: Math.PI };
        const receivingStance = railStance(rx, rz);
        const receive: Vec3 = receivingStance.position;
        const receiveYaw = receivingStance.yaw;
        const sideFacade = p.kind === 'facade' && Math.abs(rx) === 9 && Math.abs(rz) < 6;
        const dockNodeX = sideFacade ? rx : rx <= -6 ? rx + 3 : rx - 3;
        const dockNodeZ = sideFacade ? (rz < 3 ? rz + 3 : rz - 3) : rz;
        const dockingStance = railStance(dockNodeX, dockNodeZ);
        const carrierDock: Vec3 = dockingStance.position;
        routeSupportIds.push(columnId(supportFloor, (rx + 9) / 3, (rz + 6) / 3), columnId(supportFloor, (dockNodeX + 9) / 3, (dockNodeZ + 6) / 3));
        prerequisites.push(...routeSupportIds.slice(-2));
        const previous = assemblerPosition[l];
        const shaft: Vec3 = [AX[l], y, -6.93];
        const accessTo = (point: Vec3): Vec3[] => {
          if (p.kind !== 'facade') return [shaft, [point[0], y, -6.93], point];
          const side = AX[l] < 0 ? -9.93 : 9.93;
          return point[2] < -6 ? [shaft, point] : [shaft, [side, y, -6.93], [side, y, point[2]], point];
        };
        const access = accessTo(receive), carrierAccess = accessTo(carrierDock);
        // Reverse the last reserved route, ascend on exterior accepted columns, then traverse.
        const reposition = route(begin, [previous, ...assemblerExit[l], ...access], .6);
        finishFacing(reposition, receiveYaw);
        addTrack(assemblerId, 'climb and traverse to supported receiving position', reposition, undefined, routeSupportIds);
        const receiverReady = reposition[reposition.length - 1].time;
        const carrierHome = robots.find(r => r.id === carrierId)!.home;
        const pickupApproach = route(begin, [carrierHome, loadRack], .7);
        addTrack(carrierId, 'leave reserved parking and approach material cradle', pickupApproach);
        pickup = pickupApproach[pickupApproach.length - 1].time;
        if (uses[l] % 12 === 0) {
          addTrack(carrierId, 'battery exchange at mobile service cradle', [{ time: pickup, pose: pickupApproach[pickupApproach.length - 1].pose }, { time: pickup + 45, pose: pickupApproach[pickupApproach.length - 1].pose }]);
          pickup += 45;
        }
        secured = pickup + 12;
        const approach = route(secured, [loadRack, [AX[l], .72, -13], [AX[l], .72, -6.93]], .7, pickupApproach[pickupApproach.length - 1].pose.rotation[1]);
        attached = approach[approach.length - 1].time;
        const ascent = route(attached + 8, [[AX[l], .72, -6.93], ...carrierAccess], .55, approach[approach.length - 1].pose.rotation[1]);
        finishFacing(ascent, dockingStance.yaw);
        delivery = [...approach, ...ascent];
        const travelEnd = delivery[delivery.length - 1].time;
        rendezvous = Math.max(travelEnd, receiverReady + 5);
        if (rendezvous > travelEnd) delivery.push({ time: rendezvous, pose: delivery[delivery.length - 1].pose });
        captured = rendezvous + 12;
        installed = captured + 24;
        addTrack(carrierId, 'secure payload · approach · attach · loaded climb · rendezvous', [{ time: pickup, pose: pickupApproach[pickupApproach.length - 1].pose }, ...delivery], p.id, routeSupportIds);
        addTrack(carrierId, 'retain payload during receiver capture and fastening', [{ time: rendezvous, pose: delivery[delivery.length - 1].pose }, { time: installed, pose: delivery[delivery.length - 1].pose }], p.id, routeSupportIds);
        addTrack(assemblerId, 'supported receiver · overlap capture · seat · connect · verify', [{ time: receiverReady, pose: pose(receive, [0, receiveYaw, 0]) }, { time: installed, pose: pose(receive, [0, receiveYaw, 0]) }], p.id, routeSupportIds);
        const returnRoute = route(installed + 4, [delivery[delivery.length - 1].pose.position, ...[...ascent].reverse().map(w => w.pose.position), [AX[l], .72, -13], loadRack, carrierHome], .7);
        returned = returnRoute[returnRoute.length - 1].time;
        addTrack(carrierId, 'empty return · descend · supply queue', returnRoute, undefined, routeSupportIds);
        assemblerPosition[l] = receive;
        assemblerExit[l] = [...access].reverse();
        laneFree[l] = returned + 8;
      }
      missions.push({ id: `install-${p.id}`, partId: p.id, carrierId, assemblerId, lane: l, arrivalStart, arrived, pickup, secured, attached, rendezvous, captured, installed, returned, prerequisites, routeSupportIds, waypoints: delivery });
      groupEnd = Math.max(groupEnd, returned);
    }
    accepted.push(...group.map(p => p.id));
    groupStart = groupEnd + 12;
    stages.push({ phase, start: phaseStart, end: groupStart, label });
  }
  installGroup(parts.filter(p => p.kind === 'temp_service'), 'bootstrap', 'Deploy supplied tools, survey and mobile battery service', true);
  installGroup(parts.filter(p => p.id.startsWith('supply-cradle-')), 'bootstrap', 'Unpack delivered reusable material cradles', true);
  installGroup(parts.filter(p => p.kind === 'pile'), 'foundations', 'Ground builders screw delivered modular piles into assumed qualified ground', true);
  installGroup(parts.filter(p => p.kind === 'foundation' && !p.temporary), 'foundations', 'Install reversible grillages and accepted base seats', true);
  installGroup(parts.filter(p => p.id.startsWith('ground-floor-')), 'first-frame', 'Install delivered ground deck and stair access datum', true);
  for (let f = 0; f < FLOORS; f++) {
    const phase: ConstructionPhase = f === 0 ? 'first-frame' : f === 1 ? 'climbing' : f === FLOORS - 1 ? 'completion' : 'swarm';
    const ground = f === 0;
    for (const kinds of [['column'], ['beam'], ['temp_brace', 'brace'], ['floor', 'core', 'stair', 'landing', 'service'], ['terrace', 'planter']] as PartKind[][]) {
      installGroup(parts.filter(p => p.floor === f && kinds.includes(p.kind)), phase, `Storey ${f + 1} · ${kinds.join(', ')} · supported installation`, ground);
    }
  }
  installGroup(parts.filter(p => p.kind === 'roof'), 'completion', 'Deliver, connect and close roof cassettes');
  // Enclose only after all interior logistics; access shafts remain exterior for descent.
  for (let f = 0; f < FLOORS; f++) installGroup(parts.filter(p => p.kind === 'facade' && p.floor === f), 'completion', `Storey ${f + 1} exterior facade closure`, f === 0);
  const inspectionStart = groupStart;
  for (let l = 0; l < 4; l++) {
    const current = assemblerPosition[l];
    const inspect = route(groupStart, [current, ...assemblerExit[l], [AX[l], .72, -6.93], robots.find(r => r.id === `assembler-${l}`)!.home], .4);
    addTrack(`assembler-${l}`, 'inspect installed connections and exterior descent route', inspect, undefined, [columnId(19, (AX[l] + 9) / 3, 0)]);
    groupStart = Math.max(groupStart, inspect[inspect.length - 1].time + 30);
  }
  stages.push({ phase: 'inspection', start: inspectionStart, end: groupStart, label: 'Inspect roof, weather closure, circulation and declared service modules; assemblers descend' });
  const recoveryStart = groupStart;
  // Each temporary asset leaves on an actual finite cargo rover. Recover braces
  // before their staging cradles, and retain the service skid until the last trip.
  const recoveryOrder = (p: PartDefinition) => p.kind === 'temp_brace' ? 0 : p.kind === 'temp_service' ? 2 : 1;
  const lastPose = (id: string): Pose => {
    const list = tracks.filter(t => t.robotId === id).sort((a, b) => a.start - b.start);
    const last = list[list.length - 1];
    return structuredClone(last.waypoints[last.waypoints.length - 1].pose);
  };
  for (const p of parts.filter(p => p.temporary).sort((a, b) => recoveryOrder(a) - recoveryOrder(b))) {
    const m = missions.find(mission => mission.partId === p.id)!;
    const builder = `builder-${p.lane % 2}`, rover = `cargo-${p.lane}`;
    const home = groundHome(p.lane % 2);
    const packingBay: Vec3 = [rack(p.lane)[0], 0, -18.2];
    const builderBay: Vec3 = [packingBay[0], 0, -16];
    const roverApproach = route(groupStart, [lastPose(rover).position, [packingBay[0], 0, boundary(p.lane)[2]], packingBay], .8);
    addTrack(rover, 'approach recovery bay with empty cargo restraint', roverApproach);
    const approach = route(groupStart, [lastPose(builder).position, [p.finalPose.position[0], 0, p.finalPose.position[2] - .8]], .6);
    addTrack(builder, 'inspect and release temporary equipment', approach);
    m.removalStart = approach[approach.length - 1].time;
    const releasePose = approach[approach.length - 1].pose;
    addTrack(builder, 'grasp temporary asset before releasing its connections', [{ time: m.removalStart, pose: releasePose }, { time: m.removalStart + 16, pose: releasePose }], p.id);
    const recovery = route(m.removalStart + 16, [releasePose.position, [releasePose.position[0], 0, -10], builderBay], .6, releasePose.rotation[1]);
    m.removalWaypoints = recovery;
    addTrack(builder, 'carry recovered equipment to the outgoing vehicle', recovery, p.id);
    const builderReady = recovery[recovery.length - 1].time;
    const roverReady = roverApproach[roverApproach.length - 1].time;
    m.recoveryLoadStart = Math.max(builderReady, roverReady);
    m.recoveryLoaded = m.recoveryLoadStart + 16;
    m.recoveryRoverId = rover;
    const builderPose = recovery[recovery.length - 1].pose;
    const roverPose = roverApproach[roverApproach.length - 1].pose;
    addTrack(builder, 'retain recovered asset through cargo capture and restraint', [{ time: builderReady, pose: builderPose }, { time: m.recoveryLoaded, pose: builderPose }], p.id);
    addTrack(rover, 'receive and secure recovered temporary equipment', [{ time: roverReady, pose: roverPose }, { time: m.recoveryLoaded, pose: roverPose }], p.id);
    const outgoing = route(m.recoveryLoaded, [packingBay, [packingBay[0], 0, boundary(p.lane)[2]], boundary(p.lane)], .8, roverPose.rotation[1]);
    m.outgoingWaypoints = outgoing;
    m.removed = outgoing[outgoing.length - 1].time;
    addTrack(rover, 'transport recovered asset across the supply boundary', outgoing, p.id);
    const leave = route(m.recoveryLoaded, [builderBay, home]);
    addTrack(builder, 'return after outgoing cargo restraint is secured', leave);
    groupStart = Math.max(leave[leave.length - 1].time, m.removed) + 15;
  }
  stages.push({ phase: 'recovery', start: recoveryStart, end: groupStart, label: 'Recover bootstrap braces, pack service equipment and inspect ground restoration' });
  const departureStart = groupStart;
  for (const r of robots) {
    const robotTracks = tracks.filter(t => t.robotId === r.id).sort((a, b) => a.start - b.start);
    const last = robotTracks[robotTracks.length - 1];
    const from = last.waypoints[last.waypoints.length - 1].pose.position;
    const departure = route(departureStart + robots.indexOf(r) * 3, [from, [from[0], r.home[1], -16], [-25, r.home[1], -16], [boundary(r.lane)[0], r.home[1], boundary(r.lane)[2]]], .9);
    addTrack(r.id, 'packed fleet departure', departure);
    groupStart = Math.max(groupStart, departure[departure.length - 1].time);
  }
  stages.push({ phase: 'departure', start: departureStart, end: groupStart, label: 'All machines leave via the supply boundary' });
  stages.push({ phase: 'complete', start: groupStart, end: groupStart + 30, label: 'Defined 20-storey building complete · fleet departed' });
  return { schemaVersion: 1, catalogueRevision, evidence: 'planned-motion', dimensions, parts, robots, missions, tracks, stages, duration: groupStart + 30, notes: ['Authored planning motions and support assumptions, not solved contact dynamics or qualified construction capacity.', `${constructionContract.robot.specifiedPayloadLimitKg} kg proposed payload envelope is unqualified; kit column mass is ${cataloguePart('column').massKg} kg (${catalogueRevision}).`, 'Vertical timing uses the representative measured loaded speed .01174 m/s; other payloads remain unverified. Four external climbing lanes reserve loaded ascent, dock and empty descent; two carriers alternate per lane.', 'Locked reversible foundation base seats provisionally restrain individual first columns until beam and brace connections exist. Ground-qualified reversible pile groups are assumed; soil, lateral resistance, wind and staged structure require engineering qualification.', 'The ground entrance aligns with the stair/core entrance; opaque core-half entrance surrounds are provisional and exterior weather qualification remains unverified.', 'Completed scope: foundations, frame/braces, floors, modular stair/core, service risers, facade, terraces, planting and roof; commissioning and interior fit-out remain outside this demonstration.'] };
}


/** Transport orientation is robot-local, independent of the installed part yaw. */
export function transitRotation(p: PartDefinition): Vec3 {
  if (p.kind === 'brace' || p.kind === 'temp_brace') return [0, Math.PI / 2, -Math.atan2(p.dimensions[1], p.dimensions[0])];
  if (['column', 'pile', 'facade', 'core', 'service', 'temp_service'].includes(p.kind)) return [Math.PI / 2, 0, 0];
  if (p.kind === 'stair') return [0, 0, Math.PI / 2];
  // Beam and cassette longitudinal local X becomes transverse robot-local Z.
  return ['beam', 'floor', 'roof', 'landing', 'terrace'].includes(p.kind) ? [0, Math.PI / 2, 0] : [0, 0, 0];
}
export function restrainedPayloadPose(root: Pose, p: PartDefinition, robotId: string): Pose {
  const mount: Vec3 = robotId.startsWith('builder') || robotId.startsWith('cargo') ? [0, 1.1, 0] : [...constructionContract.robot.payloadMountGltfM] as Vec3;
  return composePose(root, pose(mount, transitRotation(p)));
}
function stockPose(p: PartDefinition, arrivingPose: Pose, supportTop: number, lane: number): Pose {
  const extentY = p.kind === 'brace' || p.kind === 'temp_brace' ? p.dimensions[2] / 2 : p.dimensions.reduce((sum, dimension, axis) => {
    const basis: Vec3 = [0, 0, 0]; basis[axis] = 1;
    return sum + Math.abs(transformedAxis(arrivingPose, basis)[1]) * dimension / 2;
  }, 0);
  return pose([rack(lane)[0], supportTop + extentY, rack(lane)[2]], [...arrivingPose.rotation]);
}

interface PlanIndex { parts: Map<string, PartDefinition>; missions: Map<string, ConstructionMission>; tracks: Map<string, RobotTrack[]>; arrivals: Map<string, Pose>; terrainStock: Map<string, Pose>; cradleStock: Map<string, Pose> }
const cache = new WeakMap<ConstructionPlan, PlanIndex>();
function index(plan: ConstructionPlan): PlanIndex {
  let entry = cache.get(plan);
  if (!entry) {
    entry = { parts: new Map(plan.parts.map(p => [p.id, p])), missions: new Map(plan.missions.map(m => [m.partId, m])), tracks: new Map(), arrivals: new Map(), terrainStock: new Map(), cradleStock: new Map() };
    for (const track of plan.tracks) {
      const list = entry.tracks.get(track.robotId) ?? [];
      list.push(track); entry.tracks.set(track.robotId, list);
    }
    for (const list of entry.tracks.values()) list.sort((a, b) => a.start - b.start);
    for (const p of plan.parts) {
      const m = entry.missions.get(p.id)!;
      const arrival = restrainedPayloadPose(robotPoseAt(entry, `cargo-${m.lane}`, m.arrived), p, `cargo-${m.lane}`);
      const cradle = entry.parts.get(`supply-cradle-${m.lane}`)!;
      entry.arrivals.set(p.id, arrival);
      entry.terrainStock.set(p.id, stockPose(p, arrival, 0, m.lane));
      entry.cradleStock.set(p.id, stockPose(p, arrival, cradle.finalPose.position[1] + cradle.dimensions[1] / 2, m.lane));
    }
    cache.set(plan, entry);
  }
  return entry;
}
function currentTrack(list: RobotTrack[], time: number): RobotTrack | undefined {
  let lo = 0, hi = list.length;
  while (lo < hi) { const mid = (lo + hi) >>> 1; if (list[mid].start <= time) lo = mid + 1; else hi = mid; }
  return list[lo - 1];
}
function robotPoseAt(ix: PlanIndex, robotId: string, time: number): Pose {
  const track = currentTrack(ix.tracks.get(robotId) ?? [], time);
  if (!track) throw new Error(`No pose for ${robotId} at ${time}`);
  return sampleRoute(track.waypoints, time);
}
function samplePartState(ix: PlanIndex, p: PartDefinition, time: number): PartState {
  const m = ix.missions.get(p.id)!;
  let status: PartState['status'] = 'incoming', custodian = `cargo-${m.lane}`, supports = [custodian], visible = time >= m.arrivalStart;
  const cradleMission = ix.missions.get(`supply-cradle-${m.lane}`);
  const cradleReady = cradleMission && time >= cradleMission.installed;
  const cargoAtArrival = ix.arrivals.get(p.id)!;
  const cradle = ix.parts.get(`supply-cradle-${m.lane}`)!;
  const stored = (cradleReady ? ix.cradleStock : ix.terrainStock).get(p.id)!;
  let at = structuredClone(cargoAtArrival);
  let progress = 0;
  if (time >= m.arrivalStart && time < m.arrived) {
    status = 'cargo';
    at = restrainedPayloadPose(robotPoseAt(ix, custodian, time), p, custodian);
  } else if (time >= m.arrived && time < m.pickup) {
    status = 'stored'; custodian = cradleReady ? `supply-cradle-${m.lane}` : 'terrain'; supports = [custodian];
    at = interpolatePose(cargoAtArrival, stored, (time - m.arrived) / 12);
    if (time < m.arrived + 12) supports.push(`cargo-${m.lane}`);
  } else if (time >= m.pickup && time < m.rendezvous) {
    status = 'carried'; custodian = m.carrierId; supports = [custodian];
    const mounted = restrainedPayloadPose(robotPoseAt(ix, m.carrierId, time), p, m.carrierId);
    at = time < m.secured ? interpolatePose(stored, mounted, (time - m.pickup) / (m.secured - m.pickup)) : mounted;
    if (time < m.secured) supports.push(cradleReady ? cradle.id : 'terrain');
    progress = clamp((time - m.pickup) / (m.rendezvous - m.pickup));
  } else if (time >= m.rendezvous && time < m.installed) {
    status = time < m.captured ? 'handoff' : 'installing'; custodian = time < m.captured ? `${m.carrierId}+${m.assemblerId}` : m.assemblerId;
    supports = time < m.captured ? [m.carrierId, m.assemblerId] : [m.carrierId, m.assemblerId, `capture-seat-${p.id}`];
    const from = restrainedPayloadPose(robotPoseAt(ix, m.carrierId, m.rendezvous), p, m.carrierId);
    progress = clamp((time - m.rendezvous) / (m.installed - m.rendezvous));
    at = interpolatePose(from, p.finalPose, progress);
  } else if (time >= m.installed) {
    status = 'installed'; custodian = 'accepted-structure'; supports = [`installed-joint-${p.id}`]; at = structuredClone(p.finalPose); progress = 1;

  }
  if (m.removalStart !== undefined && time >= m.removalStart) {
    const builder = `builder-${p.lane % 2}`, rover = m.recoveryRoverId!;
    status = time < m.recoveryLoadStart! ? 'recovering' : time < m.recoveryLoaded! ? 'packing' : time < m.removed! ? 'outgoing' : 'removed';
    if (time < m.recoveryLoadStart!) {
      custodian = builder; supports = [builder];
      const u = clamp((time - m.removalStart) / 16);
      if (u < 1) supports.push(`installed-joint-${p.id}`);
      const carried = restrainedPayloadPose(robotPoseAt(ix, builder, time), p, builder);
      at = interpolatePose(p.finalPose, carried, u);
    } else if (time < m.recoveryLoaded!) {
      const carried = restrainedPayloadPose(robotPoseAt(ix, builder, time), p, builder);
      const loaded = restrainedPayloadPose(robotPoseAt(ix, rover, time), p, rover);
      const u = clamp((time - m.recoveryLoadStart!) / (m.recoveryLoaded! - m.recoveryLoadStart!));
      at = interpolatePose(carried, loaded, u);
      custodian = `${builder}+${rover}`; supports = [builder, rover];
    } else {
      custodian = rover; supports = [rover];
      at = restrainedPayloadPose(robotPoseAt(ix, rover, Math.min(time, m.removed!)), p, rover);
    }
    visible = time < m.removed!;
  }
  return { id: p.id, kind: p.kind, status, pose: at, custodian, supports, progress, visible };
}
/** Reconstruct one persistent part, useful for follow cameras and inventory validation. */
export function sampleConstructionPart(plan: ConstructionPlan, partId: string, requestedTime: number): PartState {
  const ix = index(plan), p = ix.parts.get(partId);
  if (!p) throw new Error(`Unknown construction part ${partId}`);
  return samplePartState(ix, p, clamp(Number.isFinite(requestedTime) ? requestedTime : 0, 0, plan.duration));
}
/** Pure arbitrary-time reconstruction: playback speed and seek order cannot change custody. */
export function sampleConstruction(plan: ConstructionPlan, requestedTime: number): ConstructionSnapshot {
  const time = clamp(Number.isFinite(requestedTime) ? requestedTime : 0, 0, plan.duration);
  const ix = index(plan);
  const stage = plan.stages.find(s => time >= s.start && time < s.end) ?? plan.stages[plan.stages.length - 1];
  const parts = plan.parts.map(p => samplePartState(ix, p, time));
  const installedCount = parts.filter(p => p.status === 'installed' && !ix.parts.get(p.id)!.temporary).length;
  const robots: RobotState[] = plan.robots.map(r => {
    const list = ix.tracks.get(r.id)!, track = currentTrack(list, time);
    const visible = !!track && !(track.action === 'packed fleet departure' && time >= track.end);
    const running = !!track && time < track.end;
    const at = track ? sampleRoute(track.waypoints, time) : pose(boundary(r.lane));
    const heldPart = track?.partId ? parts.find(p => p.id === track.partId) : undefined;
    const payloadId = running && heldPart?.visible && heldPart.supports.includes(r.id) ? heldPart.id : null;
    const segmentEnd = running ? track!.waypoints.findIndex((w, i) => i > 0 && time <= w.time) : -1;
    const segmentA = segmentEnd > 0 ? track!.waypoints[segmentEnd - 1] : undefined;
    const segmentB = segmentEnd > 0 ? track!.waypoints[segmentEnd] : undefined;
    const dy = segmentA && segmentB ? segmentB.pose.position[1] - segmentA.pose.position[1] : 0;
    const dh = segmentA && segmentB ? Math.hypot(segmentB.pose.position[0] - segmentA.pose.position[0], segmentB.pose.position[2] - segmentA.pose.position[2]) : 0;
    const locomotion: RobotState['locomotion'] = Math.abs(dy) > .001 && dh < .001 && Math.abs(at.position[2] + 6.93) < .02 ? 'vertical-climb' : dh > .001 ? at.position[1] > 1.1 ? 'frame-traverse' : 'ground-travel' : 'hold';
    const climbing = at.position[1] > 1.1 && (r.kind === 'carrier' || r.kind === 'assembler');
    return { id: r.id, kind: r.kind, pose: at, action: running ? track!.action : visible ? 'supported wait for reserved work' : time === 0 ? 'outside supply boundary' : 'departed', payloadId, supports: climbing ? (track?.supportIds ?? []) : ['terrain'], lane: r.lane, progress: track ? clamp((time - track.start) / Math.max(1, track.end - track.start)) : 0, visible, locomotion, climbDirection: dy >= 0 ? 1 : -1, climbStartHeight: segmentA?.pose.position[1] ?? at.position[1], gait: running ? (time * .65 + r.lane) % (Math.PI * 2) : 0, gripCount: climbing ? running ? 3 : 4 : 0 };
  });
  return { time, phase: stage.phase, label: stage.label, parts, robots, installedCount, totalCount: plan.parts.filter(p => !p.temporary).length, activeTasks: robots.filter(r => r.visible && r.action !== 'supported wait for reserved work').map(r => `${r.id}: ${r.action}`), complete: stage.phase === 'complete' && robots.every(r => !r.visible) && parts.every(p => !ix.parts.get(p.id)!.temporary || p.status === 'removed') && installedCount === plan.parts.filter(p => !p.temporary).length, evidence: 'planned-motion' };
}
