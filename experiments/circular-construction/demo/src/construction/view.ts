import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { solvePlantedClimb, type PlannedGrip } from './plantedGrip';
import { entryDoorHinge, entryDoorMatrix, entryDoorOpenness, type PartHinge } from './partArticulation';
import type { ConstructionPlan, ConstructionSnapshot, PartState, RobotState } from './types';

export type CameraMode = 'site' | 'carrier' | 'assembler' | 'part';
interface Batch { mesh: THREE.InstancedMesh; local: THREE.Matrix4; hinge?: PartHinge; ids: string[]; activeIds: string[]; previous: string[] }
interface FleetSource { mesh: THREE.Mesh; root: THREE.Object3D; robotId: string }
interface FleetBatch { mesh: THREE.InstancedMesh; sources: FleetSource[]; ids: string[] }
interface RobotVisual { root: THREE.Object3D; pivots: Map<string, THREE.Object3D>; rests: Map<string, THREE.Quaternion> }
export interface RobotGeometryReport {
  mode: 'planned-planted-ik' | 'planned-ground-travel' | 'missing-traverse-targets' | 'planned-hold';
  plantedCount: number;
  unreachable: string[];
  missingBindings: string[];
  contacts: { limb: string; planted: boolean; saddleIndex: number; target: number[]; actual: number[]; errorM: number }[];
  note: string;
}
export interface ConstructionView {
  update(snapshot: ConstructionSnapshot, elapsed: number): void;
  camera(mode: CameraMode): void;
  select(id: string | null): void;
  onSelect: ((id: string) => void) | null;
  onSubject: ((id: string) => void) | null;
  readonly renderer: THREE.WebGLRenderer;
  readonly scene: THREE.Scene;
  readonly cameraObject: THREE.PerspectiveCamera;
  robotGeometry(id: string): RobotGeometryReport | undefined;
  dispose(): void;
}

const dummy = new THREE.Object3D();
const temporaryMatrix = new THREE.Matrix4();

