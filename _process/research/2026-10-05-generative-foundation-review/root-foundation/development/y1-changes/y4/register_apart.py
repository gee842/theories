#!/usr/bin/env python3
"""Register Y4's apart roots in THEOREM-CONNECTIVITY-APART.json: what the 彖, the 小象, the 文言 and the line texts say
of named configurations, the censuses, 王弼's argument as a fact about the text's statements, and the witnesses and
census of the twelve configurations with a sole line. Each is a fact about configurations of the text or about its
lists, checked on them; the relations they instance are read on the base along runs.
usage: python3 -B register_apart.py [CHECKOUT_ROOT]"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else HERE.parents[6]
REG = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY-APART.json'
MOD = 'Becoming.HexagramSites'
TEXT = ('what the {where} says of {what}: a fact about one configuration of the text, checked on it; the relation it '
        'instances is read on the base by {law}')
CENSUS = ('the census of the {where}\'s statements {what} holds of each listed configuration: a fact about the '
          'text\'s list, found in the preserved pages by verify_mapping.py and checked here; the relation is read on '
          'the base by {law}')
TWELVE = ('{what}: a fact about the twelve configurations with a sole line, checked on each; the sole line is read on '
          'the base by sole_shown_along_run and run_sole')
ENTRIES = {
    'top_no_parity': ('model-witness', '王弼\'s dilemma (辯位): no parity of the top place leaves both 需\'s and 乾\'s '
                      'top lines out of phase, as the 小象 and the 文言 say they are; a fact about two configurations of '
                      'the text, checked on them; the second relation is read on the base by between_shown_along_runs'),
    'statements_fix_parity': ('model-witness', 'every parity on which the 小象\'s statements of place hold gives places 3, '
                              '4 and 5 the parity of odd: a fact about the text\'s list, checked on three of its '
                              'statements; the phases are read on the base by run_between_rises'),
    'centre_fixes_parity': ('model-witness', 'every parity on which the 小象\'s statements of 中正 hold gives place 2 '
                            'the parity of odd: a fact about the text\'s list, checked on one of its statements; the '
                            'phases are read on the base by run_between_rises'),
    'placeStatements_between': ('model-witness', CENSUS.format(where='小象', what='of place (位當, 位不當, ...), each '
                                                               'between the ends', law='changes_run_between')),
    'placeStatements_hold': ('model-witness', CENSUS.format(where='小象', what='of place with 乾\'s and 需\'s top lines, '
                                                            'under the second relation',
                                                            law='between_shown_along_runs and changes_run_between')),
    'xu_top_no_place': ('model-witness', TEXT.format(where='小象', what='需\'s top line (雖不當位), under the second '
                                                     'relation', law='between_shown_along_runs')),
    'qian_top': ('model-witness', TEXT.format(where='文言', what='乾\'s top line (貴而无位)', law='between_shown_along_runs')),
    'tuanPlaceStatements_agree': ('model-witness', CENSUS.format(where='彖', what='of the place of one line',
                                                                 law='between_shown_along_runs')),
    'tuanWhole_between': ('model-witness', CENSUS.format(where='彖', what='of the place of the whole configuration, '
                                                         'between the ends', law='between_glue_along_run')),
    'tuanWhole_six': ('model-witness', 'the 彖\'s statements of the place of the whole read at six places: three of five '
                      'fail on their configurations, a fact about the text\'s list checked on them; the second relation '
                      'is read on the base by between_glue_along_run'),
    'answeredStatements_sole': ('model-witness', CENSUS.format(where='彖', what='of 上下應', law='sole_shown_along_run')),
    'xiaoXu_answered': ('model-witness', TEXT.format(where='彖', what='小畜\'s fourth line (上下應之)',
                                                     law='sole_shown_along_run')),
    'daYou_answered': ('model-witness', TEXT.format(where='彖', what='大有\'s fifth line (上下應之)',
                                                    law='sole_shown_along_run')),
    'guai_sole': ('model-witness', TEXT.format(where='彖', what='夬\'s top line (柔乘五剛)', law='sole_shown_along_run')),
    'lv_sole': ('model-witness', 'what 王弼\'s 略例下 says of 履\'s third line (成卦之體，在斯一爻): a fact about one '
                'configuration of the text, checked on it; the sole line is read on the base by sole_shown_along_run'),
    'feng_no_sole': ('model-witness', 'what 王弼\'s 略例下 says of 豐 (read by its two trigrams): a fact about one '
                     'configuration of the text, checked on it; the sole line is read on the base by '
                     'sole_shown_along_run'),
    'lineTextMiddle_places': ('model-witness', CENSUS.format(where='line texts', what='of 中 and 中行',
                                                             law='between_shown_along_runs')),
    'lineTextPlace_holds': ('model-witness', CENSUS.format(where='line texts', what='of 位 (萃有位)',
                                                           law='between_shown_along_runs')),
    'jie_one_opposed': ('model-witness', '節 is opposed at one height and has no sole line: a witness that one opposed '
                        'height does not make a sole line, checked on one configuration; the sole line is read on the '
                        'base by sole_shown_along_run'),
    'sole_any_phase': ('model-witness', TWELVE.format(what='at every place and with either phase there is a '
                                                      'configuration with a sole line')),
    'sole_places': ('model-witness', TWELVE.format(what='of the twelve, four hold their place between the ends, four '
                                                   'are out of phase there and four are at the ends')),
}
data = json.loads(REG.read_text())
for name, (category, reason) in ENTRIES.items():
    full = f'Becoming.Hexagram.{name}'
    assert full not in data['roots'], full
    data['roots'][full] = {'module': MOD, 'category': category, 'reason': reason[0].upper() + reason[1:] + '.'}
REG.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n')
print('registered', len(ENTRIES))
