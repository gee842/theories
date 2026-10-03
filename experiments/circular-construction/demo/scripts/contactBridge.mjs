#!/usr/bin/env node
/** Headless fixed-pose bridge runner; --write-fixtures records request/result JSON. */
import { build } from 'esbuild';
import { spawnSync } from 'node:child_process';
import { existsSync, mkdirSync, writeFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const bundled = await build({ entryPoints: [join(root, 'scripts/contactBridgeCases.ts')], bundle: true,
  platform: 'node', format: 'esm', write: false, logLevel: 'silent' });
const { contactBridgeCases, assessContactResult } = await import(`data:text/javascript;base64,${Buffer.from(bundled.outputFiles[0].contents).toString('base64')}`);
const cases = await contactBridgeCases();
const python = process.env.CONTACT_PYTHON || (existsSync(join(root, 'numerical/.venv/bin/python'))
  ? join(root, 'numerical/.venv/bin/python') : 'python3');
const output = [];
for (const item of cases) {
  const invocation = spawnSync(python, [join(root, 'numerical/contact_solver.py')], {
    input: `${JSON.stringify(item.request)}\n`, encoding: 'utf8', timeout: 30_000, maxBuffer: 4 * 1024 * 1024,
  });
  let result = null;
  try { result = JSON.parse(invocation.stdout || 'null'); } catch { /* invalid JSON stays unverified */ }
  // The same request is current in this deterministic fixture run. A live caller
  // must rebuild it from its latest RobotState and WorldState before assessment.
  const assessment = await assessContactResult(item.request, result, item.request);
  const entry = { name: item.name, expected: item.expected, expectedAssessment: item.expectedAssessment, request: item.request, result, assessment,
    processExitCode: invocation.status, processError: invocation.error?.message ?? null };
  output.push(entry);
  if (process.argv.includes('--write-fixtures') && invocation.status === 0 && result?.status === item.expected) {
    const directory = join(root, 'numerical/fixtures');
    mkdirSync(directory, { recursive: true });
    writeFileSync(join(directory, `${item.name}.request.json`), `${JSON.stringify(item.request, null, 2)}\n`);
    writeFileSync(join(directory, `${item.name}.result.json`), `${JSON.stringify(result, null, 2)}\n`);
  }
}
console.log(JSON.stringify(output, null, 2));
if (output.some(item => item.processExitCode !== 0 || item.processError))
  process.exitCode = 1;
if (output.some(item => item.assessment.stale ||
  item.result?.solver?.status !== 'unavailable' && item.assessment.status !==
    (item.expectedAssessment ?? (item.expected === 'failed' ? 'fail' : item.expected === 'passed' ? 'pass' : 'unverified'))))
  process.exitCode = 1;
if (output.some(item => item.processExitCode === 0 && item.result?.solver?.status !== 'unavailable' &&
  item.result?.status !== item.expected))
  process.exitCode = 1;
if (process.argv.includes('--write-fixtures') && output.some(item =>
  item.result?.status !== item.expected))
  process.exitCode = 1;
