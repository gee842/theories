#!/usr/bin/env python3
"""Dry run of the N1 renaming: what would change, where, and what needs a decision (18 October 2026).

usage (from the repository root):
  python3 -B _process/research/2026-10-05-generative-foundation-review/root-foundation/development/n1-migration/migration_dry_run.py

Reads the canonical Lean files of the Becoming package (not the check receipts), the result records, the canonical
chapter and the live Markdown, and writes MIGRATION-DRY-RUN.json and MIGRATION-DRY-RUN.md beside this script.
Changes no other file. The adopted vocabulary is study section 7 of REGISTRATION-VOCABULARY-STUDY.md
(Ren, 18 October 2026: "Agree with the candidates as proposed and with 识 option (b) ... still no renames").

Two kinds of entry:
* definitions, renamed by the explicit table DEFS (each new name chosen by hand from study section 7);
* theorems whose names carry an old word in its learning or registration sense, with a proposed name made by token
  substitution by the sense of the module family (WEB_TOKENS: coupling and exclusion; LEARNING_TOKENS: prefix,
  miss, accord, elimination) and marked for review; the logical sense of "unrefuted" and "refutable" (a double
  negation, P58b) is left out (KEEP), and modules outside the two families (Experiment's record) are not touched.
"""
import json, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
PKG = ROOT / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
LEAN = sorted((PKG / 'Becoming').glob('*.lean')) + [PKG / 'Becoming.lean']

# Definitions: (module, old full name) -> new full name.
DEFS = {
    ('Testing', 'Web.Registers'): 'Web.CoupledInto',
    ('Testing', 'Web.RegistersAlike'): 'Web.AlikeThrough',
    ('Testing', 'Web.RegistersAlikeUpTo'): 'Web.AlikeThroughUpTo',
    ('Testing', 'Web.RegistersAlikeAll'): 'Web.AlikeThroughAll',
    ('Testing', 'Web.Belief'): 'Web.ClassThrough',
    ('Testing', 'Web.Refutes'): 'Web.Excludes',
    ('Testing', 'Web.RefutesWithin'): 'Web.ExcludesWithin',
    ('Testing', 'Web.RefutesBy'): 'Web.ExcludesBy',
    ('Testing', 'Flow.RegisteredFrom'): 'Flow.CoupledFrom',
    ('Testing', 'Flow.WithinRegistration'): 'Flow.WithinCoupling',
    ('Testing', 'Flow.RegisteredFromEither'): 'Flow.CoupledFromEither',
    ('Testing', 'supportOnly'): 'thresholdOnly',
    ('TimedResponse', 'TimedResponse.RegistersAt'): 'TimedResponse.CoupledIntoAt',
    ('Likeness', 'Registers'): 'RespectsClaims',
    ('Response', 'Flow.RespondsThroughRegistration'): 'Flow.RespondsThroughCoupling',
    ('Unfolding', 'Law.registered'): 'Law.frameBy',
    ('Learning', 'Learning.record'): 'Learning.prefix',
    ('Learning', 'Learning.Refuted'): 'Learning.Misses',
    ('Learning', 'Learning.RefutedAt'): 'Learning.MissesAt',
    ('Learning', 'Learning.Holds'): 'Learning.Accords',
    ('Learning', 'Learning.learner'): 'Learning.byElimination',
    ('Parting', 'Parting.worldLearner'): 'Parting.fromProcess',
    ('Learnable', 'Learnable.withWorld'): 'Learnable.fromLaw',
    ('Learnable', 'Learnable.withWorldAt'): 'Learnable.fromLawAt',
    ('Keeping', 'Viability.Answering.registers'): 'Viability.Answering.keeps',
    ('Keeping', 'Viability.Matching.registered'): 'Viability.Matching.keepsBit',
    ('Keeping', 'Viability.Matching.blind'): 'Viability.Matching.keepsNothing',
    ('Description', 'Negation.register'): 'Negation.course',
    ('Revision', 'Revising.registration'): 'Revising.linkProcess',
    ('ReferencePlan', 'ReferencePlan.registered'): 'ReferencePlan.alikeOnInstalled',
}

