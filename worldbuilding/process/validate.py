#!/usr/bin/env python3
"""Read-only integrity and reference checks for the worldbuilding collection.

Run from any directory with Python 3. Standard library only. Archive hashes
verify the captured files against the saved manifest, not platform history.
Markdown checks cover local inline-link file targets, not heading anchors or
external websites. This does not assess the truth of claims or render diagrams.
"""

from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parent.parent
errors = []


def check(condition, message):
    if not condition:
        errors.append(message)


def read_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        errors.append(f"Cannot load {path.relative_to(ROOT)}: {exc}")
        return {}


manifest = read_json(ROOT / "archive/manifest.json")
archive_files = manifest.get("files", [])
check(bool(archive_files), "Archive manifest contains no files.")
for entry in archive_files:
    path = ROOT / "archive" / entry["path"]
    if not path.is_file():
        errors.append(f"Missing archived message: {entry['path']}")
        continue
    content = path.read_bytes()
    check(len(content) == entry["bytes"], f"Archive size changed: {entry['path']}")
    check(hashlib.sha256(content).hexdigest() == entry["sha256"],
          f"Archive hash changed: {entry['path']}")

graph_path = ROOT / "foundations/possibility-map.json"
graph = read_json(graph_path)
nodes = graph.get("nodes", [])
edges = graph.get("edges", [])
ids = [node.get("id") for node in nodes]
check(bool(nodes), "Possibility graph contains no nodes.")
check(all(isinstance(node_id, str) and node_id for node_id in ids),
      "Every node needs a nonempty string ID.")
check(len(ids) == len(set(ids)), "Duplicate graph node IDs.")
node_ids = set(ids)
sources = graph.get("sources", {})
for source_id, source in sources.items():
    check((graph_path.parent / source["path"]).is_file(),
          f"Missing graph source path for {source_id}.")

for node in nodes:
    node_id = node.get("id", "[missing]")
    for field in ("type", "title", "description", "status", "source_refs"):
        check(bool(node.get(field)), f"{node_id}: missing {field}.")
    check(node.get("type") in graph.get("node_types", {}),
          f"{node_id}: unknown node type.")
    for ref in node.get("source_refs", []):
        check(ref in sources, f"{node_id}: unknown source {ref}.")
    if node.get("artifact"):
        check((graph_path.parent / node["artifact"]).is_file(),
              f"{node_id}: missing artifact path.")

edge_keys = []
for edge in edges:
    edge_key = (edge.get("source"), edge.get("relation"), edge.get("target"))
    edge_keys.append(edge_key)
    check(edge.get("source") in node_ids and edge.get("target") in node_ids,
          f"Unknown endpoint: {edge_key}.")
    check(edge.get("relation") in graph.get("relation_semantics", {}),
          f"Unknown relation: {edge_key}.")
    check(bool(edge.get("rationale")), f"Missing rationale: {edge_key}.")
check(len(edge_keys) == len(set(edge_keys)), "Duplicate graph relationships.")

map_path = ROOT / "foundations/possibility-map.md"
if map_path.is_file():
    catalog_ids = re.findall(r"^\| ([PAMEWTQ]\d+) \|", map_path.read_text(encoding="utf-8"), re.M)
    check(Counter(catalog_ids) == Counter(ids),
          "Markdown catalog differs from JSON node IDs or repeats a node.")

link_count = 0
for path in sorted(ROOT.rglob("*.md")):
    body = path.read_text(encoding="utf-8")
    # Ignore code examples; only real inline links are checked.
    body = re.sub(r"```[^\n]*\n.*?```", "", body, flags=re.S)
    for raw_target in re.findall(r"(?<!!)\[[^\]\n]+\]\(([^\n]+?)\)", body):
        target = raw_target.strip()
        if target.startswith("<") and ">" in target:
            target = target[1:target.index(">")]
        else:
            target = target.split(' "', 1)[0]
        parsed = urlsplit(target)
        if parsed.scheme or not parsed.path:
            continue
        resolved = path.parent / unquote(parsed.path)
        link_count += 1
        check(resolved.exists(),
              f"Broken local link in {path.relative_to(ROOT)}: {target}")

if errors:
    print("Validation failed:", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    sys.exit(1)

print(f"Validated {len(archive_files)} archived messages, {len(nodes)} graph nodes, "
      f"{len(edges)} relationships, and {link_count} local Markdown links.")
