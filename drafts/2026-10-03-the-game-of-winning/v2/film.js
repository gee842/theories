// The Game of Winning, v2. Scenes follow SCREENPLAY.md; numbers follow ../trajectory.py.
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
const ll = (lon, lat) => { const a = lon * D2R, b = lat * D2R; return [Math.cos(b) * Math.sin(a), Math.sin(b), Math.cos(b) * Math.cos(a)]; };
function slerp(a, b, t) { const d = clamp(dot(a, b), -1, 1), w = Math.acos(d); if (w < 1e-5) return a; const s = Math.sin(w); return add(scl(a, Math.sin((1 - t) * w) / s), scl(b, Math.sin(t * w) / s)); }
const AMBER = [1.0, 0.52, 0.16];

/* ---------- the clock of the film: years, power, population ---------- */
function keyed(keys, t, log) {
  if (t <= keys[0][0]) return keys[0][1];
  for (let i = 1; i < keys.length; i++) if (t <= keys[i][0]) { const [t0, v0] = keys[i - 1], [t1, v1] = keys[i], u = (t - t0) / (t1 - t0); return log ? v0 * Math.pow(v1 / v0, u) : lerp(v0, v1, u); }
  return keys[keys.length - 1][1];
}
const YEARS = [[12, 2026], [20, 2026], [34, 2046], [39, 2050], [48, 2068], [58, 2097], [72, 2113], [82, 2120], [90, 2132], [104, 2170], [110, 2185], [124, 2291], [145, 2300]];
const YEARS_DEEP = [[145, 2300], [147, 11300], [168, 14300], [195, 2002300], [215, 2002300], [232, 2002400], [262, 2600000], [272, 2650000]];
function yearAt(t) { return t < 145 ? keyed(YEARS, t) : keyed(YEARS_DEEP, t, true); }
// trajectory.py: data-centre power 108 GW in 2030, growing 14.7% a year, until it has the whole Sun
const G = Math.pow(945 / 415, 1 / 6) - 1, P2030 = 945e12 / 8766;
function powerAt(t) {
  if (t < 145) return Math.min(3.8e26, P2030 * Math.pow(1 + G, yearAt(t) - 2030));
  if (t < 168) return 3.8e26 * (1 + 0.02 * ss(145, 168, t));
  if (t < 223) return Math.exp(lerp(Math.log(3.9e26), Math.log(1e37), ss(168, 195, t)));
  return 1e37 * aliveFraction(t);
}
// UN World Population Prospects 2024 (medium) until the heat wall; after that the film's illustration
const POP = [[2026, 8.3e9], [2050, 9.66e9], [2084, 10.3e9], [2097, 9.9e9], [2105, 6.1e9], [2110, 3.4e9], [2113, 0.9e9], [2120, 4.2e7], [2291, 2.0e6]];
function popAt(t) { return keyed(POP, yearAt(t), true); }

/* ---------- state ---------- */
let E, ctx, tex = {}, ready = false;
const PT = new Float32Array(8 * 420000), LN = new Float32Array(11 * 90000);
let np = 0, nl = 0;
function pt(p, c, a, size) { if (np >= 420000) return; const o = np * 8; PT[o] = p[0]; PT[o + 1] = p[1]; PT[o + 2] = p[2]; PT[o + 3] = c[0]; PT[o + 4] = c[1]; PT[o + 5] = c[2]; PT[o + 6] = a; PT[o + 7] = size; np++; }
function ln(a, b, c, alpha, w) { if (nl >= 90000) return; const o = nl * 11; LN[o] = a[0]; LN[o + 1] = a[1]; LN[o + 2] = a[2]; LN[o + 3] = b[0]; LN[o + 4] = b[1]; LN[o + 5] = b[2]; LN[o + 6] = c[0]; LN[o + 7] = c[1]; LN[o + 8] = c[2]; LN[o + 9] = alpha; LN[o + 10] = w; nl++; }
function flushPts(opt) { E.points(PT, np, opt); np = 0; }
function flushLns(opt) { E.lines(LN, nl, opt); nl = 0; }

/* ---------- the background sky ---------- */
const STARS = (() => { const r = rngOf(3), s = []; for (let i = 0; i < 9000; i++) { const z = r() * 2 - 1, a = r() * TAU, q = Math.sqrt(1 - z * z); const m = Math.pow(r(), 6); s.push({ d: [q * Math.cos(a), z, q * Math.sin(a)], b: 0.05 + m * 2.2, s: 1 + m * 2.5, w: r() }); } return s; })();
function starfield(center, k = 1) {
  for (const s of STARS) pt(add(center, scl(s.d, 4000)), [0.75 + 0.25 * s.w, 0.82, 1.0 - 0.2 * s.w], s.b * k, s.s);
  flushPts({ persp: 0, depth: true });
}

/* ---------- Earth: real data-centre regions, and the colony grown from them ---------- */
const DC_REGIONS = [[-77.49, 39.04], [-97.0, 32.9], [-112.0, 33.4], [-99.73, 32.45], [-83.0, 40.0], [-84.4, 33.75], [-87.6, 41.9], [-121.9, 37.4], [-122.9, 45.5], [-95.9, 41.3], [-73.6, 45.5],
  [-6.26, 53.35], [-0.1, 51.5], [4.9, 52.37], [8.68, 50.1], [2.35, 48.86], [22.15, 65.58], [-3.7, 40.4], [9.19, 45.46], [21.0, 52.23], [139.7, 35.68], [135.5, 34.7], [126.98, 37.56],
  [114.9, 40.8], [121.5, 31.2], [106.6, 26.6], [113.1, 41.0], [114.2, 22.3], [103.8, 1.35], [103.7, 1.5], [106.8, -6.2], [72.88, 19.07], [80.27, 13.08], [151.2, -33.87], [144.96, -37.8],
  [-46.63, -23.55], [-100.4, 20.6], [28.05, -26.2], [54.38, 24.45], [46.7, 24.7], [34.78, 32.08]];
let NET = null;
function buildNet(nightImg, dayImg) {
  const cv = document.createElement("canvas"); cv.width = 1024; cv.height = 512; const c2 = cv.getContext("2d");
  c2.drawImage(nightImg, 0, 0, 1024, 512); const night = c2.getImageData(0, 0, 1024, 512).data;
  c2.drawImage(dayImg, 0, 0, 1024, 512); const day = c2.getImageData(0, 0, 1024, 512).data;
  const at = (lon, lat) => { const x = clamp(Math.floor((lon + 180) / 360 * 1024), 0, 1023), y = clamp(Math.floor((90 - lat) / 180 * 512), 0, 511), i = (y * 1024 + x) * 4; return { light: (night[i] + night[i + 1] + night[i + 2]) / 765, ocean: day[i + 2] > day[i] * 1.05 && day[i + 2] > day[i + 1] * 0.95 && day[i] < 90 }; };
  const r = rngOf(17), seeds = DC_REGIONS.map(([lo, la]) => ll(lo, la)), nodes = [];
  seeds.forEach((v, i) => nodes.push({ v, year: 2026, seed: true, par: -1, i }));
  let tries = 0;
  while (nodes.length < 5200 && tries < 400000) {
    tries++; const z = r() * 2 - 1, a = r() * TAU, lat = Math.asin(z) / D2R, lon = a / D2R - 180; const s = at(lon, lat);
    if (s.ocean) continue; const p = 0.05 + Math.pow(s.light, 0.6) * 1.4; if (r() > p) continue;
    const v = ll(lon, lat); let d = 9; for (const q of seeds) d = Math.min(d, Math.acos(clamp(dot(v, q), -1, 1)));
    const cost = d * (1.25 - 0.9 * Math.min(1, s.light * 2)) + r() * 0.08;
    nodes.push({ v, cost, seed: false });
  }
  let maxc = 0; nodes.forEach(n => { if (!n.seed) maxc = Math.max(maxc, n.cost); });
  nodes.forEach(n => { if (!n.seed) n.year = 2027 + Math.pow(n.cost / maxc, 0.75) * 84; });
  for (let k = 0; k < 1600; k++) { const z = r() * 2 - 1, a = r() * TAU, lat = Math.asin(z) / D2R, lon = a / D2R - 180; if (!at(lon, lat).ocean) continue; nodes.push({ v: ll(lon, lat), year: 2113 + r() * 9, seed: false }); }
  nodes.sort((a, b) => a.year - b.year);
  // each node links to the nearest node that was already there
  const edges = [];
  for (let i = 0; i < nodes.length; i++) {
    const n = nodes[i]; if (n.seed) continue; let best = -1, bd = -2;
    for (let j = 0; j < i; j++) { const d = dot(n.v, nodes[j].v); if (d > bd) { bd = d; best = j; } }
    const ang = Math.acos(clamp(bd, -1, 1)); edges.push({ a: nodes[best].v, b: n.v, year: n.year, segs: Math.max(1, Math.ceil(ang / 0.015)) });
  }
  NET = { nodes, edges, seeds };
}
function drawNet(t, { intensity = 1, rOff = 1.0012, nodeK = 1, showSeeds = 1 } = {}) {
  const y = yearAt(t), grow = 1.6;
  for (const e of NET.edges) {
    if (e.year > y) continue; const f = clamp((y - e.year) / grow); const k = 1.6 * intensity * (0.55 + 0.45 * clamp(1 - (y - e.year) / 30));
    let prev = scl(e.a, rOff); const n = Math.max(1, Math.round(e.segs * f));
    for (let s = 1; s <= n; s++) { const p = scl(slerp(e.a, e.b, s / e.segs), rOff); ln(prev, p, AMBER, k, 1.35); prev = p; }
  }
  for (const n of NET.nodes) { if (n.year > y) continue; const age = y - n.year; pt(scl(n.v, rOff), AMBER, (age < 1.5 ? 6 * (1 - age / 1.5) + 1.2 : 1.2) * intensity * nodeK, age < 1.5 ? 7 : 3.2); }
  if (showSeeds) for (const s of NET.seeds) pt(scl(s, rOff), [1, 0.62, 0.25], (2.5 + 1.5 * Math.sin(t * 4)) * showSeeds, 9);
  flushLns({ depth: true }); flushPts({ depth: true });
}

