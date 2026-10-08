#!/usr/bin/env python3
"""Reanalyse a published, checksum-verified survival table without modifying it.

This is exploratory empirical estimation, not a new mathematical proof or an
independent biological replication. Each culture is one observation. The five
old and five new cultures at each isolate age are NOT treated as paired.
Only Python's standard library is required. No source download occurs here.
"""
from collections import defaultdict
import csv
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path
import random
import statistics
import sys

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "RESEARCH.md").is_file())
SOURCE = ROOT / "sources/evolutionary-selection/ratcliff-2013"
RAW = SOURCE / "settling survival compiled data.csv"
BOOTSTRAPS = 40000
SEED = 8102013


def digest(path, algorithm="sha256"):
    return hashlib.new(algorithm, path.read_bytes()).hexdigest()


def percentile(xs, p):
    ordered = sorted(xs)
    position = (len(ordered) - 1) * p
    i = int(position)
    fraction = position - i
    return ordered[i] * (1 - fraction) + ordered[min(i + 1, len(ordered) - 1)] * fraction


def enumerate_label_contrasts(old, new):
    """Exhaust all 252 allocations of these ten culture values to groups of 5.

    A two-sided permutation reference probability needs exchangeability under
    the null. The publication does not document random assignment here, so it
    is a sensitivity calculation, not a certified randomization test.
    """
    values = old + new
    total = sum(values)
    observed = abs(statistics.mean(new) - statistics.mean(old))
    contrasts = []
    for ids in itertools.combinations(range(10), 5):
        selected = sum(values[i] for i in ids)
        contrasts.append(abs((2 * selected - total) / 5))
    return {
        "allocations": len(contrasts),
        "at_least_as_extreme": sum(x >= observed for x in contrasts),
        "two_sided_reference_probability": sum(x >= observed for x in contrasts) / len(contrasts),
        "assumption": "Exchangeability of culture labels under the null; not documented random assignment.",
    }


def balanced_holdout(old, new):
    """Omit every possible old/new pair, never assuming the rows were paired.

    Score the omitted cultures from eight training cultures. The common-rate
    baseline omits transfer regime. The conditional-rate model is ordinary
    stratified estimation, also available to a conventional explanation.
    Reused holdouts are not independent samples for an uncertainty claim.
    """
    baseline, conditional = [], []
    for oi, ni in itertools.product(range(5), repeat=2):
        ot = old[:oi] + old[oi + 1:]
        nt = new[:ni] + new[ni + 1:]
        pooled = statistics.mean(ot + nt)
        baseline.extend([(old[oi] - pooled) ** 2, (new[ni] - pooled) ** 2])
        conditional.extend([(old[oi] - statistics.mean(ot)) ** 2,
                            (new[ni] - statistics.mean(nt)) ** 2])
    return {
        "folds": 25,
        "scored_occurrences": 50,
        "unique_cultures": 10,
        "common_rate_rmse": float(statistics.mean(baseline)) ** 0.5,
        "regime_conditional_rmse": float(statistics.mean(conditional)) ** 0.5,
        "comparison_scope": "Value of retaining the observed transfer regime, not superiority over conventional evolutionary models.",
    }


def main():
    metadata = json.loads((SOURCE / "file-metadata.json").read_text())
    entry = next(x for x in metadata["_embedded"]["stash:files"] if x["path"] == RAW.name)
    assert entry["size"] == RAW.stat().st_size == 643
    assert entry["digestType"] == "md5"
    assert digest(RAW, "md5") == entry["digest"] == "686faa3b6b625634c073bfc33095d4a0"
    grouped = defaultdict(list)
    with RAW.open(newline="") as file:
        reader = csv.DictReader(file)
        assert reader.fieldnames == ["Days of Evolution", "Selection regime (old or new)", "Survival"]
        for row in reader:
            age, regime, value = int(row["Days of Evolution"]), row["Selection regime (old or new)"], Fraction(row["Survival"])
            assert age in (7, 28, 65) and regime in ("old", "new") and 0 <= value <= 1
            grouped[age, regime].append(value)
    assert len(grouped) == 6 and all(len(v) == 5 for v in grouped.values())
    rng = random.Random(SEED)
    results = []
    for age in (7, 28, 65):
        old, new = grouped[age, "old"], grouped[age, "new"]
        om, nm = statistics.mean(old), statistics.mean(new)
        # A second, direct exact-decimal aggregation checks the means. Bootstrap
        # sampling stays within independently observed culture groups.
        assert om == sum(old) / 5 and nm == sum(new) / 5
        of, nf = list(map(float, old)), list(map(float, new))
        ratios, differences = [], []
        for _ in range(BOOTSTRAPS):
            ob = sum(rng.choices(of, k=5)) / 5
            nb = sum(rng.choices(nf, k=5)) / 5
            ratios.append(nb / ob)
            differences.append(nb - ob)
        result = {
            "isolate_day": age,
            "cultures_per_regime": 5,
            "old_mean": float(om), "new_mean": float(nm),
            "old_sample_sd": statistics.stdev(of), "new_sample_sd": statistics.stdev(nf),
            "mean_difference_new_minus_old": float(nm - om),
            "ratio_of_means_new_over_old": float(nm / om),
            "bootstrap_ratio_percentiles_2_5_97_5": [percentile(ratios, .025), percentile(ratios, .975)],
            "bootstrap_difference_percentiles_2_5_97_5": [percentile(differences, .025), percentile(differences, .975)],
            "permutation_sensitivity": enumerate_label_contrasts(old, new),
            "balanced_holdout": balanced_holdout(old, new),
            "old_values": of, "new_values": nf,
        }
        results.append(result)
    output = {
        "status": "analysis_completed_at_declared_empirical_scope",
        "scope": "30 culture observations, three sampled isolates from one historical lineage; not 30 evolutionary lineages",
        "source_doi": "10.5061/dryad.2hr77",
        "source_bytes": RAW.stat().st_size,
        "source_md5_matches_repository": True,
        "source_sha256": digest(RAW),
        "analysis_sha256": digest(Path(__file__)),
        "python_version": sys.version,
        "bootstrap_replicates": BOOTSTRAPS, "bootstrap_seed": SEED,
        "bootstrap_scope": "Exploratory culture-level sampling uncertainty; n=5 per regime. No evolutionary-lineage generalization.",
        "proof_status": "Numerical empirical calculations; no new theorem or Lean claim.",
        "results": results,
        "missing": ["Complete velocity/area table", "linked cluster identities across trait, survival and offspring records",
                    "descendant yield and metabolic renewal measurements for these 30 cultures",
                    "prospective independent validation and adequately informed rival comparison"],
    }
    (HERE / "survival-results.json").write_text(json.dumps(output, indent=2) + "\n")
    for r in results:
        print(f"day {r['isolate_day']}: old={100*r['old_mean']:.4f}%, new={100*r['new_mean']:.4f}%, ratio={r['ratio_of_means_new_over_old']:.4f}; bootstrap {r['bootstrap_ratio_percentiles_2_5_97_5']}")
        print("  holdout:", r["balanced_holdout"])


if __name__ == "__main__":
    main()
