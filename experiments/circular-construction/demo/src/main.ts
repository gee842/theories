import { BEAM_ID, createBeamScenario, type BeamFailure } from './scenarios';
import { equipmentPoseAtTime, partPoseAtTime, runScenario, worldAtTime } from './simulation';
import { runGatedScenario } from './simulation/gated';
import type { ExecutionEvent, Scenario, SimulationTrace, WorldState } from './domain/types';
import { createRailClimber } from './robotics';
import { createRobotTaskTrace, robotTaskAtTime } from './integration/robotTask';
import { assessConstructionStages, createBracedTripodExample } from './structure';
import { materialBalances, REFORGED_BEAM_ID, runBeamMaterialLifecycle } from './material';
import { runTwoByTwoFrameExample } from './planning';
import { screenDualClosedSockets, screenScenarioConnectorMotions } from './connectors';
import { createBeamHandoffGates, EvidenceRegistry, evaluateEventGate, type EngineeringInputs } from './validation';
import guideContact from '../numerical/fixtures/robot-task-guide-three-grip.result.json';
import actualGuidingContact from '../numerical/fixtures/robot-task-actual-guiding-incomplete.result.json';
import collinearContact from '../numerical/fixtures/collinear-roll.result.json';
import frameStudy from '../numerical/frame/fixtures/study-summary.json';
import { createRobotVisual } from './view/robotVisual';
import { createFramePreview } from './view/framePreview';
import { createSiteView } from './view/site';
import './style.css';

