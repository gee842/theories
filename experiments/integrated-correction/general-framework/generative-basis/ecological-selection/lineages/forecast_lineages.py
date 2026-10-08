"""Chronological recorded-viability forecasts; see FORECAST-PROTOCOL.md.

AI-authored implementation, not an execution of colgen. Its beta transition
family is credited to the preserved colgen source. No future observations,
endpoint coalescence or inferred genotypes enter inference.
"""
import argparse
from collections import defaultdict
import csv
import hashlib
import json
from pathlib import Path
import sys

import numpy as np
import scipy
from scipy.special import betainc, betaincc, logsumexp

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p/'RESEARCH.md').exists())
SIGMAS = (1, 2, 5, 10, 25, 50, 100, 250, 500, 1500)
MODELS = ('constant_stage', 'changing_stage', 'inherited_lineage')


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load():
    with (HERE/'genealogy-reading.csv').open() as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r['time'] = int(r['node'].split(':')[0])
        r['phase'] = int(r['phase'])
        r['cycle'] = int(r['cycle'])
        r['alive'] = 1-int(r['extinct'])
    return rows


def kernel(grid, sigmas=SIGMAS):
    """Parent-by-child bin mass, preserving small upper-tail differences."""
    x = (np.arange(grid)+0.5)/grid
    edge = np.arange(grid+1)/grid
    s = np.asarray(sigmas)[:, None, None]
    a = 1+s*x[None, :, None]
    b = 1+s*(1-x[None, :, None])
    cdf = betainc(a, b, edge[None, None, :])
    sf = betaincc(a, b, edge[None, None, :])
    k = np.where(cdf[:, :, :-1] < 0.5, np.diff(cdf, axis=2), -np.diff(sf, axis=2))
    assert np.min(k) >= -1e-14
    k = np.maximum(k, 0)
    assert np.max(np.abs(k.sum(axis=2)-1)) < 1e-12
    k /= k.sum(axis=2, keepdims=True)
    return x, k


def forest_inference(parents, log_emission, log_k):
    """Numerical sum-product over a parent-before-child forest.

    Return each sigma's data log likelihood and node posterior marginals.
    Every root receives a uniform probability-state prior. log_emission is
    node-by-state; a synthetic founder has zero log emission everywhere.
    """
    n, grid = log_emission.shape
    ns = log_k.shape[0]
    sub = np.broadcast_to(log_emission, (ns, n, grid)).copy()
    messages = np.zeros_like(sub)
    for i in range(n-1, -1, -1):
        p = parents[i]
        if p >= 0:
            assert p < i
            messages[:, i] = logsumexp(log_k+sub[:, i, None, :], axis=2)
            sub[:, p] += messages[:, i]
    outside = np.zeros_like(sub)
    evidence = np.zeros(ns)
    posterior = np.zeros_like(sub)
    for i, p in enumerate(parents):
        if p < 0:
            outside[:, i] = -np.log(grid)
            evidence += logsumexp(outside[:, i]+sub[:, i], axis=1)
        else:
            cavity = outside[:, p]+sub[:, p]-messages[:, i]
            outside[:, i] = logsumexp(cavity[:, :, None]+log_k, axis=1)
            outside[:, i] -= logsumexp(outside[:, i], axis=1)[:, None]
        q = outside[:, i]+sub[:, i]
        posterior[:, i] = np.exp(q-logsumexp(q, axis=1)[:, None])
    return evidence, posterior


def normalize_weights(evidence):
    # Equal sigma prior: its constant cancels in normalization.
    return np.exp(evidence-logsumexp(evidence))


def incoming(tube, time, prefix):
    """Assignments are read only from already completed phases."""
    prev = prefix.get(f'{time-1}:{tube}')
    if prev is None:
        return ''
    donor = prev['replaced']
    if donor in ('0', '', 'na'):
        donor = tube
    node = f'{time-1}:{donor}'
    return node if node in prefix else ''


def phase_parent(node, prefix):
    parent = prefix[node]['parent']
    if parent in prefix:
        return prefix[parent]['parent']
    return ''


def forecast_batch(prefix_rows, time, tubes, x, k):
    """This function receives NO current/future rows or current outcomes."""
    assert all(r['time'] < time for r in prefix_rows)
    phase = 1 if time % 2 else 2
    prefix = {r['node']: r for r in prefix_rows}
    history = sorted((r for r in prefix_rows if r['phase']==phase), key=lambda r:(r['time'], r['tube']))
    with np.errstate(divide='ignore'):
        log_k = np.log(k)
    grid = len(x)
    emissions = [np.zeros(grid)]  # shared unobserved initial founder
    parents = [-1]
    names = {'FOUNDER': 0}
    for r in history:
        pp = phase_parent(r['node'], prefix)
        p = names.get(pp, -1)
        if r['time']==phase:
            p = 0
        parents.append(p)
        names[r['node']] = len(emissions)
        emissions.append(np.log(x if r['alive'] else 1-x))
    evidence, marginals = forest_inference(parents, np.asarray(emissions), log_k)
    weights = normalize_weights(evidence)
    transition_mean = k@x
    constant = (1+sum(r['alive'] for r in history))/(2+len(history))

    # Conventional alternative: one changing latent stage propensity per batch.
    stage_logq = np.full((len(SIGMAS), grid), -np.log(grid))
    stage_evidence = np.zeros(len(SIGMAS))
    times = sorted({r['time'] for r in history})
    for j, t in enumerate(times):
        if j:
            stage_logq = logsumexp(stage_logq[:, :, None]+log_k, axis=1)
        batch = [r for r in history if r['time']==t]
        y = sum(r['alive'] for r in batch)
        stage_logq += y*np.log(x)+(len(batch)-y)*np.log1p(-x)
        z = logsumexp(stage_logq, axis=1)
        stage_evidence += z
        stage_logq -= z[:, None]
    stage_weights = normalize_weights(stage_evidence)
    if times:
        stage_by_sigma = (np.exp(stage_logq)*transition_mean).sum(axis=1)
    else:
        stage_by_sigma = np.full(len(SIGMAS), 0.5)
    changing = float(stage_weights@stage_by_sigma)
    result=[]
    for tube in tubes:
        parent = incoming(tube, time, prefix)
        pp = prefix[parent]['parent'] if parent else ''
        if time==phase:
            pp = 'FOUNDER'
        if pp in names:
            by_sigma = (marginals[:, names[pp]]*transition_mean).sum(axis=1)
        else:
            by_sigma = np.full(len(SIGMAS), 0.5)
        result.append(dict(node=f'{time}:{tube}', parent=parent, same_phase_parent=pp,
                           time=time, cycle=(time+1)//2, phase=phase, tube=tube,
                           constant_stage=constant, changing_stage=changing,
                           inherited_lineage=float(weights@by_sigma),
                           training_nodes=len(history), latest_training_time=max(times, default=0)))
    diagnostic=dict(time=time, phase=phase, training_nodes=len(history),
                    lineage_sigma_weights=weights.tolist(), stage_sigma_weights=stage_weights.tolist(),
                    lineage_log_evidence=evidence.tolist(), stage_log_evidence=stage_evidence.tolist())
    return result, diagnostic