# Token substitutions proposed for theorem names, by the sense the module family uses.
WEB_TOKENS = [
    ('registersAt_registers', 'coupledIntoAt_coupledInto'),
    ('withinRegistration', 'withinCoupling'), ('WithinRegistration', 'WithinCoupling'),
    ('RespondsThroughRegistration', 'RespondsThroughCoupling'),
    ('registersAlike', 'alikeThrough'), ('RegistersAlike', 'AlikeThrough'),
    ('registeredFrom', 'coupledFrom'), ('RegisteredFrom', 'CoupledFrom'),
    ('unregistered', 'uncoupled'), ('registered', 'coupled'), ('registers', 'couples'),
    ('Registers', 'CoupledInto'), ('belief', 'class'), ('Belief', 'Class'),
    ('refutes', 'excludes'), ('Refutes', 'Excludes'), ('refuted', 'excluded'),
    ('registersAt', 'coupledIntoAt'), ('registration', 'coupling'), ('supportOnly', 'thresholdOnly'),
]
LEARNING_TOKENS = [
    ('worldLearner', 'fromProcess'), ('learner', 'byElimination'), ('Learner', 'ByElimination'),
    ('refutes', 'misses'), ('refuted', 'missed'), ('Refuted', 'Missed'), ('refutations', 'misses'),
    ('registered_alike', 'alike_through_map'), ('registered', 'mapped'), ('register', 'course'),
    ('records', 'prefixes'), ('record', 'prefix'), ('holds', 'accords'),
]
WEB = {'Testing', 'Selection', 'Response', 'TimedResponse', 'Runaway', 'Counterfactual', 'Thresholds',
       'Observation', 'LevelCoupling', 'Seeking', 'Capture', 'Feedback', 'SelectionRuns', 'Keeping'}
LEARNING = {'Learning', 'Learnable', 'Identification', 'Parting', 'LearnableRuns', 'IdentificationRuns',
            'LearningRuns', 'Sensitivity', 'Tail', 'Description'}
SCOPE = WEB | LEARNING
# Words kept: the logical sense (P58b "unrefuted", Horizon.Refutable) and Experiment's record.
KEEP = re.compile(r'unrefuted|Unrefuted|[Rr]efutable')

DECL = re.compile(r"^\s*(?:@\[[^\]]*\]\s*)?(?:noncomputable\s+|private\s+|protected\s+)*"
                  r"(theorem|def|abbrev|structure|inductive|instance|class)\s+([A-Za-z0-9_.'?!]+)", re.M)
NS = re.compile(r'^\s*(namespace|end)\s+([A-Za-z0-9_.]+)\s*$', re.M)


def declarations(path):
    """(kind, full name without the Becoming prefix, line) for each declaration, tracking namespaces."""
    text = path.read_text()
    events = sorted([(m.start(), 'ns', m) for m in NS.finditer(text)] + [(m.start(), 'decl', m) for m in DECL.finditer(text)],
                    key=lambda e: e[0])
    stack, out = [], []
    for pos, kind, m in events:
        if kind == 'ns':
            if m.group(1) == 'namespace':
                stack.append(m.group(2))
            elif stack and stack[-1] == m.group(2):
                stack.pop()
        else:
            name = '.'.join(stack + [m.group(2)])
            while name.startswith('Becoming.'):
                name = name[len('Becoming.'):]
            out.append((m.group(1), name, text.count('\n', 0, pos) + 1))
    return out


def substitute(name, module):
    new = name
    for old, rep in (LEARNING_TOKENS if module in LEARNING else WEB_TOKENS):
        new = new.replace(old, rep)
    return new


def last(name):
    return name.rsplit('.', 1)[-1]