const app = document.querySelector<HTMLDivElement>('#app');
if (!app) throw new Error('Missing app root');
const benchGates = createBeamHandoffGates({
  connectorMotion: { id: 'sampled-connector-path', version: '1' },
  robotBeamContact: { id: 'robot-beam-contact', version: '1' },
  hoistLoad: { id: 'hoist-load', version: '1' },
  beamFrame: { id: 'linear-frame', version: '1' },
  jointStrength: { id: 'reversible-joint', version: '1' },
  hostFrame: { id: 'supporting-frame', version: '1' },
});
app.innerHTML = `
  <div class="shell">
    <header class="topbar">
      <div class="brand"><span class="brand-mark" aria-hidden="true"></span><div><strong>Reversible Construction</strong><small>Mechanism laboratory</small></div></div>
      <div class="topbar-right"><span class="topbar-phase">ONE BEAM · TWO USES</span><span class="research-badge">RESEARCH MODEL</span></div>
    </header>
    <main class="layout">
      <section class="stage" aria-label="Three-dimensional construction experiment">
        <div class="stage-viewport" id="viewport"></div>
        <div class="stage-label"><span class="stage-dot"></span><span id="stage-label-text">GROUND-FIXTURE BENCH / 3 M MEMBER</span></div>
        <div class="stage-evidence" id="stage-evidence">FULL TASK UNVERIFIED</div>
        <div class="stage-key" id="stage-key" aria-label="Scene legend"><span><i class="key-block key-steel"></i> existing steel</span><span><i class="key-block key-beam"></i> tracked beam</span><span><i class="key-block key-temp"></i> temporary capture</span></div>
      </section>
      <aside class="panel" aria-label="Experiment controls and inspection">
        <div class="panel-section intro"><div class="eyebrow" id="intro-eyebrow">Experiment 01</div><h1 id="intro-title">Can one beam have two lives?</h1><p id="intro-description">Follow the same identified steel member as a robot team installs it, recovers it, inspects it, and installs it at a second position.</p></div>
        <div class="panel-section view-section"><label for="view-mode" class="eyebrow">View</label><select id="view-mode" class="select"><option value="beam">One-beam mechanism</option><option value="frame">Two-storey plan preview</option></select></div>
        <div class="panel-section scenario-section"><label for="scenario" class="eyebrow">Run condition</label><select id="scenario" class="select"><option value="none">Nominal operation</option><option value="mis-seat">Latch misalignment</option><option value="grip-unavailable">Unavailable grip</option><option value="delivery-delay">Delayed delivery</option></select></div>
        <div class="panel-section operation"><div class="eyebrow" id="chapter">Preparing</div><h2 id="operation-label">Allocating component</h2><p id="operation-explanation">The finite stock and supports are tracked throughout this run.</p><div class="operation-progress"><span id="event-counter">0 / 0 operations</span><span id="time-label">00:00</span></div><input aria-label="Construction timeline" id="timeline" type="range" min="0" max="1" value="0" step="0.1"></div>
        <div class="panel-section playback"><div class="buttons"><button id="previous" type="button" aria-label="Previous operation">←</button><button id="play" class="play" type="button">Pause</button><button id="next" type="button" aria-label="Next operation">→</button></div><label class="speed-label" for="speed">Playback speed <output id="speed-value">1×</output></label><input id="speed" type="range" min="0.25" max="4" step="0.25" value="1"></div>
        <div class="panel-section inspect"><div class="eyebrow">Selected component</div><div class="part-head"><strong id="part-name">STEEL-BEAM-001</strong><span id="part-use-count">0 uses</span></div><dl><div><dt>Location</dt><dd id="part-location">Stock rack</dd></div><div><dt>Support</dt><dd id="part-support">Stock rack</dd></div><div><dt>End joints</dt><dd id="part-connections">Absent</dd></div><div><dt>Condition</dt><dd id="part-condition">Qualified</dd></div></dl></div>
        <details class="panel-section material-study gate-audit" open><summary>Fail-closed engineering gates</summary><p>The schematic replay and the evidence-gated execution are separate. The gated execution stops before an operation changes custody when required evidence is missing.</p><dl><div><dt>First guide</dt><dd id="gate-guide"></dd></div><div><dt>First load transfer</dt><dd id="gate-transfer"></dd></div><div><dt>Held support</dt><dd id="gate-support"></dd></div></dl><p class="material-scope">The load-transfer row audits a schematic checkpoint; it is not a reachable state in this strict run because the guide gate already holds. The separate revision-10 frame study cannot qualify these event revisions.</p></details>
        <div class="panel-section structure-screen"><div class="eyebrow">Independent structural experiment</div><h2>Temporary support matters</h2><p>A three-dimensional pin-jointed tripod shows why a member cannot be released merely because it looks connected.</p><label for="structure-stage" class="screen-label">Construction stage</label><select id="structure-stage" class="select"><option value="0">Two legs + temporary restraint</option><option value="1">Restraint released too early</option><option value="2">Third leg installed</option><option value="3">Three legs, overloaded</option></select><div id="structure-result" class="screen-result"><strong id="structure-status"></strong><span id="structure-metric"></span></div><p id="structure-detail" class="screen-detail"></p><p class="screen-scope">Axial truss screen only. The bending frame and connectors in the main scene remain unverified.</p></div>
        <details class="panel-section material-study"><summary>Reversible joint geometry</summary><p>Sampled insertion and extraction paths for the visible open seats are screened against the fixture solids and docking rails.</p><dl><div><dt>A insertion</dt><dd id="joint-a-in"></dd></div><div><dt>A extraction</dt><dd id="joint-a-out"></dd></div><div><dt>B insertion</dt><dd id="joint-b-in"></dd></div><div><dt>B reverse path</dt><dd id="joint-b-out"></dd></div><div><dt>Two closed sockets</dt><dd id="joint-closed"></dd></div></dl><p class="material-scope">Sampled geometric clearance only. B extraction is a reverse-path study; connector forces, fit in the field and frame strength are unverified.</p></details>
        <details class="panel-section material-study"><summary>Robot contact equilibrium</summary><p>Recorded Python solver cases compare one fixed A-guide standoff pose with an impossible collinear point-grip geometry.</p><dl><div><dt>Standoff self-weight</dt><dd id="contact-guide"></dd></div><div><dt>Actual beam guidance</dt><dd id="contact-actual"></dd></div><div><dt>Self-weight load</dt><dd id="contact-weight"></dd></div><div><dt>Collinear grips</dt><dd id="contact-collinear"></dd></div></dl><p class="material-scope">The standoff self-weight equilibrium passes only within the assumed grip and conservative actuator model. The tool stops 0.25 m short of the beam; interaction loads and attachment are not modeled, so actual guidance and host-frame capacity remain unverified.</p></details>
        <details class="panel-section material-study"><summary>Beam-column frame study</summary><p>The visible four-post fixture is represented by a separate linear 3D bending and torsion model. Compare its four load-transfer stages.</p><label for="frame-stage" class="screen-label">Load stage</label><select id="frame-stage" class="select"><option value="temporary-capture">Temporary capture · 80% hoist</option><option value="final-joint">Final joints · 80% hoist</option><option value="hoist-handoff">Partial handoff · 40% hoist</option><option value="hoist-released">Hoist released · 0% hoist</option></select><dl><div><dt>Fixture A</dt><dd id="frame-a"></dd></div><div><dt>Fixture B</dt><dd id="frame-b"></dd></div><div><dt>Missing capture restraint</dt><dd id="frame-negative"></dd></div></dl><p class="material-scope">Independent revision-10 numerical study, not bound to the replay's event revisions. Sections, joint stiffness, base fixity and loads are assumed or incomplete; member, joint and foundation capacities are not qualified. No load release is authorized.</p></details>
        <details class="panel-section material-study"><summary>Material passport and recovery</summary><p>The same identified beam is used twice. An independent accounting scenario then damages it and reforges the recovered steel into a new part ID.</p><dl><div><dt>Opening inventory</dt><dd id="material-opening"></dd></div><div><dt>New beam output</dt><dd id="material-output"></dd></div><div><dt>Process remainder</dt><dd id="material-loss"></dd></div><div><dt>Balance residual</dt><dd id="material-residual"></dd></div><div><dt>Process energy</dt><dd id="material-energy"></dd></div></dl><p class="material-scope">Synthetic inspection and assumed yields. Temporary steel work and fasteners remain in the inventory balance; this does not represent whole-building circularity.</p></details>
        <details class="panel-section material-study planning-study" id="planning-study"><summary>Two-storey scheduling study</summary><p>A separate task graph plans eight bays with temporary braces, rail extensions, lifts, capture, verification, hoist release and one recovery.</p><dl><div><dt>Planned tasks</dt><dd id="schedule-tasks"></dd></div><div><dt>Dependency-only path</dt><dd id="schedule-critical"></dd></div><div><dt>One hoist</dt><dd id="schedule-duration"></dd></div><div><dt>Two hoists</dt><dd id="schedule-two-hoists"></dd></div><div><dt>One-hoist occupancy</dt><dd id="schedule-hoist"></dd></div></dl><p class="material-scope">All task durations and capacity inputs are assumed. Every planned operation remains mechanically unverified; these are scheduling figures, not construction-time predictions.</p></details>
        <div class="panel-section robot-controls"><div class="eyebrow">Four-limb robot task projection</div><p id="robot-status"></p><p id="robot-evidence" class="robot-evidence"></p><div class="buttons"><button id="climb" type="button">Run isolated climbing trial</button><button id="forces" type="button" aria-pressed="false">Show grip forces</button></div></div>
        <div class="panel-note"><span class="note-symbol">i</span><p id="panel-note-text">Four robots are in the bench inventory, with visible primitives sampled under assumed grip limits. Their detailed limb states and validation IDs are not committed to the beam events. Beam contact, rail strength, joint qualification and frame response remain unverified.</p></div>
      </aside>
    </main>
  </div>`;

