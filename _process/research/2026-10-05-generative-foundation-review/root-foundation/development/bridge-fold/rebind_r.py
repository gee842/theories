#!/usr/bin/env python3
"""F3R (18 October 2026): rebind the records whose proofs cite the family to its core statements.

usage (from the checkout root): python3 -B rebind_r.py RECEIPT_ID [MODULE ...]

RECEIPT_ID is the passing core receipt in this checkout; MODULE limits the run to records citing
those periphery modules (default: every module of `port_r.FAMILY` and its joins). A port is not
a new result: claims are unchanged. For every record with a proof reference to a family file:
* each cited declaration with a core counterpart in `port_r.py` (or in the definition and join
  tables below) gains that counterpart in a proof reference to the core source that elaborates it
  (added, with the source's hash, where the record had none), and in every law listing the
  declaration, right after it; the periphery reference stays until the sweep retires the module;
* the canonical source moves to the core source holding most of the counterparts, where it was a
  family file;
* a proof binding to the receipt is added for each core source gained that had none, with the
  receipt as a reference;
* a history note names F3R and says what was added.
"""
import glob
import hashlib
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import port_r  # noqa: E402

RID = sys.argv[1]
ONLY = set(sys.argv[2:])
LEAN = 'experiments/integrated-correction/general-framework/generative-basis/lean/'
PKG = LEAN + 'becoming/'
RECEIPT = PKG + 'becoming-checks/' + RID + '/verification.json'
receipt = json.load(open(RECEIPT))
assert receipt['status'] == 'passed', receipt['status']
path_of = {m: LEAN + p for m, p in receipt['source_paths'].items()}
module_of = {p: m for m, p in path_of.items()}
home = {}
for m in receipt.get('modules', []):
    for d in m.get('declarations', []):
        if isinstance(d, dict):
            home.setdefault(d['name'], m['module'])

MC = 'Becoming.MatchedCourses.'
DEFS = {
    'Becoming.RepairComparison': {
        'Repair': MC + 'Move', 'Life': MC + 'Position', 'Claim': MC + 'Claim', 'State': MC + 'State',
        'start': MC + 'start', 'backboneAfter': MC + 'baseAfter', 'advance': MC + 'advance',
        'process': MC + 'process', 'states': MC + 'states', 'run': MC + 'run', 'episodeTime': MC + 'time',
        'lifeOf': MC + 'positionOf', 'protects': MC + 'covers', 'frame': MC + 'frame',
        'decidableRealized': MC + 'decidableRealized', 'outageAt': MC + 'gapAt',
        'firstEpisodeOf': MC + 'firstClaimOf', 'availableNow': MC + 'supportedAt', 'supportedNow': MC + 'Supported',
        'decidableSupportedNow': MC + 'decidableSupported', 'finalState': MC + 'final',
        'sameEpisode': MC + 'BasicAlike', 'toB1': MC + 'matchB1', 'toA': MC + 'matchA', 'swapB2': MC + 'swapB2',
        'SufficientMatching': 'Becoming.Frame.SufficientMatching', 'allClaims': MC + 'allClaims',
        'lostCount': MC + 'lostCount'},
    'GenerativeLossComparison': {n: 'Becoming.StrictTransport.' + n for n in ('Strict', 'Transitive', 'Compatible')}
    | {'PracticalBridge': 'Becoming.StrictTransport.SuppliesReason'},
    'RenewalComparison': {'relationalInventory': 'Becoming.Ranking.wholeRun',
                          'broadInventory': 'Becoming.ActiveReading.active',
                          'undisturbed': 'Becoming.Ranking.undisturbed', 'absent': 'Becoming.Ranking.absent',
                          'course': 'Becoming.Ranking.course', 'contest': 'Becoming.Ranking.contest',
                          'preferOccurs': 'Becoming.Ranking.preferOccurs'},
    'RenewalRecovery': {'pulse': 'Becoming.SupportRecovery.pulse'},
}
JOIN_FILES = {
    'Becoming.Instances': {
        'assured_iff_completes': ['Becoming.AssurancePlans.Routes.completes_iff'],
        'routes_assured_iff': ['Becoming.AssurancePlans.Routes.completes_iff'],
        'regulation_assured_iff': ['Becoming.AssurancePlans.Regulation.kept_along'],
        'diagonal_no_decoder': ['Becoming.Dephasing.no_diagonal_response_decoder'],
        'dephase_no_restore': ['Becoming.Dephasing.no_uniform_dephase_inverse'],
        'local_pair_no_update': ['Becoming.JointPhase.no_local_pair_update'],
        'local_pair_carries_no_law': ['Becoming.JointPhase.local_pair_carries_no_law'],
    },
    'Becoming.RenewalBridge': {
        'pulse_restores': ['Becoming.SupportGated.repair_restores', 'Becoming.SupportRecovery.pulse_levels'],
        'overdraw_extension': ['Becoming.Ranking.whole_run_extends'],
        'contest_extensions': ['Becoming.ActiveReading.contest_readings'],
    },
}


