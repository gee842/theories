#!/usr/bin/env python3
"""M3 (18 October 2026): what-pooled-coupling-reaches named "whether a pool's selection responds to what it separates"
as a next step; M3 states what a pool's acts respond to. Update that record's next_delta and related list, with a
history note, before rehash_refs.py runs. usage (from the repository root): python3 -B m2_record_next.py"""
import json

PATH = 'theories/becoming/results/records/what-pooled-coupling-reaches.json'
d = json.load(open(PATH))
OLD_EN = 'whether a pool\'s selection responds to what it separates; '
OLD_ZH = '一组的选择是否回应它所分开者；'
assert d['next_delta']['en'].count(OLD_EN) == 1 and d['next_delta']['zh'].count(OLD_ZH) == 1
d['next_delta']['en'] = d['next_delta']['en'].replace(
    OLD_EN, 'which responses to what a pool separates correct the act (what a pool\'s acts can respond to is stated in '
            'what-a-pools-acts-respond-to); ')
d['next_delta']['zh'] = d['next_delta']['zh'].replace(
    OLD_ZH, '对一组所分开者的哪些回应纠正动作（一组的动作能回应什么，见 what-a-pools-acts-respond-to）；')
assert all(r['id'] != 'what-a-pools-acts-respond-to' for r in d['related'])
d['related'].append({
    'id': 'what-a-pools-acts-respond-to',
    'detail': {'en': 'Derives this record\'s premise that a selection goes through the pooled coupling for what a pool '
                     'decides by its acts, where each member\'s law reads through its coupling, and turns the gap for a '
                     'pool\'s act into the gap for its response.',
               'zh': '每个成员的律都经其耦合而读时，为一组以其动作所决定者推出本成果“选择经合起来的耦合”的前提，并把一组之动作的'
                     '缺口变为其回应的缺口。'}})
d['history'].append({
    'en': '18 October 2026, M3 (Becoming.PoolResponse): next_delta updated, since what-a-pools-acts-respond-to states '
          'what a pool\'s acts can respond to (exactly bounded by the members\' coupling, and not fixed by it); which '
          'responses correct stays open. The claim is unchanged.',
    'zh': '2026年10月18日，M3（Becoming.PoolResponse）：next_delta 更新，因为 what-a-pools-acts-respond-to 陈述了一组的动作能'
          '回应什么（由成员的耦合精确界定，而不由它确定）；哪些回应纠正仍开放。论断不变。'})
open(PATH, 'w').write(json.dumps(d, ensure_ascii=False, indent=2) + '\n')
print('updated', PATH)
