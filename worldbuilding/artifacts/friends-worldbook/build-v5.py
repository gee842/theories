#!/usr/bin/env python3
"""Edition 05: complete uncropped concept frames with compact reading panels."""
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
BOOK=json.loads((ROOT/'content-v5.json').read_text())
OUT=ROOT/'output/pdf/worlds-we-can-inhabit-v5.pdf';QA=ROOT/'tmp/pdfs-v5'
OUT.parent.mkdir(parents=True,exist_ok=True);QA.mkdir(parents=True,exist_ok=True)
W,H,M=1000,920,40;CW=W-2*M;IH=2000/3
INK=HexColor('#203C32');PAPER=HexColor('#F5F1E8');SOFT=HexColor('#E8E9DF');MUTED=HexColor('#576C5D');LINE=HexColor('#C2CCBD');TERRA=HexColor('#AB593A')
c=canvas.Canvas(str(OUT),pagesize=(W,H),pageCompression=1)
c.setTitle(BOOK['title']+' / Edition 05');c.setAuthor('Ren; developed with AI');c.setSubject('An atlas of embodied futures, shared productive capacity, and generative worldmaking');c.setCreator('Worldbuilding / ReportLab')
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
    rule(896);para('WORLDS WE CAN INHABIT / EDITION 05',902,size=7.5,leading=10,color=MUTED)
    para(f'{page_num:02d} / {len(BOOK["pages"]):02d}',902,x=920,w=40,size=7.5,leading=10,color=MUTED)
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
    para(p['title'],713,w=345,size=28,leading=34,font='Serif',maxh=140)
    para(p['caption'],708,x=400,w=560,size=13.3,leading=20,maxh=162)
    if p.get('flow'):
        for i,label in enumerate(p['flow']):
            x=M+i*315;box(x,852,290,29)
            para(label,857,x=x+10,w=270,size=10,leading=15,font='SansBold',maxh=16)
            if i<2:
                if p['id']=='ar-section' and i==1:arrow(x+310,867,x+295,867)
                else:arrow(x+295,867,x+310,867)
    if p['layout']=='cover':para(BOOK['credit'],869,x=400,w=560,size=8,leading=12,color=MUTED,maxh=13)

def story(p):
    photo(p['image']);tag(p['kicker'],681)
    para(p['title'],708,size=29,leading=36,font='Serif',maxh=38)
    for i,(head,copy) in enumerate(p['parts']):
        x=M+i*315
        para(head,759,x=x,w=290,size=13,leading=19,font='SansBold',maxh=21)
        para(copy,786,x=x,w=290,size=12.1,leading=18,maxh=100)

def card_grid(cards,top,height=160,size=13):
    for i,(head,copy) in enumerate(cards):
        x=M+i*315;box(x,top,290,height)
        y=para(head,top+17,x=x+17,w=256,size=15,leading=21,font='SansBold',maxh=43)
        para(copy,y+13,x=x+17,w=256,size=size,leading=size*1.48,maxh=height-(y-top)-28)

def closed_loop(labels,top,caption=None):
    for i,label in enumerate(labels):
        x=M+i*236;box(x,top,212,71,INK)
        para(label,top+13,x=x+14,w=184,size=14,leading=20,font='SansBold',color=PAPER,maxh=42)
        if i<3:arrow(x+216,top+35,x+231,top+35)
    c.setStrokeColor(MUTED);c.setLineWidth(1.3)
    q=c.beginPath();q.moveTo(855,H-top-75);q.lineTo(855,H-top-99);q.lineTo(147,H-top-99);c.drawPath(q)
    arrow(147,top+99,147,top+75)
    if caption:para(caption,top+107,size=10.5,leading=15,color=MUTED,maxh=32)

