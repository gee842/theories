import { readFile, writeFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import { fileURLToPath } from 'node:url';

const source = new URL('../production/physics/climb-prototype/nominal-trace.json', import.meta.url);
const destination = new URL('../public/assets/climb-trace.json', import.meta.url);
const bytes = await readFile(source);
const trace = JSON.parse(bytes);
const lastTime = trace.frames.at(-1).time;
const phases = [];
for (let cycle = 1; cycle <= 12; cycle++) {
  const original = trace.phases.filter(phase => phase.description === `Actual MuJoCo state; cycle ${cycle}`);
  if (!original.length || original.at(-1).label !== 'raise') throw new Error(`Incomplete source cycle ${cycle}`);
  phases.push({
    id: `stroke-${cycle}`, label: `${String(cycle).padStart(2, '0')} · ${(cycle * .3).toFixed(1)} m`,
    start: original[0].start, end: original.at(-1).end,
    description: `Stroke ${cycle}/12: sequentially advance and recapture all four grips, then raise the chassis 0.30 m. Target cumulative ascent ${(cycle * .3).toFixed(1)} m.`,
  });
}
const hold = trace.phases.at(-1);
if (hold.label !== 'final-hold') throw new Error('Expected final hold');
phases.push({ id: 'final-hold', label: 'Final hold', start: hold.start, end: lastTime, description: 'All four grips locked after the full-storey ascent. No construction load or building connection is simulated.' });
const output = {
  ...trace,
  phases,
  sourcePhases: trace.phases,
  presentationExport: {
    script: 'scripts/exportClimbTrace.mjs',
    source: 'production/physics/climb-prototype/nominal-trace.json',
    sourceSha256: createHash('sha256').update(bytes).digest('hex'),
    description: 'Only phase navigation is grouped. All source frames, poses, metrics, events, bindings and provenance are retained without resampling. Final phase ends at the final recorded frame.',
    sourceFrameCount: trace.frames.length,
  },
};
await writeFile(destination, `${JSON.stringify(output)}\n`);
const reread = JSON.parse(await readFile(destination, 'utf8'));
for (const key of ['frames', 'events', 'bindings', 'provenance']) {
  if (JSON.stringify(reread[key]) !== JSON.stringify(trace[key])) throw new Error(`Source ${key} changed`);
}
console.log(`${fileURLToPath(destination)}: ${trace.frames.length} unchanged frames, ${phases.length} navigation phases, ${lastTime.toFixed(3)} s`);
