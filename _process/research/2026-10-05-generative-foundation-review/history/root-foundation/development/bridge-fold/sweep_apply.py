#!/usr/bin/env python3
"""F3 final sweep (19 October 2026): apply the plan of `ring_meta.py` once every family has landed.

usage (from the checkout root):
  python3 -B sweep_apply.py check PLAN.json        report what would happen; change nothing
  python3 -B sweep_apply.py apply PLAN.json        apply it

PLAN.json is `ring_meta.py plan OUT MODULE ...` run with every module of `retire.json`. The sweep
holds only where every bridge and join module leaves the package: each ring file is whole in the
plan (none of its declarations stays), or what stays in it is graded in a family's port file (a
theorem with a port row, or a definition nothing outside the file uses). Then:

1. every bridge and join file moves to `lean/history/becoming/Becoming/` with `research.py move`
   (bytes kept; live references, records included, follow the move; the receipt that last
   checked a file still names its bytes). The package's Lean files are pinned against moves in
   `research-config.json`, since a live module's path is its name; these modules leave the
   package, so the pin is lifted for this one move and restored, byte for byte, after it;
2. `check_becoming.py`: `BRIDGE` and `PERIPHERY_JOINS` are empty, `SUPERSEDED` lists every retired
   module with the core modules stating it (`retire.json`), the bridge environment audit runs
   only when a bridge module exists, and the checked examples import the root `Becoming`
   (the continuation example reads `Becoming.Jointly` on a region of reached configurations,
   where it read `JointContinuationClassification.Jointly` through the bridge's
   `Frame.continuations`);
3. `MachineInstances` (a periphery module with its own checker, outside the Becoming run) took
   two periphery-typed lemmas from `Becoming.Instances`: they are stated in it, with the imports
   `Becoming.Instances` gave it, and its checker's docstring follows.

4. the connectivity dump imports no bridge or join module.

Counts, chapter rows, records' notes and the apart register follow the checker run (`sweep_text.py`).
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path.cwd()
HERE = Path(__file__).resolve().parent
LEAN = Path('experiments/integrated-correction/general-framework/generative-basis/lean')
PKG = LEAN / 'becoming'
CHECKER = PKG / 'check_becoming.py'
HISTORY = LEAN / 'history/becoming'
MACHINE = LEAN / 'universal-ethics/generative-capacity/MachineInstances.lean'
MACHINE_CHECK = LEAN / 'universal-ethics/generative-capacity/check_machine_instances.py'
DUMP = Path('_process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY-DUMP.lean')
SRC = re.compile(r'(?:Becoming|Generative)\.[\w.\'₀-₉]+')

sys.path.insert(0, str(HERE))
import ring_meta  # noqa: E402


def port_rows():
    """(module short name, theorem short name) of every row of every family port file."""
    rows = set()
    for port in sorted(HERE.glob('port-*.md')):
        head, cols = None, None
        for line in port.read_text().split('\n'):
            m = re.match(r'^#{2,4}\s+(.*)', line)
            if m:
                head, cols = m.group(1).strip().strip('`'), None
                continue
            if not line.startswith('|'):
                cols = None
                continue
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            if cols is None:
                cols = [c.lower() for c in cells]
                continue
            if set(''.join(cells)) <= set('-: ') or len(cells) < len(cols):
                continue
            ti = next((i for i, c in enumerate(cols) if c in ('theorem', 'theorems', 'declaration')), None)
            if ti is None or not any('counterpart' in c or c == 'core' for c in cols):
                continue
            mi = next((i for i, c in enumerate(cols) if c in ('join', 'module', 'bridge')), None)
            cell = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', cells[mi] if mi is not None else head)
            mods = [m.strip().strip('`').split('.')[-1] for m in cell.split(',')]
            names = ['*'] if cells[ti].startswith('all') else (re.findall(r'`([^`]+)`', cells[ti]) or [cells[ti]])
            for mod in mods:
                for name in names:
                    rows.add((mod, name.split(' ')[0].split('.')[-1]))
    return rows


def assess(plan):
    L = ring_meta.lists()
    ring = L['BRIDGE'] + L['PERIPHERY_JOINS']
    whole = set(plan['whole_files'])
    going = {n for v in plan['source_declarations_going'].values() for n in v}
    data = json.loads((Path(plan['_out']) / 'ring-meta.json').read_text()) if '_out' in plan else None
    rows = port_rows()
    problems, residual = [], {}
    for m in ring:
        if m in whole:
            continue
        staying = sorted(n for n in ring_meta.source_names(m) if n not in going)
        short = m.split('.')[-1]
        unported = [n for n in staying if (short, '*') not in rows and (short, n.split('.')[-1]) not in rows]
        if data is not None:
            info = {d['name']: d for d in data['decls']}
            own = {d['name'] for d in data['decls'] if d['module'] == m}
            used_outside = {n for d in data['decls'] if d['name'] not in own and d['name'] not in going
                            for n in set(d['type']) | set(d['value']) if n in own}
            unported = [n for n in unported if not (info.get(n, {}).get('kind') != 'theorem' and n not in used_outside)]
        residual[m] = staying
        if unported:
            problems.append((m, unported))
    pinned_outside = {}
    for r, files in plan['ring_files_importing_a_retired_module'].items():
        rest = [f for f in files if f not in ring]
        if rest:
            pinned_outside[r] = rest
    return ring, residual, problems, pinned_outside


def move_plan(ring):
    lines = []
    for m in ring:
        rel = m.replace('.', '/') + '.lean'
        lines.append(f'{PKG / rel}\t{HISTORY / rel}\tF3 sweep (19 October 2026): every declaration reads only '
                     'superseded periphery modules, whose content the core states (bridge-fold port files)')
    return '\n'.join(lines) + '\n'


def edit_checker(retire):
    src = CHECKER.read_text()
    before = src
    # The lists.
    start = src.index('BRIDGE = [')
    end = src.index('SPINE = CORE + BRIDGE')
    src = src[:start] + (
        '# The bridge: emptied by the F3 sweep (19 October 2026). Every bridge and pure join module is in\n'
        '# lean/history/becoming/Becoming/ with its bytes, checked by the receipts before the sweep; the core\n'
        '# states the content of the periphery modules they read (SUPERSEDED).\n'
        'BRIDGE = []\n') + src[end:]
    start = src.index('# Periphery joins (U2, 17 October 2026)')
    end = src.index('CHECKED = SPINE + PERIPHERY_JOINS')
    src = src[:start] + (
        '# Periphery joins (U2, 17 October 2026): modules stating periphery theorems\' laws of the base through\n'
        '# periphery roots whose own axiom reports are not empty. Emptied by the F3 sweep (19 October 2026)\n'
        '# with the bridge; each declaration of a join, were one added, may carry only axioms it inherits.\n'
        'PERIPHERY_JOINS = []\n') + src[end:]
    start = src.index('SUPERSEDED = {')
    end = src.index('\n}\n', start) + 3
    entries = ''.join(f'    "{name}": {json.dumps(sorted(v["stated_by"]))},\n' for name, v in sorted(retire.items()))
    src = src[:start] + 'SUPERSEDED = {\n' + entries + '}\n' + src[end:]
    src = src.replace(
        'assert stated_by and all(m in CORE for m in stated_by), ("superseded module not stated by the core", name, stated_by)',
        'assert stated_by and all(m in CORE + FOUNDATION for m in stated_by), ("superseded module not stated by the core", name, stated_by)')
    # The checked examples import the root and read joint realization on the core.
    src = src.replace('CONTROLS = """import Becoming.Bridge\n', 'CONTROLS = """import Becoming\n')
    src = src.replace(
        'example : JointContinuationClassification.Jointly (grow.continuations false) (fun _ => True) :=\n',
        'example : Jointly grow (Reach grow.P false) (fun _ => True) :=\n')
    # The bridge environment audit runs only when there is a bridge.
    old_task = ('            tasks["bridge environment"] = (compiled(bridge_environment),\n'
                '                                           driver_step("BridgeEnvironmentAudit.lean", bridge_environment))\n')
    assert old_task in src
    src = src.replace(old_task, '            if BRIDGE:\n    ' + old_task.replace('\n            ', '\n                '))
    src = src.replace('            sequence += ["EnvironmentAudit.log", "BridgeEnvironmentAudit.log", "Controls.log"]\n',
                      '            sequence += ["EnvironmentAudit.log"] + (["BridgeEnvironmentAudit.log"] if BRIDGE else []) + ["Controls.log"]\n')
    old_use = ('            constants, generated = environment_audit(outputs["bridge environment"], BRIDGE)\n')
    assert old_use in src
    src = src.replace(old_use, '            constants, generated = (environment_audit(outputs["bridge environment"], BRIDGE)\n'
                               '                                    if BRIDGE else ({}, {}))\n')
    # The docstring says what is there now.
    src = src.replace('"""One checker for the Becoming package: the formal core and its bridge.',
                      '"""One checker for the Becoming package: the formal core.')
    old_doc = src[src.index('The bridge imports existing modules'):src.index('The declaration scanner reads')]
    src = src.replace(old_doc, (
        'Since the F3 sweep (19 October 2026) the package has no bridge and no periphery join: the core states\n'
        'the content of every periphery module that was in the run (`SUPERSEDED`), and the bridge and join\n'
        'files are in `lean/history/becoming/` with their bytes, checked by the receipts before the sweep. A\n'
        'superseded module keeps its bytes, stays out of the run (the run asserts that nothing compiled here\n'
        'imports it), and the receipt records its sha256 and the core modules stating it. The checker still\n'
        'checks a bridge (`BRIDGE`: modules importing existing modules to show that their interfaces are the\n'
        'core\'s, with empty axiom reports and their own constants audited) or periphery joins\n'
        '(`PERIPHERY_JOINS`: declarations carrying only the axioms they inherit), were one added.\n'))
    src = src.replace('be audited by name, are listed in the receipt (`not_audited_by_name`) and, in the core closure\n'
                      'and the bridge, covered by the environment audits.',
                      'be audited by name, are listed in the receipt (`not_audited_by_name`) and, in the core closure\n'
                      '(and a bridge, were there one), covered by the environment audits.')
    src = src.replace('# core layers and their root, then the bridge.', '# core layers and their root.')
    assert src != before
    return src


