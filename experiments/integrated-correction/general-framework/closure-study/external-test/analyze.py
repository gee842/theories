"""Fixed exploratory secondary analysis; see PROTOCOL.md before interpretation."""
from pathlib import Path
from collections import defaultdict, Counter
import csv
import hashlib
import json
import platform
import numpy as np

ROOT = Path(__file__).resolve().parent
SEED = 20261005


def read(name):
    with (ROOT / 'data' / name).open() as handle:
        return list(csv.DictReader(handle))


def key(row, biomass=False):
    return (row['cond'] if biomass else row['inoc'],
            int(row['salt'].replace('%', '')),
            15 if row['temp'] == '15C' else 20,
            int(row['day'][1:]))


def finite_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return np.nan


def mean_if_complete(values, n):
    assert len(values) == n, (len(values), n)
    return float(np.mean(values)) if np.isfinite(values).all() else np.nan


def prepare():
    od = read('all_od_data.csv')
    blanks = defaultdict(list)
    for row in od:
        if row['cond'] == 'blank':
            blanks[(row['day'], row['temp'], row['salt'])].append(float(row['od']))
    od_groups = defaultdict(list)
    for row in od:
        if row['cond'] != 'blank':
            blank = mean_if_complete(blanks[(row['day'], row['temp'], row['salt'])], 20)
            od_groups[key(row, True)].append(finite_float(row['od']) - blank)
    means = {k: mean_if_complete(v, 3) for k, v in od_groups.items()}
    summaries = {}
    for filename, field, metric in [('mcn_df_norare.csv', 'mcn', None),
                                     ('diversity_df_norare.csv', 'div_value', 'Shannon')]:
        groups = defaultdict(list)
        for row in read(filename):
            if row['day'] not in ['D1', 'D3', 'D5']:
                continue
            if metric is not None and row['diversity_metric'] != metric:
                continue
            groups[key(row)].append(finite_float(row[field]))
        summaries['mcn' if metric is None else 'shannon'] = {
            k: mean_if_complete(v, 3) for k, v in groups.items()}
    rows, excluded = [], []
    for k in sorted(means):
        source, salt, temp, cycle = k
        if cycle not in [1, 3, 5]:
            continue
        row = dict(source=source, salt=salt, temp=temp, cycle=cycle,
                   current_od=means[k], next_od=means.get((source, salt, temp, cycle+1), np.nan),
                   mcn=summaries['mcn'].get(k, np.nan), shannon=summaries['shannon'].get(k, np.nan))
        if all(np.isfinite(row[c]) for c in ['current_od', 'next_od', 'mcn', 'shannon']):
            rows.append(row)
        else:
            excluded.append(row)
    group_counts = Counter((r['source'], r['salt'], r['temp']) for r in rows)
    complete = {k for k, count in group_counts.items() if count == 3}
    assert len(complete) >= 18, 'Insufficient complete trajectories per frozen protocol'
    assert len(complete) == len(group_counts), 'Incomplete trajectories require transparent protocol repair'
    return rows, dict(n_rows=len(rows), n_conditions=len(group_counts),
                      n_sources=len(set(r['source'] for r in rows)),
                      biological_replicates_per_condition=3, excluded_rows=excluded,
                      finite_summary_rows={name: len(v) for name, v in summaries.items()})


def features(rows):
    sources = sorted({r['source'] for r in rows})
    vals = []
    for r in rows:
        salt, temp, cycle = r['salt'], r['temp'], r['cycle']
        v = [r['current_od'], salt, salt**2, temp, cycle, cycle**2, salt*temp]
        for source in sources:
            indicator = float(r['source'] == source)
            v += [indicator, indicator*salt, indicator*temp]
        vals.append(v)
    return np.array(vals, dtype=float), np.array([[r['mcn'], r['shannon']] for r in rows])


def ridge_predict(X, y, train, test, alpha):
    mu = X[train].mean(axis=0)
    sd = X[train].std(axis=0)
    active = sd > 1e-12
    Z = (X[train][:, active] - mu[active]) / sd[active]
    T = (X[test][:, active] - mu[active]) / sd[active]
    ym = y[train].mean()
    beta = np.linalg.solve(Z.T @ Z + alpha*np.eye(Z.shape[1]), Z.T @ (y[train]-ym))
    return ym + T @ beta