function element<T extends HTMLElement>(selector: string): T {
  const found = app!.querySelector<T>(selector);
  if (!found) throw new Error(`Missing UI element ${selector}`);
  return found;
}
const viewport = element<HTMLDivElement>('#viewport');
const site = createSiteView(viewport);
// SiteView adds shared lights, ground and grid first; everything after is the bench.
if (site.scene.children[0]?.type !== 'HemisphereLight' || site.scene.children[1]?.type !== 'DirectionalLight' ||
    site.scene.children[2]?.type !== 'Mesh' || site.scene.children[3]?.type !== 'GridHelper')
  throw new Error('SiteView shared/bench scene boundary changed');
const benchObjects = site.scene.children.slice(4);
const beamCamera = site.camera.position.clone();
const beamTarget = site.controls.target.clone();
const visualA = createRobotVisual();
const visualB = createRobotVisual();
const visualC = createRobotVisual();
const visualD = createRobotVisual();
site.robotLayer.add(visualA.group, visualB.group, visualC.group, visualD.group);
let climberA = createRailClimber('climber-1', [0, 0, 0], 1.55);
let climberB = createRailClimber('climber-2', [3, 0, 0], 1.45);
visualA.update(climberA.state);
visualB.update(climberB.state);
let climbing = false;
let forceOverlay = false;
let trace: SimulationTrace = runScenario(createBeamScenario());
let robotTaskTrace = createRobotTaskTrace(trace, { deployment: 'four-robot-bench' });
let clock = 0;
let beamClock = 0;
let planClock = 0;
let viewMode: 'beam' | 'frame' = 'beam';
let playing = true;
let speed = 1;
let previousFrame = performance.now();
const clockRate = 10; // Declared playback mapping, not a change to modeled task durations.
const planClockRate = 300; // Viewer playback only; the plan remains 19,080 modeled seconds.
const timeline = element<HTMLInputElement>('#timeline');
const speedInput = element<HTMLInputElement>('#speed');
const playButton = element<HTMLButtonElement>('#play');
const structuralExample = createBracedTripodExample();
const structuralResults = assessConstructionStages(structuralExample.model, structuralExample.stages);
const structureStage = element<HTMLSelectElement>('#structure-stage');