MACHINE_LEMMAS = '''
/-! ## Grouping and adoption of the periphery machines

Stated here since the F3 sweep (19 October 2026), with their proofs, from the pure bridge
`Becoming.Instances` (now in `lean/history/becoming/`): the two-word grouping law of
`AcquiredSegmentation` from the core's `Segmentation.encode_iff`, and that only an adoption changes
the rule of `OrganizationalRuleInheritance` (`Gated.KeptBy`). The core states both on its own
machines (`LearnedGrouping.two_word_iff`, `RuleHandoff.rule_kept`). -/

section Grouping

open Generative.AcquiredSegmentation

/-- `AcquiredSegmentation.chunks` is the core's grouping. -/
theorem chunks_eq (r : Sound → Sound → Bool) :
    ∀ xs : List Sound, AcquiredSegmentation.chunks r xs = Segmentation.chunks r xs
  | [] => rfl
  | x :: xs => by
    show (match AcquiredSegmentation.chunks r xs with
      | [] => [[x]]
      | [] :: rest => [x] :: rest
      | (y :: ys) :: rest => if r x y then (x :: y :: ys) :: rest else [x] :: (y :: ys) :: rest) =
      Segmentation.glue r x (Segmentation.chunks r xs)
    rw [chunks_eq r xs]
    cases Segmentation.chunks r xs with
    | nil => rfl
    | cons g rest =>
      cases g with
      | nil => rfl
      | cons y ys => rfl

theorem flatten_eq_join {α : Type} : ∀ L : List (List α), L.flatten = Segmentation.join L
  | [] => rfl
  | g :: gs => congrArg (g ++ ·) (flatten_eq_join gs)

/-- The two-word encoding is the core's encoding. -/
theorem encode_eq (ws : List Bool) :
    AcquiredSegmentation.encode ws = Segmentation.encode AcquiredSegmentation.word ws :=
  flatten_eq_join (ws.map AcquiredSegmentation.word)

/-- The first sound of each word. -/
def wordFirst : Bool → Sound
  | false => .a
  | true => .c

/-- The rest of each word. -/
def wordRest : Bool → List Sound
  | false => [.b]
  | true => [.d]

theorem spelled : Segmentation.Spelled AcquiredSegmentation.word wordFirst wordRest
  | false => rfl
  | true => rfl

/-- **For every grouping relation, grouping recovers the words of every sequence in the two-word
encoding exactly when `a→b` and `c→d` are linked and `b→a`, `b→c`, `d→a`, `d→c` are not.** -/
theorem two_word_iff (r : Sound → Sound → Bool) :
    (∀ ws, AcquiredSegmentation.chunks r (AcquiredSegmentation.encode ws) =
        ws.map AcquiredSegmentation.word) ↔
      r .a .b = true ∧ r .c .d = true ∧ r .b .a = false ∧ r .b .c = false ∧
        r .d .a = false ∧ r .d .c = false :=
  have core := Segmentation.encode_iff r spelled
  ⟨fun every =>
    have every' : ∀ ws, Segmentation.chunks r (Segmentation.encode AcquiredSegmentation.word ws) =
        ws.map AcquiredSegmentation.word := fun ws =>
      (encode_eq ws ▸ chunks_eq r _ ▸ every ws)
    match core.mp every' with
    | ⟨inside, between⟩ =>
      ⟨(inside false).1, (inside true).1, between false false, between false true,
       between true false, between true true⟩,
   fun ⟨ab, cd, ba, bc, da, dc⟩ ws =>
    have inside : ∀ w, Segmentation.LinkedFrom r (wordFirst w) (wordRest w) := fun
      | false => ⟨ab, trivial⟩
      | true => ⟨cd, trivial⟩
    have between : ∀ w v, r (Segmentation.lastOf (wordFirst w) (wordRest w)) (wordFirst v) =
        false := fun
      | false, false => ba
      | false, true => bc
      | true, false => da
      | true, true => dc
    (chunks_eq r _).trans ((congrArg (Segmentation.chunks r) (encode_eq ws)).trans
      (core.mpr ⟨inside, between⟩ ws))⟩

end Grouping

section Governance

open OrganizationalRuleInheritance

/-- The gate: adoption. -/
def adopts : Event → Bool
  | .review _ _ => false
  | .enroll _ _ => false
  | .propose _ _ => false
  | .adopt _ => true
  | .integrate _ => false
  | .handoff _ => false

theorem ite_some {β : Type} {c : Prop} {d : Decidable c} {x t : β} :
    (@ite _ c d (some x) none) = some t → x = t :=
  match d with
  | isTrue _ => fun same => Option.some.inj same
  | isFalse _ => fun same => nomatch same

/-- **Only an adoption changes the rule.** -/
theorem rule_kept : Gated.KeptBy OrganizationalRuleInheritance.process adopts State.rule
  | s, .review r c, t, step, _ =>
    have same : { s with reviews := (r, c) :: s.reviews } = t := ite_some step
    (congrArg State.rule same).symm
  | s, .enroll c _, t, step, _ =>
    have same : { s with roster := s.roster ++ [c] } = t := ite_some step
    (congrArg State.rule same).symm
  | s, .propose _ p, t, step, _ =>
    have same : { s with proposal := some p } = t := ite_some step
    (congrArg State.rule same).symm
  | _, .adopt _, _, _, gated => nomatch gated
  | s, .integrate _, t, step, _ =>
    have same : { s with accepted := s.accepted + 1 } = t := ite_some step
    (congrArg State.rule same).symm
  | s, .handoff cs, t, step, _ =>
    have same : handoff s cs = t := Option.some.inj step
    (congrArg State.rule same).symm

end Governance
'''

