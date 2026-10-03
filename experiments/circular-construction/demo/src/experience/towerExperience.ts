import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';
import type { BodyBinding, SimulationTrace, TowerExperience, TowerManifest, TraceFrame } from './types';
import './towerExperience.css';

function element<K extends keyof HTMLElementTagNameMap>(tag: K, className = '', text = ''): HTMLElementTagNameMap[K] {
  const node = document.createElement(tag);
  node.className = className;
  node.textContent = text;
  return node;
}

/** Reject malformed traces before applying any model motion. */
export function validateTrace(trace: SimulationTrace): string[] {
  const errors: string[] = [];
  if (trace.schemaVersion !== 1 || trace.coordinates !== 'gltf-y-up') errors.push('Unsupported trace schema or coordinate frame.');
  if (trace.units?.length !== 'm' || trace.units?.time !== 's' || trace.units?.force !== 'N') errors.push('Trace must use metres, seconds, and newtons.');
  if (!trace.provenance?.engine || !trace.provenance?.coordinateConversion || !trace.provenance?.description || !Array.isArray(trace.provenance?.limitations)) errors.push('Trace provenance, limitations, and coordinate conversion are required.');
  if (!Array.isArray(trace.phases)) errors.push('Trace phase metadata is required.');
  else for (const phase of trace.phases) {
    if (!phase.id || !phase.label || !Number.isFinite(phase.start) || !Number.isFinite(phase.end) || phase.end < phase.start) errors.push('Invalid trace phase metadata.');
  }
  const boundNodes = new Set<string>();
  for (const binding of trace.bindings ?? []) {
    const key = `${binding.assetId}/${binding.node}`;
    if (!binding.body || !binding.assetId || !binding.node || boundNodes.has(key)) errors.push(`Invalid or duplicate visual binding: ${key}.`);
    boundNodes.add(key);
    if (binding.positionOffset && (binding.positionOffset.length !== 3 || !binding.positionOffset.every(Number.isFinite))) errors.push(`Invalid position offset: ${key}.`);
    if (binding.quaternionOffset && (binding.quaternionOffset.length !== 4 || !binding.quaternionOffset.every(Number.isFinite) || Math.abs(Math.hypot(...binding.quaternionOffset) - 1) > .01)) errors.push(`Invalid quaternion offset: ${key}.`);
  }
  if (!Array.isArray(trace.frames) || trace.frames.length < 2) return [...errors, 'At least two simulation frames are required for playback.'];
  let previous = -Infinity;
  for (const frame of trace.frames) {
    if (!Number.isFinite(frame.time) || frame.time <= previous) { errors.push('Frame times must increase strictly.'); break; }
    previous = frame.time;
    if (frame.metrics && !Object.values(frame.metrics).every(Number.isFinite)) errors.push('Recorded metrics must be finite.');
    if (frame.contacts && frame.contacts.some(contact => !contact.bodyA || !contact.bodyB || !Number.isFinite(contact.normalForce) || contact.normalForce < 0)) errors.push('Invalid recorded contact evidence.');
    for (const binding of trace.bindings ?? []) {
      const pose = frame.bodies?.[binding.body];
      if (!pose || pose.position?.length !== 3 || pose.quaternion?.length !== 4 || ![...pose.position, ...pose.quaternion].every(Number.isFinite)) {
        errors.push(`Missing or invalid rigid-body pose: ${binding.body}.`); break;
      }
      const norm = Math.hypot(...pose.quaternion);
      if (Math.abs(norm - 1) > 0.01) { errors.push(`Non-unit quaternion: ${binding.body}.`); break; }
    }
    if (errors.length) break;
  }
  if (!trace.bindings?.length) errors.push('Trace has no visual body bindings.');
  return errors;
}

