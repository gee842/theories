#!/usr/bin/env python3
"""Build R35's moves.tsv (analysis table) and the move-tool plan files (old_path<TAB>new_path<TAB>reason).
Run from the repository root: python3 -B make_moves.py SCRATCH_DIR. Reads refscan.json; writes only in SCRATCH_DIR."""
import json, subprocess, sys, os, glob, collections
SC = sys.argv[1]
ref = json.load(open(f'{SC}/data/refscan.json'))
G = '_process/research/2026-10-05-generative-foundation-review'
RF = G + '/root-foundation'
HRF = G + '/history/root-foundation'
CH = 'theories/becoming/chapters'
TH = 'theories/becoming/history'
RES = 'theories/becoming/results'
tracked = set(subprocess.run(['git', 'ls-files'], capture_output=True, text=True).stdout.split('\n'))

# records citing a path (references), by id
cites = collections.defaultdict(set)
for p in glob.glob('theories/becoming/results/records/*.json'):
    r = json.load(open(p))
    for x in r['references']:
        cites[x['path'].split('#')[0]].add(r['id'])

def rec_ids(path):
    s = set()
    for k, v in cites.items():
        if k == path or k.startswith(path + '/'):
            s |= v
    return sorted(s)

def live_refs(path):
    v = ref.get(path, {}).get('refs', {})
    out = sorted({f for r, fs in v.items() if r in ('live/text', 'live/json', 'live/code') for f in fs
                  if '/development/' not in f and 'repository-reconciliation' not in f and 'twentieth-review' not in f
                  and not f.startswith('theories/becoming/results/records/')})
    return out

def pins(path):
    v = ref.get(path, {})
    p = []
    for k, why in v.get('pinned_tsv', {}).items():
        p.append(f'PINNED.tsv: {why}')
    fr = sorted({f for r, fs in v.get('refs', {}).items() if r.endswith('/freeze') for f in fs})
    p += [f'freeze: {f}' for f in fr]
    code = sorted({f for r, fs in v.get('refs', {}).items() if r == 'live/code' for f in fs if '/development/' not in f})
    p += [f'code: {f}' for f in code]
    return p

rows, plans = [], collections.defaultdict(list)

def add(batch, action, old, new, finding, change, plan=None, reason=None):
    ids = rec_ids(old)
    lr = live_refs(old)
    pn = pins(old)
    rows.append([batch, action, old, new or '', finding, f'{len(ids)}' + (f' ({", ".join(ids[:6])}{"…" if len(ids) > 6 else ""})' if ids else ''),
                 '; '.join(pn) or '-', f'{len(lr)}' + (f' ({"; ".join(x.split("/")[-1] for x in lr[:5])}{"…" if len(lr) > 5 else ""})' if lr else ''), change])
    if plan and new and action.startswith('move'):
        plans[plan].append((old, new, reason or finding))

