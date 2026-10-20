#!/usr/bin/env python3
"""Apply the N1 renaming to a checkout (18 October 2026). Ren chose "Renames, full scope".

usage: python3 -B apply_renames.py TREE [--table-only]

TREE is the root of a checkout (a worktree). The script is deterministic and re-runnable on a fresh tree:
* builds the rename table: the 30 definitions of study section 7, the theorem names the dry run proposed
  (reviewed; overrides in OVERRIDES), and the theorem families named after a renamed definition (EXTRAS);
* renames identifiers in the Becoming package's Lean files: in code, and inside backticks in comments and
  docstrings; prose words are left alone (they change by reading, not substitution);
* writes RENAME-TABLE.json (every old full name -> new full name, read off the declarations before and after)
  beside this script.
Records, the chapter and other text are rewritten by rebind_records.py from that table.
"""
import json, re, sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
TREE = Path(sys.argv[1]).resolve()
PKG = TREE / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
LEAN = sorted((PKG / 'Becoming').glob('*.lean')) + [PKG / 'Becoming.lean']

# Definitions: study section 7. `prefix` is a Lean keyword, so the record of a sequence is `prefixOf`.
DEFS = {
    'Web.Registers': 'Web.CoupledInto', 'Web.RegistersAlike': 'Web.AlikeThrough',
    'Web.RegistersAlikeUpTo': 'Web.AlikeThroughUpTo', 'Web.RegistersAlikeAll': 'Web.AlikeThroughAll',
    'Web.Belief': 'Web.ClassThrough', 'Web.Refutes': 'Web.Excludes', 'Web.RefutesWithin': 'Web.ExcludesWithin',
    'Web.RefutesBy': 'Web.ExcludesBy', 'Flow.RegisteredFrom': 'Flow.CoupledFrom',
    'Flow.WithinRegistration': 'Flow.WithinCoupling', 'Flow.RegisteredFromEither': 'Flow.CoupledFromEither',
    'supportOnly': 'thresholdOnly', 'TimedResponse.RegistersAt': 'TimedResponse.CoupledIntoAt',
    'Registers': 'RespectsClaims', 'Flow.RespondsThroughRegistration': 'Flow.RespondsThroughCoupling',
    'Law.registered': 'Law.frameBy', 'Learning.record': 'Learning.prefixOf', 'Learning.Refuted': 'Learning.Misses',
    'Learning.RefutedAt': 'Learning.MissesAt', 'Learning.Holds': 'Learning.Accords',
    'Learning.learner': 'Learning.byElimination', 'Parting.worldLearner': 'Parting.fromProcess',
    'Learnable.withWorld': 'Learnable.fromLaw', 'Learnable.withWorldAt': 'Learnable.fromLawAt',
    'Viability.Answering.registers': 'Viability.Answering.keeps',
    'Viability.Matching.registered': 'Viability.Matching.keepsBit',
    'Viability.Matching.blind': 'Viability.Matching.keepsNothing', 'Negation.register': 'Negation.course',
    'Revising.registration': 'Revising.linkProcess', 'ReferencePlan.registered': 'ReferencePlan.alikeOnInstalled',
    # Families named after a renamed definition, outside the dry run's token families.
    'recordThen': 'prefixThen', 'Learning.decRefuted': 'Learning.decMisses',
    'Learning.decRefutedAt': 'Learning.decMissesAt',
}
# Theorem names the dry run proposed, where review changed the proposal.
OVERRIDES = {
    'Viability.Matching.registered_kept': 'Viability.Matching.keepsBit_kept',
    'Viability.Matching.registration_matters': 'Viability.Matching.keeping_matters',
    'LearningRuns.determines_iff_registered_alike': 'LearningRuns.determines_iff_lumped_alike',
}
# Theorem families of renamed definitions that the dry run's token families did not reach (by last component).
EXTRAS = {
    'registered_across_exact': 'frameBy_across_exact', 'registered_within_exact': 'frameBy_within_exact',
    'residual_registers_nothing': 'residual_couples_nothing', 'blind_not_kept': 'keepsNothing_not_kept',
    'alike_registers': 'alike_respectsClaims', 'alikeTo_registered_iff': 'alikeTo_frameBy_iff',
    'respondsThroughRegistration_withhold': 'respondsThroughCoupling_withhold',
    'least_registration': 'least_coupling', 'tailLaw_no_least_registration': 'tailLaw_no_least_coupling',
    'wholeLaw_no_least_registration': 'wholeLaw_no_least_coupling', 'tail_unrefuted': 'tail_unexcluded',
    'unrefuted_beyond_registration': 'unexcluded_beyond_coupling', 'registered_determined': 'frameBy_determined',
    'fits_of_unrefuted': 'fits_of_no_miss', 'unrefuted_persists': 'no_miss_persists',
    'unrefuted_of': 'not_missed_of',
}
EXTRA_MODULES = {'Distinguishing', 'FallibleInquiry', 'Keeping', 'Likeness', 'Response', 'Sensitivity', 'Tail',
                 'Testing', 'Unfolding', 'Identification'}
