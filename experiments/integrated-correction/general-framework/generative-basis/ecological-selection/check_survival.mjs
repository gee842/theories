import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import assert from 'node:assert/strict';
import { fileURLToPath } from 'node:url';

// Independent arithmetic check of the empirical summary, not a mathematical
// theorem or an independent biological replication.
const here = path.dirname(fileURLToPath(import.meta.url));
let root = here;
while (!fs.existsSync(path.join(root, 'RESEARCH.md'))) root = path.dirname(root);
const source = path.join(root, 'sources/evolutionary-selection/ratcliff-2013');
const raw = fs.readFileSync(path.join(source, 'settling survival compiled data.csv'));
const hash = (data, alg = 'sha256') => crypto.createHash(alg).update(data).digest('hex');
const resultPath = path.join(here, 'survival-results.json');
const results = JSON.parse(fs.readFileSync(resultPath));
assert.equal(raw.length, 643);
assert.equal(hash(raw, 'md5'), '686faa3b6b625634c073bfc33095d4a0');
assert.equal(hash(raw), results.source_sha256);
assert.equal(hash(fs.readFileSync(path.join(here, 'analyze_survival.py'))), results.analysis_sha256);
const lines = raw.toString('utf8').trimEnd().split('\r\n');
assert.equal(lines.length, 31);
assert.equal(lines.shift(), 'Days of Evolution,Selection regime (old or new),Survival');
const groups = new Map();
for (const line of lines) {
  const [day, regime, text] = line.split(',');
  assert.match(text, /^0\.\d{1,9}$/);
  const units = BigInt(text.split('.')[1].padEnd(9, '0'));
  const key = `${day}/${regime}`;
  if (!groups.has(key)) groups.set(key, []);
  groups.get(key).push(units);
}
const sum = xs => xs.reduce((a, b) => a + b, 0n);
const abs = x => x < 0n ? -x : x;
const close = (a, b) => assert.ok(Math.abs(a - b) < 1e-12, `${a} != ${b}`);
for (const r of results.results) {
  const old = groups.get(`${r.isolate_day}/old`), fresh = groups.get(`${r.isolate_day}/new`);
  assert.equal(old.length, 5); assert.equal(fresh.length, 5);
  const so = sum(old), sn = sum(fresh);
  close(r.old_mean, Number(so) / 5e9);
  close(r.new_mean, Number(sn) / 5e9);
  close(r.mean_difference_new_minus_old, Number(sn - so) / 5e9);
  close(r.ratio_of_means_new_over_old, Number(sn) / Number(so));
  const all = [...old, ...fresh];
  let allocations = 0, extreme = 0;
  // Bit masks provide a separately implemented allocation enumeration.
  for (let mask = 0; mask < 1024; mask++) {
    const selected = all.filter((_, i) => mask & (1 << i));
    if (selected.length !== 5) continue;
    allocations++;
    if (abs(2n * sum(selected) - so - sn) >= abs(sn - so)) extreme++;
  }
  assert.equal(allocations, 252);
  assert.equal(extreme, r.permutation_sensitivity.at_least_as_extreme);
  close(extreme / allocations, r.permutation_sensitivity.two_sided_reference_probability);
  let pooledLoss = 0, conditionalLoss = 0;
  for (let i = 0; i < 5; i++) for (let j = 0; j < 5; j++) {
    const om = Number(so - old[i]) / 4e9, nm = Number(sn - fresh[j]) / 4e9;
    const ov = Number(old[i]) / 1e9, nv = Number(fresh[j]) / 1e9;
    pooledLoss += (ov - (om + nm) / 2) ** 2 + (nv - (om + nm) / 2) ** 2;
    conditionalLoss += (ov - om) ** 2 + (nv - nm) ** 2;
  }
  close(Math.sqrt(pooledLoss / 50), r.balanced_holdout.common_rate_rmse);
  close(Math.sqrt(conditionalLoss / 50), r.balanced_holdout.regime_conditional_rmse);
  assert.equal(r.balanced_holdout.unique_cultures, 10);
  for (const name of ['bootstrap_ratio_percentiles_2_5_97_5', 'bootstrap_difference_percentiles_2_5_97_5']) {
    assert.equal(r[name].length, 2);
    assert.ok(r[name].every(Number.isFinite) && r[name][0] <= r[name][1]);
  }
}
const receipt = {
  status: 'passed',
  checks: ['published byte size and MD5', 'input and analysis SHA256 bindings',
    '30 rows and six five-culture groups', 'exact integer means and contrasts',
    'independent 252-allocation enumeration', 'independent balanced holdout losses'],
  scope: 'Independent numerical implementation check, not an independent scientific review or Lean proof.',
  bootstrap_check: 'Finite ordered output only; bootstrap percentiles are not independently recomputed.',
  source_sha256: hash(raw), results_sha256: hash(fs.readFileSync(resultPath)),
  checker_sha256: hash(fs.readFileSync(fileURLToPath(import.meta.url))),
  node_version: process.version,
};
fs.writeFileSync(path.join(here, 'verification.json'), JSON.stringify(receipt, null, 2) + '\n');
console.log(JSON.stringify(receipt, null, 2));
