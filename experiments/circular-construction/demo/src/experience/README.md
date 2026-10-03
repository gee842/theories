# Blender construction experience

`createTowerExperience(container, manifest, trace?)` loads Blender-authored GLB assets into Three.js. It returns `ready`, `seek(seconds)`, `setPlaying(boolean)`, `setCameraView('tower' | 'workcell')`, `diagnostics()`, and `dispose()`. `ready` resolves after all asset load attempts; failed assets are reported in the evidence panel and diagnostics. The module owns its container child, canvas, controls, scoped styles, renderer, and resource cleanup.

The containing element must have a height. The viewer reserves at least 660px (760px on narrow screens). The inspection panel scrolls within the space above the measured timeline, including when evidence is expanded. Import types from `types.ts` and the constructor from `towerExperience.ts`.

## Asset contract

All display coordinates are metres in glTF Y-up space. Blender world `(x,y,z)` becomes glTF `(x,z,-y)`. Do not rotate the loaded scene back into Z-up space. The 20-storey site is 36m by 24m, with 3.6m storeys and an active workcell at level 12, y=43.2m. The active beam is centred around `[9,43.425,12]` when seated, runs along x, and is 5.6m long.

The manifest supplies one or more `{id,url,position?,quaternion?}` asset instances. Use `public/assets/tower-site.glb` and `public/assets/climber-robot.glb` via `/assets/...` URLs. Every named layer, inspectable, and trace binding is scoped to a manifest asset `id`. Match exact exported glTF names; names are verified for uniqueness rather than guessed by substring. Loading the same robot GLB as two asset instances permits distinct body bindings and initial placements.

Site names are `Level_01` through `Level_20`, `ActiveBeam` (a parent alias), `lifted_beam` (the moving beam), and `ActiveHoist`. Robot names are `robot_chassis`, `limb_fl_upper/lower/grip`, corresponding `fr`, `rl`, `rr` nodes, and `robot_tool`. The robot must export articulated pivots as separate nodes. Each node's geometry remains relative to its authored pivot.

Exact `Level_NN` groups above `activeLevel` represent planned floors. The viewer gives their meshes cloned translucent gray materials in the whole-tower view and hides those groups in the workcell view. A visible stage note identifies them as planned. This keeps future steel out of the active lift corridor. Returning to the whole tower restores the planned groups subject to their layer switches. Authored materials are preserved for cleanup.

`ActiveHoist` must have its pivot at the `hoist_carrier` body position: Blender `[9,-12,46.45]`, or glTF `[9,46.45,12]` in the initial pose. Its geometry contains the spreader and pulley hardware, with the crane attachment about 0.5m above that pivot. Do not bake long crane cables or beam slings into this moving group. `lifted_beam` likewise uses the physical beam body pivot; lifting lug attachment sites are local glTF `[±1.6,0.225,0]`.

An example manifest:

```ts
const manifest: TowerManifest = {
  title: 'A tower assembled by robots',
  storeys: 20, storeyHeight: 3.6, activeLevel: 12,
  assets: [
    { id: 'site', url: '/assets/tower-site.glb' },
    { id: 'robot', url: '/assets/climber-robot.glb', position: [5.55,44.3,12] },
  ],
  layers: [{ id: 'upper', label: 'Upper frame', assetId: 'site',
    nodes: Array.from({length: 8}, (_, i) => `Level_${String(i+13).padStart(2,'0')}`) }],
  inspectables: [
    { id: 'beam', label: 'Incoming beam', assetId: 'site', node: 'lifted_beam', description: 'Beam and end connection geometry.' },
    { id: 'robot', label: 'Climbing robot', assetId: 'robot', node: 'robot_chassis', description: 'Four articulated contact limbs and fastening tool.' },
    { id: 'hoist', label: 'Lifting assembly', assetId: 'site', node: 'ActiveHoist', description: 'Suspended lifting hardware.' },
  ],
  source: { blender: '/assets/construction-site.blend', description: 'Blender source with separate architectural and robot assemblies.' },
};
const experience = createTowerExperience(container, manifest, trace);
await experience.ready;
```

Use the actual generated `.blend` filename for `source.blender`. Stage layers are explicit scene-node lists; the viewer never infers construction completion from time. Completed decks, partial active floor, facade extent, and future steel must be represented by the Blender model and manifest.

