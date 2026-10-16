#!/bin/sh
# Draft build with Tectonic (XeTeX), for checking only. Submit a pdfLaTeX build (e.g. on Overleaf).
set -e
cd "$(dirname "$0")"
python3 figures_v3.py > /dev/null && python3 checks_v31.py > /dev/null
rm -rf out && mkdir out
cp references.bib fig-rate.tex aaai2027.bst aaai2027x.sty out/
sed -e 's/{aaai2027}/{aaai2027x}/' main.tex > out/main.tex
cd out && ${TECTONIC:-/Applications/ChatGPT.app/Contents/Resources/tectonic/tectonic} main.tex 2>&1 | grep -E "warning|error|Error|!" | grep -v "Underfull\|Overfull" | head -40
