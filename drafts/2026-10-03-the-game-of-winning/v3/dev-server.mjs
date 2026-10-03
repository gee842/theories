// Live development server for the film: serves this folder without caching and tells open pages to reload
// (resuming at the same second) whenever a file here changes.   node dev-server.mjs [port]
import { createServer } from "node:http";
import { readFileSync, existsSync, statSync, watch } from "node:fs";
import { dirname, join, extname, normalize } from "node:path";
import { fileURLToPath } from "node:url";
const here = dirname(fileURLToPath(import.meta.url)), port = Number(process.argv[2] || process.env.PORT || 5173);
const TYPES = { ".html": "text/html; charset=utf-8", ".js": "text/javascript", ".mjs": "text/javascript", ".jpg": "image/jpeg", ".png": "image/png", ".mp3": "audio/mpeg", ".json": "application/json" };
const clients = new Set();
createServer((req, res) => {
  const url = decodeURIComponent(req.url.split("?")[0]);
  if (url === "/__events") { res.writeHead(200, { "content-type": "text/event-stream", "cache-control": "no-cache", connection: "keep-alive" }); res.write("retry: 500\n\n"); clients.add(res); req.on("close", () => clients.delete(res)); return; }
  const f = normalize(join(here, url === "/" ? "index.html" : url));
  if (!f.startsWith(here) || !existsSync(f) || statSync(f).isDirectory()) { res.writeHead(404); return res.end("not found"); }
  res.writeHead(200, { "content-type": TYPES[extname(f)] || "application/octet-stream", "cache-control": "no-store" }); res.end(readFileSync(f));
}).listen(port, "127.0.0.1", () => console.log(`film dev server: http://127.0.0.1:${port}/  (live reload on)`));
let timer = null;
watch(here, { recursive: true }, (ev, name) => {
  if (!name || name.startsWith("out") || name.startsWith("assets") || name.endsWith(".mp3")) return;
  clearTimeout(timer); timer = setTimeout(() => { console.log("changed:", name); for (const c of clients) c.write(`data: ${name}\n\n`); }, 120);
});
