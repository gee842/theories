#!/bin/sh
# Draft build with Tectonic (XeTeX), for checking only. Submit a pdfLaTeX build of submission/ (e.g. on Overleaf).
set -e
cd "$(dirname "$0")"
python3 figures.py
cp fig-capacity.tex fig-field.tex fig-hysteresis.tex tab-robust.tex ../submission/
rm -rf out && mkdir out
cp ../submission/references.bib ../submission/fig-*.tex ../submission/tab-robust.tex ../submission/aaai2027.bst aaai2027x.sty out/
sed -e 's/{aaai2027}/{aaai2027x}/' ../submission/main.tex > out/main.tex
cd out && ${TECTONIC:-tectonic} main.tex
