"""Build the PDF of *Shengsheng Buxi: A Theory of Unceasing Generation* (English edition, 2026-10).

Source: drafts/2026-10-02-shengsheng-en/parts/*.md, concatenated into Shengsheng-Buxi-EN.md.
Rendering: a small markdown-to-HTML converter, then headless Google Chrome print-to-PDF
(same approach as build_xiaokang_datong.py).
Run from the repo root:  python3 tmp/pdfs/build_shengsheng_en.py
"""
import html
import pathlib
import re
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from build_xiaokang_datong import fix_tounicode  # noqa: E402  (normalizes CJK radicals in ToUnicode maps)

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC_DIR = ROOT / "drafts" / "2026-10-02-shengsheng-en"
PARTS = SRC_DIR / "parts"
BOOK_MD = SRC_DIR / "Shengsheng-Buxi-EN.md"
OUT = ROOT / "output" / "pdf" / "Shengsheng-Buxi-EN-2026-10.pdf"
BUILD = ROOT / "tmp" / "pdfs" / "shengsheng-en"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

TITLE = "Shengsheng Buxi"
SUBTITLE = "A Theory of Unceasing Generation"
SUBSUB = "Life, selection, intelligence, and the conditions that keep a world open"
EDITION = "ENGLISH EDITION · OCTOBER 2026"
RUNNING = "Shengsheng Buxi · A Theory of Unceasing Generation"


def assemble() -> str:
    text = "\n\n".join(p.read_text(encoding="utf-8").rstrip() for p in sorted(PARTS.glob("*.md"))) + "\n"
    BOOK_MD.write_text(text, encoding="utf-8")
    return text


def inline(text: str) -> str:
    t = html.escape(text, quote=False)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    return t


def convert(md: str):
    lines = md.split("\n")
    # The cover carries the title block: drop everything before the first epigraph.
    start = next(i for i, l in enumerate(lines) if l.startswith(">"))
    body = lines[start:]
    out, toc = [], []
    i, n = 0, 0
    para: list[str] = []
    mode = "body"  # body | skip | refs

    def flush():
        nonlocal para
        if not para:
            return
        text = " ".join(para).strip()
        para = []
        if mode == "refs":
            out.append(f'<p class="ref">{inline(text)}</p>')
        elif re.fullmatch(r"\*[^*].*\*", text) and len(text) < 140:
            out.append(f'<p class="formula">{inline(text)}</p>')
        else:
            out.append(f"<p>{inline(text)}</p>")

    while i < len(body):
        l = body[i]
        if mode == "skip":
            if l.strip() == "---":
                mode = "body"
                out.append("<!--TOC-->")
            i += 1
            continue
        if l.startswith("# "):
            flush()
            n += 1
            title = l[2:].strip()
            mode = "refs" if title == "References" else "body"
            toc.append((f"s{n}", title, 1))
            out.append(f'<h1 class="part" id="s{n}">{inline(title)}</h1>')
        elif l.startswith("## "):
            flush()
            title = l[3:].strip()
            if title == "Contents":
                mode = "skip"
                i += 1
                continue
            n += 1
            cls = "chapter" if (re.match(r"^\d+\.", title) or title.startswith(("Prologue", "Epilogue", "Appendix", "A note"))) else "sub"
            if mode == "refs":
                cls = "sub"
            toc.append((f"s{n}", title, 2))
            out.append(f'<h2 class="{cls}" id="s{n}">{inline(title)}</h2>')
        elif l.startswith("### "):
            flush()
            out.append(f"<h3>{inline(l[4:].strip())}</h3>")
        elif l.startswith(">"):
            flush()
            quote = []
            while i < len(body) and body[i].startswith(">"):
                quote.append(body[i][1:].strip())
                i += 1
            blocks, cur = [], []
            for q in quote:
                if q:
                    cur.append(q)
                elif cur:
                    blocks.append(cur)
                    cur = []
            if cur:
                blocks.append(cur)
            inner = "".join("<p>" + "<br/>".join(inline(x) for x in b) + "</p>" for b in blocks)
            out.append(f'<blockquote class="epigraph">{inner}</blockquote>')
            continue
        elif l.strip() == "---":
            flush()  # section rules are for the markdown only; the PDF uses page breaks
        elif l.startswith("- "):
            flush()
            items = []
            while i < len(body) and body[i].startswith("- "):
                items.append(body[i][2:])
                i += 1
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>")
            continue
        elif l.startswith("|"):
            flush()
            rows = []
            while i < len(body) and body[i].startswith("|"):
                rows.append([c.strip() for c in body[i].strip().strip("|").split("|")])
                i += 1
            head, rest = rows[0], [r for r in rows[1:] if not set("".join(r)) <= set("-: ")]
            cols = len(head)
            t = f'<table class="c{cols}"><thead><tr>' + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>"
            t += "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in rest)
            out.append(t + "</tbody></table>")
            continue
        elif not l.strip():
            flush()
        else:
            para.append(l.strip())
        i += 1
    flush()
    return "\n".join(out), toc


