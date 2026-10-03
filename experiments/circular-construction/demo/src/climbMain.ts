import { createTowerExperience } from './experience/towerExperience';
import type { SimulationTrace, TowerManifest } from './experience/types';
import './climb.css';

const base = import.meta.env.BASE_URL;
const asset = (name: string): string => `${base}assets/${name}`;
const manifest: TowerManifest = {
  title: 'One storey, twelve strokes',
  storeys: 1, storeyHeight: 3.6, activeLevel: 1,
  presentation: {
    kicker: 'Robotics / Local rail study',
    subtitle: '3.6 m ascent · 12 strokes · 48 recorded recaptures',
    overviewLabel: 'Full rail fixture', workcellLabel: 'Follow robot ↗',
    inspectionPlaceholder: 'Select robot, link or receiver',
    inspectionIntroduction: 'Move four grips, then lift the chassis 0.30 m. Follow the robot or inspect the fixed rail fixture.',
    layerLabel: 'Study geometry',
    qualification: 'Ideal point clamps · Rigid rails · Collisions disabled · No payload',
    metrics: [
      { label: 'Recorded ascent', key: 'climbAdvanceM', unit: 'm', decimals: 2 },
      { label: 'Active ideal clamps', key: 'activeGripLocks', unit: '/ 4' },
    ],
  },
  cameras: {
    initialView: 'workcell', trackingBody: 'robot_chassis',
    tower: { position: [-10, 2.7, 14], target: [.25, 1.4, 0] },
    workcell: { position: [-3.2, 1.8, 4.8], target: [.1, .85, 0] },
  },
  assets: [
    { id: 'fixture', url: asset('climb-rail-fixture.glb') },
    { id: 'robot', url: asset('climber-robot-climb.glb') },
  ],
  inspectables: [
    { id: 'robot', cameraView: 'workcell', label: 'Four-limb robot / 137 kg model', assetId: 'robot', node: 'robot_chassis', description: '69 kg chassis plus four 17 kg limbs. Each limb has two 0.45 m links. Eight torque-limited motors move the mechanism; every pose comes from the recorded MuJoCo simulation.' },
    { id: 'rails', cameraView: 'tower', label: 'Fixed rail fixture / 0.30 m pitch', assetId: 'fixture', node: 'ClimbRailFixture', description: 'Local rigid fixture with two rails 0.50 m apart and separate front/rear receiver sequences at 0.30 m pitch. Receiver centers match the simulation contract. Rail compliance and attachment to a tower are outside this study.' },
    { id: 'upper', label: 'Front-left upper link / 0.45 m', assetId: 'robot', node: 'limb_fl_upper', description: 'Shoulder-to-elbow span: 0.45 m. MuJoCo body transforms drive this model directly; the motor torque bound is 450 N·m.' },
    { id: 'grip', label: 'Front-left ideal grip', assetId: 'robot', node: 'limb_fl_grip', description: 'Capture guard: within 4 mm and below 0.025 m/s. A point constraint carries forces once captured. The visible jaws illustrate the concept; their latch, teeth, moments, strength and collision clearance are not simulated.' },
    { id: 'receiver', label: 'Starting front-left receiver', assetId: 'fixture', node: 'rail_fl_0', description: 'Fixed receiver at local viewer coordinates (0.55, 1.52, 0.25) m. Its counterpart and the rear receivers form four ideal support points.' },
  ],
  source: { description: 'Separate Blender climb assets built from production/physics/climb-prototype/geometry-contract.json. Local origin, glTF Y-up. The 1,994 actual MuJoCo frames cover 199.3 s; navigation groups the original 110 detailed phases into twelve strokes and a final hold. This is a local, unloaded climb study; a whole-tower ascent is not demonstrated.' },
};

const app = document.querySelector<HTMLDivElement>('#app');
if (!app) throw new Error('Missing climb host');
app.innerHTML = `<header class="climb-bar"><a class="climb-brand" href="${base}index.html"><strong>REGENERATIVE CONSTRUCTION</strong><small>Full-storey climb study</small></a><nav aria-label="Study navigation"><span>MuJoCo · unloaded prototype</span><a href="${base}architecture.html">Planned Design ↗</a><a href="${base}workcell.html">Tower workcell ↗</a><a href="${base}lab.html">Mechanism lab ↗</a></nav></header><main id="climb-experience" aria-label="Interactive full-storey robot climb"></main><footer class="climb-footer"><span>Recorded dynamics · Independent climb geometry</span><span>Concept study · Not a certified robot or tower attachment</span></footer>`;
const mount = app.querySelector<HTMLElement>('#climb-experience');
if (!mount) throw new Error('Missing climb mount');

async function start(): Promise<void> {
  let trace: SimulationTrace | null = null;
  try {
    const response = await fetch(asset('climb-trace.json'));
    if (!response.ok) throw new Error(`Climb trace: HTTP ${response.status}`);
    trace = await response.json() as SimulationTrace;
  } catch (error) { console.error(error); }
  const experience = createTowerExperience(mount!, manifest, trace);
  await experience.ready;
  const diagnostics = experience.diagnostics();
  if (diagnostics.length) console.warn('Climb study diagnostics:', diagnostics);
}
void start();