/** Every visible material pose comes from the construction snapshot. No independent growth clock. */
export async function createConstructionView(container: HTMLElement, plan: ConstructionPlan): Promise<ConstructionView> {
  const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false, powerPreference: 'high-performance' });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.7));
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.12;
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  renderer.domElement.setAttribute('aria-label', 'Continuous three-dimensional planned construction scene');
  container.append(renderer.domElement);
  const scene = new THREE.Scene();
  scene.background = new THREE.Color('#cbdde4');
  scene.fog = new THREE.Fog('#cbdde4', 170, 350);
  const camera = new THREE.PerspectiveCamera(43, 1, 0.1, 600);
  camera.position.set(39, 27, 39);
  const controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.dampingFactor = .08;
  controls.minDistance = 2;
  controls.maxDistance = 175;
  controls.maxPolarAngle = Math.PI * .485;
  controls.target.set(0, 3, 0);
  scene.add(new THREE.HemisphereLight('#d5e6ef', '#8b8066', 2.1));
  const sunlight = new THREE.DirectionalLight('#fff1dc', 3.25);
  sunlight.position.set(-35, 65, 28);
  sunlight.castShadow = true;
  sunlight.shadow.mapSize.set(2048, 2048);
  Object.assign(sunlight.shadow.camera, { left: -46, right: 46, top: 77, bottom: -38, near: .5, far: 180 });
  sunlight.shadow.bias = -.0004;
  sunlight.shadow.normalBias = .035;
  scene.add(sunlight, sunlight.target);
  const fill = new THREE.DirectionalLight('#e4eef5', .65);
  fill.position.set(30, 25, -40);
  scene.add(fill);
  createTerrain(scene);

  // Asset failures propagate to the visible error panel. Building/robot geometry has no substitute.
  const loader = new GLTFLoader();
  const [kit, fleet] = await Promise.all([
    loader.loadAsync('/assets/construction-kit.glb'),
    loader.loadAsync('/assets/construction-robots.glb'),
  ]);
  const batches: Batch[] = [];
  const byAsset = new Map<string, string[]>();
  for (const part of plan.parts) {
    const ids = byAsset.get(part.asset) ?? [];
    ids.push(part.id); byAsset.set(part.asset, ids);
  }
  const instanceLookup = new Map<THREE.Object3D, string[]>();
  const bounds = new Map<string, THREE.Box3>();
  for (const [asset, ids] of byAsset) {
    const template = kit.scene.getObjectByName(asset);
    if (!template) throw new Error(`Blender construction kit is missing named root: ${asset}`);
    template.updateWorldMatrix(true, true);
    const inverse = template.matrixWorld.clone().invert();
    bounds.set(asset, new THREE.Box3().setFromObject(template));
    template.traverse((node) => {
      if (!(node instanceof THREE.Mesh)) return;
      const local = inverse.clone().multiply(node.matrixWorld);
      const mesh = new THREE.InstancedMesh(node.geometry, node.material, ids.length);
      mesh.name = `${asset}:${node.name}`;
      mesh.instanceMatrix.setUsage(THREE.DynamicDrawUsage);
      mesh.frustumCulled = false;
      mesh.castShadow = true; mesh.receiveShadow = true;
      mesh.count = 0; mesh.visible = false;
      const activeIds: string[] = [];
      scene.add(mesh);
      batches.push({ mesh, local, hinge: entryDoorHinge(node, inverse), ids, activeIds, previous: [] });
      instanceLookup.set(mesh, activeIds);
    });
  }
  const robots = new Map<string, RobotVisual>();
  const fleetSources = new Map<string, FleetSource[]>();
  for (const definition of plan.robots) {
    const template = fleet.scene.getObjectByName(definition.kind);
    if (!template) throw new Error(`Blender fleet is missing named root: ${definition.kind}`);
    const root = template.clone(true);
    root.name = definition.id;
    root.visible = false;
    const pivots = new Map<string, THREE.Object3D>();
    const rests = new Map<string, THREE.Quaternion>();
    root.traverse((node) => {
      const binding = node.name.replace(/(?:\.\d+|\d{3}|_\d+)$/, '');
      pivots.set(binding, node); rests.set(binding, node.quaternion.clone());
      if (node instanceof THREE.Mesh) {
        const materials = Array.isArray(node.material) ? node.material : [node.material];
        const key = `${node.geometry.uuid}:${materials.map((m) => m.uuid).join(',')}`;
        const sources = fleetSources.get(key) ?? [];
        sources.push({ mesh: node, root, robotId: definition.id }); fleetSources.set(key, sources);
        // Keep the exact mesh and its bounding geometry in the articulated hierarchy.
        // Drawing and picking use the fleet instances instead of these source meshes.
        node.visible = false; node.layers.disable(0);
      }
      node.userData.robotId = definition.id;
    });
    scene.add(root); robots.set(definition.id, { root, pivots, rests });
  }
  const fleetBatches: FleetBatch[] = [];
  for (const sources of fleetSources.values()) {
    const source = sources[0].mesh;
    const mesh = new THREE.InstancedMesh(source.geometry, source.material, sources.length);
    mesh.name = `fleet:${source.name}`;
    mesh.instanceMatrix.setUsage(THREE.DynamicDrawUsage);
    mesh.castShadow = true; mesh.receiveShadow = true;
    mesh.frustumCulled = false; mesh.count = 0; mesh.visible = false;
    const ids: string[] = [];
    scene.add(mesh); instanceLookup.set(mesh, ids);
    fleetBatches.push({ mesh, sources, ids });
  }
  const marker = new THREE.Box3Helper(new THREE.Box3(), new THREE.Color('#e6a04d'));
  marker.material = new THREE.LineBasicMaterial({ color: '#e6a04d', transparent: true, opacity: .8, depthTest: false });
  marker.visible = false;
  marker.renderOrder = 10;
  scene.add(marker);
  const definitionById = new Map(plan.parts.map((p) => [p.id, p]));
  const geometryReports = new Map<string, RobotGeometryReport>();
  let snapshot: ConstructionSnapshot | null = null;
  let selected: string | null = null;
  let mode: CameraMode = 'site';
  let manualCamera = false;
  let initialized = false;
  let previousTime = 0;
  let latestHeight = 0;
  const desiredTarget = new THREE.Vector3();
  const desiredCamera = new THREE.Vector3();
  controls.addEventListener('start', () => { manualCamera = true; });
  let pointerStart = new THREE.Vector2();
  const raycaster = new THREE.Raycaster();
  const pointer = new THREE.Vector2();
  renderer.domElement.addEventListener('pointerdown', (event) => { pointerStart.set(event.clientX, event.clientY); });
  const selectFromPointer = (event: PointerEvent) => {
    if (pointerStart.distanceTo(new THREE.Vector2(event.clientX, event.clientY)) > 5) return;
    const rect = renderer.domElement.getBoundingClientRect();
    pointer.set((event.clientX - rect.left) / rect.width * 2 - 1, -(event.clientY - rect.top) / rect.height * 2 + 1);
    raycaster.setFromCamera(pointer, camera);
    const hits = raycaster.intersectObjects(scene.children, true);
    for (const hit of hits) {
      if (!hit.object.visible) continue;
      if (typeof hit.object.userData.robotId === 'string') { api.onSelect?.(hit.object.userData.robotId); return; }
      if (hit.instanceId !== undefined) {
        const id = instanceLookup.get(hit.object)?.[hit.instanceId];
        if (id) { api.onSelect?.(id); return; }
      }
    }
  };
  renderer.domElement.addEventListener('pointerup', selectFromPointer);
  const resize = () => {
    const width = container.clientWidth, height = container.clientHeight;
    renderer.setSize(width, height);
    camera.aspect = width / Math.max(1, height); camera.updateProjectionMatrix();
  };
  const observer = new ResizeObserver(resize); observer.observe(container); resize();

  function chooseSubject(): RobotState | PartState | undefined {
    if (!snapshot) return;
    const selectedRobot = snapshot.robots.find((r) => r.id === selected && r.visible);
    const selectedPart = snapshot.parts.find((p) => p.id === selected && p.visible);
    if (mode === 'part') {
      if (selectedPart) return selectedPart;
      if (selectedRobot?.payloadId) return snapshot.parts.find((p) => p.id === selectedRobot.payloadId);
      return snapshot.parts.find((p) => p.visible && ['handoff', 'installing', 'carried', 'recovering', 'packing', 'outgoing'].includes(p.status));
    }
    const kind = mode === 'assembler' ? 'assembler' : 'carrier';
    if (selectedRobot?.kind === kind) return selectedRobot;
    return snapshot.robots.find((r) => r.visible && r.kind === kind && r.payloadId)
      ?? snapshot.robots.find((r) => r.visible && r.kind === kind);
  }
  const api: ConstructionView = {
    renderer, scene, cameraObject: camera, onSelect: null, onSubject: null,
    robotGeometry(id) { return geometryReports.get(id); },
    camera(next) { mode = next; manualCamera = false; },
    select(id) { selected = id; manualCamera = false; },
    update(next, elapsed) {
      snapshot = next;
      const partById = new Map(next.parts.map((p) => [p.id, p]));
      latestHeight = 0;
      for (const part of next.parts) if (part.visible && part.status === 'installed') latestHeight = Math.max(latestHeight, part.pose.position[1]);
      for (const batch of batches) {
        let changed = false, count = 0;
        for (const id of batch.ids) {
          const part = partById.get(id);
          if (!part?.visible) continue;
          const slot = count++;
          batch.activeIds[slot] = id;
          // Include the persistent ID: removing an earlier part compacts later parts
          // into new slots, even when their cached poses have not changed.
          const key = `${id}|${part.pose.position}|${part.pose.rotation}|${batch.hinge ? entryDoorOpenness(part) : ''}`;
          if (batch.previous[slot] === key) continue;
          batch.previous[slot] = key; changed = true;
          setPose(dummy, part.pose);
          dummy.scale.fromArray(definitionById.get(id)?.assetScale ?? [1, 1, 1]);
          dummy.updateMatrix();
          const local = batch.hinge ? entryDoorMatrix(batch.hinge, entryDoorOpenness(part)) : batch.local;
          temporaryMatrix.multiplyMatrices(dummy.matrix, local);
          batch.mesh.setMatrixAt(slot, temporaryMatrix);
        }
        const countChanged = batch.mesh.count !== count;
        batch.activeIds.length = count; batch.previous.length = count;
        batch.mesh.count = count; batch.mesh.visible = count > 0;
        if (changed) batch.mesh.instanceMatrix.needsUpdate = true;
        if (changed || countChanged) { batch.mesh.boundingSphere = null; batch.mesh.boundingBox = null; }
      }
      for (const state of next.robots) {
        const visual = robots.get(state.id);
        if (!visual) continue;
        visual.root.visible = state.visible;
        if (!state.visible) continue;
        setPose(visual.root, state.pose);
        geometryReports.set(state.id, articulateRobot(visual, state));
        // Hidden drawing meshes still provide the live articulated world matrices.
        visual.root.updateWorldMatrix(true, true);
      }
      for (const batch of fleetBatches) {
        let count = 0;
        for (const source of batch.sources) {
          if (!source.root.visible) continue;
          batch.mesh.setMatrixAt(count, source.mesh.matrixWorld);
          batch.ids[count] = source.robotId; count++;
        }
        batch.ids.length = count;
        batch.mesh.count = count; batch.mesh.visible = count > 0;
        if (count) batch.mesh.instanceMatrix.needsUpdate = true;
        batch.mesh.boundingSphere = null; batch.mesh.boundingBox = null;
      }
      const pickedPart = selected ? partById.get(selected) : undefined;
      const pickedRobot = next.robots.find((r) => r.id === selected);
      const selectedGeometry = selected ? geometryReports.get(selected) : undefined;
      (marker.material as THREE.LineBasicMaterial).color.set(selectedGeometry?.unreachable.length || selectedGeometry?.missingBindings.length ? '#bf4e31' : '#e6a04d');
      if (pickedPart?.visible) {
        const definition = definitionById.get(pickedPart.id)!;
        const box = bounds.get(definition.asset);
        if (box) {
          setPose(dummy, pickedPart.pose); dummy.scale.fromArray(definition.assetScale ?? [1, 1, 1]); dummy.updateMatrix();
          marker.box.copy(box).applyMatrix4(dummy.matrix).expandByScalar(.08);
          marker.visible = true;
        }
      } else if (pickedRobot?.visible) {
        marker.box.setFromObject(robots.get(pickedRobot.id)!.root).expandByScalar(.1); marker.visible = true;
      } else marker.visible = false;
      if (!manualCamera) {
        const subject = mode === 'site' ? undefined : chooseSubject();
        if (subject && !selected) api.onSubject?.(subject.id);
        if (subject) {
          desiredTarget.fromArray(subject.pose.position).add(new THREE.Vector3(0, .25, 0));
          const isPart = 'status' in subject;
          const distance = isPart ? 6.8 : 7.5;
          const yaw = subject.pose.rotation[1];
          desiredCamera.copy(desiredTarget).add(new THREE.Vector3(Math.cos(yaw) * distance, distance * .55, Math.sin(yaw) * distance + 5));
        } else {
          const height = Math.max(12, latestHeight + 3);
          // Leave the tower base and recovery fleet above the playback deck.
          // A tall building fitted to the full canvas would hide its ground work.
          const verticalRoom = Math.max(.42, (container.clientHeight - 230) / container.clientHeight);
          const dist = Math.max(62, height * 1.42 / verticalRoom);
          desiredTarget.set(-5, height * .3, -3);
          desiredCamera.set(dist * .78, height * .68 + 17, dist * .81);
        }
        const jump = !initialized || Math.abs(next.time - previousTime) > 1800;
        const blend = jump ? 1 : 1 - Math.exp(-Math.min(elapsed, .12) * 4);
        controls.target.lerp(desiredTarget, blend); camera.position.lerp(desiredCamera, blend);
      }
      initialized = true; previousTime = next.time;
      controls.update(); renderer.render(scene, camera);
    },
    dispose() { observer.disconnect(); controls.dispose(); for (const batch of fleetBatches) batch.mesh.dispose(); renderer.dispose(); renderer.domElement.remove(); },
  };
  return api;
}

