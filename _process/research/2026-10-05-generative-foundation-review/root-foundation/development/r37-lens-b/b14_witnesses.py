#!/usr/bin/env python3
"""R37 B14: the rebuilt witness models as one-line instances of Becoming.Witnesses.

usage: python3 -B b14_witnesses.py [--dry]

Edits the core sources in place (this checkout), each edit exact:
* processes: a closed free process at Type -> `everyStep S A` (Becoming.World); the process with
  no step -> `Witnesses.halted S A`; one step from a to b -> `Witnesses.single A a b`; the flip ->
  `Law.process not` (Becoming.Recurrence);
* profiles: a definition `Nat -> Nat/Prop/Bool` by literal cases then one value ->
  `Witnesses.profile [..] rest`;
* flows and webs: the flow in which nothing takes part, one formation giving one unit, the webs
  with nothing required that the named twins build;
* the renewer and two takers (Exceeding, Excluding, Race).
Adds `import Becoming.Witnesses` where a changed module's closure lacks it. Logs every edit to
b14.log.tsv."""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PKG = HERE.parents[5] / 'experiments/integrated-correction/general-framework/generative-basis/lean/becoming'
B = PKG / 'Becoming'
sys.path.insert(0, str(PKG))
import check_becoming as cb  # noqa: E402

DRY = '--dry' in sys.argv
log = []
changed = {}


def text(mod):
    if mod not in changed:
        changed[mod] = (B / f'{mod}.lean').read_text()
    return changed[mod]


def replace(mod, old, new, count=1, kind=''):
    s = text(mod)
    n = s.count(old)
    assert n == count, (mod, old, n)
    changed[mod] = s.replace(old, new)
    log.append((kind, mod, old.strip().split('\n')[0][:120], new.strip().split('\n')[0][:120]))


# --- processes -------------------------------------------------------------------------------
FREE = [('AssurancePlans', 'def process : Process Bool Unit := ⟨fun _ _ _ => True⟩', 'def process : Process Bool Unit := everyStep Bool Unit'),
        ('Enough', 'def process : Process Bool Unit := ⟨fun _ _ _ => True⟩', 'def process : Process Bool Unit := everyStep Bool Unit'),
        ('LawAlongRun', 'def process : Process Bool Unit := ⟨fun _ _ _ => True⟩', 'def process : Process Bool Unit := everyStep Bool Unit'),
        ('MoveOutcomeProcesses', 'def free : Process Bool Unit := ⟨fun _ _ _ => True⟩', 'def free : Process Bool Unit := everyStep Bool Unit'),
        ('Carriers', 'def singletonLoop : Process Unit Unit := ⟨fun _ _ _ => True⟩', 'def singletonLoop : Process Unit Unit := everyStep Unit Unit'),
        ('Courses', 'def loop : Process Unit Bool := ⟨fun _ _ _ => True⟩', 'def loop : Process Unit Bool := everyStep Unit Bool'),
        ('Junctures', 'def process : Process Unit Nat := ⟨fun _ _ _ => True⟩', 'def process : Process Unit Nat := everyStep Unit Nat')]
HALTED = [('AssurancePlans', 'def process : Process Bool Unit := ⟨fun _ _ _ => False⟩', 'def process : Process Bool Unit := Witnesses.halted Bool Unit'),
          ('Carriers', 'def idle : Process Bool Unit := ⟨fun _ _ _ => False⟩', 'def idle : Process Bool Unit := Witnesses.halted Bool Unit'),
          ('MoveOutcomeProcesses', 'def halted : Process Bool Unit := ⟨fun _ _ _ => False⟩', 'def halted : Process Bool Unit := Witnesses.halted Bool Unit')]
SINGLE = [('Labelled', 'def law : Process Bool Unit :=\n  ⟨fun s _ t => s = false ∧ t = true⟩', 'def law : Process Bool Unit := Witnesses.single Unit false true'),
          ('Viability', 'def process : Process Bool Unit := ⟨fun s _ t => s = true ∧ t = false⟩', 'def process : Process Bool Unit := Witnesses.single Unit true false'),
          ('LawAlongRun', 'def process : Process Bool Unit := ⟨fun s _ u => s = true ∧ u = true⟩', 'def process : Process Bool Unit := Witnesses.single Unit true true')]
FLIP = [('Carriers', 'def toggle : Process Bool Unit := ⟨fun s _ t => t = !s⟩', 'def toggle : Process Bool Unit := Law.process not'),
        ('Irreversibility', 'def flip : Process Bool Unit := ⟨fun s _ t => t = !s⟩', 'def flip : Process Bool Unit := Law.process not')]