# ---------------- B1 chapters (E14) -----------------------------------------------------------
SEC11 = 'edit THE-THEORY-OF-BECOMING.md §11 row (+ zh §11) to the history status; chapters README regenerates; links rewritten by the tool'
CHAIN = 'tool rewrites GENERATIVITY-CHAIN.md / generativity-chain.json path strings: note the path-only change in GENERATIVITY-CHAIN-INDEX-RECORD (chain maintenance record), once per batch'
for name, why, extra in [
    ('FORMAL-CORE', 'E14: historical (5 Oct), 0 records; pinned only by a frozen checker', 'lift PINNED.tsv H4 row (exact_check.py is frozen evidence of 9 Oct, not in CI; its exact-check.json input_sha256 stays true of the bytes at the new path, reached through the move receipt)'),
    ('FORMAL-SPECIFICATION', 'E14: historical (5 Oct, v0.10), 0 records; pinned only by a frozen checker', 'lift PINNED.tsv H4 row (same checker as FORMAL-CORE); experiments/shared-renewal-capability/formal/README.md link rewritten'),
    ('ALIGNMENT-COMPLETION', 'E14: 6 Oct conditional-candidate closure, 0 records; pinned only by foundation-assessment/FRONTIER-CHECK.py', 'lift PINNED.tsv H4 row (FRONTIER-CHECK.py frozen since 9 Oct; foundation-assessment declared evidence, B6); ALIGNMENT-DIRECTION(.zh) links rewritten'),
    ('MATHEMATICAL-ROOT-FRONTIER', 'E14/E1: superseded by §8 and §9; 0 records', 'MATHEMATICAL-CORE.md link rewritten (or re-pointed to chapter §9)'),
    ('PHILOSOPHICAL-ACCOUNT', 'E14/E1: 8 Oct whole-restatement, 0 records', 'chapter §3 cites it: replace the citation by the §3 text it supports, or keep the link to the history copy; KNOWLEDGE, ETHICAL-LEARNING links rewritten'),
    ('G0-WARRANT', 'E14: framing historical (axiom adopted 9 Oct, now a condition, §6.15)', 'BEFORE the move: fold §2-§3 ("what each kind of support contributes") as one paragraph into chapter §8.5 (en+zh); 2 records (integration) re-keyed by the tool; CHINESE-SOURCES, DAO, WANG links rewritten'),
    ('G0-WARRANT.zh', 'E14/E5: unmaintained edition titled as if G0 were an adopted axiom', 'moves with its English'),
    ('PLURAL-SYSTEMS-AND-CORRECTION', 'E14: §15 is the live framing; rest superseded; 0 records', 'BEFORE the move: fold §15 "Responsive transformation" into chapter §4 (en+zh); theories/meta-attractor/COLLECTIVE-DESTRUCTIVE-ATTRACTORS(.zh) links rewritten'),
    ('PLURAL-SYSTEMS-AND-CORRECTION.zh', 'E14: edition of a retired chapter', 'moves with its English'),
    ('NONINSTRUMENTAL-CONCERN', 'E14 (judgment): 90 KB, 7 Oct banner, 0 records; overlaps WANG-YANGMING and §5', 'tools/research/lean_catalogue.py GROUPS["concern"] conceptual entry: point at chapter §5 anchor instead (current() would follow the receipt to history); ETHICAL-LEARNING(.zh), WANG-YANGMING links rewritten; experiments/.../noninstrumental-concern/README.md link rewritten'),
    ('RELATIONS-ACROSS-SCALES', 'E14 (judgment): 0 records, live successors (§2, §4)', 'ZERO-AXIOM-PRACTICAL-JUDGMENT(.zh) and lean/systems-complexity/README.md links rewritten'),
    ('RELATIONS-ACROSS-SCALES.zh', 'E14: edition of a retired chapter', 'moves with its English'),
]:
    add('B1-chapters', 'move', f'{CH}/{name}.md', f'{TH}/{name}.md', why, f'{SEC11}; {extra}; {CHAIN}', 'R35-B1-chapters')
# E15 fold: listed as edits, then the compact chapters move under dated names (RH originals already hold the plain names)
for name, sec in [('DAO-AND-GENERATIVITY', '§5.2/§9 neighbourhood'), ('HANZI-AND-THEORY-TREE', '§6 (keep the old §5 criteria anchor: ZH uses "HANZI §5 criteria")'),
                  ('PRE-QIN-AND-WENYAN', '§7-§8'), ('WANG-YANGMING', '§5.3')]:
    add('B1-chapters (E15)', 'edit (fold)', f'{CH}/{name}.md', f'{CH}/CHINESE-SOURCES-AND-BECOMING.md', 'E15: fold the compact rewrite in as a section of CHINESE-SOURCES', f'new section of CHINESE-SOURCES at {sec}, with <a id> anchors for the compact chapter\'s headings; coordinate with ZH (board row ZH, branch zhonghua, reads HANZI §5 and extends the RO map)')
    add('B1-chapters (E15)', 'move', f'{CH}/{name}.md', f'{TH}/{name}-2026-10-19.md', 'E15: after the fold; RH originals already at history/' + name + '.md', 'after the move, re-point the live links the tool rewrote to the history copy to the new CHINESE-SOURCES section instead (CHINESE-SOURCES, chapter §11, LIANGZHI-EVOLUTION, theories/jian-and-wenyan-as-formal-language/README.md); ' + CHAIN, 'R35-B1-chapters', 'superseded: folded into CHINESE-SOURCES-AND-BECOMING as a section (E15); the 6-7 October originals are at history/' + name + '.md')
