// Render film.html to stills or to an MP4 with the local Chrome (headless) and ffmpeg.
// No dependencies: Node's built-in WebSocket speaks the DevTools protocol.
//   node render.mjs --stills 5,40,100            → out/stills/t005.0.png …
//   node render.mjs --video [--coda] [--jobs 4]   → out/the-game-of-winning[-coda].mp4
//   node render.mjs --soundtrack                  → soundtrack.mp3, which the player in film.html plays
// Each job runs its own Chrome and encodes one segment; the segments are joined without re-encoding.
import { spawn } from "node:child_process";
import { mkdirSync, writeFileSync, rmSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { tmpdir } from "node:os";

const here = dirname(fileURLToPath(import.meta.url));
const args = process.argv.slice(2);
const opt = (name) => { const i = args.indexOf(name); return i < 0 ? null : (args[i + 1] ?? ""); };
const has = (name) => args.includes(name);
const CHROME = process.env.CHROME || "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const outDir = join(here, "out");
mkdirSync(outDir, { recursive: true });

function launch(tag) {
  const profile = join(process.env.TMPDIR || tmpdir(), `gow-chrome-${process.pid}-${tag}`);
  const p = spawn(CHROME, ["--headless=new", "--disable-gpu", "--hide-scrollbars", "--mute-audio", "--no-first-run", "--no-default-browser-check",
    `--user-data-dir=${profile}`, "--remote-debugging-port=0", "--window-size=1920,1080", "about:blank"], { stdio: ["ignore", "ignore", "pipe"] });
  return new Promise((res, rej) => {
    let buf = "";
    p.stderr.on("data", d => { buf += d; const m = buf.match(/DevTools listening on (ws:\/\/\S+)/); if (m) res({ p, ws: m[1], profile }); });
    p.on("exit", c => rej(new Error("Chrome exited " + c + "\n" + buf)));
    setTimeout(() => rej(new Error("Chrome did not start\n" + buf)), 20000);
  });
}

function cdp(url) {
  const ws = new WebSocket(url); let id = 0; const pending = new Map();
  ws.onmessage = (ev) => { const m = JSON.parse(ev.data); if (m.id && pending.has(m.id)) { const { res, rej } = pending.get(m.id); pending.delete(m.id); m.error ? rej(new Error(JSON.stringify(m.error))) : res(m.result); } };
  const send = (method, params = {}, sessionId) => new Promise((res, rej) => { const i = ++id; pending.set(i, { res, rej }); ws.send(JSON.stringify({ id: i, method, params, sessionId })); });
  return new Promise(res => { ws.onopen = () => res({ send, close: () => ws.close() }); });
}

// One Chrome with the film loaded; returns helpers and a close function.
async function openFilm(tag) {
  const { p, ws, profile } = await launch(tag);
  const c = await cdp(ws);
  const { targetId } = await c.send("Target.createTarget", { url: "about:blank" });
  const { sessionId } = await c.send("Target.attachToTarget", { targetId, flatten: true });
  const S = (m, q) => c.send(m, q, sessionId);
  await S("Page.navigate", { url: pathToFileURL(join(here, "film.html")).href + "?render=1" });
  const evalv = async (expr, awaitPromise = false) => { const r = await S("Runtime.evaluate", { expression: expr, returnByValue: true, awaitPromise }); if (r.exceptionDetails) throw new Error(JSON.stringify(r.exceptionDetails)); return r.result.value; };
  for (let i = 0; i < 200; i++) { try { if (await evalv("!!window.FILM")) break; } catch {} await new Promise(r => setTimeout(r, 100)); }
  const frame = async (t) => Buffer.from((await evalv(`FILM.frame(${t})`)).split(",")[1], "base64");
  const close = () => { c.close(); p.kill(); try { rmSync(profile, { recursive: true, force: true }); } catch {} };
  return { evalv, frame, close };
}

const run = (argv) => new Promise((res, rej) => { const f = spawn("ffmpeg", argv, { stdio: ["ignore", "inherit", "inherit"] }); f.on("exit", c => c === 0 ? res() : rej(new Error("ffmpeg " + c))); });

async function segment(i0, i1, fps, file, tag, progress) {
  const film = await openFilm(tag);
  try {
    const ff = spawn("ffmpeg", ["-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", String(fps), "-c:v", "png", "-i", "-",
      "-c:v", "libx264", "-preset", "medium", "-crf", "17", "-pix_fmt", "yuv420p", "-r", String(fps), file], { stdio: ["pipe", "inherit", "inherit"] });
    for (let i = i0; i < i1; i++) {
      const png = await film.frame(i / fps);
      if (!ff.stdin.write(png)) await new Promise(r => ff.stdin.once("drain", r));
      progress();
    }
    ff.stdin.end();
    await new Promise((res, rej) => ff.on("exit", code => code === 0 ? res() : rej(new Error("ffmpeg " + code))));
  } finally { film.close(); }
}

if (opt("--stills") !== null) {
  const film = await openFilm("stills");
  try {
    const dir = join(outDir, "stills"); mkdirSync(dir, { recursive: true });
    for (const s of opt("--stills").split(",").map(Number)) { const f = join(dir, `t${s.toFixed(1).padStart(5, "0")}.png`); writeFileSync(f, await film.frame(s)); console.log(f); }
  } finally { film.close(); }
}

const LOUD = ["-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", "48000", "-c:a", "aac", "-b:a", "192k"];
async function soundtrackWav(file) {
  const film = await openFilm("audio");
  try {
    const len = await film.evalv("FILM.audio()", true), parts = [], CH = 1 << 20;
    for (let i = 0; i < len; i += CH) parts.push(Buffer.from(await film.evalv(`FILM.audioChunk(${i}, ${CH})`), "base64"));
    writeFileSync(file, Buffer.concat(parts));
  } finally { film.close(); }
}

if (has("--soundtrack")) {
  const wav = join(outDir, "soundtrack.wav");
  await soundtrackWav(wav);
  await run(["-y", "-loglevel", "error", "-i", wav, "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", "44100", "-c:a", "libmp3lame", "-b:a", "160k", join(here, "soundtrack.mp3")]);
  rmSync(wav);
  console.log(join(here, "soundtrack.mp3"));
}

if (has("--video")) {
  const coda = has("--coda"), fps = Number(opt("--fps") || 30), jobs = Number(opt("--jobs") || 4);
  const dur = coda ? 314 : 300, n = Math.round(dur * fps), name = coda ? "the-game-of-winning-coda" : "the-game-of-winning";
  const work = join(outDir, "work-" + name); mkdirSync(work, { recursive: true });
  const wav = join(work, "sound.wav");
  await soundtrackWav(wav);
  // frames, in parallel segments
  let done = 0; const t0 = Date.now();
  const tick = () => { done++; if (done % 600 === 0) console.log(`${done}/${n} frames  ${((Date.now() - t0) / 1000).toFixed(0)}s`); };
  const segs = [];
  for (let j = 0; j < jobs; j++) { const a = Math.floor(n * j / jobs), b = Math.floor(n * (j + 1) / jobs); segs.push({ a, b, file: join(work, `seg${j}.mp4`) }); }
  await Promise.all(segs.map((s, j) => segment(s.a, s.b, fps, s.file, "seg" + j, tick)));
  writeFileSync(join(work, "list.txt"), segs.map(s => `file '${s.file}'`).join("\n") + "\n");
  const mp4 = join(outDir, name + ".mp4");
  await run(["-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", join(work, "list.txt"), "-i", wav, "-t", String(dur),
    "-map", "0:v", "-map", "1:a", "-c:v", "copy", ...LOUD, "-movflags", "+faststart", mp4]);
  rmSync(work, { recursive: true, force: true });
  console.log(`${mp4}  (${((Date.now() - t0) / 1000).toFixed(0)}s)`);
}