INSTANCES_IMPORTS = ['Becoming.Assurance', 'Becoming.Segmentation', 'Becoming.Readout', 'Becoming.Gated',
                     'WisdomResponseStructure', 'RelationalReduction', 'OrganizationalRuleInheritance',
                     'AcquiredSegmentation']


def edit_dump(ring):
    src = DUMP.read_text()
    for m in ring:
        assert src.count('import ' + m + '\n') <= 1
        src = src.replace('import ' + m + '\n', '')
    old = ('(the modules of the spine run: foundation, core, bridge\n'
           'and the inherited modules the bridge imports; that is, every module not rooted at `Init`, `Std`,\n'
           '`Lean` or `Lake`)')
    assert old in src
    src = src.replace(old, '(the modules of the spine run: the foundation and the core,\n'
                           'with a bridge and the modules it imports were there one; that is, every module not rooted\n'
                           'at `Init`, `Std`, `Lean` or `Lake`)')
    return src


def edit_machine():
    src = MACHINE.read_text()
    assert src.startswith('import Becoming.Instances\n')
    have = re.findall(r'^import\s+(\S+)', src, re.M)
    added = [m for m in INSTANCES_IMPORTS if m not in have]
    src = ''.join('import ' + m + '\n' for m in added) + src[len('import Becoming.Instances\n'):]
    anchor = 'namespace Becoming.MachineInstances\n\nopen Generative Becoming.Assurance\n'
    assert anchor in src
    src = src.replace(anchor, anchor + MACHINE_LEMMAS, 1)
    assert src.count('Instances.two_word_iff') == 1 and src.count('Instances.rule_kept') == 5
    src = src.replace('(Instances.two_word_iff (bond log))', '(two_word_iff (bond log))')
    src = src.replace('exact Instances.rule_kept _ _ _ moved rfl', 'exact rule_kept _ _ _ moved rfl')
    src = src.replace('so their instances of the core\'s laws are stated\nhere rather than in the pure bridge `Becoming.Instances`.',
                      'so their instances of the core\'s laws are stated\nhere (the pure bridge `Becoming.Instances` they once shared is in `lean/history/becoming/` since\nthe F3 sweep).')
    chk = MACHINE_CHECK.read_text()
    old = '`MachineInstances` imports the pure bridge `Becoming.Instances`, the core\'s\n'
    assert old in chk
    chk = chk.replace(old, '`MachineInstances` imports the core\'s `Becoming.Assurance`, `Segmentation`, `Readout` and `Gated`, the\n'
                           'periphery modules the pure bridge `Becoming.Instances` gave it (`WisdomResponseStructure`,\n'
                           '`RelationalReduction`, `OrganizationalRuleInheritance`, `AcquiredSegmentation`; the bridge is in\n'
                           '`lean/history/becoming/` since the F3 sweep), the core\'s\n')
    chk = chk.replace('instances, so these instances are stated here rather than in the pure bridge, and their',
                      'instances, so these instances are stated here rather than in the core, and their')
    return src, chk