# optional: unmaintained zh editions carrying G0 whose English stays live (E5, judgment)
for name, n in [('ETHICAL-LEARNING.zh', 50), ('PRACTICAL-JUDGMENT.zh', 18), ('BASIC-CONFLICT-JUDGMENT.zh', 13), ('CHOICE-AND-GENERATIVE-CONTEXT.zh', 9), ('WISDOM-AND-CONTEXT.zh', 9), ('ALIGNMENT-DIRECTION.zh', 8)]:
    p = f'{CH}/{name}.md'
    add('B1z-zh-editions (option)', 'move (judgment) or banner', p, f'{TH}/{name}.md', f'E5: unmaintained edition, G0 x{n}; English is canonical', 'Option A: move (AGENTS allows English-only); Option B: one-line banner naming the current terms. ETHICAL-LEARNING.zh is the original Chinese text: banner, not move')

# ---------------- B2 REFERENCE (E2) -----------------------------------------------------------
add('B2-reference', 'move', f'{CH}/THE-THEORY-OF-BECOMING-REFERENCE.md', f'{TH}/THE-THEORY-OF-BECOMING-REFERENCE.md',
    'E2: verbatim pre-restructure lists (l.1-113) are history; the declaration catalogue (l.114-218) and module table (l.219-475) duplicate LEAN-INDEX and the Lean README; whole file moves, nothing kept live',
    'chapter links (status block, §9) rewritten by the tool, then reworded "the 17 October declaration lists (history)"; tools/research/tests/test_indexes.py names the path: update the fixture; no record binds it (104 records mention it only in history notes)', 'R35-B2-reference')

# ---------------- B3 generated snapshots (E2) ---------------------------------------------------
GEN = ('stop rendering first: reading_catalogue.outputs() returns README.md only; research.py index_outputs() drops session_map.render_output(); '
       'remove the path from _process/architecture/generated-manifest.json and from research-config indexes.adopted_pages')
add('B3-generated', 'move --keep-references + stub', f'{RES}/ARGUMENTS-A-L.md', f'{TH}/ARGUMENTS-A-L-2026-10-08.md',
    'E2: "Readings of 8 October 2026 and later"; 105 of 144 entries link history chapters; G0 x62 across the two volumes',
    GEN + '; GENERATIVITY-CHAIN.md line 5 links this page (Ren\'s curated chain changes only through its maintenance record), so leave a generated stub at the old path (title, "frozen 8 October reading, see history/…", no body) and do not rewrite links; reading_catalogue.index() (results/README.md) links the history copy with its anchors', 'R35-B3-generated-keep', 'frozen: 8 October reading edition; the live register is RESULTS.md and the chapters README')
add('B3-generated', 'move --keep-references + stub', f'{RES}/ARGUMENTS-M-Z.md', f'{TH}/ARGUMENTS-M-Z-2026-10-08.md', 'E2: as ARGUMENTS-A-L', 'as ARGUMENTS-A-L', 'R35-B3-generated-keep', 'frozen: 8 October reading edition; the live register is RESULTS.md and the chapters README')
add('B3-generated', 'move', f'{RES}/THEORY-MAP.md', f'{TH}/THEORY-MAP-2026-10-08.md', 'E2: "Readings of 8 October 2026" of the September branches',
    GEN + '; links in MAP.md, theories/jian-and-wenyan-as-formal-language/README.md, HANZI chapter rewritten by the tool; reading_catalogue.index() rows 242-256 drop THEORY-MAP/ARGUMENTS/SESSION links or point to history; research-config readme text mentioning THEORY-MAP (rewritten as JSON path string)', 'R35-B3-generated')
add('B3-generated', 'move', f'{RES}/SESSION-RESULTS.md', f'{TH}/SESSION-RESULTS-2026-10-08.md', 'E2: "8 October 2026 … dated chat coverage"',
    GEN + '; registry.py l.823 (every record page header links "Session map"): remove the link (279 record pages re-render, no record JSON change); navigation.py l.493 drop the link; session_map.py REPORT/HERE constants to the history paths (or mark the tool historical; build_session_result_map.py wrapper stays); RESULT-WORKFLOW.md l.236 sentence on the session map rewritten; data/session-results.json STAYS (records\' required `family` F01-F22 and generativity-chain.json use its family ids)', 'R35-B3-generated')