# frames with no step
FRAMES = [('Alternatives', '⟨⟨fun _ _ _ => False⟩, realized⟩', '⟨Witnesses.halted _ _, realized⟩'),
          ('Bundles', '⟨⟨fun _ _ _ => False⟩, realized⟩', '⟨Witnesses.halted _ _, realized⟩'),
          ('Bundles', '⟨⟨fun _ _ _ => False⟩, fun r bundle =>', '⟨Witnesses.halted _ _, fun r bundle =>'),
          ('Extension', '⟨⟨fun _ _ _ => False⟩, fun l e =>', '⟨Witnesses.halted _ _, fun l e =>'),
          ('Granularity', '⟨⟨fun _ _ _ => False⟩, fun _ _ => p⟩', '⟨Witnesses.halted _ _, fun _ _ => p⟩'),
          ('Handoff', '⟨⟨fun _ _ _ => False⟩, fun h q =>', '⟨Witnesses.halted _ _, fun h q =>')]
for group, kind in ((FREE, 'free'), (HALTED, 'halted'), (SINGLE, 'single'), (FLIP, 'flip'), (FRAMES, 'halted-frame')):
    for mod, old, new in group:
        replace(mod, old, new, kind=kind)
replace('Composition', '  P := ⟨fun _ _ _ => False⟩', '  P := Witnesses.halted _ _', count=2, kind='halted-frame')

# --- flows and webs --------------------------------------------------------------------------
EMPTY = '⟨fun _ => [], fun _ _ _ => 0, fun _ _ _ => 0⟩'
for mod in ('Regulation', 'Reserve', 'Roles'):
    replace(mod, f'def flow : Flow Unit Unit := {EMPTY}', 'def flow : Flow Unit Unit := Witnesses.emptyFlow Unit Unit', kind='emptyFlow')
replace('Flow', 'def flow : Flow Unit Unit := ⟨fun _ => [()], fun _ _ _ => 0, fun _ _ _ => 1⟩',
        'def flow : Flow Unit Unit := Witnesses.giving () 1', kind='giving')
replace('Space', 'def flow : Flow Unit Unit :=\n  ⟨fun _ => [()], fun _ _ _ => 0, fun _ _ _ => 1⟩',
        'def flow : Flow Unit Unit := Witnesses.giving () 1', kind='giving')
replace('Flow', '''def web : Web Unit Unit where
  level t _ := t + 1
  active _ _ := True
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False''', 'def web : Web Unit Unit := Witnesses.unrequired (fun t _ => t + 1) (fun _ _ => True)', kind='unrequired')
replace('Space', '''def web : Web Unit Unit where
  level t _ := t
  active _ _ := False
  requires _ _ _ := False
  need _ _ _ := 0
  draws _ _ _ := False''', 'def web : Web Unit Unit := Witnesses.unrequired (fun t _ => t) (fun _ _ => False)', kind='unrequired')
replace('Regulation', '''def web : Web Unit Unit :=
  ⟨fun _ _ => 2, fun _ _ => True, fun _ _ _ => False, fun _ _ _ => 0, fun _ _ _ => False⟩''',
        'def web : Web Unit Unit := Witnesses.unrequired (fun _ _ => 2) (fun _ _ => True)', kind='unrequired')

# --- the renewer and two takers --------------------------------------------------------------
RELAY_TAKE = '''  take _ f _ := match f with
    | .renewer => 0
    | .first => {a}
    | .second => {b}
  give _ f _ := match f with
    | .renewer => 2
    | .first => 0
    | .second => 0'''
DRAWS = '''  requires _ _ _ := True
  need _ _ _ := 1
  draws _ f _ := match f with
    | .renewer => False
    | .first => True
    | .second => True'''
MEMBER_RENEWER = '''inductive Member where
  | renewer
  | first
  | second'''
replace('Continuation', '/-- A renewer and two takers share one condition. -/\n' + MEMBER_RENEWER,
        '/-- A renewer and two takers share one condition. -/\nabbrev Member := Witnesses.Member', kind='relay')
replace('RelativePosition', '/-- A renewer and two parts sharing one condition. -/\n' + MEMBER_RENEWER,
        '/-- A renewer and two parts sharing one condition. -/\nabbrev Member := Witnesses.Member', kind='relay')
