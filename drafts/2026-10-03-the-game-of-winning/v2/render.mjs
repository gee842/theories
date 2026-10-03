// Render v2 (index.html) to stills or video with headless Chrome on the GPU. A small static server
// serves this folder so WebGL can read the maps. No dependencies.
//   node render.mjs --stills 30,54,66        → out/stills/t030.0.png …
import { spawn } from "node:child_process";
import { createServer } from "node:http";
import { mkdirSync, writeFileSync, readFileSync, existsSync, rmSync } from "node:fs";
import { dirname, join, extname } from "node:path";
import { fileURLToPath } from "node:url";
import { tmpdir } from "node:os";

const here = dirname(fileURLToPath(import.meta.url));
const args = process.argv.slice(2);
const opt = (name) => { const i = args.indexOf(name); return i < 0 ? null : (args[i + 1] ?? ""); };
const CHROME = process.env.CHROME || "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const outDir = join(here, "out"); mkdirSync(outDir, { recursive: true });
const TYPES = { ".html": "text/html; charset=utf-8", ".js": "text/javascript", ".jpg": "image/jpeg", ".png": "image/png", ".mp3": "audio/mpeg" };

const server = createServer((req, res) => {
  const f = join(here, decodeURIComponent(req.url.split("?")[0]));
  if (!f.startsWith(here) || !existsSync(f)) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { "content-type": TYPES[extname(f)] || "application/octet-stream" }); res.end(readFileSync(f));
});
await new Promise(r => server.listen(0, "127.0.0.1", r));
const origin = `http://127.0.0.1:${server.address().port}`;

async function openFilm(tag) {
  const profile = join(process.env.TMPDIR || tmpdir(), `gow2-${process.pid}-${tag}`);
  const p = spawn(CHROME, ["--headless=new", "--use-angle=metal", "--enable-gpu-rasterization", "--ignore-gpu-blocklist", "--hide-scrollbars", "--mute-audio", "--no-first-run",
    `--user-data-dir=${profile}`, "--remote-debugging-port=0", "--window-size=1920,1080", "about:blank"], { stdio: ["ignore", "ignore", "pipe"] });
  const ws = await new Promise((res, rej) => { let b = ""; p.stderr.on("data", d => { b += d; const m = b.match(/DevTools listening on (ws:\S+)/); if (m) res(m[1]); }); setTimeout(() => rej(new Error("Chrome did not start\n" + b)), 20000); });
  const sock = new WebSocket(ws); let id = 0; const pend = new Map();
  sock.onmessage = e => { const m = JSON.parse(e.data); if (m.id && pend.has(m.id)) { const { res, rej } = pend.get(m.id); pend.delete(m.id); m.error ? rej(new Error(JSON.stringify(m.error))) : res(m.result); } };
  await new Promise(r => sock.onopen = r);
  const send = (method, params = {}, sessionId) => new Promise((res, rej) => { const i = ++id; pend.set(i, { res, rej }); sock.send(JSON.stringify({ id: i, method, params, sessionId })); });
  const { targetId } = await send("Target.createTarget", { url: "about:blank" });
  const { sessionId } = await send("Target.attachToTarget", { targetId, flatten: true });
  const S = (m, q) => send(m, q, sessionId);
  await S("Runtime.enable");
  await S("Page.navigate", { url: `${origin}/index.html?render=1` });
  const evalv = async (expr) => { const r = await S("Runtime.evaluate", { expression: expr, returnByValue: true, awaitPromise: true }); if (r.exceptionDetails) throw new Error(JSON.stringify(r.exceptionDetails.exception?.description || r.exceptionDetails)); return r.result.value; };
  for (let i = 0; i < 600; i++) {
    let st = null; try { st = await evalv("window.FILM && ({ ready: FILM.ready, error: FILM.error })"); } catch {}
    if (st?.error) throw new Error(st.error); if (st?.ready) break; await new Promise(r => setTimeout(r, 100));
  }
  const frame = async (t) => Buffer.from((await evalv(`FILM.frame(${t})`)).split(",")[1], "base64");
  const close = () => { sock.close(); p.kill(); try { rmSync(profile, { recursive: true, force: true }); } catch {} };
  return { evalv, frame, close };
}