def table(module):
    """Short name -> core counterparts, for one family or join module."""
    if module in JOIN_FILES:
        return JOIN_FILES[module]
    out = {k: [v] for k, v in DEFS.get(module, {}).items()}
    for old, _, after, counterpart, _ in port_r.FAMILY[module]['rows']:
        if after in ('same', 'step') and counterpart != '—':
            out[old] = [c if c.startswith(('Becoming.', 'Generative.', 'RelationalRenewal.')) else
                        counterpart.split(', ')[0].rsplit('.', 1)[0] + '.' + c for c in counterpart.split(', ')]
    return out


FAMILY_PATHS = {}
for name, d in port_r.FAMILY.items():
    FAMILY_PATHS[LEAN + d['path']] = name
for name in JOIN_FILES:
    FAMILY_PATHS[path_of[name]] = name
if ONLY:
    FAMILY_PATHS = {p: n for p, n in FAMILY_PATHS.items() if n in ONLY}

h = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()


def binding(src):
    return {'source': src, 'receipt': RECEIPT, 'sha256_pointer': '/source_sha256/' + module_of[src],
            'success_pointer': '/status', 'success_value': 'passed'}


summary = []
for f in sorted(glob.glob('theories/becoming/results/records/*.json')):
    d = json.load(open(f))
    before = json.dumps(d, ensure_ascii=False)
    refs = d.get('references', [])
    by_path = {r['path']: r for r in refs}
    added = {}            # core source -> new names
    new_of = {}           # old full name -> new full names
    from_canonical = []
    for r in list(refs):
        if r.get('role') != 'proof' or r['path'] not in FAMILY_PATHS or not r.get('declarations'):
            continue
        tab = table(FAMILY_PATHS[r['path']])
        for name in r['declarations']:
            news = tab.get(name.rsplit('.', 1)[-1])
            if not news:
                continue
            for new in news:
                mod = home.get(new)
                assert mod in path_of, (f, name, new)
                src = path_of[mod]
                if src not in by_path:
                    by_path[src] = {'path': src, 'role': 'proof', 'sha256': h(src), 'declarations': []}
                    refs.insert(refs.index(r) + 1, by_path[src])
                if new not in by_path[src]['declarations']:
                    by_path[src]['declarations'].append(new)
                added.setdefault(src, []).append(new)
                new_of.setdefault(name, []).append(new)
                if d.get('canonical_source') == r['path']:
                    from_canonical.append(src)
    if not added:
        continue
    for law in d.get('laws', []):
        decls = law.get('declarations', [])
        out = []
        for n in decls:
            out.append(n)
            out += [m for m in new_of.get(n, []) if m not in decls and m not in out]
        law['declarations'] = out
    if from_canonical:
        d['canonical_source'] = max(set(from_canonical), key=from_canonical.count)
    if d.get('proof_bindings') is not None:
        bound = {b['source'] for b in d['proof_bindings']}
        for src in added:
            if src not in bound:
                d['proof_bindings'].append(binding(src))
        if RECEIPT not in by_path:
            refs.append({'path': RECEIPT, 'role': 'receipt', 'sha256': h(RECEIPT), 'declarations': []})
    for src in added:
        by_path[src]['sha256'] = h(src)
    if json.dumps(d, ensure_ascii=False) == before:
        continue
    mods = sorted({module_of[s].split('.', 1)[-1] for s in added})
    note = ('19 October 2026, F3R, the port of the renewal, loss, systems and wisdom family into the core (Ren: '
            '"work with other sessions, totally resolve these extra/ugly bridges, and move toward to the direction '
            'of unification"): the core statements of the cited declarations are added beside them ('
            + ', '.join(mods) + '; verdicts in port-r.md), bound to core receipt ' + RID
            + (', and the canonical source is the core module' if from_canonical else '')
            + '. The periphery references stay until the sweep retires their modules. No new result; the claim is '
              'unchanged.')
    d['history'].append({'en': note, 'zh': '2026年10月19日，F3R 将更新、损失、系统与智慧族移入核心：所引声明旁加上核心陈述（'
                         + '、'.join(mods) + '），绑定到核心回执；外围引用保留到清扫退役其模块。无新结果，论断不变。'})
    open(f, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
    summary.append((f.rsplit('/', 1)[-1], {module_of[s]: len(v) for s, v in added.items()}))
for s in summary:
    print(*s)
print(len(summary), 'records changed')