/* ---------- scene helpers ---------- */
function orbitCam(dir, dist, look = [0, 0, 0], up = [0, 1, 0], fov = 35) { const d = norm(dir); return E.camera(scl(d, dist), look, up, fov); }
const sunFrom = (camDir, deg, upDeg = 15) => { const d = norm(camDir); const side = norm(cross([0, 1, 0], d)); const a = deg * D2R, b = upDeg * D2R; return norm(add(add(scl(d, Math.cos(a)), scl(side, Math.sin(a))), [0, Math.sin(b), 0])); };

function earthBase(t, camDir, dist, opt = {}) {
  const cam = orbitCam(camDir, dist, opt.look, opt.up, opt.fov);
  starfield([0, 0, 0], 0.8);
  const sun = opt.sun || sunFrom(camDir, 160, 10);
  E.sphere({ mode: 0, day: tex.earthDay, night: tex.earthNight, radius: 1, sun, nightGain: opt.nightGain ?? 1.4, dayGain: opt.dayGain ?? 1.0, thermal: opt.thermal || 0, heat: opt.heat || 0, ocean: opt.ocean ?? 1, atmo: [0.35, 0.6, 1.0], atmoK: 1.0, time: t });
  return cam;
}

/* ---------- 1–3. the word, today, the colony ---------- */
function sToday(t) {
  // 0:12–0:34, three framings
  if (t < 25) { const u = ss(12, 25, t); const dir = ll(lerp(-112, -88, u), lerp(30, 38, u)); earthBase(t, dir, lerp(2.1, 2.3, u), { fov: 36 }); drawNet(t, { showSeeds: t < 20 ? 1 : 0.4 }); }
  else if (t < 29.5) { const u = ss(25, 29.5, t); const dir = ll(lerp(30, 75, u), 62); earthBase(t, dir, 2.6, { fov: 38 }); drawNet(t, { showSeeds: 0.3 }); }
  else { const u = ss(29.5, 34, t); const dir = ll(lerp(10, 40, u), 22); earthBase(t, dir, lerp(3.0, 3.6, u), { fov: 38 }); drawNet(t, { showSeeds: 0 }); }
}

/* ---------- 6. the heat ---------- */
function sHeat(t) {
  const dir = ll(lerp(-20, 10, ss(48, 58, t)), 28);
  const y = yearAt(t), heat = clamp((y - 2050) / 60);
  earthBase(t, dir, 3.1, { thermal: ss(48.2, 49.6, t), heat, fov: 38 });
  drawNet(t, { intensity: 0.6, showSeeds: 0 });
}

/* ---------- 7. the oceans ---------- */
const JETS = (() => { const r = rngOf(29), j = []; for (let i = 0; i < 18; i++) j.push({ u: r(), h: (r() - 0.5) * 1.5, ph: r(), v: 0.7 + r() * 0.5, w: r() }); return j; })();
function sOceans(t) {
  const camDir = ll(-25, 8), sun = sunFrom(camDir, 75, 20);
  const look = scl(ll(-25 + 70, 8), 0.55);
  E.camera(scl(camDir, 2.05), look, [0, 1, 0], 34);
  starfield([0, 0, 0], 0.7);
  const y = yearAt(t), ocean = 1 - 0.75 * ss(2097, 2113, y) - 0.25 * ss(2113, 2122, y);
  E.sphere({ mode: 0, day: tex.earthDay, night: tex.earthNight, radius: 1, sun, nightGain: 1.0, dayGain: 1.0, ocean, atmo: [0.35, 0.6, 1.0], atmoK: 1.1, time: t });
  drawNet(t, { intensity: 0.7, showSeeds: 0 });
  // plumes: seawater thrown off the planet, seen in profile along the limb (a turbulent-column shader)
  const on = ss(58.5, 61, t) * (1 - ss(71, 72, t));
  if (on > 0) {
    if (!PLUME) PLUME = E.program(PLUME_FS);
    const cd = norm(camDir), ex = norm(cross([0, 1, 0], cd)), ey = cross(cd, ex), J = [], K = [];
    for (const j of JETS) {
      const ang = -0.9 + j.u * 2.2, rim = norm(add(add(scl(ex, Math.cos(ang)), scl(ey, Math.sin(ang))), scl(cd, 0.06 + 0.04 * j.h)));
      const hMax = (0.18 + 0.28 * j.v) * ss(58.5 + j.ph * 3, 62 + j.ph * 3, t);
      const p0 = E.project(rim), p1 = E.project(scl(rim, 1 + hMax)); if (!p0 || !p1) continue;
      const dx = p1[0] - p0[0], dy = -(p1[1] - p0[1]);
      J.push(p0[0], H - p0[1], Math.atan2(dy, dx), Math.hypot(dx, dy)); K.push(10 + 16 * j.w, on * (0.35 + 0.35 * j.w), j.ph, 0);
    }
    while (J.length < 96) { J.push(0, 0, 0, 0); K.push(0, 0, 0, 0); }
    E.fullscreen(PLUME, { uTime: t, uN: Math.min(24, JETS.length), uJ: J, uK: K });
  }
}
let PLUME = null;
const PLUME_FS = `#version 300 es
precision highp float; in vec2 vUV; out vec4 o; uniform vec2 uRes; uniform float uTime, uN; uniform vec4 uJ[24]; uniform vec4 uK[24];
float h21(vec2 p){ p = fract(p * vec2(123.34, 456.21)); p += dot(p, p + 45.32); return fract(p.x * p.y); }
float n2(vec2 p){ vec2 i = floor(p), f = fract(p); f = f*f*(3.0-2.0*f); return mix(mix(h21(i), h21(i+vec2(1,0)), f.x), mix(h21(i+vec2(0,1)), h21(i+vec2(1,1)), f.x), f.y); }
float fb(vec2 p){ float a = 0.5, s = 0.0; for (int i = 0; i < 5; i++) { s += a * n2(p); p = p * 2.03 + 7.3; a *= 0.5; } return s; }
void main(){
  vec2 px = vUV * uRes; vec3 col = vec3(0.0);
  for (int i = 0; i < 24; i++) {
    if (float(i) >= uN) break;
    vec4 J = uJ[i], K = uK[i]; if (J.w < 1.0) continue;
    vec2 d = vec2(cos(J.z), sin(J.z)); vec2 rel = px - J.xy; float a = dot(rel, d); float c = dot(rel, vec2(-d.y, d.x));
    if (a < -10.0 || a > J.w * 1.25) continue;
    float u = a / J.w; float w = K.x * (0.3 + 2.2 * u);
    float turb = fb(vec2(a * 0.018 - uTime * 2.2 + K.z * 13.0, c * 0.03 / (0.3 + u) + K.z * 7.0));
    float core = exp(-pow(c / w, 2.0) * 1.3);
    float dens = core * (0.35 + turb) * smoothstep(-0.02, 0.05, u) * (1.0 - smoothstep(0.5, 1.2, u)) * (1.0 - 0.4 * u);
    col += vec3(0.86, 0.91, 1.0) * dens * K.y;
  }
  o = vec4(col, 0.0);
}`;

/* ---------- 10. Mercury ---------- */
const MD = (() => { const r = rngOf(37), m = []; for (let i = 0; i < 40; i++) m.push({ a: r() * TAU, ph: r(), v: 0.6 + r() * 0.6, c: r() }); return m; })();
function sMercury(t) {
  const camDir = norm([0.15, 0.25, 1]), sun = norm([0.85, 0.3, 0.45]);
  E.camera(scl(camDir, 3.3), [0.25, 0.05, 0], [0, 1, 0], 34);
  starfield([0, 0, 0], 0.9);
  const lesC = norm([-0.85, 0.3, 0.45]);
  const R = 1 - 0.35 * ss(100.5, 104, t), lesR = 2.4 * ss(92.5, 101, t), op = 1 - ss(102.5, 104, t);
  const rot = bodyRot(0, 0);
  E.sphere({ mode: 1, day: tex.mercury, radius: R, sun, desat: 0.82, tint: [1.0, 0.97, 0.92], dayGain: 1.5, lesC, lesR, lesK: 1.2, rot, opacity: op, time: t });
  // mass drivers along the front fling ore into orbit
  if (lesR > 0.15) {
    const toWorld = v => [rot[0] * v[0] + rot[1] * v[1] + rot[2] * v[2], rot[3] * v[0] + rot[4] * v[1] + rot[5] * v[2], rot[6] * v[0] + rot[7] * v[1] + rot[8] * v[2]];
    const c = toWorld(lesC), ax = norm(cross(c, [0, 1, 0])), ay = cross(ax, c);
    for (const m of MD) {
      const ang = Math.min(lesR * 0.92, 2.2), dir = add(scl(ax, Math.cos(m.a)), scl(ay, Math.sin(m.a)));
      const p = norm(add(scl(c, Math.cos(ang)), scl(dir, Math.sin(ang))));
      const tang = norm(sub(scl(p, dot(c, p)), c));
      const surf = scl(p, R * 1.003);
      ln(surf, add(surf, scl(tang, 0.18)), AMBER, 2.2 * op, 1.6);
      for (let k = 0; k < 24; k++) {
        const age = ((t * 0.5 * m.v + m.ph + k / 24) % 1);
        const q = add(add(surf, scl(tang, 0.18 + age * 1.6)), scl(p, age * age * 0.9));
        pt(q, [1, 0.7, 0.4], 1.8 * (1 - age) * op + 0.2, 3);
      }
    }
  }
  // the debris ring, gathering as the planet thins
  const ringK = ss(97, 104, t);
  if (ringK > 0) { const r = rngOf(41); for (let i = 0; i < 9000; i++) { const a = r() * TAU, rr = 1.6 + r() * 1.4 + gauss(r) * 0.1, y0 = gauss(r) * 0.03; const vis = r() < ringK; if (!vis) continue; const ang = a + t * 0.05 / rr; pt([Math.cos(ang) * rr, y0 + Math.sin(ang) * rr * 0.12, Math.sin(ang) * rr], [1, 0.62, 0.3], 0.5 * ringK, 1.6); } }
  flushLns({ depth: true }); flushPts({ depth: true });
}

