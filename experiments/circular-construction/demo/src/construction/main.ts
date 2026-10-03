import { buildConstructionPlan, sampleConstruction } from './runtime';
import { createConstructionView, type CameraMode } from './view';
import { advanceTour, buildTour, tourSpanAt } from './tour';
import './style.css';

const app = document.querySelector<HTMLDivElement>('#app');
if (!app) throw new Error('Missing app root');
app.innerHTML = `
  <main class="construction-experience">
    <div id="construction-viewport" class="construction-viewport"></div>
    <header class="construction-header">
      <div class="construction-brand"><span class="brand-symbol" aria-hidden="true">◌</span><div><p class="eyebrow">Circular construction</p><h1>From bare earth to a building.</h1></div></div>
      <span class="evidence-tag">Planned construction · motion unverified</span>
    </header>
    <nav class="camera-controls" aria-label="Camera viewpoint">
      <button data-camera="site" aria-pressed="true">Whole site</button><button data-camera="carrier" aria-pressed="false">Follow carrier</button><button data-camera="assembler" aria-pressed="false">Follow assembler</button><button data-camera="part" aria-pressed="false">Follow part</button>
    </nav>
    <div class="scene-caption"><p class="eyebrow" id="phase-number">01 / Empty site</p><h2 id="phase-title">Bare land. No hidden infrastructure.</h2><p id="phase-detail">An arriving fleet will bring the kit, establish support and build upward.</p></div>
    <aside class="selection-card" aria-label="Selected robot or component">
      <div class="selection-top"><span class="eyebrow">Inspect the work</span><button id="hide-inspector" aria-label="Collapse inspector" title="Collapse inspector">−</button></div>
      <div id="inspector-content"><label class="visually-hidden" for="selected-object">Selected robot or part</label><select id="selected-object"><option value="">Select a robot or click a part</option></select>
      <div id="selection-info"><p class="selection-hint">Select a carrier to follow its load, route and supported handoff.</p></div></div>
    </aside>
    <footer class="playback-deck">
      <div class="timeline-head"><span id="timeline-action">Empty site</span><span class="site-scope">20 storeys · 18 × 12 m</span><span id="site-clock">00:00</span></div>
      <div class="timeline-track"><input id="construction-timeline" type="range" min="0" max="1" step="0.1" value="0" aria-label="Construction simulation time"><div class="phase-marks" id="phase-marks"></div></div>
      <div class="playback-row"><div class="transport"><button id="restart" aria-label="Restart construction" title="Restart">↺</button><button id="previous-phase" aria-label="Previous construction phase" title="Previous phase">‹</button><button id="play-construction" class="play-button">Play construction</button><button id="next-phase" aria-label="Next construction phase" title="Next phase">›</button></div><div class="playback-meta"><span id="parts-count">0 installed parts</span><label for="construction-speed">Playback <select id="construction-speed"><option value="0" selected>Guided tour</option><option value="1">1×</option><option value="30">30×</option><option value="120">120×</option><option value="600">600×</option><option value="3000">3,000×</option><option value="15000">15,000×</option><option value="60000">60,000×</option></select></label></div></div>
      <div class="phase-navigation" id="phase-navigation" aria-label="Construction phases"></div>
    </footer>
    <div class="loading-panel" id="loading-panel"><span class="loading-orbit"></span><strong>Preparing the construction world</strong><p>Loading the Blender material kit and articulated fleet.</p></div>
    <div class="scene-help">Drag to orbit · scroll to approach · click to inspect</div>
  </main>`;
