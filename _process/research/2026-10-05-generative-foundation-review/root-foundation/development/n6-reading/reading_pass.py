#!/usr/bin/env python3
"""N6, the reading pass the N1 renaming left open (18 October 2026).

The renaming (N5) changed identifiers only; the prose words "registers", "record", "learner", "refutes",
"belief", ... were left to be changed by reading. Each change here was written after reading its sentence;
the edit files hold the reading as data, so the pass can be reviewed, re-applied on a later head and rendered
as the proposal table.

usage (from the root of a checkout):
  python3 -B reading_pass.py concord FILE [WORDS]   print the hits of WORDS (regex) in FILE's prose, with context
  python3 -B reading_pass.py apply [--dry] [--base=REV]  apply every edit file to REV's text (default: the
                                                    merge base with main) and write the results
  python3 -B reading_pass.py table                  write PROPOSAL-FULL.md (every change) next to this script
  python3 -B reading_pass.py left [WORDS]           count what is left in prose after applying

Edit files (edits/*.txt) hold blocks:

  ### TARGET                 a repository path, `lean:Module` (the package's Becoming/Module.lean) or `record:stem`
  = SENSE [*|N] [note]       the sense read (see SENSES); `*` replaces every occurrence, N expects exactly N
  - old text                 one or more lines: the exact old text (joined by newlines)
  + new text                 one or more lines: the new text

In Lean files the code with comments and strings removed must be identical before and after (statements
unchanged). In records only live fields change: never history, text_versions, references, proof_bindings,
declarations, aliases or ids.
"""
import glob, json, re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PKG = 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming/'
RECORDS = 'theories/becoming/results/records/'
FROZEN = {'history', 'text_versions', 'references', 'proof_bindings', 'declarations', 'aliases', 'id', 'sha256',
          'path', 'schema_version', 'kind', 'family', 'reviewed_at_utc', 'canonical_source', 'source', 'receipt'}

# Each sense: the adopted wording (naming study section 7) and why the old word goes.
SENSES = {
    'S1': ('a map out of the configuration: "registration" → the map, its lumping; "registered course/future/value" → '
           'the course, future or value through the map (row 2)',
           'the theorems use only the map and the partition it induces; no recorder is in the statement'),
    'S2': ('what couples into a formation: "g registers c" → c couples into g, by threshold or by level; '
           '"observed" → coupled by level; "depended on, not observed" → coupled by threshold only (row 1)',
           'a directed coupling of a condition into a formation, of two grains; "registers" adds an observer'),
    'S3': ('histories alike through the couplings: "registers alike" → alike through g\'s couplings (row 3)',
           'an equivalence of histories, not an act of recording'),
    'S4': ('the coupling closure: "registration closure", "within registration" → coupling closure (row 4)',
           'the closure under exchange with a condition coupled into g'),
    'S5': ('the class alike through g: "belief" → the class alike through g; "refutes" (web) → excludes (rows 5–6)',
           '`ClassThrough` is a set of histories; a belief is a mental state the Lean does not contain'),
    'S6': ('a relation respecting claims: "registers" (Likeness) → respects the claims (row 7)',
           'a congruence, unrelated to coupling; one word for two relations is an overload'),
    'S7': ('local senses (row 7′): the value a step keeps (`keeps`, `keepsBit`, `keepsNothing`), the negation\'s course, '
           'the link process, alike on installed addresses, responding through the coupling',
           'each a specific map, process or premise; named after its definition'),
    'L-prefix': ('"record" of a course → prefix (row 8)',
                 '`Learning.prefixOf` is the values before a step; "record" keeps its physical (entropy) sense'),
    'L-extrap': ('"learner", "claim", "prediction rule" → extrapolation; it proposes a value or stays silent (row 9)',
                 'a map from prefixes to a proposed value or silence, not an agent'),
    'L-miss': ('"refuted", "refutation" (learning) → misses, a miss; "holds" → accords (row 10)',
               'a proposed value differs from the value that comes; no dialogue of claim and answer'),
    'L-feature': ('"target" (`val`) → feature of the configuration (row 11)', 'no aim is implied by the Lean'),
    'L-elim': ('"hypotheses" → candidates; "learner by refutation" → extrapolation by elimination (row 12)',
               'a list of candidate extrapolations and the one that moves past each candidate that misses'),
    'L-built': ('"learner given the world" → extrapolation built from the process or from the law (row 13)',
                'the construction uses the start, the listed moves and configurations; "given the world" omits them'),
    'L-fix': ('"identification", "identifies" (Gold sense) → fixing: a bounded prefix fixes the course (section 4)',
              '`IdentifiesAlike` (equating) stays; the Gold sense is a knower naming an object'),
    'L-formation': ('an actual part of the unfolding that comes into accord → "a formation that learns" (row 9 note)',
                    'learning stays a process word; only the noun "learner" goes'),
    'ZH': ('Chinese: 识 at the primitive → 耦合入 / 归并 / 经映射; 学习者 → 外推; 否证 → 不合 (learning) or 排除 (web); '
           '目标 → 特征; 记录 (of a course) → 前段; 假设 (candidates) → 候选; 信念 → 经 g 无别之类',
           'section 7, the zh column; 识 kept only for a formation\'s own course factoring through its own lumping'),
    'ZH-keep': ('识 kept: a formation\'s own further course factors through the lumping its own couplings make',
                'section 7, option (b): the derived structure where differentiation by a part shapes that part\'s course'),
    'NAME': ('identifier proposed for a leftover sense (naming study section 8)', 'see the table of names'),
    'TEXT': ('wording around a changed word (grammar, a sentence that names the new words)',
             'needed for the sentence to read'),
}


