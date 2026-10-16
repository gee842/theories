"""Repair only global prevalence filtering; preserve source feature definitions."""
from pathlib import Path
import csv
import json
import hashlib
import numpy as np
import rdata

ROOT = Path(__file__).resolve().parent
DATA = ROOT / 'data'


def records(path, delimiter=','):
    with path.open() as handle:
        return list(csv.DictReader(handle, delimiter=delimiter))


def normalized(value):
    return 'NA' if value is None else str(value)


def calculate(counts, copies):
    total = counts.sum(axis=1)
    assert np.all(total > 0)
    proportions = counts / total[:, None]
    logp = np.zeros_like(proportions)
    np.log(proportions, out=logp, where=proportions > 0)
    shannon = -(proportions * logp).sum(axis=1)
    corrected = counts / copies[None, :]
    mcn = total / corrected.sum(axis=1)
    return mcn, shannon


def main():
    seq = rdata.read_rds(DATA / 'seqtab.nochim.rds')
    parsed = rdata.parser.parse_file(DATA / 'taxa.rds')
    attrs = rdata.conversion.convert(parsed.object.attributes)
    tax = np.asarray(rdata.conversion.convert(parsed)).reshape(tuple(attrs['dim']), order='F')
    assert np.array_equal(seq.coords['dim_1'].values, attrs['dimnames'][0])
    assert list(attrs['dimnames'][1]) == ['Kingdom','Phylum','Class','Order','Family','Genus','Species']
    counts = np.asarray(seq.values, dtype=float)
    # R subset_taxa removes entries whose eligibility expression evaluates NA.
    eligible = np.array([normalized(t[0]) == 'Bacteria' and normalized(t[4]) not in ['Mitochondria','NA']
                         and normalized(t[1]) != 'NA' for t in tax])
    tax = tax[eligible]
    counts = counts[:, eligible]
    rrn = {}
    for row in records(DATA / 'rrnDB-5.8_pantaxa_stats_NCBI.tsv', '\t'):
        k = (row['rank'], row['name'])
        assert k not in rrn, 'Ambiguous reference mapping'
        rrn[k] = float(row['mean'])
    ranks = ['superkingdom','phylum','class','order','family','genus','species']
    copies, resolution = [], []
    for values in tax:
        names = [normalized(v) for v in values]
        names[-1] = names[-2] + ' ' + names[-1]
        for rank, name in reversed(list(zip(ranks, names))):
            if (rank, name) in rrn:
                copies.append(rrn[(rank, name)])
                resolution.append(rank)
                break
        else:
            raise AssertionError('No copy number reference found')
    copies = np.asarray(copies)
    assert np.all(copies > 0)
    metadata = {(r['plate']+'_'+r['well']):r for r in records(DATA/'metadata.csv')}
    assert len(metadata) == len(seq.coords['dim_0'])
    meta = [metadata[str(sample)] for sample in seq.coords['dim_0'].values]
    keys = ['rep','day','inoc','salt','temp']
    def mk(row):
        return tuple(row[k] for k in keys)
    assert len(set(mk(row) for row in meta)) == len(meta)
    # Reproduce v1 only as a measurement implementation check.
    prevalence_mask = (counts > 0).sum(axis=0) > 1
    old_mcn, old_shannon = calculate(counts[:, prevalence_mask], copies[prevalence_mask])
    expected_mcn = {mk(r):float(r['mcn']) for r in records(DATA/'mcn_df_norare.csv')}
    expected_shannon = {mk(r):float(r['div_value']) for r in records(DATA/'diversity_df_norare.csv')
                        if r['diversity_metric'] == 'Shannon'}
    errors = dict(mcn_max_abs=max(abs(v-expected_mcn[mk(r)]) for v,r in zip(old_mcn, meta)),
                  shannon_max_abs=max(abs(v-expected_shannon[mk(r)]) for v,r in zip(old_shannon, meta)))
    assert max(errors.values()) <= 1e-7, errors
    # Corrected summaries use only this sample's own counts plus the fixed taxonomy/reference.
    mcn, shannon = calculate(counts, copies)
    for filename, field, values in [('mcn_df_unfiltered.csv','mcn',mcn),
                                     ('diversity_df_unfiltered.csv','div_value',shannon)]:
        fields = keys + (['diversity_metric'] if field == 'div_value' else []) + [field]
        with (DATA/filename).open('w') as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            for row, value in zip(meta, values):
                result = {k:row[k] for k in keys}
                if field == 'div_value':
                    result['diversity_metric'] = 'Shannon'
                result[field] = value
                writer.writerow(result)
    report = dict(n_samples=len(meta), n_original_taxa=int(len(eligible)),
                  n_fixed_eligible_taxa=int(eligible.sum()), n_globally_retained_taxa=int(prevalence_mask.sum()),
                  original_replication_error=errors,
                  per_sample_max_feature_change=dict(mcn=float(np.max(np.abs(mcn-old_mcn))),
                                                     shannon=float(np.max(np.abs(shannon-old_shannon)))),
                  protocol_repair_sha256=hashlib.sha256((ROOT/'PROTOCOL-REPAIR.md').read_bytes()).hexdigest(),
                  reconstruction_code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  rdata_version=rdata.__version__)
    (DATA/'reconstruction_audit.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