Optional `manifest.structural` supplies separate structural evidence:

```ts
structural: {
  engine: 'OpenSees',
  stage12RoofDisplacementM: 0.01742,
  finalSeatReactionsN: [3132.15, 3132.15],
  braceSensitivity: {
    roofDisplacementRatio: 1.1065,
    description: '12-storey case without east-face temporary braces',
  },
  qualification: 'Concept-stage elastic equilibrium study; no safety certification.',
  assumptions: ['Populate with the actual analysis assumptions.'],
  source: '/assets/tower-structure.json',
}
```

The values above illustrate the schema; integration must fetch validated results from the actual export. The panel shows roof displacement in millimetres, the two final seat reactions in kilonewtons, and the relative roof-displacement increase in the missing-brace case. Qualification, assumptions and source appear in model evidence. Structural results do not drive object motion or imply connection certification.

## Dynamics trace

`SimulationTrace` is the shared JSON schema in `types.ts`. Export world-space body poses from MuJoCo, convert them into glTF coordinates, and reorder quaternions from MuJoCo `(w,x,y,z)` into glTF `(x,y,z,w)`. The proper axis conversion is a rotation of −90° around X. For orientations, use `q_gltf = q_conversion * q_mujoco * inverse(q_conversion)`. Record that convention explicitly in `provenance.coordinateConversion`.

Bind simulator body names to exact authored nodes with `{body,assetId,node}`. The optional `positionOffset` and `quaternionOffset` specify the visual pivot's transform relative to the simulator body frame. This matters if a lifting body's origin sits at the hook while the authored group origin sits at the beam. Offsets themselves are expressed in the converted rigid body's local frame.

Each frame contains `{time,bodies:{bodyName:{position,quaternion}}}` for every bound body. All bindings must have finite poses in every frame, unit quaternions, and strictly increasing times. The viewer validates these before playback. It applies world transforms in parent-first order and converts each to a local node transform using the current parent matrix. Robot segments therefore follow recorded rigid-body transforms rather than assumed joint axes or hand-authored limb cycles.

Position interpolation and quaternion SLERP reconstruct between exported frames for smooth rendering. Contact forces, actuator readings, and discrete connection/support states are held from the preceding sample and labeled as recorded data. Rendering does not run a physics solver and interpolation does not constitute new simulated contact evidence.

When both `hoist_carrier` and `lifted_beam` bind successfully, the viewer creates three reusable dark cable cylinders in world space. Each seek transforms carrier sites `[±1.6,0,0]` and beam lug sites `[±1.6,0.225,0]` by their interpolated body quaternions and positions. A third cable joins fixed trolley `[9,81,12]` to carrier site `[0,0.5,0]`. These endpoints use rigid-body poses directly, so visual-origin offsets cannot shift the physical attachment sites. The unit cylinder geometry retains valid local bounds while its orientation and length change; it is disposed with the viewer.

Slings are hidden whenever the recorded `state.support` is `two seats` or `metrics.hoistTensionN` is zero or negative. Scrubbing back restores them from that sample's state; release is never inferred from phase labels or elapsed time. The crane cable remains attached after sling release. The exact final timestamp uses the final frame's discrete evidence. Traces without the paired body bindings show no generated rigging, and invalid traces keep playback disabled.

Provide `phases` with simulator event times and descriptions. Phase times and all supplied numerical metrics must be finite; contact evidence must identify both bodies and have a finite nonnegative normal force. A phase label describes the exported scenario; it must not claim a grasp, lock, fastener engagement, or release that was not modeled. Trace provenance must state engine, description, limitations, and conversion. These are visible in “Model & simulation evidence.” Structural analysis is separate evidence and should be identified distinctly in the integration UI.

If no trace is supplied or validation fails, the viewer shows the still Blender model with playback disabled. If any body fails to bind to a unique asset node, the entire playback is disabled and the missing nodes are named in diagnostics. This avoids a mixture of simulated and stationary limbs being shown as a complete dynamics result.

The implementation uses the official [Three.js GLTFLoader](https://threejs.org/docs/pages/GLTFLoader.html), [OrbitControls](https://threejs.org/docs/pages/OrbitControls.html), and physically based material pipeline with environment lighting and a shadow-casting sun. Orbiting can interrupt a continuous camera transition. The viewer raycasts actual modeled assemblies for inspection; no placeholder robots or building primitives are created.
