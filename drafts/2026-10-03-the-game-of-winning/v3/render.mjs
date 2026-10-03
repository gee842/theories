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

async function openFilm(tag, extra = "") {
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
  await S("Page.navigate", { url: `${origin}/index.html?render=1${extra ? "&" + extra : ""}` });
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
    const ff = spawn("ffmpeg", ["-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", String(fps), "-c:v", "png", "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "21", "-pix_fmt", "yuv420p", "-r", String(fps), file], { stdio: ["pipe", "inherit", "inherit"] });
    for (let i = i0; i < i1; i++) { const png = await film.frame(i / fps); if (!ff.stdin.write(png)) await new Promise(r => ff.stdin.once("drain", r)); tick(); }
    ff.stdin.end(); await new Promise((res, rej) => ff.on("exit", c => c === 0 ? res() : rej(new Error("ffmpeg " + c))));
  } finally { film.close(); }
}
try {
  if (args.includes("--audio")) {
    const film = await openFilm("audio"); const len = await film.evalv("FILM.audio()"); const parts = []; const CH = 1 << 20;
    for (let i = 0; i < len; i += CH) parts.push(Buffer.from(await film.evalv(`FILM.audioChunk(${i}, ${CH})`), "base64")); film.close();
    writeFileSync(join(outDir, "sound.wav"), Buffer.concat(parts)); console.log(join(outDir, "sound.wav"));
    // the player's soundtrack: static gain and a limiter (no loudness normalisation, which pumps)
    await run(["-y", "-loglevel", "error", "-i", join(outDir, "sound.wav"), "-af", "volume=15.5dB,alimiter=limit=0.85:level=disabled", "-ar", "44100", "-c:a", "libmp3lame", "-b:a", "160k", join(here, "soundtrack.mp3")]);
    console.log(join(here, "soundtrack.mp3"));
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
    const mp4 = join(outDir, "the-game-of-winning-v3.mp4");
    await run(["-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", join(work, "list.txt"), "-i", wav, "-t", String(dur), "-map", "0:v", "-map", "1:a", "-c:v", "copy",
      "-af", "volume=12.7dB,alimiter=limit=0.85:level=disabled", "-ar", "48000", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", mp4]);
    rmSync(work, { recursive: true, force: true }); console.log(`${mp4}  (${((Date.now() - t0) / 1000).toFixed(0)}s)`);
  }
  if (args.includes("--growth")) {   // compute the growth map once (index.html?regrow) and save it as growth.png
    const film = await openFilm("growth", "regrow"); const url = await film.evalv("Film.exportGrowth()"); film.close();
    writeFileSync(join(here, "growth.png"), Buffer.from(url.split(",")[1], "base64")); console.log(join(here, "growth.png"));
  }
  if (opt("--sheet") !== null) {   // --sheet from,to,step[,cols]  → out/sheet.png, one image for a fast look at a stretch of the film
    // or --sheet @t1:t2:t3…[,cols] for chosen moments; --out NAME writes out/NAME.png
    const spec = opt("--sheet"), list = spec.startsWith("@"); const parts = spec.replace("@", "").split(",");
    const ts = [], cols = +(list ? parts[1] : parts[3]) || 4; const film = await openFilm("sheet"); const dir = join(outDir, "sheet"); mkdirSync(dir, { recursive: true });
    if (list) ts.push(...parts[0].split(":").map(Number)); else { const [a, b, st] = parts.map(Number); for (let x = a; x <= b + 1e-6; x += st) ts.push(+x.toFixed(2)); }
    // --story: the times are story seconds (the screenplay's clock), mapped to film seconds through the time map
    if (args.includes("--story")) for (let i = 0; i < ts.length; i++) ts[i] = +(await film.evalv(`Film.filmT(${ts[i]})`)).toFixed(3);
    try { for (const [i, x] of ts.entries()) writeFileSync(join(dir, `f${String(i).padStart(3, "0")}.png`), await film.frame(x)); } finally { film.close(); }
    await run(["-y", "-loglevel", "error", "-start_number", "0", "-i", join(dir, "f%03d.png"), "-frames:v", "1", "-vf", `scale=640:-1,tile=${cols}x${Math.ceil(ts.length / cols)}:padding=4:color=0x222222`, join(outDir, (opt("--out") || "sheet") + ".png")]);
    for (const [i] of ts.entries()) rmSync(join(dir, `f${String(i).padStart(3, "0")}.png`));
    console.log(join(outDir, (opt("--out") || "sheet") + ".png"), ts.join(" "));
  }
  if (opt("--perf") !== null) {   // --perf a,b,step: GPU time per frame (ms, story seconds) — the live player needs < 16
    const [a, b, st] = opt("--perf").split(",").map(Number); const film = await openFilm("perf"); if (opt("--js")) console.log("js →", await film.evalv(opt("--js")));
    try { for (let x = a; x <= b + 1e-6; x += st) { const ft = await film.evalv(`Film.filmT(${x})`); await film.evalv(`Film.timeFrame(${ft})`); let ms = 0; for (let k = 0; k < 3; k++) ms += await film.evalv(`Film.timeFrame(${ft})`); console.log(`story ${x.toFixed(1)}  ${(ms / 3).toFixed(1)} ms  ${await film.evalv(`Film.sceneAt(${ft})`)}`); } } finally { film.close(); }
  }
  if (opt("--stills") !== null) {
    const film = await openFilm("stills"); if (opt("--js")) console.log("js →", await film.evalv(opt("--js")));
    try {
      const dir = join(outDir, "stills"); mkdirSync(dir, { recursive: true });
      for (const s of opt("--stills").split(",").map(Number)) { const t0 = Date.now(); const f = join(dir, `t${s.toFixed(1).padStart(5, "0")}.png`); writeFileSync(f, await film.frame(s)); console.log(f, `${Date.now() - t0}ms`); }
    } finally { film.close(); }
  }
} finally { server.close(); }