add('B3-generated', 'move', f'{RES}/lean-declarations/becoming-bridge.md', f'{TH}/lean-declarations/becoming-bridge.md', 'E2: empty group after the F3 sweep (0 modules)',
    'lean_catalogue.py: delete GROUPS["becoming-bridge"] and RECEIPT_GROUPS["bridge"]; tests/test_indexes.py l.72 expects group "becoming-bridge" for Bridge.lean: change the fixture; LEAN-DECLARATIONS.md row disappears on render; remove from generated-manifest.json', 'R35-B3-generated')

# ---------------- B4 study files (E10) ------------------------------------------------------------
study = {
 # executed plans / answered briefs / superseded reviews
 'BECOMING-UNIFICATION-PLAN.md': ('move', 'E10: executed plan (P0-P63, I4); still the statement source of 26 records and integration of 15: the tool re-keys them', 'records keep their claims; GOALS/plan links rewritten; r22-names/rebind.py touched its rename table on 19 Oct: confirm no open item edits it (R30 will hold the one rename table)'),
 'BECOMING-UNIFICATION-PLAN.zh.md': ('move', 'E10: edition of the executed plan', 'moves with its English'),
 'ZERO-PREMISE-PLAN.md': ('move', 'E10: executed plan (I4); 4 records cite it (integration)', 'moves with ZERO-PREMISE-INVENTORY.py; target-1/K1-K7 text (approved 20 Oct) points at chapter §8 and GOALS, not here'),
 'ZERO-PREMISE-PLAN.zh.md': ('move', 'E10: edition of the executed plan', 'moves with its English'),
 'ZERO-PREMISE-INVENTORY.py': ('move', 'E10: the plan\'s inventory script', 'parents[4] depth: frozen evidence after the move (not rerun)'),
 'BECOMING-BRIDGE-FOLD.md': ('move', 'E10: executed (F1-F3 sweep landed 2f8b4d3b3)', 'moves after E8 (records plan) reads development/bridge-fold/retire.json'),
 'MODULE-CLASSIFICATION.md': ('move', 'E10: executed by I4 and F3 ("nothing is marked, moved or deleted before Ren decides")', 'drafts/…/formal/*.lean comments name it (no link, unchanged)'),
 'MODULE-CLASSIFICATION.zh.md': ('move', 'E10: edition', 'moves with its English'),
 'SPINE-INTEGRATION.py': ('move', 'E10: I4 tool (16 Oct), executed', 'moves with development/integration-i4a; parents[3] depth: frozen evidence'),
 'READINGS-PENDING-REN.md': ('move', 'E10: answered (D45, 19 Oct)', 'board/AGENTS links rewritten'),
 'PHRASE-READINGS-PENDING-REN.md': ('move', 'E10: answered (D45)', '-'),
 'BECOMING-EIGHTEENTH-REVIEW.md': ('move', 'E10: superseded review', 'REVIEWS.md (generated) re-renders'),
 'BECOMING-EIGHTEENTH-REVIEW.zh.md': ('move', 'E10: edition', '-'),
 'BECOMING-GENERAL-LAWS-REVIEW.md': ('move', 'E10: superseded review (seventeenth)', 'historical-source-binding history notes link it (history field, not rewritten; resolves through the receipt)'),
 'BECOMING-GENERAL-LAWS-REVIEW.zh.md': ('move', 'E10: edition', '-'),
 'BECOMING-RELEASE-READINESS-REVIEW.md': ('move', 'E10: superseded review', '-'),
 'BECOMING-NINETEENTH-REVIEW.md': ('move (judgment)', 'E10 kept it as latest; the twentieth review supersedes it and R21 landed its fixes', 'judgment: keep only the latest review live'),
 'RESULTS-CATALOGUE-RECORD.md': ('move', 'E2/E10: editing record of the frozen catalogue volumes', 'reading_catalogue.py l.278 footer link: point to the history path'),
 'RESULTS-CATALOGUE-RECORD.zh.md': ('move', 'edition', '-'),
 # uncited 13-14 Oct check outputs
 'COMPARISON-CONTENT-INTEGRATION-CHECKS.json': ('move', 'E10: uncited check output (14 Oct)', '-'),
 'COMPLETE-EPISODE-COMPARISON-INTEGRATION-CHECKS.json': ('move', 'E10: uncited check output (14 Oct)', '-'),
 'EPISODE-AND-SUSTAINED-HARM-INTEGRATION-CHECKS.json': ('move', 'E10: uncited check output (14 Oct)', '-'),
 'FINITE-RESPONSIVENESS-INTEGRATION-CHECKS.json': ('move', 'E10: uncited check output (14 Oct)', '-'),
 'TIMELY-CONTINUATION-INTEGRATION-CHECKS.json': ('move', 'E10: uncited check output (14 Oct)', '-'),
 'META-ATTRACTOR-COMPLETION-CHECKS.json': ('move', 'E10: uncited check output (13 Oct)', '-'),
 'META-ATTRACTOR-REFERENCE-PLAN-INTEGRATION-CHECKS.json': ('move', 'E10: uncited check output (13 Oct)', '-'),
 'META-ATTRACTOR-REVISION-INTEGRATION-CHECKS.json': ('move', 'E10: uncited check output (13 Oct)', '-'),
 'OPEN-FORM-BRIDGE-CHECKS.json': ('move', 'E10: uncited check output (13 Oct)', '-'),
 # session map inputs (move with SESSION-RESULTS)
 'SESSION-CLASSIFIER-CORRECTION.json': ('move', 'E2/E10: session-map input, frozen with SESSION-RESULTS', 'session_map.py constants'),
 'SESSION-INTEGRATION-AUDIT.md': ('move', 'E2/E10: session-map audit', 'session_map.py constant'),
 'SESSION-INTEGRATION-BASELINE.json': ('move', 'E2/E10: session-map input', 'session_map.py BASELINE constant'),
 'SESSION-INTEGRATION-FINAL-CHECKS.json': ('move', 'E2/E10: session-map check output', '-'),
 'SESSION-INTEGRATION-NAVIGATION.json': ('move', 'E2/E10: session-map navigation output', '-'),
 'SESSION-OUTCOME-SNAPSHOT.json': ('move', 'E2/E10: session-map input', 'session_map.py SNAPSHOT constant'),
 'SESSION-PROOF-OVERLAP.json': ('move', 'E2/E10: session-map inventory', 'session_map.py INVENTORY constant'),
 'SESSION-PROOF-REUSE-SOURCE-CHECKS.json': ('move', 'E2/E10: session-map check; 2 records cite it (review)', 'records re-keyed by the tool'),
 'SESSION-RESULT-MAP-CHECKS.json': ('move', 'E2/E10: session-map check output', 'session_map.py CHECKS constant'),
}
keep = {
 'BECOMING-RENEWAL-READING.md': 'live study log; move_pinned in research-config (the tool refuses); E10 option: close as volume §1-§218, continue in a new file (separate step)',
 'BECOMING-RENEWAL-READING.zh.md': 'edition of the live log',
 'BECOMING-TWENTIETH-REVIEW.md': 'the latest review (with twentieth-review/)',
 'CHAIN-RELABELLING-PENDING-REN.md': 'live proposal on Ren\'s chain',
 'GENERATIVITY-CHAIN-INDEX-RECORD.md': 'the chain\'s maintenance record',
 'DELEGATED-CHOICES.md': 'live readings register', 'DELEGATED-CHOICES.zh.md': 'edition',
 'REGISTRATION-VOCABULARY-STUDY.md': 'adopted vocabulary (§7-§9)',
 'THEOREM-CONNECTIVITY.md': 'live measure', 'THEOREM-CONNECTIVITY.zh.md': 'edition', 'THEOREM-CONNECTIVITY.json': 'live measure data',
 'THEOREM-CONNECTIVITY.py': 'live instrument', 'THEOREM-CONNECTIVITY-APART.json': 'apart register', 'THEOREM-CONNECTIVITY-DUMP.lean': 'instrument input',
 'DECIDABILITY-INVENTORY.md': 'chapter §2 cites it as the live list of theorems conditioned on decidability', 'DECIDABILITY-INVENTORY.zh.md': 'edition',
 'DECIDABILITY-INVENTORY.lean': 'inventory input', 'DECIDABILITY-INVENTORY.py': 'inventory script',
 'README.md': 'generated study index', 'INDEX.md': 'generated', 'REVIEWS.md': 'generated review ledger',
 'CORE-CONSTRAINT-AND-WISDOM.md': 'canonical source of wisdom-root (open)', 'CROSSED-CLAIMS-ARGUMENT.md': 'canonical source of a live record', 'CROSSED-CLAIMS-ARGUMENT.zh.md': 'edition',
 'CROSSED-CLAIMS-INTEGRATION.md': 'record-cited integration note', 'CROSSED-CLAIMS-INTEGRATION.zh.md': 'edition',
 'SCIENTIFIC-INQUIRY-CONDITIONS.md': 'record-cited (integration 3, review 1)', 'SCIENTIFIC-INQUIRY-EVIDENCE.md': 'record-cited (review 2)',
 'ETHICAL-LEARNING-INTEGRATION.md': 'record-cited', 'META-ATTRACTOR-RECONCILIATION.md': 'record-cited', 'META-ATTRACTOR-RECONCILIATION.zh.md': 'edition',
 'RISK-CONDITIONING-INTEGRATION.md': 'record-cited', 'ZERO-AXIOM-PRACTICAL-JUDGMENT-INTEGRATION.md': 'record-cited', 'ZERO-AXIOM-PRACTICAL-JUDGMENT-INTEGRATION.zh.md': 'edition',
 'CONTINUATION-GROUNDING-REVIEW.md': 'record-cited review (5)', 'SSBX-REPOSITORY-REVIEW.md': 'record-cited (provenance 4)',
 'SCIENTIFIC-FOUNDATION-CORRESPONDENCE-REVIEW.json': 'review receipt set bound by records: keep the 7 SCIENTIFIC-*-REVIEW.json together as evidence (add to evidence_paths)',
 'SCIENTIFIC-INQUIRY-CONTINUATION-REVIEW.json': 'review receipt set', 'SCIENTIFIC-INQUIRY-DEMARCATION-REVIEW.json': 'review receipt set', 'SCIENTIFIC-INQUIRY-PREMISE-REVIEW.json': 'review receipt set (uncited member)',
 'SCIENTIFIC-INQUIRY-RELATIONS-REVIEW.json': 'review receipt set (uncited member)', 'SCIENTIFIC-INQUIRY-TIMING-REVIEW.json': 'review receipt set', 'SCIENTIFIC-INQUIRY-WARRANT-REVIEW.json': 'review receipt set',
 'build_generative_chain.py': 'compatibility wrapper (tools README); imported by foundation-assessment and experiment checkers', 'build_lean_catalogue.py': 'compatibility wrapper', 'build_result_registry.py': 'compatibility wrapper; tests import it',
 'build_results_catalogue.py': 'compatibility wrapper', 'build_session_result_map.py': 'compatibility wrapper', 'test_result_registry.py': 'test of the wrapper',
}
for c in sorted(k for k in ref if k.startswith(RF + '/') and '/development/' not in k):
    name = c[len(RF) + 1:]
    if ref[c]['pinned_tsv'] or any(r.endswith('/freeze') for r in ref[c]['refs']):
        add('B4-study', 'stay (pinned)', c, '', 'E10 listed some of these as uncited; they are pinned (PINNED.tsv H5: hard-coded in experiment checkers or freeze manifests)', 'label as pinned evidence in the study README (generated) / evidence_paths; moves only with its checker')
    elif name in study:
        a, why, ch = study[name]
        add('B4-study', a, c, f'{HRF}/{name}', why, ch, 'R35-B4-study')
    elif name in keep:
        add('B4-study', 'stay (live)', c, '', 'E10 live working state', keep[name])
    else:
        add('B4-study', 'REVIEW', c, '', 'unclassified', '')

