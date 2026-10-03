import { describe, expect, it } from 'vitest';
import { gripForward, solvePlantedClimb } from './plantedGrip';

describe('planned planted-grip geometry', () => {
  it('puts all exported wrist-offset throats on their targets without stretching links', () => {
    for (let h = 1.44; h <= 64; h += .011) {
      const stance = solvePlantedClimb(h);
      expect(stance.plantedCount).toBeGreaterThanOrEqual(3);
      for (const grip of stance.grips) {
        expect(grip.reachable).toBe(true);
        const actual = gripForward(grip, h + (grip.limb[0] === 'f' ? .48 : -.48));
        expect(actual.x).toBeCloseTo(grip.contactX, 9);
        expect(actual.y).toBeCloseTo(grip.worldHeight, 9);
        expect(grip.shoulder + grip.elbow + grip.wrist).toBeCloseTo(0, 10);
        if (grip.planted) expect(grip.worldHeight / .32).toBeCloseTo(grip.anchorIndex, 9);
      }
    }
  });
  it('keeps three retained contacts fixed in world space while the body moves', () => {
    const a = solvePlantedClimb(2.72), b = solvePlantedClimb(2.73);
    for (let i = 0; i < a.grips.length; i++) {
      const first = a.grips[i], next = b.grips[i];
      if (first.planted && next.planted && first.anchorIndex === next.anchorIndex) expect(next.worldHeight).toBe(first.worldHeight);
    }
  });
  it('does not jump at a stride boundary and reports unreachable geometry', () => {
    const left = solvePlantedClimb(3.27999999), right = solvePlantedClimb(3.28000001);
    for (let i = 0; i < left.grips.length; i++) expect(left.grips[i].worldHeight).toBeCloseTo(right.grips[i].worldHeight, 6);
    expect(solvePlantedClimb(3, 2).grips.every((g) => !g.reachable)).toBe(true);
  });
});

// Verify the editable Blender export, rather than only rechecking the solver's own equations.
const nodeFsModule = 'node:fs';
const { readFileSync } = await import(/* @vite-ignore */ nodeFsModule);
import * as THREE from 'three';
it('binds both Blender robot rigs and places their actual named jaw throats on world targets', () => {
  const file = readFileSync(new URL('../../public/assets/construction-robots.glb', import.meta.url));
  const jsonLength = file.readUInt32LE(12);
  const gltf = JSON.parse(file.subarray(20, 20 + jsonLength).toString('utf8')) as { nodes: { name: string; children?: number[]; translation?: number[]; rotation?: number[] }[] };
  for (const role of ['carrier', 'assembler']) {
    const rootIndex = gltf.nodes.findIndex((n) => n.name === role);
    const bindings = new Map<string, THREE.Object3D>();
    const create = (index: number): THREE.Object3D => {
      const data = gltf.nodes[index], node = new THREE.Object3D();
      node.name = data.name;
      if (data.translation) node.position.fromArray(data.translation);
      if (data.rotation) node.quaternion.fromArray(data.rotation);
      bindings.set(data.name.replace(/(?:\.\d+|\d{3}|_\d+)$/, ''), node);
      for (const child of data.children ?? []) node.add(create(child));
      return node;
    };
    const root = create(rootIndex);
    for (const height of [1.44, 1.46, 1.55, 1.67, 1.75, 2.02, 17.319, 63.99]) {
      root.position.set(-9, height, -6.93); root.rotation.y = -Math.PI / 2;
      const stance = solvePlantedClimb(height);
      for (const grip of stance.grips) {
        bindings.get(`limb_${grip.limb}_hip`)!.rotation.set(0, 0, grip.shoulder);
        bindings.get(`limb_${grip.limb}_knee`)!.rotation.set(0, 0, grip.elbow);
        bindings.get(`limb_${grip.limb}_wrist`)!.rotation.set(0, 0, grip.wrist);
      }
      root.updateWorldMatrix(true, true);
      for (const grip of stance.grips) {
        const actual = bindings.get(`limb_${grip.limb}_grip_contact`)!.getWorldPosition(new THREE.Vector3());
        const target = new THREE.Vector3(grip.contactX, grip.worldHeight - height, grip.lateral).applyMatrix4(root.matrixWorld);
        expect(actual.distanceTo(target)).toBeLessThan(2e-6);
        if (grip.planted) expect(actual.y / .32).toBeCloseTo(grip.anchorIndex, 5);
      }
    }
  }
});
