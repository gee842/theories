import { createTowerExperience } from './experience/towerExperience';
import type { SimulationTrace, TowerManifest } from './experience/types';
import './production.css';

const base = import.meta.env.BASE_URL;
const asset = (name: string): string => `${base}assets/${name}`;

const manifest: TowerManifest = {
  title: 'The growing tower',
  storeys: 20,
  storeyHeight: 3.6,
  activeLevel: 12,
  assets: [
    { id: 'site', url: asset('tower-site.glb') },
    { id: 'robot', url: asset('climber-robot.glb') },
  ],
  layers: [
    { id: 'robot-rails', label: 'Robot grip rails', assetId: 'site', nodes: ['RobotGripRails'] },
    { id: 'temporary-braces', label: 'Temporary braces', assetId: 'site', nodes: ['TemporaryYBraces'] },
    { id: 'crane', label: 'Crane', assetId: 'site', nodes: ['TowerCrane'] },
    { id: 'core', label: 'Core', assetId: 'site', nodes: ['ConcreteCore'] },
    { id: 'site-yard', label: 'Staging yard', assetId: 'site', nodes: ['SiteAndFabricationYard'] },
  ],
  inspectables: [
    { id: 'beam', label: 'I-section beam / 5.6 m', assetId: 'site', node: 'lifted_beam', description: 'Open steel I-section with lifting lugs and drilled end plates. MuJoCo models the 638.6 kg member as a free rigid body with compound I-section collision geometry; it lands on two physical seats.' },
    { id: 'seats', label: 'Paired connection seats', assetId: 'site', node: 'ActiveConnectionSeats', description: 'Bracket and fin-plate geometry supports the beam after hoist release. The dynamics model verifies two seat reactions; it does not yet simulate pin insertion, bolt preload or a certified connection.' },
    { id: 'robot', label: 'Four-limb climbing robot', assetId: 'robot', node: 'robot_chassis', description: 'Articulated four-limb concept with motor torque limits and ideal rail clamps. The recorded motion raises its chassis 0.211 m and releases and reacquires one grip while the other three stay locked.' },
    { id: 'hoist', label: 'Hoist and slings', assetId: 'site', node: 'ActiveHoist', description: 'The carrier follows a prescribed path. MuJoCo simulates tension-only slings and beam motion; release occurs only after both seats carry the beam.' },
  ],
  source: {
    blender: asset('assembly-preview.blend'),
    description: 'Blender 5.2.1 source models: 36 × 24 m grid, 20 × 3.6 m storeys, 5.6 m I-section member, bracket seats and articulated robot. Geometry is a dimensioned concept, not manufacturer CAD.',
  },
};

const app = document.querySelector<HTMLDivElement>('#app');
if (!app) throw new Error('Missing experience host');
app.innerHTML = `<header class="production-bar"><div class="production-brand"><span class="production-mark" aria-hidden="true"></span><div><strong>REGENERATIVE CONSTRUCTION</strong><small>Engineering feasibility demonstrator</small></div></div><div class="production-links"><span class="production-state">Seated beam · fastening pending</span><a href="${base}index.html">Full construction ↗</a><a href="${base}architecture.html">Planned Design ↗</a><a href="${base}climb.html">Climb study ↗</a><a href="${base}lab.html">Mechanism lab ↗</a></div></header><main id="experience" aria-label="Interactive 20-storey construction site"></main><footer class="production-footer"><span>Blender assets · MuJoCo dynamics · OpenSees staged analysis</span><span>Research prototype, not a certified structural or robotics design</span></footer>`;
const mount = app.querySelector<HTMLElement>('#experience');
if (!mount) throw new Error('Missing 3D mount');

interface StructureExport {
  schemaVersion: number;
  engine: string;
  qualification: string;
  assumptions: string[];
  stages: { storeys: number; status: string; roofMaxHorizontalM: number }[];
  activeBeam: { status: string; seatReactionsN: [number, number] };
  negativeBraceCase: { status: string; roofDisplacementRatioToNominal: number };
}

async function fetchJson<T>(name: string): Promise<T> {
  const response = await fetch(asset(name));
  if (!response.ok) throw new Error(`${name}: ${response.status} ${response.statusText}`);
  return await response.json() as T;
}

async function start(): Promise<void> {
  const [physicsResult, structureResult] = await Promise.allSettled([
    fetchJson<SimulationTrace>('workcell-trace.json'),
    fetchJson<StructureExport>('tower-structure.json'),
  ]);
  const trace = physicsResult.status === 'fulfilled' ? physicsResult.value : null;
  if (physicsResult.status === 'rejected') console.error('Could not load physics trace:', physicsResult.reason);
  if (structureResult.status === 'fulfilled') {
    const report = structureResult.value;
    const stage12 = report.stages.find(stage => stage.storeys === 12 && stage.status === 'converged');
    const reactions = report.activeBeam?.seatReactionsN;
    const ratio = report.negativeBraceCase?.roofDisplacementRatioToNominal;
    if (report.schemaVersion === 1 && stage12 && Number.isFinite(stage12.roofMaxHorizontalM)
      && report.activeBeam?.status === 'converged' && reactions?.length === 2
      && reactions.every(Number.isFinite) && Number.isFinite(ratio)) {
      manifest.structural = {
        engine: report.engine,
        stage12RoofDisplacementM: stage12.roofMaxHorizontalM,
        finalSeatReactionsN: reactions,
        braceSensitivity: { roofDisplacementRatio: ratio, description: '12-storey case without east-face temporary braces' },
        qualification: report.qualification,
        assumptions: report.assumptions,
        source: asset('tower-structure.json'),
      };
    } else console.warn('Structural export failed schema and finite-result checks.');
  } else {
    console.warn('Could not load structural export:', structureResult.reason);
  }
  const experience = createTowerExperience(mount!, manifest, trace);
  await experience.ready;
  const diagnostics = experience.diagnostics();
  if (diagnostics.length) console.warn('Tower experience diagnostics:', diagnostics);
}
void start();