# ---------------- B5 development kits ---------------------------------------------------------------
KEEP_KITS = {'y1-changes': 'live passage map: YI-ZHUAN chapter table = passages.json (verify_mapping.py --table); G12 adds law_level here; ZH extends the maps',
             'ro-relational-sources': 'live passage map: CHINESE-SOURCES tables = passages.json via build_passages.py FIXES (verify_ro.py); ZH (active) extends it; G12',
             'zero-axiom-classification-before': 'pinned (PINNED.tsv H5)'}
COLLIDE = {'becoming-general-laws-plan', 'integration-i3e'}
for c in sorted(k for k in ref if k.startswith(RF + '/development/')):
    kit = c.rsplit('/', 1)[1]
    if kit in KEEP_KITS:
        add('B5-kits', 'stay (live)' if 'pinned' not in KEEP_KITS[kit] else 'stay (pinned)', c, '', 'E10', KEEP_KITS[kit])
        continue
    why = 'E10: landed-item kit'
    if kit.startswith('r2') and kit[2:3].isdigit():
        why = 'E10: kit of a landed R-item; no record references it (only history notes mention r22-names)'
    ch = 'remove ignored .build/ and __pycache__/ first (build output of a landed item, not data); lean-index.json/source-index.json re-render'
    if kit == 'bridge-fold':
        ch = 'after E8 reads retire.json; lean Becoming README + chapter + LEAN-INDEX links rewritten; ' + ch
    if kit == 'becoming-general-laws-plan':
        ch = 'RESULT-WORKFLOW.md links readability/drafts: rewritten by the tool; ' + ch
    if kit == 'integration-i4a':
        ch = 'moves with SPINE-INTEGRATION.py; ' + ch
    if kit in ('a2-chain', 'a3-chain'):
        ch = 'GENERATIVITY-CHAIN-INDEX-RECORD links rewritten (chain maintenance record, AI-written: allowed); ' + ch
    if kit in COLLIDE:
        files = sorted(t for t in tracked if t.startswith(c + '/'))
        add('B5-kits', 'move (per file: target dir exists in history)', c, f'{HRF}/development/{kit}', why, ch)
        for f in files:
            plans['R35-B5-kits'].append((f, HRF + f[len(RF):], why))
    else:
        add('B5-kits', 'move', c, f'{HRF}/development/{kit}', why, ch, 'R35-B5-kits')