def recursion(p):
    tag(p['kicker']);title(p['title']);para(p['intro'],198,size=17,leading=25,maxh=54)
    para('01 / PRODUCTION FEEDBACK',276,size=10,leading=14,font='SansBold',color=TERRA)
    closed_loop(p['loops'][0],302)
    para('02 / KNOWLEDGE FEEDBACK',438,size=10,leading=14,font='SansBold',color=TERRA)
    closed_loop(p['loops'][1],464)
    # Explicit coupling: observations go down; tested deployment informs production.
    arrow(475,408,475,455);arrow(500,455,500,408);para('Operation teaches; tested knowledge improves production',412,x=525,w=416,size=10,leading=15,color=MUTED,maxh=31)
    card_grid(p['notes'],604,183,12.5)
    para(p['closing'],804,size=14.7,leading=22,font='Serif',maxh=73)

def construction(p):
    tag(p['kicker']);title(p['title']);para(p['intro'],201,size=17,leading=26,maxh=78)
    for i,(head,copy) in enumerate(p['cards']):
        y=309+i*136;rule(y)
        para(head,y+17,w=275,size=19,leading=26,font='Serif',maxh=54)
        para(copy,y+17,x=360,w=600,size=14.5,leading=22,maxh=93)
    para(p['closing'],745,w=900,size=17,leading=25,font='Serif',maxh=78)
    para(p['note'],845,size=11.5,leading=17,color=MUTED,maxh=35)

def provision(p):
    tag(p['kicker']);title(p['title']);para(p['intro'],202,size=17,leading=26,maxh=78)
    for i,label in enumerate(p['chain']):
        x=M+i*236;box(x,311,212,92,INK)
        para(label,328,x=x+15,w=182,size=15,leading=22,font='SansBold',color=PAPER,maxh=66)
        if i==0:para('+',345,x=x+214,w=20,size=19,leading=24,font='SansBold',maxh=25)
        elif i<3:arrow(x+216,357,x+231,357)
    card_grid(p['cards'],455,272,13.7)
    para(p['closing'],758,size=18,leading=27,font='Serif',maxh=84)
    para(p['note'],850,size=11.5,leading=17,color=MUTED,maxh=35)

def ar_routes(p):
    tag(p['kicker']);title(p['title']);para(p['intro'],202,size=16,leading=24,maxh=74)
    # Floor relationship, with cores in the same orientation as the art.
    box(40,315,112,315,INK);box(848,315,112,315,TERRA)
    para('LEFT\nPassenger\ncore',332,x=50,w=92,size=13,leading=21,font='SansBold',color=PAPER,maxh=70)
    para('RIGHT\nFreight &\nservice core',332,x=858,w=92,size=13,leading=21,font='SansBold',color=PAPER,maxh=90)
    box(179,315,642,315,HexColor('#E3E6DC'))
    para('MIDDLE HALL / HARBOR',331,x=199,w=602,size=11,leading=15,font='SansBold',color=MUTED)
    box(210,393,183,74,PAPER);para('Curved promenade',411,x=225,w=153,size=14,leading=21,font='SansBold',maxh=44)
    box(447,393,205,74,PAPER);para('Music table\nFirst Arrival',405,x=461,w=177,size=14,leading=21,font='SansBold',maxh=44)
    box(210,528,206,72,PAPER);para('Quiet edge &\nordinary return',540,x=224,w=178,size=14,leading=21,font='SansBold',maxh=44)
    box(676,519,124,82,HexColor('#EEE0CE'));para('Closed change\narea / module',534,x=686,w=104,size=12.7,leading=19,font='SansBold',maxh=58)
    box(676,393,124,74,PAPER);para('Tactile\nsetting',408,x=686,w=104,size=13,leading=21,font='SansBold',maxh=43)
    arrow(155,431,205,431);arrow(399,431,442,431);arrow(550,475,550,560);arrow(550,560,423,560);arrow(203,565,158,565)
    arrow(843,549,806,549,TERRA);arrow(806,574,843,574,TERRA);arrow(728,513,728,474,TERRA);arrow(750,474,750,513,TERRA)
    para('Checked before\nreopening',480,x=578,w=135,size=9.7,leading=14,color=TERRA,maxh=30)
    box(676,674,284,66,HexColor('#EEE0CE'));para('Ground repair & storage',695,x=692,w=254,size=13.5,leading=20,font='SansBold',maxh=22)
    arrow(904,669,904,636,TERRA);arrow(931,636,931,669,TERRA)
    para('VISIT (green) | MODULE DELIVERY & RETURN (terracotta)',655,w=620,size=10,leading=15,color=MUTED,maxh=30)
    para(p['closing'],773,size=14.6,leading=22,maxh=68)
    para(p['note'],850,size=11.2,leading=17,color=MUTED,maxh=35)
    # Keep conceptual route labels in the reading extraction, independently of art.