function setPose(object: THREE.Object3D, pose: { position: [number, number, number]; rotation: [number, number, number] }) {
  object.position.fromArray(pose.position); object.rotation.set(...pose.rotation, 'XYZ');
}

function articulateRobot(visual: RobotVisual, state: RobotState): RobotGeometryReport {
  const nearShaft = Math.abs(state.pose.position[2] + 6.93) < .015 && Math.abs(state.pose.rotation[1] + Math.PI / 2) < .03;
  const usePlanted = (state.kind === 'carrier' || state.kind === 'assembler') && nearShaft && (state.locomotion === 'vertical-climb' || state.locomotion === 'hold') && state.pose.position[1] >= .72;
  const report: RobotGeometryReport = {
    mode: usePlanted ? 'planned-planted-ik' : state.locomotion === 'ground-travel' ? 'planned-ground-travel' : state.locomotion === 'frame-traverse' ? 'missing-traverse-targets' : 'planned-hold',
    plantedCount: 0, unreachable: [], missingBindings: [], contacts: [],
    note: usePlanted ? 'Three retained jaw throats stay at fixed rail gaps; one transfers. Geometric IK, forces unverified.' : state.locomotion === 'frame-traverse' ? 'Horizontal frame travel has no qualified grip targets; transport stance only.' : 'Authored transport or waiting pose; no contact dynamics claim.',
  };
  // Reset every authored limb from its export rest pose before applying a new absolute IK solution.
  for (const limb of ['fl', 'fr', 'rl', 'rr']) {
    for (const joint of ['hip', 'knee', 'wrist']) {
      const name = `limb_${limb}_${joint}`, node = visual.pivots.get(name), rest = visual.rests.get(name);
      if (node && rest) node.quaternion.copy(rest);
    }
    for (const [jaw, sign] of [['a', -1], ['b', 1]] as [string, number][]) {
      const node = visual.pivots.get(`limb_${limb}_jaw_${jaw}`);
      if (node) node.position.z = sign * .15;
    }
    const wheel = visual.pivots.get(`wheel_${limb}`);
    if (wheel) wheel.rotation.x = state.locomotion === 'ground-travel' ? state.gait : 0;
  }
  if (usePlanted) {
    const solution = solvePlantedClimb(state.pose.position[1]);
    for (const grip of solution.grips) applyGrip(visual, grip, report);
    visual.root.updateWorldMatrix(true, true);
    for (const grip of solution.grips) {
      const throat = visual.pivots.get(`limb_${grip.limb}_grip_contact`);
      if (!throat) { report.missingBindings.push(`limb_${grip.limb}_grip_contact`); continue; }
      const target = new THREE.Vector3(grip.contactX, grip.worldHeight - state.pose.position[1], grip.lateral).applyMatrix4(visual.root.matrixWorld);
      const actual = throat.getWorldPosition(new THREE.Vector3());
      const errorM = target.distanceTo(actual);
      report.contacts.push({ limb: grip.limb, planted: grip.planted, saddleIndex: grip.anchorIndex, target: target.toArray(), actual: actual.toArray(), errorM });
      if (grip.planted && grip.reachable && errorM < .005) report.plantedCount++;
      if (errorM >= .005) report.unreachable.push(`${grip.limb}: exported throat misses target by ${errorM.toFixed(3)} m`);
    }
    if (state.pose.position[1] < 1.44) report.note = 'Ground-to-rail attachment transition; lower gap availability and support remain planned.';
  }
  const shoulder = visual.pivots.get('tool_shoulder');
  const elbow = visual.pivots.get('tool_elbow');
  const wrist = visual.pivots.get('tool_wrist');
  const handling = /install|receiv|capture|connect|verify|handoff|seat|place/i.test(state.action);
  if (shoulder) shoulder.rotation.z = handling ? -.18 + Math.sin(state.progress * Math.PI) * .28 : -.25;
  if (elbow) elbow.rotation.z = handling ? .25 + Math.sin(state.progress * Math.PI) * .4 : .65;
  if (wrist) wrist.rotation.z = handling ? -.15 : -.25;
  visual.root.userData.plannedGripGeometry = report;
  return report;
}

