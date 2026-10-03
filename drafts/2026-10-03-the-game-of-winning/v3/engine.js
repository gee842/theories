// A small deterministic WebGL2 renderer for The Game of Winning, v3 (real time).
// HDR scene buffer with depth, planets ray-traced per pixel, additive points and lines, bloom, ACES tone map, grain.
"use strict";
const Engine = (() => {

const NOISE = `
float hash13(vec3 p){ p = fract(p * 0.1031); p += dot(p, p.zyx + 31.32); return fract((p.x + p.y) * p.z); }
float vnoise(vec3 p){ vec3 i = floor(p), f = fract(p); f = f*f*(3.0-2.0*f);
  return mix(mix(mix(hash13(i), hash13(i+vec3(1,0,0)), f.x), mix(hash13(i+vec3(0,1,0)), hash13(i+vec3(1,1,0)), f.x), f.y),
             mix(mix(hash13(i+vec3(0,0,1)), hash13(i+vec3(1,0,1)), f.x), mix(hash13(i+vec3(0,1,1)), hash13(i+vec3(1,1,1)), f.x), f.y), f.z); }
float fbm(vec3 p){ float a = 0.5, s = 0.0; for (int i = 0; i < 5; i++) { s += a * vnoise(p); p = p * 2.03 + 17.1; a *= 0.5; } return s; }
float ridged(vec3 p){ float a = 0.5, s = 0.0; for (int i = 0; i < 5; i++) { float n = 1.0 - abs(vnoise(p) * 2.0 - 1.0); s += a * n * n; p = p * 2.1 + 9.7; a *= 0.5; } return s; }
`;

const FULL_VS = `#version 300 es
out vec2 vUV; void main(){ vec2 p = vec2((gl_VertexID << 1) & 2, gl_VertexID & 2); vUV = p; gl_Position = vec4(p * 2.0 - 1.0, 0.0, 1.0); }`;

// --- planets -------------------------------------------------------------
const SPHERE_FS = `#version 300 es
precision highp float;
in vec2 vUV; out vec4 o;
uniform vec3 uCamPos, uCamR, uCamU, uCamF; uniform float uTanHalf, uAspect; uniform mat4 uVP;
uniform vec3 uCenter; uniform float uRadius; uniform mat3 uRot; uniform vec3 uSun;
uniform sampler2D uDay, uNight; uniform int uMode; uniform float uDayGain, uNightGain, uOpacity;
uniform float uThermal, uHeat, uOcean, uIr, uEmissive, uTime, uDesat;
uniform vec3 uAtmo; uniform float uAtmoK;
uniform vec3 uLesC; uniform float uLesR, uLesK;
uniform vec3 uTint; uniform sampler2D uGrow; uniform float uYear, uClouds, uHasGrow, uSeaStart, uSeaEnd;
${NOISE}
vec3 toLin(vec3 c){ return pow(c, vec3(2.2)); }
vec3 ironbow(float x){ x = clamp(x, 0.0, 1.0);
  vec3 c = mix(vec3(0.002,0.001,0.014), vec3(0.258,0.039,0.406), smoothstep(0.0,0.2,x));
  c = mix(c, vec3(0.578,0.148,0.404), smoothstep(0.2,0.4,x)); c = mix(c, vec3(0.865,0.317,0.226), smoothstep(0.4,0.6,x));
  c = mix(c, vec3(0.988,0.645,0.04), smoothstep(0.6,0.8,x)); c = mix(c, vec3(0.988,0.998,0.645), smoothstep(0.8,1.0,x)); return pow(c, vec3(2.2)); }
void main(){
  vec2 ndc = vUV * 2.0 - 1.0;
  vec3 rd = normalize(uCamF + ndc.x * uTanHalf * uAspect * uCamR + ndc.y * uTanHalf * uCamU);
  vec3 oc = uCamPos - uCenter; float b = dot(oc, rd); float c = dot(oc, oc) - uRadius * uRadius; float h = b * b - c;
  float dmin = sqrt(max(dot(oc, oc) - b * b, 0.0));
  if (h < 0.0 || -b - sqrt(max(h,0.0)) < 0.0) {
    // halo outside the limb (atmosphere, or the Sun's corona)
    if (b > 0.0) discard;
    gl_FragDepth = 1.0;
    float x = (dmin - uRadius) / uRadius;
    vec3 hc = vec3(0.0);
    if (uMode == 2) hc = uAtmo * uEmissive * (0.5 * exp(-x * 9.0) + 0.12 * exp(-x * 1.6));
    else if (uAtmoK > 0.0) { vec3 cp = uCamPos + rd * (-b) - uCenter; float lit = clamp(dot(normalize(cp), uSun) * 1.4 + 0.4, 0.0, 1.0); hc = uAtmo * uAtmoK * exp(-x * 55.0) * lit; }
    o = vec4(hc * uOpacity, 0.0); return;
  }
  float t = -b - sqrt(h); vec3 P = uCamPos + rd * t; vec3 N = normalize(P - uCenter);
  vec4 clip = uVP * vec4(P, 1.0); gl_FragDepth = clamp(clip.z / clip.w * 0.5 + 0.5, 0.0, 1.0);
  vec3 q = uRot * N; float lon = atan(q.x, q.z); float lat = asin(clamp(q.y, -1.0, 1.0));
  vec2 uv = vec2(lon / 6.2831853 + 0.5, 0.5 - lat / 3.1415927);
  float ndl = dot(N, uSun); float view = clamp(dot(N, -rd), 0.0, 1.0);
  vec3 col = vec3(0.0);
  if (uMode == 0) {                                   // Earth
    vec3 day = toLin(texture(uDay, uv).rgb); vec3 night = toLin(texture(uNight, uv).rgb);
    vec4 gr = uHasGrow > 0.5 ? texture(uGrow, uv) : vec4(1.0, 0.0, 0.0, 1.0);
    float depth = gr.g, isSea = step(0.004, depth);
    float dryYear = uSeaStart + pow(depth, 0.7) * (uSeaEnd - uSeaStart);
    float sea = isSea * (1.0 - smoothstep(dryYear - 1.5, dryYear + 1.5, uYear));
    float gYear = 2026.0 + gr.r * 128.0 + (fbm(q * 55.0) - 0.5) * 16.0 + (vnoise(q * 240.0) - 0.5) * 5.0;
    if (isSea > 0.5) gYear = dryYear + 6.0 + 20.0 * hash13(floor(q * 300.0));
    float grown = smoothstep(gYear, gYear + 4.0, uYear) * (1.0 - sea);
    // dried sea floor: salt and silt
    vec3 salt = mix(vec3(0.42, 0.39, 0.34), vec3(0.62, 0.59, 0.53), fbm(q * 40.0)) * (0.8 + 0.4 * depth);
    day = mix(day, salt, isSea * (1.0 - sea));
    // solar glass over grown land: dark, gridded, glinting
    float grid = max(pow(abs(sin(lon * 900.0)), 30.0), pow(abs(sin(lat * 900.0)), 30.0));
    vec3 glass = vec3(0.018, 0.024, 0.04) * (1.0 + 0.6 * grid);
    float ice = smoothstep(0.55, 0.8, min(day.r, min(day.g, day.b)) / max(max(day.r, day.g), 1e-3) * dot(day, vec3(0.33)) * 2.0);
    float glassK = grown * (1.0 - ice * 0.6) * (0.55 + 0.45 * fbm(q * 90.0));
    day = mix(day, glass, glassK);
    float dl = smoothstep(-0.08, 0.3, ndl);
    vec3 dcol = day * dl * uDayGain;
    vec3 hv = normalize(uSun - rd); float spec = pow(max(dot(N, hv), 0.0), 70.0);
    dcol += vec3(1.0, 0.95, 0.85) * pow(max(dot(N, hv), 0.0), 600.0) * sea * 0.9 * dl * uDayGain + vec3(0.9, 0.92, 1.0) * spec * sea * 0.04 * dl * uDayGain;
    dcol += vec3(1.0, 0.93, 0.8) * pow(max(dot(N, hv), 0.0), 260.0) * glassK * 3.0 * dl * uDayGain;
    // night: city lights, then industrial amber in settlement-scale grain
    float nl = smoothstep(0.12, -0.15, ndl);
    float nlum = dot(night, vec3(0.3, 0.59, 0.11)); vec3 nb = mix(vec3(nlum), night, 0.55); nb = max(nb - 0.0015, 0.0) * smoothstep(0.0, 0.02, nlum);
    float grain = smoothstep(0.55, 0.9, vnoise(q * 700.0)) * 0.8 + smoothstep(0.62, 0.95, vnoise(q * 2600.0)) * 0.7;
    vec3 amber = vec3(1.0, 0.5, 0.15);
    vec3 ncol = nb * vec3(1.0, 0.84, 0.6) * 1.3 * (1.0 - grown * 0.5) + amber * grown * (0.006 + 0.13 * grain + nlum * 1.3);
    float cl = 0.0;
    if (uClouds > 0.0) { vec3 cq = q * 9.0 + vec3(uTime * 0.006, 0.0, 0.0); float w = fbm(cq * 0.5); cl = smoothstep(0.6, 0.74, fbm(cq + w * 2.0) * (0.7 + 0.45 * pow(abs(sin(lat * 3.0)), 0.6))) * uClouds; }
    dcol = mix(dcol, vec3(0.88, 0.9, 0.93) * dl * uDayGain, cl * 0.75);
    ncol *= 1.0 - cl * 0.55;
    col = dcol + ncol * nl * uNightGain;
    if (uThermal > 0.0) {
      float cl2 = cos(lat);
      float heat = 0.015 + 0.07 * cl2 * cl2 + (1.0 - sea) * 0.07 + uHeat * 0.05 + grown * (0.3 + 0.4 * uHeat) * (0.55 + 0.45 * grain) + nlum * 0.9 * uHeat;
      col = mix(col, ironbow(heat) * 1.1, uThermal);
    }
    col += uAtmo * uAtmoK * pow(1.0 - view, 3.0) * clamp(ndl * 1.5 + 0.35, 0.0, 1.0) * 0.6;
  } else if (uMode == 1) {                            // rocky worlds: Mercury, the Moon, an alien planet
    vec3 alb = toLin(texture(uDay, uv).rgb); float lum = dot(alb, vec3(0.3, 0.59, 0.11)); alb = mix(alb, vec3(lum), uDesat) * uTint;
    col = alb * smoothstep(-0.03, 0.2, ndl) * uDayGain + alb * 0.012;
    if (uLesR > 0.0) {
      float a = acos(clamp(dot(q, uLesC), -1.0, 1.0));
      float n = fbm(q * 7.0) - 0.5; float e = a - uLesR - n * 0.35 * uLesR;
      float inside = 1.0 - smoothstep(-0.004, 0.004, e);
      vec3 cell = floor(q * 140.0); float lit = step(0.982, hash13(cell)) * (0.6 + 0.4 * hash13(cell + 7.0));
      float chan = pow(ridged(q * 22.0 + 3.0), 9.0);
      vec3 scar = vec3(0.018, 0.016, 0.015) * (0.6 + 0.8 * fbm(q * 30.0)) + vec3(1.0, 0.55, 0.18) * (lit * 1.4 + chan * 0.5) * uLesK;
      col = mix(col, scar * (0.7 + 0.6 * smoothstep(-0.05, 0.25, ndl)), inside);
      float edge = exp(-abs(e) / 0.005) * uLesK;
      float veins = pow(ridged(q * 18.0), 8.0) * smoothstep(0.22 * uLesR + 0.06, 0.0, e) * step(0.0, e) * uLesK;
      col += vec3(1.0, 0.52, 0.14) * (edge * 2.2 + veins * 1.8);
    }
    col += uAtmo * uAtmoK * pow(1.0 - view, 4.0);
  } else if (uMode == 2) {                            // the Sun
    float g = fbm(q * 40.0 + uTime * 0.05) * 0.6 + fbm(q * 9.0 - uTime * 0.02) * 0.4;
    float limb = pow(view, 0.45);
    vec3 vis = vec3(1.0, 0.86, 0.62) * (0.75 + 0.5 * g) * limb;
    vec3 ir = vec3(0.6, 0.06, 0.02) * (0.7 + 0.6 * g) * limb;
    col = mix(vis, ir, uIr) * uEmissive;
  } else if (uMode == 3) {                            // Venus under its clouds
    float bands = fbm(vec3(q.x * 3.0, q.y * 14.0, q.z * 3.0) + uTime * 0.01) * 0.65 + fbm(q * 18.0 + vec3(0.0, uTime * 0.02, 0.0)) * 0.35;
    vec3 alb = mix(vec3(0.78, 0.66, 0.46), vec3(0.97, 0.92, 0.8), smoothstep(0.25, 0.75, bands));
    col = alb * smoothstep(-0.05, 0.3, ndl) * uDayGain;
    if (uLesR > 0.0) {
      float a = acos(clamp(dot(q, uLesC), -1.0, 1.0)); float n = fbm(q * 6.0) - 0.5; float e = a - uLesR - n * 0.4 * uLesR;
      float inside = 1.0 - smoothstep(-0.006, 0.006, e);
      vec3 cell = floor(q * 130.0); float lit = step(0.98, hash13(cell)) * (0.6 + 0.4 * hash13(cell + 7.0));
      float chan = pow(ridged(q * 20.0 + 5.0), 9.0);
      vec3 scar = vec3(0.02, 0.016, 0.013) * (0.6 + 0.8 * fbm(q * 30.0)) + vec3(1.0, 0.55, 0.18) * (lit * 1.4 + chan * 0.5) * uLesK;
      col = mix(col, scar, inside);
      col += vec3(1.0, 0.5, 0.14) * (exp(-abs(e) / 0.006) * 2.2 + pow(ridged(q * 16.0), 8.0) * smoothstep(0.25 * uLesR + 0.06, 0.0, e) * step(0.0, e) * 1.6) * uLesK;
      col += uAtmo * uAtmoK * pow(1.0 - view, 2.0) * clamp(ndl + 0.4, 0.0, 1.0) * (1.0 - 0.85 * inside);
    } else {
      col += uAtmo * uAtmoK * pow(1.0 - view, 2.0) * clamp(ndl + 0.4, 0.0, 1.0);
    }
  }
  o = vec4(col * uOpacity, uOpacity);
}`;

// --- points ---------------------------------------------------------------
const POINTS_VS = `#version 300 es
layout(location=0) in vec3 aPos; layout(location=1) in vec4 aCol; layout(location=2) in float aSize;
uniform mat4 uVP; uniform float uSizeK; uniform int uScreen; uniform float uPersp;
out vec4 vCol;
void main(){
  if (uScreen == 1) { gl_Position = vec4(aPos.xy, 0.0, 1.0); gl_PointSize = aSize * uSizeK; }
  else { gl_Position = uVP * vec4(aPos, 1.0); gl_PointSize = aSize * uSizeK * mix(1.0, 1.0 / max(gl_Position.w, 0.001), uPersp); }
  vCol = aCol; if (aCol.a <= 0.0) gl_Position = vec4(2.0, 2.0, 2.0, 1.0);
}`;
const POINTS_FS = `#version 300 es
precision highp float; in vec4 vCol; out vec4 o;
void main(){ vec2 d = gl_PointCoord * 2.0 - 1.0; float r2 = dot(d, d); if (r2 > 1.0) discard; float k = exp(-r2 * 4.0); o = vec4(vCol.rgb * vCol.a * k, 0.0); }`;

// --- lines: instanced screen-space quads ----------------------------------------
const LINES_VS = `#version 300 es
layout(location=0) in vec2 aCorner; layout(location=1) in vec3 aA; layout(location=2) in vec3 aB; layout(location=3) in vec4 aCol; layout(location=4) in float aW;
uniform mat4 uVP; uniform vec2 uRes; uniform float uWK; out vec4 vCol; out float vAcross;
void main(){
  vec4 ca = uVP * vec4(aA, 1.0), cb = uVP * vec4(aB, 1.0);
  if (ca.w < 0.001 || cb.w < 0.001 || aCol.a <= 0.0) { gl_Position = vec4(2.0, 2.0, 2.0, 1.0); vCol = vec4(0.0); vAcross = 0.0; return; }
  vec2 pa = ca.xy / ca.w * uRes * 0.5, pb = cb.xy / cb.w * uRes * 0.5;
  vec2 dir = pb - pa; float len = length(dir); dir = len > 1e-4 ? dir / len : vec2(1.0, 0.0); vec2 nrm = vec2(-dir.y, dir.x);
  float w = aW * uWK; vec2 p = mix(pa, pb, aCorner.x) + nrm * aCorner.y * w + dir * (aCorner.x * 2.0 - 1.0) * w * 0.5;
  float z = mix(ca.z / ca.w, cb.z / cb.w, aCorner.x);
  gl_Position = vec4(p / (uRes * 0.5), z, 1.0); vCol = aCol; vAcross = aCorner.y;
}`;
const LINES_FS = `#version 300 es
precision highp float; in vec4 vCol; in float vAcross; out vec4 o;
void main(){ float k = 1.0 - abs(vAcross); k = k * k * (3.0 - 2.0 * k); o = vec4(vCol.rgb * vCol.a * k, 0.0); }`;

// --- GPU particle systems: static buffers, positions computed from uniforms in the vertex shader -------
const PART_HEAD = `#version 300 es
layout(location=0) in vec4 a0; layout(location=1) in vec4 a1; layout(location=2) in vec4 a2; layout(location=3) in vec4 a3;
uniform mat4 uVP; uniform float uT, uSizeK, uYear; uniform vec3 uCenter; out vec4 vCol;
float hash11(float n){ return fract(sin(n * 12.9898) * 43758.5453); }
vec3 hash31(float n){ return fract(sin(vec3(n, n + 1.7, n + 3.1) * vec3(12.9898, 78.233, 37.719)) * 43758.5453); }
`;
const PART_TAIL = `
void main(){ vec3 pos; vec4 col; float size; particle(pos, col, size);
  if (col.a <= 0.0) { gl_Position = vec4(2.0, 2.0, 2.0, 1.0); gl_PointSize = 0.0; vCol = vec4(0.0); return; }
  gl_Position = uVP * vec4(pos, 1.0); gl_PointSize = size * uSizeK; vCol = col; }`;

// --- post -----------------------------------------------------------------
const DOWN_FS = `#version 300 es
precision highp float; in vec2 vUV; out vec4 o; uniform sampler2D uSrc; uniform vec2 uTexel; uniform float uThresh;
vec3 s(vec2 d){ return texture(uSrc, vUV + d * uTexel).rgb; }
void main(){
  vec3 c = s(vec2(0)) * 0.125 + (s(vec2(-1,-1)) + s(vec2(1,-1)) + s(vec2(-1,1)) + s(vec2(1,1))) * 0.125
         + (s(vec2(-2,0)) + s(vec2(2,0)) + s(vec2(0,-2)) + s(vec2(0,2))) * 0.0625 + (s(vec2(-2,-2)) + s(vec2(2,-2)) + s(vec2(-2,2)) + s(vec2(2,2))) * 0.03125;
  if (uThresh > 0.0) { float l = max(c.r, max(c.g, c.b)); c *= max(l - uThresh, 0.0) / max(l, 1e-4); }
  o = vec4(c, 1.0); }`;
const UP_FS = `#version 300 es
precision highp float; in vec2 vUV; out vec4 o; uniform sampler2D uSrc; uniform vec2 uTexel;
void main(){ vec3 c = vec3(0.0);
  for (int y = -1; y <= 1; y++) for (int x = -1; x <= 1; x++) { float w = (x == 0 ? 2.0 : 1.0) * (y == 0 ? 2.0 : 1.0); c += texture(uSrc, vUV + vec2(x, y) * uTexel).rgb * w; }
  o = vec4(c / 16.0, 1.0); }`;
const COMP_FS = `#version 300 es
precision highp float; in vec2 vUV; out vec4 o; uniform sampler2D uHdr, uBloom; uniform float uBloomK, uExposure, uGrain, uSeed, uVignette, uFade; uniform vec3 uFadeCol;
float h(vec2 p){ return fract(sin(dot(p, vec2(12.9898, 78.233)) + uSeed) * 43758.5453); }
void main(){
  vec3 c = texture(uHdr, vUV).rgb + texture(uBloom, vUV).rgb * uBloomK;
  c *= uExposure; c = clamp(c * (2.51 * c + 0.03) / (c * (2.43 * c + 0.59) + 0.14), 0.0, 1.0);
  vec2 d = vUV - 0.5; c *= 1.0 - uVignette * dot(d, d) * 1.6;
  c = pow(c, vec3(1.0 / 2.2)); c += (h(gl_FragCoord.xy) - 0.5) * uGrain; c = mix(uFadeCol, c, uFade);
  o = vec4(c, 1.0); }`;

function create(canvas, W, H) {
  const gl = canvas.getContext("webgl2", { antialias: false, alpha: false, depth: false, preserveDrawingBuffer: true, premultipliedAlpha: false });
  if (!gl) throw new Error("WebGL2 is not available");
  if (!gl.getExtension("EXT_color_buffer_float")) throw new Error("float render targets are not available");
  gl.getExtension("OES_texture_float_linear");
  const aniso = gl.getExtension("EXT_texture_filter_anisotropic");

  function prog(vs, fs) {
    const p = gl.createProgram();
    for (const [type, src] of [[gl.VERTEX_SHADER, vs], [gl.FRAGMENT_SHADER, fs]]) {
      const s = gl.createShader(type); gl.shaderSource(s, src); gl.compileShader(s);
      if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) throw new Error(gl.getShaderInfoLog(s) + "\n" + src.split("\n").map((l, i) => (i + 1) + ": " + l).join("\n"));
      gl.attachShader(p, s);
    }
    gl.linkProgram(p); if (!gl.getProgramParameter(p, gl.LINK_STATUS)) throw new Error(gl.getProgramInfoLog(p));
    const loc = {}; const n = gl.getProgramParameter(p, gl.ACTIVE_UNIFORMS);
    for (let i = 0; i < n; i++) { const u = gl.getActiveUniform(p, i); loc[u.name.replace(/\[0\]$/, "")] = gl.getUniformLocation(p, u.name); }
    return { p, loc };
  }
  function setU(pr, name, v) {
    const l = pr.loc[name]; if (l == null) return;
    if (typeof v === "number") gl.uniform1f(l, v);
    else if (v.length === 2) gl.uniform2fv(l, v); else if (v.length === 3) gl.uniform3fv(l, v); else if (v.length === 4) gl.uniform4fv(l, v);
    else if (v.length === 9) gl.uniformMatrix3fv(l, false, v); else if (v.length === 16) gl.uniformMatrix4fv(l, false, v);
    else if (v.length % 4 === 0) gl.uniform4fv(l, v);
  }
  function setI(pr, name, v) { const l = pr.loc[name]; if (l != null) gl.uniform1i(l, v); }

  function target(w, h, depth) {
    const tex = gl.createTexture(); gl.bindTexture(gl.TEXTURE_2D, tex);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA16F, w, h, 0, gl.RGBA, gl.HALF_FLOAT, null);
    for (const [k, v] of [[gl.TEXTURE_MIN_FILTER, gl.LINEAR], [gl.TEXTURE_MAG_FILTER, gl.LINEAR], [gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE], [gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE]]) gl.texParameteri(gl.TEXTURE_2D, k, v);
    const fb = gl.createFramebuffer(); gl.bindFramebuffer(gl.FRAMEBUFFER, fb); gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, tex, 0);
    if (depth) { const rb = gl.createRenderbuffer(); gl.bindRenderbuffer(gl.RENDERBUFFER, rb); gl.renderbufferStorage(gl.RENDERBUFFER, gl.DEPTH_COMPONENT24, w, h); gl.framebufferRenderbuffer(gl.FRAMEBUFFER, gl.DEPTH_ATTACHMENT, gl.RENDERBUFFER, rb); }
    return { tex, fb, w, h };
  }

  const P = {
    sphere: prog(FULL_VS, SPHERE_FS), points: prog(POINTS_VS, POINTS_FS), lines: prog(LINES_VS, LINES_FS),
    down: prog(FULL_VS, DOWN_FS), up: prog(FULL_VS, UP_FS), comp: prog(FULL_VS, COMP_FS),
  };
  const hdr = target(W, H, true);
  const mips = []; { let w = W, h = H; for (let i = 0; i < 6; i++) { w = Math.max(1, w >> 1); h = Math.max(1, h >> 1); mips.push(target(w, h, false)); } }
  const vaoEmpty = gl.createVertexArray();

  // dynamic buffers
  const ptBuf = gl.createBuffer(), ptVao = gl.createVertexArray();
  gl.bindVertexArray(ptVao); gl.bindBuffer(gl.ARRAY_BUFFER, ptBuf);
  gl.enableVertexAttribArray(0); gl.vertexAttribPointer(0, 3, gl.FLOAT, false, 32, 0);
  gl.enableVertexAttribArray(1); gl.vertexAttribPointer(1, 4, gl.FLOAT, false, 32, 12);
  gl.enableVertexAttribArray(2); gl.vertexAttribPointer(2, 1, gl.FLOAT, false, 32, 28);
  const lnBuf = gl.createBuffer(), lnVao = gl.createVertexArray(), corner = gl.createBuffer();
  gl.bindVertexArray(lnVao);
  gl.bindBuffer(gl.ARRAY_BUFFER, corner); gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([0, -1, 1, -1, 0, 1, 1, 1]), gl.STATIC_DRAW);
  gl.enableVertexAttribArray(0); gl.vertexAttribPointer(0, 2, gl.FLOAT, false, 0, 0);
  gl.bindBuffer(gl.ARRAY_BUFFER, lnBuf);
  gl.enableVertexAttribArray(1); gl.vertexAttribPointer(1, 3, gl.FLOAT, false, 44, 0); gl.vertexAttribDivisor(1, 1);
  gl.enableVertexAttribArray(2); gl.vertexAttribPointer(2, 3, gl.FLOAT, false, 44, 12); gl.vertexAttribDivisor(2, 1);
  gl.enableVertexAttribArray(3); gl.vertexAttribPointer(3, 4, gl.FLOAT, false, 44, 24); gl.vertexAttribDivisor(3, 1);
  gl.enableVertexAttribArray(4); gl.vertexAttribPointer(4, 1, gl.FLOAT, false, 44, 40); gl.vertexAttribDivisor(4, 1);
  gl.bindVertexArray(null);

  let cam = null;

  function particles(data, nVec4, body) {
    const pr = prog(PART_HEAD + body + PART_TAIL, POINTS_FS);
    const vao = gl.createVertexArray(), buf = gl.createBuffer();
    gl.bindVertexArray(vao); gl.bindBuffer(gl.ARRAY_BUFFER, buf); gl.bufferData(gl.ARRAY_BUFFER, data, gl.STATIC_DRAW);
    for (let i = 0; i < 4; i++) { if (i < nVec4) { gl.enableVertexAttribArray(i); gl.vertexAttribPointer(i, 4, gl.FLOAT, false, nVec4 * 16, i * 16); } else { gl.disableVertexAttribArray(i); gl.vertexAttrib4f(i, 0, 0, 0, 0); } }
    gl.bindVertexArray(null);
    return { pr, vao, n: data.length / (nVec4 * 4) };
  }
  const api = {
    gl, W, H, particles,
    drawParticles(sys, uniforms = {}, { depth = true, additive = true, count } = {}) {
      const pr = sys.pr; gl.useProgram(pr.p); gl.bindVertexArray(sys.vao);
      gl.enable(gl.BLEND); gl.blendFunc(gl.ONE, gl.ONE); gl.depthMask(false);
      if (depth) { gl.enable(gl.DEPTH_TEST); gl.depthFunc(gl.LEQUAL); } else gl.disable(gl.DEPTH_TEST);
      setU(pr, "uVP", cam.vp); setU(pr, "uSizeK", uniforms.uSizeK ?? 1);
      for (const [k, v] of Object.entries(uniforms)) setU(pr, k, v);
      gl.drawArrays(gl.POINTS, 0, count ?? sys.n);
    },
    dataTexture(w, h, bytes) {
      const t = gl.createTexture(); gl.bindTexture(gl.TEXTURE_2D, t); gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, false);
      gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA8, w, h, 0, gl.RGBA, gl.UNSIGNED_BYTE, bytes);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.REPEAT); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
      return { tex: t };
    },
    resize(w, h) { /* the film renders at a fixed internal size; the player scales the canvas */ },
    loadTexture(url) {
      return new Promise((res, rej) => {
        const img = new Image(); img.onload = () => {
          const t = gl.createTexture(); gl.bindTexture(gl.TEXTURE_2D, t); gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, false);
          gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA8, gl.RGBA, gl.UNSIGNED_BYTE, img); gl.generateMipmap(gl.TEXTURE_2D);
          gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR_MIPMAP_LINEAR); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
          gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.REPEAT); gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
          if (aniso) gl.texParameterf(gl.TEXTURE_2D, aniso.TEXTURE_MAX_ANISOTROPY_EXT, 8);
          res({ tex: t, img });
        };
        img.onerror = () => rej(new Error("could not load " + url)); img.src = url;
      });
    },
    // camera: position, target, up, vertical fov (degrees)
    camera(pos, tgt, up, fovDeg, near = 0.01, far = 1e6) {
      const f = norm(sub(tgt, pos)), r = norm(cross(f, up)), u = cross(r, f);
      const tanHalf = Math.tan(fovDeg * Math.PI / 360), aspect = W / H;
      const view = [r[0], u[0], -f[0], 0, r[1], u[1], -f[1], 0, r[2], u[2], -f[2], 0, -dot(r, pos), -dot(u, pos), dot(f, pos), 1];
      const proj = [1 / (tanHalf * aspect), 0, 0, 0, 0, 1 / tanHalf, 0, 0, 0, 0, -(far + near) / (far - near), -1, 0, 0, -2 * far * near / (far - near), 0];
      cam = { pos, f, r, u, tanHalf, aspect, vp: mul4(proj, view) };
      return cam;
    },
    project(p) { const v = cam.vp, x = v[0] * p[0] + v[4] * p[1] + v[8] * p[2] + v[12], y = v[1] * p[0] + v[5] * p[1] + v[9] * p[2] + v[13], w = v[3] * p[0] + v[7] * p[1] + v[11] * p[2] + v[15]; return w <= 0 ? null : [(x / w * 0.5 + 0.5) * W, (1 - (y / w * 0.5 + 0.5)) * H, w]; },
    begin() {
      gl.bindFramebuffer(gl.FRAMEBUFFER, hdr.fb); gl.viewport(0, 0, W, H);
      gl.clearColor(0, 0, 0, 1); gl.clearDepth(1); gl.depthMask(true); gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
    },
    sphere(o) {
      const pr = P.sphere; gl.useProgram(pr.p); gl.bindVertexArray(vaoEmpty);
      gl.enable(gl.BLEND); gl.blendFunc(gl.ONE, gl.ONE_MINUS_SRC_ALPHA); gl.enable(gl.DEPTH_TEST); gl.depthFunc(gl.LEQUAL); gl.depthMask(true);
      setU(pr, "uCamPos", cam.pos); setU(pr, "uCamR", cam.r); setU(pr, "uCamU", cam.u); setU(pr, "uCamF", cam.f); setU(pr, "uTanHalf", cam.tanHalf); setU(pr, "uAspect", cam.aspect); setU(pr, "uVP", cam.vp);
      const d = { center: [0, 0, 0], radius: 1, rot: [1, 0, 0, 0, 1, 0, 0, 0, 1], sun: [1, 0, 0], mode: 0, dayGain: 1, nightGain: 1, opacity: 1, thermal: 0, heat: 0, ocean: 1, ir: 0, emissive: 1, time: 0, desat: 0, atmo: [0.3, 0.55, 1.0], atmoK: 0, lesC: [0, 1, 0], lesR: 0, lesK: 1, tint: [1, 1, 1], year: 2026, clouds: 0, hasGrow: 0, seaStart: 2100, seaEnd: 2191, ...o };
      if (d.grow) d.hasGrow = 1;
      for (const [k, v] of Object.entries(d)) if (!["mode", "day", "night", "grow"].includes(k)) setU(pr, "u" + k[0].toUpperCase() + k.slice(1), v);
      setI(pr, "uMode", d.mode);
      gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, d.day ? d.day.tex : null); setI(pr, "uDay", 0);
      gl.activeTexture(gl.TEXTURE1); gl.bindTexture(gl.TEXTURE_2D, d.night ? d.night.tex : null); setI(pr, "uNight", 1);
      gl.activeTexture(gl.TEXTURE2); gl.bindTexture(gl.TEXTURE_2D, d.grow ? d.grow.tex : null); setI(pr, "uGrow", 2);
      gl.drawArrays(gl.TRIANGLES, 0, 3);
    },
    // points: Float32Array of [x,y,z, r,g,b,a, size] * n
    points(data, n, { screen = false, sizeK = 1, persp = 0, depth = true } = {}) {
      if (!n) return;
      const pr = P.points; gl.useProgram(pr.p); gl.bindVertexArray(ptVao);
      gl.bindBuffer(gl.ARRAY_BUFFER, ptBuf); gl.bufferData(gl.ARRAY_BUFFER, data.subarray(0, n * 8), gl.STREAM_DRAW);
      gl.enable(gl.BLEND); gl.blendFunc(gl.ONE, gl.ONE); gl.depthMask(false);
      if (depth && !screen) { gl.enable(gl.DEPTH_TEST); gl.depthFunc(gl.LEQUAL); } else gl.disable(gl.DEPTH_TEST);
      setU(pr, "uVP", cam ? cam.vp : identity()); setU(pr, "uSizeK", sizeK); setI(pr, "uScreen", screen ? 1 : 0); setU(pr, "uPersp", persp);
      gl.drawArrays(gl.POINTS, 0, n);
    },
    // lines: Float32Array of [ax,ay,az, bx,by,bz, r,g,b,a, width] * n
    lines(data, n, { wK = 1, depth = true } = {}) {
      if (!n) return;
      const pr = P.lines; gl.useProgram(pr.p); gl.bindVertexArray(lnVao);
      gl.bindBuffer(gl.ARRAY_BUFFER, lnBuf); gl.bufferData(gl.ARRAY_BUFFER, data.subarray(0, n * 11), gl.STREAM_DRAW);
      gl.enable(gl.BLEND); gl.blendFunc(gl.ONE, gl.ONE); gl.depthMask(false);
      if (depth) { gl.enable(gl.DEPTH_TEST); gl.depthFunc(gl.LEQUAL); } else gl.disable(gl.DEPTH_TEST);
      setU(pr, "uVP", cam.vp); setU(pr, "uRes", [W, H]); setU(pr, "uWK", wK);
      gl.drawArraysInstanced(gl.TRIANGLE_STRIP, 0, 4, n);
    },
    // a full-screen program written by a scene (procedural skies, grounds)
    program(fs) { return prog(FULL_VS, fs); },
    fullscreen(pr, uniforms = {}, textures = {}, blend = "add") {
      gl.useProgram(pr.p); gl.bindVertexArray(vaoEmpty); gl.disable(gl.DEPTH_TEST); gl.depthMask(false);
      gl.enable(gl.BLEND); if (blend === "add") gl.blendFunc(gl.ONE, gl.ONE); else gl.blendFunc(gl.ONE, gl.ONE_MINUS_SRC_ALPHA);
      let unit = 0; for (const [k, t] of Object.entries(textures)) { gl.activeTexture(gl.TEXTURE0 + unit); gl.bindTexture(gl.TEXTURE_2D, t.tex); setI(pr, k, unit); unit++; }
      setU(pr, "uRes", [W, H]); for (const [k, v] of Object.entries(uniforms)) (Number.isInteger(v) && k.startsWith("i")) ? setI(pr, k, v) : setU(pr, k, v);
      gl.drawArrays(gl.TRIANGLES, 0, 3);
    },
    end({ bloom = 0.9, exposure = 1, grain = 0.035, vignette = 0.35, fade = 1, seed = 0, thresh = 0.9, fadeCol = [0, 0, 0] } = {}) {
      gl.disable(gl.DEPTH_TEST); gl.disable(gl.BLEND); gl.bindVertexArray(vaoEmpty);
      let src = hdr;
      for (let i = 0; i < mips.length; i++) {
        const m = mips[i]; gl.bindFramebuffer(gl.FRAMEBUFFER, m.fb); gl.viewport(0, 0, m.w, m.h);
        gl.useProgram(P.down.p); gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, src.tex); setI(P.down, "uSrc", 0);
        setU(P.down, "uTexel", [1 / src.w, 1 / src.h]); setU(P.down, "uThresh", i === 0 ? thresh : 0); gl.drawArrays(gl.TRIANGLES, 0, 3); src = m;
      }
      gl.enable(gl.BLEND); gl.blendFunc(gl.ONE, gl.ONE);
      for (let i = mips.length - 1; i > 0; i--) {
        const s = mips[i], d = mips[i - 1]; gl.bindFramebuffer(gl.FRAMEBUFFER, d.fb); gl.viewport(0, 0, d.w, d.h);
        gl.useProgram(P.up.p); gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, s.tex); setI(P.up, "uSrc", 0); setU(P.up, "uTexel", [1 / s.w, 1 / s.h]);
        gl.drawArrays(gl.TRIANGLES, 0, 3);
      }
      gl.disable(gl.BLEND);
      gl.bindFramebuffer(gl.FRAMEBUFFER, null); gl.viewport(0, 0, W, H);
      gl.useProgram(P.comp.p);
      gl.activeTexture(gl.TEXTURE0); gl.bindTexture(gl.TEXTURE_2D, hdr.tex); setI(P.comp, "uHdr", 0);
      gl.activeTexture(gl.TEXTURE1); gl.bindTexture(gl.TEXTURE_2D, mips[0].tex); setI(P.comp, "uBloom", 1);
      setU(P.comp, "uBloomK", bloom); setU(P.comp, "uExposure", exposure); setU(P.comp, "uGrain", grain); setU(P.comp, "uSeed", seed); setU(P.comp, "uVignette", vignette); setU(P.comp, "uFade", fade); setU(P.comp, "uFadeCol", fadeCol);
      gl.drawArrays(gl.TRIANGLES, 0, 3);
    },
  };
  return api;
}

