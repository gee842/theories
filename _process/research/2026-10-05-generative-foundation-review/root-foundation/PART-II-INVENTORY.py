"""Inventory for Part II (PART-II-INVENTORY.md, section 3): for each declaration that Part II of the chapter
names (from the heading of Part II to that of section 8), find it among the sources bound by the core and
periphery receipts, split its signature into hypotheses and statement, and list which hypotheses use the axiom,
G0 or its parts, the other evaluative conditions, the structural conditions, or Part I's premises.
Usage: python3 -B PART-II-INVENTORY.py [--points]. With --points, also list where each proof that takes the axiom
applies it. A mention in the statement (an iff or a conclusion) is not a use. Which points the axiom is used at,
and which law for any significance each use specializes, is read by hand (inventory 3.1); this script finds the
candidates."""
import json
import re
import sys
from pathlib import Path

R = Path(__file__).resolve().parents[4]
L = R / 'experiments/integrated-correction/general-framework/generative-basis/lean'
CHAPTER = R / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
RECEIPTS = [L / 'becoming/becoming-verification.json',
            L / 'universal-ethics/generative-capacity/correction-inquiry-verification.json']
KEYWORDS = ('theorem', 'lemma', 'def', 'abbrev', 'structure', 'inductive', 'class', 'instance')
DECL = re.compile(r'^(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+)*(' + '|'.join(KEYWORDS) +
                  r')\s+([^\s(:{\[]+)')
# What a hypothesis can use. Axiom: Ren's one axiom. Evaluative: G0, its parts and the other premises of Part II.
# Structural: conditions on a valuation's relations. Premises: Part I's premises and decidability.
AXIOM = r'\bUnrestricted\b'
EVALUATIVE = {'G0': r'\bG0\b|\bSignificant\b', 'grounds': r'\bGrounds\b', 'seed': r'\bSeed\b',
              'S0': r'\bSelfGood\b', 'N': r'\bNeutral\b', 'A': r'\b[Aa]rticulates\w*\b',
              'C': r'\bComparison\b', 'L': r'\bLifted\w*\b', 'J': r'\bBetterAt\b',
              'presupposition': r'\bSubTrue\b', 'invariance': r'\bBoundaryInvariant\b|\bStandpointInvariant\b'}
STRUCTURAL = {'connected': r'\bConnected\b', 'held': r'\bHeld\b'}
PREMISES = {'balance': r'\bBalances\b|\bBalancesOn\b', 'dissipation': r'\bDissipat\w*\b',
            'embodiment': r'\bEmbodied\b', 'census': r'\bCensus\b|\bCountedBy\b|\bListed\b',
            'taking': r'\bTaking\b', 'acting': r'\bActing\b', 'dependent': r'\bDependent\b',
            'enclosure': r'\bEnclos\w*\b', 'finiteness': r'\bFinite\b|\bFintype\b',
            'decidability': r'\bDecidable\w*\b'}


def declarations():
    paths = {}
    for receipt in RECEIPTS:
        for module, rel in json.loads(receipt.read_text())['source_paths'].items():
            paths[module] = L / rel
    found = {}
    for module, path in sorted(paths.items()):
        lines = path.read_text().split('\n')
        stack, depth_comment, i = [], 0, 0
        while i < len(lines):
            line, stripped = lines[i], lines[i].strip()
            if depth_comment:
                depth_comment += line.count('/-') - line.count('-/')
                i += 1
                continue
            if stripped.startswith('/-'):
                depth_comment = line.count('/-') - line.count('-/')
                i += 1
                continue
            m = re.match(r'^namespace\s+(\S+)', stripped)
            if m:
                stack.append(m.group(1))
                i += 1
                continue
            if re.match(r'^section\b', stripped):
                stack.append(None)
                i += 1
                continue
            if re.match(r'^end\b', stripped):
                if stack:
                    stack.pop()
                i += 1
                continue
            m = DECL.match(line)
            if not m:
                i += 1
                continue
            name = '.'.join([n for n in stack if n] + [m.group(2)])
            sig, depth, j = [], 0, i
            while j < len(lines):
                seg = lines[j]
                if j > i and (DECL.match(seg) or seg.startswith('/-') or (depth == 0 and re.match(r'^\s*\|', seg))):
                    break
                cut = None
                for k, ch in enumerate(seg):
                    if ch in '([{⟨':
                        depth += 1
                    elif ch in ')]}⟩':
                        depth -= 1
                    elif depth == 0 and seg[k:k + 2] == ':=':
                        cut = k
                        break
                if cut is not None:
                    sig.append(seg[:cut])
                    j += 1
                    break
                sig.append(seg)
                j += 1
                if depth == 0 and re.search(r'\swhere\s*$', seg):
                    break
            end = j
            while end < len(lines) and not DECL.match(lines[end]) and not lines[end].startswith('/-'):
                end += 1
            found.setdefault(name, []).append({'module': module, 'kind': m.group(1), 'signature': '\n'.join(sig),
                                               'body': '\n'.join(lines[j - 1:end])})
            i = j
    return found


