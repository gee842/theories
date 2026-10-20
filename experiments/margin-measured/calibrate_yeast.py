"""Calibration of test bed A before the freeze (no test is run): fixed points per dilution factor,
and the stationary coefficient of variation of the level for candidate sigmas, compared with the
paper's ~0.05 far from the fold (Fig. 3B). Output: results/calibration_yeast.json."""
import json, statistics, sys
import yeast

out = {"fixed_points": {}, "cv": {}}
for df in (250, 500, 750, 1000, 1400, 1600, 1700):
    out["fixed_points"][df] = [round(r, 1) for r in yeast.fixed_points(df)]
for sigma in (0.03, 0.05, 0.08):
    for df in (500, 750, 1000, 1400):
        # ensemble CV over 60 replicates on each of days 10..14 (the paper: >= 46 replicates, 5 days)
        cvs = []
        for d in range(10, 15):
            xs = [yeast.stationary(df, seed, days=d + 1, burn=d, sigma=sigma)[0] for seed in range(60)]
            xs = [x for x in xs if x > 0]
            cvs.append(statistics.pstdev(xs) / statistics.mean(xs))
        out["cv"][f"{sigma}/{df}"] = round(statistics.mean(cvs), 4)
json.dump(out, open("results/calibration_yeast.json", "w"), indent=1)
print(json.dumps(out, indent=1))
