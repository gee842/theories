#!/usr/bin/env python3
"""Edition 04: complete uncropped concept frames with compact reading panels."""
from pathlib import Path
from io import BytesIO
import argparse, hashlib, json, math, re
from xml.sax.saxutils import escape
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT=Path(__file__).resolve().parent
DEFAULT_FONTS=Path(Path.home(), '.cache/codex-runtimes/codex-primary-runtime/dependencies/native/libreoffice-headless/libreoffice/LibreOfficeDev.app/Contents/Resources/fonts/truetype')
a=argparse.ArgumentParser();a.add_argument('--font-dir',type=Path,default=DEFAULT_FONTS);a.add_argument('--cjk-font',type=Path,default=Path('/System/Library/Fonts/Supplemental/Arial Unicode.ttf'));args=a.parse_args()
for name,fn in [('Serif','NotoSerif-Regular.ttf'),('SerifItalic','NotoSerif-Italic.ttf'),('Sans','NotoSans-Regular.ttf'),('SansBold','NotoSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(args.font_dir/fn)))
pdfmetrics.registerFont(TTFont('CJK',str(args.cjk_font)))
pdfmetrics.registerFontFamily('Sans',normal='Sans',bold='SansBold')
BOOK=json.loads((ROOT/'content-v4.json').read_text())
OUT=ROOT/'output/pdf/worlds-we-can-inhabit-v4.pdf';QA=ROOT/'tmp/pdfs-v4'
OUT.parent.mkdir(parents=True,exist_ok=True);QA.mkdir(parents=True,exist_ok=True)
W,H,M=1000,820,40;CW=W-2*M;IH=2000/3
INK=HexColor('#203C32');PAPER=HexColor('#F5F1E8');SOFT=HexColor('#E8E9DF');MUTED=HexColor('#576C5D');LINE=HexColor('#C2CCBD');TERRA=HexColor('#AB593A')
c=canvas.Canvas(str(OUT),pagesize=(W,H),pageCompression=1)
c.setTitle(BOOK['title']+' / Edition 04');c.setAuthor('Ren; developed with AI');c.setSubject('An atlas of embodied futures, shared productive capacity, and generative worldmaking');c.setCreator('Worldbuilding / ReportLab')
layout=[];placements=[];page_num=0

def norm(t):return t.replace('\u2011','-').replace('\u2013','-').replace('\u2014','-')
def record(kind,x,top,w,h,label=''):
    if min(x,top)<-.1 or x+w>W+.1 or top+h>H+.1:raise ValueError(f'Outside page {page_num}: {label[:60]}')
    layout.append(dict(page=page_num,kind=kind,x=x,top=top,width=w,height=h,label=label))
def para(text,top,x=M,w=CW,size=15,leading=22,font='Sans',color=INK,maxh=None,url=None):
    s=escape(norm(text)).replace('\n','<br/>').replace('生生不息','<font name="CJK">生生不息</font>')
    ev={e['id']:e['url'] for e in BOOK['evidence']}
    s=re.sub(r'\[(E\d+)\]',lambda m:'<link href="'+ev[m[1]]+'">['+m[1]+']</link>',s)
    if url:s='<link href="'+escape(url)+'">'+s+'</link>'
    p=Paragraph(s,ParagraphStyle('p',fontName=font,fontSize=size,leading=leading,textColor=color,splitLongWords=False,allowWidows=0,allowOrphans=0))
    _,h=p.wrap(w,H)
    if maxh is not None and h>maxh+.1:raise ValueError(f'Overflow p{page_num}, {h}>{maxh}: {text[:80]}')
    p.drawOn(c,x,H-top-h);record('text',x,top,w,h,text);return top+h

def rule(top,x=M,w=CW,color=LINE):
    c.setStrokeColor(color);c.setLineWidth(.7);c.line(x,H-top,x+w,H-top)
def box(x,top,w,h,color=SOFT):
    c.setFillColor(color);c.roundRect(x,H-top-h,w,h,5,fill=1,stroke=0)
def tag(t,top=37):return para(t.upper(),top,size=10,leading=14,font='SansBold',color=MUTED)
def title(t,top=77,size=43):return para(t,top,size=size,leading=size*1.18,font='Serif',maxh=size*2.4)
def arrow(x1,y1,x2,y2,color=MUTED):
    c.setStrokeColor(color);c.setFillColor(color);c.setLineWidth(1.2);c.line(x1,H-y1,x2,H-y2)
    a=math.atan2(y2-y1,x2-x1);p=c.beginPath();p.moveTo(x2,H-y2)
    for b in [a-.5,a+.5]:p.lineTo(x2-7*math.cos(b),H-(y2-7*math.sin(b)))
    p.close();c.drawPath(p,fill=1,stroke=0)
def begin(p):
    global page_num
    page_num+=1;c.setFillColor(PAPER);c.rect(0,0,W,H,fill=1,stroke=0)
    c.bookmarkPage(p['id']);c.addOutlineEntry(p['title'].replace('\n',' '),p['id'],0,False)
    rule(796);para('WORLDS WE CAN INHABIT / EDITION 04',802,size=7.5,leading=10,color=MUTED)
    para(f'{page_num:02d} / {len(BOOK["pages"]):02d}',802,x=920,w=40,size=7.5,leading=10,color=MUTED)
def photo(pathname):
    path=ROOT/pathname;digest=hashlib.sha256(path.read_bytes()).hexdigest()
    if digest in [p['sha256'] for p in placements]:raise ValueError('Repeated image: '+pathname)
    with Image.open(path) as im:
        iw,ih=im.size
        if abs(iw/ih-W/IH)>.001:raise ValueError('Uncropped frame ratio mismatch: '+pathname)
        stream=BytesIO();im.convert('RGB').save(stream,format='JPEG',quality=90,subsampling=0,optimize=True);stream.seek(0)
        c.drawImage(ImageReader(stream),0,H-IH,width=W,height=IH)
    placements.append(dict(page=page_num,path=pathname,sha256=digest,width=iw,height=ih,crop='none'))
    record('image',0,0,W,IH,pathname)
def scene(p):
    photo(p['image']);tag(p['kicker'],681)
    para(p['title'],706,w=345,size=27.5,leading=32.4,font='Serif',maxh=79)
    para(p['caption'],700,x=400,w=560,size=12.6,leading=17.9,maxh=90)
    if p['layout']=='cover':
        para(BOOK['credit'],778,x=400,w=560,size=8,leading=11,color=MUTED,maxh=12)
    for pin in p.get('pins',[]):
        x,y=pin['x'],pin['y'];c.setFillColor(PAPER);c.circle(x,H-y,10,stroke=0,fill=1)
        para(pin['label'],y-6,x=x-6,w=12,size=8,leading=11,font='SansBold')
def engine(p):
    tag(p['kicker']);title(p['title']);para(p['intro'],197,w=830,size=17,leading=25,maxh=52)
    for i,(head,copy) in enumerate(p['cards']):
        x=M+i*315;box(x,280,290,190)
        para(f'0{i+1}',295,x=x+18,w=252,size=11,leading=15,color=TERRA,font='SansBold')
        para(head,323,x=x+18,w=254,size=17,leading=24,font='Serif',maxh=49)
        para(copy,374,x=x+18,w=254,size=12.6,leading=18.5,maxh=80)
    for i,label in enumerate(p['chain']):
        x=M+i*236;box(x,492,212,62,INK)
        para(label,503,x=x+14,w=184,size=14,leading=20,font='SansBold',color=PAPER,maxh=42)
        if i<3:arrow(x+217,523,x+231,523)
    para(p['body'],592,w=885,size=19,leading=29,font='Serif',maxh=91)
    rule(712);para(p['note'],730,size=11.7,leading=17,color=MUTED,maxh=53)
def principles(p):
    tag(p['kicker']);title(p['title'])
    box(M,195,CW,92)
    y=para('“'+p['quote']+'”',209,x=58,w=884,size=23,leading=30,font='SerifItalic',maxh=61)
    para(p['attribution'],y+7,x=58,w=884,size=9.5,leading=13,color=MUTED)
    para(p['intro'],310,size=16.2,leading=24,maxh=49)
    for i,label in enumerate(p['loop']):
        x=M+i*236;box(x,378,212,53)
        para(label,385,x=x+13,w=186,size=12.8,leading=19,font='SansBold',maxh=38)
        if i<3:arrow(x+218,404,x+231,404)
    # Complete the cultural feedback loop visibly beneath its forward path.
    c.setStrokeColor(MUTED);c.setLineWidth(1)
    path=c.beginPath();path.moveTo(855,H-434);path.lineTo(855,H-451);path.lineTo(147,H-451);c.drawPath(path)
    arrow(147,451,147,434)
    for i,(head,copy) in enumerate(p['principles']):
        row,col=divmod(i,3);x=M+col*315;y=482+row*119
        rule(y,x=x,w=290);para(head,y+12,x=x,w=284,size=14.3,leading=21,font='SansBold',maxh=43)
        para(copy,y+42,x=x,w=284,size=12.6,leading=19,maxh=58)
    para(p['note'],746,size=11.5,leading=17,color=MUTED,maxh=36)
def invitation(p):
    tag(p['kicker']);title(p['title'],77,53);para(p['intro'],226,w=795,size=19,leading=29,maxh=60)
    for i,(head,copy) in enumerate(p['steps']):
        row,col=divmod(i,2);x=M+col*470;y=338+row*143
        para(f'0{i+1}',y,x=x,w=40,size=19,leading=25,font='Serif',color=TERRA)
        para(head,y,x=x+56,w=370,size=22,leading=29,font='Serif')
        para(copy,y+41,x=x+56,w=350,size=14.7,leading=22,maxh=68)
    rule(661);para(p['closing'],686,w=910,size=19,leading=29,font='Serif',maxh=88)
def evidence(p):
    tag(p['kicker']);title(p['title']);para(p['intro'],198,w=880,size=15,leading=22,maxh=47)
    for i,e in enumerate(BOOK['evidence']):
        y=273+i*71;rule(y)
        para(e['id'],y+13,w=38,size=12,leading=17,font='SansBold',color=TERRA)
        para(e['title'],y+11,x=95,w=385,size=12.7,leading=18.5,font='SansBold',url=e['url'],maxh=43)
        para(e['detail'],y+11,x=530,w=430,size=12.7,leading=18.5,maxh=55)
def provenance(p):
    tag(p['kicker']);title(p['title'])
    for i,(head,copy) in enumerate(p['blocks']):
        row,col=divmod(i,2);x=M+col*475;y=218+row*194
        rule(y,x=x,w=445);para(head,y+15,x=x,w=432,size=16,leading=23,font='Serif',maxh=25)
        para(copy,y+53,x=x,w=432,size=13,leading=19.5,maxh=137)
    rule(629);para('MATERIAL FOUNDATIONS / FURTHER READING',645,size=10,leading=14,font='SansBold',color=MUTED)
    for i,(label,url) in enumerate(p['references']):para(label,676+i*28,size=12.5,leading=19,url=url,maxh=20)
    para(BOOK['credit'],768,size=9,leading=13,color=MUTED,maxh=15)

for p in BOOK['pages']:
    begin(p)
    {'cover':scene,'photo':scene,'engine':engine,'principles':principles,'invitation':invitation,'evidence':evidence,'provenance':provenance}[p['layout']](p)
    c.showPage()
c.save()
(QA/'layout.json').write_text(json.dumps(layout,indent=2,ensure_ascii=False)+'\n')
(ROOT/'image-placements-v4.json').write_text(json.dumps(placements,indent=2)+'\n')
print(json.dumps(dict(pdf=str(OUT),pages=page_num,images=len(placements),bytes=OUT.stat().st_size)))
