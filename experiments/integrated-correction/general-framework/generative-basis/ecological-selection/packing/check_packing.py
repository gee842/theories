#!/usr/bin/env python3
"""Independent standard-library checks of extraction and selected arithmetic.

Does not import the analysis, openpyxl, NumPy, SciPy or its geometry routines.
This is a second implementation, not an independent scientific review.
"""
from collections import defaultdict
import csv
import hashlib
import io
import json
import math
from pathlib import Path
import statistics
import xml.etree.ElementTree as ET
import zipfile

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "RESEARCH.md").exists())
SOURCE = ROOT / "sources/evolutionary-selection/day-2022"
NS = {"s": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def close(a, b):
    assert math.isclose(a, b, rel_tol=1e-10, abs_tol=1e-10), (a,b)


def lower_gamma_regularized(a, x):
    # Positive convergent series; used here only for the small threshold x.
    term = 1/a
    total = term
    for i in range(1, 10000):
        term *= x/(a+i)
        total += term
        if term < abs(total)*1e-15:
            return total * math.exp(-x + a*math.log(x) - math.lgamma(a))
    raise AssertionError("series failed to converge")


def main():
    result = json.loads((HERE / "packing-results.json").read_text())
    manifest = json.loads((SOURCE / "manifest.json").read_text())
    assert result["code_sha256"] == digest(HERE / "analyze_packing.py")
    for name, expected in result["source_sha256"].items():
        assert digest(SOURCE / name) == expected
        assert manifest["preserved_files"][name]["sha256"] == expected
    for path in SOURCE.glob("*.zip"):
        with zipfile.ZipFile(path) as z:
            assert z.testzip() is None
    reading = list(csv.DictReader((HERE / "diameter-reading.csv").open()))
    pooled, row_number = [], 0
    with zipfile.ZipFile(SOURCE / "size-data.zip") as outer:
        for record in result["coulter_files"]:
            raw = outer.read(record["file"])
            assert hashlib.sha256(raw).hexdigest() == record["sha256"]
            with zipfile.ZipFile(io.BytesIO(raw)) as inner:
                strings = ["".join(x.itertext()) for x in ET.fromstring(inner.read("xl/sharedStrings.xml"))]
                xml = ET.fromstring(inner.read("xl/worksheets/sheet1.xml"))
                rows = xml.findall("s:sheetData/s:row", NS)
                assert strings == ["Sequence", "Diameter", "µm"]
                ds = []
                for seq, row in enumerate(rows[2:],1):
                    cells = row.findall("s:c", NS)
                    assert len(cells) == 2 and all(c.find("s:f",NS) is None for c in cells)
                    assert int(cells[0].find("s:v",NS).text) == seq
                    d = float(cells[1].find("s:v",NS).text)
                    n = 4*math.pi*(d/2)**3/(3*17.44)
                    entry=reading[row_number]; row_number+=1
                    assert entry["source_file"] == record["file"] and int(entry["sequence"]) == seq
                    close(float(entry["diameter_um"]),d); close(float(entry["estimated_cells_vc17_44"]),n)
                    ds.append(d)
            ns = [4*math.pi*(d/2)**3/(3*17.44) for d in ds]
            assert len(ns) == record["observations"] == 5010
            close(statistics.mean(ns),record["estimated_cells_mean"])
            close(statistics.median(ns),record["estimated_cells_median"])
            close(max(ns),record["estimated_cells_max"])
            assert sum(n>350 for n in ns) == record["estimated_cells_above_350"]
            assert sum(300<=n<350 for n in ns) == record["estimated_cells_300_to_350"]
            pooled.extend(ns)
    assert row_number == len(reading) == result["coulter_pooled"]["observations"] == 10020
    close(statistics.mean(pooled),result["coulter_pooled"]["mean_estimated_cells"])
    assert sum(n>350 for n in pooled) == result["coulter_pooled"]["above_350"] == 1657
    volume_rows=list(csv.DictReader((HERE / "voronoi-reading.csv").open()))
    volumes=[float(r["bounded_voronoi_volume_um3"]) for r in volume_rows]
    group=defaultdict(list)
    for row in volume_rows: group[row["source_file"]].append(float(row["bounded_voronoi_volume_um3"]))
    with zipfile.ZipFile(SOURCE / "packing-data.zip") as z:
        for name, vs in group.items():
            assert len(z.read(name).decode().splitlines()) == len(vs)
    assert len(group) == 20 and len(volumes) == 2106
    geometry=result["packing"]["3.0"]
    mean=statistics.mean(volumes); variance=statistics.pvariance(volumes)
    k=(mean-17.44)**2/variance; scale=variance/(mean-17.44)
    p=lower_gamma_regularized(k,17.44*1.02/scale)
    close(mean,geometry["mean_volume_um3"]); close(variance,geometry["variance_um6"])
    close(k,geometry["k"]); close(p,geometry["p_star"])
    assert sum(v<=17.44*2.02 for v in volumes) == 28
    for record in geometry["clusters"]:
        vs=group[record["file"]]
        close(sum(vs),record["hull_volume_um3"])
    # Check the reported sensitivity arithmetic, without claiming to recompute
    # the one- and five-micrometer geometric partitions in this verifier.
    for stats in result["packing"].values():
        close(stats["k"], (stats["mean_volume_um3"]-17.44)**2/stats["variance_um6"])
        close(stats["p_star"], lower_gamma_regularized(stats["k"],17.44*1.02/stats["scale_um3"]))
    files=["analyze_packing.py","check_packing.py","packing-results.json","diameter-reading.csv","voronoi-reading.csv"]
    verification={"status":"passed", "scope":"Independent XML extraction and selected statistics; geometry has numerical internal checks, not independent reimplementation or a formal proof.",
                  "checks":{"xlsx_rows":row_number,"packing_cells":len(volumes),"packing_clusters":len(group),"empirical_threshold_crossings":28,"source_archive_crc":"passed","gamma_threshold_series":"matches SciPy"},
                  "not_established":["published Figure 5C reproduced", "p-star is a measured fracture hazard", "independent biological replication", "complete generational mechanism", "superiority of our theory"],
                  "files_sha256":{n:digest(HERE/n) for n in files},"source_manifest_sha256":digest(SOURCE/"manifest.json")}
    (HERE/"verification.json").write_text(json.dumps(verification,indent=2)+"\n")
    print(json.dumps(verification["checks"],indent=2))


if __name__=="__main__":main()
