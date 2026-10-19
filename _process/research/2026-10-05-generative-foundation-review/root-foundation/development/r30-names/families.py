"""R30 check: theorems not in the table whose name carries the old word of a renamed definition and whose
statement uses that definition (candidates for a family row). Read-only; prints the candidates."""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from parse import strip_comments  # noqa: E402

d = json.load(open(HERE + '/decls.json'))['decls']
t = json.load(open(HERE + '/rename-draft.json'))
REN = {r['old_full_name']: r['new_full_name'] for r in t if r['kind'] == 'decl' and r['decision'].startswith('apply')}
words = {'Web.Returns': 'returns', 'Web.ReturnsWithin': 'returns', 'Becoming.Returns': 'returns',
         'Flow.Lossless': 'lossless', 'Flow.LosslessOn': 'lossless', 'HistoryIdeals.Settles': 'settles',
         'Stretches.Settles': 'settles', 'Learnable.RestsFrom': 'rests', 'Learnable.Rests': 'rests',
         'LearnableRuns.RestsFrom': 'rests', 'LearnableRuns.Rests': 'rests', 'Ideals.Closed': 'closed',
         'ReferencePlan.Alike': 'alike', 'Contacts.Alike': 'alike', 'Joining.Neutral': 'neutral',
         'RuleCapture.Counts': 'counts', 'Countdown.Counts': 'counts', 'SharedCodes.Image': 'image',
         'Registration.History': 'history', 'Flow.history': 'history', 'Activation.History': 'history',
         'ExchangeLaw.generation': 'generation', 'SharedCodes.generation': 'generation', 'Becoming.G0': 'g0',
         'Valuation.SelfGood': 'selfgood', 'ProfileReach.SelfGood': 'selfgood',
         'Becoming.SecuresPositiveGround': 'positive', 'Onward.DependentSelection': 'selection',
         'Web.Regenerating': 'regenerat'}
for x in d:
    if x['full'] in REN:
        continue
    nm = x['full'].rsplit('.', 1)[-1].lower().replace('_', '')
    stmt = strip_comments(x['text']).split(':=')[0]
    for k, w in words.items():
        last = k.rsplit('.', 1)[-1]
        if w in nm and re.search(r'(?<![\w])' + re.escape(last) + r'(?![\w])', stmt):
            print(x['full'], '|', k, '|', ' '.join(stmt.split())[:150])
