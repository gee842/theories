#!/usr/bin/env python3
"""Build edition 02 from editable copy and unique, preserved concept images."""
from pathlib import Path
from io import BytesIO
import argparse
import hashlib
import json
import math
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image

ROOT = Path(__file__).resolve().parent
DEFAULT_FONTS = Path(Path.home(), '.cache/codex-runtimes/codex-primary-runtime/dependencies/native/libreoffice-headless/libreoffice/LibreOfficeDev.app/Contents/Resources/fonts/truetype')
parser = argparse.ArgumentParser()
parser.add_argument('--font-dir', type=Path, default=DEFAULT_FONTS)
parser.add_argument('--cjk-font', type=Path, default=Path('/System/Library/Fonts/Supplemental/Arial Unicode.ttf'))
args = parser.parse_args()
for name, filename in [('Serif','NotoSerif-Regular.ttf'),('SerifItalic','NotoSerif-Italic.ttf'),('Sans','NotoSans-Regular.ttf'),('SansBold','NotoSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(args.font_dir/filename)))
pdfmetrics.registerFont(TTFont('CJK',str(args.cjk_font)))
pdfmetrics.registerFontFamily('Sans',normal='Sans',bold='SansBold')

BOOK = json.loads((ROOT/'content-v2.json').read_text())
OUT = ROOT/'output/pdf/worlds-we-can-inhabit-v2.pdf'
QA = ROOT/'tmp/pdfs-v2'
OUT.parent.mkdir(parents=True,exist_ok=True)
QA.mkdir(parents=True,exist_ok=True)
W,H,M = 540,720,38
CW = W-2*M
INK=HexColor('#203C32'); PAPER=HexColor('#F5F1E8'); SOFT=HexColor('#E8E9DF')
MUTED=HexColor('#576C5D'); LINE=HexColor('#C2CCBD'); TERRA=HexColor('#AB593A')
layout=[]; placements=[]; page_num=0
c=canvas.Canvas(str(OUT),pagesize=(W,H),pageCompression=1)
c.setTitle(BOOK['title']+' / Edition 02')
c.setAuthor('Ren; developed with AI')
c.setSubject('Generative worldmaking, plural cultures, shared material capacity, and future worlds')
c.setCreator('Worldbuilding / ReportLab')

def norm(s):
    return s.replace('\u2011','-').replace('\u2013','-').replace('\u2014','-')

def record(kind,x,top,w,h,label=''):
    if x < -.1 or top < -.1 or x+w > W+.1 or top+h > H+.1:
        raise ValueError(f'Page {page_num}: outside page: {label} {(x,top,w,h)}')
    layout.append(dict(page=page_num,kind=kind,x=x,top=top,width=w,height=h,label=label))

def para(text,top,x=M,w=CW,size=12,leading=17.6,font='Sans',color=INK,maxh=None):
    style=ParagraphStyle('p',fontName=font,fontSize=size,leading=leading,textColor=color,splitLongWords=False,allowWidows=0,allowOrphans=0)
    escaped=escape(norm(text)).replace('\n','<br/>')
    escaped=escaped.replace('生生不息','<font name="CJK">生生不息</font>')
    p=Paragraph(escaped,style)
    _,ph=p.wrap(w,H)
    if maxh is not None and ph>maxh+.1:
        raise ValueError(f'Page {page_num}: text exceeds {maxh}: {ph}: {text[:85]}')
    p.drawOn(c,x,H-top-ph)
    record('text',x,top,w,ph,text)
    return top+ph

def body(paras,top,size=12,leading=17.6,gap=10,bottom=664,**kw):
    for p in paras:
        top=para(p,top,size=size,leading=leading,**kw)+gap
    if top-gap>bottom+.1:
        raise ValueError(f'Page {page_num}: body ends at {top-gap}, limit {bottom}')
    return top-gap

def rule(top,x=M,w=CW,color=LINE):
    c.setStrokeColor(color);c.setLineWidth(.65);c.line(x,H-top,x+w,H-top)

def tag(text,top=34,color=MUTED):
    return para(text.upper(),top,size=8.1,leading=11.3,font='SansBold',color=color)

def title(text,top=65,size=33,color=INK):
    return para(text,top,size=size,leading=size*1.15,font='Serif',color=color)

def begin(p,dark=False):
    global page_num
    page_num+=1
    c.setFillColor(INK if dark else PAPER);c.rect(0,0,W,H,fill=1,stroke=0)
    c.bookmarkPage(p['id']);c.addOutlineEntry(p['title'].replace('\n',' '),p['id'],0,False)
    rule(681,color=MUTED if dark else LINE)
    color=LINE if dark else MUTED
    para('WORLDS WE CAN INHABIT',690,size=7.6,leading=10,color=color)
    para(f'{page_num:02d} / {len(BOOK["pages"]):02d}',690,x=W-M-48,w=48,size=7.6,leading=10,color=color)

def photo(filename,top,h,x=0,w=W):
    path=ROOT/filename
    digest=hashlib.sha256(path.read_bytes()).hexdigest()
    if digest in [p['sha256'] for p in placements]:
        raise ValueError(f'Repeated source image on page {page_num}: {filename}')
    # PDF serialization only. Source pixels and original PNGs are preserved;
    # the PDF uses compact JPEG streams at the original pixel dimensions.
    with Image.open(path) as source:
        encoded=BytesIO()
        source.convert('RGB').save(encoded,format='JPEG',quality=90,subsampling=0,optimize=True)
        encoded.seek(0);im=ImageReader(encoded)
    iw,ih=im.getSize(); scale=max(w/iw,h/ih);dw,dh=iw*scale,ih*scale
    c.saveState();clip=c.beginPath();clip.rect(x,H-top-h,w,h)
    c.clipPath(clip,stroke=0,fill=0)
    c.drawImage(im,x+(w-dw)/2,H-top-h+(h-dh)/2,width=dw,height=dh)
    c.restoreState()
    record('image',x,top,w,h,filename)
    placements.append(dict(page=page_num,path=filename,sha256=digest,width=iw,height=ih))

def arrow(x1,y1,x2,y2,color=MUTED):
    a=math.atan2(y2-y1,x2-x1);length=5
    c.setStrokeColor(color);c.setFillColor(color);c.setLineWidth(.8)
    c.line(x1,H-y1,x2,H-y2)
    p=c.beginPath();p.moveTo(x2,H-y2)
    p.lineTo(x2-length*math.cos(a-.5),H-(y2-length*math.sin(a-.5)))
    p.lineTo(x2-length*math.cos(a+.5),H-(y2-length*math.sin(a+.5)))
    p.close();c.drawPath(p,fill=1,stroke=0)

def cover(p):
    tag(BOOK['edition'],31)
    title(p['title'],66,46)
    para(BOOK['subtitle'],189,w=442,size=13,leading=19,maxh=61)
    para(BOOK['credit'],261,size=9.2,leading=14,color=MUTED)
    photo(p['image'],306,360)

def essay(p):
    dark=p['id']=='coexistence'
    fg=PAPER if dark else INK
    tag(p['kicker'],color=LINE if dark else MUTED)
    bottom=title(p['title'],69,32,color=fg)
    bottom=para(p['intro'],bottom+23,size=13.1,leading=19.5,color=fg)
    rule(bottom+20,color=MUTED if dark else LINE)
    bottom=body(p['body'],bottom+39,size=11.8,leading=17.5,gap=11,color=fg,bottom=607)
    para(p['pull'],632,size=14.1,leading=20.5,font='SerifItalic',color=fg,maxh=42)

def feedback(p):
    tag(p['kicker']);y=title(p['title'],67,33)
    para(p['intro'],y+19,size=12,leading=17.6,maxh=56)
    cols=[M,M+162,M+324]; rows=[245,345]; nw=140;nh=72
    for idx,(head,copy) in enumerate(p['nodes']):
        row,col=divmod(idx,3);x=cols[col];top=rows[row]
        c.setFillColor(SOFT);c.roundRect(x,H-top-nh,nw,nh,4,fill=1,stroke=0)
        para(head,top+11,x=x+11,w=nw-22,size=10.2,leading=14,font='SansBold',maxh=28)
        para(copy,top+33,x=x+11,w=nw-22,size=9.4,leading=13,color=MUTED,maxh=28)
    # Top row moves right; bottom row moves left; these directions preserve
    # the intended causal order independently of JSON's visual row ordering.
    for i in range(2):arrow(cols[i]+nw+3,281,cols[i+1]-3,281)
    arrow(cols[2]+nw/2,rows[0]+nh+4,cols[2]+nw/2,rows[1]-4)
    for i in [2,1]:arrow(cols[i]-3,381,cols[i-1]+nw+3,381)
    arrow(cols[0]+nw/2,rows[1]-4,cols[0]+nw/2,rows[0]+nh+4)
    body(p['body'],441,size=11.3,leading=16.5,gap=10,bottom=637)
    para(p['note'],647,size=8.8,leading=12.6,color=MUTED,maxh=26)

def principles(p):
    tag(p['kicker']);title(p['title'],65,33)
    c.setFillColor(SOFT);c.roundRect(M, H-162-78,CW,78,3,fill=1,stroke=0)
    q=para('“'+p['quote']+'”',174,x=M+15,w=CW-30,size=14.2,leading=20,font='SerifItalic',maxh=41)
    para(p['attribution'],q+7,x=M+15,size=8.5,leading=12,color=MUTED)
    for i,(head,copy) in enumerate(p['principles']):
        row,col=divmod(i,2); x=M+col*244;top=261+row*119
        rule(top,x=x,w=220)
        para(f'0{i+1} / '+head,top+11,x=x,w=220,size=10.5,leading=14.5,font='SansBold',maxh=30)
        para(copy,top+37,x=x,w=220,size=10.35,leading=14.8,maxh=76)
    para(p['note'],634,size=9.3,leading=13.8,color=MUTED,maxh=42)

def blocks(p):
    tag(p['kicker']);y=title(p['title'],66,36)
    y=para(p['intro'],y+21,size=12.3,leading=18.2)+24
    for i,(head,copy) in enumerate(p['blocks'],1):
        rule(y);para(f'0{i}',y+13,w=35,size=12,leading=18,font='Serif',color=TERRA)
        b=para(head,y+12,x=M+46,w=CW-46,size=11.4,leading=16.4,font='SansBold')
        b=para(copy,b+6,x=M+46,w=CW-46,size=11.1,leading=16.1)
        y=b+19
    if y>598:raise ValueError(f'Blocks too long: {y}')
    para(p['pull'],600,size=14.2,leading=20.3,font='SerifItalic',maxh=42)
    para(p['note'],650,size=8,leading=10.5,color=MUTED,maxh=22)

def scene(p):
    photo(p['image'],0,309)
    tag(p['kicker'],331)
    y=title(p['title'],352,29.5)
    y=body(p['body'],y+18,size=11.35,leading=16.35,gap=8.5,bottom=625)
    para(p['pull'],641,size=13.8,leading=20,font='SerifItalic',maxh=30)

def portal(p):
    tag(p['kicker'],27);title(p['title'],50,32)
    photo(p['image'],139,360)
    para(p['caption'],508,size=8.5,leading=12,color=MUTED,maxh=25)
    body(p['body'],546,size=11.1,leading=15.4,gap=8,bottom=671)

def circulation(p):
    tag(p['kicker']);y=title(p['title'],66,35)
    para(p['intro'],y+20,size=12.5,leading=18.5,maxh=57)
    labels=['Use + care','Recover +\nassess','Adapt +\nuse again'];xs=[M,M+163,M+326]
    for x,label in zip(xs,labels):
        c.setFillColor(SOFT);c.roundRect(x,H-264-59,138,59,4,fill=1,stroke=0)
        para(label,277,x=x+12,w=114,size=11.3,leading=15.5,font='SansBold',maxh=33)
    arrow(xs[0]+142,293,xs[1]-4,293);arrow(xs[1]+142,293,xs[2]-4,293)
    c.setStrokeColor(MUTED);c.setLineWidth(.8)
    c.line(xs[2]+69,H-327,xs[2]+69,H-347);c.line(xs[2]+69,H-347,xs[0]+69,H-347)
    arrow(xs[0]+69,347,xs[0]+69,327)
    para('Energy and process inputs enter; losses and residues need destinations.',360,size=9,leading=13,color=MUTED)
    body(p['body'],395,size=11.4,leading=16.5,gap=10,bottom=624)
    para(p['pull'],642,size=13.6,leading=19.5,font='SerifItalic',maxh=30)

def invitation(p):
    tag(p['kicker']);y=title(p['title'],70,37)
    y=para(p['intro'],y+21,size=12.4,leading=18.3)+27
    for i,(head,question) in enumerate(p['questions'],1):
        rule(y);para(f'0{i}',y+14,w=33,size=11,leading=16,color=TERRA)
        b=para(head,y+10,x=M+42,w=CW-42,size=14.1,leading=20,font='Serif')
        b=para(question,b+5,x=M+42,w=CW-42,size=11.2,leading=16.4)
        y=b+17
    if y>579:raise ValueError(f'Invitation too long: {y}')
    para(p['closing'],600,size=12,leading=17.8,maxh=72)

def sources(p):
    tag(p['kicker']);y=title(p['title'],64,33)+24
    for head,copy in p['blocks']:
        y=para(head,y,size=10.9,leading=15.6,font='SansBold')+4
        y=para(copy,y,size=10.5,leading=15.2)+17
    if y>570:raise ValueError(f'Sources too long: {y}')
    rule(581);tag('Material references / click to read',594)
    y=616
    for label,url in p['references']:
        b=para(label,y,size=9.1,leading=13.1,color=MUTED)
        c.linkURL(url,(M,H-b,W-M,H-y),relative=0,thickness=0)
        y=b+5
    if y>677:raise ValueError(f'References too long: {y}')

renderers={k:v for k,v in [('cover',cover),('essay',essay),('feedback',feedback),('principles',principles),('blocks',blocks),('scene',scene),('portal',portal),('circulation',circulation),('invitation',invitation),('sources',sources)]}
for p in BOOK['pages']:
    begin(p,dark=p['id']=='coexistence')
    renderers[p['layout']](p)
    c.showPage()
assert page_num==15 and len(placements)==7
c.save()
(QA/'layout.json').write_text(json.dumps(layout,ensure_ascii=False,indent=2)+'\n')
(ROOT/'image-placements-v2.json').write_text(json.dumps(placements,indent=2)+'\n')
print(f'Built {OUT} ({page_num} pages; {len(placements)} unique images)')