/* ---------- 12. the swarm ---------- */
const SWARM = (() => {
  const r = rngOf(43), n = 240000, planes = [];
  for (let k = 0; k < 64; k++) { const a = r() * TAU, inc = Math.acos(1 - 2 * r()); const nn = norm([Math.sin(inc) * Math.cos(a), Math.cos(inc), Math.sin(inc) * Math.sin(a)]); const ax = norm(cross(nn, [0.3, 0.1, 1])); planes.push({ n: nn, ax, ay: cross(nn, ax), r: 1.7 + r() * 1.9, t0: 111 + 11 * Math.pow(r(), 0.9) }); }
  const s = new Float32Array(n * 6);
  for (let i = 0; i < n; i++) { const k = i % planes.length; s[i * 6] = planes[k].r + gauss(r) * 0.03; s[i * 6 + 1] = r() * TAU; s[i * 6 + 2] = k; s[i * 6 + 3] = r(); s[i * 6 + 4] = planes[k].t0 + r() * 1.5; s[i * 6 + 5] = r(); }
  return { s, n, planes };
})();
function sSwarm(t) {
  const camDir = norm([0.35, 0.32, 1]);
  E.camera(scl(camDir, lerp(14.5, 12.5, ss(110, 124, t))), [0, -0.3, 0], [0, 1, 0], 30);
  starfield([0, 0, 0], 0.9);
  const ir = ss(119.2, 120.6, t);
  let fill = 0; { let c = 0; for (let i = 0; i < SWARM.n; i += 97) if (SWARM.s[i * 6 + 4] <= t) c++; fill = c / Math.ceil(SWARM.n / 97); }
  E.sphere({ mode: 2, radius: 1, emissive: lerp(lerp(3.2, 0.7, fill), 0.55, ir), ir, atmo: ir < 0.5 ? [1.0, 0.72, 0.42] : [0.7, 0.08, 0.03], time: t });
  const vis = [1.0, 0.88, 0.7], red = [0.75, 0.1, 0.035];
  for (let i = 0; i < SWARM.n; i++) {
    const o = i * 6; if (SWARM.s[o + 4] > t) continue;
    const rr = SWARM.s[o], pl = SWARM.planes[SWARM.s[o + 2]], ph = SWARM.s[o + 1] + t * 0.35 / Math.pow(rr, 1.5);
    const p = add(scl(pl.ax, Math.cos(ph) * rr), scl(pl.ay, Math.sin(ph) * rr));
    const glint = Math.pow(SWARM.s[o + 3], 16) * 5 + 0.09;
    const age = clamp((t - SWARM.s[o + 4]) / 0.6);
    const c = ir > 0 ? [lerp(vis[0], red[0], ir), lerp(vis[1], red[1], ir), lerp(vis[2], red[2], ir)] : vis;
    pt(p, c, (lerp(glint, 0.55, ir)) * age, 1.6);
  }
  flushPts({ depth: true });
}

/* ---------- 14. the sky: two suns ---------- */
let SKY = null;
const SKY_FS = `#version 300 es
precision highp float; in vec2 vUV; out vec4 o; uniform vec2 uRes; uniform float uTime, uFade, uSunDim, uMoon, uMode, uStars, uDomeLight;
float h21(vec2 p){ p = fract(p * vec2(123.34, 456.21)); p += dot(p, p + 45.32); return fract(p.x * p.y); }
float n2(vec2 p){ vec2 i = floor(p), f = fract(p); f = f*f*(3.0-2.0*f); return mix(mix(h21(i), h21(i+vec2(1,0)), f.x), mix(h21(i+vec2(0,1)), h21(i+vec2(1,1)), f.x), f.y); }
float fb(vec2 p){ float a = 0.5, s = 0.0; for (int i = 0; i < 6; i++) { s += a * n2(p); p = p * 2.02 + 7.3; a *= 0.5; } return s; }
vec2 vor(vec2 p){ vec2 i = floor(p), f = fract(p); float d1 = 9.0, d2 = 9.0; for (int y = -1; y <= 1; y++) for (int x = -1; x <= 1; x++) { vec2 g = vec2(x, y); vec2 c = g + vec2(h21(i + g), h21(i + g + 3.1)); float d = length(c - f); if (d < d1) { d2 = d1; d1 = d; } else if (d < d2) d2 = d; } return vec2(d1, d2); }
float sdCapsule(vec2 p, vec2 a, vec2 b, float r){ vec2 pa = p - a, ba = b - a; float hh = clamp(dot(pa, ba) / dot(ba, ba), 0.0, 1.0); return length(pa - ba * hh) - r; }
float person(vec2 p, vec2 at, float s, float lean){ p = (p - at) / s; p.x -= p.y * lean;
  float d = length((p - vec2(0.0, 0.93)) * vec2(1.0, 0.85)) - 0.075;                  // head, tilted up
  d = min(d, sdCapsule(p, vec2(0.0, 0.82), vec2(0.0, 0.47), 0.075));                    // torso
  d = min(d, sdCapsule(p, vec2(-0.035, 0.47), vec2(-0.05, 0.02), 0.045)); d = min(d, sdCapsule(p, vec2(0.035, 0.47), vec2(0.055, 0.02), 0.045));
  d = min(d, sdCapsule(p, vec2(-0.05, 0.78), vec2(-0.08, 0.5), 0.034)); d = min(d, sdCapsule(p, vec2(0.05, 0.78), vec2(0.085, 0.5), 0.034)); return d * s; }
void main(){
  vec2 uv = vUV; float asp = uRes.x / uRes.y; vec2 p = vec2((uv.x - 0.5) * asp, uv.y);
  float hz = 0.33; vec3 col;
  vec2 moon = vec2(0.46, 0.8), sun = vec2(-0.55, 0.56);
  float dm = length(p - moon), ds = length(p - sun);
  if (p.y > hz) {
    float e = (p.y - hz) / (1.0 - hz);
    col = mix(vec3(0.045, 0.05, 0.06), vec3(0.004, 0.006, 0.012), pow(e, 0.5));
    if (uMode > 0.5 && uMode < 1.5) col = mix(vec3(0.62, 0.62, 0.6), vec3(0.36, 0.39, 0.43), pow(e, 0.7));
    if (uMode > 1.5) { col = mix(vec3(0.012, 0.014, 0.02), vec3(0.002, 0.003, 0.006), pow(e, 0.5));
      vec2 cell = floor(p * vec2(140.0, 140.0)); float hs = h21(cell); vec2 sp = (cell + vec2(h21(cell + 1.7), h21(cell + 4.1))) / 140.0;
      float star = step(0.975, hs) * step(h21(cell + 9.3), uStars) * smoothstep(0.0022, 0.0, length(p - sp)); col += vec3(0.9, 0.93, 1.0) * star * (1.0 + 6.0 * pow(hs, 40.0)); }
    col += vec3(0.7, 0.78, 0.92) * 0.10 * exp(-dm * 7.0) * uMoon + vec3(0.6, 0.68, 0.8) * 0.03 * exp(-dm * 1.6) * uMoon;
    col += vec3(0.8, 0.22, 0.06) * 0.05 * exp(-ds * 6.0) * step(uMode, 0.5);
    // steam columns: billowing, widening as they rise
    for (int i = 0; i < 4; i++) { float fi = float(i); float x0 = -0.95 + fi * 0.58 + 0.07 * sin(fi * 7.0); float w = 0.015 + 0.11 * e * (0.7 + 0.3 * sin(fi * 3.0));
      float xx = p.x - x0 - 0.06 * e * sin(fi * 2.0 + 1.0); float tw = fb(vec2(xx * 9.0 / (0.3 + e), p.y * 5.0 - uTime * 0.25 + fi * 3.0));
      float c = smoothstep(w, w * 0.2, abs(xx)) * smoothstep(0.0, 0.25, tw - 0.25) * smoothstep(1.05, 0.2, e) * step(uMode, 1.5); col += (uMode > 0.5 ? vec3(0.85, 0.86, 0.86) : vec3(0.42, 0.44, 0.47)) * c * (uMode > 0.5 ? 0.35 : 0.2); }
    // the Moon, receiving the beam: small, white-hot
    col += vec3(1.0, 0.98, 0.94) * 14.0 * uMoon * smoothstep(0.022, 0.019, dm);
    // the enclosed Sun: a dull red disc behind a shimmer of collectors
    float sd = smoothstep(0.03, 0.027, ds) * step(uMode, 0.5); col = mix(col, vec3(0.62, 0.14, 0.045) * 1.3 * uSunDim, sd);
    float ang = atan(p.y - sun.y, p.x - sun.x);
    float ring = smoothstep(0.09, 0.03, ds) * (1.0 - sd);
    float glit = step(0.93, h21(floor(vec2(ang * 60.0, ds * 220.0) + floor(uTime * 6.0))));
    col += vec3(1.0, 0.4, 0.12) * ring * (0.05 + glit * 0.35) * step(uMode, 0.5);
  } else {
    float d = (hz - p.y); float z = 0.05 / max(d, 0.0006); float x = p.x * z;
    vec2 g = vec2(x, z) * 0.9; vec2 v = vor(g * 1.3); float crack = smoothstep(0.05, 0.0, v.y - v.x);
    vec3 salt = mix(vec3(0.30, 0.28, 0.26), vec3(0.40, 0.37, 0.33), fb(g * 0.7));
    col = salt * (1.0 - crack * 0.75) * (uMode > 0.5 && uMode < 1.5 ? 1.15 : uMode > 1.5 ? 0.025 : 0.05 + 0.07 * uMoon);
    float far = smoothstep(2.5, 10.0, z);
    float gx = smoothstep(0.03, 0.0, abs(fract(x * 1.1) - 0.5) - 0.47), gz = smoothstep(0.025, 0.0, abs(fract(z * 2.2) - 0.5) - 0.47);
    float lights = step(0.86, h21(floor(vec2(x * 3.0, z * 4.0)))) * far;
    col += vec3(1.0, 0.52, 0.16) * ((gx + gz) * 0.25 + lights * 1.2) * far * (1.0 - smoothstep(20.0, 80.0, z) * 0.7);
    col = mix(col, uMode > 0.5 && uMode < 1.5 ? vec3(0.62, 0.62, 0.6) : uMode > 1.5 ? vec3(0.012, 0.014, 0.02) : vec3(0.045, 0.05, 0.06), smoothstep(10.0, 60.0, z) * 0.85);
  }
  // the dome
  vec2 dc = vec2(-0.2, hz - 0.003); vec2 q = (p - dc) / vec2(0.34, 0.22); float r = length(q);
  if (q.y > 0.0 && r < 1.0) {
    float fres = pow(r, 7.0); vec3 inner = vec3(1.0, 0.7, 0.4) * 0.16 * (1.0 - q.y * 0.5) * uDomeLight * (uMode > 0.5 && uMode < 1.5 ? 3.0 : 1.0);
    float canopy = 0.22 + 0.14 * fb(vec2(q.x * 7.0, 1.3)) + 0.12 * exp(-pow((q.x + 0.25) * 4.0, 2.0)) + 0.08 * exp(-pow((q.x - 0.35) * 5.0, 2.0));
    inner = mix(inner, vec3(0.02, 0.035, 0.02), smoothstep(0.015, -0.015, q.y - canopy));
    float frame = max(smoothstep(0.01, 0.0, abs(fract(atan(q.y, q.x) / 3.14159 * 10.0) - 0.5) - 0.485), smoothstep(0.008, 0.0, abs(fract(r * 5.0) - 0.5) - 0.485));
    if (uMode > 0.5 && uMode < 1.5) { inner = mix(inner, vec3(0.08, 0.2, 0.08), smoothstep(0.015, -0.015, q.y - canopy) * 0.8);
      for (int k = 0; k < 3; k++) { float fx = -0.35 + float(k) * 0.3; float pf = person(q, vec2(fx, 0.02), 0.2, 0.0); inner = mix(inner, vec3(0.03, 0.03, 0.035), smoothstep(0.004, -0.004, pf)); } }
    vec3 glass = inner + vec3(0.6, 0.66, 0.78) * fres * 0.28 * (uMoon + (uMode > 0.5 && uMode < 1.5 ? 1.6 : 0.0) + (uMode > 1.5 ? 0.15 : 0.0)) + vec3(0.5, 0.55, 0.65) * frame * (uMode > 0.5 && uMode < 1.5 ? 0.18 : 0.05);
    if (uMode > 1.5) { float crk = smoothstep(0.006, 0.0, abs(fb(q * 6.0) - 0.5) - 0.0) * smoothstep(0.2, 0.9, r); glass += vec3(0.5, 0.55, 0.6) * crk * 0.04; }
    glass += vec3(1.0, 0.98, 0.95) * exp(-length(q - vec2(0.5, 0.66)) * 26.0) * 2.2 * uMoon;
    col = mix(col, glass, 0.94);
  }
  // two figures by the glass, looking up toward the Moon
  float f1 = person(p, vec2(0.2, hz - 0.028), 0.07, -0.05), f2 = person(p, vec2(0.245, hz - 0.03), 0.062, -0.08); if (uMode > 0.5) { f1 = 1.0; f2 = 1.0; }
  float fd = min(f1, f2); col = mix(col, vec3(0.006, 0.007, 0.009), smoothstep(0.0012, -0.0012, fd));
  col += vec3(0.7, 0.78, 0.95) * smoothstep(0.0025, 0.0, abs(fd)) * step(0.0, p.x - 0.19) * 0.18 * uMoon;
  o = vec4(col * uFade, 0.0);
}`;
function sSkyTwoSuns(t) {
  E.camera([0, 0, 0], [0, 0, -1], [0, 1, 0], 40);
  if (!SKY) SKY = E.program(SKY_FS);
  const a = ss(130, 130.4, t) * (1 - ss(136.6, 137, t));
  E.fullscreen(SKY, { uTime: t, uFade: a, uSunDim: 1.0, uMoon: 1.0, uMode: 0, uStars: 1, uDomeLight: 1 });
}

