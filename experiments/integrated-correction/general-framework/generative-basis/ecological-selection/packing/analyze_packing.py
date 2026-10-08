#!/usr/bin/env python3
"""Numerical correspondence audit of Day et al. (2022), not a proof.

Read the original ZIPs without editing spreadsheets. Reconstruct bounded
Voronoi volumes from 20 SEM clusters, using the paper's radial hull extension.
The Coulter export is interpreted as volume-equivalent spherical diameter.
No scale factor is fitted to the published figure. No biological replicates
are inferred from file suffixes. No offspring sizes are inferred from a census.
"""
import csv
import hashlib
import io
import json
import math
from pathlib import Path
import platform
import zipfile

import numpy as np
import scipy
from scipy.spatial import ConvexHull, HalfspaceIntersection
from scipy.special import gammainc
import openpyxl

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "RESEARCH.md").exists())
SOURCE = ROOT / "sources/evolutionary-selection/day-2022"
VC = 17.44
VSTAR_RATIO = 2.02


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def bounded_volumes(points, boundary):
    """Intersect each nearest-center region with an explicit convex boundary.

    Work in cell-centered coordinates to avoid loss of precision from the
    source's image-coordinate offset. Distinct centers must be strictly inside
    the boundary. All geometry is floating point, checked numerically.
    """
    hull = ConvexHull(boundary)
    volumes = []
    max_violation = 0.0
    for i, p in enumerate(points):
        delta = np.delete(points - p, i, axis=0)
        assert np.all(np.linalg.norm(delta, axis=1) > 0)
        neighbor = np.c_[delta, -np.einsum("ij,ij->i", delta, delta) / 2]
        edge = hull.equations.copy()
        edge[:, 3] += edge[:, :3] @ p
        planes = np.r_[neighbor, edge]
        assert np.max(planes[:, 3]) < 0
        vertices = HalfspaceIntersection(planes, np.zeros(3)).intersections
        max_violation = max(max_violation, float(np.max(vertices @ planes[:, :3].T + planes[:, 3])))
        volumes.append(ConvexHull(vertices).volume)
    relative_error = abs(sum(volumes) - hull.volume) / hull.volume
    assert relative_error < 1e-9, relative_error
    assert max_violation < 1e-7, max_violation
    return np.array(volumes), float(hull.volume), relative_error, max_violation


def reconstructed_volumes(points, extension):
    centered = points - np.mean(points, axis=0)
    vertices = centered[ConvexHull(centered).vertices]
    radii = np.linalg.norm(vertices, axis=1)
    boundary = vertices * (1 + extension / radii[:, None])
    # The paper's initial sphere has max-center radius + 5; with extension <=5
    # this boundary lies inside it. Direct convex intersection avoids spherical
    # approximation. Original Voro++/Matlab wrapper is not reproduced.
    return bounded_volumes(centered, boundary)


def moment_prediction(volumes):
    mean = float(np.mean(volumes))
    variance = float(np.var(volumes, ddof=0))
    k = (mean - VC) ** 2 / variance
    scale = variance / (mean - VC)
    p = float(gammainc(k, (VSTAR_RATIO * VC - VC) / scale))
    ordered = np.sort(volumes)
    cdf = gammainc(k, np.maximum(ordered - VC, 0) / scale)
    ranks = (np.arange(len(volumes)) + .5) / len(volumes)
    return dict(cells=len(volumes), mean_volume_um3=mean, variance_um6=variance,
                minimum_volume_um3=float(min(volumes)), k=k, scale_um3=scale,
                p_star=p, decay_rate=-math.log1p(-p),
                empirical_fraction_below_v_star=float(np.mean(volumes <= VC * VSTAR_RATIO)),
                empirical_fraction_below_v_c=float(np.mean(volumes < VC)),
                cdf_midrank_rmse=float(np.sqrt(np.mean((ranks - cdf)**2))))


