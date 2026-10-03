// The soundtrack of v2, synthesized from the film's own clocks: one click per doubling of POWER,
// a tone that rises with it, and the events of each scene. Deterministic; rendered offline.
"use strict";
const Sound = (() => {
function rngOf(seed) { let a = seed >>> 0; return () => { a = (a + 0x6D2B79F5) | 0; let t = Math.imul(a ^ (a >>> 15), 1 | a); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; }
async function render(dur = 300, sr = 44100) {
  const ac = new OfflineAudioContext(1, Math.ceil(sr * dur), sr);
  const master = ac.createGain(); master.gain.value = 0.9;
  const comp = ac.createDynamicsCompressor(); comp.threshold.value = -18; comp.ratio.value = 3.5; master.connect(comp); comp.connect(ac.destination);
  const nb = ac.createBuffer(1, sr * 2, sr); { const d = nb.getChannelData(0), r = rngOf(5); let b = 0; for (let i = 0; i < d.length; i++) d[i] = r() * 2 - 1; }
  const r = rngOf(9);
  function noise(t0, t1, type, f0, f1, q, env) {
    const s = ac.createBufferSource(); s.buffer = nb; s.loop = true;
    const f = ac.createBiquadFilter(); f.type = type; f.Q.value = q; f.frequency.setValueAtTime(f0, t0); f.frequency.exponentialRampToValueAtTime(f1, Math.max(t1, t0 + 0.01));
    const g = ac.createGain(); g.gain.setValueAtTime(0, t0); env(g.gain);
    s.connect(f); f.connect(g); g.connect(master); s.start(t0, r() * 1.5); s.stop(t1 + 0.05);
  }
  function tone(t0, t1, f0, f1, peak, type = "sine", attack = 0.01) {
    const o = ac.createOscillator(); o.type = type; o.frequency.setValueAtTime(f0, t0); if (f1 !== f0) o.frequency.exponentialRampToValueAtTime(f1, t1);
    const g = ac.createGain(); g.gain.setValueAtTime(0.0001, t0); g.gain.exponentialRampToValueAtTime(peak, t0 + attack); g.gain.exponentialRampToValueAtTime(0.0001, t1);
    o.connect(g); g.connect(master); o.start(t0); o.stop(t1 + 0.02);
  }
  function pad(t0, t1, freqs, peak, type = "sine", fadeIn = 1, fadeOut = 1) {
    for (const fr of freqs) { const o = ac.createOscillator(); o.type = type; o.frequency.value = fr; const g = ac.createGain(); g.gain.setValueAtTime(0, t0); g.gain.linearRampToValueAtTime(peak, t0 + fadeIn); g.gain.setValueAtTime(peak, t1 - fadeOut); g.gain.linearRampToValueAtTime(0, t1); o.connect(g); g.connect(master); o.start(t0); o.stop(t1 + 0.02); }
  }
  const L = t => Math.log10(Math.max(1, Film.powerAt(t)));
  // 1. room tone; the first click as the Earth appears
  noise(0.3, 7.2, "lowpass", 260, 260, 0.6, g => { g.linearRampToValueAtTime(0.05, 1.8); g.setValueAtTime(0.05, 5.5); g.linearRampToValueAtTime(0, 7.2); });
  tone(6.9, 7.0, 1500, 1500, 0.15);
  // the compounding clock: one click per doubling of POWER, pitch rising with it; muffled in the ground shots
  const ground = t => (t >= 33 && t < 41) || (t >= 72 && t < 84.5) || (t >= 138 && t < 144);
  let last = Math.floor(Math.log2(Film.powerAt(7.5)));
  for (let t = 7.5; t < 132; t += 0.004) {
    const d = Math.floor(Math.log2(Film.powerAt(t)));
    if (d > last) { last = d; const k = ground(t) ? 0.35 : 1; const f = 1100 + (L(t) - 10.8) * 70; tone(t, t + 0.06, f, f, 0.13 * k); noise(t, t + 0.02, "bandpass", ground(t) ? 900 : 4000, ground(t) ? 900 : 4000, 2, g => { g.linearRampToValueAtTime(0.06 * k, t + 0.002); g.exponentialRampToValueAtTime(0.0001, t + 0.02); }); }
  }
  // the tone that rises with the power, ducked on the ground
  {
    const f = ac.createBiquadFilter(); f.type = "lowpass"; f.Q.value = 2.5; const g = ac.createGain(); g.gain.setValueAtTime(0, 7);
    const fc = [], pitch = []; for (let k = 0; k <= 500; k++) { const t = 7 + k * 0.25; const x = (L(t) - 10.8) / 15.8; fc.push((ground(t) ? 0.35 : 1) * (180 + Math.pow(Math.max(0, x), 1.4) * 1800)); pitch.push(55 * Math.pow(2, Math.max(0, x) * 2)); }
    f.frequency.setValueCurveAtTime(Float32Array.from(fc), 7, 125);
    const keys = [[7, 0], [12, 0.03], [33, 0.05], [33.3, 0.012], [40.7, 0.012], [41.2, 0.06], [72, 0.08], [72.3, 0.02], [84.3, 0.02], [84.8, 0.09], [132, 0.13], [138, 0.06], [138.3, 0.015], [143.7, 0.015], [144.2, 0.05], [149, 0]];
    for (const [t, v] of keys) g.gain.linearRampToValueAtTime(v, t);
    for (const [k, type, det] of [[0, "sawtooth", 1], [1, "sawtooth", 1.006], [2, "sine", 0.5]]) { const o = ac.createOscillator(); o.type = type; o.frequency.setValueCurveAtTime(Float32Array.from(pitch.map(p => p * det)), 7, 125); const og = ac.createGain(); og.gain.value = k === 2 ? 0.9 : 0.4; o.connect(og); og.connect(f); o.start(7); o.stop(149.1); }
    f.connect(g); g.connect(master);
  }
  // the dive and the campus: air, then a launch
  noise(30.5, 33.2, "bandpass", 300, 1800, 0.5, g => { g.linearRampToValueAtTime(0.1, 32.6); g.linearRampToValueAtTime(0, 33.2); });
  noise(33, 41, "lowpass", 500, 500, 0.4, g => { g.linearRampToValueAtTime(0.025, 34); g.setValueAtTime(0.025, 40); g.linearRampToValueAtTime(0, 41); });
  noise(35.2, 42, "lowpass", 140, 90, 0.7, g => { g.linearRampToValueAtTime(0.24, 39); g.linearRampToValueAtTime(0, 42); });
  // sensor switches
  tone(50, 50.08, 2400, 2400, 0.05); tone(59.6, 59.68, 2400, 2400, 0.05);
  // the vents
  noise(60, 72, "bandpass", 450, 700, 0.5, g => { g.linearRampToValueAtTime(0.12, 63); g.setValueAtTime(0.12, 70.8); g.linearRampToValueAtTime(0, 72); });
  noise(70, 72.2, "bandpass", 300, 1800, 0.5, g => { g.linearRampToValueAtTime(0.1, 71.6); g.linearRampToValueAtTime(0, 72.2); });
  // inside the glass world: wind and a low hum
  noise(72, 84.5, "lowpass", 380, 380, 0.5, g => { g.linearRampToValueAtTime(0.04, 73); g.setValueAtTime(0.04, 83.8); g.linearRampToValueAtTime(0, 84.5); });
  pad(74, 84, [110, 164.8], 0.011, "sine", 0.8, 0.8);
  // the rise and the flight inward
  noise(84.3, 86, "bandpass", 1800, 300, 0.6, g => { g.linearRampToValueAtTime(0.08, 84.6); g.linearRampToValueAtTime(0, 86); });
  noise(92, 98.8, "bandpass", 400, 1600, 0.6, g => { g.linearRampToValueAtTime(0.07, 96); g.linearRampToValueAtTime(0, 98.8); });
  // Mercury and Venus
  for (let i = 0; i < 140; i++) { const f = i / 140, t = 100 + 8 * Math.pow(f, 0.6); tone(t, t + 0.03, 2800 + r() * 1400, 2800, 0.02); }
  noise(107.3, 111.2, "lowpass", 150, 80, 0.8, g => { g.linearRampToValueAtTime(0.3, 109); g.linearRampToValueAtTime(0, 111.2); });
  noise(111.2, 113.8, "bandpass", 600, 1400, 0.6, g => { g.linearRampToValueAtTime(0.05, 112.5); g.linearRampToValueAtTime(0, 113.8); });
  for (let i = 0; i < 70; i++) { const t = 113.8 + 3.6 * Math.pow(i / 70, 0.7); tone(t, t + 0.03, 3200 + r() * 900, 3200, 0.018); }
  noise(116, 118.6, "lowpass", 140, 80, 0.8, g => { g.linearRampToValueAtTime(0.22, 117.2); g.linearRampToValueAtTime(0, 118.6); });
  // the swarm; the drop into infrared
  noise(119, 132, "highpass", 5000, 7000, 0.4, g => { g.linearRampToValueAtTime(0.035, 127); g.linearRampToValueAtTime(0.01, 129.5); g.linearRampToValueAtTime(0, 132); });
  noise(127.5, 129.5, "bandpass", 1200, 150, 0.8, g => { g.linearRampToValueAtTime(0.08, 127.8); g.exponentialRampToValueAtTime(0.0001, 129.5); });
  // the relay
  tone(132.4, 134.6, 300, 900, 0.07); pad(134.5, 137.8, [880], 0.02, "sine", 0.4, 0.6);
  // two suns
  pad(138.2, 143.8, [1318.5], 0.014, "sine", 1, 1);
  // probes, the ride, the transit
  for (let i = 0; i < 160; i++) { const t = 144.3 + Math.pow(r(), 1.6) * 4; tone(t, t + 0.04, 1800 + r() * 1600, 1500, 0.018); }
  noise(147, 154.5, "bandpass", 300, 2600, 0.6, g => { g.linearRampToValueAtTime(0.09, 151.5); g.linearRampToValueAtTime(0, 154.5); });
  // the cell
  pad(154, 171, [55], 0.025, "sine", 1.5, 1.5);
  tone(158.5, 159.4, 90, 38, 0.32);
  for (let i = 0; i < 90; i++) { const t = 158.8 + 5.2 * Math.pow(i / 90, 0.65); tone(t, t + 0.03, 3000 + r() * 900, 3000, 0.018); }
  noise(163, 166.7, "lowpass", 160, 80, 0.8, g => { g.linearRampToValueAtTime(0.24, 164.5); g.linearRampToValueAtTime(0, 166.7); });
  pad(166, 171, [65.4], 0.06, "sine", 1, 3.5);
  // the front
  noise(171, 195, "highpass", 3500, 6500, 0.5, g => { g.linearRampToValueAtTime(0.045, 190); g.linearRampToValueAtTime(0, 195); });
  { const o = ac.createOscillator(); o.type = "triangle"; o.frequency.setValueAtTime(110, 171); o.frequency.exponentialRampToValueAtTime(220, 194); const g = ac.createGain(); g.gain.setValueAtTime(0, 171); g.gain.linearRampToValueAtTime(0.035, 190); g.gain.linearRampToValueAtTime(0, 195); o.connect(g); g.connect(master); o.start(171); o.stop(195.1); }
  // the last sky, the efficient galaxy, the edge
  pad(195, 202, [55, 82.5], 0.025, "sine", 0.6, 0.6);
  pad(202, 215, [55, 110], 0.028, "sine", 0.8, 0.8);
  pad(215, 223, [110], 0.02, "sine", 0.5, 2.5);
  // 21. the split: dissonance
  pad(223.3, 262, [110, 116.5, 155.6], 0.035, "triangle", 6, 3);
  // 22–23. beams leave, impacts arrive late
  const G = Film.galaxy(); let n = 0, lastBoom = 0;
  for (const v of G.volleys.slice().sort((a, b) => a.t0 - b.t0)) { if (n++ > 400) break; if (v.t0 < 262) tone(v.t0, v.t0 + 0.25, 2100 + r() * 500, 260, 0.028); if (v.t1 < 262 && v.t1 - lastBoom > 0.09) { lastBoom = v.t1; tone(v.t1, v.t1 + 0.7, 72, 34, 0.1); } }
  if (G.sweep.length) noise(G.sweep[0].t - 0.6, G.sweep[G.sweep.length - 1].t + 0.5, "bandpass", 3000, 500, 1.4, g => { g.linearRampToValueAtTime(0.09, G.sweep[0].t - 0.2); g.linearRampToValueAtTime(0, G.sweep[G.sweep.length - 1].t + 0.5); });
  for (const s of G.sweep) tone(s.t, s.t + 0.6, 70, 34, 0.08);
  tone(262.6, 263.2, 1900, 240, 0.05); tone(262.62, 263.2, 1700, 220, 0.05);
  tone(268.6, 272, 50, 22, 0.5); noise(268.6, 272, "lowpass", 320, 60, 0.7, g => { g.linearRampToValueAtTime(0.4, 268.7); g.exponentialRampToValueAtTime(0.0001, 272); });
  // 25. the title
  for (const [k, fr] of [98, 196, 293.7].entries()) tone(281.2, 290, fr, fr, 0.12 / (k + 1), "sine", 0.02);
  return ac.startRendering();
}
function wav(buf) {
  const sr = buf.sampleRate, d = buf.getChannelData(0), n = d.length, out = new DataView(new ArrayBuffer(44 + n * 2));
  const w = (o, s) => { for (let i = 0; i < s.length; i++) out.setUint8(o + i, s.charCodeAt(i)); };
  w(0, "RIFF"); out.setUint32(4, 36 + n * 2, true); w(8, "WAVE"); w(12, "fmt "); out.setUint32(16, 16, true); out.setUint16(20, 1, true); out.setUint16(22, 1, true);
  out.setUint32(24, sr, true); out.setUint32(28, sr * 2, true); out.setUint16(32, 2, true); out.setUint16(34, 16, true); w(36, "data"); out.setUint32(40, n * 2, true);
  for (let i = 0; i < n; i++) out.setInt16(44 + i * 2, Math.round(Math.max(-1, Math.min(1, d[i])) * 32767), true);
  return new Uint8Array(out.buffer);
}
return { render, wav };
})();
