import * as THREE from 'three';
import type { PlannedTask, PlanningTask, ScheduleResult, TaskGraph } from '../planning/types';

export const FRAME_PREVIEW_LABEL = 'SCHEMATIC • Planning sequence • Mechanically unverified';
export const FRAME_PREVIEW_DESCRIPTION = 'Eight generic bay-member tokens; dashed outlines are spatial guides. Reveals indicate task progress, not robot motion, load transfer, or structural validation.';

export type PreviewTaskPhase = 'pending' | 'queued' | 'active' | 'complete' | 'blocked' | 'invalid' | 'unscheduled';

export interface PreviewTaskState {
  taskId: string;
  phase: PreviewTaskPhase;
  progress: number;
  mechanicalStatus: 'unverified';
}

export interface PreviewBayState {
  bayId: string;
  memberPartId: string;
  member: PreviewTaskState;
  brace: PreviewTaskState;
  rail: PreviewTaskState;
  /** Workflow task only: completing verification does not change mechanicalStatus. */
  operation: PreviewTaskState;
  /** Reservation timing only; this does not prove hoist support. */
  liftReservationHeld: boolean;
  releasedInPlan: boolean;
  mechanicalStatus: 'unverified';
}

export interface FramePreviewSnapshot {
  label: typeof FRAME_PREVIEW_LABEL;
  timeS: number;
  durationS: number;
  scheduleStatus: ScheduleResult['status'];
  tasks: readonly PreviewTaskState[];
  bays: readonly PreviewBayState[];
  activeTaskIds: readonly string[];
  completedTaskCount: number;
  mechanicalStatus: 'unverified';
}

export interface FramePreview {
  /** Add to the host's scene. Host owns camera, renderer, clock, and visibility. */
  group: THREE.Group;
  durationS: number;
  label: typeof FRAME_PREVIEW_LABEL;
  description: typeof FRAME_PREVIEW_DESCRIPTION;
  /** Absolute planning seconds. Scrubbing backward is identical to a fresh sample. */
  setTime(timeS: number): FramePreviewSnapshot;
  snapshot(): FramePreviewSnapshot;
  dispose(): void;
}

interface Bay {
  id: string;
  storey: number;
  x: number;
  y: number;
  tasks: readonly PlanningTask[];
  memberPartId: string;
}

const colors = { complete: 0x91c5c4, active: 0xf4bd70, recovery: 0xe78072,
  brace: 0xac9575, rail: 0xb6c5d0, guide: 0x486475, seed: 0x8c9b9c };
const order = (a: string, b: string) => a < b ? -1 : a > b ? 1 : 0;

function fixtureBays(graph: TaskGraph): Bay[] {
  const bays = graph.tasks.filter(task => task.kind === 'member-placement').map(task => {
    const match = /^place-(s([12])-x([01])-y([01]))$/.exec(task.id);
    if (!match) throw new Error('Frame preview supports the two-storey 2 × 2 planning fixture only.');
    const id = match[1];
    const part = task.parts.find(item => item.mode === 'allocate');
    if (!part) throw new Error(`Missing member part for ${id}.`);
    return { id, storey: Number(match[2]), x: Number(match[3]), y: Number(match[4]),
      memberPartId: part.partId,
      tasks: graph.tasks.filter(candidate => candidate.id.endsWith(`-${id}`)).sort((a, b) => order(a.id, b.id)) };
  }).sort((a, b) => order(a.id, b.id));
  if (bays.length !== 8 || new Set(bays.map(bay => bay.id)).size !== 8)
    throw new Error('Frame preview requires eight uniquely identified bay member tasks.');
  return bays;
}

function taskState(taskId: string, row: PlannedTask | undefined, timeS: number): PreviewTaskState {
  let phase: PreviewTaskPhase = 'unscheduled';
  let progress = 0;
  if (row?.status === 'blocked' || row?.status === 'invalid') phase = row.status;
  else if (row?.startS !== undefined && row.endS !== undefined) {
    if (timeS >= row.endS) { phase = 'complete'; progress = 1; }
    else if (timeS >= row.startS) {
      phase = 'active';
      progress = (timeS - row.startS) / (row.endS - row.startS);
    } else phase = row.readyAtS !== undefined && timeS >= row.readyAtS ? 'queued' : 'pending';
  }
  return { taskId, phase, progress, mechanicalStatus: 'unverified' };
}