CSS = """
:root { --serif: "Iowan Old Style", "Charter", Georgia, "Songti SC", serif;
        --sans: "Avenir Next", "Helvetica Neue", "PingFang SC", sans-serif;
        --ink: #1f1c18; --muted: #6e675d; --rule: #c9bfae; --accent: #8c2f1e; }
@page { size: A4; margin: 24mm 23mm 22mm 23mm;
  @top-center { content: "RUNNING"; font-family: var(--sans); font-size: 7.5pt; color: #8a8378; letter-spacing: .06em; }
  @bottom-center { content: counter(page); font-family: var(--sans); font-size: 8pt; color: #8a8378; } }
@page :first { margin: 0; @top-center { content: none; } @bottom-center { content: none; } }
html { color: var(--ink); background: #fff; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { margin: 0; font-family: var(--serif); font-size: 10.8pt; line-height: 1.58; text-align: justify; hyphens: auto;
  font-variant-ligatures: no-common-ligatures; font-feature-settings: "liga" 0, "clig" 0; }
.cover { text-align: left; hyphens: none; height: 297mm; box-sizing: border-box; padding: 58mm 26mm 30mm 26mm;
  display: flex; flex-direction: column; page-break-after: always; background: #f7f3ea; }
.cover .edition { font-family: var(--sans); font-size: 9pt; letter-spacing: .12em; color: var(--muted); }
.cover h1 { font-size: 36pt; line-height: 1.1; margin: 14mm 0 4mm; font-weight: 600; }
.cover .zh { font-family: "Songti SC", "STSong", serif; font-size: 20pt; letter-spacing: .3em; color: var(--accent); margin-bottom: 8mm; }
.cover .subtitle { font-size: 17pt; line-height: 1.4; color: var(--ink); }
.cover .subsub { font-size: 12pt; line-height: 1.5; color: var(--muted); margin-top: 3mm; max-width: 140mm; }
.cover .bar { width: 22mm; height: 2px; background: var(--accent); margin: 16mm 0 0; }
.cover .motto { margin-top: auto; font-size: 11pt; line-height: 1.8; max-width: 135mm; }
.toc { page-break-before: always; page-break-after: always; }
.toc h2 { border: none; margin-top: 0; }
.toc ol { list-style: none; padding: 0; margin: 0; }
.toc li { padding: 1.2mm 0; border-bottom: .5px solid #ece6da; font-size: 10pt; text-align: left; }
.toc li.l1 { font-family: var(--sans); font-weight: 600; font-size: 9pt; letter-spacing: .04em; color: var(--muted); padding-top: 4mm; border-bottom: none; }
.toc li.l2 { padding-left: 4mm; }
.toc a { color: var(--ink); text-decoration: none; }
blockquote.epigraph { margin: 0 0 0 0; padding: 40mm 8mm 0 8mm; text-align: left; font-size: 11pt; line-height: 1.7; page-break-after: always; }
blockquote.epigraph p { margin: 0 0 9mm; }
h1.part { page-break-before: always; font-size: 21pt; font-weight: 600; margin: 50mm 0 18mm; text-align: left; letter-spacing: .01em; color: var(--accent); }
h2 { font-size: 16pt; line-height: 1.35; font-weight: 600; margin: 12mm 0 6mm; padding-bottom: 2.5mm; border-bottom: .6px solid var(--rule); page-break-after: avoid; text-align: left; }
h2.chapter { page-break-before: always; margin-top: 8mm; }
h1.part + h2.chapter { page-break-before: avoid; }
h2.sub { font-size: 13pt; border-bottom: none; }
h3 { font-size: 11.6pt; font-weight: 600; margin: 7mm 0 2.5mm; color: #3b342c; page-break-after: avoid; text-align: left; }
p { margin: 0 0 3.2mm; orphans: 2; widows: 2; }
p.formula { text-align: center; margin: 4mm 0 5mm; font-size: 1.04em; }
p.ref { text-align: left; font-size: .86em; line-height: 1.5; padding-left: 6mm; text-indent: -6mm; margin-bottom: 1.8mm; hyphens: none; }
strong { font-weight: 600; }
a { color: var(--accent); text-decoration: none; }
ul { margin: 0 0 3.5mm; padding-left: 6mm; }
li { margin: 0 0 1.6mm; }
table { width: 100%; border-collapse: collapse; margin: 3mm 0 5mm; font-size: .86em; line-height: 1.4; page-break-inside: avoid; text-align: left; hyphens: none; }
table.c5 { font-size: .78em; }
th, td { vertical-align: top; padding: 1.8mm 2mm; border-bottom: .5px solid #d9d0c0; }
th { font-family: var(--sans); font-weight: 600; font-size: .9em; color: var(--muted); border-bottom: .8px solid var(--rule); }
td:first-child { font-weight: 600; }
hr.end { border: none; border-top: .6px solid var(--rule); margin: 10mm 0 6mm; }
"""


