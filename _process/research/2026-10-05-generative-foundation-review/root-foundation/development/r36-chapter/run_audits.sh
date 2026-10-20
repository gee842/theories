#!/bin/sh
# R36: the preservation audit of both live editions against their frozen copies (run from the checkout root).
python3 -B _process/research/2026-10-05-generative-foundation-review/root-foundation/development/r36-chapter/audit.py . theories/becoming/history/THE-THEORY-OF-BECOMING-2026-10-20.md theories/becoming/chapters/THE-THEORY-OF-BECOMING.md --json _process/research/2026-10-05-generative-foundation-review/root-foundation/development/r36-chapter/audit-en.json --peer THE-THEORY-OF-BECOMING.zh.md=theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md
echo "en exit $?"
python3 -B _process/research/2026-10-05-generative-foundation-review/root-foundation/development/r36-chapter/audit.py . theories/becoming/history/THE-THEORY-OF-BECOMING-2026-10-20.zh.md theories/becoming/chapters/THE-THEORY-OF-BECOMING.zh.md --mirror --json _process/research/2026-10-05-generative-foundation-review/root-foundation/development/r36-chapter/audit-zh.json --peer THE-THEORY-OF-BECOMING.md=theories/becoming/chapters/THE-THEORY-OF-BECOMING.md
echo "zh exit $?"