# Last components too common to rename wherever they stand bare: bare uses are renamed only in the files below.
SCOPED_BARE = {
    'record': ('Learning',), 'learner': ('Learning',), 'Holds': ('Learning',), 'Refuted': ('Learning',),
    'RefutedAt': ('Learning',), 'Registers': (), 'registered': (), 'registers': (), 'blind': (),
    'register': ('Negation',), 'registration': ('Revising',), 'Belief': ('Web',), 'Refutes': ('Web',),
}

DECL = re.compile(r"^\s*(?:@\[[^\]]*\]\s*)?(?:noncomputable\s+|private\s+|protected\s+)*"
                  r"(theorem|def|abbrev|structure|inductive|instance|class)\s+([A-Za-z0-9_.'?!]+)", re.M)
NS = re.compile(r'^\s*(namespace|end)\s+([A-Za-z0-9_.]+)\s*$', re.M)
OPEN = re.compile(r'^\s*open\s+([^\n]*)$', re.M)
IDENT = re.compile(r"(?<![A-Za-z0-9_'!?])\.?[A-Za-z_][A-Za-z0-9_'!?]*(?:\.[A-Za-z_][A-Za-z0-9_'!?]*)*")


def declarations(text):
    events = sorted([(m.start(), 'ns', m) for m in NS.finditer(text)] +
                    [(m.start(), 'decl', m) for m in DECL.finditer(text)], key=lambda e: e[0])
    stack, out = [], []
    for _, kind, m in events:
        if kind == 'ns':
            if m.group(1) == 'namespace':
                stack.append(m.group(2))
            elif stack and stack[-1] == m.group(2):
                stack.pop()
        else:
            name = '.'.join(stack + [m.group(2)])
            while name.startswith('Becoming.'):
                name = name[len('Becoming.'):]
            out.append((m.group(1), name))
    return out


def table():
    dry = json.loads((HERE / 'MIGRATION-DRY-RUN.json').read_text())
    ren = dict(DEFS)
    for e in dry['entries']:
        if e['how'].startswith('theorem'):
            ren[e['name']] = OVERRIDES.get(e['name'], e['new'])
    for p in LEAN:
        if p.stem in EXTRA_MODULES:
            for kind, name in declarations(p.read_text()):
                last = name.rsplit('.', 1)[-1]
                if kind in ('theorem', 'instance') and last in EXTRAS:
                    ren[name] = name[:len(name) - len(last)] + EXTRAS[last]
    return ren


ren = table()
# Component maps. A window of at least two components (or one, prefixed by Becoming) matching an old name's
# tail renames its last component; a last component that is unique to renamed declarations renames anywhere.
all_decls = {p: declarations(p.read_text()) for p in LEAN}
by_last = defaultdict(set)
for decls in all_decls.values():
    for _, name in decls:
        by_last[name.rsplit('.', 1)[-1]].add(name)
windows = {}
for old, new in ren.items():
    o, n = old.split('.'), new.split('.')
    assert len(o) == len(n), (old, new)
    for k in range(2, len(o) + 1):
        windows[tuple(o[-k:])] = n[-k:]
    windows[('Becoming',) + tuple(o)] = ['Becoming'] + n
comp = defaultdict(set)
for old, new in ren.items():
    comp[old.rsplit('.', 1)[-1]].add(new.rsplit('.', 1)[-1])
GLOBAL, conflicts = {}, []
for c, news in comp.items():
    if c in SCOPED_BARE or news == {c}:
        continue
    others = [d for d in by_last[c] if d not in ren]
    if len(news) == 1 and not others:
        GLOBAL[c] = next(iter(news))
    else:
        conflicts.append((c, sorted(news), others))
# Dot uses (after a value, such as `W.Registers`) of the Web definitions and of every global component.
DOT = dict(GLOBAL)
for c in ('Registers', 'RegistersAlike', 'RegistersAlikeUpTo', 'RegistersAlikeAll', 'Belief', 'Refutes',
          'RefutesWithin', 'RefutesBy'):
    DOT[c] = ren['Web.' + c].rsplit('.', 1)[-1]
for c in ('RegisteredFrom', 'WithinRegistration', 'RegisteredFromEither', 'RespondsThroughRegistration'):
    DOT[c] = ren['Flow.' + c].rsplit('.', 1)[-1]


