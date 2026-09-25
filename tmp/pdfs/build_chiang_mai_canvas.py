from pathlib import Path
import re
from xml.sax.saxutils import escape

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from pypdf import PdfReader

ROOT = Path('/Users/ren/theories')
OUT = ROOT / 'output/pdf'
SOURCE = OUT / 'generative-chiang-mai-2045.md'
PDF = OUT / 'generative-chiang-mai-2045.pdf'

FONTDIR = Path('/System/Library/Fonts/Supplemental')
for name, filename in [('Body', 'Arial.ttf'), ('BodyBold', 'Arial Bold.ttf'),
                       ('BodyItalic', 'Arial Italic.ttf'),
                       ('Heading', 'DIN Condensed Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(FONTDIR / filename)))
pdfmetrics.registerFontFamily('Body', normal='Body', bold='BodyBold', italic='BodyItalic', boldItalic='BodyBold')

W, H = 1440, 809
PLUM = HexColor('#6A4963')
PALE = HexColor('#E2DDE1')
GOLD = HexColor('#F3D28D')
INK = HexColor('#352E37')
MUTED = HexColor('#8F8690')

c = canvas.Canvas(str(PDF), pagesize=(W, H))
c.setTitle('Generative Chiang Mai 2045: A City of Many Beginnings')
c.setAuthor("Ren's vision; synthesis drafted with Codex")
c.setSubject('Completed Cosmolocal CNX Fiction Canvas; speculative 2045 scenario')

def rect(x, top, width, height, fill, stroke=None, radius=0):
    c.setFillColor(fill)
    c.setStrokeColor(stroke or fill)
    if radius:
        c.roundRect(x, H-top-height, width, height, radius, stroke=bool(stroke), fill=1)
    else:
        c.rect(x, H-top-height, width, height, stroke=bool(stroke), fill=1)

def line(x1, y1, x2, y2):
    c.setStrokeColor(PLUM)
    c.setLineWidth(1.2)
    c.line(x1, H-y1, x2, H-y2)

def text(txt, x, top, font='Body', size=14, color=INK):
    c.setFont(font, size)
    c.setFillColor(color)
    c.drawString(x, H-top-size, txt)

def paragraph(txt, x, top, width, max_height, size=13.4, leading=17.5, color=INK, font='Body'):
    style = ParagraphStyle('p', fontName=font, fontSize=size, leading=leading,
                           textColor=color, spaceAfter=0, allowWidows=0, allowOrphans=0)
    p = Paragraph(txt, style)
    _, height = p.wrap(width, max_height)
    if height > max_height + .01:
        raise ValueError(f'Text overflow: {height} > {max_height}: {txt[:90]}')
    p.drawOn(c, x, H-top-height)
    return height

md = SOURCE.read_text()
def section(heading):
    return md.split('## '+heading+'\n\n', 1)[1].split('\n## ', 1)[0].strip()

# Re-created vector worksheet: the supplied image is the layout reference.
rect(18, 13, 302, 44, GOLD, radius=8)
text('NAME', 34, 26, 'Heading', 17, PLUM)
text('Ren', 100, 24, 'BodyBold', 19, PLUM)
c.setFont('Heading', 20)
c.setFillColor(PLUM)
c.drawRightString(1395, H-43, 'COSMOLOCAL CNX FICTION CANVAS')

L, R = 48, 1394
X1, X2 = L + (R-L)/3, L + 2*(R-L)/3
rect(L, 78, R-L, 77, PALE)
rect(L, 239, R-L, 101, PALE)
rect(L, 477, R-L, 77, PALE)
for y in [78, 155, 239, 340, 477, 554, 756]:
    line(L, y, R, y)
line(L, 78, L, 756)
line(R, 78, R, 756)
for x in [X1, X2]:
    line(x, 239, x, 477)

text('TITLE', 63, 92, 'Heading', 21, PLUM)
text('write this at end once story has taken shape', 63, 122, 'BodyItalic', 15, PLUM)
text('GENERATIVE CHIANG MAI 2045: A CITY OF MANY BEGINNINGS', 65, 169, 'Heading', 29, PLUM)
paragraph('Shared abundance, mutual care and a regenerative culture give diverse people and communities the means to cultivate a flourishing world together.',
          65, 209, 1304, 23, size=14.3, leading=18)

headers = [
    ('WORLD / SITUATION / SCENARIO, 2045',
     'what has transpired in the larger world or context?<br/>pick 1-2 focal dynamics, no need to be comprehensive'),
    ('ADAPTABILITY / FLOURISHABILITY',
     'how is this chiang mai able to thrive in this world?<br/>(from an adaptation / evolutionary / fitness pov)'),
    ('BECOMING / HOW THIS CAPABILITY GREW',
     'how has this capability developed?<br/>(practices, routines, enablers, beginnings / seeds)'),
]
for x, (head, desc) in zip([L, X1, X2], headers):
    text(head, x+15, 254, 'Heading', 19.2, PLUM)
    paragraph(desc, x+15, 282, (R-L)/3-30, 49, size=14.3, leading=23, color=PLUM, font='BodyItalic')

for x, heading in zip([L, X1, X2], ['World / Situation / Scenario, 2045', 'Adaptability / Flourishability', 'Becoming / How This Capability Grew']):
    paragraph(escape(section(heading)), x+15, 351, (R-L)/3-30, 116, size=13.2, leading=16.5)

text('STORY', 63, 492, 'Heading', 21, PLUM)
paragraph('use chronological bullets, as told from 2045 looking back: how did we (begin to) grow into this adaptable condition? what seeds did it start with? what was the journey like?',
          63, 521, 1316, 24, size=14, leading=18, color=PLUM, font='BodyItalic')

story = section('Story').split('\n---', 1)[0]
items = [s[2:] for s in story.splitlines() if s.startswith('- ')]
y = 567
for item in items:
    rich = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', escape(item))
    c.setFillColor(PLUM)
    c.circle(66, H-y-7, 2, fill=1, stroke=0)
    height = paragraph(rich, 78, y, 1297, 39, size=13.2, leading=16.4)
    y += height + 3.1
if y > 750:
    raise ValueError(f'Story overflows bottom boundary: {y}')

c.setFont('Body', 8.4)
c.setFillColor(MUTED)
c.drawCentredString(W/2, 21,
    "SPECULATIVE 2045 SCENARIO  |  REN'S THEORIES  |  Worksheet: COSMOLOCAL CNX / SEAPUNK STUDIOS, SEP 2026")
c.showPage()
c.save()

r = PdfReader(PDF)
assert len(r.pages) == 1
extracted = ' '.join(r.pages[0].extract_text().split())
for required in ['Ren', 'MANY BEGINNINGS', '2026-2029', '2043-2045', 'Ping River', 'future generations', 'shared prosperity and mutual care', 'Climate recovery is underway']:
    assert required in extracted, required
print(f'Created {PDF}; one page; story ends at {y:.1f}/750 points.')