/* ---------- 17–23. the galaxy ---------- */
let GAL = null;
function buildGalaxy() {
  const r = rngOf(53), n = 190000, pos = new Float32Array(n * 3), col = new Float32Array(n * 3), b = new Float32Array(n), dom = new Uint16Array(n), seam = new Float32Array(n);
  for (let i = 0; i < n; i++) {
    let x, y, z, c;
    if (i < 34000) { x = gauss(r) * 4.2; z = gauss(r) * 3.6; y = gauss(r) * 1.5; c = [1.0, 0.86, 0.62]; }
    else { const arm = i % 2, rr = 3 + -Math.log(1 - r() * 0.985) * 12; const th = arm * Math.PI + Math.log(rr / 3) / Math.tan(13 * D2R) + gauss(r) * 0.22; x = rr * Math.cos(th) + gauss(r) * 1.1; z = rr * Math.sin(th) + gauss(r) * 1.1; y = gauss(r) * 0.35; const hot = r(); c = hot < 0.2 ? [0.7, 0.8, 1.0] : hot < 0.75 ? [1.0, 0.95, 0.88] : [1.0, 0.8, 0.6]; }
    pos[i * 3] = x; pos[i * 3 + 1] = y; pos[i * 3 + 2] = z; col[i * 3] = c[0]; col[i * 3 + 1] = c[1]; col[i * 3 + 2] = c[2]; b[i] = 0.25 + Math.pow(r(), 4) * 2.5;
  }
  // rival domains: one per swarm cluster
  const ND = 212, cen = []; for (let k = 0; k < ND; k++) { const i = Math.floor(r() * n); cen.push([pos[i * 3], pos[i * 3 + 2]]); }
  for (let i = 0; i < n; i++) { let d1 = 1e9, d2 = 1e9, k1 = 0; const x = pos[i * 3] + Math.sin(pos[i * 3 + 2] * 0.7) * 1.6 + gauss(r) * 0.5, z = pos[i * 3 + 2] + Math.cos(pos[i * 3] * 0.6) * 1.6 + gauss(r) * 0.5; for (let k = 0; k < ND; k++) { const d = (x - cen[k][0]) ** 2 + (z - cen[k][1]) ** 2; if (d < d1) { d2 = d1; d1 = d; k1 = k; } else if (d < d2) d2 = d; } dom[i] = k1; seam[i] = Math.sqrt(d2) - Math.sqrt(d1); }
  // the source star of each domain: the brightest near its centre
  const src = cen.map(c => { let bi = 0, bd = 1e9; for (let i = 0; i < n; i += 7) { const d = (pos[i * 3] - c[0]) ** 2 + (pos[i * 3 + 2] - c[1]) ** 2; if (d < bd) { bd = d; bi = i; } } return bi; });
  // The war, fixed in advance. Deaths are placed so that the number of players follows the screenplay
  // (212 → 40 → 6 → 2), then each death is given a shooter that is still alive and a beam that left in time.
  const PLAYERS = [[232, 212], [248, 40], [258, 6], [262, 2]];
  const Nat = t => keyed(PLAYERS, t, true);
  const rr = rngOf(59), order = [...Array(ND).keys()].sort(() => rr() - 0.5);
  let fa = 0, fb2 = 1, fd = 0; for (let i = 0; i < ND; i++) for (let j = i + 1; j < ND; j++) { const d = Math.hypot(cen[i][0] - cen[j][0], cen[i][1] - cen[j][1]); if (d > fd && Math.hypot(cen[i][0], cen[i][1]) < 30 && Math.hypot(cen[j][0], cen[j][1]) < 30) { fd = d; fa = i; fb2 = j; } }
  const final = [fa, fb2], doomed = order.filter(k => k !== fa && k !== fb2);
  const death = new Float32Array(ND).fill(1e9), volleys = [], sweep = [];
  doomed.forEach((k, i) => { const target = ND - 1 - i; let lo = 232, hi = 262; for (let it = 0; it < 40; it++) { const m = (lo + hi) / 2; if (Nat(m) > target) lo = m; else hi = m; } death[k] = hi + (rr() - 0.5) * 0.08; });
  const dist = (a, b) => Math.hypot(cen[a][0] - cen[b][0], cen[a][1] - cen[b][1]);
  const sweeper = final[1];
  for (const k of doomed) {
    const td = death[k];
    if (td > 254 && td < 257.2) { sweep.push({ t: td, b: k }); continue; }            // the sweep from the far side
    const cands = []; for (let j = 0; j < ND; j++) if (j !== k && death[j] > td + 0.3) cands.push(j);
    let a = cands[Math.floor(rr() * cands.length)]; for (let q = 0; q < 6; q++) { const c2 = cands[Math.floor(rr() * cands.length)]; if (dist(c2, k) < dist(a, k)) a = c2; }
    const travel = Math.min(0.5 + dist(a, k) / 38, td - 232.2);
    volleys.push({ t0: td - travel, t1: td, a, b: k });
  }
  sweep.sort((x, y) => x.t - y.t);
  volleys.push({ t0: 262.6, t1: 268.6, a: final[0], b: final[1] }, { t0: 262.6, t1: 268.6, a: final[1], b: final[0] });
  death[final[0]] = death[final[1]] = 268.6;
  // conversion: the front leaves the Orion Arm (a star two-thirds of the way out along an arm)
  let sunI = 34000, sbest = 1e9; for (let i = 34000; i < n; i += 3) { const rr2 = Math.hypot(pos[i * 3], pos[i * 3 + 2]); const d = Math.abs(rr2 - 24) + Math.abs(pos[i * 3 + 1]) * 3; if (d < sbest) { sbest = d; sunI = i; } }
  const sun = [pos[sunI * 3], pos[sunI * 3 + 1], pos[sunI * 3 + 2]];
  const conv = new Float32Array(n); let dmax = 0;
  for (let i = 0; i < n; i++) { const d = Math.hypot(pos[i * 3] - sun[0], pos[i * 3 + 2] - sun[2]); conv[i] = d; dmax = Math.max(dmax, d); }
  for (let i = 0; i < n; i++) conv[i] = 169 + 25 * Math.pow(conv[i] / dmax, 0.9) + (r() - 0.5) * 1.5;
  // a ripple: within a domain, stars die outward from the centre
  const ripple = new Float32Array(n); { const rad = new Float32Array(ND); for (let i = 0; i < n; i++) { const k = dom[i]; rad[k] = Math.max(rad[k], Math.hypot(pos[i * 3] - cen[k][0], pos[i * 3 + 2] - cen[k][1])); } for (let i = 0; i < n; i++) { const k = dom[i]; ripple[i] = 0.55 * Math.hypot(pos[i * 3] - cen[k][0], pos[i * 3 + 2] - cen[k][1]) / Math.max(rad[k], 1e-3); } }
  GAL = { n, pos, col, b, dom, seam, cen, death, volleys, src, conv, ND, sweep, sweeper, ripple, sun, sunI };
}
function aliveFraction(t) { if (!GAL) return 1; let a = 0; for (let k = 0; k < GAL.ND; k++) if (GAL.death[k] > t) a++; return a / GAL.ND; }
function playersAt(t) { if (!GAL || t < 223) return 1; const split = Math.round(Math.exp(lerp(0, Math.log(212), ss(223.5, 231, t)))); if (t < 232) return split; let a = 0; for (let k = 0; k < GAL.ND; k++) if (GAL.death[k] > t) a++; return a; }
function galCamFull(t) { const ang = 0.3 + t * 0.002; return { pos: [Math.cos(ang) * 50, 52, Math.sin(ang) * 50], look: [0, -3, 0] }; }
function sGalaxyWar(t) {
  const G = GAL; const gc = galCamFull(t);
  E.camera(gc.pos, gc.look, [0, 1, 0], 42);
  starfield([0, 0, 0], 0.35);
  const red = [0.85, 0.12, 0.05];
  for (let i = 0; i < G.n; i++) {
    const k = G.dom[i], dt = t - G.death[k] - G.ripple[i]; if (dt > 0.7) continue;
    const p = [G.pos[i * 3], G.pos[i * 3 + 1], G.pos[i * 3 + 2]];
    let a = G.b[i] * 0.8, c = red;
    const seamK = ss(223.5, 231, t) * clamp(1 - G.seam[i] / 0.35);
    if (seamK > 0) { c = [lerp(red[0], 1.0, seamK), lerp(red[1], 0.75, seamK), lerp(red[2], 0.6, seamK)]; a += seamK * 1.6; }
    if (dt > 0) { c = [1.0, 0.85, 0.7]; a = 9 * (1 - dt / 0.7); }
    pt(p, c, a, 1.4);
  }
  flushPts({ depth: false });
  for (const v of G.volleys) {
    if (t < v.t0 || t > v.t1 + 0.9) continue;
    const A = G.src[v.a], B = G.src[v.b];
    const pa = [G.pos[A * 3], G.pos[A * 3 + 1] + 0.2, G.pos[A * 3 + 2]], pb = [G.pos[B * 3], G.pos[B * 3 + 1] + 0.2, G.pos[B * 3 + 2]];
    const u = clamp((t - v.t0) / (v.t1 - v.t0)), fade = 1 - clamp((t - v.t1) / 0.9);
    const head = [lerp(pa[0], pb[0], u), lerp(pa[1], pb[1], u), lerp(pa[2], pb[2], u)];
    ln(pa, head, [1.0, 0.93, 0.85], 5.5 * fade, 2.6); pt(head, [1, 1, 1], 14 * fade * (u < 1 ? 1 : 0), 16); pt(pa, [1, 0.85, 0.7], 6 * fade, 22);
  }
  // the sweep: one beam from the far side, turning from target to target
  if (G.sweep.length && t > G.sweep[0].t - 0.6 && t < G.sweep[G.sweep.length - 1].t + 0.5) {
    const S = G.src[G.sweeper], ps = [G.pos[S * 3], G.pos[S * 3 + 1] + 0.2, G.pos[S * 3 + 2]];
    let i = 0; while (i < G.sweep.length - 1 && G.sweep[i + 1].t < t) i++;
    const A = G.sweep[i], B = G.sweep[Math.min(i + 1, G.sweep.length - 1)];
    const u = B.t > A.t ? clamp((t - A.t) / (B.t - A.t)) : 0;
    const pa = G.src[A.b], pb = G.src[B.b];
    const tgt = [lerp(G.pos[pa * 3], G.pos[pb * 3], u), 0.2, lerp(G.pos[pa * 3 + 2], G.pos[pb * 3 + 2], u)];
    const dir = norm(sub(tgt, ps)), end = add(ps, scl(dir, 70));
    const k = ss(G.sweep[0].t - 0.6, G.sweep[0].t - 0.2, t) * (1 - ss(G.sweep[G.sweep.length - 1].t, G.sweep[G.sweep.length - 1].t + 0.5, t));
    ln(ps, end, [1.0, 0.95, 0.9], 4.5 * k, 2.2); pt(ps, [1, 0.9, 0.8], 8 * k, 24);
  }
  flushLns({ depth: false }); flushPts({ depth: false });
}


