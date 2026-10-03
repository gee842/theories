/** Viewer-space SI units: x east, y up, z south; quaternions use x,y,z,w. */
export type Vec3 = [number, number, number];
export type Quat = [number, number, number, number];

export interface AssetInstance {
  id: string;
  url: string;
  position?: Vec3;
  quaternion?: Quat;
}
/** Separate structural evidence; values are analysis results, not playback motion. */
export interface TowerStructuralSummary {
  engine: string;
  stage12RoofDisplacementM: number;
  /** Final left and right support reactions imported from the dynamics model. */
  finalSeatReactionsN: [number, number];
  braceSensitivity: { roofDisplacementRatio: number; description: string };
  qualification: string;
  assumptions: string[];
  source?: string;
}
export interface TowerManifest {
  title?: string;
  /** Authored architecture only: no trajectory, playback controls or physics metrics. */
  mode?: 'static-design';
  /** Optional presentation for a local mechanism study using the same trace viewer. */
  presentation?: {
    kicker: string; subtitle: string; overviewLabel: string; workcellLabel: string;
    inspectionPlaceholder: string; inspectionIntroduction: string; layerLabel?: string;
    qualification?: string;
    metrics?: { label: string; key: string; unit?: string; decimals?: number }[];
  };
  cameras?: {
    initialView?: 'tower' | 'workcell';
    tower: { position: Vec3; target: Vec3 };
    workcell: { position: Vec3; target: Vec3 };
    /** Follow only vertical movement, retaining the user's orbit and distance. */
    trackingBody?: string;
  };
  storeys: number;
  storeyHeight: number;
  activeLevel: number;
  assets: AssetInstance[];
  /** Node names are exact glTF object names, scoped to an asset instance. */
  layers?: { id: string; label: string; assetId: string; nodes: string[] }[];
  inspectables?: { id: string; label: string; assetId: string; node: string; description: string; cameraView?: 'tower' | 'workcell' }[];
  source?: { blender?: string; description?: string };
  structural?: TowerStructuralSummary;
}

export interface BodyBinding {
  body: string;
  assetId: string;
  node: string;
  /** Optional visual-origin offset in the rigid body's local frame. */
  positionOffset?: Vec3;
  quaternionOffset?: Quat;
}
export interface BodyPose { position: Vec3; quaternion: Quat }
export interface TraceFrame {
  time: number;
  bodies: Record<string, BodyPose>;
  contacts?: { bodyA: string; bodyB: string; normalForce: number }[];
  actuators?: Record<string, { force: number; position?: number }>;
  metrics?: Record<string, number>;
  /** Discrete simulator state, held from the preceding frame. */
  state?: { support?: string; connection?: string; note?: string };
}
export interface SimulationTrace {
  schemaVersion: 1;
  coordinates: 'gltf-y-up';
  units: { length: 'm'; time: 's'; force: 'N' };
  provenance: {
    engine: string;
    engineVersion?: string;
    model?: string;
    generatedAt?: string;
    description: string;
    limitations: string[];
    /** Describe the conversion applied by the exporter, including quaternion order. */
    coordinateConversion: string;
  };
  bindings: BodyBinding[];
  phases: { id: string; label: string; start: number; end: number; description: string }[];
  frames: TraceFrame[];
}

export interface TowerExperience {
  ready: Promise<void>;
  dispose(): void;
  seek(time: number): void;
  setPlaying(playing: boolean): void;
  setCameraView(view: 'tower' | 'workcell'): void;
  diagnostics(): string[];
}