function applyGrip(visual: RobotVisual, grip: PlannedGrip, report: RobotGeometryReport) {
  if (!grip.reachable) { report.unreachable.push(`${grip.limb}: wrist target outside the two-link workspace`); return; }
  // These angles already include the rest-angle geometry. Do not multiply export q0 a second time.
  for (const [joint, angle] of [['hip', grip.shoulder], ['knee', grip.elbow], ['wrist', grip.wrist]] as [string, number][]) {
    const node = visual.pivots.get(`limb_${grip.limb}_${joint}`);
    if (node) node.rotation.set(0, 0, angle);
    else report.missingBindings.push(`limb_${grip.limb}_${joint}`);
  }
  for (const [jaw, sign] of [['a', -1], ['b', 1]] as [string, number][]) {
    const node = visual.pivots.get(`limb_${grip.limb}_jaw_${jaw}`);
    if (node) node.position.z = sign * grip.jawCenter;
    else report.missingBindings.push(`limb_${grip.limb}_jaw_${jaw}`);
  }
}

function createTerrain(scene: THREE.Scene) {
  const canvas = document.createElement('canvas'); canvas.width = 512; canvas.height = 512;
  const context = canvas.getContext('2d')!;
  context.fillStyle = '#c0b298'; context.fillRect(0, 0, 512, 512);
  let seed = 5913;
  const random = () => { seed = (seed * 1664525 + 1013904223) >>> 0; return seed / 4294967296; };
  for (let i = 0; i < 55000; i++) {
    const shade = Math.floor(115 + random() * 95);
    context.fillStyle = `rgba(${shade},${shade - 10},${shade - 30},.12)`;
    context.fillRect(random() * 512, random() * 512, 1 + random() * 2, 1 + random() * 2);
  }
  const texture = new THREE.CanvasTexture(canvas); texture.wrapS = texture.wrapT = THREE.RepeatWrapping; texture.repeat.set(12, 12); texture.colorSpace = THREE.SRGBColorSpace;
  const terrain = new THREE.Mesh(new THREE.PlaneGeometry(220, 220), new THREE.MeshStandardMaterial({ map: texture, roughness: 1, color: '#e1d7bf' }));
  terrain.rotation.x = -Math.PI / 2; terrain.position.y = -.07; terrain.receiveShadow = true; terrain.name = 'bare-earth'; scene.add(terrain);
}