function drawStructuralScreen(): void {
  const result = structuralResults[Number(structureStage.value)];
  const status = result.stability === 'stable' ? (result.capacity === 'pass' ? 'Pass within axial model' : 'Capacity failed') : result.stability === 'mechanism' ? 'Mechanism detected' : 'Unverified conditioning';
  const maxUtilization = Math.max(0, ...result.members.map(member => member.utilization ?? 0));
  const metric = result.stability === 'mechanism'
    ? `Stiffness rank ${result.diagnostics.stiffnessRank} / ${result.diagnostics.freeDofCount}`
    : result.capacity === 'unverified' ? 'No transferable result' : `Peak axial use ${(maxUtilization * 100).toFixed(0)}%`;
  const detail = result.stability === 'mechanism'
    ? 'The remaining legs permit a free motion when the temporary restraint is removed. The load transfer is blocked.'
    : result.capacity === 'fail'
      ? 'The frame is stable in this idealized model, but member compression exceeds the declared axial capacity.'
      : 'The listed load has a force path to the ground supports under the stated pin-jointed, linear assumptions.';
  const output = element<HTMLDivElement>('#structure-result');
  output.dataset.status = result.canTransferLoad ? 'pass' : 'hold';
  element<HTMLElement>('#structure-status').textContent = status;
  element<HTMLElement>('#structure-metric').textContent = metric;
  element<HTMLElement>('#structure-detail').textContent = detail;
}
structureStage.addEventListener('change', drawStructuralScreen);
drawStructuralScreen();
const jointPaths = screenScenarioConnectorMotions();
for (const [fixture, operation, id] of [['A', 'guide', '#joint-a-in'], ['A', 'lower', '#joint-a-out'], ['B', 'guide', '#joint-b-in'], ['B', 'lower', '#joint-b-out']] as const) {
  const path = jointPaths.find(item => item.fixture === fixture && item.operation === operation);
  element<HTMLElement>(id).textContent = path?.result.status === 'passed' ? 'Clear in model' : 'Blocked';
}
element<HTMLElement>('#joint-closed').textContent = screenDualClosedSockets().status === 'failed' ? 'Blocked' : 'Unexpected clearance';
element<HTMLElement>('#contact-guide').textContent = guideContact.status === 'passed' ? 'Conditional pass' : guideContact.status;
element<HTMLElement>('#contact-actual').textContent = actualGuidingContact.status === 'passed' ? 'Unverified · loads incomplete' : actualGuidingContact.status;
element<HTMLElement>('#contact-weight').textContent = `${Math.abs(guideContact.external_wrench.force_N[2]).toFixed(0)} N`;
element<HTMLElement>('#contact-collinear').textContent = collinearContact.status === 'failed' ? 'No equilibrium' : collinearContact.status;
const frameStageSelect = element<HTMLSelectElement>('#frame-stage');
function drawFrameStudy(): void {
  for (const [fixture, selector] of [['A', '#frame-a'], ['B', '#frame-b']] as const) {
    const result = frameStudy.cases.find(item => item.id === `fixture-${fixture}-nominal`)
      ?.stages.find(item => item.id === frameStageSelect.value);
    const displacement = result?.max_member_translation_m;
    element<HTMLElement>(selector).textContent = result
      ? `${result.status} · ${displacement === null || displacement === undefined ? 'no displacement witness' : `${(displacement * 1000).toFixed(3)} mm modeled peak`}`
      : 'No matching stage';
  }
  const negative = frameStudy.cases.find(item => item.id === 'fixture-A-missing-capture-roll')
    ?.stages.find(item => item.id === 'temporary-capture');
  element<HTMLElement>('#frame-negative').textContent = negative?.status === 'failed'
    ? 'Torsional mechanism detected' : 'No recorded result';
}
frameStageSelect.addEventListener('change', drawFrameStudy);
drawFrameStudy();
const materialStudy = runBeamMaterialLifecycle();
const materialBalance = materialBalances(materialStudy).steel;
const reforgedBeam = materialStudy.assets[REFORGED_BEAM_ID];
element<HTMLElement>('#material-opening').textContent = `${materialBalance.openingMassKg.toFixed(1)} kg steel`;
element<HTMLElement>('#material-output').textContent = `${reforgedBeam.massKg.toFixed(1)} kg · new ID`;
element<HTMLElement>('#material-loss').textContent = `${materialBalance.unrecoveredMassKg.toFixed(1)} kg tracked`;
element<HTMLElement>('#material-residual').textContent = `${materialBalance.residualKg.toFixed(3)} kg`;
element<HTMLElement>('#material-energy').textContent = `${materialStudy.processes.reduce((sum, process) => sum + process.energyKWh, 0).toFixed(0)} kWh assumed`;
const scheduleStudy = runTwoByTwoFrameExample();
const scheduleReport = scheduleStudy.schedule.report;
if (!scheduleReport) throw new Error('The bundled scheduling fixture did not produce a report');
const framePreview = createFramePreview(scheduleStudy.graph, scheduleStudy.schedule);
framePreview.group.visible = false;
site.scene.add(framePreview.group);
const twoHoistReport = runTwoByTwoFrameExample({ hoistCount: 2 }).schedule.report;
if (!twoHoistReport) throw new Error('The two-hoist scheduling fixture did not produce a report');
const hoursAndMinutes = (seconds: number): string => `${Math.floor(seconds / 3600)} h ${Math.floor((seconds % 3600) / 60)} min`;
element<HTMLElement>('#schedule-tasks').textContent = String(scheduleStudy.graph.tasks.length);
element<HTMLElement>('#schedule-critical').textContent = hoursAndMinutes(scheduleReport.precedenceCriticalPathS);
element<HTMLElement>('#schedule-duration').textContent = hoursAndMinutes(scheduleReport.resourceLimitedMakespanS);
element<HTMLElement>('#schedule-two-hoists').textContent = hoursAndMinutes(twoHoistReport.resourceLimitedMakespanS);
element<HTMLElement>('#schedule-hoist').textContent = `${((scheduleReport.resources.find(resource => resource.kind === 'hoist')?.utilization ?? 0) * 100).toFixed(0)}%`;