corpus = {p: p.read_text() for p in LEAN}
records = sorted((ROOT / 'theories/becoming/results/records').glob('*.json'))
rec_text = {p: p.read_text() for p in records}
chapter = (ROOT / 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md').read_text()


def uses(name):
    word = re.compile(r'(?<![A-Za-z0-9_.])(?:Becoming\.)?' + re.escape(name) + r'(?![A-Za-z0-9_])')
    tail = re.compile(r'(?<![A-Za-z0-9_])' + re.escape(last(name)) + r'(?![A-Za-z0-9_])')
    lean_files = sorted({p.name for p, t in corpus.items() if tail.search(t)})
    recs = sorted(p.stem for p, t in rec_text.items() if word.search(t))
    return {'lean_files': len(lean_files), 'lean_file_names': lean_files[:12], 'records': len(recs),
            'record_ids': recs[:12], 'chapter': len(word.findall(chapter))}


entries, taken = [], set()
for p in LEAN:
    module = p.stem
    for kind, name, line in declarations(p):
        taken.add(name)
for p in LEAN:
    module = p.stem
    for kind, name, line in declarations(p):
        new, how = None, None
        if (module, name) in DEFS:
            new, how = DEFS[(module, name)], 'definition (study section 7)'
        elif module in SCOPE and kind == 'theorem' and not KEEP.search(last(name)):
            cand = substitute(name, module)
            if cand != name:
                new, how = cand, 'theorem name, token substitution (review)'
        if new:
            entries.append({'module': module, 'kind': kind, 'name': name, 'new': new, 'how': how, 'line': line,
                            'clash': new in taken, **uses(name)})

missing = [f'{m}:{n}' for (m, n) in DEFS if not any(e['module'] == m and e['name'] == n for e in entries)]
defs = [e for e in entries if e['how'].startswith('definition')]
thms = [e for e in entries if not e['how'].startswith('definition')]
summary = {
    'definitions': len(defs), 'theorem_names': len(thms), 'clashes': [e['name'] for e in entries if e['clash']],
    'definitions_not_found': missing,
    'lean_files_touched': len({f for e in entries for f in e['lean_file_names']}),
    'records_touched': len({r for e in entries for r in e['record_ids']}),
}
(HERE / 'MIGRATION-DRY-RUN.json').write_text(json.dumps({'summary': summary, 'entries': entries}, ensure_ascii=False,
                                                         indent=1) + '\n')

md = ['# N1 migration: dry run', '',
      'Generated by [migration_dry_run.py](migration_dry_run.py) on the current checkout; it changes no file. '
      'Adopted vocabulary: [study section 7](../../REGISTRATION-VOCABULARY-STUDY.md#7-decisions-18-october-2026). '
      'Nothing here is applied: Ren\'s instruction of 18 October was "still no renames".', '',
      f"Definitions: {summary['definitions']}. Theorem names with a proposed substitution (to review): "
      f"{summary['theorem_names']}. Clashes with an existing name: {len(summary['clashes'])}. "
      f"Definitions in the table not found: {len(missing)}.", '',
      '## Definitions', '', '| Module | Kind | Current | Adopted | Lean files | Records | Chapter |', '|---|---|---|---|---|---|---|']
for e in defs:
    md.append(f"| {e['module']} | {e['kind']} | `{e['name']}` | `{e['new']}`{' (clash)' if e['clash'] else ''} | "
              f"{e['lean_files']} | {e['records']} | {e['chapter']} |")
md += ['', '## Theorem names (proposed by substitution; each needs review)', '',
       '| Module | Current | Proposed | Lean files | Records |', '|---|---|---|---|---|']
for e in thms:
    md.append(f"| {e['module']} | `{e['name']}` | `{e['new']}`{' (clash)' if e['clash'] else ''} | {e['lean_files']} | {e['records']} |")
if missing:
    md += ['', '## Not found', ''] + [f'- `{m}`' for m in missing]
(HERE / 'MIGRATION-DRY-RUN.md').write_text('\n'.join(md) + '\n')
print(json.dumps(summary, ensure_ascii=False, indent=1))
