#!/usr/bin/env python3
"""Exploratory checks of preserved biological data; no original code is executed."""
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict
import csv
import hashlib
import io
import json
import platform
import statistics
import xml.etree.ElementTree as ET
import zipfile

import numpy as np
import openpyxl
import scipy
from scipy.optimize import least_squares

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'RESEARCH.md').exists())
SOURCE = ROOT / 'sources/biological-scale-correspondence'
NS = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def summary(values):
    a = np.asarray(values, dtype=float)
    assert len(a) > 1 and np.isfinite(a).all()
    return dict(n=len(a), mean=float(a.mean()), sd=float(a.std(ddof=1)),
                median=float(np.median(a)), q25=float(np.quantile(a, .25)),
                q75=float(np.quantile(a, .75)), min=float(a.min()), max=float(a.max()))


def source_workbook():
    path = SOURCE / 'pgen-1011178/pgen.1011178.s005.xlsx'
    wb = openpyxl.load_workbook(path, data_only=True, read_only=True)
    # An independent decoder verifies every numeric cell in the original file,
    # including unselected panels; no workbook is rewritten.
    checked = 0
    with zipfile.ZipFile(path) as z:
        workbook = ET.fromstring(z.read('xl/workbook.xml'))
        rels = ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))
        targets = {v.attrib['Id']: v.attrib['Target'] for v in rels}
        for sheet in workbook.findall('s:sheets/s:sheet', NS):
            key = sheet.attrib['{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id']
            target = targets[key]
            target = target.lstrip('/') if target.startswith('/') else 'xl/' + target
            xml_values = {}
            for cell in ET.fromstring(z.read(target)).findall('.//s:c', NS):
                value = cell.find('s:v', NS)
                if cell.attrib.get('t', 'n') == 'n' and value is not None and value.text:
                    xml_values[cell.attrib['r']] = float(value.text)
            py_values = {c.coordinate: float(c.value) for row in wb[sheet.attrib['name']]
                         for c in row if isinstance(c.value, (int, float)) and not isinstance(c.value, bool)}
            assert xml_values == py_values, sheet.attrib['name']
            checked += len(xml_values)
    return wb, checked


def memory_analysis():
    wb, checked = source_workbook()
    panels = {}

    def extract(key, sheet, first, last, names, unit):
        groups = {}
        for col, name in names.items():
            values, cells = [], []
            for row in range(first, last + 1):
                cell = wb[sheet][f'{col}{row}']
                if isinstance(cell.value, (int, float)):
                    values.append(float(cell.value))
                    cells.append(cell.coordinate)
            groups[name] = dict(**summary(values), cells=cells, values=values)
        panels[key] = dict(sheet=sheet, rows=[first, last], unit=unit, groups=groups)
        return panels[key]

    for key, start, end in [('F1', 4, 70), ('F2', 74, 124), ('F4', 128, 192), ('F5', 194, 248)]:
        panel = extract('ASI_' + key, 'Figure 3', start, end,
                        {'A': 'OP50', 'B': 'GRb0427'}, 'ASI neuron; worm and batch identities unavailable')
        g = panel['groups']
        panel['trained_minus_control'] = g['GRb0427']['mean'] - g['OP50']['mean']
        panel['trained_to_control_ratio'] = g['GRb0427']['mean'] / g['OP50']['mean']
    panel = extract('choice_generations', 'Figure 3', 252, 299,
                    {chr(65 + 2*i + j): f'{gen}_{treatment}'
                     for i, gen in enumerate(['P0', 'F1', 'F2', 'F3', 'F4', 'F5'])
                     for j, treatment in enumerate(['OP50', 'GRb0427'])}, 'choice-assay plate')
    panel['trained_minus_control'] = {
        gen: panel['groups'][gen + '_GRb0427']['mean'] - panel['groups'][gen + '_OP50']['mean']
        for gen in ['P0', 'F1', 'F2', 'F3', 'F4', 'F5']}
    # One Figure 3E observation extends into a row whose column A starts 3F.
    assert 'J299' in panel['groups']['F4_GRb0427']['cells']
    extract('source_learning_indices', 'Figure 3', 302, 306,
            {chr(65+i): gen for i, gen in enumerate(['P0', 'F1', 'F2', 'F3', 'F4', 'F5'])},
            'source experiment-level learning index; no cross-panel pairing inferred')
    for key, first, last, names, unit in [
        ('deletion_F2_choice', 387, 419, {'A': 'OP50', 'B': 'GRb0427', 'C': 'GRb0427_delta16'}, 'choice-assay plate'),
        ('deletion_ASI', 423, 487, {'A': 'OP50', 'B': 'GRb0427', 'C': 'GRb0427_delta16'}, 'ASI neuron; worm and batch identities unavailable'),
        ('mismatch_choice', 491, 531, {'A': 'empty', 'B': 'Pv1', 'C': 'Pv1_mismatch'}, 'choice-assay plate')]:
        panel = extract(key, 'Figure 8', first, last, names, unit)
        control = next(iter(names.values()))
        panel['mean_minus_control'] = {name: v['mean'] - panel['groups'][control]['mean']
                                      for name, v in panel['groups'].items()}
    for mutant, first, last in [('sid2', 5, 35), ('dcr1', 40, 62), ('sid1', 67, 93), ('hrde1', 98, 132)]:
        panel = extract('pathway_' + mutant, 'Figure 9', first, last,
                        {'A': 'N2_empty', 'B': 'N2_Pv1', 'C': mutant+'_empty', 'D': mutant+'_Pv1'},
                        'choice-assay plate')
        panel['Pv1_minus_empty'] = {
            strain: panel['groups'][strain + '_Pv1']['mean'] - panel['groups'][strain + '_empty']['mean']
            for strain in ['N2', mutant]}
    wb.close()
    return dict(numeric_cells_cross_checked=checked, panels=panels,
                inference='Descriptive within-panel comparisons only. No independence of neurons, cross-generation camera calibration, fabricated individual joins or new p-values.')