# untracked leftovers inside development/
for d, why in [('becoming-landing-kit', 'untracked: only __pycache__'), ('becoming-p87-landing', 'untracked: empty lean/, evidence/, docs/ folders and __pycache__')]:
    rows.append(['B5-kits', 'remove (untracked, not data)', f'{RF}/development/{d}', '', 'E12', '0', '-', '0', why])

# ---------------- B6 foundation-assessment, B7 process leftovers ---------------------------------------
add('B6-foundation-assessment', 'stay as declared evidence (recommended)', f'{G}/foundation-assessment', '',
    'E10: last substantive change 9 Oct; 5 records cite MARKET-INTERNET-DEGENERATION.md',
    'cannot move whole: ACTION-CORRECTION-{DESIGN,EVIDENCE,REVIEW}.md are pinned by experiments/agentdojo-evidence-boundary/correction-action/FREEZE.json (move tool refuses) and prepare.py hard-codes DESIGN; 9 checkers use HERE.parents[3]; history/foundation-assessment/README.md already exists. Add the folder to research-config path_roles.evidence_paths with this reason; README banner; study README lists it as evidence. Alternative (B): per-file move of the 102 unpinned files to history/foundation-assessment/ (README collides), leaving the 3 frozen files: splits the evidence set, not recommended')
