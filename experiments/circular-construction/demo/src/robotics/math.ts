/** Small deterministic geometry kernel. Metres, seconds, kilograms; Z is up. */
export type Vec3 = [number, number, number];
export const add = (a: Vec3,b: Vec3): Vec3 => [a[0]+b[0],a[1]+b[1],a[2]+b[2]];
export const sub = (a: Vec3,b: Vec3): Vec3 => [a[0]-b[0],a[1]-b[1],a[2]-b[2]];
export const scale = (a: Vec3,s: number): Vec3 => [a[0]*s,a[1]*s,a[2]*s];
export const dot = (a: Vec3,b: Vec3): number => a[0]*b[0]+a[1]*b[1]+a[2]*b[2];
export const length = (a: Vec3): number => Math.hypot(...a);
export const cross = (a: Vec3,b: Vec3): Vec3 => [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
export const unit = (a: Vec3): Vec3 => scale(a,1/(length(a)||1));
export const mix = (a: Vec3,b: Vec3,t: number): Vec3 => add(scale(a,1-t),scale(b,t));
export const rotateZ = (p: Vec3, yaw: number): Vec3 => [p[0]*Math.cos(yaw)-p[1]*Math.sin(yaw),p[0]*Math.sin(yaw)+p[1]*Math.cos(yaw),p[2]];
export const clamp = (v: number,a: number,b: number): number => Math.min(b,Math.max(a,v));
export interface Obstacle { id: string; min: Vec3; max: Vec3; }

/** Conservative capsule/box test: exact segment/slab test against an expanded box. */
export function capsuleIntersectsBox(a: Vec3,b: Vec3,radius: number, box: Obstacle): boolean {
  let near=0,far=1;
  for(let k=0;k<3;k++) {
    const delta=b[k]-a[k], lo=box.min[k]-radius, hi=box.max[k]+radius;
    if(Math.abs(delta)<1e-10) { if(a[k]<lo||a[k]>hi)return false; }
    else { const p=(lo-a[k])/delta,q=(hi-a[k])/delta; near=Math.max(near,Math.min(p,q));far=Math.min(far,Math.max(p,q));if(near>far)return false; }
  }
  return true;
}

/** Closest distance between two finite segments, including parallel/degenerate cases. */
export function segmentDistance(a: Vec3,b: Vec3,c: Vec3,d: Vec3): number {
  const u=sub(b,a),v=sub(d,c),w=sub(a,c),A=dot(u,u),B=dot(u,v),C=dot(v,v),D=dot(u,w),E=dot(v,w);
  if(A<1e-12&&C<1e-12)return length(w);
  if(A<1e-12)return length(sub(a,mix(c,d,clamp(E/C,0,1))));
  if(C<1e-12)return length(sub(mix(a,b,clamp(-D/A,0,1)),c));
  const denom=A*C-B*B;
  let s=denom>1e-12?clamp((B*E-C*D)/denom,0,1):0;
  let t=(B*s+E)/C;
  if(t<0){t=0;s=clamp(-D/A,0,1);}else if(t>1){t=1;s=clamp((B-D)/A,0,1);}
  return length(sub(mix(a,b,s),mix(c,d,t)));
}