def circulation(p):
    tag(p['kicker']);title(p['title'],77,40);para(p['intro'],205,size=17,leading=25,maxh=54)
    closed_loop(p['loop'],312,'Finite stock moving through successive lives. The arrow back enables another cycle, not another simultaneous copy.')
    card_grid(p['cards'],483,225,13)
    para(p['closing'],747,size=18,leading=27,font='Serif',maxh=84)
    para(p['note'],850,size=11.5,leading=17,color=MUTED,maxh=35)

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
        row,col=divmod(i,3);x=M+col*315;y=496+row*143
        rule(y,x=x,w=290);para(head,y+12,x=x,w=284,size=14.3,leading=21,font='SansBold',maxh=43)
        para(copy,y+42,x=x,w=284,size=12.6,leading=19,maxh=58)
    para(p['note'],842,size=11.5,leading=17,color=MUTED,maxh=36)
def invitation(p):
    tag(p['kicker']);title(p['title'],77,53);para(p['intro'],226,w=795,size=19,leading=29,maxh=60)
    for i,(head,copy) in enumerate(p['steps']):
        row,col=divmod(i,2);x=M+col*470;y=358+row*157
        para(f'0{i+1}',y,x=x,w=40,size=19,leading=25,font='Serif',color=TERRA)
        para(head,y,x=x+56,w=370,size=22,leading=29,font='Serif')
        para(copy,y+41,x=x+56,w=350,size=14.7,leading=22,maxh=68)
    rule(704);para(p['closing'],734,w=910,size=19,leading=29,font='Serif',maxh=125)
def evidence(p):
    tag(p['kicker']);title(p['title']);para(p['intro'],198,w=880,size=15,leading=22,maxh=47)
    for i,e in enumerate(BOOK['evidence']):
        y=291+i*81;rule(y)
        para(e['id'],y+13,w=38,size=12,leading=17,font='SansBold',color=TERRA)
        para(e['title'],y+11,x=95,w=385,size=12.7,leading=18.5,font='SansBold',url=e['url'],maxh=43)
        para(e['detail'],y+11,x=530,w=430,size=12.7,leading=18.5,maxh=55)
def provenance(p):
    tag(p['kicker']);title(p['title'])
    for i,(head,copy) in enumerate(p['blocks']):
        row,col=divmod(i,2);x=M+col*475;y=224+row*224
        rule(y,x=x,w=445);para(head,y+15,x=x,w=432,size=16,leading=23,font='Serif',maxh=25)
        para(copy,y+53,x=x,w=432,size=13,leading=19.5,maxh=157)
    rule(706);para('MATERIAL FOUNDATIONS / FURTHER READING',722,size=10,leading=14,font='SansBold',color=MUTED)
    for i,(label,url) in enumerate(p['references']):para(label,755+i*30,size=12.5,leading=19,url=url,maxh=20)
    para(BOOK['credit'],865,size=9,leading=13,color=MUTED,maxh=15)

for p in BOOK['pages']:
    begin(p)
    {'cover':scene,'photo':scene,'story':story,'recursion':recursion,'construction':construction,'provision':provision,'ar-routes':ar_routes,'circulation':circulation,'principles':principles,'invitation':invitation,'evidence':evidence,'provenance':provenance}[p['layout']](p)
    c.showPage()
c.save()
(QA/'layout.json').write_text(json.dumps(layout,indent=2,ensure_ascii=False)+'\n')
(ROOT/'image-placements-v5.json').write_text(json.dumps(placements,indent=2)+'\n')
print(json.dumps(dict(pdf=str(OUT),pages=page_num,images=len(placements),bytes=OUT.stat().st_size)))
