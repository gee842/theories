"""Export the prespecified per-condition paired errors from saved predictions."""
from pathlib import Path
import csv
from collections import defaultdict

ROOT = Path(__file__).resolve().parent

for version in ['results', 'results-unfiltered']:
    groups = defaultdict(lambda: defaultdict(list))
    with (ROOT/version/'predictions.csv').open() as handle:
        for r in csv.DictReader(handle):
            if r['model'] in ['baseline','augmented']:
                key = tuple(r[k] for k in ['split','alpha','source','salt','temp'])
                groups[key][r['model']].append((float(r['observed'])-float(r['predicted']))**2)
    with (ROOT/version/'paired_condition_errors.csv').open('w') as handle:
        fields = ['split','alpha','source','salt','temp','n_cycles','baseline_mse','augmented_mse','mse_gain']
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for key, values in sorted(groups.items()):
            assert len(values['baseline']) == len(values['augmented']) == 3
            b = sum(values['baseline'])/3
            a = sum(values['augmented'])/3
            writer.writerow(dict(zip(fields, list(key)+[3,b,a,b-a])))