/* ---------- 4. the sky I: satellites over a campus ---------- */
let SKY1 = null;
const SKY1_FS = `#version 300 es
precision highp float; in vec2 vUV; out vec4 o; uniform vec2 uRes; uniform float uTime, uFade, uLaunch;
float h21(vec2 p){ p = fract(p * vec2(123.34, 456.21)); p += dot(p, p + 45.32); return fract(p.x * p.y); }
void main(){
  float asp = uRes.x / uRes.y; vec2 p = vec2((vUV.x - 0.5) * asp, vUV.y); float hz = 0.27; vec3 col = vec3(0.0);
  if (p.y > hz) {
    float e = (p.y - hz) / (1.0 - hz);
    col = mix(vec3(0.075, 0.05, 0.032), vec3(0.004, 0.006, 0.013), pow(e, 0.45));
    vec2 cell = floor(p * 90.0); float hs = h21(cell); vec2 sp = (cell + vec2(h21(cell + 1.3), h21(cell + 2.9))) / 90.0;
    col += vec3(0.85, 0.9, 1.0) * step(0.992, hs) * smoothstep(0.003, 0.0, length(p - sp)) * smoothstep(0.1, 0.5, e) * 1.5;
    // satellite trains
    for (int k = 0; k < 7; k++) {
      float fk = float(k); vec2 a = vec2(-1.3 + h21(vec2(fk, 1.0)) * 0.6, 0.45 + h21(vec2(fk, 2.0)) * 0.5); vec2 d = normalize(vec2(1.0, (h21(vec2(fk, 3.0)) - 0.5) * 0.5));
      float speed = 0.05 + 0.03 * h21(vec2(fk, 4.0)); vec2 head = a + d * mod(uTime * speed + fk * 0.37, 2.8);
      vec2 rel = p - head; float along = dot(rel, -d), across = dot(rel, vec2(-d.y, d.x));
      float sp2 = 0.012; float idx = clamp(floor(along / sp2 + 0.5), 0.0, 28.0); float dd = length(vec2(along - idx * sp2, across));
      col += vec3(0.95, 0.97, 1.0) * smoothstep(0.0028, 0.0, dd) * step(-0.01, along) * 1.4;
    }
    // a launch climbing from the horizon
    float lu = uLaunch; vec2 lh = vec2(0.62 - lu * 0.08, hz + 0.02 + pow(lu, 1.4) * 0.62);
    if (lu > 0.0) { col += vec3(1.0, 0.92, 0.75) * 18.0 * smoothstep(0.006, 0.0, length(p - lh));
      float trail = smoothstep(0.012, 0.0, abs(p.x - (0.62 - (p.y - hz) / 0.62 * 0.08 * 1.0)))  * step(p.y, lh.y) * step(hz, p.y) * pow(clamp((p.y - hz) / max(lh.y - hz, 1e-3), 0.0, 1.0), 2.0);
      col += vec3(1.0, 0.75, 0.45) * trail * 0.9; col += vec3(0.6, 0.35, 0.15) * 0.25 * exp(-length(p - vec2(0.62, hz)) * 9.0) * smoothstep(0.0, 0.2, lu); }
  } else {
    col = vec3(0.004, 0.004, 0.005);
  }
  // the campus: long halls, rooftop plant, pylons
  float x = p.x; float bh = 0.0;
  for (int k = 0; k < 9; k++) { float fk = float(k); float x0 = -0.95 + fk * 0.24 + h21(vec2(fk, 7.0)) * 0.05; float w = 0.16 + 0.05 * h21(vec2(fk, 8.0)); float hh = 0.035 + 0.03 * h21(vec2(fk, 9.0));
    if (x > x0 && x < x0 + w) { bh = max(bh, hh + step(0.7, fract((x - x0) * 60.0)) * 0.006 * step(0.4, h21(vec2(floor((x - x0) * 60.0), fk)))); } }
  if (p.y > hz && p.y < hz + bh) col = vec3(0.006, 0.006, 0.008);
  float roof = smoothstep(0.0015, 0.0, abs(p.y - (hz + bh))) * step(0.001, bh);
  vec2 lc = floor(vec2(x * 40.0, 0.0)); float blink = step(0.5, fract(uTime * 0.7 + h21(lc) * 3.0));
  float red = step(0.7, h21(lc + 3.0)) * smoothstep(0.003, 0.0, length(vec2(fract(x * 40.0) - 0.5, (p.y - hz - bh - 0.003) * 40.0)) / 40.0) * blink;
  col += vec3(1.0, 0.08, 0.04) * red * 6.0 + vec3(0.6, 0.4, 0.2) * roof * 0.15;
  float fence = smoothstep(0.002, 0.0, abs(p.y - hz - 0.004)) * step(0.85, h21(floor(vec2(x * 160.0, 1.0))));
  col += vec3(1.0, 0.65, 0.3) * fence * 2.0;
  o = vec4(col * uFade, 0.0);
}`;
function sSky1(t) { E.camera([0, 0, 0], [0, 0, -1], [0, 1, 0], 40); if (!SKY1) SKY1 = E.program(SKY1_FS); E.fullscreen(SKY1, { uTime: t, uFade: ss(34, 34.3, t) * (1 - ss(38.7, 39, t)), uLaunch: ss(35, 39, t) }); }