def build() -> None:
    md = assemble()
    body, toc = convert(md)
    toc_html = '<section class="toc"><h2>Contents</h2><ol>' + "".join(
        f'<li class="l{lvl}"><a href="#{a}">{inline(t)}</a></li>'
        for a, t, lvl in toc if not t.startswith("A note")) + "</ol></section>"
    body = body.replace("<!--TOC-->", toc_html, 1)
    css = CSS.replace("RUNNING", RUNNING)
    motto = ("Keep the conditions of becoming alive. Do not close the world.")
    doc = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>{TITLE} — {SUBTITLE}</title><style>{css}</style></head><body>
<section class="cover"><div class="edition">{EDITION}</div><h1>{TITLE}</h1>
<div class="zh">生生不息论</div>
<div class="subtitle">{SUBTITLE}</div><div class="subsub">{SUBSUB}</div><div class="bar"></div>
<div class="motto">{motto}</div></section>
<main>{body}</main></body></html>"""
    BUILD.mkdir(parents=True, exist_ok=True)
    page = BUILD / "en.html"
    page.write_text(doc, encoding="utf-8")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    if OUT.exists():
        OUT.unlink()
    # Chrome sometimes exits non-zero on teardown after writing the file; judge by the output.
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    "--run-all-compositor-stages-before-draw", "--virtual-time-budget=8000",
                    f"--print-to-pdf={OUT}", page.as_uri()],
                   check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if not OUT.exists() or OUT.stat().st_size == 0:
        raise SystemExit("Chrome did not write the PDF")
    fixed = fix_tounicode(OUT)
    print("wrote", OUT, f"({fixed} glyph mappings normalized)")


if __name__ == "__main__":
    build()