function prettyTime(seconds: number): string {
  const whole = Math.floor(seconds);
  return `${Math.floor(whole / 60).toString().padStart(2, '0')}:${(whole % 60).toString().padStart(2, '0')}`;
}
function planTime(seconds: number): string {
  return hoursAndMinutes(seconds);
}
function drawPlanState(): void {
  const snapshot = framePreview.setTime(clock);
  const active = snapshot.activeTaskIds[0];
  const task = scheduleStudy.graph.tasks.find(item => item.id === active);
  const status = element<HTMLDivElement>('#stage-evidence');
  status.dataset.status = 'unverified';
  status.textContent = 'SCHEMATIC PLAN · MECHANICS UNVERIFIED';
  element<HTMLElement>('#chapter').textContent = active ? 'SCHEDULED OPERATION' : snapshot.completedTaskCount === snapshot.tasks.length ? 'PLAN FINISHED' : 'WAITING IN PLAN';
  element<HTMLElement>('#operation-label').textContent = task?.id.replaceAll('-', ' ') ?? (snapshot.completedTaskCount === snapshot.tasks.length ? 'All workflow tasks scheduled' : 'Waiting for a workfront');
  element<HTMLElement>('#operation-explanation').textContent = task?.description ?? framePreview.description;
  element<HTMLElement>('#event-counter').textContent = `${snapshot.completedTaskCount} / ${snapshot.tasks.length} planned tasks`;
  element<HTMLElement>('#time-label').textContent = planTime(clock);
  timeline.value = String(clock);
  playButton.textContent = playing ? 'Pause' : 'Play';
}
function activeEventAt(t: number): ExecutionEvent | undefined {
  return trace.events.find(event => t >= event.time - event.duration && t < event.time) ?? trace.events.at(-1);
}
function stageFor(event: ExecutionEvent | undefined): string {
  if (!event) return 'Prepare';
  if (event.action === 'fault' || event.action === 'recover') return 'Recovery';
  if (['begin-removal', 'unfasten', 'release-capture', 'lower', 'return'].includes(event.action)) return 'Dismantle';
  if (['inspect-part', 'qualify-reuse'].includes(event.action)) return 'Inspect and reuse';
  if (event.sequence > trace.events.findIndex(item => item.action === 'qualify-reuse') + 1 && trace.events.some(item => item.action === 'qualify-reuse')) return 'Second use';
  if (['reserve', 'receive', 'deliver', 'attach-hoist', 'move-carrier', 'move-hook'].includes(event.action)) return 'Supply';
  return 'Assembly';
}
function supportName(kind: string): string {
  return ({ 'stock-rack': 'Stock rack', carrier: 'Carrier cradle', hoist: 'Hoist', 'capture-seat': 'Capture seat', 'installed-joint': 'Verified joints', 'ground-anchor': 'Ground anchor' } as Record<string, string>)[kind] ?? kind;
}
function connectionPhrase(phase: string): string {
  return ({absent: 'Not connected', aligned: 'Aligned, hoist held', captured: 'Temporarily captured', final: 'Fastened, awaiting check', verified: 'Verified in the task model'} as Record<string, string>)[phase] ?? phase;
}
function benchEngineeringInputs(world: Readonly<WorldState>, event: Readonly<ExecutionEvent>): EngineeringInputs {
  const part = world.parts[event.partId];
  const partType = world.partTypes[part.typeId];
  const proposedSupports = event.action === 'transfer-load'
    ? [...part.supports.filter(support => support.kind !== 'capture-seat'),
      { kind: 'installed-joint', id: part.assignedTarget }]
    : event.action === 'detach-hoist'
      ? part.supports.filter(support => support.kind !== 'hoist') : part.supports;
  return {
    geometry: { partId: part.id, partType, position: part.position,
      connections: part.connections, connectorGeometry: 'not yet linked to event evidence' },
    supports: { current: part.supports, proposed: proposedSupports,
      equipment: world.equipment, robots: world.robots },
    loads: { beamSelfWeightN: partType.massKg * 9.81,
      robotContactAndHoistReactions: 'not completely calculated',
      lateralConstructionLoads: 'not calculated' },
    capacities: {},
  };
}
function drawGateAudit(scenario: Scenario): void {
  const registry = new EvidenceRegistry();
  const gated = runGatedScenario(scenario, registry, benchEngineeringInputs, {
    guide: benchGates.guide,
    'transfer-load': benchGates.transferLoad,
    'detach-hoist': benchGates.detachHoist,
  });
  const firstTransfer = scenario.events.find(event => event.action === 'transfer-load');
  if (!firstTransfer) throw new Error('Beam scenario has no load-transfer event');
  const schematicBeforeTransfer = trace.checkpoints[firstTransfer.sequence - 2]?.world;
  if (!schematicBeforeTransfer) throw new Error('Missing schematic pre-transfer checkpoint');
  const transferAudit = evaluateEventGate(registry, schematicBeforeTransfer, firstTransfer,
    benchEngineeringInputs(schematicBeforeTransfer, firstTransfer), benchGates.transferLoad);
  element<HTMLElement>('#gate-guide').textContent = gated.hold?.event.action === 'guide'
    ? `Held · ${gated.hold.decision.holds.length} missing checks`
    : gated.status === 'complete' ? 'Passed under named gates' : `Held at ${gated.hold?.event.action}`;
  element<HTMLElement>('#gate-transfer').textContent = transferAudit.allowed
    ? 'Passed under named gates' : `Held · ${transferAudit.holds.length} missing checks`;
  element<HTMLElement>('#gate-support').textContent = gated.world.parts[BEAM_ID].supports
    .map(support => supportName(support.kind)).join(' + ');
}
function drawState(): void {
  if (viewMode === 'frame') { drawPlanState(); return; }
  const world = worldAtTime(trace, clock);
  const part = world.parts[BEAM_ID];
  const pose = partPoseAtTime(trace, BEAM_ID, clock);
  const current = activeEventAt(clock);
  const hoist = part.supports.some(support => support.kind === 'hoist');
  site.updateBeam(pose, part.location === 'installed', hoist);
  site.updateHoistHook(equipmentPoseAtTime(trace, 'hoistHook', clock), hoist, pose);
  const target = part.assignedTarget;
  site.updateConnections(target === 'configuration-A' ? part.connections.A.phase : 'absent', target === 'configuration-B' ? part.connections.A.phase : 'absent');
  site.updateCarrier(equipmentPoseAtTime(trace, 'carrier', clock));
  element<HTMLElement>('#chapter').textContent = stageFor(current).toUpperCase();
  element<HTMLElement>('#operation-label').textContent = current?.label ?? 'Ready';
  element<HTMLElement>('#operation-explanation').textContent = current?.data.message ?? (current?.action === 'complete' ? 'The identified member is now part of its second configuration.' : 'The active operation advances only through its recorded support and connection states.');
  const completed = trace.events.filter(event => event.time <= clock).length;
  element<HTMLElement>('#event-counter').textContent = `${completed} / ${trace.events.length} operations`;
  element<HTMLElement>('#time-label').textContent = prettyTime(clock);
  element<HTMLElement>('#part-use-count').textContent = `${part.useCount} ${part.useCount === 1 ? 'use' : 'uses'}`;
  element<HTMLElement>('#part-location').textContent = ({stock: 'Qualified stock', carrier: 'Carrier', workfront: 'Construction front', installed: 'Installed', 'inspection-yard': 'Inspection yard'} as Record<string, string>)[part.location];
  element<HTMLElement>('#part-support').textContent = part.supports.map(support => supportName(support.kind)).join(' + ');
  element<HTMLElement>('#part-connections').textContent = connectionPhrase(part.connections.A.phase);
  element<HTMLElement>('#part-condition').textContent = part.condition.replace('-', ' ');
  const task = robotTaskAtTime(robotTaskTrace, clock);
  const evidenceBadge = element<HTMLDivElement>('#stage-evidence');
  const localStatus = task.activeEvent?.localGeometry.status ?? 'unverified';
  const earlierUnapproved = robotTaskTrace.events.find(event => event.end <= clock && event.localGeometry.status !== 'pass');
  evidenceBadge.dataset.status = localStatus === 'fail' && !earlierUnapproved ? 'fail' : 'unverified';
  evidenceBadge.textContent = earlierUnapproved
    ? 'ROBOT CHECK UNRESOLVED · SCHEMATIC REPLAY'
    : localStatus === 'pass'
    ? 'LOCAL ROBOT CHECK · FULL TASK UNVERIFIED'
    : localStatus === 'fail' ? 'ROBOT POSE FAILED · SCHEMATIC REPLAY' : 'ROBOT POSE UNVERIFIED · SCHEMATIC REPLAY';
  if (climbing) {
    visualA.update(climberA.state);
    visualB.update(climberB.state);
    visualC.group.visible = false;
    visualD.group.visible = false;
    element<HTMLElement>('#robot-status').textContent = `${climberA.status}. ${climberA.state.completedSteps + climberB.state.completedSteps} verified steps in an isolated rail trial.`;
    element<HTMLElement>('#robot-evidence').textContent = 'This trial has its own clock and is separate from the beam transaction.';
  } else {
    for (const [visual, robotId] of [[visualA, 'climber-1'], [visualB, 'climber-2'], [visualC, 'climber-3'], [visualD, 'climber-4']] as const) visual.update(task.states[robotId]);
    visualC.group.visible = true;
    visualD.group.visible = true;
    const local = task.activeEvent?.localGeometry;
    element<HTMLElement>('#robot-status').textContent = local ? `Local pose and motion: ${local.status.toUpperCase()} under the sampled robot model. ${task.activeMotions.length} active primitive${task.activeMotions.length === 1 ? '' : 's'}.` : 'Waiting for a robot task.';
    element<HTMLElement>('#robot-evidence').textContent = earlierUnapproved
      ? `Earlier robot operation ${earlierUnapproved.eventId} was ${earlierUnapproved.localGeometry.status}; the beam animation continued schematically.`
      : task.activeEvent?.transaction.reasons[0] ?? 'Full beam and frame transaction remains unverified.';
  }
  timeline.value = String(clock);
  playButton.textContent = playing ? 'Pause' : 'Play';
}
function setViewMode(mode: 'beam' | 'frame'): void {
  if (mode === viewMode) return;
  if (viewMode === 'beam') beamClock = clock;
  else planClock = clock;
  viewMode = mode;
  clock = mode === 'beam' ? beamClock : planClock;
  playing = false;
  app!.classList.toggle('frame-mode', mode === 'frame');
  benchObjects.forEach(object => { object.visible = mode === 'beam'; });
  framePreview.group.visible = mode === 'frame';
  timeline.max = String(mode === 'beam' ? trace.finalWorld.time : framePreview.durationS);
  element<HTMLElement>('#stage-label-text').textContent = mode === 'beam' ? 'GROUND-FIXTURE BENCH / 3 M MEMBER' : 'TWO-STOREY FRAME / EIGHT BAYS';
  element<HTMLElement>('#stage-key').innerHTML = mode === 'beam'
    ? '<span><i class="key-block key-steel"></i> existing steel</span><span><i class="key-block key-beam"></i> tracked beam</span><span><i class="key-block key-temp"></i> temporary capture</span>'
    : '<span><i class="key-block key-beam"></i> planned member</span><span><i class="key-block key-temp"></i> active task</span><span><i class="key-block key-steel"></i> dashed guides</span>';
  element<HTMLElement>('#intro-eyebrow').textContent = mode === 'beam' ? 'Experiment 01' : 'Planning study 02';
  element<HTMLElement>('#intro-title').textContent = mode === 'beam' ? 'Can one beam have two lives?' : 'How would a frame grow?';
  element<HTMLElement>('#intro-description').textContent = mode === 'beam'
    ? 'Follow the same identified steel member as a robot team installs it, recovers it, inspects it, and installs it at a second position.'
    : framePreview.description;
  element<HTMLElement>('#panel-note-text').textContent = mode === 'beam'
    ? 'Four robots are in the bench inventory, with visible primitives sampled under assumed grip limits. Their detailed limb states and validation IDs are not committed to the beam events. Beam contact, rail strength, joint qualification and frame response remain unverified.'
    : 'This is a workflow and resource preview. Its member, brace and rail reveals are schematic tokens; the planner has not executed or mechanically validated this frame.';
  element<HTMLElement>('.topbar-phase').textContent = mode === 'beam' ? 'ONE BEAM · TWO USES' : 'EIGHT BAYS · TWO STOREYS';
  element<HTMLDetailsElement>('#planning-study').open = mode === 'frame';
  if (mode === 'frame') {
    site.camera.position.set(11.8, -12.5, 11.2);
    site.controls.target.set(3, 3, 3.1);
  } else {
    site.camera.position.copy(beamCamera);
    site.controls.target.copy(beamTarget);
  }
  site.controls.update();
  drawState();
}
element<HTMLSelectElement>('#view-mode').addEventListener('change', event =>
  setViewMode((event.target as HTMLSelectElement).value as 'beam' | 'frame'));
