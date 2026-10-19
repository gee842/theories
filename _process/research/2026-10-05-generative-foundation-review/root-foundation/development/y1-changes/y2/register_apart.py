#!/usr/bin/env python3
"""Register Y2's apart roots in THEOREM-CONNECTIVITY-APART.json: what the 彖 and the 象 say of named configurations and
the four censuses (facts about the text's configurations, checked on them), and the six-step law on the orbit, which
the base states along every run. usage: python3 -B register_apart.py [CHECKOUT_ROOT]"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else HERE.parents[6]
REG = ROOT / '_process/research/2026-10-05-generative-foundation-review/root-foundation/THEOREM-CONNECTIVITY-APART.json'
MOD = 'Becoming.HexagramPlaces'
TEXT = ('what the {where} says of {what}: a fact about one configuration of the text, checked on it; the laws it '
        'instances are read on the base by {law}')
CENSUS = ('the census of the {where}\'s statements {what} holds of each listed configuration: a fact about the '
          'text\'s list, found in the preserved pages by verify_mapping.py and checked here; the relation is read on '
          'the base by {law}')
ENTRIES = {
    'weiJi_opposed': ('model-witness', TEXT.format(where='彖', what='未濟 (剛柔應)', law='shown_along_run')),
    'heng_opposed': ('model-witness', TEXT.format(where='彖', what='恒 (剛柔皆應)', law='shown_along_run')),
    'xian_opposed': ('model-witness', TEXT.format(where='彖', what='咸 (二氣感應)', law='shown_along_run')),
    'gen_halves_glue': ('model-witness', TEXT.format(where='彖', what='艮 (上下敵應)', law='run_doubled_three')),
    'tongRen_second': ('model-witness', TEXT.format(where='彖', what='同人\'s second line', law='shown_along_run')),
    'xiaoXu_fourth': ('model-witness', TEXT.format(where='彖', what='小畜\'s fourth line', law='shown_along_run')),
    'daYou_fifth': ('model-witness', TEXT.format(where='彖', what='大有\'s fifth line', law='shown_along_run')),
    'guiMei_falls': ('model-witness', TEXT.format(where='彖', what='歸妹 (柔乘剛)', law='run_carried')),
    'guai_falls': ('model-witness', TEXT.format(where='彖', what='夬 (柔乘五剛)', law='run_carried')),
    'xu_top_inPhase': ('model-witness', TEXT.format(where='小象', what='需\'s top line, where it parts from the parity '
                                                    'of its place', law='run_phase_rises')),
    'gen_fifth_out_of_phase': ('model-witness', TEXT.format(where='小象', what='艮\'s fifth line, where it parts from '
                                                            'the parity of its place', law='run_phase_rises')),
    'placeStatements_agree': ('model-witness', CENSUS.format(where='小象', what='of place (位當, 位不當, ...)',
                                                             law='run_phase_rises and changes_run_phase')),
    'centreStatements_agree': ('model-witness', CENSUS.format(where='小象', what='of 中正 and 正中',
                                                              law='run_phase_rises')),
    'fallStatements_agree': ('model-witness', CENSUS.format(where='小象', what='of 乘剛', law='run_carried')),
    'middleOppositionStatements_agree': ('model-witness', CENSUS.format(where='彖', what='of 剛中而應',
                                                                        law='shown_along_run')),
    'opposition_six': ('restates', 'six steps of the law keep every opposition: restated on the base by run_six_keeps, '
                                   'the same law along every run of waxing and waning, derived there from the phases'),
}
data = json.loads(REG.read_text())
for name, (category, reason) in ENTRIES.items():
    full = f'Becoming.Hexagram.{name}'
    assert full not in data['roots'], full
    data['roots'][full] = {'module': MOD, 'category': category, 'reason': reason[0].upper() + reason[1:] + '.'}
REG.write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n')
print('registered', len(ENTRIES))
