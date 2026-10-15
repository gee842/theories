"""List the phrases in result records that leave a reading or name to Ren.

Usage: python3 -B scan_pending.py ROOT [OUT]

Walks every record JSON under theories/becoming/results/records, skipping the
history, text versions, proof bindings and paths, and prints each string field
that holds such a phrase, with its record, path and schema version. The P110
reconciliation (reconcile_records.py) is checked against this list: what remains
after it runs is what stays Ren's (section 10 of DELEGATED-CHOICES).
"""
import glob
import json
import os
import re
import sys

PATTERN = re.compile(
    r"待 Ren|pending Ren|awaits Ren|await Ren|Ren 的选择|Ren['’]s choice|由 Ren 选择|"
    r"Ren['’]s to choose|属于 Ren|Ren 判断|Ren['’]s judg|由 Ren 定|由 Ren 决定|"
    r"Ren['’]s to decide|（Ren）|\(Ren\)|for Ren to|留给 Ren|left to Ren|"
    r"Ren['’]s decision|Ren 的决定|Ren 的判断|Ren 选择|Ren chooses|Ren to choose|"
    r"is Ren['’]s|are Ren['’]s|remains Ren['’]s|stays Ren['’]s|仍属 Ren|归 Ren")
SKIP = {"history", "text_versions", "proof_bindings", "canonical_source", "aliases",
        "dependencies", "id", "reviewed_at_utc", "schema_version", "status", "kind",
        "family", "standard_boundaries"}


def walk(value, path):
    if isinstance(value, str):
        yield path, value
    elif isinstance(value, dict):
        for key, item in value.items():
            if not path and key in SKIP:
                continue
            if key in ("path", "anchor", "role"):
                continue
            yield from walk(item, path + [str(key)])
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from walk(item, path + [str(index)])


def scan(root):
    found = []
    for name in sorted(glob.glob(os.path.join(root, "theories/becoming/results/records/*.json"))):
        record = json.load(open(name, encoding="utf-8"))
        for path, text in walk(record, []):
            if PATTERN.search(text):
                found.append((record["id"], ".".join(path), record.get("schema_version"), text))
    return found


def main():
    root = sys.argv[1]
    found = scan(root)
    out = open(sys.argv[2], "w", encoding="utf-8") if len(sys.argv) > 2 else sys.stdout
    for rid, path, version, text in found:
        out.write(f"### {rid} | {path} | v{version}\n{text}\n\n")
    print(f"{len(found)} fields in {len({f[0] for f in found})} records", file=sys.stderr)


if __name__ == "__main__":
    main()
