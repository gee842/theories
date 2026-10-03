// The soundtrack, synthesized from the film's own clocks and rendered offline. Events are written in story
// time and placed in film time through Film.filmT, so the tightened pacing stays in sync.
// Design: a slow chord pad that darkens act by act; a soft clock tick per doubling of compute; a low tone
// that rises with compute; scene events; reverb on everything; silence before the title.
"use strict";
const Sound = (() => {
function rngOf(seed) { let a = seed >>> 0; return () => { a = (a + 0x6D2B79F5) | 0; let t = Math.imul(a ^ (a >>> 15), 1 | a); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; }
async function render(sr = 44100) {
  const F = t => Film.filmT(t), S = f => Film.storyT(f), DUR = Film.DUR;
  const ac = new OfflineAudioContext(2, Math.ceil(sr * DUR), sr);
  // buses: dry → master; send → reverb → master
  const master = ac.createGain(); master.gain.value = 0.85;
  const comp = ac.createDynamicsCompressor(); comp.threshold.value = -20; comp.ratio.value = 3; comp.attack.value = 0.01; comp.release.value = 0.4;
  master.connect(comp); comp.connect(ac.destination);
  const verb = ac.createConvolver(); { const len = sr * 4.2, ir = ac.createBuffer(2, len, sr), r = rngOf(17); for (let c = 0; c < 2; c++) { const d = ir.getChannelData(c); for (let i = 0; i < len; i++) d[i] = (r() * 2 - 1) * Math.pow(1 - i / len, 3.2) * (i < sr * 0.012 ? i / (sr * 0.012) : 1); } verb.buffer = ir; }
  const wet = ac.createGain(); wet.gain.value = 0.55; verb.connect(wet); wet.connect(master);
  const out = (node, send = 0.5, pan = 0) => { const p = ac.createStereoPanner(); p.pan.value = pan; node.connect(p); p.connect(master); if (send > 0) { const sg = ac.createGain(); sg.gain.value = send; p.connect(sg); sg.connect(verb); } };
  const nb = ac.createBuffer(1, sr * 2, sr); { const d = nb.getChannelData(0), r = rngOf(5); for (let i = 0; i < d.length; i++) d[i] = r() * 2 - 1; }
  const r = rngOf(9);
  const P = g => ({ setValueAtTime: (v, t) => g.setValueAtTime(v, F(t)), linearRampToValueAtTime: (v, t) => g.linearRampToValueAtTime(v, F(t)), exponentialRampToValueAtTime: (v, t) => g.exponentialRampToValueAtTime(v, F(t)) });
  function noise(t0, t1, type, f0, f1, q, env, send = 0.5, pan = 0) {
    const s = ac.createBufferSource(); s.buffer = nb; s.loop = true;
    const f = ac.createBiquadFilter(); f.type = type; f.Q.value = q; f.frequency.setValueAtTime(f0, F(t0)); f.frequency.exponentialRampToValueAtTime(f1, Math.max(F(t1), F(t0) + 0.01));
    const g = ac.createGain(); g.gain.setValueAtTime(0, F(t0)); env(P(g.gain));
    s.connect(f); f.connect(g); out(g, send, pan); s.start(F(t0), r() * 1.5); s.stop(F(t1) + 0.05);
  }
  function tone(t0, t1, f0, f1, peak, type = "sine", attack = 0.01, send = 0.5, pan = 0) {
    const a = F(t0), b = Math.max(F(t1), a + 0.02); const o = ac.createOscillator(); o.type = type; o.frequency.setValueAtTime(f0, a); if (f1 !== f0) o.frequency.exponentialRampToValueAtTime(f1, b);
    const g = ac.createGain(); g.gain.setValueAtTime(0.0001, a); g.gain.exponentialRampToValueAtTime(peak, a + attack); g.gain.exponentialRampToValueAtTime(0.0001, b);
    o.connect(g); out(g, send, pan); o.start(a); o.stop(b + 0.02);
  }
  // a soft clock tick: a short filtered click and a low thump
  function tick(t, k = 1) { const a = F(t); noise(t, S(a + 0.03), "bandpass", 2100, 1800, 5, g => { g.linearRampToValueAtTime(0.09 * k, S(a + 0.002)); g.exponentialRampToValueAtTime(0.0001, S(a + 0.03)); }, 0.35); tone(t, S(a + 0.09), 95, 60, 0.12 * k, "sine", 0.004, 0.2); }
  // the pad: chords that change by act, slowly, with a breathing lowpass
  function chord(t0, t1, freqs, peak, cutoff = 900, fadeIn = 3, fadeOut = 3) {
    const a = F(t0), b = F(t1); const f = ac.createBiquadFilter(); f.type = "lowpass"; f.frequency.value = cutoff; f.Q.value = 0.5;
    const g = ac.createGain(); g.gain.setValueAtTime(0, a); g.gain.linearRampToValueAtTime(peak, a + fadeIn); g.gain.setValueAtTime(peak, Math.max(a + fadeIn, b - fadeOut)); g.gain.linearRampToValueAtTime(0, b);
    const lfo = ac.createOscillator(); lfo.frequency.value = 0.07; const lg = ac.createGain(); lg.gain.value = cutoff * 0.25; lfo.connect(lg); lg.connect(f.frequency); lfo.start(a); lfo.stop(b + 0.1);
    for (const [i, fr] of freqs.entries()) for (const det of [-7, 0, 7]) { const o = ac.createOscillator(); o.type = i === 0 ? "sine" : "sawtooth"; o.frequency.value = fr; o.detune.value = det; const og = ac.createGain(); og.gain.value = i === 0 ? 1 : 0.32; o.connect(og); og.connect(f); o.start(a); o.stop(b + 0.1); }
    f.connect(g); out(g, 0.8, 0);
  }
  // a progression: the span is shared among the chords, each crossfading into the next
  function prog(t0, t1, chords, peak, cutoff, fade = 2.5) { const n = chords.length, len = (t1 - t0) / n;
    chords.forEach((c, i) => chord(t0 + i * len - (i ? fade / 2 : 0), t0 + (i + 1) * len + (i < n - 1 ? fade / 2 : 0), c, peak, cutoff, i ? fade : 4, i < n - 1 ? fade : 4)); }
  // a felt-piano note: a few partials with their own decays, a soft hammer
  function pnote(t, fr, vel = 0.05, dur = 5, pan = 0) { const a = F(t);
    for (const [m, amp, dec] of [[1, 1, 1], [2, 0.38, 0.65], [3, 0.14, 0.45], [4.03, 0.06, 0.3], [5.12, 0.03, 0.22]]) { const o = ac.createOscillator(); o.frequency.value = fr * m; const g = ac.createGain();
      g.gain.setValueAtTime(0.0001, a); g.gain.exponentialRampToValueAtTime(vel * amp, a + 0.006); g.gain.exponentialRampToValueAtTime(0.0001, a + dur * dec); o.connect(g); out(g, 0.75, pan); o.start(a); o.stop(a + dur * dec + 0.05); }
    noise(t, S(a + 0.06), "lowpass", 1400, 300, 0.5, g => { g.linearRampToValueAtTime(vel * 0.35, S(a + 0.003)); g.exponentialRampToValueAtTime(0.0001, S(a + 0.06)); }, 0.3, pan); }
  // the motif: four falling notes, the game's figure; stated at every wall, lower as it goes; it breaks off when nothing is left to win
  const MOTIF = [523.25, 493.88, 440, 329.63];
  function motif(t0, oct = 1, vel = 0.045, notes = 4, gap = 0.95) { const a = F(t0); for (let k = 0; k < notes; k++) pnote(S(a + k * gap), MOTIF[k] * oct, vel * (k === 3 ? 1.15 : 1), k === notes - 1 ? 7 : 4.5, (k - 1.5) * 0.12); }
  const L10 = t => Math.log10(Math.max(1, Film.powerAt(t)));
  const ground = t => (t >= 33 && t < 41) || (t >= 72 && t < 84.5) || (t >= 138 && t < 144) || (t >= 195 && t < 202);
  // ---- the pad, act by act (story time)
  const Am = [110, 164.81, 220, 261.63, 329.63], F_ = [87.31, 130.81, 174.61, 220, 261.63], C = [65.41, 130.81, 196, 261.63, 329.63], G_ = [98, 146.83, 196, 246.94, 293.66],
    Dm = [73.42, 110, 146.83, 174.61, 220], E_ = [82.41, 123.47, 164.81, 207.65, 246.94], Cm = [65.41, 98, 130.81, 155.56, 196], Ab = [51.91, 103.83, 155.56, 207.65, 261.63], Eb = [77.78, 116.54, 155.56, 196, 233.08], Bb = [58.27, 116.54, 174.61, 233.08, 293.66];
  prog(0.5, 33, [Am, F_, C, G_], 0.012, 650);                    // today and the race: i VI III VII
  prog(33, 84.5, [Am, F_, C, G_, Am, F_, Dm, E_], 0.013, 750);    // the Earth: the same turn, then darker
  prog(84.5, 138, [F_, C, Dm, Am, F_, E_], 0.014, 850);           // the Sun
  prog(138, 171, [Dm, Am, Dm, E_], 0.013, 700);                   // the probes, the cell
  prog(171, 223, [Cm, Ab, Eb, Bb, Cm, Ab], 0.013, 600);           // the galaxy taken
  chord(223, 268, [61.74, 92.5, 116.54, 130.81, 185], 0.011, 520, 4, 5);   // a cluster: the split and the war
  // the motif at each wall
  motif(9.7); motif(27.6); motif(47.6, 1, 0.04); motif(56.8, 0.5, 0.05); motif(88.6, 0.5, 0.045); motif(129, 0.5, 0.05); motif(166.8, 0.5, 0.045); motif(190.4, 0.25, 0.06);
  motif(224.2, 0.5, 0.05, 3);                                     // nothing is left to win: it does not resolve
  // ---- 1. room tone; the Earth appears
  noise(0.3, 7.2, "lowpass", 260, 260, 0.6, g => { g.linearRampToValueAtTime(0.045, 1.8); g.setValueAtTime(0.045, 5.5); g.linearRampToValueAtTime(0, 7.2); }, 0.2);
  // ---- the compounding clock: one tick per doubling of compute; quieter on the ground
  let last = Math.floor(Math.log2(Film.powerAt(7.5)));
  for (let t = 7.5; t < 132; t += 0.004) { const d = Math.floor(Math.log2(Film.powerAt(t))); if (d > last) { last = d; tick(t, ground(t) ? 0.35 : 1); } }
  // ---- the low tone that rises with compute
  {
    const f = ac.createBiquadFilter(); f.type = "lowpass"; f.Q.value = 1.5; const g = ac.createGain(); g.gain.setValueAtTime(0, F(7));
    const fa = F(7), fb = F(148), n = Math.ceil((fb - fa) / 0.25), fc = [], pitch = [];
    for (let k = 0; k <= n; k++) { const st = S(fa + (fb - fa) * k / n); const x = Math.max(0, (L10(st) - 10.8) / 15.8); fc.push((ground(st) ? 0.4 : 1) * (150 + Math.pow(x, 1.4) * 1300)); pitch.push(55 * Math.pow(2, x * 1.5)); }
    f.frequency.setValueCurveAtTime(Float32Array.from(fc), fa, fb - fa);
    for (const [t, v] of [[7, 0], [14, 0.025], [33, 0.04], [33.3, 0.01], [40.7, 0.01], [41.2, 0.05], [72, 0.065], [72.3, 0.016], [84.3, 0.016], [84.8, 0.075], [132, 0.1], [138, 0.05], [138.3, 0.012], [143.7, 0.012], [144.2, 0.04], [148, 0]]) g.gain.linearRampToValueAtTime(v, F(t));
    for (const [k, type, det] of [[0, "sawtooth", 1], [1, "sawtooth", 1.005], [2, "sine", 0.5]]) { const o = ac.createOscillator(); o.type = type; o.frequency.setValueCurveAtTime(Float32Array.from(pitch.map(p => p * det)), fa, fb - fa); const og = ac.createGain(); og.gain.value = k === 2 ? 0.9 : 0.35; o.connect(og); og.connect(f); o.start(fa); o.stop(fb + 0.1); }
    const dg = ac.createGain(); dg.gain.value = 0.7; f.connect(g); g.connect(dg); out(dg, 0.4);
  }
  // ---- scene events
  noise(30.5, 33.2, "bandpass", 300, 1800, 0.5, g => { g.linearRampToValueAtTime(0.08, 32.6); g.linearRampToValueAtTime(0, 33.2); });                 // the dive
  noise(33, 41, "lowpass", 500, 500, 0.4, g => { g.linearRampToValueAtTime(0.02, 34); g.setValueAtTime(0.02, 40); g.linearRampToValueAtTime(0, 41); }, 0.3);
  noise(35.2, 42, "lowpass", 140, 80, 0.7, g => { g.linearRampToValueAtTime(0.22, 39); g.linearRampToValueAtTime(0, 42); }, 0.6);                    // a launch
  tone(50, 50.12, 2600, 2600, 0.025, "sine", 0.005, 0.6); tone(59.6, 59.72, 2600, 2600, 0.025, "sine", 0.005, 0.6);                                      // sensor switches
  noise(60, 72, "bandpass", 450, 700, 0.5, g => { g.linearRampToValueAtTime(0.1, 63); g.setValueAtTime(0.1, 70.8); g.linearRampToValueAtTime(0, 72); }, 0.5);   // the vents
  noise(70, 72.2, "bandpass", 300, 1800, 0.5, g => { g.linearRampToValueAtTime(0.08, 71.6); g.linearRampToValueAtTime(0, 72.2); });
  noise(72, 84.5, "lowpass", 380, 380, 0.5, g => { g.linearRampToValueAtTime(0.03, 73); g.setValueAtTime(0.03, 83.8); g.linearRampToValueAtTime(0, 84.5); }, 0.4);   // wind on the salt
  noise(84.3, 86, "bandpass", 1800, 300, 0.6, g => { g.linearRampToValueAtTime(0.06, 84.6); g.linearRampToValueAtTime(0, 86); });
  noise(92, 98.8, "bandpass", 400, 1600, 0.6, g => { g.linearRampToValueAtTime(0.05, 96); g.linearRampToValueAtTime(0, 98.8); });                    // the flight inward
  for (let i = 0; i < 120; i++) { const t = 100 + 8 * Math.pow(i / 120, 0.6); tone(t, t + 0.035, 2600 + r() * 1400, 2600, 0.012, "sine", 0.003, 0.6, (r() - 0.5) * 0.8); }   // factories
  noise(107.3, 111.2, "lowpass", 150, 70, 0.8, g => { g.linearRampToValueAtTime(0.26, 109); g.linearRampToValueAtTime(0, 111.2); }, 0.6);             // Mercury comes apart
  for (let i = 0; i < 60; i++) { const t = 113.8 + 3.6 * Math.pow(i / 60, 0.7); tone(t, t + 0.035, 3000 + r() * 900, 3000, 0.011, "sine", 0.003, 0.6, (r() - 0.5) * 0.8); }
  noise(116, 118.6, "lowpass", 140, 70, 0.8, g => { g.linearRampToValueAtTime(0.2, 117.2); g.linearRampToValueAtTime(0, 118.6); }, 0.6);
  noise(119, 132, "highpass", 5000, 7000, 0.4, g => { g.linearRampToValueAtTime(0.025, 127); g.linearRampToValueAtTime(0.008, 129.5); g.linearRampToValueAtTime(0, 132); }, 0.7);   // the swarm glitters
  noise(127.5, 129.5, "bandpass", 1200, 150, 0.8, g => { g.linearRampToValueAtTime(0.06, 127.8); g.exponentialRampToValueAtTime(0.0001, 129.5); });   // into the infrared
  tone(132.4, 134.6, 300, 900, 0.05, "sine", 0.3, 0.7); tone(134.5, 137.8, 880, 880, 0.015, "sine", 0.4, 0.8);                                         // the relay
  tone(138.2, 143.8, 1318.5, 1318.5, 0.01, "sine", 1.0, 0.9);                                                                                           // two suns
  for (let i = 0; i < 120; i++) { const t = 144.3 + Math.pow(r(), 1.6) * 4; tone(t, t + 0.05, 1800 + r() * 1600, 1500, 0.012, "sine", 0.003, 0.6, (r() - 0.5)); }   // probes
  noise(147, 154.5, "bandpass", 300, 2600, 0.6, g => { g.linearRampToValueAtTime(0.07, 151.5); g.linearRampToValueAtTime(0, 154.5); }, 0.5);          // the ride
  tone(158.5, 159.6, 90, 36, 0.28, "sine", 0.005, 0.5);                                                                                                  // landing
  for (let i = 0; i < 80; i++) { const t = 158.8 + 5.2 * Math.pow(i / 80, 0.65); tone(t, t + 0.035, 3000 + r() * 900, 3000, 0.011, "sine", 0.003, 0.6, (r() - 0.5) * 0.8); }
  noise(163, 166.7, "lowpass", 160, 70, 0.8, g => { g.linearRampToValueAtTime(0.2, 164.5); g.linearRampToValueAtTime(0, 166.7); }, 0.6);
  tone(166, 171, 65.4, 65.4, 0.05, "sine", 1.5, 0.8);                                                                                                   // the star goes dark
  noise(171, 195, "highpass", 3500, 6500, 0.5, g => { g.linearRampToValueAtTime(0.03, 190); g.linearRampToValueAtTime(0, 195); }, 0.7);               // the front
  // ---- the war: beams leave; impacts arrive late
  const G = Film.galaxy(); let n = 0, lastBoom = 0;
  for (const v of G.volleys.slice().sort((a, b) => a.t0 - b.t0)) { if (n++ > 360) break; if (v.t0 < 262) tone(v.t0, v.t0 + 0.25, 2000 + r() * 500, 260, 0.016, "sine", 0.004, 0.5, (r() - 0.5) * 1.2); if (v.t1 < 262 && v.t1 - lastBoom > 0.09) { lastBoom = v.t1; tone(v.t1, v.t1 + 0.8, 70, 32, 0.075, "sine", 0.006, 0.5, (r() - 0.5) * 1.2); } }
  if (G.sweep.length) noise(G.sweep[0].t - 0.6, G.sweep[G.sweep.length - 1].t + 0.5, "bandpass", 3000, 500, 1.4, g => { g.linearRampToValueAtTime(0.06, G.sweep[0].t - 0.2); g.linearRampToValueAtTime(0, G.sweep[G.sweep.length - 1].t + 0.5); }, 0.6);
  for (const s of G.sweep) tone(s.t, s.t + 0.6, 70, 32, 0.06, "sine", 0.006, 0.5);
  tone(262.6, 263.2, 1900, 240, 0.035, "sine", 0.004, 0.6, -0.4); tone(262.62, 263.2, 1700, 220, 0.035, "sine", 0.004, 0.6, 0.4);
  tone(268.6, 272.5, 48, 22, 0.42, "sine", 0.008, 0.9); noise(268.6, 272.5, "lowpass", 320, 50, 0.7, g => { g.linearRampToValueAtTime(0.32, 268.7); g.exponentialRampToValueAtTime(0.0001, 272.5); }, 0.9);
  // ---- the title: one low A, then nothing
  for (const [k, fr] of [55, 110, 164.81].entries()) tone(281.2, 292, fr, fr, 0.09 / (k + 1), "sine", 0.03, 0.9);
  motif(281.6, 0.5, 0.05, 4, 1.4);                                 // and once more, slowly, under the title
  return ac.startRendering();
}
function wav(buf) {
  const sr = buf.sampleRate, ch = buf.numberOfChannels, n = buf.length, out = new DataView(new ArrayBuffer(44 + n * 2 * ch));
  const w = (o, s) => { for (let i = 0; i < s.length; i++) out.setUint8(o + i, s.charCodeAt(i)); };
  w(0, "RIFF"); out.setUint32(4, 36 + n * 2 * ch, true); w(8, "WAVE"); w(12, "fmt "); out.setUint32(16, 16, true); out.setUint16(20, 1, true); out.setUint16(22, ch, true);
  out.setUint32(24, sr, true); out.setUint32(28, sr * 2 * ch, true); out.setUint16(32, 2 * ch, true); out.setUint16(34, 16, true); w(36, "data"); out.setUint32(40, n * 2 * ch, true);
  const data = []; for (let c = 0; c < ch; c++) data.push(buf.getChannelData(c));
  for (let i = 0; i < n; i++) for (let c = 0; c < ch; c++) out.setInt16(44 + (i * ch + c) * 2, Math.round(Math.max(-1, Math.min(1, data[c][i])) * 32767), true);
  return new Uint8Array(out.buffer);
}
return { render, wav };
})();