/** Compile once for repeated deterministic sampling; never starts a timer. */
export function createFramePreviewSampler(graph: TaskGraph, schedule: ScheduleResult):
  { durationS: number; sample(timeS: number): FramePreviewSnapshot } {
  if (schedule.graphId !== graph.id) throw new Error('Frame preview graph and schedule IDs differ.');
  const bays = fixtureBays(graph);
  const rows = new Map(schedule.tasks.map(row => [row.taskId, row]));
  const ordered = [...graph.tasks].sort((a, b) => order(a.id, b.id));
  const durationS = Math.max(0, ...schedule.tasks.map(row => row.endS ?? 0));
  return { durationS, sample(inputS) {
    if (!Number.isFinite(inputS)) throw new Error('Frame preview time must be finite.');
    const timeS = Math.min(durationS, Math.max(0, inputS));
    const tasks = ordered.map(task => taskState(task.id, rows.get(task.id), timeS));
    const states = new Map(tasks.map(task => [task.taskId, task]));
    const state = (id: string) => states.get(id) ?? taskState(id, undefined, timeS);
    return { label: FRAME_PREVIEW_LABEL, timeS, durationS, scheduleStatus: schedule.status, tasks,
      activeTaskIds: tasks.filter(task => task.phase === 'active').map(task => task.taskId),
      completedTaskCount: tasks.filter(task => task.phase === 'complete').length,
      mechanicalStatus: 'unverified',
      bays: bays.map(bay => {
        const placement = rows.get(`place-${bay.id}`);
        const release = rows.get(`release-${bay.id}`);
        // A blocked schedule can have a started lift without a scheduled release.
        const liftReservationHeld = placement?.status === 'planned'
          && placement.startS !== undefined && timeS >= placement.startS
          && (release?.endS === undefined || timeS < release.endS);
        const active = bay.tasks.map(task => state(task.id)).find(task => task.phase === 'active');
        const completed = bay.tasks.filter(task => state(task.id).phase === 'complete')
          .sort((a, b) => (rows.get(b.id)?.endS ?? 0) - (rows.get(a.id)?.endS ?? 0)
            || order(a.id, b.id));
        return { bayId: bay.id, memberPartId: bay.memberPartId,
          member: state(`place-${bay.id}`), brace: state(`brace-${bay.id}`), rail: state(`rail-${bay.id}`),
          operation: active ?? state(completed[0]?.id ?? `place-${bay.id}`),
          liftReservationHeld, releasedInPlan: state(`release-${bay.id}`).phase === 'complete',
          mechanicalStatus: 'unverified' };
      }) };
  } };
}