def main():
    # Numerical sanity check: eight equal octants of a unit cube.
    corners = np.array([[x, y, z] for x in (-.5, .5) for y in (-.5, .5) for z in (-.5, .5)])
    cube, _, cube_err, _ = bounded_volumes(corners / 2, corners)
    assert np.max(abs(cube - .125)) < 1e-12
    result = dict(scope="Exploratory numerical correspondence audit; no new theorem or biological replication",
                  source_sha256={p.name: sha(p) for p in sorted(SOURCE.iterdir()) if p.suffix in (".zip", ".pdf")},
                  code_sha256=sha(Path(__file__)),
                  runtime=dict(python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__, openpyxl=openpyxl.__version__),
                  assumptions=dict(cell_volume_um3=VC, critical_volume_over_cell_volume=VSTAR_RATIO,
                                   coordinate_unit="micrometers, following article SEM methods",
                                   diameter="volume-equivalent spherical diameter in micrometers",
                                   variance="population variance of pooled cell neighborhoods",
                                   boundary="convex-hull vertices shifted radially from centroid by 3 micrometers"),
                  numerical_sanity=dict(unit_cube_max_volume_error=float(np.max(abs(cube-.125))), relative_partition_error=cube_err))
    all_diameters, files, export_rows = [], [], []
    with zipfile.ZipFile(SOURCE / "size-data.zip") as archive:
        for name in sorted(n for n in archive.namelist() if n.endswith(".xlsx")):
            wb = openpyxl.load_workbook(io.BytesIO(archive.read(name)), read_only=True, data_only=True)
            assert wb.sheetnames == ["Sheet1"]
            rows = list(wb.active.values)
            assert rows[0] == ("Sequence", "Diameter") and rows[1] == (None, "µm")
            seq = [r[0] for r in rows[2:]]
            assert seq == list(range(1, len(seq)+1))
            ds = np.array([r[1] for r in rows[2:]], dtype=float)
            assert np.all(np.isfinite(ds)) and np.all(ds > 0)
            ns = math.pi / (6*VC) * ds**3
            files.append(dict(file=name, sha256=hashlib.sha256(archive.read(name)).hexdigest(), observations=len(ds),
                              diameter_min_um=float(min(ds)), diameter_mean_um=float(np.mean(ds)), diameter_max_um=float(max(ds)),
                              estimated_cells_mean=float(np.mean(ns)), estimated_cells_median=float(np.median(ns)),
                              estimated_cells_max=float(max(ns)), estimated_cells_above_350=int(sum(ns > 350)),
                              estimated_cells_300_to_350=int(sum((ns >= 300) & (ns < 350)))))
            all_diameters.extend(ds)
            export_rows.extend((name, int(i), float(d), float(n)) for i, d, n in zip(seq, ds, ns))
            wb.close()
    result["coulter_files"] = files
    diameters = np.array(all_diameters)
    cell_counts = math.pi / (6*VC) * diameters**3
    result["coulter_pooled"] = dict(observations=len(cell_counts), mean_estimated_cells=float(np.mean(cell_counts)),
                                    above_350=int(sum(cell_counts > 350)), fraction_above_350=float(np.mean(cell_counts > 350)))
    # Preserve a transparent reading edition, not a replacement for source XLSX.
    with (HERE / "diameter-reading.csv").open("w", newline="") as f:
        out = csv.writer(f); out.writerow(["source_file", "sequence", "diameter_um", "estimated_cells_vc17_44"]); out.writerows(export_rows)
    clusters = []
    with zipfile.ZipFile(SOURCE / "packing-data.zip") as archive:
        for name in sorted(n for n in archive.namelist() if "/Snowflake_SEM_positions/particles-" in n and n.endswith(".txt")):
            data = np.loadtxt(io.BytesIO(archive.read(name)))
            assert data.shape[1] == 4 and len(np.unique(data[:, 0])) == len(data)
            clusters.append((name, data[:, 1:]))
    result["packing"] = {}
    volume_rows = []
    for extension in (1.0, 3.0, 5.0):
        pooled, cluster_stats, partition_errors = [], [], []
        for name, points in clusters:
            volumes, hull_volume, error, violation = reconstructed_volumes(points, extension)
            pooled.extend(volumes)
            partition_errors.append(error)
            cluster_stats.append(dict(file=name, cells=len(points), hull_volume_um3=hull_volume,
                                      partition_relative_error=error, maximum_halfspace_violation=violation,
                                      **{k:v for k,v in moment_prediction(volumes).items() if k != "cells"}))
            if extension == 3:
                volume_rows.extend((name, i+1, float(v)) for i,v in enumerate(volumes))
        stats = moment_prediction(np.array(pooled))
        stats.update(cluster_count=len(clusters), maximum_partition_error=max(partition_errors), clusters=cluster_stats)
        result["packing"][str(extension)] = stats
    with (HERE / "voronoi-reading.csv").open("w", newline="") as f:
        out=csv.writer(f); out.writerow(["source_file", "source_row_one_based", "bounded_voronoi_volume_um3"]); out.writerows(volume_rows)
    result["scope_limits"] = [
        "10,020 observations are a population census, not 10,020 independent evolutionary lineages or fracture events.",
        "Suffixes 01/02 do not establish independent biological replication.",
        "Cell-volume spread 7.33 is not treated as standard error or confidence interval for the mean.",
        "One- and five-micrometer boundaries are sensitivity choices, not uncertainty bounds.",
        "Geometry reconstruction checks the stated boundary interpretation, not exact replication of unpublished preprocessing.",
        "Critical local packing threshold and independence are supplied from the paper, not validated by this computation.",
        "No fitted rescaling repairs the source-data/figure correspondence.",
        "A census distribution does not supply fracture-product sizes, their future survival, or resource renewal."
    ]
    (HERE / "packing-results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"coulter": result["coulter_pooled"], "packing": {k: {x:v[x] for x in ("cells","cluster_count","k","p_star","cdf_midrank_rmse","maximum_partition_error")} for k,v in result["packing"].items()}}, indent=2))


if __name__ == "__main__":
    main()