function element<T extends HTMLElement>(id: string): T {
  const result = document.getElementById(id); if (!result) throw new Error(`Missing construction control ${id}`); return result as T;
}
const plan = buildConstructionPlan();
const timeline = element<HTMLInputElement>('construction-timeline'); timeline.max = String(plan.duration);
const robotSelect = element<HTMLSelectElement>('selected-object');
for (const robot of plan.robots) robotSelect.add(new Option(`${robot.id} · ${robot.kind.replace('_', ' ')}`, robot.id));
const phaseNav = element<HTMLDivElement>('phase-navigation');
const phaseMarks = element<HTMLDivElement>('phase-marks');
const shortLabels: Record<string, string> = { empty: 'Bare ground', arrival: 'Robots arrive', bootstrap: 'Prepare the site', foundations: 'Foundations', 'first-frame': 'The first frame', climbing: 'The first loaded climb', swarm: 'Build upward', completion: 'Enclose and finish', inspection: 'Inspect the building', recovery: 'Clear the site', departure: 'The fleet leaves', complete: 'A completed building' };
const majorStages = plan.stages.filter((stage, index, all) => index === 0 || stage.phase !== all[index - 1].phase).map((stage) => ({ ...stage, end: Math.max(...plan.stages.filter((s) => s.phase === stage.phase).map((s) => s.end)) }));
const navLabels: Record<string, string> = { arrival: 'Arrival', bootstrap: 'Groundwork', foundations: 'Foundations', 'first-frame': 'First frame', climbing: 'Loaded climb', swarm: 'Swarm', completion: 'Enclosure', inspection: 'Inspection', recovery: 'Cleanup', departure: 'Departure' };
for (const stage of majorStages) {
  if (navLabels[stage.phase]) {
    const button = document.createElement('button'); button.textContent = navLabels[stage.phase]; button.dataset.phase = stage.phase;
    button.title = `${shortLabels[stage.phase]} · ${formatTime(stage.start)}`; button.addEventListener('click', () => seek(stage.start)); phaseNav.append(button);
  }
  const mark = document.createElement('span'); mark.style.left = `${stage.start / plan.duration * 100}%`; mark.title = stage.label; phaseMarks.append(mark);
}
const tour = buildTour(plan);
function effectiveSpeed() {
  if (speed) return speed;
  const span = tourSpanAt(tour, time);
  return span ? (span.end - span.start) / span.seconds : 1;
}
let time = 0, speed = 0, playing = false, mode: CameraMode = 'site', selected: string | null = null;
let snapshot = sampleConstruction(plan, 0);
let view: Awaited<ReturnType<typeof createConstructionView>> | null = null;
let lastUiTime = -1;
let explicitSelection = false;
let tourCameraEnabled = true, tourFocusActive = false;
let selectedPartOption: HTMLOptionElement | null = null;
const playButton = element<HTMLButtonElement>('play-construction');
function setPlaying(next: boolean) { playing = next; playButton.textContent = next ? 'Pause' : time >= plan.duration ? 'Replay construction' : 'Play construction'; playButton.setAttribute('aria-pressed', String(next)); }
function seek(next: number) { time = Math.max(0, Math.min(plan.duration, next)); snapshot = sampleConstruction(plan, time); lastUiTime = -1; renderUi(); view?.update(snapshot, .016); }
function select(id: string | null) {
  tourCameraEnabled = false;
  explicitSelection = Boolean(id); selected = id;
  if (id && !plan.robots.some((r) => r.id === id)) {
    selectedPartOption?.remove(); selectedPartOption = new Option(id, id); robotSelect.add(selectedPartOption);
  }
  robotSelect.value = id ?? ''; view?.select(id); renderSelection();
}
robotSelect.addEventListener('change', () => select(robotSelect.value || null));
timeline.addEventListener('input', () => seek(Number(timeline.value)));
playButton.addEventListener('click', () => { if (time >= plan.duration) seek(0); setPlaying(!playing); });
element('restart').addEventListener('click', () => { setPlaying(false); tourCameraEnabled = true; tourFocusActive = false; mode = 'site'; view?.camera('site'); select(null); tourCameraEnabled = true; seek(0); });
element('previous-phase').addEventListener('click', () => { const stage = [...plan.stages].reverse().find((s) => s.start < time - .5); seek(stage?.start ?? 0); });
element('next-phase').addEventListener('click', () => { const stage = plan.stages.find((s) => s.start > time + .5); seek(stage?.start ?? plan.duration); });
element<HTMLSelectElement>('construction-speed').addEventListener('change', (event) => { speed = Number((event.target as HTMLSelectElement).value); });
for (const button of Array.from(document.querySelectorAll<HTMLButtonElement>('[data-camera]'))) button.addEventListener('click', () => {
  tourCameraEnabled = false;
  mode = button.dataset.camera as CameraMode; view?.camera(mode);
  for (const other of Array.from(document.querySelectorAll('[data-camera]'))) other.setAttribute('aria-pressed', String(other === button));
  if (mode !== 'site') {
    const existing = snapshot.robots.find((r) => r.id === selected && r.visible);
    const existingPart = snapshot.parts.find((p) => p.id === selected && p.visible);
    const kind = mode === 'assembler' ? 'assembler' : 'carrier';
    if (!(explicitSelection && (mode === 'part' ? Boolean(existingPart || existing?.payloadId) : existing?.kind === kind))) {
      explicitSelection = false; selected = null; view?.select(null); robotSelect.value = ''; renderSelection();
    }
  }

});
element('construction-viewport').addEventListener('pointerdown', () => { tourCameraEnabled = false; });
function updateTourCamera() {
  if (!tourCameraEnabled || speed) return;
  const span = tourSpanAt(tour, time), focus = Boolean(span?.carrierId);
  if (focus === tourFocusActive) return;
  tourFocusActive = focus;
  mode = focus ? 'carrier' : 'site'; selected = span?.carrierId ?? null;
  explicitSelection = focus;
  robotSelect.value = selected ?? '';
  view?.select(selected); view?.camera(mode);
  for (const button of Array.from(document.querySelectorAll<HTMLButtonElement>('[data-camera]'))) button.setAttribute('aria-pressed', String(button.dataset.camera === mode));
}
const narrowScreen = window.matchMedia('(max-width:650px)');
let inspectorPreferenceSet = false;
function collapseInspector(collapsed: boolean) {
  document.querySelector('.selection-card')!.classList.toggle('collapsed', collapsed);
  const button = element('hide-inspector');
  button.textContent = collapsed ? '+' : '−';
  button.setAttribute('aria-label', collapsed ? 'Expand inspector' : 'Collapse inspector');
  button.setAttribute('aria-expanded', String(!collapsed));
  button.title = collapsed ? 'Expand inspector' : 'Collapse inspector';
}
collapseInspector(narrowScreen.matches);
narrowScreen.addEventListener('change', event => { if (!inspectorPreferenceSet) collapseInspector(event.matches); });
element('hide-inspector').addEventListener('click', () => {
  inspectorPreferenceSet = true;
  collapseInspector(!document.querySelector('.selection-card')!.classList.contains('collapsed'));
});
const explanations: Record<string, string> = {
  empty: 'An arriving fleet will bring the kit, establish support and build upward.',
  arrival: 'Mobile robots enter with restrained materials. Each part keeps its identity through the run.',
  bootstrap: 'Ground machines deploy their own service equipment and establish the first working area.',
  foundations: 'Delivered pile sections and foundation modules form the planned ground support system.',
  'first-frame': 'Ground builders hold, brace and join the first structure before climbers mount it.',
  climbing: 'A secured load travels with its carrier up the structure that has just been built.',
  swarm: 'Carriers and assemblers share supported routes and handoff stations across growing workfronts.',
  completion: 'Roof, glazing, circulation and declared service modules arrive through the same material history.',
  inspection: 'The completed scope is inspected while machine access remains available.',
  recovery: 'The fleet removes and carries away its temporary equipment.',
  departure: 'Robots descend, pack their equipment and leave the completed building.',
  complete: 'The defined building remains. This is a planned sequence; load, contact and commissioning evidence remain separate.',
};
function renderUi() {
  timeline.value = String(time);
  for (const button of Array.from(document.querySelectorAll<HTMLButtonElement>('[data-camera]'))) button.setAttribute('aria-pressed', String(button.dataset.camera === mode));
  const stageIndex = Math.max(0, majorStages.findIndex((s) => s.phase === snapshot.phase));
  element('phase-number').textContent = `${String(stageIndex + 1).padStart(2, '0')} / ${snapshot.phase.replaceAll('-', ' ')}`;
  element('phase-title').textContent = shortLabels[snapshot.phase] ?? snapshot.label;
  element('phase-detail').textContent = explanations[snapshot.phase] ?? '';
  element('timeline-action').textContent = snapshot.activeTasks[0] ?? snapshot.label;
  element('site-clock').textContent = `${formatTime(time)} / ${formatTime(plan.duration)} simulated`;
  element('parts-count').textContent = `${snapshot.installedCount.toLocaleString()} / ${snapshot.totalCount.toLocaleString()} parts installed`;
  for (const button of Array.from(phaseNav.querySelectorAll('button'))) button.classList.toggle('active', button.dataset.phase === snapshot.phase);

  renderSelection();
}
function renderSelection() {
  const info = element('selection-info');
  const robot = snapshot.robots.find((r) => r.id === selected);
  const part = snapshot.parts.find((p) => p.id === selected);
  if (robot) {
    const load = snapshot.parts.find((p) => p.id === robot.payloadId);
    const definition = plan.parts.find((p) => p.id === robot.payloadId);
    const geometry = view?.robotGeometry(robot.id);
    const motionLabel = geometry?.mode === 'planned-planted-ik' ? `${geometry.plantedCount} planted jaw targets · IK` : geometry?.mode === 'missing-traverse-targets' ? 'Traverse grips not defined' : 'Planned transport stance';
    info.innerHTML = `<h3>${escapeText(robot.id)}</h3><p class="selected-action">${escapeText(robot.visible ? robot.action : 'Off site')}</p><dl><div><dt>Load</dt><dd>${escapeText(load ? `${load.id} · ${Math.round(definition?.massKg ?? 0)} kg` : 'Empty')}</dd></div><div><dt>Support</dt><dd>${escapeText(supportSummary(robot.supports) || 'Ground / arriving vehicle')}</dd></div><div><dt>Motion</dt><dd>${escapeText(motionLabel)}</dd></div>${load ? `<div><dt>Part support</dt><dd>${escapeText(supportSummary(load.supports) || load.custodian)}</dd></div>` : ''}</dl><p class="selection-note">${escapeText(geometry?.note ?? 'Articulation and support targets are authored motion. Matching loaded dynamics are unverified.')}</p>${geometry?.unreachable.length || geometry?.missingBindings.length ? `<p class="geometry-warning">Grip geometry unavailable: ${escapeText([...geometry.unreachable, ...geometry.missingBindings].join('; '))}</p>` : ''}`;
  } else if (part) {
    const definition = plan.parts.find((p) => p.id === part.id);
    const destination = !definition ? 'Unspecified' : definition.floor < 0 ? 'Ground / site equipment' : definition.kind === 'roof' ? 'Roof' : `Storey ${definition.floor + 1}`;
    info.innerHTML = `<h3>${escapeText(part.id)}</h3><p class="selected-action">${escapeText(part.status.replaceAll('-', ' '))} · ${definition?.massKg ?? '?'} kg</p><dl><div><dt>Custody</dt><dd>${escapeText(part.custodian)}</dd></div><div><dt>Support</dt><dd>${escapeText(supportSummary(part.supports) || 'Awaiting delivery')}</dd></div><div><dt>Destination</dt><dd>${destination}</dd></div></dl><p class="selection-note">Persistent material identity · planned transfer</p>`;
  } else info.innerHTML = '<p class="selection-hint">Select a carrier to follow its load, route and supported handoff.</p>';
}
function supportSummary(ids: string[]) { return ids.length > 3 ? `${ids.length} frame interfaces · ${ids[0]} → ${ids[ids.length - 1]}` : ids.join(' + '); }
function escapeText(text: string) { return text.replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]!)); }
function formatTime(seconds: number) {
  const hours = Math.floor(seconds / 3600), minutes = Math.floor(seconds % 3600 / 60), secs = Math.floor(seconds % 60);
  return hours ? `${hours}h ${String(minutes).padStart(2, '0')}m` : `${String(minutes).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
}
renderUi();
// Read-only browser inspection bridge. Controls, time and world history still have one owner.
Object.defineProperty(window, '__construction', { configurable: true, get: () => Object.freeze({
  ready: Boolean(view), time, duration: plan.duration, playing, speed: effectiveSpeed(), guidedTour: speed === 0, camera: mode, selected,
  state: snapshot, phase: snapshot.phase,
  geometry: selected ? view?.robotGeometry(selected) ?? null : null,
  robotGeometry: snapshot.robots.filter((r) => r.visible).map((r) => ({ id: r.id, ...view?.robotGeometry(r.id) })),
  stages: plan.stages.map((s) => ({ ...s })),
  assets: ['/assets/construction-kit.glb', '/assets/construction-robots.glb'],
  rendered: view ? { calls: view.renderer.info.render.calls, triangles: view.renderer.info.render.triangles } : null,
}) });
try {
  view = await createConstructionView(element('construction-viewport'), plan);
  view.onSelect = select;
  view.onSubject = (id) => {
    if (explicitSelection || selected === id) return;
    selected = id;
    if (!plan.robots.some((r) => r.id === id)) {
      selectedPartOption?.remove(); selectedPartOption = new Option(id, id); robotSelect.add(selectedPartOption);
    }
    robotSelect.value = id; renderSelection();
  };
  element('loading-panel').remove();
  view.update(snapshot, .016);
  let lastFrame = performance.now();
  const animate = (now: number) => {
    const elapsed = Math.min(.1, (now - lastFrame) / 1000); lastFrame = now;
    if (playing) {
      time = speed ? Math.min(plan.duration, time + elapsed * speed) : advanceTour(tour, time, elapsed);
      snapshot = sampleConstruction(plan, time);
      updateTourCamera();
      if (time >= plan.duration) setPlaying(false);
    }
    if (now - lastUiTime > 180) { renderUi(); lastUiTime = now; }
    view!.update(snapshot, elapsed);
    requestAnimationFrame(animate);
  };
  requestAnimationFrame(animate);
} catch (error) {
  const panel = element('loading-panel'); panel.classList.add('load-error');
  panel.innerHTML = `<strong>Construction assets could not load</strong><p>${escapeText(error instanceof Error ? error.message : String(error))}</p><p>The scene needs its Blender kit and fleet. Reload after the assets are available.</p>`;
  console.error(error);
}