# ---------- Lean: comment and code spans ----------

def spans(src):
    i, n, out = 0, len(src), []
    while i < n:
        if src.startswith('/-', i):
            depth, j = 1, i + 2
            while j < n and depth:
                if src.startswith('/-', j):
                    depth, j = depth + 1, j + 2
                elif src.startswith('-/', j):
                    depth, j = depth - 1, j + 2
                else:
                    j += 1
            out.append(('c', i, j)); i = j
        elif src.startswith('--', i):
            j = src.find('\n', i); j = n if j < 0 else j
            out.append(('c', i, j)); i = j
        elif src[i] == '"' and not (i > 0 and src[i - 1] == "'" and src[i + 1:i + 2] == "'"):
            j = i + 1
            while j < n and src[j] != '"':
                j += 2 if src[j] == '\\' else 1
            out.append(('s', i, j + 1)); i = j + 1
        else:
            j = i + 1
            while j < n and not src.startswith('/-', j) and not src.startswith('--', j) and src[j] != '"':
                j += 1
            out.append(('k', i, j)); i = j
    return out


def code_of(src):
    return re.sub(r'\s+', ' ', ''.join(src[a:b] for k, a, b in spans(src) if k == 'k'))


def prose_of(src):
    return [(a, src[a:b]) for k, a, b in spans(src) if k == 'c']


# ---------- edit files ----------

def target_path(t):
    if t.startswith('lean:'):
        return PKG + 'Becoming/' + t[5:].replace('.', '/') + '.lean'
    if t.startswith('record:'):
        return RECORDS + t[7:] + '.json'
    return t