/* ---------- 5 & 9. orbit: compute shells and launch tracks ---------- */
const ORBITERS = (() => { const r = rngOf(67), n = 70000, planes = []; for (let k = 0; k < 120; k++) { const a = r() * TAU, inc = Math.acos(1 - 2 * r()) * 0.9; const nn = norm([Math.sin(inc) * Math.cos(a), Math.cos(inc), Math.sin(inc) * Math.sin(a)]); const ax = norm(cross(nn, [0.2, 0.3, 1])); planes.push({ ax, ay: cross(nn, ax), r: 1.05 + Math.pow(r(), 2) * 0.22 }); }
  const s = []; for (let i = 0; i < n; i++) s.push({ k: i % 120, ph: r() * TAU, yr: 2034 + Math.pow(i / n, 0.55) * 85, g: r() }); return { s, planes }; })();
function drawOrbiters(t, sun, k = 1) {
  const y = yearAt(t);
  for (const o of ORBITERS.s) { if (o.yr > y) continue; const pl = ORBITERS.planes[o.k], ph = o.ph + t * 0.6 / Math.pow(pl.r, 1.5);
    const p = add(scl(pl.ax, Math.cos(ph) * pl.r), scl(pl.ay, Math.sin(ph) * pl.r)); const lit = dot(norm(p), sun) > -0.15 ? 1 : 0.12;
    pt(p, [1.0, 0.9, 0.75], (0.55 + Math.pow(o.g, 12) * 6) * lit * k, 1.8); }
  flushPts({ depth: true });
}
function launchTracks(t, n, sun, k = 1) {
  const r = rngOf(71); for (let i = 0; i < n; i++) { const base = norm([r() * 2 - 1, r() * 1.4 - 0.6, r() * 2 - 1]); const ph = (t * 0.35 + r()) % 1; const side = norm(cross(base, [0, 1, 0]));
    let prev = scl(base, 1.001); for (let sgm = 1; sgm <= 18; sgm++) { const u = sgm / 18 * ph; const dir = norm(add(scl(base, Math.cos(u * 1.2)), scl(side, Math.sin(u * 1.2)))); const p = scl(dir, 1.0 + 0.12 * Math.sin(Math.min(u, 1) * Math.PI / 2)); ln(prev, p, AMBER, 2.0 * k * (1 - ph * 0.6), 1.3); prev = p; } }
  flushLns({ depth: true });
}
function sOrbit(t) {
  const dir = ll(lerp(-40, -10, ss(39, 48, t)), 18), sun = sunFrom(dir, 95, 12);
  earthBase(t, dir, lerp(2.5, 2.9, ss(39, 48, t)), { sun, fov: 36 });
  drawNet(t, { intensity: 0.7, showSeeds: 0 }); drawOrbiters(t, sun); launchTracks(t, 14, sun);
}
function sNotEnough(t) {
  const dir = ll(-15, 12), sun = sunFrom(dir, 70, 8);
  earthBase(t, dir, lerp(4.2, 5.0, ss(82, 90, t)), { sun, fov: 34, ocean: 0.05 });
  drawNet(t, { intensity: 0.9, showSeeds: 0 }); drawOrbiters(t, sun, 1.2);
  // two tracks reach inward, toward the Sun
  const sunScreenDir = sun; const k = ss(84.5, 86.5, t);
  for (const [off, lift] of [[0.15, 0.25], [-0.2, -0.15]]) { let prev = scl(norm(add(sunScreenDir, [0, lift, off])), 1.05); for (let sgm = 1; sgm <= 40; sgm++) { const u = sgm / 40 * k; const p = add(scl(norm(add(sunScreenDir, [0, lift, off])), 1.05 + u * 6), [0, Math.sin(u * 2) * lift * 0.6, 0]); ln(prev, p, AMBER, 2.4, 1.6); prev = p; } }
  flushLns({ depth: true });
}

/* ---------- 8 & 18. the dome by day; the dome when the stars go out ---------- */
function sSky2(t) { E.camera([0, 0, 0], [0, 0, -1], [0, 1, 0], 40); if (!SKY) SKY = E.program(SKY_FS); E.fullscreen(SKY, { uTime: t, uFade: ss(72, 72.3, t) * (1 - ss(81.7, 82, t)), uSunDim: 0, uMoon: 0, uMode: 1, uStars: 0, uDomeLight: 1 }); }
function sSky4(t) { E.camera([0, 0, 0], [0, 0, -1], [0, 1, 0], 40); if (!SKY) SKY = E.program(SKY_FS); E.fullscreen(SKY, { uTime: t, uFade: ss(195, 195.4, t) * (1 - ss(201.6, 202, t)), uSunDim: 0, uMoon: 0, uMode: 2, uStars: 1 - ss(196.2, 201, t), uDomeLight: 0 }); }

/* ---------- 11. Venus ---------- */
function sVenus(t) {
  const camDir = norm([-0.1, 0.2, 1]), sun = norm([0.75, 0.3, 0.6]);
  E.camera(scl(camDir, 3.6), [0.1, 0, 0], [0, 1, 0], 34); starfield([0, 0, 0], 0.9);
  const R = 1 - 0.3 * ss(108, 110, t), op = 1 - ss(109, 110, t);
  E.sphere({ mode: 3, radius: R, sun, dayGain: 0.95, lesC: norm([-0.25, 0.25, 0.94]), lesR: 2.5 * ss(104.3, 109, t), lesK: 1.4, atmo: [1.0, 0.9, 0.7], atmoK: 0.6, opacity: op, time: t });
  const ringK = ss(106, 110, t); if (ringK > 0) { const r = rngOf(47); for (let i = 0; i < 9000; i++) { const a = r() * TAU, rr = 1.6 + r() * 1.5; if (r() > ringK) continue; const ang = a + t * 0.05 / rr; pt([Math.cos(ang) * rr, gauss(r) * 0.03 + Math.sin(ang) * rr * 0.1, Math.sin(ang) * rr], [1, 0.62, 0.3], 0.5 * ringK, 1.6); } flushPts({ depth: true }); }
}

/* ---------- 13. the relay ---------- */
function sRelay(t) {
  E.camera([3.2, 1.0, 7.2], [-2.0, -0.2, -2.6], [0, 1, 0], 40); starfield([0, 0, 0], 0.8);
  const sun = norm([-1, 0.15, 0.25]);
  E.sphere({ mode: 0, day: tex.earthDay, night: tex.earthNight, center: [-8, -1.6, -12], radius: 3.67, sun, nightGain: 0.9, dayGain: 0.9, ocean: 0.05, atmo: [0.35, 0.6, 1.0], atmoK: 0.9, time: t, rot: bodyRot(1.2, 0.2) });
  const hit = ss(124.6, 125.4, t), blaze = ss(125, 127, t);
  E.sphere({ mode: 1, day: tex.moon, radius: 1, sun, dayGain: 1.2 + blaze * 9, tint: [1, 0.98, 0.95], time: t });
  const src = [-60, 6, -14], target = scl(norm(sub(src, [0, 0, 0])), 1.0);
  const head = [lerp(src[0], target[0], hit), lerp(src[1], target[1], hit), lerp(src[2], target[2], hit)];
  ln(src, head, [1.0, 0.95, 0.85], 5 * (0.8 + 0.2 * Math.sin(t * 40)), 2.4); flushLns({ depth: true });
  if (hit >= 1) { pt(target, [1, 0.97, 0.9], 30 * blaze, 60); flushPts({ depth: false }); }
}

/* ---------- 15. launch: the probes leave; the solar system becomes a point ---------- */
const PROBES = (() => { const r = rngOf(73), p = []; for (let i = 0; i < 4000; i++) { const z = r() * 2 - 1, a = r() * TAU, q = Math.sqrt(1 - z * z); p.push({ d: [q * Math.cos(a), z * 0.6, q * Math.sin(a)], tl: 137.3 + r() * 3.5, v: 0.6 + r() * 0.8 }); } return p; })();
function sLaunch(t) {
  if (t >= 143.4) { sGalaxyVisible(t, { fromSun: true }); return; }
  const dist = 14 * Math.pow(140, ss(138.5, 143.4, t));
  E.camera(scl(norm([0.35, 0.32, 1]), dist), [0, 0, 0], [0, 1, 0], 32); starfield([0, 0, 0], 0.9);
  E.sphere({ mode: 2, radius: 1, emissive: 0.6, ir: 0.6, atmo: [0.7, 0.1, 0.04], time: t });
  for (const pr of PROBES) { if (t < pr.tl) continue; const u = t - pr.tl, r0 = 3.5 + pr.v * 4 * u * u * (1 + u * u * 2); const a = scl(pr.d, r0), b = scl(pr.d, r0 * 0.93); ln(b, a, AMBER, 2.2, 1.1); }
  flushLns({ depth: false });
}