add('B7-process', 'move', '_process/reading-notes', '_process/history/2026-09-consolidation/reading-notes', 'E11: 11 September notes; inputs already in history/2026-09-consolidation/reading-notes-inputs',
    'tool rewrites the links in 14 September branch READMEs (theories/*/README.md), drafts/2026-09-04-one-work/STRUCTURE.md; sources/ mentions stay (never rewritten); drafts v7.3/src is evidence (frozen)', 'R35-B7-process')
rows.append(['B7-process', 'remove (untracked empty folder)', '_process/handoffs', '', 'E11', '0', '-', '1 (review-data.json, frozen review)', 'rmdir; nothing tracked, nothing to move'])
rows.append(['B7-process', 'remove (untracked scratch)', '.claude/tmp_done.txt', '', 'E12', '0', '-', '0', '693 B list of record IDs from a session; scratch area, untracked'])

hdr = ['batch', 'action', 'old_path', 'new_path', 'reason (finding)', 'records citing (references)', 'pins (PINNED.tsv / freeze / live code)', 'live referrers outside kits', 'what must change with it']
with open(f'{SC}/moves.tsv', 'w') as f:
    f.write('\t'.join(hdr) + '\n')
    for r in rows:
        f.write('\t'.join(str(x).replace('\t', ' ').replace('\n', ' ') for x in r) + '\n')
for name, entries in plans.items():
    with open(f'{SC}/plans/{name}.tsv', 'w') as f:
        f.write('old_path\tnew_path\treason\n')
        for o, n, why in entries:
            f.write(f'{o}\t{n}\t{why}\n')
c = collections.Counter((r[0], r[1]) for r in rows)
for k, v in sorted(c.items()):
    print(k, v)
print({k: len(v) for k, v in plans.items()})
