"""R36: freeze the canonical chapter's two editions into history, keeping references.

The same move as `research.py move --plan freeze-plan.tsv --keep-references --batch R36-chapter`,
with one difference: `move_pinned` in _process/research-config.json pins the canonical chapter's path
so that it is never moved by accident. Here the path is vacated on purpose and receives the
restructured chapter at once, every inbound link kept (`--keep-references`), so the pin is lifted for
this plan only; the configuration file is not changed. Without --apply it prints the dry run.

Usage: python3 -B freeze.py [--apply]
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
sys.path[:0] = [str(ROOT), str(ROOT / 'tools' / 'research')]
from tools.research import moves  # noqa: E402
from tools.research import paths as path_roles  # noqa: E402

LIFTED = 'theories/becoming/chapters/THE-THEORY-OF-BECOMING.md'


def main():
    settings = path_roles.load_config(ROOT)
    settings = dict(settings)
    settings['move_pinned'] = [p for p in settings.get('move_pinned', []) if p != LIFTED]
    entries = moves.Plan.read(HERE / 'freeze-plan.tsv')
    plan = moves.Plan(entries, root=ROOT, settings=settings, batch='R36-chapter', plan_name='freeze-plan',
                      keep_references=True).analyse()
    if '--apply' in sys.argv:
        result = plan.apply()
    else:
        result = plan.report(full=False)
        result['applied'] = False
    print(json.dumps(result, ensure_ascii=False, indent=1)[:6000])


if __name__ == '__main__':
    main()