for mod, a, b in (('Continuation', 2, 2), ('Exclusion', 2, 2), ('RelativePosition', 2, 1)):
    old = 'def flow : Flow Member Unit where\n  present := present\n' + RELAY_TAKE.format(a=a, b=b)
    replace(mod, old, f'def flow : Flow Member Unit := Witnesses.relay present 2 {a} {b}', kind='relay')
for mod in ('Continuation', 'RelativePosition'):
    replace(mod, 'def web : Web Member Unit where\n  level t _ := level t\n  active t _ := live t\n' + DRAWS,
            'def web : Web Member Unit := Witnesses.relayWeb level fun t _ => live t', kind='relay')
replace('Exclusion', '''def web : Web Member Unit where
  level t _ := level t
  active t f := match f with
    | .renewer => True
    | .first => True
    | .second => t = 0
''' + DRAWS, '''def web : Web Member Unit := Witnesses.relayWeb level fun t f => match f with
  | .renewer => True
  | .first => True
  | .second => t = 0''', kind='relay')

# --- profiles --------------------------------------------------------------------------------
HEAD = re.compile(r'^(\s*)((?:private )?(?:def|abbrev)) (\S+) : (Nat → (?:Nat|Prop|Bool))\s*$')
CASE = re.compile(r'^\s*\| (?:(\d+)|(?:[a-z_]\w*|_) \+ (\d+)|_) => (\d+|True|False|true|false)\s*$')


def profile_of(cases):
    """values and rest of literal cases, or None."""
    lits, rest = {}, None
    for i, c in enumerate(cases):
        m = CASE.match(c)
        if not m:
            return None
        lit, plus, val = m.groups()
        if lit is not None:
            if rest is not None:
                return None
            lits[int(lit)] = val
        else:
            if i != len(cases) - 1:
                return None
            rest = val
            if plus is not None:
                k = int(plus)
                if sorted(lits) != list(range(k)):
                    return None
                length = k
            else:
                length = max(lits) + 1 if lits else 0
    if rest is None:
        return None
    return [lits.get(i, rest) for i in range(length)], rest


profiles = []
for path in sorted(B.glob('*.lean')):
    mod = path.stem
    # Renewal lies below the frame (it imports the prelude and RelationalRenewal only), so its
    # profile stays a definition by cases.
    if mod in ('Witnesses', 'FallibleInquiry', 'Renewal'):
        continue
    lines = text(mod).split('\n')
    out, i, hit = [], 0, False
    while i < len(lines):
        m = HEAD.match(lines[i])
        if m:
            j = i + 1
            while j < len(lines) and lines[j].strip().startswith('|'):
                j += 1
            got = profile_of(lines[i + 1:j]) if j > i + 1 else None
            if got and j - i - 1 >= 2:
                values, rest = got
                new = f'{m.group(1)}{m.group(2)} {m.group(3)} : {m.group(4)} := Witnesses.profile [{", ".join(values)}] {rest}'
                profiles.append((mod, m.group(3), ' '.join(l.strip() for l in lines[i + 1:j]), new.strip()))
                log.append(('profile', mod, lines[i].strip(), new.strip()))
                out.append(new)
                i, hit = j, True
                continue
        out.append(lines[i])
        i += 1
    if hit:
        changed[mod] = '\n'.join(out)
    elif changed.get(mod) == path.read_text():
        del changed[mod]

# --- imports ---------------------------------------------------------------------------------
index = cb.module_index()
for mod, s in changed.items():
    if 'Witnesses.' not in s:
        continue
    imports = cb.imports_of(s.encode())
    closure = set()
    for imp in imports:
        if imp in index:
            closure |= set(cb.closure(index, [imp]))
    if 'Becoming.Witnesses' not in closure:
        lines = s.split('\n')
        last = max(k for k, l in enumerate(lines[:next(k for k, l in enumerate(lines) if l.strip() and not l.startswith('import '))]) if l.startswith('import '))
        lines.insert(last + 1, 'import Becoming.Witnesses')
        changed[mod] = '\n'.join(lines)
        log.append(('import', mod, '', 'import Becoming.Witnesses'))

print(f'{len(changed)} modules, {len(log)} edits, {len(profiles)} profiles')
if not DRY:
    for mod, s in changed.items():
        (B / f'{mod}.lean').write_text(s)
    with open(HERE / 'b14.log.tsv', 'w') as f:
        for row in log:
            f.write('\t'.join(row).replace('\n', ' ') + '\n')