def cv(X, y, groups, alpha):
    result = np.full(len(y), np.nan)
    for group in sorted(set(groups)):
        test = np.array([g == group for g in groups])
        train = ~test
        assert not set(np.array(groups)[train]) & set(np.array(groups)[test])
        result[test] = ridge_predict(X, y, train, test, alpha)
    assert np.isfinite(result).all()
    return result


def scores(y, pred):
    return dict(rmse=float(np.sqrt(np.mean((y-pred)**2))), mae=float(np.mean(np.abs(y-pred))))


def main():
    rows, audit = prepare()
    base, extra = features(rows)
    y = np.array([r['next_od'] for r in rows])
    sources = [r['source'] for r in rows]
    condition = [f"{r['source']}:{r['salt']}:{r['temp']}" for r in rows]
    models = dict(baseline=base, augmented=np.column_stack([base, extra]),
                  mcn_only=np.column_stack([base, extra[:, 0]]),
                  shannon_only=np.column_stack([base, extra[:, 1]]))
    all_results, predictions = {}, {}
    for split_name, groups in [('condition', condition), ('source', sources)]:
        all_results[split_name] = {}
        for alpha in [1, 10]:
            result, preds = {}, {}
            for name, X in models.items():
                pred = cv(X, y, groups, alpha)
                preds[name] = pred
                result[name] = scores(y, pred)
                for source in sorted(set(sources)):
                    ix = np.array([s == source for s in sources])
                    result[name].setdefault('by_source', {})[source] = scores(y[ix], pred[ix])
            result['persistence'] = scores(y, np.array([r['current_od'] for r in rows]))
            rng = np.random.default_rng(SEED)
            source_array = np.array(sorted(set(sources)))
            gains = []
            for _ in range(2000):
                blocks = rng.choice(source_array, len(source_array), replace=True)
                ix = np.concatenate([np.flatnonzero(np.array(sources) == s) for s in blocks])
                gains.append(scores(y[ix], preds['baseline'][ix])['rmse'] -
                             scores(y[ix], preds['augmented'][ix])['rmse'])
            result['source_block_bootstrap_rmse_gain_95pct'] = [float(v) for v in np.quantile(gains, [.025, .975])]
            result['n_conditions_improved_mse'] = sum(
                np.mean((y[np.array(condition)==g]-preds['augmented'][np.array(condition)==g])**2) <
                np.mean((y[np.array(condition)==g]-preds['baseline'][np.array(condition)==g])**2)
                for g in set(condition))
            result['rmse_gain'] = result['baseline']['rmse']-result['augmented']['rmse']
            all_results[split_name][str(alpha)] = result
            predictions[(split_name, alpha)] = preds
        controls = []
        for seed in range(SEED, SEED+100):
            noise = np.random.default_rng(seed).normal(size=(len(y), 2))
            pred = cv(np.column_stack([base, noise]), y, groups, 1)
            controls.append(scores(y, pred)['rmse'])
        observed = all_results[split_name]['1']['augmented']['rmse']
        all_results[split_name]['capacity_control'] = dict(
            rmse_min=float(min(controls)), rmse_median=float(np.median(controls)),
            rmse_max=float(max(controls)), n_controls_beating_augmented=sum(c < observed for c in controls),
            all_rmse=controls)
    with (ROOT/'results'/'matched_rows.csv').open('w') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)
    with (ROOT/'results'/'predictions.csv').open('w') as f:
        fields = ['split','alpha','model','source','salt','temp','cycle','observed','predicted']
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for (split, alpha), preds in predictions.items():
            for model, pred in preds.items():
                for r, observed, prediction in zip(rows, y, pred):
                    writer.writerow(dict(split=split, alpha=alpha, model=model,
                                         **{k:r[k] for k in ['source','salt','temp','cycle']},
                                         observed=observed, predicted=prediction))
    manifest = dict(protocol_sha256=hashlib.sha256((ROOT/'PROTOCOL.md').read_bytes()).hexdigest(),
                    code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                    python=platform.python_version(), numpy=np.__version__, audit=audit, results=all_results)
    (ROOT/'results'/'analysis.json').write_text(json.dumps(manifest, indent=2, default=lambda x: int(x))+'\n')
    print(json.dumps({name:{alpha:{k:v for k,v in value.items() if k not in ['by_source','all_rmse']}
                           for alpha,value in results.items()}
                      for name,results in all_results.items()}, indent=2, default=lambda x:int(x)))


if __name__ == '__main__':
    main()
