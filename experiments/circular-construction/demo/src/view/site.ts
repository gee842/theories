import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

const palette = {
  ground: 0x18252d,
  grid: 0x33434b,
  steel: 0x9eaeb3,
  edge: 0xd8e1df,
  brace: 0x677e86,
  temporary: 0xc9995e,
  material: 0x92bfb8,
  mast: 0xe2a467,
  cable: 0xead5ae,
  node: 0xdce4de,
};

export interface SiteView {
  scene: THREE.Scene;
  camera: THREE.PerspectiveCamera;
  controls: OrbitControls;
  renderer: THREE.WebGLRenderer;
  beam: THREE.Group;
  beamMaterial: THREE.MeshStandardMaterial;
  robotLayer: THREE.Group;
  updateBeam(center: readonly [number, number, number], installed: boolean, supportedByHoist: boolean): void;
  updateCarrier(center: readonly [number, number, number]): void;
  updateHoistHook(position: readonly [number, number, number], attachedToBeam: boolean, beamCenter: readonly [number, number, number]): void;
  updateConnections(configurationA: string, configurationB: string): void;
  draw(): void;
  resize(): void;
  dispose(): void;
}

function box(parent: THREE.Object3D, size: [number, number, number], position: [number, number, number], material: THREE.Material): THREE.Mesh {
  const mesh = new THREE.Mesh(new THREE.BoxGeometry(...size), material);
  mesh.position.set(...position);
  mesh.castShadow = true;
  mesh.receiveShadow = true;
  parent.add(mesh);
  return mesh;
}

function strut(parent: THREE.Object3D, start: THREE.Vector3, end: THREE.Vector3, radius: number, material: THREE.Material): THREE.Mesh {
  const direction = end.clone().sub(start);
  const mesh = new THREE.Mesh(new THREE.CylinderGeometry(radius, radius, direction.length(), 8), material);
  mesh.position.copy(start).add(end).multiplyScalar(0.5);
  mesh.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), direction.normalize());
  mesh.castShadow = true;
  parent.add(mesh);
  return mesh;
}

function placeStrut(mesh: THREE.Mesh, start: THREE.Vector3, end: THREE.Vector3, modelLength: number): void {
  const direction = end.clone().sub(start);
  mesh.position.copy(start).add(end).multiplyScalar(0.5);
  mesh.scale.set(1, Math.max(direction.length(), 0.001) / modelLength, 1);
  mesh.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), direction.normalize());
}

