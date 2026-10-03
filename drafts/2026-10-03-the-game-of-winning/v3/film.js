// The Game of Winning, v3: a real-time film. One world per act, continuous cameras, GPU-animated particles.
// Every date and number on screen follows ../trajectory.py.
"use strict";
const Film = (() => {
const W = 1920, H = 1080, TAU = Math.PI * 2, D2R = Math.PI / 180, DUR = 300;
const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
const lerp = (a, b, t) => a + (b - a) * t;
const ss = (a, b, x) => { const t = clamp((x - a) / (b - a)); return t * t * (3 - 2 * t); };
const ease = t => t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
function rngOf(seed) { let a = seed >>> 0; return () => { a = (a + 0x6D2B79F5) | 0; let t = Math.imul(a ^ (a >>> 15), 1 | a); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; }
function gauss(r) { let u = 0, v = 0; while (!u) u = r(); while (!v) v = r(); return Math.sqrt(-2 * Math.log(u)) * Math.cos(TAU * v); }
const { norm, cross, dot, sub, bodyRot } = Engine;
const add = (a, b) => [a[0] + b[0], a[1] + b[1], a[2] + b[2]], scl = (a, k) => [a[0] * k, a[1] * k, a[2] * k];
const mixv = (a, b, t) => [lerp(a[0], b[0], t), lerp(a[1], b[1], t), lerp(a[2], b[2], t)];
const len = a => Math.hypot(a[0], a[1], a[2]);
const ll = (lon, lat) => { const a = lon * D2R, b = lat * D2R; return [Math.cos(b) * Math.sin(a), Math.sin(b), Math.cos(b) * Math.cos(a)]; };
const AMBER = [1.0, 0.52, 0.16];

/* ================= the clock: years, power, population ================= */
function keyed(keys, t, log) {
  if (t <= keys[0][0]) return keys[0][1];
  for (let i = 1; i < keys.length; i++) if (t <= keys[i][0]) { const [t0, v0] = keys[i - 1], [t1, v1] = keys[i], u = (t - t0) / (t1 - t0); return log ? v0 * Math.pow(v1 / v0, u) : lerp(v0, v1, u); }
  return keys[keys.length - 1][1];
}
const YEARS = [[7, 2026], [9.5, 2026], [30, 2046], [33, 2050], [41, 2050], [50, 2068], [59, 2097], [72, 2113], [74, 2120], [84.5, 2120], [92, 2132], [98.5, 2140], [112, 2170], [118, 2185], [132, 2291], [148, 2300]];
const YEARS_DEEP = [[148, 2300], [154, 11300], [170, 14300], [195, 2002300], [215, 2002300], [232, 2002400], [262, 2600000], [272, 2650000]];
function yearAt(t) { return t < 148 ? keyed(YEARS, t) : keyed(YEARS_DEEP, t, true); }
const G_RATE = Math.pow(945 / 415, 1 / 6) - 1, P2030 = 945e12 / 8766;
function powerAt(t) {
  if (t < 148) return Math.min(3.8e26, P2030 * Math.pow(1 + G_RATE, yearAt(t) - 2030));
  if (t < 170) return 3.8e26 * (1 + 0.02 * ss(148, 170, t));
  if (t < 223) return Math.exp(lerp(Math.log(3.9e26), Math.log(1e37), ss(171, 194, t)));
  return 1e37 * aliveFraction(t);
}
const POP = [[2026, 8.3e9], [2050, 9.66e9], [2084, 10.3e9], [2097, 9.9e9], [2105, 6.1e9], [2110, 3.4e9], [2113, 0.9e9], [2120, 4.2e7], [2291, 2.0e6]];
const popAt = t => keyed(POP, yearAt(t), true);

/* ================= the worlds ================= */
// The solar system, one space (sizes exaggerated, positions consistent). Units: Earth radii, compressed distances.
const SUN = [0, 0, 0], SUN_R = 12, MERC = [63, 0, -30], MERC_R = 0.42, VEN = [98, 0, 36], VEN_R = 0.95, EARTH = [150, 0, 0], MOON = add([150, 0, 0], [-3.2, 1.2, 9.3]), MOON_R = 0.27;
const SUN_DIR_AT_EARTH = norm(sub(SUN, EARTH));
// Earth turns under a camera fixed relative to the Sun: lon of the point under the camera = phiD + spin
const earthRot = (camDirWorld, lonDeg) => { const phi = Math.atan2(camDirWorld[0], camDirWorld[2]); return bodyRot(lonDeg * D2R - phi, 0); };
const toWorld = (rot, v) => [rot[0] * v[0] + rot[1] * v[1] + rot[2] * v[2], rot[3] * v[0] + rot[4] * v[1] + rot[5] * v[2], rot[6] * v[0] + rot[7] * v[1] + rot[8] * v[2]];
const toBody = (rot, v) => [rot[0] * v[0] + rot[3] * v[1] + rot[6] * v[2], rot[1] * v[0] + rot[4] * v[1] + rot[7] * v[2], rot[2] * v[0] + rot[5] * v[1] + rot[8] * v[2]];

// Camera paths through keyframes [t, pos, look, fov]: each move eases in and out; no overshoot between distant keys
function camPath(keys, t) {
  let i = 0; while (i < keys.length - 2 && t > keys[i + 1][0]) i++;
  const k1 = keys[i], k2 = keys[Math.min(i + 1, keys.length - 1)];
  const u = k2[0] > k1[0] ? ease(clamp((t - k1[0]) / (k2[0] - k1[0]))) : 0;
  return { pos: mixv(k1[1], k2[1], u), look: mixv(k1[2], k2[2], u), fov: lerp(k1[3], k2[3], u) };
}

/* ================= state ================= */
let E, ctx, tex = {}, ready = false, GROW = null;
const PT = new Float32Array(8 * 200000), LN = new Float32Array(11 * 60000);
let np = 0, nl = 0;
function pt(p, c, a, size) { if (np >= 200000) return; const o = np * 8; PT[o] = p[0]; PT[o + 1] = p[1]; PT[o + 2] = p[2]; PT[o + 3] = c[0]; PT[o + 4] = c[1]; PT[o + 5] = c[2]; PT[o + 6] = a; PT[o + 7] = size; np++; }
function ln(a, b, c, alpha, w) { if (nl >= 60000) return; const o = nl * 11; LN.set([a[0], a[1], a[2], b[0], b[1], b[2], c[0], c[1], c[2], alpha, w], o); nl++; }
const flushPts = opt => { E.points(PT, np, opt); np = 0; };
const flushLns = opt => { E.lines(LN, nl, opt); nl = 0; };
let CAM = null;   // current camera, for labels
function camera(pos, look, fov = 40, near = 0.01, far = 20000) { CAM = { pos, look }; return E.camera(pos, look, [0, 1, 0], fov, near, far); }

/* ================= GPU particle systems ================= */
let SYS = {}, SYS_GAL_BODY = '';
function buildSystems() {
  // background stars, centred on the camera
  { const r = rngOf(3), n = 12000, d = new Float32Array(n * 8); for (let i = 0; i < n; i++) { const z = r() * 2 - 1, a = r() * TAU, q = Math.sqrt(1 - z * z), m = Math.pow(r(), 6); d.set([q * Math.cos(a), z, q * Math.sin(a), 0.05 + m * 2.2, r(), 1 + m * 2.5, 0, 0], i * 8); }
    SYS.stars = E.particles(d, 2, `uniform float uK; void particle(out vec3 pos, out vec4 col, out float size){ pos = uCenter + a0.xyz * 6000.0; col = vec4(0.75 + 0.25 * a1.x, 0.82, 1.0 - 0.2 * a1.x, a0.w * uK); size = a1.y; }`); }
  // orbital compute around the Earth, by year
  { const r = rngOf(67), n = 160000, d = new Float32Array(n * 8); for (let i = 0; i < n; i++) { const k = i % 4000; d.set([k * 7.31 + 0.5, r() * TAU, 1.04 + Math.pow(hashK(k), 2) * 0.25, r(), 2034 + Math.pow(i / n, 0.55) * 85, r(), 0, 0], i * 8); }
    SYS.orbit = E.particles(d, 2, `uniform vec3 uSunDir; uniform float uK;
      void particle(out vec3 pos, out vec4 col, out float size){
        vec3 n = normalize(hash31(a0.x) * 2.0 - 1.0); vec3 ax = normalize(cross(n, vec3(0.2, 0.3, 1.0))), ay = cross(n, ax);
        float ph = a0.y + uT * 0.5 / pow(a0.z, 1.5); vec3 rel = (ax * cos(ph) + ay * sin(ph)) * a0.z; pos = uCenter + rel;
        float lit = dot(normalize(rel), uSunDir) > -0.12 ? 1.0 : 0.08; float on = smoothstep(a1.x, a1.x + 1.5, uYear);
        col = vec4(1.0, 0.9, 0.76, (0.3 + pow(a0.w, 14.0) * 6.0) * lit * on * uK); size = 1.5; }`); }
  // the collector swarm around the Sun
  { const r = rngOf(43), n = 700000, d = new Float32Array(n * 8); for (let i = 0; i < n; i++) { const k = i % 900; d.set([k * 3.17 + 0.3, r() * TAU, 1.35 + hashK(k + 11) * 0.9 + gauss(r) * 0.01, r(), 119 + 9 * Math.pow(hashK(k + 5), 0.8) + r() * 1.2, r(), 0, 0], i * 8); }
    SYS.swarm = E.particles(d, 2, `uniform float uIR, uR, uK;
      void particle(out vec3 pos, out vec4 col, out float size){
        vec3 n = normalize(hash31(a0.x) * 2.0 - 1.0); vec3 ax = normalize(cross(n, vec3(0.3, 0.1, 1.0))), ay = cross(n, ax);
        float rr = a0.z * uR; float ph = a0.y + uT * 0.25 / pow(a0.z, 1.5); pos = uCenter + (ax * cos(ph) + ay * sin(ph)) * rr;
        float on = smoothstep(a1.x, a1.x + 0.8, uT); float glint = pow(a0.w, 18.0) * 6.0 + 0.07;
        col = vec4(mix(vec3(1.0, 0.88, 0.7), vec3(0.75, 0.1, 0.035), uIR), mix(glint, 0.42, uIR) * on * uK); size = 1.5; }`); }
  // debris rings of Mercury and Venus; later the material streams inward to the swarm
  { const r = rngOf(61), n = 120000, d = new Float32Array(n * 8); for (let i = 0; i < n; i++) { const venus = i % 2; d.set([r() - 0.5, gauss(r) * 0.5, gauss(r) * 0.15, venus, r(), 0.3 + r() * 0.7, 0, 0], i * 8); }
    SYS.debris = E.particles(d, 2, `uniform vec4 uM, uV; uniform float uSwarmR;   // uM: (orbitR, startAngle, t0, -) for Mercury; uV for Venus
      void particle(out vec3 pos, out vec4 col, out float size){
        vec4 P = a0.w > 0.5 ? uV : uM; float age = uT - P.z; if (age < 0.0) { col = vec4(0.0); pos = vec3(0.0); size = 0.0; return; }
        float spread = 6.2831853 * smoothstep(0.0, 9.0, age); float ang = P.y + a0.x * spread + age * 0.03;
        float inflow = smoothstep(120.0 + a1.x * 6.0, 126.0 + a1.x * 6.0, uT);
        float rr = mix(P.x + a0.y * mix(0.3, 2.5, smoothstep(0.0, 9.0, age)), uSwarmR * (1.4 + a1.y * 0.6), inflow);
        pos = vec3(cos(ang) * rr, a0.z + sin(ang) * rr * 0.02, sin(ang) * rr);
        col = vec4(1.0, 0.62, 0.3, 0.55 * (1.0 - inflow * 0.85)); size = 1.6; }`); }
  // the galaxy, with its whole war precomputed per star
  buildGalaxy();
  { const G = GAL, d = new Float32Array(G.n * 12); for (let i = 0; i < G.n; i++) { const k = G.dom[i]; d.set([G.pos[i * 3], G.pos[i * 3 + 1], G.pos[i * 3 + 2], G.b[i], G.col[i * 3], G.col[i * 3 + 1], G.col[i * 3 + 2], G.conv[i], G.death[k] + G.ripple[i], G.seam[i], 0, 0], i * 12); }
    SYS_GAL_BODY = `uniform float uIR, uWar, uSplit, uFrontOn, uNear, uGlow;
      void particle(out vec3 pos, out vec4 col, out float size){
        pos = a0.xyz; vec3 red = vec3(0.85, 0.12, 0.05); vec3 c = a1.xyz; float a = a0.w * 0.9 * (1.0 + 3.0 * uNear); size = 1.4 * (1.0 + 1.5 * uNear);
        if (uFrontOn > 0.5 && uT >= a1.w) { float age = uT - a1.w; if (age < 0.5) { c = vec3(1.0, 0.6, 0.2); a = 5.0 * (1.0 - age / 0.5) + 0.3; } else { c = mix(vec3(0.55, 0.14, 0.05), red, uIR); a = mix(0.32 * a0.w + 0.08, a0.w * 0.8, uIR); } }
        if (uWar > 0.5) { c = red; a = a0.w * 0.8; float sk = uSplit * clamp(1.0 - a2.y / 0.35, 0.0, 1.0); c = mix(c, vec3(1.0, 0.75, 0.6), sk); a += sk * 1.6;
          float dt = uT - a2.x; if (dt > 0.7) { col = vec4(0.0); return; } if (dt > 0.0) { c = vec3(1.0, 0.85, 0.7); a = 9.0 * (1.0 - dt / 0.7); } }
        if (uGlow > 0.0) { a *= uGlow; size = 30.0; }
        col = vec4(c, a); }`;
    SYS.galaxy = E.particles(d, 3, SYS_GAL_BODY);
    // a diffuse glow under the stars: a sparse subset drawn as large soft sprites
    const gN = 22000, gd = new Float32Array(gN * 12), rr = rngOf(91); for (let i = 0; i < gN; i++) { const j = Math.floor(rr() * G.n); gd.set(d.subarray(j * 12, j * 12 + 12), i * 12); }
    SYS.glow = E.particles(gd, 3, SYS_GAL_BODY); }
}
function hashK(k) { const x = Math.sin(k * 12.9898) * 43758.5453; return x - Math.floor(x); }

/* ================= the growth map: where and when the Earth turns industrial ================= */
const DC_REGIONS = [[-77.49, 39.04], [-97.0, 32.9], [-112.0, 33.4], [-99.73, 32.45], [-83.0, 40.0], [-84.4, 33.75], [-87.6, 41.9], [-121.9, 37.4], [-122.9, 45.5], [-95.9, 41.3], [-73.6, 45.5],
  [-6.26, 53.35], [-0.1, 51.5], [4.9, 52.37], [8.68, 50.1], [2.35, 48.86], [22.15, 65.58], [-3.7, 40.4], [9.19, 45.46], [21.0, 52.23], [139.7, 35.68], [135.5, 34.7], [126.98, 37.56],
  [114.9, 40.8], [121.5, 31.2], [106.6, 26.6], [113.1, 41.0], [114.2, 22.3], [103.8, 1.35], [106.8, -6.2], [72.88, 19.07], [80.27, 13.08], [151.2, -33.87], [144.96, -37.8],
  [-46.63, -23.55], [-100.4, 20.6], [28.05, -26.2], [54.38, 24.45], [46.7, 24.7], [34.78, 32.08]];
function buildGrowth(nightImg, dayImg) {
  const GW = 1024, GH = 512, cv = document.createElement("canvas"); cv.width = GW; cv.height = GH; const c2 = cv.getContext("2d", { willReadFrequently: true });
  c2.drawImage(nightImg, 0, 0, GW, GH); const night = c2.getImageData(0, 0, GW, GH).data;
  c2.drawImage(dayImg, 0, 0, GW, GH); const day = c2.getImageData(0, 0, GW, GH).data;
  const N = GW * GH, light = new Float32Array(N), sea = new Float32Array(N);
  for (let i = 0; i < N; i++) {
    const o = i * 4; light[i] = (night[o] + night[o + 1] + night[o + 2]) / 765;
    const r = day[o], g = day[o + 1], b = day[o + 2];
    const isSea = b > r * 1.25 && b > g * 1.05 && r < 110; sea[i] = isSea ? clamp(1 - (b - 40) / 150) * 0.97 + 0.03 : 0;   // brighter blue = shallower
  }
  // multi-source Dijkstra over land: cheaper through lit (populated, powered) land
  const cost = new Float32Array(N).fill(1e9), heap = [];
  const push = (c, i) => { heap.push([c, i]); let k = heap.length - 1; while (k > 0) { const p = (k - 1) >> 1; if (heap[p][0] <= heap[k][0]) break; [heap[p], heap[k]] = [heap[k], heap[p]]; k = p; } };
  const pop = () => { const top = heap[0], last = heap.pop(); if (heap.length) { heap[0] = last; let k = 0; for (;;) { const l = 2 * k + 1, r = l + 1; let m = k; if (l < heap.length && heap[l][0] < heap[m][0]) m = l; if (r < heap.length && heap[r][0] < heap[m][0]) m = r; if (m === k) break; [heap[m], heap[k]] = [heap[k], heap[m]]; k = m; } } return top; };
  for (const [lo, la] of DC_REGIONS) { const x = Math.floor((lo + 180) / 360 * GW), y = Math.floor((90 - la) / 180 * GH), i = y * GW + x; cost[i] = 0; push(0, i); }
  while (heap.length) {
    const [c, i] = pop(); if (c > cost[i]) continue; const x = i % GW, y = (i / GW) | 0, lat = (90 - (y + 0.5) / GH * 180) * D2R, cx = Math.cos(lat);
    for (let dy = -1; dy <= 1; dy++) for (let dx = -1; dx <= 1; dx++) {
      if (!dx && !dy) continue; const ny = y + dy; if (ny < 0 || ny >= GH) continue; const nx = (x + dx + GW) % GW, j = ny * GW + nx;
      if (sea[j] > 0) continue; const step = Math.hypot(dx * cx, dy) * (1.35 - 1.1 * Math.sqrt(Math.min(1, light[j] * 3)));
      const nc = c + step; if (nc < cost[j]) { cost[j] = nc; push(nc, j); }
    }
  }
  let maxc = 0; for (let i = 0; i < N; i++) if (sea[i] === 0 && cost[i] < 1e8) maxc = Math.max(maxc, cost[i]);
  const bytes = new Uint8Array(N * 4);
  for (let i = 0; i < N; i++) {
    const yr = sea[i] > 0 ? 2200 : cost[i] < 1e8 ? 2027 + Math.pow(cost[i] / maxc, 0.8) * 85 : 2110;   // land: 2027–2112 (Kardashev I)
    bytes[i * 4] = clamp((yr - 2026) / 128) * 255; bytes[i * 4 + 1] = sea[i] * 255; bytes[i * 4 + 2] = light[i] * 255; bytes[i * 4 + 3] = 255;
  }
  GROW = E.dataTexture(GW, GH, bytes);
}

/* ================= Earth helpers ================= */
function drawStars(k = 0.8) { E.drawParticles(SYS.stars, { uCenter: CAM.pos, uK: k }, { depth: true }); }
function earth(t, rot, o = {}) {
  const year = o.year ?? yearAt(t);
  E.sphere({ mode: 0, day: tex.earthDay, night: tex.earthNight, grow: GROW, center: EARTH, radius: 1, rot, sun: SUN_DIR_AT_EARTH, nightGain: o.nightGain ?? 1.5, dayGain: o.dayGain ?? 1.0,
    thermal: o.thermal || 0, heat: o.heat || 0, year, clouds: o.clouds ?? 0.55, atmo: [0.35, 0.6, 1.0], atmoK: 1.0, time: t, seaStart: 2100, seaEnd: 2191 });
}
// a point on the Earth's surface, in world space
const surf = (rot, lon, lat, h = 1) => add(EARTH, scl(toWorld(rot, ll(lon, lat)), h));

/* ================= 1. the word → 2. today, the colony (one continuous orbital shot) ================= */
// The camera stays on the night side; the Earth turns beneath it (Asia → Europe → the Americas), ending over Abilene, Texas.
const ABILENE = [-99.73, 32.45];
function nightShot(t) {
  const u = clamp((t - 6) / 24);
  const elev = lerp(28, ABILENE[1], ss(18, 30, t)) * D2R;
  const D = norm([Math.cos(elev), Math.sin(elev), 0.25]);
  const lon = lerp(118, ABILENE[0], ease(u));
  const rot = earthRot(D, lon);
  return { D, rot };
}
function sToday(t) {
  const { D, rot } = nightShot(t);
  let pos = add(EARTH, scl(D, lerp(2.7, 2.35, ss(7, 30, t)))), look = EARTH, fov = 36;
  if (t > 30) {   // the dive toward the campus
    const target = surf(rot, ABILENE[0], ABILENE[1]), u = ease(ss(30, 33, t));
    pos = mixv(pos, add(target, scl(norm(sub(target, EARTH)), 0.04)), u); look = mixv(EARTH, target, Math.min(1, u * 1.6)); fov = lerp(36, 50, u);
  }
  camera(pos, look, fov, 0.002, 20000); drawStars(0.8);
  earth(t, rot, { clouds: 0.25 });
  // the real data-centre regions flare in 2026
  const fl = ss(8, 9.5, t) * (1 - ss(13, 16, t));
  if (fl > 0) { for (const [lo, la] of DC_REGIONS) { const p = surf(rot, lo, la, 1.002); pt(p, [1, 0.6, 0.25], fl * (2.2 + 1.2 * Math.sin(t * 5 + lo)), 11); } flushPts({ depth: true }); }
}

/* ================= ground scenes: one ray-marched shader, four moods ================= */
let GROUND = null;
const GROUND_FS = `#version 300 es
precision highp float; in vec2 vUV; out vec4 o; uniform vec2 uRes;
uniform float uMode, uTime, uH, uPitch, uYaw, uLaunch, uStars, uFade, uHaze, uDomeLight, uFov;
float h21(vec2 p){ p = fract(p * vec2(123.34, 456.21)); p += dot(p, p + 45.32); return fract(p.x * p.y); }
float h31(vec3 p){ p = fract(p * 0.1031); p += dot(p, p.zyx + 31.32); return fract((p.x + p.y) * p.z); }
float n2(vec2 p){ vec2 i = floor(p), f = fract(p); f = f*f*(3.0-2.0*f); return mix(mix(h21(i), h21(i+vec2(1,0)), f.x), mix(h21(i+vec2(0,1)), h21(i+vec2(1,1)), f.x), f.y); }
float n3(vec3 p){ vec3 i = floor(p), f = fract(p); f = f*f*(3.0-2.0*f);
  return mix(mix(mix(h31(i), h31(i+vec3(1,0,0)), f.x), mix(h31(i+vec3(0,1,0)), h31(i+vec3(1,1,0)), f.x), f.y), mix(mix(h31(i+vec3(0,0,1)), h31(i+vec3(1,0,1)), f.x), mix(h31(i+vec3(0,1,1)), h31(i+vec3(1,1,1)), f.x), f.y), f.z); }
float fb(vec2 p){ float a = 0.5, s = 0.0; for (int i = 0; i < 5; i++) { s += a * n2(p); p = p * 2.02 + 7.3; a *= 0.5; } return s; }
float fb3(vec3 p){ float a = 0.5, s = 0.0; for (int i = 0; i < 4; i++) { s += a * n3(p); p = p * 2.03 + 7.3; a *= 0.5; } return s; }
vec2 vor(vec2 p){ vec2 i = floor(p), f = fract(p); float d1 = 9.0, d2 = 9.0; for (int y = -1; y <= 1; y++) for (int x = -1; x <= 1; x++) { vec2 g = vec2(x, y); vec2 c = g + vec2(h21(i + g), h21(i + g + 3.1)); float d = length(c - f); if (d < d1) { d2 = d1; d1 = d; } else if (d < d2) d2 = d; } return vec2(d1, d2); }
float sdBox(vec3 p, vec3 b){ vec3 q = abs(p) - b; return length(max(q, 0.0)) + min(max(q.x, max(q.y, q.z)), 0.0); }
float sdCap(vec3 p, vec3 a, vec3 b, float r){ vec3 pa = p - a, ba = b - a; float h = clamp(dot(pa, ba) / dot(ba, ba), 0.0, 1.0); return length(pa - ba * h) - r; }
const vec3 DOME = vec3(-8.0, 0.0, -52.0); const float DOME_R = 30.0;
// halls: rows of compute buildings receding to the horizon
float halls(vec3 p, out float id){
  float zStart = uMode < 0.5 ? -45.0 : -150.0;
  vec3 q = p; q.x = mod(p.x + 48.0, 96.0) - 48.0; float cz = floor((p.z + 32.0) / 64.0); q.z = mod(p.z + 32.0, 64.0) - 32.0;
  id = h21(vec2(floor((p.x + 48.0) / 96.0), cz));
  float hgt = 4.5 + 2.0 * id; float d = sdBox(q - vec3(0.0, hgt, 0.0), vec3(38.0, hgt, 15.0));
  vec3 r = q; r.x = mod(q.x + 4.0, 8.0) - 4.0; d = min(d, sdBox(r - vec3(0.0, 2.0 * hgt + 1.1, 0.0), vec3(2.4, 1.1, 10.0)) + step(36.0, abs(q.x)) * 100.0);
  d = max(d, p.z - zStart);
  if (uMode > 0.5) d = max(d, 70.0 - length(p.xz - DOME.xz));
  return d;
}
// the garden and its people, inside the dome
float garden(vec3 p){
  vec3 q = p - DOME; if (length(q) > DOME_R) return 1e3;
  float d = 1e3;
  for (int k = 0; k < 7; k++) { float fk = float(k); vec2 c = vec2(sin(fk * 2.4) * (8.0 + fk * 2.3), cos(fk * 2.4) * (6.0 + fk * 2.0)); float hgt = 7.0 + 4.0 * fract(fk * 0.37);
    d = min(d, length((q - vec3(c.x, hgt, c.y)) * vec3(1.0, 1.25, 1.0)) - (4.0 + 1.5 * fract(fk * 0.61)) - fb3(q * 0.6) * 1.2); d = min(d, sdCap(q, vec3(c.x, 0.0, c.y), vec3(c.x, hgt, c.y), 0.45)); }
  if (uMode > 0.5 && uMode < 1.5) for (int k = 0; k < 4; k++) { float fk = float(k); vec3 b = vec3(-7.0 + fk * 3.6, 0.0, 20.0 + fk * 1.2); d = min(d, sdCap(q, b + vec3(0, 0.45, 0), b + vec3(0, 1.45, 0), 0.24)); d = min(d, length(q - b - vec3(0, 1.75, 0)) - 0.13); }
  return d;
}
float figures(vec3 p){ if (uMode < 1.5 || uMode > 2.5) return 1e3; float d = 1e3; for (int k = 0; k < 2; k++) { vec3 b = vec3(6.0 + float(k) * 1.15, 0.0, 18.0 - float(k) * 0.7); float s = 1.0 - float(k) * 0.08;
    d = min(d, sdCap(p, b + vec3(-0.1, 0.05, 0), b + vec3(-0.08, 0.86, 0) * s, 0.075)); d = min(d, sdCap(p, b + vec3(0.1, 0.05, 0), b + vec3(0.08, 0.86, 0) * s, 0.075));
    d = min(d, sdCap(p, b + vec3(0, 0.95, 0) * s, b + vec3(0.02, 1.4, 0.0) * s, 0.17)); d = min(d, length(p - b - vec3(0.05, 1.64, 0.06) * s) - 0.11 * s);
    d = min(d, sdCap(p, b + vec3(-0.2, 1.38, 0) * s, b + vec3(-0.26, 0.92, 0.02) * s, 0.05)); d = min(d, sdCap(p, b + vec3(0.2, 1.38, 0) * s, b + vec3(0.26, 0.92, 0.02) * s, 0.05)); } return d; }
float scene(vec3 p, out float mat, out float id){
  float hid; float dh = halls(p, hid); float dg = uMode > 0.5 ? garden(p) : 1e3; float dgr = p.y;
  float d = dgr; mat = 0.0; id = 0.0;
  if (dh < d) { d = dh; mat = 1.0; id = hid; }
  if (dg < d) { d = dg; mat = 2.0; }
  float df = figures(p); if (df < d) { d = df; mat = 3.0; }
  return d;
}
vec3 skyCol(vec3 rd, vec3 moonDir, vec3 sunDir){
  float e = max(rd.y, 0.0); vec3 c;
  if (uMode < 0.5) { c = mix(vec3(0.07, 0.045, 0.028), vec3(0.004, 0.006, 0.013), pow(e, 0.4)); }
  else if (uMode < 1.5) { c = mix(vec3(0.66, 0.66, 0.64), vec3(0.42, 0.45, 0.5), pow(e, 0.6)); }
  else if (uMode < 2.5) { c = mix(vec3(0.035, 0.038, 0.048), vec3(0.003, 0.004, 0.009), pow(e, 0.5)); float dm = acos(clamp(dot(rd, moonDir), -1.0, 1.0)); c += vec3(0.7, 0.78, 0.92) * (0.18 * exp(-dm * 14.0) + 0.04 * exp(-dm * 2.5)); c += vec3(1.0, 0.98, 0.95) * 30.0 * smoothstep(0.0105, 0.0095, dm);
    float ds = acos(clamp(dot(rd, sunDir), -1.0, 1.0)); c = mix(c, vec3(0.62, 0.14, 0.045) * 1.4, smoothstep(0.0125, 0.0115, ds)); c += vec3(0.9, 0.3, 0.08) * 0.06 * exp(-ds * 30.0); }
  else { c = mix(vec3(0.012, 0.014, 0.02), vec3(0.002, 0.003, 0.006), pow(e, 0.5)); }
  // stars (night moods)
  if ((uMode < 0.5 || uMode > 2.5) && rd.y > 0.0) { vec3 sp = rd * 260.0; vec3 cell = floor(sp); float hs = h31(cell); vec3 cc = cell + vec3(h31(cell + 1.3), h31(cell + 2.9), h31(cell + 4.7));
    float on = uMode > 2.5 ? step(h31(cell + 9.1), uStars) : step(0.6, hs); float s = step(0.965, hs) * on * smoothstep(0.08, 0.0, length(sp - cc)); c += vec3(0.9, 0.93, 1.0) * s * (0.6 + 4.0 * pow(hs, 30.0)) * smoothstep(0.0, 0.2, rd.y); }
  // satellite trains over the campus
  if (uMode < 0.5 && rd.y > 0.05) { vec2 sk = vec2(atan(rd.x, -rd.z), rd.y);
    for (int k = 0; k < 7; k++) { float fk = float(k); vec2 a = vec2(-1.3 + h21(vec2(fk, 1.0)) * 0.7, 0.25 + h21(vec2(fk, 2.0)) * 0.5); vec2 dd = normalize(vec2(1.0, (h21(vec2(fk, 3.0)) - 0.5) * 0.4));
      vec2 head = a + dd * mod(uTime * (0.035 + 0.02 * h21(vec2(fk, 4.0))) + fk * 0.37, 2.6); vec2 rel = sk - head; float al = dot(rel, -dd), ac = dot(rel, vec2(-dd.y, dd.x));
      float idx = clamp(floor(al / 0.009 + 0.5), 0.0, 26.0); c += vec3(0.95, 0.97, 1.0) * smoothstep(0.0016, 0.0, length(vec2(al - idx * 0.009, ac))) * step(-0.004, al) * 1.3; } }
  return c;
}
void main(){
  vec2 ndc = vUV * 2.0 - 1.0; float asp = uRes.x / uRes.y; float tf = tan(uFov * 0.5);
  vec3 ro = vec3(0.0, uH, 40.0);
  vec3 fw = normalize(vec3(sin(uYaw) * cos(uPitch), sin(uPitch), -cos(uYaw) * cos(uPitch))); vec3 rt = normalize(cross(fw, vec3(0, 1, 0))); vec3 up = cross(rt, fw);
  vec3 rd = normalize(fw + ndc.x * tf * asp * rt + ndc.y * tf * up);
  vec3 moonDir = normalize(vec3(0.42, 0.62, -1.0)), sunDir = normalize(vec3(-0.75, 0.3, -1.0));
  vec3 light = uMode < 0.5 ? vec3(0.0) : uMode < 1.5 ? normalize(vec3(0.3, 1.0, 0.2)) : uMode < 2.5 ? moonDir : vec3(0.0, 1.0, 0.0);
  vec3 lightC = uMode < 0.5 ? vec3(0.0) : uMode < 1.5 ? vec3(0.95, 0.95, 0.92) : uMode < 2.5 ? vec3(0.2, 0.22, 0.28) : vec3(0.01, 0.012, 0.016);
  vec3 ambient = uMode < 0.5 ? vec3(0.012, 0.01, 0.009) : uMode < 1.5 ? vec3(0.42, 0.43, 0.44) : uMode < 2.5 ? vec3(0.025, 0.028, 0.036) : vec3(0.004, 0.005, 0.007);
  vec3 fogC = uMode < 0.5 ? vec3(0.05, 0.035, 0.025) : uMode < 1.5 ? vec3(0.66, 0.66, 0.64) : uMode < 2.5 ? vec3(0.03, 0.033, 0.042) : vec3(0.008, 0.01, 0.014);
  // march the opaque world
  float t = 0.0, mat = -1.0, id = 0.0; bool hit = false;
  if (rd.y < 0.25 || uH > 30.0) for (int i = 0; i < 140; i++) { vec3 p = ro + rd * t; float m, idd; float d = scene(p, m, idd); if (d < 0.002 * t + 0.01) { hit = true; mat = m; id = idd; break; } t += d * 0.9; if (t > 6000.0) break; }
  vec3 col;
  if (hit) {
    vec3 p = ro + rd * t; vec2 e = vec2(0.02 * (1.0 + t * 0.002), 0.0); float m2, id2;
    vec3 n = normalize(vec3(scene(p + e.xyy, m2, id2) - scene(p - e.xyy, m2, id2), scene(p + e.yxy, m2, id2) - scene(p - e.yxy, m2, id2), scene(p + e.yyx, m2, id2) - scene(p - e.yyx, m2, id2)));
    vec3 alb; vec3 emit = vec3(0.0);
    if (mat < 0.5) {   // ground
      if (uMode < 0.5) { alb = mix(vec3(0.05, 0.05, 0.05), vec3(0.12, 0.11, 0.1), fb(p.xz * 0.05)); }
      else { vec2 v = vor(p.xz * 0.12); float crack = smoothstep(0.05, 0.0, v.y - v.x); alb = mix(vec3(0.55, 0.52, 0.47), vec3(0.72, 0.69, 0.63), fb(p.xz * 0.03)) * (1.0 - crack * 0.55);
        if (length(p.xz - DOME.xz) < DOME_R) alb = vec3(0.12, 0.22, 0.08) * (0.7 + 0.6 * fb(p.xz * 0.5)); }
    } else if (mat < 1.5) {  // halls
      alb = uMode < 0.5 ? vec3(0.07, 0.07, 0.075) : uMode < 1.5 ? vec3(0.62, 0.62, 0.64) : vec3(0.3, 0.3, 0.32);
      vec3 lq = p; lq.x = mod(p.x + 48.0, 96.0) - 48.0; lq.z = mod(p.z + 32.0, 64.0) - 32.0;
      float lamp = smoothstep(0.35, 0.0, length(vec2(mod(lq.x + 6.0, 12.0) - 6.0, p.y - 6.0))) * step(0.5, abs(n.z));   // wall lights every 12 m
      float night = uMode < 0.5 || uMode > 1.5 ? 1.0 : 0.0;
      emit += vec3(1.0, 0.72, 0.42) * lamp * 3.0 * night * (uMode > 2.5 ? 0.6 : 1.0);
      float blink = step(0.55, fract(uTime * 0.6 + id * 7.0)); float corner = smoothstep(1.5, 0.0, length(vec2(abs(lq.x) - 37.0, abs(lq.z) - 14.0))) * step(0.85, n.y);
      emit += vec3(1.0, 0.06, 0.03) * corner * blink * night * 8.0;
    } else if (mat > 2.5) { alb = vec3(0.02); emit = vec3(0.0);
    } else {   // garden
      alb = vec3(0.07, 0.16, 0.05) * (0.7 + 0.6 * fb3(p * 0.5)); if (p.y < 2.2 && length(p.xz - DOME.xz) < 26.0 && uMode > 0.5 && uMode < 1.5) alb = vec3(0.06, 0.05, 0.05);
      emit += vec3(1.0, 0.72, 0.42) * 0.05 * uDomeLight;
    }
    float dif = max(dot(n, light), 0.0); float sky = 0.5 + 0.5 * n.y;
    col = alb * (lightC * dif + ambient * sky) + emit;
    if (mat > 1.5) col += alb * vec3(1.0, 0.75, 0.45) * 0.6 * uDomeLight;
    float fog = 1.0 - exp(-t * (uMode < 1.5 && uMode > 0.5 ? 0.0011 : 0.0007));
    col = mix(col, fogC, fog);
  } else col = skyCol(rd, moonDir, sunDir);
  // steam columns, with volume (day and two-suns moods)
  if (uMode > 0.5 && uMode < 2.5) {
    float tmax = hit ? t : 9000.0; vec3 acc = vec3(0.0); float tr = 1.0;
    for (int k = 0; k < 3; k++) { float fk = float(k); vec3 c0 = vec3(-900.0 + fk * 950.0, 0.0, -2600.0 - fk * 700.0); float rad = 55.0 + fk * 20.0;
      vec2 oc = ro.xz - c0.xz; float b = dot(oc, rd.xz), cc = dot(oc, oc) - (rad * 3.0) * (rad * 3.0), a2 = dot(rd.xz, rd.xz); float disc = b * b - a2 * cc; if (disc < 0.0) continue;
      float t0 = max((-b - sqrt(disc)) / a2, 0.0), t1 = min((-b + sqrt(disc)) / a2, tmax); if (t1 <= t0) continue;
      for (int j = 0; j < 14; j++) { float tt = mix(t0, t1, (float(j) + 0.5) / 14.0); vec3 p = ro + rd * tt; float hgt = p.y; if (hgt < 0.0) continue; float r = rad * (1.0 + hgt / 900.0);
        float dd = length(p.xz - c0.xz - vec2(sin(hgt * 0.002 + fk) * 120.0, 0.0)); float den = smoothstep(r, r * 0.3, dd) * smoothstep(5200.0, 600.0, hgt) * (0.5 + fb3(vec3(p.xz * 0.004, hgt * 0.003 - uTime * 0.15)));
        float a = den * (t1 - t0) / 14.0 * 0.0045; acc += tr * a * (uMode < 1.5 ? vec3(0.92, 0.93, 0.94) : vec3(0.28, 0.3, 0.34)); tr *= 1.0 - a; } }
    col = col * tr + acc;
  }
  // the dome: reflection and tint over whatever lies behind the glass
  if (uMode > 0.5) { vec3 oc = ro - DOME; float b = dot(oc, rd), c = dot(oc, oc) - DOME_R * DOME_R, h = b * b - c;
    if (h > 0.0) { float tg = -b - sqrt(h); vec3 p = ro + rd * tg; if (tg > 0.0 && p.y > 0.0 && (!hit || tg < t)) { vec3 n = normalize(p - DOME); float fr = pow(1.0 - max(dot(-rd, n), 0.0), 4.0); vec3 refl = skyCol(reflect(rd, n), moonDir, sunDir);
      float frame = max(smoothstep(0.02, 0.0, abs(fract(atan(n.z, n.x) / 3.14159 * 18.0) - 0.5) - 0.48), smoothstep(0.02, 0.0, abs(fract(asin(n.y) / 1.5708 * 7.0) - 0.5) - 0.48));
      col = mix(col * vec3(0.8, 0.86, 0.9), refl, 0.18 + 0.8 * fr) + vec3(0.6, 0.62, 0.66) * frame * (uMode < 1.5 ? 0.35 : 0.08);
      if (uMode > 2.5) col += vec3(0.4) * smoothstep(0.004, 0.0, abs(fb(n.xz * 9.0) - 0.5)) * 0.03; } } }
  // the launch over the campus: a rising flame and its trail
  if (uMode < 0.5 && uLaunch > 0.0) { vec3 base = vec3(380.0, 0.0, -2300.0); vec3 rk = base + vec3(-120.0 * uLaunch, 9000.0 * pow(uLaunch, 1.6), 0.0);
    vec3 w = rk - ro; float tc = max(dot(w, rd), 0.0); float dist = length(w - rd * tc) / max(tc, 1.0); col += vec3(1.0, 0.9, 0.7) * 22.0 * smoothstep(0.0022, 0.0, dist) * step(0.0, rk.y);
    col += vec3(1.0, 0.7, 0.4) * 0.6 * exp(-dist * 300.0);
    for (int j = 0; j < 28; j++) { float f = (float(j) + 0.5) / 28.0; vec3 q = mix(base, rk, f); vec3 wq = q - ro; float tq = max(dot(wq, rd), 1.0); float dq = length(wq - rd * tq) / tq;
      col += vec3(1.0, 0.72, 0.42) * 0.11 * smoothstep(0.003, 0.0, dq) * f * f; }
    col += vec3(0.5, 0.3, 0.15) * 0.12 * uLaunch * exp(-max(acos(clamp(dot(rd, normalize(base - ro)), -1.0, 1.0)), 0.0) * 6.0); }
  col = mix(col, uMode < 0.5 ? vec3(0.02, 0.025, 0.04) : vec3(0.75, 0.77, 0.8), uHaze);
  o = vec4(col * uFade, 0.0);
}`;
function ground(mode, t, cam) {
  E.camera([0, 0, 0], [0, 0, -1], [0, 1, 0], 40);
  if (!GROUND) GROUND = E.program(GROUND_FS);
  E.fullscreen(GROUND, { uMode: mode, uTime: t, uH: cam.h, uPitch: cam.pitch, uYaw: cam.yaw || 0, uLaunch: cam.launch || 0, uStars: cam.stars ?? 1, uFade: cam.fade ?? 1, uHaze: cam.haze || 0, uDomeLight: cam.domeLight ?? 1, uFov: (cam.fov || 50) * D2R });
}
function sCampus(t) {   // 0:33–0:41: descend to the campus, a launch rises, the camera follows it up
  const d = ss(33, 35, t), launch = ss(35.2, 41, t);
  ground(0, t, { h: lerp(420, 1.8, ease(d)), pitch: d < 1 ? lerp(-1.1, 0.04, ease(d)) : lerp(0.04, 1.1, ease(ss(36.5, 40.8, t))), yaw: 0.12, launch, haze: (1 - ss(33, 34.2, t)) * 0.9 + ss(40.6, 41, t) * 0.9, fov: 52 });
}
function sDome(t) {   // 1:12–1:24: descend into the dried basin; the dome; tilt up into the white sky
  const d = ss(72, 74.6, t);
  ground(1, t, { h: lerp(650, 1.8, ease(d)), pitch: t < 82.5 ? lerp(-1.2, 0.07, ease(d)) : lerp(0.07, 1.35, ease(ss(82.5, 84.4, t))), yaw: lerp(0.05, -0.04, ss(74, 82, t)), haze: (1 - ss(72, 73.3, t)) * 0.95 + ss(83.8, 84.5, t), fov: 50, domeLight: 1 });
}
function sTwoSuns(t) {  // 2:18–2:24
  ground(2, t, { h: 1.7, pitch: 0.2, yaw: 0.1, fade: ss(138, 138.4, t) * (1 - ss(143.6, 144, t)), fov: 56, domeLight: 1 });
}
function sLastSky(t) {  // 3:16–3:23: the stars go out; the camera tilts up into the black
  ground(3, t, { h: 1.7, pitch: t < 200.6 ? 0.22 : lerp(0.22, 1.5, ease(ss(200.6, 202, t))), yaw: 0.0, stars: 1 - ss(196.2, 200.4, t), fade: ss(195, 195.5, t) * (1 - ss(201.4, 202, t)), fov: 60, domeLight: 0 });
}

/* ================= 0:41–1:12 orbit, thermal, the oceans (one continuous orbital camera) ================= */
function orbitRot(t) { return earthRot([0, 0, 1], lerp(-95, 18, ss(41, 70, t))); }
let PLUME = null;
const PLUME_FS = `#version 300 es
precision highp float; in vec2 vUV; out vec4 o; uniform vec2 uRes; uniform float uTime, uN; uniform vec4 uJ[24]; uniform vec4 uK[24];
float h21(vec2 p){ p = fract(p * vec2(123.34, 456.21)); p += dot(p, p + 45.32); return fract(p.x * p.y); }
float n2(vec2 p){ vec2 i = floor(p), f = fract(p); f = f*f*(3.0-2.0*f); return mix(mix(h21(i), h21(i+vec2(1,0)), f.x), mix(h21(i+vec2(0,1)), h21(i+vec2(1,1)), f.x), f.y); }
float fb(vec2 p){ float a = 0.5, s = 0.0; for (int i = 0; i < 5; i++) { s += a * n2(p); p = p * 2.03 + 7.3; a *= 0.5; } return s; }
void main(){ vec2 px = vUV * uRes; vec3 col = vec3(0.0);
  for (int i = 0; i < 24; i++) { if (float(i) >= uN) break; vec4 J = uJ[i], K = uK[i]; if (J.w < 1.0) continue;
    vec2 d = vec2(cos(J.z), sin(J.z)); vec2 rel = px - J.xy; float a = dot(rel, d); float c = dot(rel, vec2(-d.y, d.x)); if (a < -10.0 || a > J.w * 1.25) continue;
    float u = a / J.w; float w = K.x * (0.3 + 2.2 * u); float turb = fb(vec2(a * 0.018 - uTime * 2.2 + K.z * 13.0, c * 0.03 / (0.3 + u) + K.z * 7.0));
    col += vec3(0.86, 0.91, 1.0) * exp(-pow(c / w, 2.0) * 1.3) * (0.35 + turb) * smoothstep(-0.02, 0.05, u) * (1.0 - smoothstep(0.5, 1.2, u)) * (1.0 - 0.4 * u) * K.y; }
  o = vec4(col, 0.0); }`;
const JETS = (() => { const r = rngOf(29), j = []; for (let i = 0; i < 20; i++) j.push({ u: r(), h: (r() - 0.5) * 1.5, ph: r(), v: 0.7 + r() * 0.5, w: r() }); return j; })();
const MEDIT = [18, 35];
function sOrbital(t) {
  const rot = orbitRot(t);
  // camera keyframes around the Earth: terminator view → thermal → limb over the Atlantic and Mediterranean → dive into the dried Mediterranean
  const k = [[41, [-0.6, 0.55, 2.3], [0, 0, 0], 38], [50, [-1.1, 0.75, 2.05], [0, 0.1, 0], 38], [59, [-1.45, 0.6, 1.6], [0, 0.15, 0], 38], [66, [-1.7, 0.5, 0.9], [0.1, 0.25, 0.55], 36], [70, [-1.55, 0.6, 0.75], [0.1, 0.3, 0.6], 36]];
  let { pos, look, fov } = camPath(k, t); pos = add(EARTH, pos); look = add(EARTH, look);
  if (t > 70) { const target = surf(rot, MEDIT[0], MEDIT[1]), u = ease(ss(70, 72, t)); pos = mixv(pos, add(target, scl(norm(sub(target, EARTH)), 0.03)), u); look = mixv(look, target, Math.min(1, u * 1.5)); fov = lerp(fov, 50, u); }
  camera(pos, look, fov, 0.002, 20000); drawStars(0.7);
  const year = yearAt(t), thermal = ss(50, 51.2, t) * (1 - ss(59, 60.2, t));
  earth(t, rot, { thermal, heat: clamp((year - 2050) / 55), clouds: lerp(0.55, 0.25, thermal) });
  E.drawParticles(SYS.orbit, { uCenter: EARTH, uYear: year, uT: t, uSunDir: SUN_DIR_AT_EARTH, uK: 1 - thermal * 0.85 }, { depth: true });
  // the rocket from the campus, climbing to join the shells
  if (t < 45.5) { const base = surf(rot, ABILENE[0], ABILENE[1], 1.0), up = norm(sub(base, EARTH)), side = norm(cross(up, [0, 1, 0])), u = ss(41, 45.5, t);
    const p = add(add(base, scl(up, 0.08 * Math.sin(u * Math.PI / 2))), scl(side, u * 0.35)); pt(p, [1, 0.9, 0.7], 8 * (1 - ss(44.5, 45.5, t)), 14); for (let i = 1; i < 30; i++) { const v = u * (1 - i / 30); pt(add(add(base, scl(up, 0.08 * Math.sin(v * Math.PI / 2))), scl(side, v * 0.35)), [1, 0.7, 0.4], 0.5 * (1 - i / 30), 5); } flushPts({ depth: true }); }
  // seawater vented to space, seen in profile along the limb
  const on = ss(60, 62, t) * (1 - ss(71.5, 72, t));
  if (on > 0) {
    if (!PLUME) PLUME = E.program(PLUME_FS);
    const cd = norm(sub(pos, EARTH)), ex = norm(cross([0, 1, 0], cd)), ey = cross(cd, ex), J = [], K = [];
    for (const j of JETS) { const ang = -1.2 + j.u * 2.6, rim = norm(add(add(scl(ex, Math.cos(ang)), scl(ey, Math.sin(ang))), scl(cd, 0.06 + 0.04 * j.h)));
      const hMax = (0.16 + 0.26 * j.v) * ss(60 + j.ph * 3, 63.5 + j.ph * 3, t); const p0 = E.project(add(EARTH, rim)), p1 = E.project(add(EARTH, scl(rim, 1 + hMax))); if (!p0 || !p1) continue;
      const dx = p1[0] - p0[0], dy = -(p1[1] - p0[1]); J.push(p0[0], H - p0[1], Math.atan2(dy, dx), Math.hypot(dx, dy)); K.push(9 + 14 * j.w, on * (0.35 + 0.35 * j.w), j.ph, 0); }
    while (J.length < 96) { J.push(0, 0, 0, 0); K.push(0, 0, 0, 0); }
    E.fullscreen(PLUME, { uTime: t, uN: 24, uJ: J, uK: K });
  }
}

/* ================= 1:24–2:18 Earth entire, then one flight through the solar system ================= */
function solarRot(t) { return earthRot(norm([0.2, 0.6, 1]), lerp(10, 40, ss(84, 98, t))); }
const SOLAR_KEYS = () => [
  [84.5, add(EARTH, [0.25, 1.3, 0.4]), EARTH, 44],
  [92, add(EARTH, [1.4, 2.2, 4.0]), EARTH, 36],
  [94.5, add(EARTH, [-5, 2.0, 6]), add(EARTH, [-30, 0, 2]), 40],
  [96.6, add(VEN, [6, 1.4, 4]), VEN, 40],
  [98.6, add(MERC, [-1.3, 0.45, 1.3]), MERC, 36],
  [111.2, add(MERC, [-1.75, 0.55, 0.9]), MERC, 36],
  [113.6, add(VEN, [-2.6, 0.7, 1.5]), VEN, 36],
  [117.5, add(VEN, [-2.9, 0.8, 1.1]), VEN, 36],
  [121, [40, 70, 175], [0, -6, 0], 40],
  [131.5, [55, 48, 120], [0, -4, 0], 36],
  [134.5, add(MOON, [8, 3, 14]), MOON, 34],
  [138, add(MOON, [1.2, 0.35, 1.5]), add(MOON, [-1.5, -0.2, -1.2]), 40],
];
let SKEYS = null;
function sSolar(t) {
  if (!SKEYS) SKEYS = SOLAR_KEYS();
  let { pos, look, fov } = camPath(SKEYS, t);
  const dE = len(sub(pos, EARTH)), near = Math.max(0.002, Math.min(dE, len(sub(pos, MERC)), len(sub(pos, VEN)), len(sub(pos, MOON))) * 0.02);
  camera(pos, look, fov, near, 30000); drawStars(0.85);
  // the Sun and its swarm
  const swarmFill = ss(119, 130, t), ir = ss(127.5, 129.5, t);
  E.sphere({ mode: 2, center: SUN, radius: SUN_R, emissive: lerp(lerp(3.0, 0.7, swarmFill), 0.55, ir), ir, atmo: ir < 0.5 ? [1.0, 0.72, 0.42] : [0.7, 0.08, 0.03], time: t });
  E.drawParticles(SYS.swarm, { uCenter: SUN, uT: t, uIR: ir, uR: SUN_R, uK: 1 }, { depth: true });
  E.drawParticles(SYS.debris, { uT: t, uM: [len(MERC), Math.atan2(MERC[2], MERC[0]), 108.5, 0], uV: [len(VEN), Math.atan2(VEN[2], VEN[0]), 116, 0], uSwarmR: SUN_R }, { depth: true });
  // the Earth, wrapped and dried
  const rot = solarRot(t);
  earth(t, rot, { clouds: 0.3 });
  E.drawParticles(SYS.orbit, { uCenter: EARTH, uYear: yearAt(t), uT: t, uSunDir: SUN_DIR_AT_EARTH, uK: 1.2 }, { depth: true });
  // the Moon; it blazes when the relay beam arrives
  const hit = ss(132.4, 134.6, t), blaze = ss(134.4, 136.5, t);
  E.sphere({ mode: 1, day: tex.moon, center: MOON, radius: MOON_R, sun: norm(sub(SUN, MOON)), dayGain: 1.3 + blaze * 9, tint: [1, 0.98, 0.95], time: t });
  if (t > 132.2) { const src = add(SUN, scl(norm(sub(MOON, SUN)), SUN_R * 1.6)), dst = add(MOON, scl(norm(sub(SUN, MOON)), MOON_R)); const head = mixv(src, dst, hit);
    ln(src, head, [1.0, 0.95, 0.85], 5.5 * (0.85 + 0.15 * Math.sin(t * 40)), 2.2); flushLns({ depth: true }); if (hit >= 1) { pt(dst, [1, 0.97, 0.9], 25 * blaze, 50); flushPts({ depth: false }); } }
  // Mercury: the scar, the mass drivers, the unravelling
  const mR = MERC_R * (1 - 0.4 * ss(107.5, 110.5, t)), mOp = 1 - ss(109.5, 111, t);
  if (mOp > 0) {
    const lesC = norm([-0.75, 0.35, 0.55]);
    E.sphere({ mode: 1, day: tex.mercury, center: MERC, radius: mR, sun: norm(sub(SUN, MERC)), desat: 0.82, tint: [1.0, 0.97, 0.92], dayGain: 1.5, lesC, lesR: 2.4 * ss(100, 108, t), lesK: 1.2, opacity: mOp, time: t });
    const lesR = 2.4 * ss(100, 108, t);
    if (lesR > 0.15) { const ax = norm(cross(lesC, [0, 1, 0])), ay = cross(ax, lesC);
      for (let m = 0; m < 34; m++) { const a = m * 2.39996, ang = Math.min(lesR * 0.92, 2.2), dir = add(scl(ax, Math.cos(a)), scl(ay, Math.sin(a))); const p = norm(add(scl(lesC, Math.cos(ang)), scl(dir, Math.sin(ang)))); const tang = norm(sub(scl(p, dot(lesC, p)), lesC));
        const s0 = add(MERC, scl(p, mR * 1.003)); for (let k = 0; k < 22; k++) { const age = ((t * 0.5 * (0.6 + (m % 5) * 0.12) + m * 0.137 + k / 22) % 1); pt(add(add(s0, scl(tang, mR * (0.3 + age * 3.5))), scl(p, mR * age * age * 2)), [1, 0.7, 0.4], (1.6 * (1 - age) + 0.2) * mOp, 3); } }
      flushPts({ depth: true }); }
  }
  // Venus: the scar tears the clouds
  const vR = VEN_R * (1 - 0.35 * ss(116, 118, t)), vOp = 1 - ss(117.2, 118.4, t);
  if (vOp > 0) E.sphere({ mode: 3, center: VEN, radius: vR, sun: norm(sub(SUN, VEN)), dayGain: 0.95, lesC: norm([-0.85, 0.3, 0.45]), lesR: 2.5 * ss(113.6, 117.4, t), lesK: 1.4, atmo: [1.0, 0.9, 0.7], atmoK: 0.6, opacity: vOp, time: t });
}

/* ================= 2:24–2:54 launch, the probe we follow, the cell ================= */
const PROBES = (() => { const r = rngOf(73), p = []; for (let i = 0; i < 3000; i++) { const z = r() * 2 - 1, a = r() * TAU, q = Math.sqrt(1 - z * z); p.push({ d: [q * Math.cos(a), z * 0.6, q * Math.sin(a)], tl: 144.2 + r() * 3.2, v: 0.6 + r() * 0.8 }); } return p; })();
const FOLLOW = norm([0.45, 0.18, 1]);
function sLaunch(t) {
  // the swarm, the probes leaving; at 147.5 the camera latches on to one probe and rides it out
  const ride = ss(147, 148.5, t), flyT = Math.max(0, t - 147);
  const probePos = scl(FOLLOW, SUN_R * 2.2 + 60 * flyT * flyT);
  let pos = mixv(add(SUN, [30, 22, 70]), add(probePos, add(scl(FOLLOW, -4), [0, 1.2, 0])), ease(ride)), look = mixv(SUN, add(probePos, scl(FOLLOW, 10)), ease(ride));
  camera(pos, look, 40, 0.05, 40000); drawStars(0.85);
  E.sphere({ mode: 2, center: SUN, radius: SUN_R, emissive: 0.55, ir: 1, atmo: [0.7, 0.08, 0.03], time: t });
  E.drawParticles(SYS.swarm, { uCenter: SUN, uT: 200, uIR: 1, uR: SUN_R, uK: 1 }, { depth: true });
  for (const pr of PROBES) { if (t < pr.tl) continue; const u = t - pr.tl, r0 = SUN_R * 2 + pr.v * 30 * u * u * (1 + u * u); const a = scl(pr.d, r0), b = scl(pr.d, r0 * 0.94); ln(b, a, AMBER, 2.0, 1.0); }
  pt(probePos, [1, 0.85, 0.6], t > 147 ? 8 : 0, 10); flushLns({ depth: true }); flushPts({ depth: true });
}
// transit: riding the probe between the stars
const NEAR = (() => { const r = rngOf(79), n = 6000, d = new Float32Array(n * 8); for (let i = 0; i < n; i++) d.set([(r() - 0.5) * 400, (r() - 0.5) * 200, r() * 4000, 0.4 + Math.pow(r(), 4) * 3, r(), 0, 0, 0], i * 8); return d; })();
function sTransit(t) {
  camera([0, 0, 0], [0, 0, 1], 40, 0.05, 40000); drawStars(0.6);
  const u = ss(149, 154.5, t), z0 = 3800 * u; const speed = Math.sin(u * Math.PI);
  for (let i = 0; i < 6000; i++) { const x = NEAR[i * 8], y = NEAR[i * 8 + 1], z = NEAR[i * 8 + 2] - z0; if (z < 2 || z > 3000) continue; const tail = 40 * speed + 1; ln([x, y, z + tail], [x, y, z], [0.85, 0.9, 1.0], NEAR[i * 8 + 3] * 0.5, 1.2); }
  flushLns({ depth: false });
  pt([0.6, -0.35, 4], [1, 0.85, 0.6], 6, 9); flushPts({ depth: false });
}
const CELL_STAR = [-12, 5, 5.5];
function sCell(t) {
  const back = ss(166.5, 171, t);            // the pull-back that hands over to the galaxy
  const e = ease(ss(163.5, 167, t));
  let look = [lerp(-0.6, CELL_STAR[0] * 0.8, e), lerp(0.2, CELL_STAR[1] * 0.8, e), lerp(0, CELL_STAR[2] * 0.8, e)];
  let pos = [lerp(1.8, 3.0, e), lerp(0.8, 1.8, e), lerp(4.4, 6.5, e)];
  if (back > 0) { const dir = norm(sub(pos, CELL_STAR)); const d0 = len(sub(pos, CELL_STAR)); pos = add(CELL_STAR, scl(dir, d0 * Math.pow(400, ease(back)))); look = CELL_STAR; }
  camera(pos, look, 40, 0.01, 1e6); drawStars(0.9 * (1 - back));
  const sun = norm(CELL_STAR), dim = ss(166, 170, t);
  E.sphere({ mode: 2, center: CELL_STAR, radius: 1.4, emissive: lerp(3.0, 0.02, dim), atmo: [1.0, 0.8, 0.5], time: t });
  const R = 1 - 0.4 * ss(163, 166, t), op = 1 - ss(165, 166.5, t);
  const rot = bodyRot(2.0, 0.25), faceW = norm([-0.33, 0.36, 0.88]), lesC = toBody(rot, faceW);
  if (op > 0) E.sphere({ mode: 1, day: tex.moon, radius: R, sun, desat: 0.2, tint: [1.15, 0.72, 0.5], dayGain: 1.6 * (1 - dim * 0.9), lesC, lesR: 2.6 * ss(158.5, 164, t), lesK: 1.3, rot, opacity: op, time: t });
  const land = scl(faceW, 1.0);
  if (t < 159) { const u = ease(ss(154, 158.5, t)); const from = [2.6, 2.2, 1.0]; const p = mixv(from, scl(land, 1.01), u);
    pt(p, [1, 0.85, 0.6], 6, 8); pt(p, [0.6, 0.75, 1.0], 1.6 * (1 - ss(157, 158.5, t)), 40); if (t > 158.5) pt(land, [1, 0.7, 0.4], 20 * (1 - ss(158.5, 159, t)), 30); }
  const ringK = ss(163, 167, t), coll = ss(165, 168, t);
  if (ringK > 0) { const r = rngOf(97); for (let i = 0; i < 14000; i++) { const a = r() * TAU, rr = 1.3 + r() * 1.2; if (r() > ringK) continue; const ang = a + t * 0.08 / rr; const local = [Math.cos(ang) * rr, gauss(r) * 0.04 + Math.sin(ang) * rr * 0.1, Math.sin(ang) * rr];
    const toward = clamp((coll - r() * 0.5) * 2); const target = add(CELL_STAR, scl(norm([Math.cos(ang * 3 + i), (r() - 0.5) * 1.4, Math.sin(ang * 3 + i)]), 1.9 + r() * 0.6));
    pt(mixv(local, target, toward), toward > 0.98 ? [lerp(1, 0.7, dim), lerp(0.7, 0.1, dim), lerp(0.4, 0.04, dim)] : [1, 0.62, 0.3], (0.6 + toward * 0.4) * (1 - dim * 0.6), 1.8); } }
  flushPts({ depth: true });
  return back;
}

/* ================= 2:52–4:40 the galaxy ================= */
let GAL = null;
function buildGalaxy() {
  const r = rngOf(53), n = 190000, pos = new Float32Array(n * 3), col = new Float32Array(n * 3), b = new Float32Array(n), dom = new Uint16Array(n), seam = new Float32Array(n);
  for (let i = 0; i < n; i++) {
    let x, y, z, c;
    if (i < 34000) { x = gauss(r) * 4.2; z = gauss(r) * 3.6; y = gauss(r) * 1.5; c = [1.0, 0.86, 0.62]; }
    else { const arm = i % 2, rr = 3 + -Math.log(1 - r() * 0.985) * 12; const th = arm * Math.PI + Math.log(rr / 3) / Math.tan(13 * D2R) + gauss(r) * 0.22; x = rr * Math.cos(th) + gauss(r) * 1.1; z = rr * Math.sin(th) + gauss(r) * 1.1; y = gauss(r) * 0.35; const hot = r(); c = hot < 0.2 ? [0.7, 0.8, 1.0] : hot < 0.75 ? [1.0, 0.95, 0.88] : [1.0, 0.8, 0.6]; }
    pos.set([x, y, z], i * 3); col.set(c, i * 3); b[i] = 0.25 + Math.pow(r(), 4) * 2.5;
  }
  const ND = 212, cen = []; for (let k = 0; k < ND; k++) { const i = Math.floor(r() * n); cen.push([pos[i * 3], pos[i * 3 + 2]]); }
  for (let i = 0; i < n; i++) { let d1 = 1e9, d2 = 1e9, k1 = 0; const x = pos[i * 3] + Math.sin(pos[i * 3 + 2] * 0.7) * 1.6 + gauss(r) * 0.5, z = pos[i * 3 + 2] + Math.cos(pos[i * 3] * 0.6) * 1.6 + gauss(r) * 0.5; for (let k = 0; k < ND; k++) { const d = (x - cen[k][0]) ** 2 + (z - cen[k][1]) ** 2; if (d < d1) { d2 = d1; d1 = d; k1 = k; } else if (d < d2) d2 = d; } dom[i] = k1; seam[i] = Math.sqrt(d2) - Math.sqrt(d1); }
  const src = cen.map(c => { let bi = 0, bd = 1e9; for (let i = 0; i < n; i += 7) { const d = (pos[i * 3] - c[0]) ** 2 + (pos[i * 3 + 2] - c[1]) ** 2; if (d < bd) { bd = d; bi = i; } } return bi; });
  const PLAYERS = [[232, 212], [248, 40], [258, 6], [262, 2]], Nat = t => keyed(PLAYERS, t, true);
  const rr = rngOf(59), order = [...Array(ND).keys()].sort(() => rr() - 0.5);
  let fa = 0, fb2 = 1, fd = 0; for (let i = 0; i < ND; i++) for (let j = i + 1; j < ND; j++) { const d = Math.hypot(cen[i][0] - cen[j][0], cen[i][1] - cen[j][1]); if (d > fd && Math.hypot(cen[i][0], cen[i][1]) < 30 && Math.hypot(cen[j][0], cen[j][1]) < 30) { fd = d; fa = i; fb2 = j; } }
  const final = [fa, fb2], doomed = order.filter(k => k !== fa && k !== fb2);
  const death = new Float32Array(ND).fill(1e9), volleys = [], sweep = [];
  doomed.forEach((k, i) => { const target = ND - 1 - i; let lo = 232, hi = 262; for (let it = 0; it < 40; it++) { const m = (lo + hi) / 2; if (Nat(m) > target) lo = m; else hi = m; } death[k] = hi + (rr() - 0.5) * 0.08; });
  const dist = (a, bb) => Math.hypot(cen[a][0] - cen[bb][0], cen[a][1] - cen[bb][1]);
  for (const k of doomed) { const td = death[k]; if (td > 254 && td < 257.2) { sweep.push({ t: td, b: k }); continue; }
    const cands = []; for (let j = 0; j < ND; j++) if (j !== k && death[j] > td + 0.3) cands.push(j);
    let a = cands[Math.floor(rr() * cands.length)]; for (let q = 0; q < 6; q++) { const c2 = cands[Math.floor(rr() * cands.length)]; if (dist(c2, k) < dist(a, k)) a = c2; }
    volleys.push({ t0: td - Math.min(0.5 + dist(a, k) / 38, td - 232.2), t1: td, a, b: k }); }
  sweep.sort((x, y) => x.t - y.t);
  volleys.push({ t0: 262.6, t1: 268.6, a: final[0], b: final[1] }, { t0: 262.6, t1: 268.6, a: final[1], b: final[0] });
  death[final[0]] = death[final[1]] = 268.6;
  let sunI = 34000, sbest = 1e9; for (let i = 34000; i < n; i += 3) { const d = Math.abs(Math.hypot(pos[i * 3], pos[i * 3 + 2]) - 24) + Math.abs(pos[i * 3 + 1]) * 3; if (d < sbest) { sbest = d; sunI = i; } }
  const sun = [pos[sunI * 3], pos[sunI * 3 + 1], pos[sunI * 3 + 2]];
  const conv = new Float32Array(n); let dmax = 0; for (let i = 0; i < n; i++) { const d = Math.hypot(pos[i * 3] - sun[0], pos[i * 3 + 2] - sun[2]); conv[i] = d; dmax = Math.max(dmax, d); }
  for (let i = 0; i < n; i++) conv[i] = 172.5 + 21 * Math.pow(conv[i] / dmax, 1.25) + (r() - 0.5) * 1.2;
  const ripple = new Float32Array(n); { const rad = new Float32Array(ND); for (let i = 0; i < n; i++) { const k = dom[i]; rad[k] = Math.max(rad[k], Math.hypot(pos[i * 3] - cen[k][0], pos[i * 3 + 2] - cen[k][1])); } for (let i = 0; i < n; i++) { const k = dom[i]; ripple[i] = 0.55 * Math.hypot(pos[i * 3] - cen[k][0], pos[i * 3 + 2] - cen[k][1]) / Math.max(rad[k], 1e-3); } }
  // the cell's star: a galaxy star near the Sun
  let cellI = sunI, cb = 1e9; for (let i = 34000; i < n; i += 2) { const d = Math.hypot(pos[i * 3] - sun[0] - 0.8, pos[i * 3 + 2] - sun[2] - 0.5); if (d < cb && i !== sunI) { cb = d; cellI = i; } }
  GAL = { n, pos, col, b, dom, seam, cen, death, volleys, src, conv, ND, sweep, sweeper: final[1], ripple, sun, cell: [pos[cellI * 3], pos[cellI * 3 + 1], pos[cellI * 3 + 2]] };
}
function aliveFraction(t) { if (!GAL) return 1; let a = 0; for (let k = 0; k < GAL.ND; k++) if (GAL.death[k] > t) a++; return a / GAL.ND; }
function playersAt(t) { if (!GAL || t < 223) return 1; const split = Math.round(Math.exp(lerp(0, Math.log(212), ss(223.5, 231, t)))); if (t < 232) return split; let a = 0; for (let k = 0; k < GAL.ND; k++) if (GAL.death[k] > t) a++; return a; }
function galFull(t) { const ang = 0.3 + t * 0.002; return { pos: [Math.cos(ang) * 50, 52, Math.sin(ang) * 50], look: [0, -3, 0] }; }
function galaxyCam(t) {
  const G = GAL, full = galFull(t);
  if (t < 186) {   // the pull-back from the cell's star to the whole galaxy
    const u = ss(171, 185, t), dir = norm(sub(full.pos, G.cell)), dFull = len(sub(full.pos, G.cell)), d = 5.0 * Math.pow(dFull / 5.0, Math.pow(u, 0.75));
    return { pos: add(G.cell, scl(dir, d)), look: mixv(G.cell, full.look, ease(ss(172, 185, t))), fov: 42 };
  }
  if (t >= 202 && t < 205) { const u = ease(ss(202, 205, t)); return { pos: add(full.pos, [0, lerp(-30, 0, u), 0]), look: full.look, fov: 42 }; }
  if (t >= 214 && t < 224) {   // drift to the rim and back
    const edge = { pos: [62, 7, 24], look: [24, -1, 2] }; const u = ss(214, 217, t) * (1 - ss(221, 224, t));
    return { pos: mixv(full.pos, edge.pos, ease(u)), look: mixv(full.look, edge.look, ease(u)), fov: 42 };
  }
  return { pos: full.pos, look: full.look, fov: 42 };
}
function sGalaxy(t, cellBack = 1) {
  const G = GAL, c = galaxyCam(t);
  camera(c.pos, c.look, c.fov, 0.01, 1e6); drawStars(0.35);
  const war = t >= 223, front = t >= 170 && t < 202, ir = t >= 202 ? 1 : ss(189.5, 193.5, t);
  const gu = { uT: t, uIR: ir, uWar: war ? 1 : 0, uSplit: ss(223.5, 231, t), uFrontOn: front || t >= 202 ? 1 : 0, uSizeK: 1, uNear: t < 185 ? 1 - ss(172, 182, t) : 0 };
  E.drawParticles(SYS.glow, { ...gu, uGlow: 0.018, uNear: 0 }, { depth: false });
  E.drawParticles(SYS.galaxy, { ...gu, uGlow: 0 }, { depth: false });
  if (t < 186) { pt(G.cell, [1, 0.62, 0.25], 4 * (1 - ss(176, 180, t)), 10); pt(G.sun, [1, 0.62, 0.25], 5 * (1 - ss(180, 184, t)), 12); flushPts({ depth: false }); }
  // probes leaving the rim, finding nothing
  if (t > 215 && t < 223) { const rr = rngOf(89); for (let k = 0; k < 70; k++) { const i = 34000 + Math.floor(rr() * (G.n - 34000)); const p = [G.pos[i * 3], G.pos[i * 3 + 1], G.pos[i * 3 + 2]]; if (Math.hypot(p[0], p[2]) < 30) continue;
    const d = norm([p[0], 0, p[2]]), t0 = 215.5 + rr() * 4, u = clamp((t - t0) / 3.5), fade = 1 - ss(t0 + 2.8, t0 + 4.5, t); if (u <= 0 || fade <= 0) continue; pt(add(p, scl(d, 2 + u * 40)), AMBER, 4 * fade, 6); } flushPts({ depth: false }); }
  if (war) {
    for (const v of G.volleys) { if (t < v.t0 || t > v.t1 + 0.9) continue; const A = G.src[v.a], B = G.src[v.b]; const pa = [G.pos[A * 3], G.pos[A * 3 + 1] + 0.2, G.pos[A * 3 + 2]], pb = [G.pos[B * 3], G.pos[B * 3 + 1] + 0.2, G.pos[B * 3 + 2]];
      const u = clamp((t - v.t0) / (v.t1 - v.t0)), fade = 1 - clamp((t - v.t1) / 0.9); const head = mixv(pa, pb, u); ln(pa, head, [1.0, 0.93, 0.85], 5.5 * fade, 2.6); pt(head, [1, 1, 1], 14 * fade * (u < 1 ? 1 : 0), 16); pt(pa, [1, 0.85, 0.7], 6 * fade, 22); }
    if (G.sweep.length && t > G.sweep[0].t - 0.6 && t < G.sweep[G.sweep.length - 1].t + 0.5) { const S = G.src[G.sweeper], ps = [G.pos[S * 3], 0.2, G.pos[S * 3 + 2]]; let i = 0; while (i < G.sweep.length - 1 && G.sweep[i + 1].t < t) i++;
      const A = G.sweep[i], B = G.sweep[Math.min(i + 1, G.sweep.length - 1)], u = B.t > A.t ? clamp((t - A.t) / (B.t - A.t)) : 0, pa = G.src[A.b], pb = G.src[B.b]; const tgt = [lerp(G.pos[pa * 3], G.pos[pb * 3], u), 0.2, lerp(G.pos[pa * 3 + 2], G.pos[pb * 3 + 2], u)];
      const k = ss(G.sweep[0].t - 0.6, G.sweep[0].t - 0.2, t) * (1 - ss(G.sweep[G.sweep.length - 1].t, G.sweep[G.sweep.length - 1].t + 0.5, t)); ln(ps, add(ps, scl(norm(sub(tgt, ps)), 70)), [1.0, 0.95, 0.9], 4.5 * k, 2.2); pt(ps, [1, 0.9, 0.8], 8 * k, 24); }
    flushLns({ depth: false }); flushPts({ depth: false });
  }
}

/* ================= the overlay: panel, instrument, callouts, cards, words ================= */
const MONO = 'Menlo, "SF Mono", Consolas, monospace', SANS = '"Avenir Next", "Helvetica Neue", Helvetica, Arial, sans-serif';
const SUP = { "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹" };
function fmtW(p) { if (p <= 0) return "0 W"; if (p < 1e12) return `${(p / 1e9).toFixed(0)} GW`; if (p < 1e15) return `${(p / 1e12).toFixed(p < 1e13 ? 1 : 0)} TW`; if (p < 1e18) return `${(p / 1e15).toFixed(p < 1e16 ? 1 : 0)} PW`; const e = Math.floor(Math.log10(p)), m = p / Math.pow(10, e); return `${m.toFixed(1)} × 10${String(e).split("").map(c => SUP[c]).join("")} W`; }
const fmtPop = p => p >= 1e9 ? `${(p / 1e9).toFixed(1)} bn` : p >= 1e6 ? `${Math.round(p / 1e6)} million` : `${Math.round(p / 1e3)} thousand`;
const fmtYear = y => y < 10000 ? String(Math.round(y)) : Math.round(y).toLocaleString("en-US");
const CARDS = [[28.5, 30.3, "2046", "1 TW of compute"], [48.4, 50.2, "2068", "compute uses all the energy humanity uses today"], [57.4, 59.2, "2097", "waste heat 2 W/m²"], [70.2, 72, "2113", "10 PW"], [89, 91.5, "2132", "all the sunlight the Earth receives"], [129.5, 131.5, "2291", "3.8 × 10²⁶ W · the Sun"], [167, 169, "", "a few thousand years"]];
const INSTR = [[7, 33, "VIIRS DAY/NIGHT BAND"], [33, 41, "GROUND"], [41, 50, "VISIBLE"], [50, 59.6, "THERMAL INFRARED  11 µm"], [59.6, 72, "VISIBLE"], [72, 84.5, "GROUND"], [84.5, 128.5, "VISIBLE"], [128.5, 138, "MID-INFRARED  12 µm"], [138, 144, "GROUND"], [144, 170, "VISIBLE"], [170, 191.5, "VISIBLE"], [191.5, 195, "MID-INFRARED  12 µm"], [195, 202, "GROUND"], [202, 272, "MID-INFRARED  12 µm"]];
// callouts: [t0, t1, text, world-point function (or null), screen fallback]
const CALL = [
  [9.5, 13, "data-centre regions, 2026", () => surf(nightShot(11).rot, 116.4, 39.9, 1.0)],
  [43, 46.5, "orbital data centres", () => add(EARTH, [0.75, 0.75, 0.45])],
  [45.5, 48.5, "solar fields", () => surf(orbitRot(47), -112, 34, 1.0)],
  [62, 65.5, "mass drivers venting seawater", null, [1460, 300]],
  [66, 69.5, "dry sea floor", () => surf(orbitRot(68), 5, 40, 1.0)],
  [102, 105.5, "mass drivers", () => add(MERC, [0.35, 0.45, 0.3])],
  [108.5, 111, "debris ring", null, [700, 640]],
  [121.5, 125, "collector swarm", () => add(SUN, [SUN_R * 1.6, SUN_R * 1.2, 0])],
  [134, 137.5, "laser relay", () => MOON],
  [145, 148, "self-replicating probes", null, [1250, 380]],
];
function overlay(t) {
  const on = ss(7.5, 9, t) * (t > 270 ? (Math.floor(t * 14) % 3 === 0 && t < 271.5 ? 1 : 0) : 1) * (t < 274 ? 1 : 0);
  ctx.save(); ctx.textBaseline = "top";
  if (on > 0) {
    ctx.globalAlpha = on; const L = 72, R = W - 72, T = 60;
    const label = (s, x, y, al) => { ctx.font = `500 13px ${MONO}`; ctx.letterSpacing = "3px"; ctx.fillStyle = "rgba(225,232,238,0.5)"; ctx.textAlign = al; ctx.fillText(s, x, y); };
    const value = (s, x, y, al, c = "rgba(240,244,247,0.95)") => { ctx.font = `400 26px ${MONO}`; ctx.letterSpacing = "1px"; ctx.fillStyle = c; ctx.textAlign = al; ctx.fillText(s, x, y); };
    label("YEAR", L, T, "left"); value(fmtYear(yearAt(t)), L, T + 22, "left");
    ctx.font = `600 12px ${MONO}`; ctx.letterSpacing = "3px"; ctx.textAlign = "left";
    if (t < 9.5) { ctx.fillStyle = "#ffb15a"; ctx.fillText("▸ TODAY", L + 92, T + 32); } else { ctx.globalAlpha = on * ss(9.5, 11, t) * 0.55; ctx.fillStyle = "rgba(225,232,238,1)"; ctx.fillText("PROJECTED", L + 92, T + 32); ctx.globalAlpha = on; }
    label("POWER", R, T, "right"); value(fmtW(powerAt(t)), R, T + 22, "right");
    const popA = 1 - ss(142, 144, t); if (popA > 0) { ctx.globalAlpha = on * popA; label("POPULATION", R, T + 72, "right"); value(fmtPop(popAt(t)), R, T + 94, "right"); ctx.globalAlpha = on; }
    if (t > 223) { ctx.globalAlpha = on * ss(223, 224, t); label("PLAYERS", R, T + 72, "right"); value(String(playersAt(t)), R, T + 94, "right", "#ffb15a"); ctx.globalAlpha = on; }
    // the instrument
    for (const [a, b, s] of INSTR) if (t >= a && t < b) { const k = ss(a, a + 0.4, t) * (1 - ss(b - 0.3, b, t)); ctx.globalAlpha = on * k * 0.7; ctx.font = `500 12px ${MONO}`; ctx.letterSpacing = "3px"; ctx.fillStyle = "rgba(225,232,238,1)"; ctx.textAlign = "left"; ctx.fillText(s, L, H - 64); }
    ctx.globalAlpha = on;
    // callouts
    for (const [a, b, s, fn, fallback] of CALL) { if (t < a || t > b) continue; const k = ss(a, a + 0.4, t) * (1 - ss(b - 0.4, b, t)); let p = null;
      if (fn) { const w = fn(); const pr = E.project(w); if (pr && pr[0] > 0 && pr[0] < W && pr[1] > 0 && pr[1] < H) p = [pr[0], pr[1]]; } else p = fallback;
      if (!p) continue; ctx.globalAlpha = on * k; ctx.fillStyle = "#ffb15a"; ctx.beginPath(); ctx.arc(p[0], p[1], 3, 0, TAU); ctx.fill();
      ctx.strokeStyle = "rgba(255,177,90,0.7)"; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(p[0] + 6, p[1] - 6); ctx.lineTo(p[0] + 22, p[1] - 22); ctx.stroke();
      ctx.font = `500 14px ${MONO}`; ctx.letterSpacing = "2px"; ctx.fillStyle = "rgba(245,247,249,0.92)"; ctx.textAlign = "left"; ctx.fillText(s, p[0] + 28, p[1] - 32); }
    ctx.globalAlpha = 1;
  }
  // chapter cards
  ctx.textAlign = "center"; ctx.textBaseline = "middle";
  for (const [a, b, yr, q] of CARDS) { const k = ss(a, a + 0.3, t) * (1 - ss(b - 0.35, b, t)); if (k <= 0) continue; ctx.globalAlpha = k;
    if (yr) { ctx.font = `200 78px ${SANS}`; ctx.letterSpacing = "10px"; ctx.fillStyle = "rgba(245,247,249,0.96)"; ctx.fillText(yr, W / 2 + 5, H * 0.76); }
    ctx.font = `500 17px ${MONO}`; ctx.letterSpacing = "3px"; ctx.fillStyle = "rgba(255,190,120,0.95)"; ctx.fillText(q.toUpperCase(), W / 2 + 2, yr ? H * 0.76 + 62 : H * 0.8); }
  // words
  const word = (s, k, y, size = 64, alpha = 0.97) => { if (k <= 0) return; ctx.globalAlpha = k; ctx.font = `300 ${size}px ${SANS}`; ctx.letterSpacing = "2px"; ctx.fillStyle = `rgba(246,248,250,${alpha})`; ctx.fillText(s, W / 2, y); };
  { const k = ss(0.6, 1.4, t) * (1 - ss(5.4, 6.4, t)); if (k > 0) { ctx.globalAlpha = k; ctx.font = `500 14px ${MONO}`; ctx.letterSpacing = "3px"; ctx.fillStyle = "rgba(225,232,238,0.55)"; ctx.fillText("UNITED NATIONS GENERAL ASSEMBLY  ·  22 SEPTEMBER 2026", W / 2, H - 120); } }
  word("super intelligence", ss(1.6, 2.4, t) * (1 - ss(5.6, 6.8, t)), H / 2);
  { const k = ss(76, 77.5, t) * (1 - ss(81.5, 82.5, t)); if (k > 0) { ctx.globalAlpha = k; ctx.font = `500 22px ${MONO}`; ctx.letterSpacing = "12px"; ctx.fillStyle = "rgba(30,32,36,0.8)"; ctx.fillText("PROGRESS", W / 2 + 6, H - 150); } }
  word("super intelligence", ss(206, 207.5, t) * (1 - ss(211.5, 213.5, t)) * 0.5, H * 0.82, 54, 0.9);
  { const k = ss(281, 283, t) * (1 - ss(296, 299, t)); if (k > 0) { ctx.globalAlpha = k; ctx.font = `200 70px ${SANS}`; ctx.letterSpacing = "22px"; ctx.fillStyle = "rgba(246,248,250,0.97)"; ctx.fillText("THE GAME OF WINNING", W / 2 + 11, H / 2); } }
  ctx.restore();
}

/* ================= the frame ================= */
function drawScene(t) {
  E.begin(); let fade = 1, bloom = 0.85, thresh = 0.9;
  if (t < 7) { if (t > 5.2) { sToday(7); fade = ss(5.2, 7, t); } }
  else if (t < 33) sToday(t);
  else if (t < 41) { sCampus(t); bloom = 0.5; thresh = 1.2; }
  else if (t < 72) { sOrbital(t); if (t < 41.6) fade = ss(41, 41.6, t); }
  else if (t < 84.5) { sDome(t); bloom = 0.3; thresh = 1.5; }
  else if (t < 138) { sSolar(t); if (t < 85.2) fade = ss(84.5, 85.2, t); }
  else if (t < 144) { sTwoSuns(t); bloom = 0.32; thresh = 1.5; }
  else if (t < 149) sLaunch(t);
  else if (t < 154) { sTransit(t); if (t < 149.4) fade = ss(149, 149.4, t); }
  else if (t < 171) { sCell(t); fade = 1 - ss(170.5, 171, t); }
  else if (t < 195) { sGalaxy(t); if (t < 171.6) fade = ss(171, 171.6, t); }
  else if (t < 202) { sLastSky(t); bloom = 0.4; thresh = 1.2; }
  else if (t < 272) { sGalaxy(t); if (t < 203.5) fade = ss(202, 203.5, t); }
  let fadeCol = [0, 0, 0];
  if (t > 32.3 && t < 33) { fade = 1 - ss(32.3, 33, t); fadeCol = [0.02, 0.025, 0.04]; }
  if (t > 71.3 && t < 72) { fade = 1 - ss(71.3, 72, t); fadeCol = [0.75, 0.77, 0.8]; }
  if (t >= 84.5 && t < 85.2) { fadeCol = [0.75, 0.77, 0.8]; }
  E.end({ bloom, thresh, exposure: 1.0, grain: 0.028, vignette: 0.4, seed: (t * 30) % 97, fade, fadeCol });
}
let COMPOSITE = true;
function frame(t) {
  if (!ready) throw new Error("not ready");
  drawScene(t);
  ctx.globalAlpha = 1;
  if (COMPOSITE) ctx.drawImage(E.gl.canvas, 0, 0, W, H); else ctx.clearRect(0, 0, W, H);
  overlay(t);
  return ctx.canvas;
}
// view: a 2D canvas for the overlay (and, when composite, the whole picture); glc: the WebGL canvas
async function init(view, onProgress = () => {}, { composite = true, glCanvas = null } = {}) {
  ctx = view.getContext("2d"); COMPOSITE = composite;
  const glc = glCanvas || document.createElement("canvas"); glc.width = W; glc.height = H;
  E = Engine.create(glc, W, H);
  const names = { earthDay: "assets/earth-day.jpg", earthNight: "assets/earth-night.jpg", mercury: "assets/mercury.jpg", moon: "assets/moon.jpg" };
  let k = 0; for (const [key, u] of Object.entries(names)) { tex[key] = await E.loadTexture(u); onProgress(++k / 6); }
  buildGrowth(tex.earthNight.img, tex.earthDay.img); onProgress(5 / 6);
  buildSystems(); onProgress(1);
  ready = true;
}
const PX = new Uint8Array(4);
function timeFrame(t) { const a = performance.now(); drawScene(t); E.gl.readPixels(0, 0, 1, 1, E.gl.RGBA, E.gl.UNSIGNED_BYTE, PX); return performance.now() - a; }
return { init, frame, timeFrame, W, H, DUR, yearAt, powerAt, galaxy: () => GAL };
})();