/* ---------- 15b, 17, 19, 20. the galaxy in visible light, the front, the efficient dark, the edge ---------- */
function sGalaxyVisible(t, { fromSun = false } = {}) {
  const G = GAL; const full = galCamFull(t);
  let pos, look;
  if (fromSun) { const e = ease(ss(143.4, 145, t)); const near = add(G.sun, [4, 5, 9]); pos = [lerp(near[0], full.pos[0] * 0.6, e), lerp(near[1], full.pos[1] * 0.6, e), lerp(near[2], full.pos[2] * 0.6, e)]; look = [lerp(G.sun[0], 0, e), lerp(G.sun[1], 0, e), lerp(G.sun[2], 0, e)]; }
  else { const e = ease(ss(168, 182, t)); const near = add(G.sun, [6, 9, 14]); pos = [lerp(near[0], full.pos[0], e), lerp(near[1], full.pos[1], e), lerp(near[2], full.pos[2], e)]; look = [lerp(G.sun[0], full.look[0], e), lerp(G.sun[1], full.look[1], e), lerp(G.sun[2], full.look[2], e)]; }
  E.camera(pos, look, [0, 1, 0], 42); starfield([0, 0, 0], 0.4);
  const ir = fromSun ? 0 : ss(190, 194, t), red = [0.85, 0.12, 0.05];
  for (let i = 0; i < G.n; i++) {
    const p = [G.pos[i * 3], G.pos[i * 3 + 1], G.pos[i * 3 + 2]], tc = fromSun ? 1e9 : G.conv[i];
    let c = [G.col[i * 3], G.col[i * 3 + 1], G.col[i * 3 + 2]], a = G.b[i] * 0.9;
    if (t >= tc) { const age = t - tc; if (age < 0.5) { c = [1, 0.6, 0.2]; a = 5 * (1 - age / 0.5) + 0.3; } else { c = [lerp(0.25, red[0], ir), lerp(0.06, red[1], ir), lerp(0.03, red[2], ir)]; a = lerp(0.12, G.b[i] * 0.8, ir); } }
    pt(p, c, a, 1.4);
  }
  flushPts({ depth: false });
  if (fromSun || t < 172) { pt(G.sun, [1, 0.62, 0.25], 6, 14); flushPts({ depth: false }); }
}
function sEfficient(t) {
  const G = GAL, gc = galCamFull(t); E.camera(gc.pos, gc.look, [0, 1, 0], 42); starfield([0, 0, 0], 0.35);
  const red = [0.85, 0.12, 0.05]; for (let i = 0; i < G.n; i++) pt([G.pos[i * 3], G.pos[i * 3 + 1], G.pos[i * 3 + 2]], red, G.b[i] * 0.8, 1.4); flushPts({ depth: false });
}
const FARGAL = [[420, 40, -160, 1.0], [-380, 90, -300, 0.6], [150, -120, 420, 0.5], [-200, 60, 380, 0.4]];
function sEdge(t) {
  const G = GAL; E.camera([78, 9, 20], [20, -2, 0], [0, 1, 0], 44); starfield([0, 0, 0], 0.5);
  const red = [0.85, 0.12, 0.05]; for (let i = 0; i < G.n; i += 1) pt([G.pos[i * 3], G.pos[i * 3 + 1], G.pos[i * 3 + 2]], red, G.b[i] * 0.8, 1.4);
  const r = rngOf(83); for (const [x, y, z, s0] of FARGAL) for (let k = 0; k < 400; k++) { const g1 = gauss(r), g2 = gauss(r); pt([x + g1 * 8 * s0, y + g2 * 2.5 * s0, z + gauss(r) * 8 * s0], [1, 0.92, 0.85], 0.35, 2); }
  flushPts({ depth: false });
  // probes leave the rim and find nothing
  const rr = rngOf(89); for (let k = 0; k < 60; k++) { const i = 34000 + Math.floor(rr() * (G.n - 34000)); const p = [G.pos[i * 3], G.pos[i * 3 + 1], G.pos[i * 3 + 2]]; if (Math.hypot(p[0], p[2]) < 30) continue;
    const d = norm([p[0], 0, p[2]]), t0 = 215.5 + rr() * 4, u = clamp((t - t0) / 3.5), fade = 1 - ss(t0 + 2.8, t0 + 4.5, t); if (u <= 0 || fade <= 0) continue;
    const head = add(p, scl(d, 2 + u * 40)); ln(p, head, AMBER, 1.8 * fade, 1.2); pt(head, AMBER, 3 * fade, 6); }
  flushLns({ depth: false }); flushPts({ depth: false });
}

/* ---------- 16. the cell ---------- */
const CELL_STAR = [-12, 5, 5.5];
function sCell(t) {
  const e = ease(ss(158.5, 164, t)); const look = [lerp(-0.6, CELL_STAR[0] * 0.8, e), lerp(0.2, CELL_STAR[1] * 0.8, e), lerp(0, CELL_STAR[2] * 0.8, e)];
  E.camera([lerp(1.8, 3.0, e), lerp(0.8, 1.8, e), lerp(4.4, 6.5, e)], look, [0, 1, 0], 40); starfield([0, 0, 0], 0.9);
  const sun = norm(CELL_STAR), dim = ss(161, 167, t);
  E.sphere({ mode: 2, center: CELL_STAR, radius: 1.4, emissive: lerp(3.0, 0.02, dim), atmo: [1.0, 0.8, 0.5], time: t, opacity: 1 - ss(166.5, 168, t) });
  const R = 1 - 0.4 * ss(155.5, 159, t), op = 1 - ss(157.5, 159.5, t);
  const rot = bodyRot(2.0, 0.25), faceW = norm([-0.33, 0.36, 0.88]);
  const lesC = [rot[0] * faceW[0] + rot[3] * faceW[1] + rot[6] * faceW[2], rot[1] * faceW[0] + rot[4] * faceW[1] + rot[7] * faceW[2], rot[2] * faceW[0] + rot[5] * faceW[1] + rot[8] * faceW[2]];
  E.sphere({ mode: 1, day: tex.mercury, radius: R, sun, desat: 0.35, tint: [1.05, 0.74, 0.55], dayGain: 1.4 * (1 - dim * 0.9), lesC, lesR: 2.6 * ss(149.8, 156.5, t), lesK: 1.3, rot, opacity: op, time: t });
  // the craft: braking, landing
  const toWorld = v => [rot[0] * v[0] + rot[1] * v[1] + rot[2] * v[2], rot[3] * v[0] + rot[4] * v[1] + rot[5] * v[2], rot[6] * v[0] + rot[7] * v[1] + rot[8] * v[2]];
  const land = scl(toWorld(lesC), 1.0);
  if (t < 150.3) { const u = ease(ss(145, 149.8, t)); const from = [2.6, 2.2, 1.0]; const p = [lerp(from[0], land[0] * 1.01, u), lerp(from[1], land[1] * 1.01, u), lerp(from[2], land[2] * 1.01, u)];
    pt(p, [1, 0.85, 0.6], 6, 7); const brake = 1 - ss(148.5, 149.8, t); void 0; pt(p, [0.6, 0.75, 1.0], 1.6 * brake, 40); if (t > 149.8) pt(land, [1, 0.7, 0.4], 20 * (1 - ss(149.8, 150.3, t)), 30); }
  // debris lifting off, then collectors around the star
  const ringK = ss(155.5, 160, t), coll = ss(159, 163, t);
  if (ringK > 0) { const r = rngOf(97); for (let i = 0; i < 12000; i++) { const a = r() * TAU, rr = 1.3 + r() * 1.2; if (r() > ringK) continue; const ang = a + t * 0.08 / rr; const local = [Math.cos(ang) * rr, gauss(r) * 0.04 + Math.sin(ang) * rr * 0.1, Math.sin(ang) * rr]; const toward = clamp((coll - r() * 0.5) * 2); const target = add(CELL_STAR, scl(norm([Math.cos(ang * 3 + i), (r() - 0.5) * 1.4, Math.sin(ang * 3 + i)]), 1.9 + r() * 0.6));
    const p = [lerp(local[0], target[0], toward), lerp(local[1], target[1], toward), lerp(local[2], target[2], toward)]; pt(p, toward > 0.98 ? [lerp(1, 0.7, dim), lerp(0.7, 0.1, dim), lerp(0.4, 0.04, dim)] : [1, 0.62, 0.3], (0.6 + toward * 0.4) * (1 - dim * 0.6), 1.8); } }
  flushPts({ depth: true });
}

