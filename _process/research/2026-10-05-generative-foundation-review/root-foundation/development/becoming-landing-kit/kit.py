"""Shared helpers for landing new core modules of the Becoming spine in one checker run.

A run directory holds `config.py` (the run's text and choices) and refers to the packages it lands
(`development/becoming-pNN-landing/`). The steps, each a script in this kit:

1. `land_lean.py RUN W`: copy the modules, register them in the root module, the checker's CORE and
   scope, and the Lean README.
2. the checkers (core, periphery) and the decidability inventory, by hand, one run at a time;
3. `land_docs.py RUN W S`: the study sections from S on with their English blocks, the unification
   plan, the chapter edits, the totals and the reading entry, from the receipts;
4. `make_records.py RUN W REVIEWED S`: the new records, completed from the packages' drafts, then
   each package's record deltas;
5. P69's `repoint.py`, the render pipeline and the link check, as in P69's landing.

Every anchor must occur exactly once; rerunning a step on a checkout it already changed fails.
"""
import hashlib
import importlib.util
import json
import re
from pathlib import Path

RF = '_process/research/2026-10-05-generative-foundation-review/root-foundation'
DEV = f'{RF}/development'
L = 'experiments/integrated-correction/general-framework/generative-basis/lean'
D = f'{L}/becoming'
RECEIPT = f'{D}/becoming-verification.json'
PERI_RECEIPT = f'{L}/universal-ethics/generative-capacity/correction-inquiry-verification.json'
STUDY = f'{RF}/BECOMING-RENEWAL-READING.md'
PLAN = f'{RF}/BECOMING-UNIFICATION-PLAN.md'
CHAPTER = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'
RECORDS = 'theories/becoming/results/records'


def load_config(run_dir):
    spec = importlib.util.spec_from_file_location('config', Path(run_dir) / 'config.py')
    config = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(config)
    return config


def lean(module):
    return f'{D}/Becoming/{module}.lean'


def source(module):
    """The source of a receipt module: `Becoming.X` under the package, the foundation (`GenerativeCore`, ...) beside it."""
    return lean(module.removeprefix('Becoming.')) if module.startswith('Becoming.') else f'{L}/{module}.lean'


def edit(root, path, pairs):
    p = Path(root) / path
    s = p.read_text()
    for a, b in pairs:
        assert s.count(a) == 1, (path, a[:80], s.count(a))
        s = s.replace(a, b)
    p.write_text(s)
    print('edited', path)


def line_start(s, prefix, last=False):
    starts = [i for i in range(len(s)) if (i == 0 or s[i - 1] == '\n') and s.startswith(prefix, i)]
    assert len(starts) == 1 or (last and starts), (prefix[:80], len(starts))
    return starts[-1]


def insert_before_line(s, prefix, text, blank, last=False):
    i = line_start(s, prefix, last)
    return s[:i] + text + ('\n\n' if blank else '\n') + s[i:]


def insert_after_line(s, prefix, text, last=False):
    i = line_start(s, prefix, last)
    j = s.index('\n', i) + 1
    return s[:j] + text + '\n' + s[j:]


def anchor(heading):
    """The anchor GitHub gives a heading: lower case, punctuation dropped, spaces as hyphens."""
    text = heading.lstrip('#').strip().lower()
    return re.sub(r'[^\w\- ]', '', text).replace(' ', '-')


class Receipts:
    def __init__(self, root):
        root = Path(root)
        self.receipt = json.loads((root / RECEIPT).read_text())
        self.periphery = json.loads((root / PERI_RECEIPT).read_text())
        assert self.receipt['status'] == self.periphery['status'] == 'passed'
        self.modules = {m['module']: m for m in self.receipt['modules']}
        spine = [m for m in self.receipt['modules'] if m['spine']]
        self.n_thm = sum(m['theorems'] for m in spine)
        self.n_decl = sum(len(m['declarations']) for m in spine)
        self.n_pkg = len(spine)
        self.n_core = len(self.receipt['core_closure'])
        self.n_inh = len(self.receipt['inherited_receipts'])
        self.run = self.receipt['utc']
        self.peri_run = self.periphery['utc']
        self.owner = {n: m for m in self.modules for n in self.names(m)}

    def names(self, module):
        return [d['name'] if isinstance(d, dict) else d for d in self.modules[module]['declarations']]

    def theorems(self, module):
        return self.modules[f'Becoming.{module}']['theorems']


def scope_lines(text):
    """The checker's scope as string-literal lines: four spaces of indent, at most about 100 columns,
    each piece ending in a space so the pieces join into the text with a space after it."""
    words, lines, cur = text.split(' '), [], ''
    for w in words:
        if cur and len(cur) + 1 + len(w) > 92:
            lines.append(cur + ' ')
            cur = w
        else:
            cur = f'{cur} {w}' if cur else w
    lines.append(cur + ' ')
    return ''.join('    "' + x.replace('\\', '\\\\').replace('"', '\\"') + '"\n' for x in lines)


def sha(root, path):
    return hashlib.sha256((Path(root) / path).read_bytes()).hexdigest()


def cited(text, receipts):
    """Declarations of the receipt named in a text, as `Becoming.`-less tokens (`Flow.foo`, `foo`)."""
    found = []
    for token in re.findall(r'[A-Za-z_][A-Za-z0-9_.]*[A-Za-z0-9_]', text):
        name = 'Becoming.' + token
        if name in receipts.owner and name not in found:
            found.append(name)
    return found


def declared(path):
    """The full names of a Lean file's declarations, each with the `/-! ## ...` section it lies in, read from the
    text (namespace, section and end tracked). make_records checks them against the receipt."""
    stack, out, heading = [], {}, ''
    for line in Path(path).read_text().split('\n'):
        if line.startswith('/-! #'):
            heading = line.lstrip('/-! #').removesuffix('-/').strip()
            continue
        m = re.match(r'^(namespace|section)(\s+(\S+))?\s*$', line)
        if m:
            stack.append((m.group(1), m.group(3) or ''))
            continue
        if re.match(r'^end(\s+\S+)?\s*$', line):
            stack.pop()
            continue
        m = re.match(r'^(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+|noncomputable\s+)*'
                     r'(theorem|lemma|def|structure|inductive|abbrev|instance|class)\s+([^\s:({\[]+)', line)
        if m:
            ns = '.'.join(n for k, n in stack if k == 'namespace')
            out[f'{ns}.{m.group(2)}' if ns else m.group(2)] = heading
    return out
