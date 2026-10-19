"""W2 at landing (19 October 2026): extend the move plan made on d22626bf0 to the re-plan on the landing tree.

usage: w2_landing_move.py KIT PLAN JOINTPLANS_HEADER OUT"""
import json, sys
kit, plan_path = sys.argv[1], sys.argv[2]
old = json.load(open(kit + '/w2/w2-move.json'))
plan = json.load(open(plan_path))
new = dict(old)
assert all(plan['moves'].get(k) == v for k, v in old['moves'].items()), 'an implemented move changed'
new['moves'] = plan['moves']
new['headers'] = dict(old['headers'])
new['headers']['Becoming.JointPlans'] = open(sys.argv[3]).read().rstrip('\n')
new['imports'] = dict(old['imports'])
new['imports']['Becoming.JointPlans'] = []
assert plan['new_modules'] == {'Becoming.ValuationFrames': old['imports']['Becoming.ValuationFrames']}, plan['new_modules']
so = dict(old['source_order'])
so['Becoming.Decidedness'] = ['Becoming.Likeness', 'Becoming.Joining', 'Becoming.Coverage']
so['Becoming.FrontierFrames'] = ['Becoming.Lexical', 'Becoming.Frontier']
so['Becoming.JointPlans'] = ['Becoming.Composition']
new['source_order'] = so
t = dict(old['titles'])
t['Becoming.Composition>Becoming.JointPlans'] = 'Nested decompositions and exclusive footprints (moved from `Becoming.Composition`)'
t['Becoming.Joining>Becoming.Decidedness'] = 'Lists joined in either grouping (moved from `Becoming.Joining`)'
t['Becoming.Coverage>Becoming.Decidedness'] = 'Membership kept under reordering (moved from `Becoming.Coverage`)'
t['Becoming.Lexical>Becoming.FrontierFrames'] = 'Two tiers on a frame (moved from `Becoming.Lexical`)'
t['Becoming.Frontier>Becoming.FrontierFrames'] = ('The formation witness as a process and on its frame, and a requirement '
                                                 'through a summary (moved from `Becoming.Frontier`)')
new['titles'] = t
pairs = {f'{s}>{d}' for s, d in plan['moves'].values()}
missing = sorted(p for p in pairs if p not in t)
assert not missing, missing
covered = {(s, d) for d, ss in so.items() for s in ss}
assert {tuple(v) for v in plan['moves'].values()} <= covered, sorted({tuple(v) for v in plan['moves'].values()} - covered)
json.dump(new, open(sys.argv[4], 'w'), indent=1, ensure_ascii=False)
print('moves', len(new['moves']), 'targets', len(so))