/** One group, one caller-owned time value. Coordinates use the site's Z-up convention. */
export function createFramePreview(graph: TaskGraph, schedule: ScheduleResult): FramePreview {
  const sampler = createFramePreviewSampler(graph, schedule);
  const bays = fixtureBays(graph);
  const group = new THREE.Group();
  group.name = `schematic-frame:${graph.id}`;
  group.userData = { label: FRAME_PREVIEW_LABEL, description: FRAME_PREVIEW_DESCRIPTION,
    mechanicalStatus: 'unverified', graphId: graph.id };
  const geometries = new Set<THREE.BufferGeometry>();
  const materials = new Set<THREE.Material>();
  const visuals = new Map<string, { member: THREE.Mesh; brace: THREE.Mesh; rail: THREE.Mesh;
    operation: THREE.Mesh; reservation: THREE.Line }>();
  const seeds = new Map<string, THREE.Mesh[]>();

  function material(color: number): THREE.MeshStandardMaterial {
    const result = new THREE.MeshStandardMaterial({ color, roughness: 0.42, metalness: 0.55 });
    materials.add(result);
    return result;
  }
  function bar(id: string, start: THREE.Vector3, end: THREE.Vector3, width: number,
    color: number, metadata: Record<string, unknown> = {}): THREE.Mesh {
    const length = start.distanceTo(end);
    const geometry = new THREE.BoxGeometry(width, length, width);
    geometries.add(geometry);
    const mesh = new THREE.Mesh(geometry, material(color));
    mesh.name = id;
    mesh.position.copy(start).add(end).multiplyScalar(0.5);
    mesh.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), end.clone().sub(start).normalize());
    mesh.castShadow = true;
    mesh.userData = { ...metadata, mechanicalStatus: 'unverified', start: start.toArray(), end: end.toArray() };
    group.add(mesh);
    return mesh;
  }
  function line(id: string, points: THREE.Vector3[], dashed: boolean): THREE.Line {
    const geometry = new THREE.BufferGeometry().setFromPoints(points);
    geometries.add(geometry);
    const lineMaterial = dashed
      ? new THREE.LineDashedMaterial({ color: colors.guide, dashSize: 0.11, gapSize: 0.10, transparent: true, opacity: 0.45 })
      : new THREE.LineBasicMaterial({ color: colors.active, transparent: true, opacity: 0.8 });
    materials.add(lineMaterial);
    const result = new THREE.Line(geometry, lineMaterial);
    result.name = id;
    result.userData = { schematicGuide: dashed, mechanicalStatus: 'unverified' };
    if (dashed) result.computeLineDistances();
    group.add(result);
    return result;
  }
  const v = (x: number, y: number, z: number) => new THREE.Vector3(x, y, z);
  // Dashed context has no task ID and never becomes installed material.
  for (const x of [0, 3, 6]) for (const y of [0, 3, 6])
    line(`guide:column:${x}:${y}`, [v(x, y, 0), v(x, y, 6)], true);
  for (const z of [3, 6]) for (const axis of [0, 3, 6]) {
    line(`guide:x:${z}:${axis}`, [v(0, axis, z), v(6, axis, z)], true);
    line(`guide:y:${z}:${axis}`, [v(axis, 0, z), v(axis, 6, z)], true);
  }
  for (const [side, x] of [['west', 1.5], ['east', 4.5]] as const) {
    const metadata = { taskId: `seed-${side}`, partId: `seed-kit-${side}`, schematicToken: true };
    seeds.set(side, [
      bar(`part:seed-kit-${side}:base`, v(x - 0.55, 0.3, 0.12), v(x + 0.55, 0.3, 0.12), 0.22, colors.seed, metadata),
      bar(`part:seed-kit-${side}:post`, v(x, 0.3, 0.12), v(x, 0.3, 1.0), 0.13, colors.seed, metadata),
      bar(`part:seed-kit-${side}:brace`, v(x - 0.5, 0.3, 0.12), v(x, 0.3, 0.9), 0.07, colors.brace, metadata),
    ]);
  }
  for (const bay of bays) {
    const x = bay.x * 3, y = bay.y * 3 + 1.5, z = bay.storey * 3;
    const meta = (taskId: string, partId: string) => ({ bayId: bay.id, taskId, partId, schematicToken: true });
    const member = bar(`part:${bay.memberPartId}`, v(x + 0.18, y, z), v(x + 2.82, y, z), 0.19,
      colors.complete, meta(`place-${bay.id}`, bay.memberPartId));
    const brace = bar(`part:part-brace-${bay.id}`, v(x + 0.18, y, z - 2.85), v(x + 2.82, y, z - 0.16), 0.07,
      colors.brace, meta(`brace-${bay.id}`, `part-brace-${bay.id}`));
    const rail = bar(`part:part-rail-${bay.id}`, v(x + 0.30, y - 0.26, z - 2.85), v(x + 0.30, y - 0.26, z), 0.08,
      colors.rail, meta(`rail-${bay.id}`, `part-rail-${bay.id}`));
    const markerGeometry = new THREE.OctahedronGeometry(0.16);
    geometries.add(markerGeometry);
    const operation = new THREE.Mesh(markerGeometry, material(colors.active));
    operation.name = `workflow:${bay.id}`;
    operation.position.set(x + 1.5, y, z + 0.3);
    operation.userData = { bayId: bay.id, schematicToken: true, mechanicalStatus: 'unverified' };
    group.add(operation);
    const reservation = line(`reservation:lift-${bay.id}`, [v(x + 0.6, y, z + 0.1),
      v(x + 1.5, y, z + 1.1), v(x + 2.4, y, z + 0.1)], false);
    reservation.userData = { leaseId: `lift-${bay.id}`, reservationToken: true, mechanicalStatus: 'unverified' };
    visuals.set(bay.id, { member, brace, rail, operation, reservation });
  }

  function reveal(mesh: THREE.Mesh, state: PreviewTaskState, baseColor: number): void {
    mesh.visible = state.phase === 'active' || state.phase === 'complete';
    // Graphical reveal along the object's axis, deliberately not a motion trajectory.
    const fraction = state.phase === 'complete' ? 1 : Math.max(0.03, state.progress);
    mesh.scale.y = fraction;
    const start = new THREE.Vector3().fromArray(mesh.userData.start);
    const end = new THREE.Vector3().fromArray(mesh.userData.end);
    mesh.position.copy(start).lerp(end, fraction / 2);
    (mesh.material as THREE.MeshStandardMaterial).color.setHex(state.phase === 'active' ? colors.active : baseColor);
    mesh.userData.phase = state.phase;
    mesh.userData.progress = state.progress;
  }
  let current: FramePreviewSnapshot;
  function setTime(timeS: number): FramePreviewSnapshot {
    current = sampler.sample(timeS);
    const tasks = new Map(current.tasks.map(task => [task.taskId, task]));
    for (const [side, meshes] of seeds) {
      const state = tasks.get(`seed-${side}`) ?? taskState(`seed-${side}`, undefined, current.timeS);
      for (const mesh of meshes) reveal(mesh, state, colors.seed);
    }
    for (const bay of current.bays) {
      const visual = visuals.get(bay.bayId)!;
      reveal(visual.member, bay.member, colors.complete);
      reveal(visual.brace, bay.brace, colors.brace);
      reveal(visual.rail, bay.rail, colors.rail);
      visual.reservation.visible = bay.liftReservationHeld;
      visual.operation.visible = bay.operation.phase === 'active';
      visual.operation.rotation.set(0, 0, current.timeS * 0.012);
      (visual.operation.material as THREE.MeshStandardMaterial).color.setHex(
        bay.operation.taskId.startsWith('recover-') ? colors.recovery : colors.active);
      visual.operation.userData.taskId = bay.operation.taskId;
      visual.member.userData.releasedInPlan = bay.releasedInPlan;
    }
    group.userData.timeS = current.timeS;
    return current;
  }
  setTime(0);
  return { group, durationS: sampler.durationS, label: FRAME_PREVIEW_LABEL,
    description: FRAME_PREVIEW_DESCRIPTION, setTime, snapshot: () => current,
    dispose() {
      group.removeFromParent();
      for (const geometry of geometries) geometry.dispose();
      for (const ownedMaterial of materials) ownedMaterial.dispose();
      group.clear();
    } };
}