def run_forecasts(rows, grid):
    x,k = kernel(grid)
    out, diagnostics = [], []
    for sheet in dict.fromkeys(r['sheet'] for r in rows):
        rr = [r for r in rows if r['sheet']==sheet]
        index = {r['node']:r for r in rr}
        tubes = sorted({r['tube'] for r in rr})
        assert len(tubes)==48
        for t in range(1,21):
            predictions, diag = forecast_batch([r for r in rr if r['time']<t], t, tubes, x, k)
            diagnostics.append(dict(sheet=sheet, **diag))
            for f in predictions:
                actual = index.get(f['node'])
                f.update(sheet=sheet, alive=actual['alive'] if actual else '',
                         condition=actual['condition'] if actual else 'MISS',
                         source_row=actual['source_row'] if actual else '')
                out.append(f)
        print(f'grid={grid}: {sheet} complete', flush=True)
    return out, diagnostics


def score(rows):
    scores=[]
    for sheet in dict.fromkeys(r['sheet'] for r in rows):
        for first in (2,6):
            for clean in (False,True):
                for phase in (0,1,2):
                    rr=[r for r in rows if r['sheet']==sheet and r['cycle']>=first
                        and r['alive']!='' and (not clean or r['condition']=='0')
                        and (not phase or r['phase']==phase)]
                    for m in MODELS:
                        p=np.array([r[m] for r in rr]); y=np.array([r['alive'] for r in rr])
                        assert np.all((p>0)&(p<1))
                        scores.append(dict(sheet=sheet, first_cycle=first, condition_zero_only=clean,
                                           phase=phase, model=m, n=len(rr),
                                           brier=float(np.mean((p-y)**2)),
                                           log_loss=float(np.mean(-y*np.log(p)-(1-y)*np.log1p(-p)))))
    return scores


def donor_counts(rows, raw):
    out=[]
    by_batch=defaultdict(list)
    for r in rows:by_batch[r['sheet'],r['time']].append(r)
    for (sheet,time), rr in by_batch.items():
        if time<2:continue
        prev=[r for r in raw if r['sheet']==sheet and r['time']==time-1]
        for p in prev:
            children=[r for r in rr if r['parent']==p['node']]
            complete=all(r['alive']!='' for r in children)
            entry=dict(sheet=sheet,time=time,donor=p['node'],assigned=len(children),
                       complete_outcomes=complete,observed_alive=sum(r['alive'] for r in children) if complete else '')
            entry.update({m:sum(r[m] for r in children) for m in MODELS})
            out.append(entry)
    return out


def dump_csv(path, rows):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--grid',type=int,default=100);args=ap.parse_args()
    rows=load(); forecasts, diagnostics=run_forecasts(rows,args.grid)
    donors=donor_counts(forecasts,rows)
    name=f'forecast-{args.grid}'
    dump_csv(HERE/f'{name}.csv',forecasts)
    dump_csv(HERE/f'{name}-donors.csv',donors)
    summary=dict(grid=args.grid,sigmas=SIGMAS,forecast_slots=len(forecasts),
                 observed=sum(r['alive']!='' for r in forecasts),scores=score(forecasts),
                 batches=diagnostics,donor_scores=[],
                 bindings={p.name:sha(p) for p in (HERE/'forecast_lineages.py',HERE/'FORECAST-PROTOCOL.md',HERE/'genealogy-reading.csv',HERE/f'{name}.csv',HERE/f'{name}-donors.csv')},
                 runtime=dict(python=sys.version,numpy=np.__version__,scipy=scipy.__version__))
    for sheet in dict.fromkeys(r['sheet'] for r in donors):
        rr=[r for r in donors if r['sheet']==sheet and r['time']>=3 and r['assigned']>0 and r['complete_outcomes']]
        for m in MODELS:
            e=np.array([r[m]-r['observed_alive'] for r in rr])
            summary['donor_scores'].append(dict(sheet=sheet,model=m,n=len(rr),mae=float(np.mean(abs(e))),rmse=float(np.sqrt(np.mean(e**2)))))
    (HERE/f'{name}-results.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps([s for s in summary['scores'] if s['first_cycle']==2 and not s['condition_zero_only'] and s['phase']==0],indent=2))


if __name__=='__main__':main()