def parse(path):
    blocks, target, cur = [], None, None
    for ln, line in enumerate(Path(path).read_text().split('\n'), 1):
        if line.startswith('### '):
            target, cur = line[4:].strip(), None
        elif line.startswith('= '):
            parts = line[2:].split(None, 2)
            sense, count, note = parts[0], 1, ''
            rest = parts[1:]
            if rest and (rest[0] == '*' or rest[0].isdigit()):
                count = '*' if rest[0] == '*' else int(rest[0]); rest = rest[1:]
            note = ' '.join(rest)
            assert sense == '.' or all(s in SENSES for s in sense.split('+')), f'{path}:{ln}: unknown sense {sense}'
            cur = {'target': target, 'sense': sense, 'count': count, 'note': note, 'old': [], 'new': [],
                   'where': f'{Path(path).name}:{ln}'}
            blocks.append(cur)
        elif line.startswith('- ') or line == '-':
            assert cur is not None and not cur['new'], f'{path}:{ln}: "-" outside a block or after "+"'
            cur['old'].append(line[2:])
        elif line.startswith('+ ') or line == '+':
            assert cur is not None and cur['old'], f'{path}:{ln}: "+" before "-"'
            cur['new'].append(line[2:])
        elif line.strip() and not line.startswith('#'):
            raise SystemExit(f'{path}:{ln}: unreadable line: {line[:60]}')
    for b in blocks:
        b['old'], b['new'] = '\n'.join(b['old']), '\n'.join(b['new'])
        assert b['old'] != b['new'], f"{b['where']}: the block changes nothing"
    return blocks


def detect(old, new):
    """The senses a change carries, read off the words it retires and the words it brings."""
    lo, ln = old.lower(), new.lower()
    gone = lambda w: lo.count(w) > ln.count(w)
    came = lambda w: ln.count(w) > lo.count(w)
    s = []
    if gone('regist') or gone('observ'):
        if came('respects'):
            s.append('S6')
        if came('coupling closure') or came('withincoupling'):
            s.append('S4')
        if came('alike through'):
            s.append('S3')
        if came('couple') or came('coupling'):
            s.append('S2')
        if came('map') or came('lumping'):
            s.append('S1')
        if came('keeps') or came('link process') or came('installed'):
            s.append('S7')
    if gone('belief') or (gone('refut') and came('exclu')):
        s.append('S5')
    if gone('record') and came('prefix'):
        s.append('L-prefix')
    if gone('given the world') or came('built from'):
        s.append('L-built')
    if gone('learner') or gone('claim') or came('propos') or came('extrapolat'):
        s.append('L-extrap')
    if (gone('refut') and came('miss')) or (gone('holds') and came('accord')):
        s.append('L-miss')
    if gone('target') and came('feature'):
        s.append('L-feature')
    if gone('hypothes') or came('candidate') or came('by elimination'):
        s.append('L-elim')
    if gone('identif') and came('fix'):
        s.append('L-fix')
    if any(ord(c) > 0x2e80 for c in old + new) and old != new:
        if any(w in old for w in ('识', '学习者', '否证', '目标', '记录', '假设', '信念', '登记')):
            s.append('ZH')
    return '+'.join(dict.fromkeys(s)) or 'TEXT'


def all_blocks():
    out = []
    for f in sorted(glob.glob(str(HERE / 'edits' / '*.txt'))):
        out += parse(f)
    for b in out:
        if b['sense'] == '.':
            b['sense'] = detect(b['old'], b['new'])
    return out


# ---------- records ----------

def live_strings(d, fn, key=None):
    """Apply fn to every live string of the record; return the new record."""
    if isinstance(d, str):
        return fn(d)
    if isinstance(d, list):
        return [live_strings(v, fn, key) for v in d]
    if isinstance(d, dict):
        return {k: (v if k in FROZEN else live_strings(v, fn, k)) for k, v in d.items()}
    return d


def count_live(d, old):
    n = [0]
    def f(s):
        n[0] += s.count(old); return s
    live_strings(d, f)
    return n[0]


# ---------- commands ----------

