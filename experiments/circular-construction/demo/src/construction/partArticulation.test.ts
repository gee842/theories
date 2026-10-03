import { expect, it } from 'vitest';
import { Matrix4, Object3D, Vector3 } from 'three';
import { entryDoorHinge, entryDoorMatrix, entryDoorOpenness } from './partArticulation';

const nodeFsModule = 'node:fs';
const { readFileSync } = await import(/* @vite-ignore */ nodeFsModule);
it('transports the actual exported door closed, then opens around its original hinge without scaling its hardware', () => {
  const file = readFileSync(new URL('../../public/assets/construction-kit.glb', import.meta.url));
  const data = JSON.parse(file.subarray(20, 20 + file.readUInt32LE(12)).toString('utf8')) as { nodes: { name: string; children?: number[]; translation?: number[]; rotation?: number[] }[] };
  const create = (i: number): Object3D => {
    const source = data.nodes[i], node = new Object3D(); node.name = source.name;
    if (source.translation) node.position.fromArray(source.translation);
    if (source.rotation) node.quaternion.fromArray(source.rotation);
    for (const child of source.children ?? []) node.add(create(child));
    return node;
  };
  const root = create(data.nodes.findIndex(n => n.name === 'kit_entry'));
  root.updateWorldMatrix(true, true);
  const pivot = root.getObjectByName('entry_door_hinge')!;
  expect(pivot).toBeTruthy();
  const probe = new Object3D(); probe.position.set(1.3, 0, 0); pivot.add(probe);
  root.updateWorldMatrix(true, true);
  const inverse = root.matrixWorld.clone().invert();
  const hinge = entryDoorHinge(probe, inverse)!;
  const closed = new Vector3().applyMatrix4(entryDoorMatrix(hinge, 0));
  const open = new Vector3().applyMatrix4(entryDoorMatrix(hinge, 1));
  expect(Math.abs(closed.z)).toBeLessThan(1e-5);
  expect(Math.abs(open.z)).toBeGreaterThan(1);
  const original = new Vector3().applyMatrix4(new Matrix4().multiplyMatrices(inverse, probe.matrixWorld));
  expect(open.distanceTo(original)).toBeLessThan(1e-8);
  expect(entryDoorOpenness({ status: 'carried', progress: 1 })).toBe(0);
  expect(entryDoorOpenness({ status: 'installing', progress: .875 })).toBeCloseTo(.5);
  expect(entryDoorOpenness({ status: 'installed', progress: 1 })).toBe(1);
});
