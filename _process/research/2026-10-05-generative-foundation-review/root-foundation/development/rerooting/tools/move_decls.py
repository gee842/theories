"""Move whole declarations between Lean modules of the Becoming package, keeping their scope.

usage: move_decls.py PACKAGE PLAN RANGES

PACKAGE is the folder holding `Becoming/`. PLAN is a JSON file
{"moves": {name: [source module, target module]}, "headers": {target: text}, "imports": {target: [module, ...]},
"source_order": {target: [module, ...]}}; a target receives its sources' declarations in that order.
RANGES is a TSV of `name, start line, start column, end line, end column`, from Lean's declaration
ranges (`findDeclarationRanges?`), with lines counted from 1.

Each declaration moves as its source text: the lines of its range, with the doc comment and the
attribute lines directly above it. In a target module, the declarations from one source keep their
order and the scope they had there: the namespaces and sections around them and the `variable`,
`open` and `universe` commands in effect, with namespaces and sections that receive nothing left
out. A source keeps everything else byte for byte; at each cut, a run of blank lines is reduced to
one. Statements and proofs are not touched, so full Lean names stay.
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

SCOPE = re.compile(r"^(namespace|section|end|variable|open|universe)\b")


def comment_depths(lines):
    """The block-comment depth at the start of each line."""
    depths, depth = [], 0
    for line in lines:
        depths.append(depth)
        i, in_string = 0, False
        while i < len(line):
            two = line[i:i + 2]
            if in_string:
                if line[i] == "\\":
                    i += 2
                    continue
                if line[i] == '"':
                    in_string = False
            elif depth > 0:
                if two == "/-":
                    depth += 1
                    i += 2
                    continue
                if two == "-/":
                    depth -= 1
                    i += 2
                    continue
            else:
                if two == "--":
                    break
                if two == "/-":
                    depth += 1
                    i += 2
                    continue
                if line[i] == '"':
                    in_string = True
            i += 1
    return depths


def block_start(lines, depths, start):
    """The first line of a declaration starting at `start` (0-based): its doc comment and attributes."""
    i = start
    while i > 0:
        prev = lines[i - 1]
        if prev.startswith("@["):
            i -= 1
            continue
        if prev.rstrip().endswith("-/"):
            # The comment ending on the line above opens on the last line before it that starts
            # outside every comment.
            k = i - 1
            while k > 0 and depths[k] > 0:
                k -= 1
            if lines[k].startswith("/--"):
                i = k
                continue
        break
    return i


def scope_commands(lines, depths):
    """(first line, last line, kind, name, text) of each scoping command, 0-based and inclusive."""
    out = []
    i = 0
    while i < len(lines):
        if depths[i] == 0 and SCOPE.match(lines[i]):
            j = i
            while j + 1 < len(lines) and lines[j + 1][:1] in (" ", "\t") and lines[j + 1].strip():
                j += 1
            word = lines[i].split()[0]
            name = lines[i].split()[1] if len(lines[i].split()) > 1 and word in ("namespace", "section", "end") else ""
            out.append((i, j, word, name, "".join(lines[i:j + 1])))
            i = j + 1
        else:
            i += 1
    return out


def skeleton(lines, depths, blocks):
    """The source's scope tree holding only `blocks` [(first, last)], as Lean text."""
    events = [(a, "scope", c) for c in scope_commands(lines, depths) for a in [c[0]]]
    events += [(a, "decl", (a, b)) for a, b in blocks]
    events.sort(key=lambda e: e[0])
    root = {"kind": "root", "name": "", "items": []}
    stack = [root]
    for _, kind, data in events:
        if kind == "decl":
            a, b = data
            stack[-1]["items"].append(("decl", "".join(lines[a:b + 1])))
            continue
        _, _, word, name, text = data
        if word in ("namespace", "section"):
            node = {"kind": word, "name": name, "items": [], "open": text}
            stack[-1]["items"].append(("node", node))
            stack.append(node)
        elif word == "end":
            if len(stack) > 1:
                stack.pop()
        else:
            stack[-1]["items"].append(("cmd", text))

    def has_decl(node):
        return any(k == "decl" or (k == "node" and has_decl(v)) for k, v in node["items"])

    def emit(node):
        parts = []
        for k, v in node["items"]:
            if k == "decl" or k == "cmd":
                parts.append(v.rstrip("\n") + "\n")
            elif has_decl(v):
                inner = emit(v)
                end = "end" + (" " + v["name"] if v["name"] else "")
                parts.append(v["open"].rstrip("\n") + "\n\n" + inner + "\n" + end + "\n")
        return "\n".join(parts)

    return emit(root)


def main():
    package, plan_path, ranges_path = sys.argv[1:4]
    package = Path(package)
    plan = json.loads(Path(plan_path).read_text())
    ranges = {}
    for row in Path(ranges_path).read_text().splitlines():
        name, sl, sc, el, ec = row.split("\t")
        ranges[name] = (int(sl) - 1, int(el) - 1)
    by_source = defaultdict(lambda: defaultdict(list))
    for name, (source, target) in plan["moves"].items():
        by_source[source][target].append(name)

    path_of = lambda m: package / (m.replace(".", "/") + ".lean")
    bodies = defaultdict(list)
    sources_order = []
    for source, targets in by_source.items():
        text = path_of(source).read_text()
        lines = text.splitlines(keepends=True)
        depths = comment_depths(lines)
        cut = []
        for target, names in targets.items():
            blocks = []
            for n in names:
                a, b = ranges[n]
                blocks.append((block_start(lines, depths, a), b))
            blocks.sort()
            cut += blocks
            bodies[target].append((source, skeleton(lines, depths, blocks)))
        sources_order.append(source)
        drop = set()
        for a, b in cut:
            drop.update(range(a, b + 1))
        kept, blank = [], False
        for i, line in enumerate(lines):
            if i in drop:
                continue
            if not line.strip():
                if blank:
                    continue
                blank = True
            else:
                blank = False
            kept.append(line)
        path_of(source).write_text("".join(kept))
        print(f"{source}: {len(cut)} declarations out")

    for target, parts in bodies.items():
        order = plan.get("source_order", {}).get(target, [])
        parts.sort(key=lambda sp: order.index(sp[0]) if sp[0] in order else len(order))
        imports = "".join(f"import {m}\n" for m in plan["imports"][target])
        header = plan["headers"][target].rstrip("\n") + "\n"
        body = "\n".join(f"-- from `{s}`\n\n{t}" for s, t in parts)
        path = path_of(target)
        if path.exists():
            raise SystemExit(f"{path} exists")
        path.write_text(imports + "\n" + header + "\n" + body)
        print(f"{target}: written from {[s for s, _ in parts]}")


if __name__ == "__main__":
    main()