export function createSiteView(container: HTMLElement): SiteView {
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0x0b151c);
  scene.fog = new THREE.Fog(0x0b151c, 23, 60);

  const camera = new THREE.PerspectiveCamera(44, 1, 0.05, 90);
  camera.up.set(0, 0, 1);
  camera.position.set(8.5, -14.0, 9.4);

  const renderer = new THREE.WebGLRenderer({ antialias: true });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.5;
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  container.append(renderer.domElement);

  const controls = new OrbitControls(camera, renderer.domElement);
  controls.target.set(-0.5, 0.3, 1.8);
  controls.enableDamping = true;
  controls.minDistance = 4;
  controls.maxDistance = 32;
  controls.maxPolarAngle = Math.PI;

  scene.add(new THREE.HemisphereLight(0xcce7ef, 0x25313a, 2.0));
  const sun = new THREE.DirectionalLight(0xffe8c9, 3.2);
  sun.position.set(-6, -8, 14);
  sun.castShadow = true;
  sun.shadow.mapSize.set(2048, 2048);
  sun.shadow.camera.left = -14;
  sun.shadow.camera.right = 14;
  sun.shadow.camera.top = 14;
  sun.shadow.camera.bottom = -14;
  sun.shadow.normalBias = 0.03;
  scene.add(sun);

  const groundMaterial = new THREE.MeshStandardMaterial({ color: palette.ground, roughness: 0.94 });
  box(scene, [30, 30, 0.12], [0, 0, -0.10], groundMaterial);
  const grid = new THREE.GridHelper(30, 30, palette.grid, palette.grid);
  grid.rotation.x = Math.PI / 2;
  grid.position.z = -0.025;
  (grid.material as THREE.Material).opacity = 0.35;
  (grid.material as THREE.Material).transparent = true;
  scene.add(grid);

  const steel = new THREE.MeshStandardMaterial({ color: palette.steel, metalness: 0.72, roughness: 0.32 });
  const beamMaterial = new THREE.MeshStandardMaterial({ color: palette.material, metalness: 0.58, roughness: 0.33 });
  const brace = new THREE.MeshStandardMaterial({ color: palette.brace, metalness: 0.58, roughness: 0.44 });
  const edge = new THREE.MeshStandardMaterial({ color: palette.edge, metalness: 0.45, roughness: 0.34 });
  const temporary = new THREE.MeshStandardMaterial({ color: palette.temporary, metalness: 0.5, roughness: 0.35 });
  const mastMaterial = new THREE.MeshStandardMaterial({ color: palette.mast, metalness: 0.54, roughness: 0.32 });
  const cableMaterial = new THREE.MeshStandardMaterial({ color: palette.cable, metalness: 0.28, roughness: 0.43 });

  // Ground-anchored lab fixtures. The same beam uses the front pair, then the rear pair.
  const latchParts: Record<'A' | 'B', THREE.Object3D[]> = { A: [], B: [] };
  const closureParts: Record<'A' | 'B', THREE.Object3D[]> = { A: [], B: [] };
  for (const x of [0, 3]) {
    for (const y of [0, 3]) {
      box(scene, [0.55, 0.55, 0.16], [x, y, 0], brace);
      box(scene, [0.18, 0.18, 3], [x, y, 1.5], steel);
      box(scene, [0.30, 0.30, 0.30], [x, y, 3.0], edge);
    }
    box(scene, [0.15, 3, 0.17], [x, 1.5, 3], steel);
    strut(scene, new THREE.Vector3(x, 0, 0.15), new THREE.Vector3(x, 3, 2.85), 0.055, brace);
    strut(scene, new THREE.Vector3(x, 3, 0.15), new THREE.Vector3(x, 0, 2.85), 0.055, brace);
    // Open capture seat: support below; final closure is a separate visible element.
    for (const y of [0, 3]) {
      const seatX = x === 0 ? 0.09 : 2.91;
      const capX = x === 0 ? 0.01 : 2.99;
      box(scene, [0.24, 0.30, 0.05], [seatX, y, 3.175], temporary);
      for (const side of [-1, 1]) {
        box(scene, [0.24, 0.055, 0.11], [seatX, y + side * 0.1225, 3.255], temporary);
      }
      const target = y === 0 ? 'A' : 'B';
      for (const side of [-1, 1]) latchParts[target].push(box(scene, [0.05, 0.06, 0.05], [seatX, y + side * 0.19, 3.255], temporary));
      closureParts[target].push(box(scene, [0.08, 0.30, 0.04], [capX, y, 3.33], edge));
    }
  }

  // A and B workfaces have explicit paired, continuous docking rails at each joint.
  // Their strength and attachments remain proposed assumptions, not validated hardware.
  for (const x of [0, 3]) for (const y of [0, 3]) for (const side of [-1, 1]) {
    const railX = x + side * 0.58;
    box(scene, [0.075, 0.095, 1.3], [railX, y, 2.25], temporary);
    for (const z of [1.7, 2.8]) {
      box(scene, [0.50, 0.075, 0.075], [x + side * 0.31, y, z], brace);
      box(scene, [0.13, 0.16, 0.08], [railX, y, z], edge);
    }
    if (y === 0) {
      box(scene, [0.055, 0.070, 1.3], [railX, 0.23, 2.55], brace);
      for (const z of [2.01, 3.09]) box(scene, [0.10, 0.10, 0.06], [railX, 0.23, z], edge);
    }
  }

  // The prototype is served by a bounded XY bridge gantry, including stock and inspection racks.
  // Its travelling bridge and trolley follow the recorded hook trajectory.
  const railY = [-5.5, 5.6] as const;
  const railX = [-6.25, 4.25] as const;
  for (const x of railX) for (const y of railY) {
    box(scene, [0.85, 0.85, 0.18], [x, y, 0.07], brace);
    box(scene, [0.19, 0.19, 5.6], [x, y, 2.8], mastMaterial);
  }
  for (const y of railY) box(scene, [railX[1] - railX[0], 0.15, 0.18], [-1, y, 5.58], mastMaterial);
  const gantryBridge = new THREE.Group();
  scene.add(gantryBridge);
  box(gantryBridge, [0.24, railY[1] - railY[0], 0.23], [0, (railY[0] + railY[1]) / 2, 5.56], mastMaterial);
  const trolley = new THREE.Group();
  scene.add(trolley);
  box(trolley, [0.62, 0.58, 0.32], [0, 0, 5.34], edge);
  const hook = new THREE.Group();
  scene.add(hook);
  box(hook, [0.22, 0.22, 0.22], [0, 0, 0], temporary);
  const cableTop = new THREE.Vector3(-1, -3, 5.18);
  const cableBottom = new THREE.Vector3(-1, -3, 4.5);
  const cableLength = cableTop.distanceTo(cableBottom);
  const cable = strut(scene, cableTop, cableBottom, 0.015, cableMaterial);
  const slingStart = new THREE.Vector3(-1, -3, 4.5);
  const slingLeftEnd = new THREE.Vector3(-2.05, -3, 3.97);
  const slingRightEnd = new THREE.Vector3(0.05, -3, 3.97);
  const slingLeftLength = slingStart.distanceTo(slingLeftEnd);
  const slingRightLength = slingStart.distanceTo(slingRightEnd);
  const slingLeft = strut(scene, slingStart, slingLeftEnd, 0.012, cableMaterial);
  const slingRight = strut(scene, slingStart, slingRightEnd, 0.012, cableMaterial);
  slingLeft.visible = false;
  slingRight.visible = false;

  // The receiving cart and inspected spare stock make material custody spatially legible.
  const cart = new THREE.Group();
  cart.position.set(-5, -4, 0.3);
  scene.add(cart);
  box(cart, [3.7, 0.7, 0.22], [0, 0, 0], brace);
  for (const x of [-1.3, 1.3]) for (const y of [-0.36, 0.36]) {
    const wheel = new THREE.Mesh(new THREE.CylinderGeometry(0.19, 0.19, 0.13, 14), brace);
    wheel.rotation.x = Math.PI / 2;
    wheel.position.set(x, y, -0.15);
    cart.add(wheel);
  }
  for (const x of [-1.2, 1.2]) {
    box(cart, [0.28, 0.20, 0.15], [x, 0, 0.22], temporary);
    for (const y of [-0.2, 0.2]) box(cart, [0.28, 0.12, 0.38], [x, y, 0.22], temporary);
  }
  for (let n = 0; n < 4; n++) {
    box(scene, [3.1, 0.10, 0.10], [-5, -4.8 + n * 0.24, 0.17], steel);
  }
  box(scene, [4.0, 1.35, 0.13], [-5, -4.45, 0.01], brace);

  const beam = new THREE.Group();
  box(beam, [2.86, 0.146, 0.254], [0, 0, 0.02], beamMaterial);
  for (const x of [-1.41, 1.41]) box(beam, [0.18, 0.13, 0.09], [x, 0, -0.082], edge);
  scene.add(beam);
  const robotLayer = new THREE.Group();
  scene.add(robotLayer);

  function updateBeam(center: readonly [number, number, number], installed: boolean, supportedByHoist: boolean): void {
    beam.position.set(...center);
    beamMaterial.color.setHex(installed ? palette.edge : palette.material);
    slingLeft.visible = supportedByHoist;
    slingRight.visible = supportedByHoist;
  }

  function updateCarrier(center: readonly [number, number, number]): void {
    cart.position.set(center[0], center[1], center[2] + 0.3);
  }

  function updateHoistHook(position: readonly [number, number, number], attachedToBeam: boolean, beamCenter: readonly [number, number, number]): void {
    const [x, y, z] = position;
    gantryBridge.position.x = x;
    trolley.position.set(x, y, 0);
    hook.position.set(x, y, z);
    placeStrut(cable, new THREE.Vector3(x, y, 5.18), new THREE.Vector3(x, y, z + 0.11), cableLength);
    slingLeft.visible = attachedToBeam;
    slingRight.visible = attachedToBeam;
    if (attachedToBeam) {
      const apex = new THREE.Vector3(x, y, z - 0.12);
      placeStrut(slingLeft, apex, new THREE.Vector3(beamCenter[0] - 1.0, beamCenter[1], beamCenter[2] + 0.16), slingLeftLength);
      placeStrut(slingRight, apex, new THREE.Vector3(beamCenter[0] + 1.0, beamCenter[1], beamCenter[2] + 0.16), slingRightLength);
    }
  }

  function updateConnections(configurationA: string, configurationB: string): void {
    for (const [target, phase] of [['A', configurationA], ['B', configurationB]] as const) {
      const captured = phase === 'captured' || phase === 'final' || phase === 'verified';
      const locked = phase === 'final' || phase === 'verified';
      latchParts[target].forEach(part => { part.visible = captured; });
      closureParts[target].forEach(part => { part.visible = locked; });
    }
  }

  function resize(): void {
    const width = Math.max(container.clientWidth, 1);
    const height = Math.max(container.clientHeight, 1);
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height, false);
  }

  updateBeam([-5, -4, 0.7], false, false);
  updateHoistHook([-1, -3, 4.5], false, [-5, -4, 0.7]);
  updateConnections('absent', 'absent');
  resize();
  const observer = new ResizeObserver(resize);
  observer.observe(container);

  return {
    scene, camera, controls, renderer, beam, beamMaterial, robotLayer, updateBeam, updateCarrier, updateHoistHook, updateConnections,
    draw() { controls.update(); renderer.render(scene, camera); },
    resize,
    dispose() {
      observer.disconnect();
      controls.dispose();
      renderer.dispose();
      renderer.domElement.remove();
      scene.traverse((object) => {
        if (object instanceof THREE.Mesh) object.geometry.dispose();
      });
    },
  };
}
