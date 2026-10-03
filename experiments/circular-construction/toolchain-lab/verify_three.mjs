import assert from 'node:assert/strict';
import { readFileSync, writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { join } from 'node:path';
import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

const output = fileURLToPath(new URL('./output/', import.meta.url));
const bytes = readFileSync(join(output, 'climber-roundtrip.glb'));
const gltf = await new GLTFLoader().parseAsync(
  bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength), '');
let meshes = 0;
gltf.scene.traverse(node => {
  if (!node.isMesh) return;
  meshes++;
  const positions = node.geometry.getAttribute('position');
  assert(positions?.count > 0);
  for (const value of positions.array) assert(Number.isFinite(value));
});
const bounds = new THREE.Box3().setFromObject(gltf.scene);
const size = bounds.getSize(new THREE.Vector3());
assert(meshes > 0 && size.length() > 0);
for (const value of size.toArray()) assert(Number.isFinite(value));
const result = { status: 'passed', threeRevision: THREE.REVISION, meshes,
  boundsMeters: size.toArray(), check: 'Actual GLTFLoader parsing of Blender export; WebGL rendering is separate.' };
writeFileSync(join(output, 'three-report.json'), JSON.stringify(result, null, 2) + '\n');
console.log(JSON.stringify(result));