/* ---------- the panel and the words ---------- */
const MONO = 'Menlo, "SF Mono", Consolas, monospace', SANS = '"Avenir Next", "Helvetica Neue", Helvetica, Arial, sans-serif';
const SUP = { "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴", "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹" };
function fmtW(p) {
  if (p <= 0) return "0 W"; if (p < 1e12) return `${(p / 1e9).toFixed(0)} GW`; if (p < 1e15) return `${(p / 1e12).toFixed(p < 1e13 ? 1 : 0)} TW`; if (p < 1e18) return `${(p / 1e15).toFixed(p < 1e16 ? 1 : 0)} PW`;
  const e = Math.floor(Math.log10(p)), m = p / Math.pow(10, e); return `${m.toFixed(1)} × 10${String(e).split("").map(c => SUP[c]).join("")} W`;
}
function fmtPop(p) { return p >= 1e9 ? `${(p / 1e9).toFixed(1)} bn` : p >= 1e6 ? `${Math.round(p / 1e6)} million` : `${Math.round(p / 1e3)} thousand`; }
function fmtYear(y) { return y < 10000 ? String(Math.round(y)) : Math.round(y).toLocaleString("en-US"); }
const CARDS = [[33, 34.6, "2046", "1 TW"], [47, 48.6, "2068", "19 TW · all the energy humanity uses today"], [57, 58.6, "2097", "waste heat 2 W/m²"], [71, 72.6, "2113", "10 PW"], [83, 85, "2132", "all the sunlight the Earth receives"], [121, 123, "2291", "3.8 × 10²⁶ W · the Sun"], [160, 162, "", "a few thousand years"]];
function panel(t) {
  const on = ss(12.5, 14, t) * (t > 270 ? (Math.floor(t * 14) % 3 === 0 && t < 271.5 ? 1 : 0) : 1);
  if (on <= 0 || t < 12) return;
  ctx.save(); ctx.globalAlpha = on; ctx.textBaseline = "top";
  const L = 72, R = W - 72, T = 60;
  const label = (s, x, y, al) => { ctx.font = `500 13px ${MONO}`; ctx.letterSpacing = "3px"; ctx.fillStyle = "rgba(225,232,238,0.5)"; ctx.textAlign = al; ctx.fillText(s, x, y); };
  const value = (s, x, y, al, c = "rgba(240,244,247,0.95)") => { ctx.font = `400 26px ${MONO}`; ctx.letterSpacing = "1px"; ctx.fillStyle = c; ctx.textAlign = al; ctx.fillText(s, x, y); };
  label("YEAR", L, T, "left"); value(fmtYear(yearAt(t)), L, T + 22, "left");
  if (t < 34) { const a = ss(13, 14, t) * (t < 20 ? 1 : 1 - ss(20, 22, t)); ctx.globalAlpha = on * a; ctx.font = `600 12px ${MONO}`; ctx.letterSpacing = "3px"; ctx.fillStyle = "#ffb15a"; ctx.textAlign = "left"; ctx.fillText("▸ TODAY", L + 92, T + 32); ctx.globalAlpha = on; }
  label("POWER", R, T, "right"); value(fmtW(powerAt(t)), R, T + 22, "right");
  const popA = 1 - ss(133, 136, t);
  if (popA > 0) { ctx.globalAlpha = on * popA; label("POPULATION", R, T + 72, "right"); value(fmtPop(popAt(t)), R, T + 94, "right"); ctx.globalAlpha = on; }
  if (t > 223) { ctx.globalAlpha = on * ss(223, 224, t); label("PLAYERS", R, T + 72, "right"); value(String(playersAt(t)), R, T + 94, "right", "#ffb15a"); }
  ctx.restore();
}
function words(t) {
  ctx.save(); ctx.textAlign = "center"; ctx.textBaseline = "middle";
  for (const [a, b, yr, q] of CARDS) {
    const k = ss(a, a + 0.25, t) * (1 - ss(b - 0.3, b, t)); if (k <= 0) continue;
    ctx.globalAlpha = k; ctx.fillStyle = "rgba(245,247,249,0.96)";
    if (yr) { ctx.font = `200 78px ${SANS}`; ctx.letterSpacing = "10px"; ctx.fillText(yr, W / 2 + 5, H * 0.76); }
    ctx.font = `500 17px ${MONO}`; ctx.letterSpacing = "3px"; ctx.fillStyle = "rgba(255,190,120,0.95)"; ctx.fillText(q.toUpperCase(), W / 2 + 2, yr ? H * 0.76 + 62 : H * 0.8);
  }
  { const k = ss(75, 76.5, t) * (1 - ss(81, 82, t)); if (k > 0) { ctx.globalAlpha = k; ctx.font = `500 22px ${MONO}`; ctx.letterSpacing = "12px"; ctx.fillStyle = "rgba(40,42,46,0.85)"; ctx.fillText("PROGRESS", W / 2 + 6, H - 150); } }
  // 1. the word, and its underline becoming the edge of the Earth
  if (t < 12) {
    const cap = ss(1.0, 1.8, t) * (1 - ss(6.5, 7.5, t));
    if (cap > 0) { ctx.globalAlpha = cap; ctx.font = `500 14px ${MONO}`; ctx.letterSpacing = "3px"; ctx.fillStyle = "rgba(225,232,238,0.55)"; ctx.fillText("UNITED NATIONS GENERAL ASSEMBLY  ·  22 SEPTEMBER 2026", W / 2, H - 120); }
    const wa = ss(2.2, 3.0, t) * (1 - ss(7.0, 8.2, t));
    if (wa > 0) { ctx.globalAlpha = wa; ctx.font = `300 64px ${SANS}`; ctx.letterSpacing = "2px"; ctx.fillStyle = "rgba(246,248,250,0.97)"; ctx.fillText("super intelligence", W / 2, H / 2); }
    // the line: under the words, then right, then up along the limb the next shot will show
    const u1 = ss(3.6, 6.4, t), u2 = ss(7.0, 10.0, t), lineA = 1 - ss(11.0, 12.0, t);
    if (u1 > 0 && lineA > 0) {
      ctx.globalAlpha = lineA; ctx.strokeStyle = "rgba(255,170,90,1)"; ctx.lineWidth = 2.4; ctx.shadowColor = "rgba(255,150,60,0.9)"; ctx.shadowBlur = 14; ctx.lineCap = "round";
      const y0 = H / 2 + 52, x0 = W / 2 - 300, xA = W / 2 + 300, cx = 960, cy = 540, R0 = 900;
      ctx.beginPath(); ctx.moveTo(x0, y0); ctx.lineTo(lerp(x0, xA, u1), y0);
      if (u2 > 0) { const xB = cx + Math.sqrt(R0 * R0 - (y0 - cy) ** 2); const seg = Math.min(1, u2 * 2); ctx.lineTo(lerp(xA, xB, seg), y0);
        if (u2 > 0.5) { const a0 = Math.atan2(y0 - cy, xB - cx), a1 = -Math.acos((cx - 1680 + 1680 - cx) / R0 || 0) ; const aEnd = Math.atan2(0 - cy, 1680 - cx); ctx.arc(cx, cy, R0, a0, lerp(a0, aEnd, (u2 - 0.5) * 2), true); } }
      ctx.stroke(); ctx.shadowBlur = 0;
    }
  }
  // 19. the reprise over the efficient galaxy
  { const k = ss(205, 206.5, t) * (1 - ss(211, 213, t)); if (k > 0) { ctx.globalAlpha = k * 0.5; ctx.font = `300 54px ${SANS}`; ctx.letterSpacing = "2px"; ctx.fillStyle = "rgba(246,248,250,0.9)"; ctx.fillText("super intelligence", W / 2, H * 0.82); } }
  // 25. the title
  { const k = ss(281, 283, t) * (1 - ss(296, 299, t)); if (k > 0) { ctx.globalAlpha = k; ctx.font = `200 70px ${SANS}`; ctx.letterSpacing = "22px"; ctx.fillStyle = "rgba(246,248,250,0.97)"; ctx.fillText("THE GAME OF WINNING", W / 2 + 11, H / 2); } }
  ctx.restore();
}

/* ---------- the frame ---------- */
function drawScene(t) {
  E.begin();
  let fade = 1;
  if (t >= 10.5 && t < 12) { sToday(12); fade = ss(10.5, 12, t); }
  else if (t >= 12 && t < 34) sToday(t);
  else if (t >= 34 && t < 39) sSky1(t);
  else if (t >= 39 && t < 48) sOrbit(t);
  else if (t >= 48 && t < 58) sHeat(t);
  else if (t >= 58 && t < 72) sOceans(t);
  else if (t >= 72 && t < 82) sSky2(t);
  else if (t >= 82 && t < 90) sNotEnough(t);
  else if (t >= 90 && t < 104) sMercury(t);
  else if (t >= 104 && t < 110) sVenus(t);
  else if (t >= 110 && t < 124) sSwarm(t);
  else if (t >= 124 && t < 130) sRelay(t);
  else if (t >= 130 && t < 137) sSkyTwoSuns(t);
  else if (t >= 137 && t < 145) sLaunch(t);
  else if (t >= 145 && t < 168) sCell(t);
  else if (t >= 168 && t < 195) sGalaxyVisible(t);
  else if (t >= 195 && t < 202) sSky4(t);
  else if (t >= 202 && t < 215) sEfficient(t);
  else if (t >= 215 && t < 223) sEdge(t);
  else if (t >= 223 && t < 272) sGalaxyWar(t);
  const bright = (t >= 130 && t < 137) || (t >= 72 && t < 82);
  E.end({ bloom: bright ? 0.32 : 0.85, thresh: bright ? 1.5 : 0.9, exposure: 1.0, grain: 0.03, vignette: 0.4, seed: (t * 30) % 97, fade });
}
function frame(t) {
  if (!ready) throw new Error("not ready");
  drawScene(t);
  ctx.globalAlpha = 1; ctx.drawImage(E.gl.canvas, 0, 0, W, H);
  panel(t); words(t);
  return ctx.canvas;
}
async function init(view) {
  ctx = view.getContext("2d");
  const glc = document.createElement("canvas"); glc.width = W; glc.height = H;
  E = Engine.create(glc, W, H);
  const names = { earthDay: "assets/earth-day.jpg", earthNight: "assets/earth-night.jpg", mercury: "assets/mercury.jpg", moon: "assets/moon.jpg" };
  for (const [k, u] of Object.entries(names)) tex[k] = await E.loadTexture(u);
  buildNet(tex.earthNight.img, tex.earthDay.img);
  buildGalaxy();
  ready = true;
}
return { init, frame, W, H, yearAt, powerAt, galaxy: () => GAL, _debug: () => ({ volleys: GAL.volleys.length, active: (t) => GAL.volleys.filter(v => t >= v.t0 && t <= v.t1 + 0.9).length, alive: (t) => GAL.death.filter(d => d > t).length, first: GAL.volleys.slice(0, 3) }) };
})();
