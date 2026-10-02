#!/bin/sh
# Draft build. Regenerates the figures and every quoted number, then compiles a
# draft PDF with Tectonic (XeTeX). The AAAI style requires pdfLaTeX, so the
# draft uses aaai2027x.sty, which is aaai2027.sty with only the engine check
# (\RequirePDFTeX) commented out; page layout is unchanged. Build the version
# you submit from ../submission/ with pdfLaTeX (for example on Overleaf),
# using the unmodified aaai2027.sty.
set -e
cd "$(dirname "$0")"
python3 figures.py                      # writes fig-*.tex and checks.log; reuses hyst-cache.json if present
cp fig-field.tex fig-hysteresis.tex ../submission/
rm -rf out && mkdir out
cp ../submission/references.bib ../submission/fig-*.tex ../submission/aaai2027.bst aaai2027x.sty out/
sed -e 's/{aaai2027}/{aaai2027x}/' ../submission/main.tex > out/main.tex
cd out && ${TECTONIC:-tectonic} main.tex
echo "draft PDF: $(pwd)/main.pdf"