def bare_scope(path, text):
    """Bare common components renamed in this file, by the namespaces it is in or opens."""
    spaces = {m.group(2).split('.')[-1] for m in NS.finditer(text) if m.group(1) == 'namespace'}
    spaces |= {n.split('.')[-1] for m in OPEN.finditer(text) for n in m.group(1).split()}
    out = {}
    for c, owners in SCOPED_BARE.items():
        for old, new in ren.items():
            parts = old.split('.')
            if parts[-1] != c:
                continue
            owner = parts[-2] if len(parts) > 1 else None
            if owner and owner in spaces and (not owners or owner in owners or path.stem in MANUAL.get(c, {})):
                out[c] = new.rsplit('.', 1)[-1]
            if owner is None and path.stem in MANUAL.get(c, {}):
                out[c] = new
    for c, files in MANUAL.items():
        if path.stem in files and files[path.stem]:
            out[c] = files[path.stem]
    return out


# Bare uses decided by reading the file (file stem -> new component).
MANUAL = {
    'Registers': {'Testing': 'CoupledInto', 'Likeness': 'RespectsClaims'},
    'registered': {'Keeping': 'keepsBit', 'ReferencePlan': 'alikeOnInstalled'},
    'registers': {'Keeping': 'keeps'},
    'blind': {'Keeping': 'keepsNothing'},
}


def rename_ident(tok, bare):
    lead = tok.startswith('.')
    c = tok[1:].split('.') if lead else tok.split('.')
    out = list(c)
    for i in range(len(c)):
        done = False
        for k in range(min(i + 1, 5), 0, -1):
            w = tuple(c[i - k + 1:i + 1])
            if w in windows and (k >= 2 or w[0] == 'Becoming'):
                out[i - k + 1:i + 1] = windows[w]
                done = True
                break
        if done:
            continue
        first = i == 0 and not lead
        if first:
            if c[i] in GLOBAL:
                out[i] = GLOBAL[c[i]]
            elif c[i] in bare:
                out[i] = bare[c[i]]
        elif c[i] in DOT:
            out[i] = DOT[c[i]]
    s = '.'.join(out)
    return '.' + s if lead else s


def segments(text):
    """(kind, start, end): code, comment or string."""
    i, n, out, start = 0, len(text), [], 0
    while i < n:
        if text.startswith('--', i):
            out.append(('code', start, i)); j = text.find('\n', i); j = n if j < 0 else j
            out.append(('comment', i, j)); i = start = j
        elif text.startswith('/-', i):
            out.append(('code', start, i)); depth, j = 1, i + 2
            while j < n and depth:
                if text.startswith('/-', j):
                    depth += 1; j += 2
                elif text.startswith('-/', j):
                    depth -= 1; j += 2
                else:
                    j += 1
            out.append(('comment', i, j)); i = start = j
        elif text[i] == '"':
            out.append(('code', start, i)); j = i + 1
            while j < n and text[j] != '"':
                j += 2 if text[j] == '\\' else 1
            out.append(('string', i, j + 1)); i = start = j + 1
        else:
            i += 1
    out.append(('code', start, n))
    return out


def rewrite(text, bare):
    sub = lambda s: IDENT.sub(lambda m: rename_ident(m.group(0), bare), s)
    parts = []
    for kind, a, b in segments(text):
        s = text[a:b]
        if kind == 'code':
            parts.append(sub(s))
        elif kind == 'comment':
            parts.append(re.sub(r'`([^`\n]+)`', lambda m: '`' + sub(m.group(1)) + '`', s))
        else:
            parts.append(s)
    return ''.join(parts)


if __name__ == '__main__':
    if '--table-only' not in sys.argv:
        for p in LEAN:
            t = p.read_text()
            new = rewrite(t, bare_scope(p, t))
            if new != t:
                p.write_text(new)
    after = {p: declarations(p.read_text()) for p in LEAN}
    full = {}
    for p in LEAN:
        before, now = all_decls[p], after[p]
        assert len(before) == len(now), p
        for (_, a), (_, b) in zip(before, now):
            if a != b:
                full['Becoming.' + a] = 'Becoming.' + b
    news = defaultdict(list)
    for a, b in full.items():
        news[b].append(a)
    clash = {b: a for b, a in news.items() if len(a) > 1}
    (HERE / 'RENAME-TABLE.json').write_text(json.dumps(
        {'renamed': full, 'global_components': GLOBAL, 'conflicts_kept_scoped': conflicts, 'clashes': clash},
        ensure_ascii=False, indent=1) + '\n')
    print(json.dumps({'table': len(ren), 'declarations_renamed': len(full), 'global': len(GLOBAL),
                      'conflicts': conflicts, 'clashes': clash}, ensure_ascii=False, indent=1))
