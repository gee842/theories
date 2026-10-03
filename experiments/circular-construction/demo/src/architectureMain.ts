import { createTowerExperience } from './experience/towerExperience';
import type { TowerManifest } from './experience/types';
import './architecture.css';

const base = import.meta.env.BASE_URL;
const asset = (name: string): string => `${base}assets/${name}`;
// GLTFLoader removes dots reserved by Three.js animation paths from Blender's .001 suffixes.
const storeyNodes = (name: string): string[] => Array.from({ length: 20 }, (_, index) => index ? `${name}${String(index).padStart(3, '0')}` : name);
const manifest: TowerManifest = {
  mode: 'static-design', title: 'A future tower design',
  storeys: 20, storeyHeight: 3.6, activeLevel: 20,
  presentation: {
    kicker: 'Planned Design / Architecture',
    subtitle: '20 storeys · 72 m · 36 × 24 m frame',
    overviewLabel: 'Whole design', workcellLabel: 'Entrance & landscape ↗',
    inspectionPlaceholder: 'Select finish, core or landscape',
    inspectionIntroduction: 'Inspect the facade, planted terraces, full-height core and landscaped entrance.',
    layerLabel: 'Design layers',
    qualification: 'Future design study. Not physically built or simulated.',
  },
  cameras: {
    tower: { position: [85, 61, 110], target: [0, 34, 0] },
    workcell: { position: [38, 20, 54], target: [0, 6, 10] },
  },
  assets: [{ id: 'design', url: asset('planned-architecture.glb') }],
  layers: [
    { id: 'finish', label: 'Architectural finish', assetId: 'design', nodes: ['ArchitecturalFinish'] },
    { id: 'facade', label: 'Facade', assetId: 'design', nodes: storeyNodes('FacadeModules') },
    { id: 'floors', label: 'Floor cassettes', assetId: 'design', nodes: storeyNodes('FloorCassettes') },
    { id: 'core', label: 'Full-height core', assetId: 'design', nodes: ['ConcreteCore'] },
  ],
  inspectables: [
    { id: 'finish', label: 'Storey 12 finish and terraces', assetId: 'design', node: 'FinishModule_12', description: 'Concept pale-stone facade details, warm soffits, bronze trim and planted terraces. These are authored finish primitives; their fabrication, attachment, weather sealing, maintenance and robotic installation are not validated.' },
    { id: 'core', label: 'Complete 20-storey core', assetId: 'design', node: 'ConcreteCore', cameraView: 'tower', description: 'The planned architectural core extends through all twenty storeys. Its appearance does not establish structural stiffness, reinforcement, fire performance or a simulated construction sequence.' },
    { id: 'core-floor', label: 'Storey 12 core module', assetId: 'design', node: 'CoreModule_12', description: 'An authored core module in the future twenty-storey design. Concrete-core stiffness and construction do not receive engineering credit from this geometry.' },
    { id: 'landscape', label: 'Entrance and landscaped forecourt', assetId: 'design', node: 'LandscapedForecourt', cameraView: 'workcell', description: 'Concept entrance canopy, paving, planted trees, planters and benches. This is a visual design proposal, with no physical installation, drainage, access, planting or occupancy simulation.' },
  ],
  source: {
    blender: asset('planned-architecture.blend'),
    description: 'Editable Blender future-design study. The planned scene completes twenty storeys of floor, glazing, core and finish geometry and closes the active beam bay for this design view only. Construction crane, staging yard and active workcell are omitted. Finish pieces are visual concepts, not validated construction lifts or structural components. No dynamics trace, physics metrics, autonomous assembly or occupancy simulation is shown.',
  },
};

const app = document.querySelector<HTMLDivElement>('#app');
if (!app) throw new Error('Missing architecture host');
app.innerHTML = `<header class="architecture-bar"><a class="architecture-brand" href="${base}index.html"><strong>REGENERATIVE CONSTRUCTION</strong><small>Planned Design</small></a><nav aria-label="Design navigation"><span>Future architecture study · Not simulated</span><a href="${base}workcell.html">Tower workcell ↗</a><a href="${base}climb.html">Climb study ↗</a></nav></header><main id="architecture-experience" aria-label="Interactive planned 20-storey architectural design"></main><footer class="architecture-footer"><span>Authored Blender geometry · Orbit, zoom and inspect</span><span>20-storey future design study · Not physically built or simulated</span></footer>`;
const mount = app.querySelector<HTMLElement>('#architecture-experience');
if (!mount) throw new Error('Missing architecture mount');
const experience = createTowerExperience(mount, manifest, null);
void experience.ready.then(() => {
  const diagnostics = experience.diagnostics();
  if (diagnostics.length) console.warn(`Planned Design diagnostics: ${JSON.stringify(diagnostics)}`);
});
