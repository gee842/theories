#!/usr/bin/env python3
"""Build the illustrated worldbook from editable copy and preserved concept art.

Requires reportlab. See README.md for the bundled runtime command and fonts.
Images are placed as document layout assets; the originals are not modified.
"""
from pathlib import Path
from io import BytesIO
import argparse
import json
from xml.sax.saxutils import escape

from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image

ROOT = Path(__file__).resolve().parent
DEFAULT_FONTS = Path('/Users/ren/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/libreoffice-headless/libreoffice/LibreOfficeDev.app/Contents/Resources/fonts/truetype')
parser = argparse.ArgumentParser()
parser.add_argument('--font-dir', type=Path, default=DEFAULT_FONTS)
args = parser.parse_args()
for name, file in [('Serif','NotoSerif-Regular.ttf'),('SerifItalic','NotoSerif-Italic.ttf'),('Sans','NotoSans-Regular.ttf'),('SansBold','NotoSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(args.font_dir / file)))
pdfmetrics.registerFontFamily('Sans', normal='Sans', bold='SansBold')
pdfmetrics.registerFontFamily('Serif', normal='Serif', italic='SerifItalic')

BOOK = json.loads((ROOT / 'content.json').read_text(encoding='utf-8'))
PAGES = {p['id']: p for p in BOOK['pages']}
OUT = ROOT / 'output/pdf/worlds-we-can-inhabit.pdf'
OUT.parent.mkdir(parents=True, exist_ok=True)
QA = ROOT / 'tmp/pdfs'
QA.mkdir(parents=True, exist_ok=True)
W, H, M = 540, 720, 38
CW = W - 2*M
INK = HexColor('#203C32')
PAPER = HexColor('#F5F1E8')
SOFT = HexColor('#E8E9DF')
MUTED = HexColor('#576C5D')
LINE = HexColor('#C2CCBD')
TERRA = HexColor('#AB593A')
LIGHT = HexColor('#F5F1E8')
layout = []
page_num = 0
image_cache = {}

c = canvas.Canvas(str(OUT), pagesize=(W,H), pageCompression=1)
c.setTitle(BOOK['title'])
c.setAuthor('Ren; developed with AI')
c.setSubject('An illustrated invitation to a speculative, regenerative future')
c.setCreator('Worldbuilding / ReportLab')

def norm(s):
    return s.replace('\u2011','-').replace('\u2013','-').replace('\u2014','-')

def record(kind,x,top,w,h,label=''):
    if x < -0.1 or top < -0.1 or x+w > W+0.1 or top+h > H+0.1:
        raise ValueError(f'Page {page_num}: outside page: {label} at {(x,top,w,h)}')
    layout.append(dict(page=page_num,kind=kind,x=x,top=top,width=w,height=h,label=label[:90]))

def para(text,x,top,w=CW,size=12,leading=18,font='Sans',color=INK,maxh=None):
    style=ParagraphStyle('p',fontName=font,fontSize=size,leading=leading,textColor=color,spaceAfter=0,splitLongWords=False,allowWidows=0,allowOrphans=0)
    p=Paragraph(escape(norm(text)).replace('\n','<br/>'),style)
    pw,ph=p.wrap(w,H)
    if maxh is not None and ph > maxh+0.1:
        raise ValueError(f'Page {page_num}: text exceeds {maxh}: {ph}, {text[:60]}')
    p.drawOn(c,x,H-top-ph)
    record('text',x,top,w,ph,text)
    return top+ph

def body(paragraphs,top,size=12,leading=17.6,gap=10,color=INK,x=M,w=CW,bottom=665):
    for p in paragraphs:
        top=para(p,x,top,w,size,leading,color=color)+gap
    if top-gap > bottom:
        raise ValueError(f'Page {page_num}: body exceeds content bottom ({top-gap}>{bottom})')
    return top-gap

def rule(top,x=M,w=CW,color=LINE):
    c.setStrokeColor(color);c.setLineWidth(.6);c.line(x,H-top,x+w,H-top)

def tag(text,top=35,color=MUTED):
    return para(text.upper(),M,top,size=8.4,leading=12,font='SansBold',color=color)

def title(text,top=68,size=33,color=INK):
    return para(text,M,top,size=size,leading=size*1.16,font='Serif',color=color)

def photo(filename,top,h,x=0,w=W,anchor=.5):
    path=ROOT / 'assets' / filename
    if not path.is_file():
        raise FileNotFoundError(path)
    # Export encoding only: preserve the source pixels/dimensions and the PNG
    # originals while using compact high-quality JPEG streams inside the PDF.
    if filename not in image_cache:
        with Image.open(path) as source:
            encoded=BytesIO()
            source.convert('RGB').save(encoded,format='JPEG',quality=90,subsampling=0,optimize=True)
            encoded.seek(0)
            image_cache[filename]=ImageReader(encoded)
    im=image_cache[filename]; iw,ih=im.getSize()
    scale=max(w/iw,h/ih);dw,dh=iw*scale,ih*scale
    dx=x+(w-dw)/2;dy=H-top-h+(h-dh)*anchor
    c.saveState()
    clip=c.beginPath();clip.rect(x,H-top-h,w,h);c.clipPath(clip,stroke=0,fill=0)
    c.drawImage(im,dx,dy,width=dw,height=dh,mask='auto')
    c.restoreState();record('image',x,top,w,h,filename)

def begin(name,bg=PAPER,dark=False):
    global page_num
    page_num+=1
    c.setFillColor(bg);c.rect(0,0,W,H,fill=1,stroke=0)
    c.bookmarkPage(name);c.addOutlineEntry(name,name,0,False)
    color=LINE if dark else MUTED
    rule(681,color=Color(.75,.81,.73,.35) if dark else LINE)
    para('WORLDS WE CAN INHABIT',M,690,size=7.6,leading=10,color=color)
    para(f'{page_num:02d} / 10',W-M-47,690,w=47,size=7.6,leading=10,color=color)

def end():
    c.showPage()

def arrow(x1,y1,x2,y2,color=MUTED):
    # Coordinates use top-origin as the rest of the layout.
    import math
    a=math.atan2(y2-y1,x2-x1); length=5
    c.setStrokeColor(color);c.setFillColor(color);c.setLineWidth(.9)
    c.line(x1,H-y1,x2,H-y2)
    p=c.beginPath();p.moveTo(x2,H-y2)
    p.lineTo(x2-length*math.cos(a-.5),H-(y2-length*math.sin(a-.5)))
    p.lineTo(x2-length*math.cos(a+.5),H-(y2-length*math.sin(a+.5)))
    p.close();c.drawPath(p,fill=1,stroke=0)

# 1 / Cover
begin('Worlds we can inhabit')
tag(BOOK['edition'],31)
title('Worlds we\ncan inhabit',67,47)
para(BOOK['subtitle'],M,197,w=425,size=13.4,leading=19.5,maxh=70)
photo('garden-district.png',293,380,anchor=.5)
para(BOOK['credit'],M,263,size=9.3,leading=14,color=MUTED)
end()

# 2 / Living Garden
p=PAGES['garden'];begin('An ordinary day')
photo('garden-district.png',0,253,anchor=.22)
tag(p['kicker'],277)
title(p['title'],299,31)
bottom=body(p['body'],390,size=12,leading=17.6,gap=9,bottom=617)
para(p['pull'],M,637,w=CW,size=14.2,leading=21,font='SerifItalic')
end()

# 3 / Premise, rights, recourse
p=PAGES['foundation'];begin('The conditions of freedom')
tag(p['kicker']);title(p['title'],69,36)
para(p['intro'],M,173,size=12.2,leading=18.1,maxh=93)
top=276
for i,(head,copy) in enumerate(p['blocks'],1):
    rule(top)
    para(f'0{i}',M,top+15,w=35,size=12,leading=18,font='Serif',color=TERRA)
    para(head,M+48,top+12,w=CW-48,size=12,leading=18,font='SansBold')
    bottom=para(copy,M+48,top+37,w=CW-48,size=11.3,leading=16.5,maxh=69)
    top=max(top+108,bottom+16)
para(p['pull'],M,631,w=CW,size=15.2,leading=22,font='SerifItalic',maxh=44)
end()

# 4 / Open University
p=PAGES['university'];begin('Many ways to spend a life')
photo('open-university.png',0,248,anchor=.5)
tag(p['kicker'],272);title(p['title'],294,31)
body(p['body'],382,size=12,leading=17.2,gap=9,bottom=616)
para(p['pull'],M,632,w=CW,size=13.2,leading=19,font='SerifItalic',maxh=39)
end()

# 5 / House of Worlds
p=PAGES['house'];begin('House of Worlds')
photo('house-of-worlds.png',0,276,anchor=.5)
tag(p['kicker'],300);title(p['title'],322,31)
body(p['body'],410,size=12,leading=17.8,gap=11,bottom=661)
end()

# 6 / The life of a cup
p=PAGES['cup'];begin('A cup with a next life')
tag(p['kicker']);title(p['title'],70,37)
para(p['intro'],M,172,size=12.4,leading=18.6,maxh=76)
rule(261)
tag('A proposed loop / recovery is part of the design',276)
node_y=314
labels=['Use','Return','Clean +\ninspect','Use again']
nodew,gap=98,24
for i,label in enumerate(labels):
    x=M+i*(nodew+gap)
    c.setFillColor(SOFT);c.roundRect(x,H-node_y-55,nodew,55,3,fill=1,stroke=0)
    para(label,x+9,node_y+12,w=nodew-18,size=11,leading=15,font='SansBold')
    if i<3: arrow(x+nodew+4,node_y+27,x+nodew+gap-4,node_y+27)
# Return route: the repeated-use loop is the primary loop.
c.setStrokeColor(MUTED);c.setLineWidth(.9)
c.line(453,H-372,453,H-391);c.line(453,H-391,87,H-391)
arrow(87,391,87,372)
para('When needed: repair, assess, recover material, and make again.',M,408,w=CW,size=9.7,leading=14,color=MUTED)
para('Energy and process inputs enter. Losses and residues need destinations.',M,430,w=CW,size=9.3,leading=13.4,color=MUTED)
body(p['body'],469,size=11.7,leading=17.1,gap=10,bottom=665)
end()

# 7 / Material library and reusable architecture
p=PAGES['building'];begin("A building's next life")
photo('material-lives.png',0,243,anchor=.5)
tag(p['kicker'],266);title(p['title'],288,32)
body(p['body'],380,size=11.8,leading=17.2,gap=9,bottom=620)
para(p['pull'],M,632,w=CW,size=13.3,leading=19.4,font='SerifItalic',maxh=40)
end()

# 8 / Disagreement is part of the world
p=PAGES['disagreement'];begin('The machines are ready',bg=INK,dark=True)
tag(p['kicker'],35,color=LINE);title(p['title'],77,40,color=LIGHT)
rule(244,color=Color(.75,.81,.73,.45))
body(p['body'],267,size=12.4,leading=18.7,gap=13,color=LIGHT,bottom=663)
end()

# 9 / Invitation, with ample room for discussion
p=PAGES['invitation'];begin('Come imagine it with us')
tag(p['kicker']);title(p['title'],77,39)
para(p['intro'],M,188,size=12.1,leading=18.1,maxh=80)
top=290
for i,q in enumerate(p['questions'],1):
    rule(top)
    para(f'0{i}',M,top+16,w=36,size=11.5,leading=17,color=TERRA)
    para(q,M+46,top+13,w=CW-46,size=16.5,leading=23,font='Serif',maxh=49)
    top+=75
para(p['body'],M,535,size=11.8,leading=17.8,maxh=96)
para(p['pull'],M,636,size=14,leading=20,font='SerifItalic',maxh=40)
end()

# 10 / Short, portable context and sources
begin('About this invitation')
tag('About this invitation');title('A possible world.\nAn open project.',72,34)
top=176
top=body([
    'This booklet introduces a worldbuilding project by Ren, developed with AI. It brings together secure existence, plural ways of living, public knowledge, and materials designed for continuing use and transformation.',
    'The places and institutions are proposals. Broad autonomous provision is a scenario assumption. The images are generated concepts, not architectural plans or evidence that the depicted systems work.',
    'The project develops through lived scenes, research, spatial studies, and eventual explorable worlds. Disagreement and a closer look at the details are welcome.'
],top,size=11.7,leading=17.4,gap=10,bottom=392)
rule(407);tag('A few material realities / further reading',423)
top=455
for source in BOOK['sources']:
    label=f"[{source['number']}] {source['title']} ({source['date']})"
    bottom=para(label,M,top,w=CW,size=9.7,leading=14,font='SansBold',maxh=29)
    c.linkURL(source['url'],(M,H-bottom,W-M,H-top),relative=0,thickness=0)
    bottom=para(source['scope'],M,bottom+5,w=CW,size=9.7,leading=14,color=MUTED,maxh=29)
    top=bottom+16
para('Edition 01 / September 2026',M,646,size=9.2,leading=14,color=MUTED)
end()

if page_num != 10:
    raise ValueError(f'Expected 10 pages, got {page_num}')
c.save()
(QA / 'layout.json').write_text(json.dumps(layout,indent=2)+'\n',encoding='utf-8')
print(f'Built {OUT} ({page_num} pages)')