export function createTowerExperience(container: HTMLElement, manifest: TowerManifest, suppliedTrace?: SimulationTrace | null): TowerExperience {
  const messages: string[] = [];
  const staticDesign = manifest.mode === 'static-design';
  let trace = staticDesign ? null : suppliedTrace ?? null;
  if (trace) { const errors = validateTrace(trace); messages.push(...errors); if (errors.length) trace = null; }
  const presentation = manifest.presentation;
  const initialView = manifest.cameras?.initialView ?? 'tower';
  const initialCamera = manifest.cameras?.[initialView];
  const host = element('div', 'tower-experience');
  container.append(host);
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0xc8d2d5);
  scene.fog = new THREE.Fog(0xc8d2d5, 140, 410);
  const camera = new THREE.PerspectiveCamera(43, 1, 0.03, 700);
  const towerHeight = manifest.storeys * manifest.storeyHeight;
  const activeHeight = manifest.activeLevel * manifest.storeyHeight;
  camera.position.fromArray(initialCamera?.position ?? [110, 80, 126]);
  const renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: 'high-performance' });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.1;
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  host.append(renderer.domElement);
  const controls = new OrbitControls(camera, renderer.domElement);
  controls.target.fromArray(initialCamera?.target ?? [0, towerHeight * .46, 0]);
  controls.enableDamping = true;
  controls.dampingFactor = .08;
  controls.minDistance = 1.3;
  controls.maxDistance = 250;
  controls.maxPolarAngle = Math.PI * .91;
  const pmrem = new THREE.PMREMGenerator(renderer);
  const environment = new RoomEnvironment();
  const environmentTarget = pmrem.fromScene(environment, .04);
  scene.environment = environmentTarget.texture;
  scene.environmentIntensity = .45;
  environment.dispose();
  pmrem.dispose();
  scene.add(new THREE.HemisphereLight(0xdae9f3, 0x716753, 1.8));
  const sun = new THREE.DirectionalLight(0xffe3bb, 3.2);
  sun.position.set(-50, 108, 65);
  sun.target.position.set(0, activeHeight * .6, 0);
  sun.castShadow = true;
  sun.shadow.mapSize.set(2048, 2048);
  sun.shadow.camera.left = -66; sun.shadow.camera.right = 66;
  sun.shadow.camera.top = 66; sun.shadow.camera.bottom = -66;
  sun.shadow.camera.near = 1; sun.shadow.camera.far = 250;
  sun.shadow.normalBias = .035;
  sun.shadow.bias = -.00015;
  scene.add(sun, sun.target);

  const header = element('div', 'te-header');
  const title = element('div', 'te-title');
  title.append(element('div', 'te-kicker', presentation?.kicker ?? `Construction / Workcell ${manifest.activeLevel}`), element('h2', '', manifest.title ?? 'The growing tower'), element('div', 'te-subtitle', presentation?.subtitle ?? `${manifest.storeys} storeys · ${towerHeight.toFixed(1)} m · Active floor ${manifest.activeLevel}`));
  const badge = element('div', 'te-badge', staticDesign ? 'Planned design · authored Blender geometry' : trace ? `${trace.provenance.engine} dynamics · recorded trajectory` : 'Blender model · still preview');
  title.append(badge);
  const views = element('div', 'te-views');
  const overviewButton = element('button', '', presentation?.overviewLabel ?? 'Whole tower');
  const workcellButton = element('button', '', presentation?.workcellLabel ?? 'Active floor ↗');
  views.append(overviewButton, workcellButton);
  header.append(title, views);
  host.append(header);
  const panel = element('div', 'te-panel');
  panel.append(element('div', 'te-kicker', staticDesign ? 'Inspect the design' : 'Inspect the assembly'));
  const inspection = element('select');
  inspection.setAttribute('aria-label', 'Inspect modeled object');
  const emptyOption = element('option', '', presentation?.inspectionPlaceholder ?? 'Select beam, robot or hoist'); emptyOption.value = ''; inspection.append(emptyOption);
  const detail = element('p', 'te-detail', presentation?.inspectionIntroduction ?? 'Move from the whole site into the working floor. Select a modeled assembly to inspect its geometry.');
  panel.append(inspection, detail);
  const layerList = element('div', 'te-layer-list');
  if (manifest.layers?.length) panel.append(element('label', '', presentation?.layerLabel ?? 'Construction layers'), layerList);
  const stats = element('div', 'te-stats');
  const contactStat = element('div', 'te-stat', 'Recorded contacts');
  const contactValue = element('strong', '', '—'); contactStat.append(contactValue);
  const forceStat = element('div', 'te-stat', 'Peak contact force');
  const forceValue = element('strong', '', '—'); forceStat.append(forceValue);
  const metricValues = (presentation?.metrics ?? []).map(metric => {
    const stat = element('div', 'te-stat', metric.label);
    const value = element('strong', '', '—'); stat.append(value); stats.append(stat);
    return { ...metric, value };
  });
  if (!metricValues.length) stats.append(contactStat, forceStat);
  if (presentation) {
    if (!staticDesign) panel.insertBefore(stats, detail);
    if (presentation.qualification) panel.insertBefore(element('p', 'te-warning', presentation.qualification), detail);
  } else if (!staticDesign) panel.append(stats);
  if (manifest.structural && !staticDesign) {
    const structural = manifest.structural;
    const structureSection = element('div', 'te-structure');
    structureSection.append(element('div', 'te-kicker', `${structural.engine} / 12-storey analysis`));
    const structureStats = element('div', 'te-stats');
    const roof = element('div', 'te-stat', 'Roof displacement');
    roof.append(element('strong', '', `${(structural.stage12RoofDisplacementM * 1000).toFixed(1)} mm`));
    const seats = element('div', 'te-stat', 'Final seats · left / right');
    seats.append(element('strong', '', `${structural.finalSeatReactionsN.map(force => (force / 1000).toFixed(2)).join(' / ')} kN`));
    structureStats.append(roof, seats); structureSection.append(structureStats);
    structureSection.append(element('p', 'te-structure-note', `Missing braces: roof motion +${((structural.braceSensitivity.roofDisplacementRatio - 1) * 100).toFixed(1)}%`));
    panel.append(structureSection);
  }
  const evidence = element('details');
  evidence.append(element('summary', '', staticDesign ? 'Model & design notes' : 'Model & simulation evidence'));
  const evidenceText = element('p', 'te-evidence-text'); evidence.append(evidenceText); panel.append(evidence);
  panel.append(element('p', 'te-instructions', 'Drag to orbit · Scroll to approach · Click an assembly'));
  if (manifest.source?.blender) { const download = element('a', 'te-download', 'Open editable Blender source ↗'); download.href = manifest.source.blender; download.target = '_blank'; download.rel = 'noopener'; panel.append(download); }
  host.append(panel);
  const timeline = element('div', 'te-timeline');
  const playbar = element('div', 'te-playbar');
  const play = element('button', '', trace ? '▶ Play' : 'Still model'); play.disabled = !trace;
  const slider = element('input'); slider.type = 'range'; slider.min = '0'; slider.step = '.01'; slider.setAttribute('aria-label', 'Simulation time'); slider.disabled = !trace;
  const timeDisplay = element('div', 'te-time', 'No motion trace');
  playbar.append(play, slider, timeDisplay);
  if (presentation) {
    const speed = element('select'); speed.setAttribute('aria-label', 'Playback speed');
    for (const multiplier of [1, 2, 4, 8]) {
      const option = element('option', '', `${multiplier}×`); option.value = String(multiplier); speed.append(option);
    }
    speed.addEventListener('change', () => { playbackSpeed = Number(speed.value); });
    playbar.append(speed);
  }
  timeline.append(playbar);
  const phases = element('div', 'te-phases');
  const phaseDescription = element('div', 'te-phase-description', trace ? 'Recorded dynamics, interpolated between simulator samples.' : 'The model is available for inspection. Playback requires a validated dynamics trace.');
  timeline.append(phases, phaseDescription);
  if (!staticDesign) host.append(timeline);
  const status = element('div', 'te-status', 'Loading Blender models…'); status.setAttribute('role', 'status'); host.append(status);
  const roots = new Map<string, THREE.Object3D>();
  const plannedNodes = new Map<THREE.Object3D, boolean>();
  const plannedMaterials = new Map<THREE.Material, THREE.Material>();
  const authoredMaterials = new Map<THREE.Mesh, THREE.Material | THREE.Material[]>();
  let cameraView: 'tower' | 'workcell' = initialView;
  let tracking = initialView === 'workcell' && !!manifest.cameras?.trackingBody;
  let trackedY = trace?.frames[0]?.bodies[manifest.cameras?.trackingBody ?? '']?.position[1] ?? 0;
  const trackedStartY = trackedY;
  let cameraTrackedY = trackedY;
  let playbackSpeed = 1;
  const stageNote = element('div', 'te-stage-note'); stageNote.hidden = true; title.append(stageNote);
  const selectedNodes = new Map<string, { node: THREE.Object3D; description: string; cameraView?: 'tower' | 'workcell' }>();
  const bindings: { binding: BodyBinding; node: THREE.Object3D; depth: number }[] = [];
  let selected: THREE.Object3D | null = null;
  const highlight = new THREE.Box3Helper(new THREE.Box3(), 0xe4b56b); highlight.visible = false; scene.add(highlight);
  let playing = false, disposed = false, elapsed = trace?.frames[0]?.time ?? 0;
  const startTime = trace?.frames[0]?.time ?? 0;
  const endTime = trace?.frames.at(-1)?.time ?? 0;
  slider.min = String(startTime); slider.max = String(endTime);
  let transition: { position: THREE.Vector3; target: THREE.Vector3; fromPosition: THREE.Vector3; fromTarget: THREE.Vector3; start: number } | null = null;
  const phaseButtons = new Map<string, HTMLButtonElement>();

  function updateEvidence(): void {
    const structural = staticDesign ? undefined : manifest.structural;
    evidenceText.textContent = [manifest.source?.description ?? 'Editable Blender geometry loaded as glTF.', trace ? `${trace.provenance.engine}${trace.provenance.engineVersion ? ` ${trace.provenance.engineVersion}` : ''}\n${trace.provenance.description}\n${trace.provenance.coordinateConversion}\n${trace.provenance.limitations.join('\n')}` : staticDesign ? 'Authored geometry only. No construction, robotic installation or occupancy simulation is represented.' : 'No valid simulator trajectory is loaded; all assemblies remain in their authored pose.', structural ? `${structural.engine} structural evidence\n${structural.qualification}\n${structural.braceSensitivity.description}\n${structural.assumptions.join('\n')}${structural.source ? `\nSource: ${structural.source}` : ''}` : '', ...messages].filter(Boolean).join('\n\n');
  }
  function findNode(assetId: string, name: string): THREE.Object3D | null {
    const root = roots.get(assetId);
    if (!root) { messages.push(`Missing asset instance: ${assetId}.`); return null; }
    const matches: THREE.Object3D[] = [];
    root.traverse(node => { if (node.name === name) matches.push(node); });
    if (matches.length !== 1) { messages.push(`${assetId}/${name}: ${matches.length ? 'ambiguous node name' : 'node absent from model'}.`); return null; }
    return matches[0];
  }
  function moveCamera(position: THREE.Vector3, target: THREE.Vector3): void {
    transition = { position, target, fromPosition: camera.position.clone(), fromTarget: controls.target.clone(), start: performance.now() };
  }
  function setCameraView(view: 'tower' | 'workcell'): void {
    cameraView = view; updatePlannedVisibility();
    tracking = view === 'workcell' && !!manifest.cameras?.trackingBody;
    const configured = manifest.cameras?.[view];
    cameraTrackedY = tracking ? trackedY : trackedStartY;
    if (configured) {
      const vertical = tracking ? trackedY - trackedStartY : 0;
      moveCamera(new THREE.Vector3().fromArray(configured.position).add(new THREE.Vector3(0, vertical, 0)), new THREE.Vector3().fromArray(configured.target).add(new THREE.Vector3(0, vertical, 0)));
    } else if (view === 'tower') moveCamera(new THREE.Vector3(110, 80, 126), new THREE.Vector3(0, towerHeight * .46, 0));
    else moveCamera(new THREE.Vector3(18, activeHeight + 5.5, 24), new THREE.Vector3(9, activeHeight + 1.4, 12));
  }
  function updatePlannedVisibility(): void {
    for (const [node, enabled] of plannedNodes) node.visible = enabled && cameraView === 'tower';
    stageNote.hidden = !plannedNodes.size;
    stageNote.textContent = `Levels ${manifest.activeLevel + 1}–${manifest.storeys} planned · ${cameraView === 'tower' ? 'shown as ghost geometry' : 'hidden for workcell inspection'}`;
  }
  function ghostPlannedLevels(root: THREE.Object3D): void {
    root.traverse(node => {
      const level = /^Level_(\d+)$/.exec(node.name);
      if (!level || Number(level[1]) <= manifest.activeLevel) return;
      plannedNodes.set(node, true);
      node.traverse(child => {
        if (!(child instanceof THREE.Mesh)) return;
        authoredMaterials.set(child, child.material);
        const ghost = (source: THREE.Material): THREE.Material => {
          let material = plannedMaterials.get(source);
          if (!material) {
            material = source.clone(); material.transparent = true; material.opacity = .13; material.depthWrite = false;
            if (material instanceof THREE.MeshStandardMaterial) { material.color.set(0x9ca8af); material.metalness = 0; material.roughness = 1; }
            plannedMaterials.set(source, material);
          }
          return material;
        };
        child.material = Array.isArray(child.material) ? child.material.map(ghost) : ghost(child.material);
        child.castShadow = false; child.receiveShadow = false;
      });
    });
  }
  function inspect(id: string): void {
    const entry = selectedNodes.get(id); selected = entry?.node ?? null;
    highlight.visible = !!selected;
    if (!entry) return;
    tracking = false;
    inspection.value = id; detail.textContent = entry.description;
    if (entry.cameraView) { setCameraView(entry.cameraView); return; }
    const bounds = new THREE.Box3().setFromObject(entry.node);
    const center = bounds.getCenter(new THREE.Vector3());
    if (Math.abs(center.y - activeHeight) < manifest.storeyHeight * 2.5) { cameraView = 'workcell'; updatePlannedVisibility(); }
    const radius = Math.max(bounds.getSize(new THREE.Vector3()).length() * .8, manifest.cameras ? 2.2 : 3.5);
    moveCamera(center.clone().add(new THREE.Vector3(.9, .55, 1.25).normalize().multiplyScalar(radius)), center);
  }
  const raycaster = new THREE.Raycaster();
  const pointer = new THREE.Vector2();
  let downX = 0, downY = 0;
  renderer.domElement.addEventListener('pointerdown', event => { downX = event.clientX; downY = event.clientY; });
  renderer.domElement.addEventListener('pointerup', event => {
    if (Math.hypot(event.clientX - downX, event.clientY - downY) > 5) return;
    const rect = renderer.domElement.getBoundingClientRect();
    pointer.set((event.clientX - rect.left) / rect.width * 2 - 1, -(event.clientY - rect.top) / rect.height * 2 + 1);
    raycaster.setFromCamera(pointer, camera);
    const hits = raycaster.intersectObjects([...selectedNodes.values()].map(entry => entry.node), true);
    if (!hits.length) return;
    for (const [id, entry] of selectedNodes) {
      let node: THREE.Object3D | null = hits[0].object;
      while (node) { if (node === entry.node) { inspect(id); return; } node = node.parent; }
    }
  });
  inspection.addEventListener('change', () => inspect(inspection.value));
  overviewButton.addEventListener('click', () => setCameraView('tower'));
  workcellButton.addEventListener('click', () => setCameraView('workcell'));
  controls.addEventListener('start', () => { transition = null; });
  function setPlaying(value: boolean): void { playing = !!trace && bindings.length > 0 && value; play.textContent = playing ? 'Ⅱ Pause' : '▶ Play'; }
  play.addEventListener('click', () => { if (elapsed >= endTime) seek(startTime); setPlaying(!playing); });
  slider.addEventListener('input', () => seek(Number(slider.value)));
  for (const phase of trace?.phases ?? []) {
    const button = element('button', '', phase.label); button.addEventListener('click', () => seek(phase.start)); phases.append(button); phaseButtons.set(phase.id, button);
  }
  const p = new THREE.Vector3(), nextP = new THREE.Vector3(), q = new THREE.Quaternion(), nextQ = new THREE.Quaternion(), offset = new THREE.Vector3(), offsetQ = new THREE.Quaternion();
  const unitScale = new THREE.Vector3(1, 1, 1), worldMatrix = new THREE.Matrix4(), inverseParent = new THREE.Matrix4();
  const ignoredScale = new THREE.Vector3();
  const rigging = new THREE.Group(); rigging.name = 'TraceRigging'; rigging.visible = false; scene.add(rigging);
  const cableGeometry = new THREE.CylinderGeometry(.012, .012, 1, 8);
  const cableMaterial = new THREE.MeshStandardMaterial({ color: 0x20282b, metalness: .5, roughness: .62 });
  const slingCables = [-1, 1].map(side => {
    const cable = new THREE.Mesh(cableGeometry, cableMaterial); cable.name = side < 0 ? 'TraceSlingLeft' : 'TraceSlingRight';
    cable.castShadow = true; rigging.add(cable); return { side, cable };
  });
  const craneCable = new THREE.Mesh(cableGeometry, cableMaterial); craneCable.name = 'TraceCraneCable'; rigging.add(craneCable);
  const trolley = new THREE.Vector3(9, 81, 12), carrierP = new THREE.Vector3(), carrierQ = new THREE.Quaternion(), beamP = new THREE.Vector3(), beamQ = new THREE.Quaternion();
  const cableStart = new THREE.Vector3(), cableEnd = new THREE.Vector3(), cableDirection = new THREE.Vector3(), cableAxis = new THREE.Vector3(0, 1, 0);
  function setCable(cable: THREE.Mesh, start: THREE.Vector3, end: THREE.Vector3, radiusScale = 1): void {
    cableDirection.subVectors(end, start);
    const length = cableDirection.length();
    cable.visible = length > 1e-6;
    if (!cable.visible) return;
    cable.position.copy(start).add(end).multiplyScalar(.5);
    cable.quaternion.setFromUnitVectors(cableAxis, cableDirection.divideScalar(length));
    cable.scale.set(radiusScale, length, radiusScale);
    cable.updateMatrix();
  }
  function interpolateBody(body: string, a: TraceFrame, b: TraceFrame, alpha: number, position: THREE.Vector3, quaternion: THREE.Quaternion): void {
    position.fromArray(a.bodies[body].position).lerp(nextP.fromArray(b.bodies[body].position), alpha);
    quaternion.fromArray(a.bodies[body].quaternion).slerp(nextQ.fromArray(b.bodies[body].quaternion), alpha).normalize();
  }
  function updateRigging(a: TraceFrame, b: TraceFrame, alpha: number, sample: TraceFrame): void {
    if (!rigging.visible) return;
    interpolateBody('hoist_carrier', a, b, alpha, carrierP, carrierQ);
    interpolateBody('lifted_beam', a, b, alpha, beamP, beamQ);
    cableEnd.set(0, .5, 0).applyQuaternion(carrierQ).add(carrierP);
    setCable(craneCable, trolley, cableEnd, 1.5);
    const tension = sample.metrics?.hoistTensionN;
    const released = sample.state?.support === 'two seats' || (tension !== undefined && tension <= 0);
    for (const { side, cable } of slingCables) {
      if (released) { cable.visible = false; continue; }
      cableStart.set(side * 1.6, 0, 0).applyQuaternion(carrierQ).add(carrierP);
      cableEnd.set(side * 1.6, .225, 0).applyQuaternion(beamQ).add(beamP);
      setCable(cable, cableStart, cableEnd);
    }
  }
  function applyFrames(a: TraceFrame, b: TraceFrame, alpha: number, sample: TraceFrame): void {
    for (const { binding, node } of bindings) {
      const pa = a.bodies[binding.body], pb = b.bodies[binding.body];
      if (!pa || !pb) continue;
      interpolateBody(binding.body, a, b, alpha, p, q);
      offset.fromArray(binding.positionOffset ?? [0, 0, 0]).applyQuaternion(q); p.add(offset);
      offsetQ.fromArray(binding.quaternionOffset ?? [0, 0, 0, 1]); q.multiply(offsetQ);
      worldMatrix.compose(p, q, unitScale);
      if (node.parent) { node.parent.updateWorldMatrix(true, false); inverseParent.copy(node.parent.matrixWorld).invert(); worldMatrix.premultiply(inverseParent); }
      worldMatrix.decompose(node.position, node.quaternion, ignoredScale);
      node.updateMatrix(); node.updateWorldMatrix(false, true);
    }
    if (manifest.cameras?.trackingBody && a.bodies[manifest.cameras.trackingBody]) {
      const body = manifest.cameras.trackingBody;
      trackedY = THREE.MathUtils.lerp(a.bodies[body].position[1], b.bodies[body].position[1], alpha);
    }
    for (const metric of metricValues) {
      const value = sample.metrics?.[metric.key];
      metric.value.textContent = value === undefined ? '—' : `${value.toFixed(metric.decimals ?? 0)}${metric.unit ? ` ${metric.unit}` : ''}`;
    }
    updateRigging(a, b, alpha, sample);
    contactValue.textContent = sample.contacts ? String(sample.contacts.length) : '—';
    forceValue.textContent = sample.contacts?.length ? `${Math.max(...sample.contacts.map(contact => contact.normalForce)).toFixed(0)} N` : '—';
  }
  function seek(time: number): void {
    if (!trace || !bindings.length) return;
    elapsed = THREE.MathUtils.clamp(time, startTime, endTime);
    const frames = trace.frames;
    let low = 0, high = frames.length - 1;
    while (low < high - 1) { const middle = Math.floor((low + high) / 2); if (frames[middle].time <= elapsed) low = middle; else high = middle; }
    const a = frames[low], b = frames[high];
    const alpha = b.time === a.time ? 0 : THREE.MathUtils.clamp((elapsed - a.time) / (b.time - a.time), 0, 1);
    const sample = alpha === 1 ? b : a;
    applyFrames(a, b, alpha, sample);
    slider.value = String(elapsed);
    timeDisplay.textContent = `${elapsed.toFixed(1)} / ${endTime.toFixed(1)} s`;
    const phase = trace.phases.find(item => elapsed >= item.start && (elapsed < item.end || (elapsed === endTime && item.end === endTime)));
    for (const [id, button] of phaseButtons) button.setAttribute('aria-current', String(id === phase?.id));
    phaseDescription.textContent = [phase?.description, sample.state?.note, sample.state?.support ? `Support: ${sample.state.support}` : '', sample.state?.connection ? `Connection: ${sample.state.connection}` : ''].filter(Boolean).join(' · ') || 'Recorded dynamics, interpolated between simulator samples.';
  }

  const loader = new GLTFLoader();
  const ready = (async () => {
    const results = await Promise.allSettled(manifest.assets.map(async asset => {
      const gltf = await loader.loadAsync(asset.url);
      if (disposed) { disposeObject(gltf.scene); return; }
      gltf.scene.name = `Asset:${asset.id}`;
      if (asset.position) gltf.scene.position.fromArray(asset.position);
      if (asset.quaternion) gltf.scene.quaternion.fromArray(asset.quaternion);
      gltf.scene.traverse(node => { if (node instanceof THREE.Mesh) { node.castShadow = true; node.receiveShadow = true; } });
      ghostPlannedLevels(gltf.scene);
      roots.set(asset.id, gltf.scene); scene.add(gltf.scene);
    }));
    if (disposed) return;
    results.forEach((result, index) => { if (result.status === 'rejected') messages.push(`Could not load ${manifest.assets[index].url}: ${String(result.reason)}`); });
    for (const item of manifest.inspectables ?? []) {
      const node = findNode(item.assetId, item.node);
      if (!node) continue;
      selectedNodes.set(item.id, { node, description: item.description, cameraView: item.cameraView });
      const option = element('option', '', item.label); option.value = item.id; inspection.append(option);
    }
    for (const layer of manifest.layers ?? []) {
      const nodes = layer.nodes.map(name => findNode(layer.assetId, name)).filter((node): node is THREE.Object3D => !!node);
      if (!nodes.length) continue;
      const label = element('label'); const input = element('input'); input.type = 'checkbox'; input.checked = true;
      input.addEventListener('change', () => {
        nodes.forEach(node => { if (plannedNodes.has(node)) plannedNodes.set(node, input.checked); else node.visible = input.checked; });
        updatePlannedVisibility();
      }); label.append(input, document.createTextNode(layer.label)); layerList.append(label);
    }
    if (trace) {
      for (const binding of trace.bindings) {
        const node = findNode(binding.assetId, binding.node);
        if (!node) continue;
        let depth = 0; let parent = node.parent; while (parent) { depth++; parent = parent.parent; }
        bindings.push({ binding, node, depth });
      }
      bindings.sort((a, b) => a.depth - b.depth);
      if (bindings.length !== trace.bindings.length) {
        messages.push('Playback disabled: every simulator body must resolve to a unique visual node.');
        bindings.length = 0; trace = null;
        play.disabled = true; slider.disabled = true; phaseButtons.forEach(button => { button.disabled = true; });
        badge.textContent = 'Blender model · trace binding incomplete';
        phaseDescription.textContent = 'Still preview. Some recorded bodies could not be matched to modeled assemblies; see model evidence.';
      } else {
        rigging.visible = ['hoist_carrier', 'lifted_beam'].every(body => bindings.some(entry => entry.binding.body === body));
        seek(startTime);
      }
    }
    if (!roots.size) { status.textContent = 'The Blender assets could not be loaded. See model evidence for the failed files.'; }
    else status.hidden = true;
    updatePlannedVisibility();
    updateEvidence();
  })();
  updateEvidence();
  const resize = (): void => {
    const width = Math.max(1, host.clientWidth), height = Math.max(1, host.clientHeight);
    camera.aspect = width / height; camera.updateProjectionMatrix(); renderer.setSize(width, height, false);
  };
  const observer = new ResizeObserver(resize); observer.observe(host); resize();
  const timelineObserver = new ResizeObserver(() => host.style.setProperty('--te-timeline-height', `${timeline.offsetHeight}px`));
  timelineObserver.observe(timeline); host.style.setProperty('--te-timeline-height', `${timeline.offsetHeight}px`);
  let lastTime = performance.now(), request = 0;
  function draw(now: number): void {
    if (disposed) return;
    const delta = Math.min((now - lastTime) / 1000, .1); lastTime = now;
    if (playing) { seek(elapsed + delta * playbackSpeed); if (elapsed >= endTime) setPlaying(false); }
    if (transition) {
      const alpha = THREE.MathUtils.clamp((now - transition.start) / 1600, 0, 1);
      const smooth = alpha * alpha * (3 - 2 * alpha);
      camera.position.lerpVectors(transition.fromPosition, transition.position, smooth);
      controls.target.lerpVectors(transition.fromTarget, transition.target, smooth);
      if (alpha === 1) transition = null;
    }
    if (tracking && !transition) {
      const nextY = THREE.MathUtils.lerp(cameraTrackedY, trackedY, 1 - Math.exp(-delta * 9));
      const shift = nextY - cameraTrackedY;
      camera.position.y += shift; controls.target.y += shift; cameraTrackedY = nextY;
    }
    controls.update();
    if (selected) highlight.box.setFromObject(selected);
    renderer.render(scene, camera); request = requestAnimationFrame(draw);
  }
  request = requestAnimationFrame(draw);
  return {
    ready, seek, setPlaying, setCameraView,
    diagnostics: () => [...messages],
    dispose() {
      disposed = true; cancelAnimationFrame(request); observer.disconnect(); timelineObserver.disconnect(); controls.dispose();
      authoredMaterials.forEach((material, mesh) => { mesh.material = material; });
      plannedMaterials.forEach(material => material.dispose());
      disposeObject(scene); environmentTarget.dispose(); renderer.dispose(); host.remove();
    },
  };
}

function disposeObject(root: THREE.Object3D): void {
  const geometries = new Set<THREE.BufferGeometry>(), materials = new Set<THREE.Material>(), textures = new Set<THREE.Texture>();
  root.traverse(node => {
    if (!(node instanceof THREE.Mesh || node instanceof THREE.Line)) return;
    geometries.add(node.geometry);
    for (const material of Array.isArray(node.material) ? node.material : [node.material]) {
      materials.add(material);
      for (const value of Object.values(material)) if (value instanceof THREE.Texture) textures.add(value);
    }
  });
  geometries.forEach(value => value.dispose()); materials.forEach(value => value.dispose()); textures.forEach(value => value.dispose());
}