function sub(a, b) { return [a[0] - b[0], a[1] - b[1], a[2] - b[2]]; }
function dot(a, b) { return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]; }
function cross(a, b) { return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]; }
function norm(a) { const l = Math.hypot(a[0], a[1], a[2]) || 1; return [a[0] / l, a[1] / l, a[2] / l]; }
function identity() { return [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]; }
function mul4(a, b) { const o = new Array(16); for (let c = 0; c < 4; c++) for (let r = 0; r < 4; r++) { let s = 0; for (let k = 0; k < 4; k++) s += a[k * 4 + r] * b[c * 4 + k]; o[c * 4 + r] = s; } return o; }
// rotation matrix (column-major mat3) mapping world to body frame: spin about the body's y axis, then tilt about x
function bodyRot(spin, tilt = 0) {
  const cs = Math.cos(spin), sn = Math.sin(spin), ct = Math.cos(tilt), st = Math.sin(tilt);
  // R = Ry(spin) * Rx(tilt); return its transpose? We want q = R * n in the shader with column-major upload.
  const rx = [1, 0, 0, 0, ct, st, 0, -st, ct], ry = [cs, 0, -sn, 0, 1, 0, sn, 0, cs];
  const m = new Array(9); for (let c = 0; c < 3; c++) for (let r = 0; r < 3; r++) { let s = 0; for (let k = 0; k < 3; k++) s += ry[k * 3 + r] * rx[c * 3 + k]; m[c * 3 + r] = s; }
  return m;
}
return { create, sub, dot, cross, norm, bodyRot };
})();