def base_text(path, base):
    r = subprocess.run(['git', 'show', f'{base}:{path}'], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def apply(dry=False, base=None):
    """Apply every edit to the base's text of each target (so the pass can be re-run), write the results."""
    if base is None:
        base = subprocess.run(['git', 'merge-base', 'HEAD', 'main'], capture_output=True, text=True).stdout.strip()
    blocks = all_blocks()
    by_target = {}
    for b in blocks:
        by_target.setdefault(target_path(b['target']), []).append(b)
    problems, changed = [], []
    for path, bs in sorted(by_target.items()):
        p = Path(path)
        raw = base_text(path, base)
        if raw is None:
            problems.append(f'{path}: missing at {base}'); continue
        if path.endswith('.json'):
            d = json.loads(raw)
            for b in bs:
                n = count_live(d, b['old'])
                want = n if b['count'] == '*' else b['count']
                if n == 0 or n != want:
                    problems.append(f"{b['where']} {path}: found {n}, expected {b['count']}: {b['old'][:70]!r}")
                    continue
                d = live_strings(d, lambda s, b=b: s.replace(b['old'], b['new']))
            new = json.dumps(d, ensure_ascii=False, indent=2) + '\n'
        else:
            new = raw
            for b in bs:
                n = new.count(b['old'])
                want = n if b['count'] == '*' else b['count']
                if n == 0 or n != want:
                    problems.append(f"{b['where']} {path}: found {n}, expected {b['count']}: {b['old'][:70]!r}")
                    continue
                new = new.replace(b['old'], b['new'])
            if path.endswith('.lean') and code_of(new) != code_of(raw):
                problems.append(f'{path}: an edit reaches code; nothing written'); continue
        if new != raw:
            changed.append(path)
        if not dry and (not p.exists() or p.read_text() != new):
            p.write_text(new)
    print(json.dumps({'blocks': len(blocks), 'files_changed': len(changed), 'problems': problems}, indent=1,
                     ensure_ascii=False))
    return changed, problems


def concord(path, words=r'regist|refut|learner|belief|\brecord|hypothes|target|identif'):
    path = target_path(path)
    src = Path(path).read_text()
    rx = re.compile(words, re.I)
    if path.endswith('.lean'):
        for a, t in prose_of(src):
            if rx.search(t):
                line = src.count('\n', 0, a) + 1
                print(f'--- {line}')
                print(t)
    elif path.endswith('.json'):
        d = json.loads(src)
        def f(s):
            if rx.search(s):
                print('---'); print(s)
            return s
        live_strings(d, f)
    else:
        for i, line in enumerate(src.split('\n'), 1):
            if rx.search(line):
                print(f'--- {i}'); print(line)


def table():
    blocks = all_blocks()
    esc = lambda s: s.replace('|', '\\|').replace('\n', ' ')
    out = ['# N6 reading pass: every change', '',
           'Generated by `reading_pass.py table` from the edit files; each row was written after reading its sentence. '
           'The summary by sense and the reasons are in [PROPOSAL.md](PROPOSAL.md).', '']
    cur = None
    for b in blocks:
        if b['target'] != cur:
            cur = b['target']
            out += ['', f'## `{cur}`', '', '| Current | Proposed | Sense |', '|---|---|---|']
        note = f" ({esc(b['note'])})" if b['note'] else ''
        out.append(f"| {esc(b['old'])} | {esc(b['new'])} | {b['sense']}{note} |")
    (HERE / 'PROPOSAL-FULL.md').write_text('\n'.join(out) + '\n')
    counts = {}
    for b in blocks:
        counts[b['sense']] = counts.get(b['sense'], 0) + 1
    print(json.dumps(counts, indent=1))


def left(words=r'regist|refut|learner|belief'):
    rx = re.compile(words, re.I)
    tot = {}
    for f in sorted(glob.glob(PKG + 'Becoming/*.lean')):
        n = sum(len(rx.findall(t)) for _, t in prose_of(Path(f).read_text()))
        if n:
            tot[Path(f).name] = n
    print(json.dumps(dict(sorted(tot.items(), key=lambda x: -x[1])), indent=0))


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'apply':
        bases = [a[7:] for a in sys.argv if a.startswith('--base=')]
        apply('--dry' in sys.argv, bases[0] if bases else None)
    elif cmd == 'concord':
        concord(*sys.argv[2:])
    elif cmd == 'table':
        table()
    elif cmd == 'left':
        left(*sys.argv[2:])