function load(failure: BeamFailure): void {
  const scenario = createBeamScenario({ failure, seed: 42 });
  trace = runScenario(scenario);
  robotTaskTrace = createRobotTaskTrace(trace, { deployment: 'four-robot-bench' });
  drawGateAudit(scenario);
  clock = 0;
  playing = true;
  timeline.max = String(trace.finalWorld.time);
  drawState();
}
element<HTMLSelectElement>('#scenario').addEventListener('change', event => load((event.target as HTMLSelectElement).value as BeamFailure));
playButton.addEventListener('click', () => { playing = !playing; drawState(); });
element<HTMLButtonElement>('#previous').addEventListener('click', () => {
  playing = false;
  const boundaries = viewMode === 'beam' ? trace.events.map(event => event.time)
    : scheduleStudy.schedule.tasks.flatMap(task => [task.startS, task.endS]).filter((time): time is number => time !== undefined).sort((a, b) => a - b);
  const previous = boundaries.filter(time => time < clock - 0.01).at(-1) ?? 0;
  clock = previous;
  drawState();
});
element<HTMLButtonElement>('#next').addEventListener('click', () => {
  playing = false;
  const boundaries = viewMode === 'beam' ? trace.events.map(event => event.time)
    : scheduleStudy.schedule.tasks.flatMap(task => [task.startS, task.endS]).filter((time): time is number => time !== undefined).sort((a, b) => a - b);
  clock = boundaries.find(time => time > clock + 0.01) ?? (viewMode === 'beam' ? trace.finalWorld.time : framePreview.durationS);
  drawState();
});
timeline.addEventListener('input', () => { playing = false; clock = Number(timeline.value); drawState(); });
speedInput.addEventListener('input', () => { speed = Number(speedInput.value); element<HTMLOutputElement>('#speed-value').textContent = `${speed}×`; });
element<HTMLButtonElement>('#climb').addEventListener('click', () => {
  if (climbing) {
    climbing = false;
    element<HTMLButtonElement>('#climb').textContent = 'Run isolated climbing trial';
    drawState();
    return;
  }
  climberA = createRailClimber('climber-1', [0, 0, 0], 1.55);
  climberB = createRailClimber('climber-2', [3, 0, 0], 1.45);
  climberA.targetHeight = 2.25;
  climberB.targetHeight = 2.15;
  climbing = true;
  element<HTMLButtonElement>('#climb').textContent = 'Stop isolated trial';
});
element<HTMLButtonElement>('#forces').addEventListener('click', event => {
  forceOverlay = !forceOverlay;
  visualA.setDiagnostics(forceOverlay);
  visualB.setDiagnostics(forceOverlay);
  visualC.setDiagnostics(forceOverlay);
  visualD.setDiagnostics(forceOverlay);
  (event.currentTarget as HTMLButtonElement).setAttribute('aria-pressed', String(forceOverlay));
  (event.currentTarget as HTMLButtonElement).textContent = forceOverlay ? 'Hide grip forces' : 'Show grip forces';
});

function frame(now: number): void {
  const elapsed = Math.min((now - previousFrame) / 1000, 0.1);
  previousFrame = now;
  if (playing) {
    const end = viewMode === 'beam' ? trace.finalWorld.time : framePreview.durationS;
    clock = Math.min(end, clock + elapsed * (viewMode === 'beam' ? clockRate : planClockRate) * speed);
    if (clock >= end) playing = false;
  }
  if (climbing) {
    climberA.update(elapsed);
    climberB.update(elapsed);
  }
  drawState();
  site.draw();
  requestAnimationFrame(frame);
}
load('none');
requestAnimationFrame(frame);
