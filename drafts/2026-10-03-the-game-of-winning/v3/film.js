// The Game of Winning, v3: a real-time film. One world per act, continuous cameras, GPU-animated particles.
// Every date and number on screen follows ../trajectory.py.
"use strict";
const Film = (() => {
const W = 1920, H = 1080, TAU = Math.PI * 2, D2R = Math.PI / 180;
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

/* ================= the time map: film seconds → story seconds ================= */
// [filmStart, filmEnd, storyStart, storyEnd]; a gap in story time is a cut (the rim drift is dropped)
const TMAP = [[0, 6, 0, 7], [6, 29, 7, 33], [29, 35.5, 33, 41], [35.5, 62, 41, 72], [62, 72, 72, 84.5], [72, 119, 84.5, 138], [119, 124.5, 138, 144], [124.5, 128.5, 144, 149],
  [128.5, 131.5, 149, 154], [131.5, 146, 154, 171], [146, 167, 171, 195], [167, 173.5, 195, 202], [173.5, 182, 202, 214], [182, 228, 223, 272], [228, 234, 272, 280], [234, 250, 280, 300]];
const DUR = 250;
function storyT(f) { for (const [f0, f1, s0, s1] of TMAP) if (f <= f1) return f <= f0 ? s0 : s0 + (f - f0) / (f1 - f0) * (s1 - s0); return 300; }
function filmT(st) { for (const [f0, f1, s0, s1] of TMAP) if (st <= s1) return st <= s0 ? f0 : f0 + (st - s0) / (s1 - s0) * (f1 - f0); return DUR; }

/* ================= the players: the race, absorption, one winner ================= */
// Each player is a mosaic of sites across continents, not a country. Player 0 (amber) wins.
const PCOL = [[1.0, 0.52, 0.16], [0.36, 0.82, 0.78], [1.0, 0.46, 0.56], [0.72, 0.92, 0.38], [0.66, 0.52, 1.0], [0.62, 0.8, 1.0], [1.0, 0.8, 0.32], [1.0, 0.58, 0.42], [0.48, 0.98, 0.62], [0.9, 0.52, 0.94], [0.42, 0.66, 1.0], [0.92, 0.86, 0.62]];
// [year, absorbed, absorber]: the race consolidates until one player is left in 2097
const ABSORB = [[2031, 11, 7], [2034, 9, 3], [2037, 5, 0], [2041, 10, 6], [2045, 8, 0], [2050, 7, 3], [2056, 4, 0], [2062, 6, 2], [2070, 3, 0], [2081, 1, 2], [2097, 2, 0]];
function players(year) {
  const parent = [...Array(12).keys()], since = new Array(12).fill(-1e9);
  for (const [y, a, b] of ABSORB) if (year >= y) { parent[a] = b; since[a] = y; }
  const root = k => { let r = k; while (parent[r] !== r) r = parent[r]; return r; };
  const cols = new Float32Array(36); const alive = new Set();
  for (let k = 0; k < 12; k++) { const r = root(k); alive.add(r); const u = clamp((year - since[k]) / 2.5); const own = k === r ? PCOL[k] : mixv(PCOL[k], PCOL[r], since[k] > -1e8 ? u : 1); cols.set(k === r ? PCOL[k] : own, k * 3); }
  return { cols, alive: [...alive].sort((x, y) => x - y), root };
}

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
let E, ctx, tex = {}, ready = false, GROW = null, SEED_PLAYER = [];
const PT = new Float32Array(8 * 200000), LN = new Float32Array(11 * 60000);
let np = 0, nl = 0;
function pt(p, c, a, size) { if (np >= 200000) return; const o = np * 8; PT[o] = p[0]; PT[o + 1] = p[1]; PT[o + 2] = p[2]; PT[o + 3] = c[0]; PT[o + 4] = c[1]; PT[o + 5] = c[2]; PT[o + 6] = a; PT[o + 7] = size; np++; }
function ln(a, b, c, alpha, w) { if (nl >= 60000) return; const o = nl * 11; LN.set([a[0], a[1], a[2], b[0], b[1], b[2], c[0], c[1], c[2], alpha, w], o); nl++; }
const flushPts = opt => { E.points(PT, np, opt); np = 0; };
const flushLns = opt => { E.lines(LN, nl, opt); nl = 0; };
let CAM = null;   // current camera, for labels
let CAMF = null;
function camera(pos, look, fov = 40, near = 0.01, far = 20000) { CAM = { pos, look }; CAMF = E.camera(pos, look, [0, 1, 0], fov, near, far); return CAMF; }

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
  { const G = GAL, d = new Float32Array(G.n * 12); for (let i = 0; i < G.n; i++) { const k = G.dom[i]; d.set([G.pos[i * 3], G.pos[i * 3 + 1], G.pos[i * 3 + 2], G.b[i], G.col[i * 3], G.col[i * 3 + 1], G.col[i * 3 + 2], G.conv[i], G.death[k] + G.ripple[i], G.seam[i], k, 0], i * 12); }
    SYS_GAL_BODY = `uniform float uIR, uWar, uSplit, uFrontOn, uNear, uGlow; uniform vec3 uPC[12];
      void particle(out vec3 pos, out vec4 col, out float size){
        pos = a0.xyz; vec3 red = vec3(0.85, 0.12, 0.05); vec3 c = a1.xyz; float a = a0.w * 0.9 * (1.0 + 3.0 * uNear); size = 1.4 * (1.0 + 1.5 * uNear);
        if (uFrontOn > 0.5 && uT >= a1.w) { float age = uT - a1.w; if (age < 0.5) { c = vec3(1.0, 0.6, 0.2); a = 5.0 * (1.0 - age / 0.5) + 0.3; } else { c = mix(vec3(0.55, 0.14, 0.05), red, uIR); a = mix(0.32 * a0.w + 0.08, a0.w * 0.8, uIR); } }
        if (uWar > 0.5) { vec3 tint = uPC[int(mod(a2.z, 12.0))]; c = mix(red, tint * 0.9, uSplit * 0.85); a = a0.w * 0.8; float sk = uSplit * clamp(1.0 - a2.y / 0.35, 0.0, 1.0); c = mix(c, vec3(1.0, 0.9, 0.8), sk * 0.6); a += sk * 1.2;
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
function buildGrowth(nightImg, dayImg, GW = 2048, GH = 1024) {
  const cv = document.createElement("canvas"); cv.width = GW; cv.height = GH; const c2 = cv.getContext("2d", { willReadFrequently: true });
  c2.drawImage(nightImg, 0, 0, GW, GH); const night = c2.getImageData(0, 0, GW, GH).data;
  c2.drawImage(dayImg, 0, 0, GW, GH); const day = c2.getImageData(0, 0, GW, GH).data;
  const N = GW * GH, light = new Float32Array(N), sea = new Float32Array(N);
  for (let i = 0; i < N; i++) {
    const o = i * 4; light[i] = (night[o] + night[o + 1] + night[o + 2]) / 765;
    const r = day[o], g = day[o + 1], b = day[o + 2];
    const isSea = b > r * 1.25 && b > g * 1.05 && r < 110; sea[i] = isSea ? clamp(1 - (b - 40) / 150) * 0.97 + 0.03 : 0;   // brighter blue = shallower
  }
  // multi-source Dijkstra over land: cheaper through lit (populated, powered) land
  const cost = new Float32Array(N).fill(1e9), heap = [], owner = new Uint8Array(N);
  const push = (c, i) => { heap.push([c, i]); let k = heap.length - 1; while (k > 0) { const p = (k - 1) >> 1; if (heap[p][0] <= heap[k][0]) break; [heap[p], heap[k]] = [heap[k], heap[p]]; k = p; } };
  const pop = () => { const top = heap[0], last = heap.pop(); if (heap.length) { heap[0] = last; let k = 0; for (;;) { const l = 2 * k + 1, r = l + 1; let m = k; if (l < heap.length && heap[l][0] < heap[m][0]) m = l; if (r < heap.length && heap[r][0] < heap[m][0]) m = r; if (m === k) break; [heap[m], heap[k]] = [heap[k], heap[m]]; k = m; } } return top; };
  const order = DC_REGIONS.map((s, i) => i).sort((a, b) => DC_REGIONS[a][0] - DC_REGIONS[b][0]); const seedPlayer = new Array(DC_REGIONS.length); order.forEach((s, k) => { seedPlayer[s] = k % 12; });
  DC_REGIONS.forEach(([lo, la], si) => { const x = Math.floor((lo + 180) / 360 * GW), y = Math.floor((90 - la) / 180 * GH), i = y * GW + x; cost[i] = 0; owner[i] = seedPlayer[si]; push(0, i); });
  SEED_PLAYER = seedPlayer;
  while (heap.length) {
    const [c, i] = pop(); if (c > cost[i]) continue; const x = i % GW, y = (i / GW) | 0, lat = (90 - (y + 0.5) / GH * 180) * D2R, cx = Math.cos(lat);
    for (let dy = -1; dy <= 1; dy++) for (let dx = -1; dx <= 1; dx++) {
      if (!dx && !dy) continue; const ny = y + dy; if (ny < 0 || ny >= GH) continue; const nx = (x + dx + GW) % GW, j = ny * GW + nx;
      if (sea[j] > 0) continue; const step = Math.hypot(dx * cx, dy) * (1.35 - 1.1 * Math.sqrt(Math.min(1, light[j] * 3)));
      const nc = c + step; if (nc < cost[j]) { cost[j] = nc; owner[j] = owner[i]; push(nc, j); }
    }
  }
  let maxc = 0; for (let i = 0; i < N; i++) if (sea[i] === 0 && cost[i] < 1e8) maxc = Math.max(maxc, cost[i]);
  const bytes = new Uint8Array(N * 4);
  for (let i = 0; i < N; i++) {
    const yr = sea[i] > 0 ? 2200 : cost[i] < 1e8 ? 2027 + Math.pow(cost[i] / maxc, 0.8) * 85 : 2110;   // land: 2027–2112 (Kardashev I)
    bytes[i * 4] = clamp((yr - 2026) / 128) * 255; bytes[i * 4 + 1] = sea[i] * 255; bytes[i * 4 + 2] = owner[i] * 20; bytes[i * 4 + 3] = 255;
  }
  GROW = E.dataTexture(GW, GH, bytes); GROW_BYTES = { GW, GH, bytes };
}
let GROW_BYTES = null;
function exportGrowth() { const { GW, GH, bytes } = GROW_BYTES; const cv = document.createElement("canvas"); cv.width = GW; cv.height = GH; const c2 = cv.getContext("2d"); const id = c2.createImageData(GW, GH); id.data.set(bytes); c2.putImageData(id, 0, 0); return cv.toDataURL("image/png"); }
async function loadGrowth() {
  const img = await new Promise((res, rej) => { const i = new Image(); i.onload = () => res(i); i.onerror = rej; i.src = "growth.png"; });
  const cv = document.createElement("canvas"); cv.width = img.width; cv.height = img.height; const c2 = cv.getContext("2d", { willReadFrequently: true }); c2.drawImage(img, 0, 0);
  const bytes = new Uint8Array(c2.getImageData(0, 0, img.width, img.height).data.buffer); GROW = E.dataTexture(img.width, img.height, bytes);
  // seeds' players must match the map: recompute the deal
  const order = DC_REGIONS.map((s0, i) => i).sort((a, b) => DC_REGIONS[a][0] - DC_REGIONS[b][0]); SEED_PLAYER = new Array(DC_REGIONS.length); order.forEach((s0, k) => { SEED_PLAYER[s0] = k % 12; });
}

/* ================= Earth helpers ================= */
function drawStars(k = 0.8) { E.drawParticles(SYS.stars, { uCenter: CAM.pos, uK: k }, { depth: true }); }
function earth(t, rot, o = {}) {
  const year = o.year ?? yearAt(t);
  E.sphere({ mode: 0, day: tex.earthDay, night: tex.earthNight, grow: GROW, cloud: tex.clouds || null, pCol: players(year).cols, center: EARTH, radius: 1, rot, sun: SUN_DIR_AT_EARTH, nightGain: o.nightGain ?? 1.5, dayGain: o.dayGain ?? 1.0,
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
  const fl = ss(8, 9.5, t) * (1 - ss(17, 21, t));
  if (fl > 0) { DC_REGIONS.forEach(([lo, la], i) => { const p = surf(rot, lo, la, 1.002); pt(p, PCOL[SEED_PLAYER[i]], fl * (2.4 + 1.2 * Math.sin(t * 5 + lo)), 12); }); flushPts({ depth: true }); }
}

/* ================= ground scenes: one ray-marched shader, four moods ================= */
let GROUND = null, NOISE = null;
const GROUND_FS = `#version 300 es
precision highp float; in vec2 vUV; out vec4 o; uniform vec2 uRes;
uniform int iZero; uniform vec4 uPl[40], uPc[40]; uniform vec3 uRk;   // always 0: loop bounds that depend on it are not unrolled, which keeps this shader small enough to run fast
uniform float uMode, uTime, uH, uPitch, uYaw, uLaunch, uStars, uFade, uHaze, uDomeLight, uFov, uCamX, uDbg;
bool off(int b){ return (int(uDbg) & b) != 0; }   // development: switch parts off to time them
// four moods: 0 West Texas at dusk · 1 the dry Mediterranean at noon · 2 two suns, a dim day · 3 the night the stars go out
// MD is defined per program (one compiled shader per mood, so each carries only its own work)
float h21(vec2 p){ p = fract(p * vec2(123.34, 456.21)); p += dot(p, p + 45.32); return fract(p.x * p.y); }
float h31(vec3 p){ p = fract(p * 0.1031); p += dot(p, p.zyx + 31.32); return fract((p.x + p.y) * p.z); }
precision highp sampler3D; uniform sampler2D uN2; uniform sampler3D uN3;
float n2(vec2 p){ vec2 i = floor(p), f = fract(p); f = f*f*(3.0-2.0*f); return texture(uN2, (i + f + 0.5) / 256.0).r; }
float n3(vec3 p){ vec3 i = floor(p), f = fract(p); f = f*f*(3.0-2.0*f); return texture(uN3, (i + f + 0.5) / 64.0).r; }
float fb(vec2 p){ float a = 0.5, s = 0.0; for (int i = 0; i < 5 + iZero; i++) { s += a * n2(p); p = p * 2.02 + 7.3; a *= 0.5; } return s; }
float fb3(vec3 p){ float a = 0.5, s = 0.0; for (int i = 0; i < 4 + iZero; i++) { s += a * n3(p); p = p * 2.03 + 7.3; a *= 0.5; } return s; }
vec2 vor(vec2 p){ vec2 i = floor(p), f = fract(p); float d1 = 9.0, d2 = 9.0; for (int y = -1; y <= 1; y++) for (int x = -1; x <= 1; x++) { vec2 g = vec2(x, y); vec2 c = g + vec2(h21(i + g), h21(i + g + 3.1)); float d = length(c - f); if (d < d1) { d2 = d1; d1 = d; } else if (d < d2) d2 = d; } return vec2(d1, d2); }
float sdBox(vec3 p, vec3 b){ vec3 q = abs(p) - b; return length(max(q, 0.0)) + min(max(q.x, max(q.y, q.z)), 0.0); }
float sdCap(vec3 p, vec3 a, vec3 b, float r){ vec3 pa = p - a, ba = b - a; float h = clamp(dot(pa, ba) / dot(ba, ba), 0.0, 1.0); return length(pa - ba * h) - r; }
float smin(float a, float b, float k){ float h = clamp(0.5 + 0.5 * (b - a) / k, 0.0, 1.0); return mix(b, a, h) - k * h * (1.0 - h); }
const vec3 DOME = vec3(-8.0, 0.0, -52.0); const float DOME_R = 30.0; const float HX = 260.0, HZ = 95.0;
vec3 SUN0 = vec3(-0.447, -0.03, -0.894);    // dusk: the sun just under the horizon, ahead and left
vec3 SUN1 = vec3(0.42, 0.6, -0.68);         // noon over the basin: high, ahead and right, so the steam is lit from behind
vec3 MOONL = vec3(0.33, 0.4, -0.855);       // the blazing Moon
vec3 RSUN = vec3(-0.55, 0.15, -0.8);        // the enclosed Sun, low and red
vec3 ro;

// the rocket, 7 km away; u runs 0 → 1 over the shot (the same path is in film.js)
vec3 rocket(float u){ return vec3(900.0 - 1500.0 * u * u, 60000.0 * pow(u, 1.8), -7000.0 - 9000.0 * u * u); }

/* ---------- geometry ---------- */
float person(vec3 p, vec3 b, float s){
  p = (p - b) / s; float d = sdCap(p, vec3(-0.1, 0.05, 0), vec3(-0.08, 0.86, 0), 0.075); d = min(d, sdCap(p, vec3(0.1, 0.05, 0), vec3(0.08, 0.86, 0), 0.075));
  d = smin(d, sdCap(p, vec3(0, 0.95, 0), vec3(0.02, 1.4, -0.03), 0.165), 0.05); d = min(d, length(p - vec3(0.03, 1.62, -0.05)) - 0.105);
  d = min(d, sdCap(p, vec3(-0.21, 1.38, 0), vec3(-0.26, 0.92, 0.03), 0.048)); d = min(d, sdCap(p, vec3(0.21, 1.38, 0), vec3(0.26, 0.92, 0.03), 0.048)); return d * s;
}
// hyperscale halls: 210 m long, 48 m deep, 14–20 m tall, a double row of chillers on the roof; the road runs between two columns
float halls(vec3 p, out float id, out vec3 q){
  float z0 = MD == 0 ? -110.0 : -1500.0;
  vec2 cell = vec2(floor(p.x / HX), floor(p.z / HZ));
  q = vec3(mod(p.x, HX) - HX * 0.5, p.y, mod(p.z, HZ) - HZ * 0.5);
  id = h21(cell + 0.37);
  float hgt = (9.0 + 5.0 * id) * (MD == 0 ? 1.0 : 2.4);
  float d = sdBox(q - vec3(0.0, hgt, 0.0), vec3(105.0, hgt, 24.0));
  vec3 r = q; r.x = mod(q.x + 4.5, 9.0) - 4.5; r.z = abs(q.z) - 11.0;
  float ch = max(sdBox(r - vec3(0.0, 2.0 * hgt + 1.2, 0.0), vec3(3.3, 1.2, 4.2)), abs(q.x) - 99.0);
  d = min(d, ch);
  if (id > 0.55) d = min(d, sdCap(q, vec3(-112.0, 0.0, 30.0), vec3(-112.0, 52.0, 30.0), 2.6));   // turbine stacks between the halls
  if (MD != 0) d = max(d, -(p.z + 1500.0 + 900.0 * h21(vec2(cell.x, 3.0))));   // the basin halls start far off, ragged
  return max(d, p.z - z0);
}
// the garden: eleven trees, their canopies precomputed as spheres (film.js, TREES); a bounding sphere per tree lets most of them be skipped
uniform vec4 uTS[55], uTA[11], uTT[11], uTB[11];
float garden(vec3 p){
  vec3 q = p - DOME; float bound = length(q) - DOME_R; if (bound > 1.0 || off(512)) return max(bound, 0.5);
  float d = 1e3;
  for (int k = 0; k < 11 + iZero; k++) { float db = length(q - uTB[k].xyz) - uTB[k].w; if (db > 1.0) { d = min(d, db); continue; }
    float dt = sdCap(q, uTA[k].xyz, uTT[k].xyz, 0.26);
    for (int j = 0; j < 5 + iZero; j++) { vec4 sp = uTS[k * 5 + j]; dt = smin(dt, length(q - sp.xyz) - sp.w, 1.3); }
    d = min(d, dt); }
  if (d < 1.5) d += (n3(q * 1.4) - 0.5) * 1.1 + (n3(q * 4.2) - 0.5) * 0.3;
  float sb = smoothstep(0.62, 0.3, n2(q.xz * 0.3)); d = min(d, max(max(q.y - 1.0 * sb + 0.25, 0.6 - 2.0 * sb), length(q.xz) - (DOME_R - 2.0)));   // shrubs, only where they grow
  // people under the glass
  if (MD == 1) for (int k = 0; k < 5 + iZero; k++) { float fk = float(k); vec3 b = vec3(-11.0 + fk * 4.3, 0.0, 22.0 - abs(fk - 2.0) * 1.6); float pb = length(q - b - vec3(0.0, 0.9, 0.0)) - 1.1;
    d = min(d, pb > 0.5 ? pb : person(q, b, 1.0 - 0.04 * fk)); }
  return d;
}
float figures(vec3 p){ if (MD != 2) return 1e3; vec3 c = vec3(5.0, 0.0, 16.0); float b = length(p - c) - 4.0; if (b > 1.0) return b; return min(person(p, vec3(4.2, 0.0, 16.3), 1.0), person(p, vec3(5.4, 0.0, 15.6), 0.93)); }
float scene(vec3 p, out float mat, out float id, out vec3 q){
  float d = 1e4; mat = -1.0; id = 0.0; q = vec3(0.0);
  float hid; vec3 hq; float dh = halls(p, hid, hq); if (dh < d) { d = dh; mat = 1.0; id = hid; q = hq; }
  if (MD != 0) { float dg = garden(p); if (dg < d) { d = dg; mat = 2.0; } }
  float df = figures(p); if (df < d) { d = df; mat = 3.0; }
  if (MD == 0) { float fx = abs(p.x); vec3 fp = vec3(mod(p.x, 3.2) - 1.6, p.y, p.z + 70.0); float dp = max(sdCap(fp, vec3(0.0), vec3(0.0, 3.0, 0.0), 0.04), 18.0 - fx); if (dp < d) { d = dp; mat = 5.0; } }
  return d;
}
float sceneD(vec3 p){ float m, i; vec3 q; return scene(p, m, i, q); }
float shadow(vec3 p, vec3 rd, float tmax){ float res = 1.0, t = 0.1; for (int i = 0; i < 40 + iZero; i++) { float h = sceneD(p + rd * t); res = min(res, 8.0 * h / t); t += clamp(h, 0.1, 8.0); if (res < 0.01 || t > tmax) break; } return clamp(res, 0.0, 1.0); }
float occlusion(vec3 p, vec3 n){ float o = 0.0, w = 1.0; for (int i = 1; i <= 4; i++) { float h = 0.5 * float(i); o += (h - min(sceneD(p + n * h), p.y + n.y * h)) * w; w *= 0.6; } return clamp(1.0 - 0.9 * o, 0.0, 1.0); }
// the old coastline: the basin floor is two kilometres below the old sea level, and the continental slope stands over it like a wall
float hallH(vec2 xz){ if (xz.y > -1500.0) return 0.0; vec2 cell = vec2(floor(xz.x / HX), floor(xz.y / HZ)); vec2 q = vec2(mod(xz.x, HX) - HX * 0.5, mod(xz.y, HZ) - HZ * 0.5);
  if (xz.y > -1500.0 - 900.0 * h21(vec2(cell.x, 3.0))) return 0.0; float id = h21(cell + 0.37); return (abs(q.x) < 105.0 && abs(q.y) < 24.0) ? (9.0 + 5.0 * id) * 4.8 + 2.4 : 0.0; }
float escH(vec2 xz){ if (xz.y > -5200.0) return 0.0; float s = -(xz.y + 10500.0 + 0.32 * xz.x); return 1500.0 * smoothstep(-2200.0, 2600.0, s + (fb(xz * 0.00045) - 0.5) * 3800.0) * (0.7 + 0.5 * fb(xz * 0.0011 + 4.0)) - 120.0 * pow(fb(xz * 0.004), 2.0); }

/* ---------- sky ---------- */
vec3 starfield(vec3 rd, float k){
  if (rd.y < -0.02 || k <= 0.0) return vec3(0.0);
  vec3 gn = MD == 3 ? vec3(0.6, -0.71, -0.36) : vec3(0.34, 0.5, 0.8); float gb = dot(rd, normalize(gn)), band = exp(-gb * gb * 22.0);   // the Milky Way, a great circle
  vec3 c = vec3(0.0);
  for (int L = 0; L < 2; L++) { float sc = L == 0 ? 170.0 : 380.0; vec3 sp = rd * sc; vec3 cell = floor(sp); float hs = h31(cell + float(L) * 17.0);
    vec3 cc = cell + 0.25 + 0.5 * vec3(h31(cell + 1.3), h31(cell + 2.9), h31(cell + 4.7));
    float th = L == 0 ? 0.955 : mix(0.992, (MD == 3 ? 0.84 : 0.97), band);
    float s = step(th, hs) * smoothstep(0.11, 0.0, length(sp - cc)) * (L == 0 ? 0.7 + 5.0 * pow(hs, 40.0) : 0.35);
    vec3 sc3 = mix(vec3(1.0, 0.82, 0.62), vec3(0.75, 0.85, 1.0), h31(cell + 5.5));
    if (MD == 3) { float th2 = mix(h31(cell + 9.1), 0.35 + 0.65 * h31(cell + 9.1), band);   // nearby stars go first, the far band last
      float alive = smoothstep(th2 - 0.03, th2 + 0.01, uStars); float red = smoothstep(th2 + 0.16, th2, uStars); s *= alive; sc3 = mix(sc3, vec3(1.0, 0.2, 0.05), red); }
    c += sc3 * s; }
  if (MD == 3) { float lane = smoothstep(0.42, 0.62, fb(vec2(atan(rd.z, rd.x) * 9.0, gb * 30.0)));
    float glow = band * (0.45 + 0.55 * fb(rd.xz * 9.0 + rd.y * 3.0)) * (1.0 - 0.55 * lane * smoothstep(0.2, 0.0, abs(gb)));
    c += mix(vec3(0.12, 0.04, 0.018), vec3(0.11, 0.11, 0.125), smoothstep(0.15, 0.7, uStars)) * glow * smoothstep(0.0, 0.5, uStars); }
  return c * k * smoothstep(-0.02, 0.12, rd.y);
}
vec3 sky(vec3 rd){
  float e = max(rd.y, 0.0); vec3 c;
  if (MD == 0) {
    vec2 hs = normalize(SUN0.xz); float az = max(dot(normalize(rd.xz + 1e-5), hs), 0.0);
    vec3 hor = mix(vec3(0.2, 0.085, 0.04), vec3(0.95, 0.38, 0.11), pow(az, 5.0));
    c = mix(hor, vec3(0.045, 0.06, 0.12), smoothstep(0.0, 0.2, e));
    c = mix(c, vec3(0.006, 0.009, 0.022), smoothstep(0.18, 0.85, e));
    c += vec3(1.0, 0.5, 0.15) * 0.7 * pow(az, 30.0) * exp(-e * 25.0);
    if (rd.y > 0.012) { vec2 cp = rd.xz / rd.y * 0.32; float cd = smoothstep(0.52, 0.82, fb(cp * vec2(0.8, 3.2) + vec2(3.0, 0.0) + uTime * 0.004)) * smoothstep(0.012, 0.1, rd.y) * smoothstep(0.85, 0.25, rd.y);
      vec3 cc = mix(vec3(0.05, 0.035, 0.045), vec3(1.0, 0.36, 0.2), pow(az, 2.5) * smoothstep(0.55, 0.04, e)); c = mix(c, cc, cd * 0.9); }
    c += starfield(rd, 0.55 * smoothstep(0.2, 0.6, e));
    // satellites still in sunlight, crossing; one train
    vec2 sk = vec2(atan(rd.x, -rd.z), rd.y);
    for (int k = 0; k < 9 + iZero; k++) { float fk = float(k); vec2 a = vec2(-1.2 + 2.4 * h21(vec2(fk, 1.0)), 0.35 + 0.5 * h21(vec2(fk, 2.0))); vec2 dd = normalize(vec2(1.0, (h21(vec2(fk, 3.0)) - 0.5) * 1.2)) * (h21(vec2(fk, 7.0)) > 0.5 ? 1.0 : -1.0);
      vec2 pos = a + dd * (uTime - 33.0) * (0.02 + 0.015 * h21(vec2(fk, 4.0))); c += vec3(0.9, 0.95, 1.0) * 0.9 * smoothstep(0.0022, 0.0, length(sk - pos)); }
    { vec2 dd = normalize(vec2(1.0, -0.22)); vec2 head = vec2(-0.9, 0.62) + dd * (uTime - 33.0) * 0.045;
      for (int k = 0; k < 14 + iZero; k++) { float fk = float(k); vec2 pos = head - dd * (fk * 0.011 + 0.004 * h21(vec2(fk, 9.0))); c += vec3(0.9, 0.95, 1.0) * 0.7 * smoothstep(0.002, 0.0, length(sk - pos)); } }
  } else if (MD == 1) {
    c = mix(vec3(0.72, 0.7, 0.66), vec3(0.4, 0.46, 0.55), pow(e, 0.5));
    float ds = max(dot(rd, SUN1), 0.0);
    c += vec3(1.0, 0.95, 0.85) * (0.3 * pow(ds, 10.0) + 0.5 * pow(ds, 150.0)) + vec3(1.0, 0.99, 0.96) * 6.0 * smoothstep(0.99985, 0.99994, ds);
    if (rd.y > 0.0) { vec2 cp = rd.xz / (rd.y + 0.05) * 0.5; float cd = smoothstep(0.38, 0.78, fb(cp + vec2(0.0, uTime * 0.01)));
      c = mix(c, vec3(0.8, 0.8, 0.79) + vec3(0.2, 0.15, 0.08) * pow(ds, 3.0), cd * (0.45 + 0.4 * smoothstep(0.55, 0.0, e))); }
  } else if (MD == 2) {
    // a dim day: the light comes from the Moon now
    c = mix(vec3(0.13, 0.14, 0.17), vec3(0.025, 0.035, 0.07), pow(e, 0.5));
    float dm = acos(clamp(dot(rd, MOONL), -1.0, 1.0));
    c += vec3(0.8, 0.86, 1.0) * (0.5 * exp(-dm * 16.0) + 0.1 * exp(-dm * 2.5));
    c += vec3(1.0, 0.99, 0.97) * 60.0 * smoothstep(0.0066, 0.0058, dm);
    float ds = acos(clamp(dot(rd, RSUN), -1.0, 1.0));
    vec3 red = vec3(0.6, 0.11, 0.03) * (0.85 + 0.3 * fb(vec2(atan(rd.x, rd.z), rd.y) * 900.0));
    c = mix(c, red * (1.5 - 0.5 * smoothstep(0.0, 0.0105, ds)), smoothstep(0.0108, 0.0101, ds));
    c += vec3(0.85, 0.22, 0.06) * (0.12 * exp(-ds * 22.0) + 0.05 * exp(-ds * 3.5)) * smoothstep(-0.02, 0.06, rd.y);
    c += starfield(rd, 0.25 * smoothstep(0.3, 0.8, e));
  } else {
    c = mix(vec3(0.01, 0.011, 0.016), vec3(0.0015, 0.002, 0.004), pow(e, 0.5));
    c += starfield(rd, 1.0);
  }
  return c;
}
vec3 fogCol(vec3 rd){ return sky(normalize(vec3(rd.x, 0.012, rd.z))) * (0.3 + 0.7 * exp(-max(-rd.y, 0.0) * 9.0)); }   // haze seen from above is dimmer than the horizon
float fogK(){ return MD == 0 ? 0.00022 : MD == 1 ? 0.00009 : MD == 2 ? 0.00016 : 0.0002; }

/* ---------- main ---------- */
void main(){
  SUN0 = normalize(SUN0); SUN1 = normalize(SUN1); MOONL = normalize(MOONL); RSUN = normalize(RSUN);
  vec2 ndc = vUV * 2.0 - 1.0; float asp = uRes.x / uRes.y; float tf = tan(uFov * 0.5);
  ro = vec3(uCamX, uH, 40.0);
  vec3 fw = normalize(vec3(sin(uYaw) * cos(uPitch), sin(uPitch), -cos(uYaw) * cos(uPitch))); vec3 rt = normalize(cross(fw, vec3(0, 1, 0))); vec3 up = cross(rt, fw);
  vec3 rd = normalize(fw + ndc.x * tf * asp * rt + ndc.y * tf * up);
  if (MD == 1) rd.y += (n2(vec2(rd.x * 260.0, uTime * 4.0)) - 0.5) * 0.0005 * smoothstep(0.03, 0.0, abs(rd.y));   // heat shimmer over the salt
  rd = normalize(rd);
  // march the structures; the ground is a plane, found exactly
  float tg = rd.y < 0.0 ? -ro.y / rd.y : 1e9;
  float t = 0.0, mat = -1.0, id = 0.0; vec3 lq = vec3(0.0); bool hit = false;
  float tmax = min(tg, MD == 0 ? 9000.0 : 1300.0);
  float ceil_ = MD == 0 ? 56.0 : 140.0;   // nothing stands taller than this (the stacks; the basin halls)
  if (ro.y > ceil_) { if (rd.y < 0.0) t = (ro.y - ceil_) / -rd.y; else t = 1e9; }
  if (off(1)) t = 1e9;
  int steps = 0;
  for (int i = 0; i < 200 + iZero; i++) { vec3 p = ro + rd * t; float m, idd; vec3 qq; float d = scene(p, m, idd, qq); steps = i;
    if (d < 0.0012 * t + 0.006) { hit = true; mat = m; id = idd; lq = qq; break; }
    t += max(d * 0.8, t * 0.0015); if (t > tmax || (p.y > 30.0 && rd.y >= 0.0 && length(p - DOME) > DOME_R + 2.0)) break; }
  if (!hit && tg < 9000.0) { hit = true; t = tg; mat = 0.0; }
  // the escarpment, a height field far off
  if (!off(32) && MD != 0 && rd.y < 0.16 && !hit) { float tt = 1300.0, prevD = ro.y + rd.y * tt, prevT = tt;
    for (int i = 0; i < 150 + iZero; i++) { vec3 p = ro + rd * tt; float hh = hallH(p.xz); float dd = p.y - max(hh, escH(p.xz));
      if (dd < 0.0) { float f = prevD / (prevD - dd + 1e-6); t = mix(prevT, tt, f); hit = true; mat = hh > 0.0 && p.y < hh + 1.0 ? 1.0 : 4.0; if (mat < 1.5) { vec3 ph = ro + rd * t; lq = vec3(mod(ph.x, HX) - HX * 0.5, ph.y, mod(ph.z, HZ) - HZ * 0.5); id = h21(vec2(floor(ph.x / HX), floor(ph.z / HZ)) + 0.37); } break; }
      if (p.y > 1600.0 && rd.y > 0.0) break; prevD = dd; prevT = tt; tt += tt < 5500.0 ? max(9.0, tt * 0.0075) : max(60.0, tt * 0.035); if (tt > 60000.0) break; } }

  vec3 L = MD == 0 ? SUN0 : MD == 1 ? SUN1 : MOONL;
  vec3 col;
  if (hit && off(1024)) { col = vec3(0.3); hit = false; t = 1e9; } else
  if (hit) {
    vec3 p = ro + rd * t; vec3 n = vec3(0.0, 1.0, 0.0);
    if (mat > 0.5 && (mat < 3.5 || mat > 4.5)) { vec2 e = vec2(0.01 * (1.0 + t * 0.002), 0.0); vec3 g = vec3(sceneD(p + e.xyy) - sceneD(p - e.xyy), sceneD(p + e.yxy) - sceneD(p - e.yxy), sceneD(p + e.yyx) - sceneD(p - e.yyx)); n = dot(g, g) > 1e-12 ? normalize(g) : vec3(0.0, 1.0, 0.0); }
    if (mat > 3.5) { float e = 25.0; n = normalize(vec3(escH(p.xz - vec2(e, 0.0)) - escH(p.xz + vec2(e, 0.0)), 2.0 * e, escH(p.xz - vec2(0.0, e)) - escH(p.xz + vec2(0.0, e)))); }
    vec3 alb = vec3(0.1); vec3 emit = vec3(0.0); float specK = 0.0;
    bool inDome = MD != 0 && length(p.xz - DOME.xz) < DOME_R;
    if (mat < 0.5) {
      if (MD == 0) {
        alb = mix(vec3(0.1, 0.085, 0.068), vec3(0.15, 0.125, 0.1), fb(p.xz * 0.04)) * (1.0 - 0.45 * smoothstep(0.62, 0.78, n2(p.xz * 0.9)) * smoothstep(300.0, 20.0, t)) * (0.85 + 0.3 * n2(p.xz * 7.0));
        float ax = abs(p.x - uCamX * 0.0);
        if (ax < 4.2) { alb = vec3(0.035, 0.034, 0.033) * (0.8 + 0.4 * n2(p.xz * 3.0)); specK = 0.4;
          alb += vec3(0.5, 0.38, 0.1) * smoothstep(0.1, 0.06, ax) * step(fract(p.z / 12.0), 0.5) + vec3(0.45) * smoothstep(0.1, 0.05, abs(ax - 3.8)); }
      } else if (inDome) { alb = vec3(0.06, 0.13, 0.04) * (0.6 + 0.7 * fb(p.xz * 0.6));
      } else {
        // salt crust: polygon plates with raised rims, a crust that reads at every distance
        vec2 wp = p.xz + vec2(fb(p.xz * 0.15), fb(p.xz * 0.15 + 5.0)) * 2.5;   // warp, so the polygons are not tiles
        vec2 v = vor(wp * 0.32); float edge = v.y - v.x; float near = smoothstep(220.0, 15.0, t);
        float ridge = smoothstep(0.16, 0.0, edge) * near;
        float big = fb(p.xz * 0.012), fine = n2(p.xz * 5.0);
        alb = mix(vec3(0.6, 0.57, 0.52), vec3(0.8, 0.78, 0.73), big) * (0.9 + 0.14 * fine);
        alb = mix(alb, vec3(0.93, 0.92, 0.89), ridge * 0.8);
        alb = mix(alb, vec3(0.44, 0.4, 0.34), smoothstep(0.6, 0.8, fb(p.xz * 0.004 + 9.0)) * 0.55);
        vec2 eps = vec2(0.06, 0.0);
        vec2 g = vec2(vor((wp + eps.xy) * 0.32).y - vor((wp + eps.xy) * 0.32).x, vor((wp + eps.yx) * 0.32).y - vor((wp + eps.yx) * 0.32).x) - edge;
        n = normalize(n - vec3(g.x, 0.0, g.y) * 4.0 * smoothstep(0.2, 0.0, edge) * near);
        specK = 0.05;
      }
    } else if (mat < 1.5) {
      float rib = smoothstep(0.32, 0.5, abs(fract(lq.x * 1.1) - 0.5)) * step(0.5, abs(n.z));
      float top = step(0.85, n.y), hgt = (9.0 + 5.0 * id) * (MD == 0 ? 1.0 : 2.4);
      alb = (MD == 0 ? vec3(0.085, 0.087, 0.092) : MD == 1 ? vec3(0.07, 0.072, 0.078) : vec3(0.05, 0.05, 0.055)) * (0.85 + 0.25 * rib) * (0.9 + 0.2 * id);
      if (top > 0.5 && p.y > 2.0 * hgt + 0.5) { vec2 fan = fract(vec2(lq.x / 2.2, lq.z / 2.1)) - 0.5; alb = vec3(0.16, 0.16, 0.165) * (0.6 + 0.4 * smoothstep(0.32, 0.38, length(fan))); }
      if (MD == 0) {
        // dock lights along the walls, warm; a lit band of louvres near the top
        float wall = step(0.5, abs(n.z)) + step(0.5, abs(n.x)); float u = abs(n.z) > 0.5 ? lq.x : lq.z;
        float lamp = smoothstep(0.45, 0.0, length(vec2(mod(u + 7.0, 14.0) - 7.0, p.y - 4.2))) * wall;
        emit += vec3(1.0, 0.68, 0.36) * lamp * 4.0;
        emit += vec3(1.0, 0.6, 0.3) * 0.03 * wall * smoothstep(0.6, 0.0, abs(p.y - (2.0 * hgt - 2.0))) * (0.6 + 0.4 * n2(vec2(u * 0.4, id * 9.0)));
        float pulse = pow(max(sin(uTime * 3.1416 * 1.0), 0.0), 3.0);   // aviation lights blink together across the whole field
        float r = max(0.9, t * 0.0016); float corner = smoothstep(r, 0.0, length(vec2(abs(lq.x) - 104.0, abs(lq.z) - 23.0))) * step(2.0 * hgt - 0.3, p.y);
        float stackTop = smoothstep(max(1.4, t * 0.002), 0.0, length(vec3(lq.x + 112.0, p.y - 52.0, lq.z - 30.0))) * step(0.55, id);
        emit += vec3(1.0, 0.05, 0.02) * (corner + stackTop) * pulse * 30.0;
      } else if (MD >= 2) { emit += vec3(1.0, 0.6, 0.3) * 0.6 * step(0.985, h21(floor(vec2(lq.x / 6.0, p.y / 3.0)) + id)) * step(0.5, abs(n.z)) * (MD == 3 ? 0.5 : 1.0); }
    } else if (mat < 2.5) {
      float trunk = step(p.y, 4.0) * step(0.9, length(n.xz)) * step(fb3(p * 0.7), 0.6);
      alb = mix(vec3(0.05, 0.11, 0.03) * (0.5 + 1.0 * fb3(p * 0.8)), vec3(0.12, 0.09, 0.06), trunk);
      if (p.y < 2.0 && length(p.xz - DOME.xz) > 14.0 && MD == 1) alb = mix(alb, vec3(0.05, 0.045, 0.045), step(0.5, abs(n.x) + abs(n.z)) * 0.0);
      emit += vec3(1.0, 0.72, 0.42) * 0.015 * uDomeLight;
    } else if (mat < 3.5) { alb = vec3(0.03, 0.028, 0.027);
    } else if (mat < 4.5) { alb = mix(vec3(0.5, 0.44, 0.36), vec3(0.62, 0.56, 0.47), fb(p.xz * 0.002)) * (0.8 + 0.3 * smoothstep(0.6, 1.0, n.y)); } else { alb = vec3(0.08); }
    // light
    vec3 lightC = MD == 0 ? vec3(0.0) : MD == 1 ? vec3(1.0, 0.94, 0.82) : MD == 2 ? vec3(0.62, 0.68, 0.82) : vec3(0.0);
    float dif = max(dot(n, L), 0.0);
    float sh = 1.0; bool caster = MD == 2 && length(p.xz - vec2(5.0, 16.0)) < 14.0; bool nearDome = length(p.xz - DOME.xz) < DOME_R + 4.0;
    if (!off(128) && (MD == 1 || MD == 2) && dif > 0.0 && caster && mat < 3.5) sh = shadow(p + n * 0.05, L, 60.0);
    float ao = (t < 250.0 && mat < 3.5 && (MD == 0 || caster || nearDome)) ? occlusion(p, n) : 1.0;
    vec3 amb;
    if (MD == 0) { vec2 hs = normalize(SUN0.xz); float face = max(dot(normalize(n.xz + 1e-4), hs), 0.0) * (1.0 - abs(n.y));
      amb = vec3(0.03, 0.036, 0.06) * (0.6 + 0.4 * n.y) + vec3(0.5, 0.2, 0.07) * 0.14 * face; }
    else if (MD == 1) amb = vec3(0.27, 0.29, 0.33) * (0.6 + 0.4 * n.y) + vec3(0.4, 0.38, 0.34) * 0.18 * (1.0 - n.y);
    else if (MD == 2) amb = vec3(0.05, 0.055, 0.075) * (0.6 + 0.4 * n.y);
    else amb = vec3(0.012, 0.013, 0.017) * (0.6 + 0.4 * n.y) * (0.3 + 0.7 * uStars);
    col = alb * (lightC * dif * sh + amb * ao) + emit;
    if (MD == 2) { float d2 = max(dot(n, RSUN), 0.0); float s2 = (d2 > 0.0 && caster && mat < 3.5) ? shadow(p + n * 0.05, RSUN, 60.0) : 1.0; col += alb * vec3(0.55, 0.1, 0.03) * 0.55 * d2 * s2; }
    if (specK > 0.0 && (MD == 1 || MD == 2)) col += lightC * specK * pow(max(dot(reflect(rd, n), L), 0.0), 60.0) * sh;
    if (mat > 1.5 && mat < 2.5) { col += alb * vec3(1.0, 0.75, 0.45) * 0.5 * uDomeLight * ao; if (MD == 1) col += vec3(0.25, 0.4, 0.08) * 0.35 * pow(max(dot(rd, L), 0.0), 3.0) * sh; }
    // street lights down the road into the campus: pools of sodium on the asphalt and the scrub
    if (MD == 0 && mat < 0.5) { float z0 = floor((p.z - 20.0) / 36.0) * 36.0 + 20.0;
      for (int k = 0; k < 2; k++) { float zl = z0 + float(k) * 36.0; vec3 lp = vec3(7.0, 9.0, zl); float dd = length(p - lp); col += alb * vec3(1.0, 0.55, 0.2) * 22.0 / (dd * dd + 4.0) * (0.4 + 0.6 * max(dot(n, normalize(lp - p)), 0.0)); }
      }
    // the mirage: far across the salt, the ground gives back the sky, like water that isn't there
    if (MD == 1 && mat < 0.5 && !inDome) { float m = smoothstep(500.0, 2600.0, t); vec3 rr = reflect(rd, vec3(0.0, 1.0, 0.0)); rr.y += (n2(vec2(rd.x * 400.0, uTime * 6.0)) - 0.5) * 0.002; col = mix(col, sky(normalize(rr)) * 0.92, m * 0.8); }
    float fk = fogK(); if (MD == 1 && mat > 3.5) fk *= 0.75;
    float fog = 1.0 - exp(-t * fk); col = mix(col, fogCol(rd), fog);
  } else col = off(2) ? vec3(0.1) : sky(rd);

  // steam: columns rising from the far halls into the deck (the basin), faint and cold later
  if (MD == 1 && !off(16)) {
    float tmx = hit ? t : 30000.0; vec3 acc = vec3(0.0); float tr = 1.0;
    for (int k = 0; k < 5 + iZero; k++) { float fk = float(k); vec3 c0 = vec3(-1500.0 + fk * 1100.0 + 300.0 * sin(fk * 3.0), 0.0, -2300.0 - 900.0 * h21(vec2(fk, 1.0)) - fk * 380.0); float rad = 150.0 + 70.0 * h21(vec2(fk, 2.0));
      if (MD == 2 && k > 1) break;
      vec2 oc = ro.xz - c0.xz; float R3 = rad * 4.0; float b = dot(oc, rd.xz), cc = dot(oc, oc) - R3 * R3, a2 = max(dot(rd.xz, rd.xz), 1e-5); float disc = b * b - a2 * cc; if (disc < 0.0) continue;
      float t0 = max((-b - sqrt(disc)) / a2, 0.0), t1 = min((-b + sqrt(disc)) / a2, tmx); if (t1 <= t0) continue;
      for (int j = 0; j < 12 + iZero; j++) { float tt = mix(t0, t1, (float(j) + 0.5 + 0.5 * h21(gl_FragCoord.xy + float(j))) / 12.0); vec3 p = ro + rd * tt; float hgt = p.y; if (hgt < 0.0 || hgt > 4200.0) continue;
        float r = rad * (1.0 + hgt / 700.0); vec2 ctr = c0.xz + vec2(sin(hgt * 0.0015 + fk) * 160.0 + hgt * 0.12, 0.0); float dd = length(p.xz - ctr);
        if (dd > r * 1.25) continue;
        vec3 sp = vec3(p.xz * 0.004, hgt * 0.0025 - uTime * 0.12); float bl = 0.5 * n3(sp) + 0.25 * n3(sp * 2.03 + 7.3) + 0.125 * n3(sp * 4.1 + 3.1) + 0.0625;
        float den = smoothstep(r, r * 0.7, dd + (bl - 0.5) * r * 1.1) * smoothstep(4200.0, 1800.0, hgt);
        vec3 nn = normalize(vec3(p.x - ctr.x, 0.0, p.z - ctr.y)); float side = 0.5 + 0.5 * dot(nn, normalize(vec3(L.x, 0.0, L.z)));
        float a = clamp(den * (t1 - t0) / 12.0 * 0.012, 0.0, 1.0);
        float lump = 0.55 + 0.9 * n3(vec3(p.xz * 0.011, hgt * 0.009 - uTime * 0.25)) * bl;   // cauliflower billows, lit and shadowed
        vec3 sc = MD == 1 ? mix(vec3(0.46, 0.48, 0.53), vec3(1.2, 1.14, 1.02), side) : mix(vec3(0.07, 0.075, 0.09), vec3(0.3, 0.32, 0.38), side);
        sc *= lump * mix(0.7, 1.0, smoothstep(0.0, 1200.0, hgt)); sc = mix(sc, fogCol(rd), 1.0 - exp(-tt * fogK() * 0.8));
        acc += tr * a * sc; tr *= 1.0 - a; if (tr < 0.02) break; } }
    col = col * tr + acc;
  }
  // the dome: a geodesic frame, glass that gives back the sky
  if (MD != 0 && !off(64)) { vec3 oc = ro - DOME; float b = dot(oc, rd), c = dot(oc, oc) - DOME_R * DOME_R, h = b * b - c;
    if (h > 0.0) { float tgl = -b - sqrt(h); vec3 p = ro + rd * tgl; if (tgl > 0.0 && p.y > 0.0 && (!hit || tgl < t)) { vec3 n = normalize(p - DOME); float fr = 0.04 + 0.96 * pow(1.0 - max(dot(-rd, n), 0.0), 5.0); vec3 refl = sky(reflect(rd, n));
      vec2 sp = vec2(atan(n.z, n.x) * 7.0, asin(n.y) * 8.0); vec2 tri = vec2(sp.x + sp.y * 0.5, sp.y * 0.866); vec2 f1 = abs(fract(tri) - 0.5); float f2 = abs(fract(tri.x - tri.y) - 0.5);
      float w = 0.485 - 0.02 * smoothstep(60.0, 300.0, tgl); float frame = max(max(smoothstep(w, 0.5, f1.x), smoothstep(w, 0.5, f1.y)), smoothstep(w, 0.5, f2)) * smoothstep(0.0, 0.04, n.y);
      float spec = pow(max(dot(reflect(rd, n), L), 0.0), 400.0) * (MD == 1 ? 14.0 : MD == 2 ? 8.0 : 0.0);
      vec3 fcol = MD == 1 ? vec3(0.85, 0.85, 0.83) * (0.35 + 0.65 * max(dot(n, L), 0.0)) : MD == 2 ? vec3(0.2, 0.22, 0.27) * (0.3 + 0.7 * max(dot(n, L), 0.0)) : vec3(0.01);
      col = mix(col * vec3(0.8, 0.86, 0.85), refl, fr * 0.9);
      col = mix(col, fcol, frame) + vec3(1.0, 0.98, 0.95) * spec * (1.0 - frame);
      col = mix(col, fogCol(rd), 1.0 - exp(-tgl * fogK())); } } }
  // the launch: a flame climbing from beyond the campus; high up the plume reaches the sunlight and opens like a jellyfish (samples from film.js, PLUME_S)
  if (MD == 0 && uLaunch > 0.0 && !off(8)) {
    vec3 w = uRk - ro; float dist = length(w); float tc = dot(w, rd); float tHit = hit ? t : 1e9;
    if (tc > 0.0 && dist < tHit + 20.0) { float ang = length(w - rd * tc) / dist; col += vec3(1.0, 0.86, 0.62) * (30.0 * exp(-pow(ang / 0.0011, 2.0)) + 1.2 * exp(-ang / 0.006)) * smoothstep(0.0, 0.03, uLaunch); }
    vec3 lit = vec3(0.0); float od = 0.0;
    for (int j = 0; j < 40 + iZero; j++) { vec4 P = uPl[j]; if (P.w <= 0.0) break; vec3 wc = P.xyz - ro; float tq = dot(wc, rd); if (tq <= 0.0 || tq > tHit) continue;
      float dp2 = max(dot(wc, wc) - tq * tq, 0.0), w2 = P.w * P.w; if (dp2 > 6.0 * w2) continue;
      float lobe = mix(1.0, 0.55 + 0.9 * n2(vec2(float(j) * 0.7, sqrt(dp2) / P.w * 2.5 + uTime * 0.4)), uPc[j].w > 0.0 ? 1.0 : 0.0);
      float dens = exp(-dp2 / w2) * abs(uPc[j].w) * lobe; lit += uPc[j].rgb * dens * exp(-od); od += dens * 0.6; }
    col = col * exp(-od * 0.5) + lit;
    col += vec3(1.0, 0.55, 0.25) * 0.05 * smoothstep(0.0, 0.06, uLaunch) * exp(-abs(rd.y) * 30.0) * exp(-(atan(rd.x, -rd.z) - 0.127) * (atan(rd.x, -rd.z) - 0.127) * 60.0);
  }
  // the perimeter fence: chain link reads as a veil at this distance
  if (MD == 0 && rd.z < 0.0) { float tf = (-70.0 - ro.z) / rd.z; vec3 fp = ro + rd * tf; if (tf > 0.0 && (!hit || tf < t) && abs(fp.x) > 18.0 && fp.y > 0.0 && fp.y < 3.0) {
    col = mix(col, vec3(0.03, 0.03, 0.035), 0.22 + 0.1 * smoothstep(0.35, 0.5, abs(fract(fp.y * 3.0 + fp.x * 3.0) - 0.5))); }
    if (tf > 0.0 && (!hit || tf < t) && abs(fp.x) > 18.0 && abs(fp.y - 3.0) < max(0.02, tf * 0.0006)) col = mix(col, vec3(0.25, 0.18, 0.14), 0.6); }
  // street lights as lamps, receding down the road
  vec3 la = vec3(7.0, 9.0, 20.0) - ro, lu = vec3(0.0, 0.0, -1.0); vec3 lc_ = cross(rd, lu); float lineAng = abs(dot(la, normalize(lc_ + 1e-6))) / max(length(la - lu * dot(la, lu)), 1.0);
  if (MD == 0 && !off(4) && lineAng < 0.02) { float tHit = hit ? t : 1e9;
    for (int k = 0; k < 40 + iZero; k++) { vec3 lp = vec3(7.0, 9.0, 20.0 - 36.0 * float(k)); vec3 w = lp - ro; float tc = dot(w, rd); if (tc <= 0.0) continue; float dist = length(w); if (dist > tHit + 1.0) continue;
      float ang = length(w - rd * tc) / dist; float px = 0.0006 + 0.25 / dist * 0.002; col += vec3(1.0, 0.62, 0.28) * (5.0 * exp(-pow(ang / px, 2.0)) + 0.025 * exp(-ang / (px * 5.0))) * exp(-dist * 0.0004); } }
  col = mix(col, MD == 1 ? vec3(0.93, 0.93, 0.91) : MD == 0 ? vec3(0.03, 0.03, 0.05) : vec3(0.05, 0.055, 0.07), uHaze);
  if (isnan(col.r + col.g + col.b) || isinf(col.r + col.g + col.b)) col = vec3(0.0);
  if (off(256)) col = vec3(float(steps) / 200.0, float(steps) / 400.0, 0.0) * 0.6;
  o = vec4(col * uFade, 0.0);
}`;
function ground(mode, t, cam) {
  if (window.GDBG) Object.assign(cam, window.GDBG);   // development: override the ground camera from the console
  E.camera([0, 0, 0], [0, 0, -1], [0, 1, 0], 40);
  if (!NOISE) { const nt = E.noiseTextures(); NOISE = { uN2: nt.n2, uN3: nt.n3 }; }
  if (!GROUND) GROUND = [0, 1, 2, 3].map(m => E.program(GROUND_FS.replace("precision highp float;", `precision highp float;\n#define MD ${m}\n`)));
  // each mood renders at the size its cost allows at 60 fps on a laptop GPU; the grain and bloom are added at full size
  E.fullscreenAt(cam.scale ?? [0.85, 0.45, 0.6, 0.75][mode], GROUND[mode], { uMode: mode, uTime: cam.time ?? t, uH: cam.h, uCamX: cam.x || 0, uPitch: cam.pitch, uYaw: cam.yaw || 0, uLaunch: cam.launch || 0, uStars: cam.stars ?? 1, uFade: cam.fade ?? 1, uHaze: cam.haze || 0, uDomeLight: cam.domeLight ?? 1, uFov: (cam.fov || 50) * D2R, uDbg: cam.dbg || 0, iZero: 0, ...TREES, ...plumeTable(cam.launch || 0), uRk: rocketAt(cam.launch || 0) }, NOISE);
}
const TREES = (() => {   // the garden's trees in dome-local metres: trunk base, trunk top, five canopy spheres, a bounding sphere
  const fr = x => x - Math.floor(x), TS = [], TA = [], TT = [], TB = [];
  for (let k = 0; k < 11; k++) { const seed = k + 1, hgt = 6 + 4 * fr(seed * 7.3), cr = 2.3 + 1.1 * fr(seed * 3.7);
    const bx = Math.sin(k * 2.4 + 0.5) * (4 + k * 1.8), bz = Math.cos(k * 2.4 + 0.5) * (4 + k * 1.6) - 4;
    TA.push(bx, 0, bz, 0); TT.push(bx + 0.4 * Math.sin(seed * 9), hgt * 0.62, bz + 0.3 * Math.cos(seed * 4), 0);
    const sp = []; for (let j = 0; j < 5; j++) { const c = [bx + Math.sin(seed * 3 + j * 1.9) * cr * 0.75, hgt * (0.6 + 0.1 * j), bz + Math.cos(seed * 5 + j * 2.3) * cr * 0.75], r = cr * (1 - 0.13 * j); sp.push([c, r]); TS.push(c[0], c[1], c[2], r); }
    const pts = [[bx, 0, bz, 0.3], ...sp.map(([c, r]) => [c[0], c[1], c[2], r])], cen = [0, 1, 2].map(i => pts.reduce((a, q) => a + q[i], 0) / pts.length);
    const rad = Math.max(...pts.map(q => Math.hypot(q[0] - cen[0], q[1] - cen[1], q[2] - cen[2]) + q[3])) + 2.0; TB.push(cen[0], cen[1], cen[2], rad); }
  return { uTS: TS, uTA: TA, uTT: TT, uTB: TB };
})();
function plumeTable(launch) {   // 40 samples along the climb: centre and width, light colour and density
  const Pl = new Float32Array(160), Pc = new Float32Array(160); if (launch <= 0) return { uPl: Pl, uPc: Pc };
  const shadowAlt = 15500, rk = rocketAt(launch);
  for (let j = 0; j < 40; j++) { const uj = (j + 0.5) / 40 * launch, c = rocketAt(uj), age = (launch - uj) * 5.8;
    const c0 = rocketAt(launch * j / 40), c1 = rocketAt(launch * (j + 1) / 40), step = Math.hypot(c1[0] - c0[0], c1[1] - c0[1], c1[2] - c0[2]);
    const sun = ss(shadowAlt - 1500, shadowAlt + 1500, c[1]), wd = Math.max(30 + 0.006 * c[1] + age * lerp(50, 420, sun), step * 0.9);
    const dens = step / wd * lerp(0.1, 0.1, sun) / (1 + age * 0.2), glow = 3.0 * Math.exp(-Math.hypot(c[0] - rk[0], c[1] - rk[1], c[2] - rk[2]) / 1200);
    const lc = mixv([glow + 0.07, glow * 0.55 + 0.06, glow * 0.25 + 0.07], [0.68, 0.88, 1.1], sun);
    Pl.set([c[0], c[1], c[2], wd], j * 4); Pc.set([lc[0], lc[1], lc[2], sun > 0.5 ? dens : -dens], j * 4); }
  return { uPl: Pl, uPc: Pc };
}
const rocketAt = u => [900 - 1500 * u * u, 60000 * Math.pow(u, 1.8), -7000 - 9000 * u * u];
function sCampus(t) {   // 0:33–0:41: down to the campus at dusk; a launch rises beyond it and the camera follows it up
  const d = ease(ss(33, 35.4, t)), launch = ss(35.6, 41, t);
  const h = lerp(520, 1.8, d), x = lerp(-60, -9, d);
  let pitch = lerp(-1.25, 0.045, d), yaw = lerp(0.35, 0.03, d), fov = lerp(55, 40, d);
  const follow = ease(ss(36.4, 39.5, t));
  if (follow > 0) { const rk = rocketAt(launch), w = sub(rk, [x, h, 40]); const ty = Math.atan2(w[0], -w[2]), tp = Math.atan2(w[1], Math.hypot(w[0], w[2]));
    yaw = lerp(yaw, ty, follow); pitch = lerp(pitch, tp - 0.12 * (1 - ss(39.5, 41, t)), follow); fov = lerp(fov, 44, follow); }
  ground(0, t, { h, x, pitch, yaw, launch, haze: (1 - ss(33, 34.2, t)) * 0.9, fov });
}
function sDome(t) {   // 1:12–1:24: down into the dried basin; the dome; then up into the white sky
  const d = ease(ss(72, 75, t));
  const tilt = ease(ss(82.4, 84.4, t));
  ground(1, t, { h: lerp(700, 1.7, d), x: lerp(-8, 10, d), pitch: lerp(lerp(-1.3, 0.07, d), 1.2, tilt), yaw: lerp(-0.1, 0.02, d) + lerp(0, 0.05, ss(75, 82.4, t)), haze: (1 - ss(72, 73.3, t)) * 0.95 + ss(83.6, 84.5, t), fov: lerp(lerp(55, 40, d), 50, tilt), domeLight: 1 });
}
function sTwoSuns(t) {  // 2:18–2:24: a dim day; the Moon is the brighter sun now
  ground(2, t, { h: 1.6, x: lerp(9, 8.4, ss(138, 144, t)), pitch: 0.16, yaw: -0.08, fade: ss(138, 138.4, t) * (1 - ss(143.6, 144, t)), fov: 58, domeLight: 1 });
}
function sLastSky(t) {  // 3:16–3:23: the stars go out; the camera tilts up into the black
  ground(3, t, { h: 1.7, x: 6, pitch: t < 200.6 ? 0.24 : lerp(0.24, 1.5, ease(ss(200.6, 202, t))), yaw: 0.06, stars: 1 - ss(196.2, 200.4, t), fade: ss(195, 195.5, t) * (1 - ss(201.4, 202, t)), fov: 62, domeLight: 0.35 });
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
  if (op > 0) E.sphere({ mode: 1, day: tex.moon, proc: 1, radius: R, sun, desat: 0.2, tint: [1, 1, 1], dayGain: 1.6 * (1 - dim * 0.9), lesC, lesR: 2.6 * ss(158.5, 164, t), lesK: 1.3, rot, opacity: op, time: t });
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
function playersAt(t) { if (t < 222) return players(yearAt(t)).alive.length; if (!GAL || t < 223) return 1; const split = Math.round(Math.exp(lerp(0, Math.log(212), ss(223.5, 231, t)))); if (t < 232) return split; let a = 0; for (let k = 0; k < GAL.ND; k++) if (GAL.death[k] > t) a++; return a; }
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

/* the galaxy's body: arms, dust lanes, star-forming knots, the core; the front; dead domains going dark */
let GALBODY = null;
const GALBODY_FS = `#version 300 es
precision highp float; in vec2 vUV; out vec4 o; uniform vec2 uRes;
uniform vec3 uCamPos, uCamR, uCamU, uCamF; uniform float uTanHalf, uAspect;
uniform float uT, uIR, uFrontOn, uWar, uSplit, uDmax, uK, uAliveFrac; uniform vec3 uSun; uniform vec4 uDomC[106]; uniform vec4 uDomD[53]; uniform vec3 uPC[12];
float h21(vec2 p){ p = fract(p * vec2(123.34, 456.21)); p += dot(p, p + 45.32); return fract(p.x * p.y); }
float n2(vec2 p){ vec2 i = floor(p), f = fract(p); f = f*f*(3.0-2.0*f); return mix(mix(h21(i), h21(i+vec2(1,0)), f.x), mix(h21(i+vec2(0,1)), h21(i+vec2(1,1)), f.x), f.y); }
float fb(vec2 p){ float a = 0.5, s = 0.0; for (int i = 0; i < 5; i++) { s += a * n2(p); p = p * 2.03 + 7.3; a *= 0.5; } return s; }
float spiral(float r, float th, float off, float sig){ float ph = th - log(max(r, 0.5) / 3.0) / tan(0.2269) - off; float d = 0.0;
  for (int k = 0; k < 2; k++) { float x = mod(ph - float(k) * 3.14159 + 3.14159, 6.28318) - 3.14159; d += exp(-x * x / (2.0 * sig * sig)); } return d; }
vec3 redOf(vec3 c){ return vec3(0.85, 0.12, 0.05) * dot(c, vec3(0.33)) * 2.4; }
void main(){
  vec2 ndc = vUV * 2.0 - 1.0; vec3 rd = normalize(uCamF + ndc.x * uTanHalf * uAspect * uCamR + ndc.y * uTanHalf * uCamU); vec3 ro = uCamPos;
  vec3 col = vec3(0.0);
  if (abs(rd.y) > 1e-4) { float tp = -ro.y / rd.y; if (tp > 0.0) {
    vec3 P = ro + rd * tp; float r = length(P.xz), th = atan(P.z, P.x);
    float disk = exp(-r / 11.0) * smoothstep(50.0, 30.0, r);
    float arms = spiral(r, th, 0.0, 0.32), clump = 0.5 + 0.95 * fb(P.xz * 0.33);
    float dust = spiral(r, th, -0.34, 0.13) * (0.55 + 0.65 * fb(P.xz * 0.6)) * smoothstep(2.5, 8.0, r);
    float knot = pow(clamp(fb(P.xz * 0.95 + 3.0) * 1.25, 0.0, 1.0), 5.0) * arms;
    vec3 c = mix(vec3(1.0, 0.8, 0.56), vec3(0.7, 0.8, 1.0), smoothstep(5.0, 16.0, r)) * disk * (0.3 + 1.7 * arms * clump);
    c += vec3(1.0, 0.42, 0.58) * knot * disk * 2.2;
    c *= 1.0 - 0.8 * dust;
    if (uFrontOn > 0.5) { float dS = length(P.xz - uSun.xz) * (1.0 + 0.32 * (fb(P.xz * 0.2) - 0.5)); float tc = 172.5 + 21.0 * pow(dS / uDmax, 1.25);
      float conv = smoothstep(tc, tc + 0.7, uT); float edge = exp(-((uT - tc) / 0.45) * ((uT - tc) / 0.45));
      c = mix(c, mix(c * 0.08 + redOf(c) * 0.22, redOf(c), uIR), conv) + vec3(1.0, 0.55, 0.18) * edge * disk * 1.6 * (0.4 + arms); }
    else if (uIR > 0.5) c = redOf(c);
    if (uWar > 0.5) {
      vec2 w = vec2(P.x + sin(P.z * 0.7) * 1.6, P.z + cos(P.x * 0.6) * 1.6); float bd = 1e9, bd2 = 1e9; int bi = 0, bi2 = 0;
      for (int k = 0; k < 212; k++) { vec4 cc = uDomC[k / 2]; vec2 c2 = (k % 2 == 0) ? cc.xy : cc.zw; vec2 dv = w - c2; float d = dot(dv, dv); if (d < bd) { bd2 = bd; bi2 = bi; bd = d; bi = k; } else if (d < bd2) { bd2 = d; bi2 = k; } }
      float rip1 = 0.6 * sqrt(bd) / 4.0, rip2 = 0.6 * sqrt(bd2) / 4.0;
      float a1 = 1.0 - smoothstep(uDomD[bi / 4][bi % 4] + rip1, uDomD[bi / 4][bi % 4] + rip1 + 1.4, uT), a2 = 1.0 - smoothstep(uDomD[bi2 / 4][bi2 % 4] + rip2, uDomD[bi2 / 4][bi2 % 4] + rip2 + 1.4, uT);
      float wb = 0.5 + 0.5 * smoothstep(0.0, 6.0, sqrt(bd2) - sqrt(bd)) + 0.2 * (fb(P.xz * 1.1) - 0.5);
      float alive = mix(a2, a1, clamp(wb, 0.0, 1.0)); vec3 tint = mix(uPC[bi2 % 12], uPC[bi % 12], clamp(wb, 0.0, 1.0));
      float seam = (1.0 - smoothstep(0.0, 0.9, sqrt(bd2) - sqrt(bd))) * uSplit;
      c = mix(c, tint * dot(c, vec3(0.33)) * 2.2, uSplit * 0.42) * alive + vec3(1.0, 0.85, 0.7) * seam * 0.06 * disk * alive;
    }
    col += c * uK * smoothstep(0.0, 0.1, abs(rd.y));
  } }
  // the core, integrated through its volume
  vec3 sc = vec3(1.0 / 4.2, 1.0 / 1.6, 1.0 / 3.6); vec3 o2 = ro * sc, d2 = rd * sc; float a = dot(d2, d2), b = dot(o2, d2), cc = dot(o2, o2) - 9.0, disc = b * b - a * cc;
  if (disc > 0.0) { float t0 = max((-b - sqrt(disc)) / a, 0.0), t1 = (-b + sqrt(disc)) / a; if (t1 > t0) { float acc = 0.0; for (int i = 0; i < 16; i++) { float tt = mix(t0, t1, (float(i) + 0.5) / 16.0); vec3 q = (ro + rd * tt) * sc; acc += exp(-0.5 * dot(q, q)); }
    acc *= (t1 - t0) / 16.0; vec3 bc = vec3(1.0, 0.82, 0.58) * min(acc * 0.05, 0.6); if (uIR > 0.5 || (uFrontOn > 0.5 && uT > 175.0)) bc = mix(bc, redOf(bc), uFrontOn > 0.5 ? smoothstep(175.0, 180.0, uT) : 1.0); col += bc * uK * uAliveFrac; } }
  o = vec4(col, 0.0);
}`;
function drawGalaxyBody(t, opt) {
  if (!GALBODY) GALBODY = E.program(GALBODY_FS);
  const G = GAL, c = CAMF;
  if (!G.domC) { G.domC = new Float32Array(424); G.cen.forEach((p, k) => { G.domC[k * 2] = p[0]; G.domC[k * 2 + 1] = p[1]; }); G.domD = new Float32Array(212); G.death.forEach((d, k) => { G.domD[k] = Math.min(d, 9999); });
    let dm = 0; for (let i = 0; i < G.n; i++) dm = Math.max(dm, Math.hypot(G.pos[i * 3] - G.sun[0], G.pos[i * 3 + 2] - G.sun[2])); G.dmax = dm; }
  E.fullscreen(GALBODY, { uCamPos: c.pos, uCamR: c.r, uCamU: c.u, uCamF: c.f, uTanHalf: c.tanHalf, uAspect: c.aspect, uT: t, uIR: opt.ir, uFrontOn: opt.front, uWar: opt.war, uSplit: opt.split, uDmax: G.dmax, uK: opt.k ?? 1, uAliveFrac: opt.alive ?? 1, uSun: G.sun, uDomC: G.domC, uDomD: G.domD, uPC: PCOL.flat() });
}

function sGalaxy(t, cellBack = 1) {
  const G = GAL, c = galaxyCam(t);
  camera(c.pos, c.look, c.fov, 0.01, 1e6); drawStars(0.35);
  const war = t >= 223, front = t >= 170 && t < 202, ir = t >= 202 ? 1 : ss(189.5, 193.5, t);
  const gu = { uT: t, uIR: ir, uWar: war ? 1 : 0, uSplit: ss(223.5, 231, t), uFrontOn: front || t >= 202 ? 1 : 0, uSizeK: 1, uNear: t < 185 ? 1 - ss(172, 182, t) : 0 };
  gu.uPC = PCOL.flat();
  drawGalaxyBody(t, { ir, front: gu.uFrontOn, war: gu.uWar, split: gu.uSplit, alive: war ? aliveFraction(t) : 1, k: ss(10, 40, c.pos[1]) });
  E.drawParticles(SYS.galaxy, { ...gu, uGlow: 0, uSizeK: 0.9 }, { depth: false });
  if (t < 186) { pt(G.cell, [1, 0.62, 0.25], 4 * (1 - ss(176, 180, t)), 10); pt(G.sun, [1, 0.62, 0.25], 5 * (1 - ss(180, 184, t)), 12); flushPts({ depth: false }); }
  // probes leaving the rim, finding nothing
  if (t > 215 && t < 223) { const rr = rngOf(89); for (let k = 0; k < 70; k++) { const i = 34000 + Math.floor(rr() * (G.n - 34000)); const p = [G.pos[i * 3], G.pos[i * 3 + 1], G.pos[i * 3 + 2]]; if (Math.hypot(p[0], p[2]) < 30) continue;
    const d = norm([p[0], 0, p[2]]), t0 = 215.5 + rr() * 4, u = clamp((t - t0) / 3.5), fade = 1 - ss(t0 + 2.8, t0 + 4.5, t); if (u <= 0 || fade <= 0) continue; pt(add(p, scl(d, 2 + u * 40)), AMBER, 4 * fade, 6); } flushPts({ depth: false }); }
  if (war) {
    for (const v of G.volleys) { if (t < v.t0 || t > v.t1 + 0.9) continue; const A = G.src[v.a], B = G.src[v.b]; const pa = [G.pos[A * 3], G.pos[A * 3 + 1] + 0.2, G.pos[A * 3 + 2]], pb = [G.pos[B * 3], G.pos[B * 3 + 1] + 0.2, G.pos[B * 3 + 2]];
      const u = clamp((t - v.t0) / (v.t1 - v.t0)), fade = 1 - clamp((t - v.t1) / 0.9); const head = mixv(pa, pb, u); const bc = mixv([1, 0.95, 0.88], PCOL[v.a % 12], 0.35); ln(pa, head, bc, 5.5 * fade, 2.6); pt(head, [1, 1, 1], 14 * fade * (u < 1 ? 1 : 0), 16); pt(pa, [1, 0.85, 0.7], 6 * fade, 22); }
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
// story-time cues. Cards say each wall in plain words; stamps say where we are.
const CARDS = [
  [9.6, 13.4, "The race for super intelligence.", "2026 · TWELVE PLAYERS"],
  [27.4, 30.6, "Compute passes a terawatt.", "2046 · 1 TW"],
  [47.4, 50.4, "Compute uses as much energy as all of humanity did in 2026.", "2068 · 19 TW"],
  [56.6, 59.6, "The planet can no longer shed its heat.", "2097 · WASTE HEAT 2 W/M²"],
  [69.4, 72, "The oceans become the coolant.", "2113 · 10 PW"],
  [88.4, 91.8, "The Earth is not enough.", "2132 · ALL THE SUNLIGHT THE EARTH RECEIVES"],
  [128.8, 132, "The Sun is enclosed.", "2291 · 3.8 × 10²⁶ W"],
  [149.6, 153.8, "One star is not enough.", "THE PROBES LEAVE"],
  [166.6, 170.4, "The star goes dark.", "A FEW THOUSAND YEARS"],
  [190.2, 194.6, "Every star in the galaxy is taken.", "TWO MILLION YEARS · 10³⁷ W"],
  [224, 228.4, "Nothing is left to win.", ""],
];
const STAMPS = [[33.6, 40.7, "WEST TEXAS"], [73.4, 84.2, "THE DRY MEDITERRANEAN"], [138.3, 143.8, "THE SAME DOME"], [154.4, 162, "ANOTHER STAR"], [195.4, 201.6, "THE SAME DOME · TWO MILLION YEARS LATER"]];
const INSTR = [[7, 33, "VIIRS DAY/NIGHT BAND"], [33, 41, "GROUND"], [41, 50, "VISIBLE"], [50, 59.6, "THERMAL INFRARED  11 µm"], [59.6, 72, "VISIBLE"], [72, 84.5, "GROUND"], [84.5, 128.5, "VISIBLE"], [128.5, 138, "MID-INFRARED  12 µm"], [138, 144, "GROUND"], [144, 170, "VISIBLE"], [170, 191.5, "VISIBLE"], [191.5, 195, "MID-INFRARED  12 µm"], [195, 202, "GROUND"], [202, 272, "MID-INFRARED  12 µm"]];
const CALL = [
  [43, 46.5, "orbital data centres", () => add(EARTH, [0.2, 0.95, 0.75])],
  [45.5, 48.5, "solar fields", () => surf(orbitRot(47), -112, 34, 1.0)],
  [62, 65.5, "mass drivers venting seawater", null, [1460, 300]],
  [66, 69.2, "dry sea floor", () => surf(orbitRot(68), 5, 40, 1.0)],
  [102, 105.5, "mass drivers", () => add(MERC, [0.35, 0.45, 0.3])],
  [108.5, 111, "debris ring", null, [700, 640]],
  [121.5, 125, "collector swarm", () => add(SUN, [SUN_R * 1.6, SUN_R * 1.2, 0])],
  [134, 137.5, "laser relay", () => MOON],
  [145, 148, "self-replicating probes", null, [1250, 380]],
  [233.5, 237.5, "beams powered by whole stars", null, [1180, 300]],
];
const LAST_ABSORB = ABSORB[ABSORB.length - 1][0];
function overlay(t) {
  const on = ss(7.5, 9, t) * (t > 270 ? (Math.floor(t * 14) % 3 === 0 && t < 271.5 ? 1 : 0) : 1) * (t < 274 ? 1 : 0);
  ctx.save(); ctx.textBaseline = "alphabetic";
  const L = 64, T = 64;
  if (on > 0) {
    ctx.globalAlpha = on; ctx.shadowColor = "rgba(0,0,0,0.5)"; ctx.shadowBlur = 10;   // stays legible over the white basin and the clouds
    const lab = (s0, x, y, a = 0.48) => { ctx.font = `500 11px ${MONO}`; ctx.letterSpacing = "3px"; ctx.fillStyle = `rgba(225,232,238,${a})`; ctx.textAlign = "left"; ctx.fillText(s0, x, y); };
    const val = (s0, x, y, c = "rgba(240,244,247,0.94)") => { ctx.font = `400 16px ${MONO}`; ctx.letterSpacing = "1px"; ctx.fillStyle = c; ctx.textAlign = "left"; ctx.fillText(s0, x, y); };
    // the year, large
    lab("YEAR", L, T);
    ctx.font = `200 44px ${SANS}`; ctx.letterSpacing = "2px"; ctx.fillStyle = "rgba(246,248,250,0.97)"; ctx.fillText(fmtYear(yearAt(t)), L - 2, T + 46);
    const yw = ctx.measureText(fmtYear(yearAt(t))).width;
    ctx.font = `600 11px ${MONO}`; ctx.letterSpacing = "3px";
    if (t < 9.5) { ctx.fillStyle = "#ffb15a"; ctx.fillText("TODAY", L + yw + 14, T + 44); } else { ctx.globalAlpha = on * ss(9.5, 11, t) * 0.5; ctx.fillStyle = "#e8eef2"; ctx.fillText("PROJECTED", L + yw + 14, T + 44); ctx.globalAlpha = on; }
    // the rows
    let y = T + 84;
    lab("COMPUTE", L, y); val(fmtW(powerAt(t)), L + 132, y); y += 26;
    const pa = t < 222 ? players(yearAt(t)) : null, pn = playersAt(t);
    lab("PLAYERS", L, y); val(String(pn), L + 132, y, t > 222 ? "#ffb15a" : "rgba(240,244,247,0.94)");
    if (pa) { const yr = yearAt(t); for (let k = 0; k < 12; k++) { const r = pa.root(k), abs = ABSORB.find(e => e[1] === k); const gone = abs ? clamp((yr - abs[0]) / 2.5) : 0; const c = r === k ? PCOL[k] : mixv(PCOL[k], PCOL[r], gone); const sz = 7 * (1 - gone * 0.75);
      ctx.globalAlpha = on * (1 - gone * 0.8); ctx.fillStyle = `rgb(${c.map(v => Math.round(v * 255)).join(",")})`; ctx.fillRect(L + 172 + k * 12 + (7 - sz) / 2, y - 9 + (7 - sz) / 2, sz, sz); } ctx.globalAlpha = on; }
    const lone = ss(LAST_ABSORB, LAST_ABSORB + 1, yearAt(t)) * (1 - ss(62, 64, t));
    if (lone > 0 && t < 70) { ctx.globalAlpha = on * lone; ctx.font = `500 12px ${MONO}`; ctx.letterSpacing = "2px"; ctx.fillStyle = "#ffb15a"; ctx.fillText("ONE PLAYER LEFT", L + 172, y); ctx.globalAlpha = on; }
    y += 26;
    const popA = 1 - ss(142, 144, t); if (popA > 0) { ctx.globalAlpha = on * popA; lab("POPULATION", L, y); val(fmtPop(popAt(t)), L + 132, y); ctx.globalAlpha = on; }
    // where we are, and with what instrument
    for (const [a, b, s0] of STAMPS) if (t >= a && t < b) { const k = ss(a, a + 0.5, t) * (1 - ss(b - 0.4, b, t)); ctx.globalAlpha = on * k; ctx.font = `500 13px ${MONO}`; ctx.letterSpacing = "4px"; ctx.fillStyle = "rgba(246,248,250,0.9)"; ctx.fillText(s0, L, H - 84); }
    for (const [a, b, s0] of INSTR) if (t >= a && t < b) { const k = ss(a, a + 0.4, t) * (1 - ss(b - 0.3, b, t)); ctx.globalAlpha = on * k; lab(s0, L, H - 60, 0.55); }
    ctx.globalAlpha = on;
    // callouts
    for (const [a, b, s0, fn, fallback] of CALL) { if (t < a || t > b) continue; const k = ss(a, a + 0.4, t) * (1 - ss(b - 0.4, b, t)); let p = null;
      if (fn) { const pr = E.project(fn()); if (pr && pr[0] > 0 && pr[0] < W && pr[1] > 0 && pr[1] < H) p = [pr[0], pr[1]]; } else p = fallback;
      if (!p) continue; ctx.globalAlpha = on * k; ctx.fillStyle = "#ffb15a"; ctx.beginPath(); ctx.arc(p[0], p[1], 2.5, 0, TAU); ctx.fill();
      ctx.strokeStyle = "rgba(255,177,90,0.6)"; ctx.lineWidth = 1; ctx.beginPath(); ctx.moveTo(p[0] + 5, p[1] - 5); ctx.lineTo(p[0] + 18, p[1] - 18); ctx.stroke();
      ctx.font = `500 13px ${MONO}`; ctx.letterSpacing = "2px"; ctx.fillStyle = "rgba(245,247,249,0.9)"; ctx.textAlign = "left"; ctx.fillText(s0, p[0] + 24, p[1] - 22); }
    ctx.globalAlpha = 1; ctx.shadowBlur = 0;
  }
  // cards: the wall in plain words
  ctx.textAlign = "center";
  for (const [a, b, line, num] of CARDS) { const k = ss(a, a + 0.45, t) * (1 - ss(b - 0.45, b, t)); if (k <= 0) continue; ctx.globalAlpha = k;
    ctx.font = `300 36px ${SANS}`; ctx.letterSpacing = "0.5px"; ctx.fillStyle = "rgba(247,249,250,0.97)"; ctx.shadowColor = "rgba(0,0,0,0.6)"; ctx.shadowBlur = 18; ctx.fillText(line, W / 2, H * 0.83);
    if (num) { ctx.font = `500 13px ${MONO}`; ctx.letterSpacing = "4px"; ctx.fillStyle = "rgba(255,190,120,0.95)"; ctx.fillText(num, W / 2 + 2, H * 0.83 + 36); } ctx.shadowBlur = 0; }
  // words
  ctx.textBaseline = "middle";
  const word = (s0, k, y, size = 64, alpha = 0.97) => { if (k <= 0) return; ctx.globalAlpha = k; ctx.font = `300 ${size}px ${SANS}`; ctx.letterSpacing = "2px"; ctx.fillStyle = `rgba(246,248,250,${alpha})`; ctx.fillText(s0, W / 2, y); };
  { const k = ss(0.6, 1.4, t) * (1 - ss(5.4, 6.4, t)); if (k > 0) { ctx.globalAlpha = k; ctx.font = `500 13px ${MONO}`; ctx.letterSpacing = "4px"; ctx.fillStyle = "rgba(225,232,238,0.55)"; ctx.fillText("UNITED NATIONS GENERAL ASSEMBLY  ·  22 SEPTEMBER 2026", W / 2, H - 120); } }
  word("super intelligence", ss(1.6, 2.4, t) * (1 - ss(5.6, 6.8, t)), H / 2);
  { const k = ss(76, 77.5, t) * (1 - ss(81.5, 82.5, t)); if (k > 0) { ctx.globalAlpha = k; ctx.font = `500 22px ${MONO}`; ctx.letterSpacing = "12px"; ctx.fillStyle = "rgba(30,32,36,0.8)"; ctx.fillText("PROGRESS", W / 2 + 6, H - 150); } }
  word("super intelligence", ss(206, 207.5, t) * (1 - ss(211.5, 213.5, t)) * 0.5, H * 0.5, 54, 0.9);
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
const SCENES = [[0, "the word"], [7, "today → 2046"], [33, "ground: West Texas"], [41, "orbit"], [50, "thermal"], [59.6, "the oceans"], [72, "ground: the dome"], [84.5, "Earth entire"], [92, "flight inward"], [98.6, "Mercury"], [111.2, "Venus"], [118, "the swarm"], [132, "the relay"], [138, "ground: two suns"], [144, "launch"], [149, "transit"], [154, "the cell"], [171, "the front"], [195, "ground: the last sky"], [202, "efficient"], [223, "the split"], [232, "the beams"], [262, "last light"], [272, "black"], [280, "title"]];
function sceneAt(ft) { const st = storyT(ft); let n = ""; for (const [a, name] of SCENES) if (st >= a) n = name; return `${n}  (story ${st.toFixed(1)})`; }
function frame(ft) {
  if (!ready) throw new Error("not ready");
  const t = storyT(ft);
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
  const names = { earthDay: "assets/earth-day.jpg", earthNight: "assets/earth-night.jpg", mercury: "assets/mercury.jpg", moon: "assets/moon.jpg", clouds: "assets/clouds.jpg" };
  let k = 0; for (const [key, u] of Object.entries(names)) { try { tex[key] = await E.loadTexture(u); } catch (e) { if (key !== "clouds") throw e; } onProgress(++k / 7); }
  if (!new URLSearchParams(location.search).has("regrow")) { try { await loadGrowth(); } catch (e) { buildGrowth(tex.earthNight.img, tex.earthDay.img); } } else buildGrowth(tex.earthNight.img, tex.earthDay.img);
  onProgress(6 / 7);
  buildSystems(); onProgress(1);
  ready = true;
}
const PX = new Uint8Array(4);
function timeFrame(ft) { const a = performance.now(); drawScene(storyT(ft)); E.gl.readPixels(0, 0, 1, 1, E.gl.RGBA, E.gl.UNSIGNED_BYTE, PX); return performance.now() - a; }
return { init, frame, timeFrame, exportGrowth, W, H, DUR, yearAt, powerAt, storyT, filmT, sceneAt, galaxy: () => GAL };
})();
