"""Frozen exploratory temporal/source holdout; see PROTOCOL.md for claim limits."""
from pathlib import Path
import csv
import hashlib
import itertools
import json
import platform
import numpy as np

HERE = Path(__file__).resolve().parent
REPO = Path('/Users/ren/theories')
SOURCE = REPO / 'experiments/integrated-correction/general-framework/closure-study/external-test/results-unfiltered/matched_rows.csv'
FROZEN_PROTOCOL = '4858ec20a8a1d194d51b3c0d72d6c043f563e4370972791dfbad0dbd4f596e66'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def candidates():
    # This order is the declared deterministic tie-break order.
    return ([dict(family='persistence'), dict(family='mean')]
            + [dict(family='ridge', alpha=a) for a in [100., 10., 1., .1]]
            + [dict(family='kernel', alpha=a, gamma=g)
               for a in [10., 1., .1, .01] for g in [.1, 1., 10.]])


def design(rows, augmented, family):
    values = []
    for r in rows:
        od, salt, temp, cycle = (r[k] for k in ['current_od', 'salt', 'temp', 'cycle'])
        v = [od, salt, temp, cycle]
        if family == 'ridge':
            v += [salt**2, cycle**2, salt*temp, od*salt, od*temp]
        if augmented:
            v += [r['mcn'], r['shannon']]
        values.append(v)
    return np.array(values, dtype=float)


def predict(rows, y, train, test, candidate, augmented):
    family = candidate['family']
    if family == 'persistence':
        return np.array([rows[i]['current_od'] for i in test])
    mean_y = np.mean(y[train])
    if family == 'mean':
        return np.full(len(test), mean_y)
    X = design(rows, augmented, family)
    mu, sd = X[train].mean(0), X[train].std(0)
    active = sd > 1e-12
    Z, T = (X[train][:, active]-mu[active])/sd[active], (X[test][:, active]-mu[active])/sd[active]
    centered_y = y[train] - mean_y
    if family == 'ridge':
        beta = np.linalg.solve(Z.T@Z + candidate['alpha']*np.eye(Z.shape[1]), Z.T@centered_y)
        return mean_y + T@beta
    assert family == 'kernel'
    p = max(1, Z.shape[1])
    def kernel(a, b):
        return np.exp(-candidate['gamma']*np.sum((a[:, None, :]-b[None, :, :])**2, axis=2)/p)
    K = kernel(Z, Z)
    beta = np.linalg.solve(K + candidate['alpha']*np.eye(len(train)), centered_y)
    return mean_y + kernel(T, Z)@beta


def scores(y, p):
    return dict(rmse=float(np.sqrt(np.mean((y-p)**2))), mae=float(np.mean(np.abs(y-p))))


def best_index(validation, families=None):
    eligible = [i for i, v in enumerate(validation) if families is None or v['candidate']['family'] in families]
    best = eligible[0]
    for i in eligible[1:]:
        if validation[i]['mse'] < validation[best]['mse']-1e-12:
            best = i
    return best