def read_member(z, suffix, inputs):
    names = [name for name in z.namelist() if name.endswith('/Data/' + suffix)]
    assert len(names) == 1
    raw = z.read(names[0])
    inputs[names[0]] = dict(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
    return list(csv.DictReader(io.StringIO(raw.decode('utf-8-sig'))))


def calibration(rows):
    records = []
    for i, row in enumerate(rows, start=2):
        green, cfu = float(row['Green']), float(row['CFU/worm'])
        assert green > 0 and cfu >= 0
        y = float(np.log10(cfu)) if cfu > 0 else None
        if y is not None:
            assert abs(y - float(row['logCFU'])) < 1e-7
        else:
            assert row['logCFU'] == 'NA'
        records.append(dict(csv_line=i, time=row['Time'], condition=row['Condition'],
                            well=row['Row'] + row['Column'], green=green, cfu=cfu,
                            log10_green=float(np.log10(green)), log10_cfu=y))
    train = [r for r in records if r['time'] == 'T48' and r['cfu'] > 0]
    test = [r for r in records if r['time'] == 'T72' and r['cfu'] > 0]
    excluded = [r for r in records if r['cfu'] == 0]
    assert len(train) == 70 and len(test) == 96 and len(excluded) == 3
    x = np.array([r['log10_green'] for r in train]); y = np.array([r['log10_cfu'] for r in train])
    x_test = np.array([r['log10_green'] for r in test]); y_test = np.array([r['log10_cfu'] for r in test])
    intercept = float(y.mean())
    linear = np.linalg.lstsq(np.column_stack([np.ones(len(x)), x]), y, rcond=None)[0]
    # Deterministic starts; neither T72 x nor y is used to fit or select a start.
    a_min = float(x.max() + 1e-6)
    starts = []
    def jacobian(p):
        a, _, c = p
        return np.column_stack([-c*x/(a*a-x*x), np.ones(len(x)), np.arctanh(x/a)])
    for a0 in [a_min + .01, a_min + .25, 5., 10., 50.]:
        z0 = np.arctanh(x / a0)
        b0, c0 = np.linalg.lstsq(np.column_stack([np.ones(len(x)), z0]), y, rcond=None)[0]
        fit = least_squares(lambda p: p[1] + p[2]*np.arctanh(x/p[0]) - y,
                            [a0, b0, max(float(c0), .01)],
                            bounds=([a_min, -np.inf, 1e-12], [100., np.inf, np.inf]),
                            jac=jacobian,
                            max_nfev=20000, ftol=1e-12, xtol=1e-12, gtol=1e-10,
                            x_scale='jac')
        starts.append(dict(initial_a=a0, parameters=fit.x.tolist(), success=bool(fit.success),
                           training_sse=float(np.sum(fit.fun**2)), optimality=float(fit.optimality),
                           gradient_max=float(np.abs(jacobian(fit.x).T @ fit.fun).max()),
                           evaluations=fit.nfev, termination=str(fit.message)))
    successful = [v for v in starts if v['success'] and np.isfinite(v['training_sse'])]
    assert successful
    chosen = min(successful, key=lambda v: v['training_sse'])
    a, b, c = chosen['parameters']
    valid = np.abs(x_test / a) < 1
    nonlinear_test = np.full(len(test), np.nan)
    nonlinear_test[valid] = b + c*np.arctanh(x_test[valid]/a)
    train_predictions = dict(constant=np.full(len(x), intercept), linear=linear[0]+linear[1]*x,
                             inverse_tanh=b+c*np.arctanh(x/a))
    test_predictions = dict(constant=np.full(len(test), intercept), linear=linear[0]+linear[1]*x_test,
                            inverse_tanh=nonlinear_test)

    def score(target, prediction):
        domain_ok = np.isfinite(prediction)
        # Complete-subset scores are null if even one prediction is undefined.
        if not domain_ok.all():
            return dict(n=len(target), domain_failures=int((~domain_ok).sum()), rmse=None, mae=None, bias=None)
        error = prediction-target
        return dict(n=len(target), domain_failures=0, rmse=float(np.sqrt(np.mean(error**2))),
                    mae=float(np.mean(np.abs(error))), bias=float(np.mean(error)))

    subsets = dict(all=np.ones(len(test), dtype=bool),
                   common_conditions=np.array([r['condition'] != 'CM25' for r in test]),
                   added_CM25=np.array([r['condition'] == 'CM25' for r in test]))
    scores = {model: dict(training=score(y, train_predictions[model]),
                         test={name: score(y_test[mask], pred[mask]) for name, mask in subsets.items()})
              for model, pred in test_predictions.items()}
    for i, row in enumerate(test):
        row['predictions'] = {name: float(v[i]) if np.isfinite(v[i]) else None
                              for name, v in test_predictions.items()}
    for i, row in enumerate(train):
        row['predictions'] = {name: float(v[i]) for name, v in train_predictions.items()}
    return dict(total_records=len(records), training_n=len(train), test_n=len(test),
                zero_cfu_excluded=excluded, constant=intercept, linear_intercept_slope=linear.tolist(),
                inverse_tanh=dict(form='b + c * atanh(log10(GFP) / a)', parameters_abc=[a,b,c],
                                  lower_a=a_min, upper_a=100., starts=starts,
                                  selected_by='lowest successful training SSE only'),
                scores=scores, training=train, test=test,
                scope='Temporal transfer in this dataset only; wells are individual worms. Experimental batch independence and cross-species/instrument transport are not established.')


def migration(rows, run):
    groups = defaultdict(list)
    for i, row in enumerate(rows, start=2):
        green = float(row['Green']); assert green > 0
        if 'logGreen' in row:
            assert abs(float(row['logGreen']) - np.log(green)) < 1e-7
        groups[(row['Time'], row['Condition'])].append((i, green))
    duplicated_baselines = []
    for initial in ['High', 'Low']:
        matching = lambda sign: [{k:v for k,v in row.items() if k != 'Condition'} for row in rows
                                 if row['Time'] == 'T0' and row['Condition'] == initial+' '+sign]
        if matching('+') == matching('-'):
            duplicated_baselines.append(dict(initial=initial, repeated_rows=len(matching('+')),
                                              scope='Entire T0 measurement sequence identical across treatment labels; not independent baselines.'))
    return dict(run=run, total_records=len(rows), duplicated_baselines=duplicated_baselines,
                groups=[dict(time=time, condition=condition, raw_green=summary([v for _,v in values]),
                             log10_green=summary(np.log10([v for _,v in values])),
                             csv_lines=[i for i,_ in values])
                        for (time, condition), values in sorted(groups.items())],
                scope='Sorted cohort distributions; no individual longitudinal identities. Changing sample counts are retained. Migration treatments and inhibition are supplied interventions; no acquired avoidance was measured.')


def main():
    for directory in ['pgen-1011178', 'boddu-2025']:
        manifest = json.loads((SOURCE/directory/'manifest.json').read_text())
        for item in manifest['files']:
            path = SOURCE/directory/item['file']
            assert sha(path) == item['sha256'] and path.stat().st_size == item['bytes']
    archive = SOURCE/'boddu-2025/varianceinwormgut-v1.0.0.zip'
    assert hashlib.md5(archive.read_bytes()).hexdigest() == '1753ae890020663d2b254136206461c0'
    members = {}
    memory = memory_analysis()
    with zipfile.ZipFile(archive) as z:
        cal = calibration(read_member(z, 'CFU Mapping.csv', members))
        mig = [migration(read_member(z, name, members), i)
               for i, name in enumerate(['Migration_Compiled.csv', 'Migration_run2_Compiled.csv'], 1)]
    inputs = {str(p.relative_to(ROOT)): sha(p) for directory in ['pgen-1011178', 'boddu-2025']
              for p in (SOURCE/directory).iterdir() if p.name != 'README.md'}
    result = dict(status='passed', generated_at_utc=datetime.now(timezone.utc).isoformat(),
                  script_sha256=sha(Path(__file__)), plan_sha256=sha(HERE/'analysis-plan.json'),
                  versions=dict(python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__, openpyxl=openpyxl.__version__),
                  inputs=inputs, archive_members=members, memory=memory, calibration=cal, migration=mig,
                  status_meaning='Data extraction, arithmetic and prescribed fits executed successfully. This is not a declaration that a biological model, calibration, or full scale loop is validated.')
    (HERE/'results.json').write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    with (HERE/'calibration-predictions.csv').open('w', newline='') as f:
        names = ['split','csv_line','time','condition','well','green','cfu','log10_green','log10_cfu','constant','linear','inverse_tanh']
        writer = csv.DictWriter(f, fieldnames=names); writer.writeheader()
        for split, rows in [('training', cal['training']), ('test', cal['test'])]:
            for row in rows:
                item = {k:v for k,v in row.items() if k != 'predictions'}
                writer.writerow(dict(split=split, **item, **row['predictions']))
    print(json.dumps(dict(numeric_cells=memory['numeric_cells_cross_checked'],
                          calibration_scores=cal['scores'],
                          inverse_parameters=cal['inverse_tanh']['parameters_abc'],
                          migration_records=[v['total_records'] for v in mig]), indent=2))


if __name__ == '__main__':
    main()
