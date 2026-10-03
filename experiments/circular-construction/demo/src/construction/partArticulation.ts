import { Matrix4, Object3D, Quaternion } from 'three';
import type { PartState } from './types';

export interface PartHinge { base: Matrix4; rest: Quaternion; child: Matrix4 }

/** Keep the exported hinge and its hardware; rotate only its descendant mesh. */
export function entryDoorHinge(mesh: Object3D, inverseRoot: Matrix4): PartHinge | undefined {
  let hinge: Object3D | null = mesh.parent;
  while (hinge && !hinge.name.startsWith('entry_door_hinge')) hinge = hinge.parent;
  if (!hinge?.parent) return;
  return {
    base: inverseRoot.clone().multiply(hinge.parent.matrixWorld).multiply(new Matrix4().makeTranslation(...hinge.position.toArray())),
    rest: hinge.quaternion.clone(),
    child: hinge.matrixWorld.clone().invert().multiply(mesh.matrixWorld),
  };
}

export function entryDoorOpenness(state: Pick<PartState, 'status' | 'progress'>): number {
  if (state.status === 'installed') return 1;
  if (state.status !== 'installing') return 0;
  const u = Math.max(0, Math.min(1, (state.progress - .75) / .25));
  return u * u * (3 - 2 * u);
}

export function entryDoorMatrix(hinge: PartHinge, openness: number): Matrix4 {
  const rotation = new Quaternion().slerp(hinge.rest, openness);
  return hinge.base.clone().multiply(new Matrix4().makeRotationFromQuaternion(rotation)).multiply(hinge.child);
}