def main():
    assert sha(HERE/'PROTOCOL.md') == FROZEN_PROTOCOL, 'Protocol changed after freeze'
    raw = list(csv.DictReader(SOURCE.open()))
    rows = [{k: v if k == 'source' else float(v) for k, v in row.items()} for row in raw]
    assert len(rows) == 72
    keys = [(r['source'], r['salt'], r['temp'], r['cycle']) for r in rows]
    assert len(set(keys)) == 72
    sources = sorted({r['source'] for r in rows})
    assert len(sources) == 4
    assert all({r['cycle'] for r in rows if r['source'] == s} == {1., 3., 5.} for s in sources)
    y = np.array([r['next_od'] for r in rows])
    assert np.isfinite([[r[k] for k in r if k != 'source'] for r in rows]).all()
    test_indices = np.array([i for i, r in enumerate(rows) if r['cycle'] == 5])
    assert len(test_indices) == 24
    predictions, folds = {}, []
    for held in sources:
        train = np.array([i for i, r in enumerate(rows) if r['source'] != held and r['cycle'] <= 3])
        test = np.array([i for i, r in enumerate(rows) if r['source'] == held and r['cycle'] == 5])
        assert len(train) == 36 and len(test) == 6
        assert not {rows[i]['source'] for i in train} & {rows[i]['source'] for i in test}
        assert max(rows[i]['cycle']+1 for i in train) < min(rows[i]['cycle'] for i in test)
        fold = dict(held_out_source=held, train_indices=train.tolist(), test_indices=test.tolist(), libraries={})
        for augmented in [False, True]:
            label = 'augmented' if augmented else 'baseline'
            validation = []
            for c in candidates():
                errors, inner_folds = [], []
                for inner_held in [s for s in sources if s != held]:
                    inner_train = np.array([i for i in train if rows[i]['source'] != inner_held and rows[i]['cycle'] == 1])
                    inner_test = np.array([i for i in train if rows[i]['source'] == inner_held and rows[i]['cycle'] == 3])
                    assert len(inner_train) == 12 and len(inner_test) == 6
                    assert not {rows[i]['source'] for i in inner_train} & {rows[i]['source'] for i in inner_test}
                    assert max(rows[i]['cycle']+1 for i in inner_train) < min(rows[i]['cycle'] for i in inner_test)
                    p = predict(rows, y, inner_train, inner_test, c, augmented)
                    errors.extend((y[inner_test]-p)**2)
                    inner_folds.append(dict(held_out_source=inner_held, train_indices=inner_train.tolist(),
                                            test_indices=inner_test.tolist(), mse=float(np.mean((y[inner_test]-p)**2))))
                validation.append(dict(candidate=c, mse=float(np.mean(errors)), inner_folds=inner_folds))
            chosen = {suffix: best_index(validation, families) for suffix, families in
                      [('selected', None), ('ridge_only', {'ridge'}), ('kernel_only', {'kernel'})]}
            for suffix, index in chosen.items():
                name = f'{label}_{suffix}'
                predictions.setdefault(name, np.full(len(rows), np.nan))[test] = predict(rows, y, train, test, validation[index]['candidate'], augmented)
            fold['libraries'][label] = dict(validation=validation, selected_indices=chosen,
                                            selected_candidates={k: validation[v]['candidate'] for k, v in chosen.items()})
        for name in ['persistence', 'mean']:
            predictions.setdefault(name, np.full(len(rows), np.nan))[test] = predict(rows, y, train, test, dict(family=name), False)
        folds.append(fold)
    assert all(np.isfinite(v[test_indices]).all() for v in predictions.values())
    pred_rows = []
    for i in test_indices:
        pred_rows.append(dict(row_index=int(i), **rows[i], **{k: float(v[i]) for k, v in predictions.items()}))
    with (HERE/'predictions.csv').open('w') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(pred_rows[0]))
        writer.writeheader()
        writer.writerows(pred_rows)
    metrics = {k: scores(y[test_indices], p[test_indices]) for k, p in predictions.items()}
    base, aug = predictions['baseline_selected'], predictions['augmented_selected']
    paired, source_indices = [], {}
    for s in sources:
        ix = np.array([i for i in test_indices if rows[i]['source'] == s])
        source_indices[s] = ix
        bs, aus = scores(y[ix], base[ix]), scores(y[ix], aug[ix])
        paired.append(dict(source=s, n=len(ix), baseline_rmse=bs['rmse'], augmented_rmse=aus['rmse'],
                           baseline_mae=bs['mae'], augmented_mae=aus['mae'],
                           mse_gain=float(np.mean((y[ix]-base[ix])**2-(y[ix]-aug[ix])**2)),
                           mae_gain=bs['mae']-aus['mae']))
    with (HERE/'paired_source_errors.csv').open('w') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(paired[0]))
        writer.writeheader()
        writer.writerows(paired)
    bootstrap, omissions = [], []
    for block_sequence in itertools.product(sources, repeat=4):
        ix = np.concatenate([source_indices[s] for s in block_sequence])
        bs, aus = scores(y[ix], base[ix]), scores(y[ix], aug[ix])
        bootstrap.append({k: bs[k]-aus[k] for k in bs})
    for omitted in sources:
        ix = np.concatenate([source_indices[s] for s in sources if s != omitted])
        bs, aus = scores(y[ix], base[ix]), scores(y[ix], aug[ix])
        omissions.append(dict(omitted_source=omitted, **{k: bs[k]-aus[k] for k in bs}))
    result = dict(protocol_sha256=sha(HERE/'PROTOCOL.md'), source_sha256=sha(SOURCE), code_sha256=sha(Path(__file__)),
                  python=platform.python_version(), numpy=np.__version__,
                  source_path=str(SOURCE), n_source_blocks=4, n_test_conditions=24, n_train_per_fold=36,
                  audit=dict(unique_complete_rows=True, strict_temporal_order=True, no_source_overlap=True,
                             train_only_scaling=True, no_source_fixed_effects=True),
                  metrics=metrics, paired_source_errors=paired,
                  primary_expectation_met=all(metrics['augmented_selected'][k] < metrics['baseline_selected'][k] for k in ['rmse', 'mae']),
                  primary_gains={k: metrics['baseline_selected'][k]-metrics['augmented_selected'][k] for k in ['rmse', 'mae']},
                  n_sources_lower_mse=sum(v['mse_gain'] > 0 for v in paired),
                  descriptive_bootstrap_gain_ranges={k: np.quantile([b[k] for b in bootstrap], [.025, .975]).tolist() for k in ['rmse', 'mae']},
                  bootstrap_replicates=256, leave_one_source_out_without_refitting=omissions, folds=folds)
    (HERE/'analysis.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'folds'}, indent=2))


if __name__ == '__main__':
    main()