def split(sig):
    """Hypotheses (binders and the antecedents of top-level arrows) and the conclusion."""
    head = re.match(r'^\s*\S+\s+\S+', sig)
    depth = 0
    binders, statement = sig, ''
    for k in range(head.end() if head else 0, len(sig)):
        ch = sig[k]
        if ch in '([{⟨':
            depth += 1
        elif ch in ')]}⟩':
            depth -= 1
        elif ch == ':' and depth == 0:
            binders, statement = sig[:k], sig[k + 1:]
            break
    # `→` is right-associative and binds looser than `∧`, `∨`; a binder (`∀`, `∃`, `fun`) or `↔` at depth zero
    # scopes to the end, so no arrow after it separates a hypothesis.
    parts, cur, depth, scoped = [], '', 0, False
    for k, ch in enumerate(statement):
        if ch in '([{⟨':
            depth += 1
        elif ch in ')]}⟩':
            depth -= 1
        if depth == 0 and not scoped and (ch in '∀∃↔' or statement.startswith('fun ', k)):
            scoped = True
        if depth == 0 and not scoped and ch == '→':
            parts.append(cur)
            cur = ''
            continue
        cur += ch
    parts.append(cur)
    named = re.findall(r'[(\[]([^()\[\]]*(?:[(\[][^()\[\]]*[)\]][^()\[\]]*)*)[)\]]', binders)
    return ' '.join(named + parts[:-1]), parts[-1]


def uses(text, table):
    return [k for k, pattern in table.items() if re.search(pattern, text)]


def classify(entry):
    hyps, conclusion = split(entry['signature'])
    row = {'axiom': bool(re.search(AXIOM, hyps)), 'evaluative': uses(hyps, EVALUATIVE),
           'structural': uses(hyps, STRUCTURAL), 'premises': uses(hyps, PREMISES),
           'characterizes': bool(re.search(AXIOM, conclusion))}
    if entry['kind'] not in ('theorem', 'lemma'):
        row['class'] = 'definition'
    elif row['axiom']:
        row['class'] = 'axiom'
    elif row['characterizes']:
        row['class'] = 'characterizes the axiom'
    elif row['evaluative']:
        row['class'] = 'evaluative condition'
    elif row['premises']:
        row['class'] = 'premises of Part I'
    elif row['structural']:
        row['class'] = 'structural condition'
    else:
        row['class'] = 'none'
    return row


def part_two_names():
    lines = CHAPTER.read_text().split('\n')
    start = next(i for i, l in enumerate(lines) if l.startswith('## 第二部分'))
    stop = next(i for i, l in enumerate(lines) if re.match(r'^## 8\. ', l))
    section, seen = 'II', {}
    for line in lines[start:stop]:
        m = re.match(r'^#{2,3} (\d+(?:\.\d+)?)', line)
        if m:
            section = m.group(1)
        for name in re.findall(r'`([A-Za-z_][A-Za-z0-9_.\']*)`', line):
            seen.setdefault(name, section)
    return seen


def main():
    decls = declarations()
    names = part_two_names()
    counts, missing, listed = {}, [], set()
    print('| § | 声明 / Declaration | 模块 / Module | 类 / Class | 假设 / Hypotheses |')
    print('|---|---|---|---|---|')
    for name, section in names.items():
        hits = {full: es for full, es in decls.items() if full == name or full.endswith('.' + name)}
        if not hits:
            missing.append(name)
            continue
        for full, entries in sorted(hits.items()):
            if full in listed:
                continue
            listed.add(full)
            for entry in entries:
                row = classify(entry)
                counts[row['class']] = counts.get(row['class'], 0) + 1
                detail = ', '.join((['axiom'] if row['axiom'] else []) + row['evaluative'] + row['structural'] +
                                   row['premises']) or '-'
                print(f"| {section} | `{full.replace('Becoming.', '')}` | {entry['module'].replace('Becoming.', '')} "
                      f"| {row['class']} | {detail} |")
                if '--points' in sys.argv and row['axiom']:
                    points = re.findall(r'\bunrestricted \(([^()]*,[^()]*)\)', entry['body'])
                    via = re.findall(r'([\w.]+) (?:\w+ )?unrestricted\b', entry['body'])
                    print(f"|  | points: {'; '.join(points) or '-'} | via: {', '.join(via) or '-'} |  |  |")
    print()
    print('counts:', json.dumps(counts, ensure_ascii=False))
    print('not declarations (modules, witness namespaces, variables):', ' '.join(missing))


if __name__ == '__main__':
    main()