const run = (argv) => new Promise((res, rej) => { const f = spawn("ffmpeg", argv, { stdio: ["ignore", "inherit", "inherit"] }); f.on("exit", c => c === 0 ? res() : rej(new Error("ffmpeg " + c))); });
async function segment(i0, i1, fps, file, tag, tick) {
  const film = await openFilm(tag);
  try {
    const ff = spawn("ffmpeg", ["-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", String(fps), "-c:v", "png", "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "16", "-pix_fmt", "yuv420p", "-r", String(fps), file], { stdio: ["pipe", "inherit", "inherit"] });
    for (let i = i0; i < i1; i++) { const png = await film.frame(i / fps); if (!ff.stdin.write(png)) await new Promise(r => ff.stdin.once("drain", r)); tick(); }
    ff.stdin.end(); await new Promise((res, rej) => ff.on("exit", c => c === 0 ? res() : rej(new Error("ffmpeg " + c))));
  } finally { film.close(); }
}
try {
  if (args.includes("--audio")) {
    const film = await openFilm("audio"); const len = await film.evalv("FILM.audio()"); const parts = []; const CH = 1 << 20;
    for (let i = 0; i < len; i += CH) parts.push(Buffer.from(await film.evalv(`FILM.audioChunk(${i}, ${CH})`), "base64")); film.close();
    writeFileSync(join(outDir, "sound.wav"), Buffer.concat(parts)); console.log(join(outDir, "sound.wav"));
  }
  if (args.includes("--video")) {
    const fps = Number(opt("--fps") || 30), jobs = Number(opt("--jobs") || 5), dur = Number(opt("--dur") || 300), n = Math.round(dur * fps);
    const work = join(outDir, "work"); mkdirSync(work, { recursive: true });
    const film = await openFilm("audio"); const len = await film.evalv("FILM.audio()"); const parts = []; const CH = 1 << 20;
    for (let i = 0; i < len; i += CH) parts.push(Buffer.from(await film.evalv(`FILM.audioChunk(${i}, ${CH})`), "base64")); film.close();
    const wav = join(work, "sound.wav"); writeFileSync(wav, Buffer.concat(parts));
    let done = 0; const t0 = Date.now(); const tick = () => { if (++done % 600 === 0) console.log(`${done}/${n} frames  ${((Date.now() - t0) / 1000).toFixed(0)}s`); };
    const segs = []; for (let j = 0; j < jobs; j++) segs.push({ a: Math.floor(n * j / jobs), b: Math.floor(n * (j + 1) / jobs), file: join(work, `seg${j}.mp4`) });
    await Promise.all(segs.map((s, j) => segment(s.a, s.b, fps, s.file, "seg" + j, tick)));
    writeFileSync(join(work, "list.txt"), segs.map(s => `file '${s.file}'`).join("\n") + "\n");
    const mp4 = join(outDir, "the-game-of-winning-v2.mp4");
    await run(["-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", join(work, "list.txt"), "-i", wav, "-t", String(dur), "-map", "0:v", "-map", "1:a", "-c:v", "copy",
      "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", "48000", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", mp4]);
    rmSync(work, { recursive: true, force: true }); console.log(`${mp4}  (${((Date.now() - t0) / 1000).toFixed(0)}s)`);
  }
  if (opt("--stills") !== null) {
    const film = await openFilm("stills");
    try {
      const dir = join(outDir, "stills"); mkdirSync(dir, { recursive: true });
      for (const s of opt("--stills").split(",").map(Number)) { const t0 = Date.now(); const f = join(dir, `t${s.toFixed(1).padStart(5, "0")}.png`); writeFileSync(f, await film.frame(s)); console.log(f, `${Date.now() - t0}ms`); }
    } finally { film.close(); }
  }
} finally { server.close(); }