def main():
    mode, plan_path = sys.argv[1], sys.argv[2]
    plan = json.loads(Path(plan_path).read_text())
    plan.setdefault('_out', str(Path(plan_path).parent / 'ring2'))
    retire = json.loads((HERE / 'retire.json').read_text())['modules']
    missing = sorted(set(plan['retired']) ^ set(retire))
    assert not missing, ('plan and retire.json name different modules', missing)
    ring, residual, problems, pinned_outside = assess(plan)
    print(json.dumps({'ring_files': len(ring), 'whole': len(plan['whole_files']),
                      'residual': {m: len(v) for m, v in residual.items()}, 'unported_residual': problems,
                      'retired_modules_imported_outside_the_ring': pinned_outside,
                      'reached_by_staying': plan['retired_modules_reached_by_staying_declarations'],
                      'blocked': len(plan['blocked'])}, indent=1))
    if problems or plan['blocked'] or plan['retired_modules_reached_by_staying_declarations']:
        sys.exit('the sweep does not hold yet')
    tsv = HERE / 'sweep-moves.tsv'
    if mode == 'check':
        print(move_plan(ring).count('\n'), 'moves')
        return
    tsv.write_text(move_plan(ring))
    checker = edit_checker(retire)
    machine, machine_check = edit_machine()
    dump = edit_dump(ring)
    # The package's Lean files are pinned against moves: a live module's path is its name. These
    # modules leave the package, so the pin is lifted for this move only and restored after it.
    config = ROOT / '_process/research-config.json'
    pinned = config.read_bytes()
    pattern = '    "' + str(PKG / 'Becoming') + '/**",\n'
    assert pattern in pinned.decode()
    config.write_text(pinned.decode().replace(pattern, '', 1))
    try:
        subprocess.run([sys.executable, '-B', 'tools/research/research.py', 'move', '--plan', str(tsv), '--apply',
                        '--batch', 'F3-sweep', '--summary'], check=True)
    finally:
        config.write_bytes(pinned)
    CHECKER.write_text(checker)
    MACHINE.write_text(machine)
    MACHINE_CHECK.write_text(machine_check)
    DUMP.write_text(dump)
    print('applied')


if __name__ == '__main__':
    main()
