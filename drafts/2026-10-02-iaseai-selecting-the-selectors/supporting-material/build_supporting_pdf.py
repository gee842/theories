"""English technical companion; AI-assisted presentation, not a research status change."""
from pathlib import Path
from hashlib import sha256
from html import escape
import json,re,math
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor,white
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph,Table,TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
OUT=HERE.parent/'output'/'pdf'
OUT.mkdir(parents=True,exist_ok=True)
PDF=OUT/'generativity-to-wisdom-supporting-statement.pdf'
SOURCE=HERE/'technical_content.json'
doc=json.loads(SOURCE.read_text())
FONTS=Path('/Users/ren/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/libreoffice-headless/libreoffice/LibreOfficeDev.app/Contents/Resources/fonts/truetype')
for name,filename in [('Body','DejaVuSans.ttf'),('BodyBold','DejaVuSans-Bold.ttf'),('Serif','NotoSerif-Regular.ttf'),('SerifBold','NotoSerif-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(FONTS/filename)))
for family in ['Body','Serif']:
    pdfmetrics.registerFontFamily(family,normal=family,bold=family+'Bold',italic=family,boldItalic=family+'Bold')
W,H=A4
M=42
CW=W-2*M
INK=HexColor('#17313B');TEAL=HexColor('#177D78');MUTED=HexColor('#586B70');PALE=HexColor('#EFF5F3');LINE=HexColor('#D8E4E1')
LIMIT=H-58
layout=[]
c=canvas.Canvas(str(PDF),pagesize=A4,pageCompression=1,invariant=1)
c.setTitle(doc['title']+': '+doc['subtitle'])
c.setAuthor(doc['author'])
c.setSubject("English technical supporting statement for the IASEAI'27 talk proposal")
def safe(text):return re.sub(r'&(?![A-Za-z]+;|#\d+;)','&amp;',text)
def para(text,width,size=9.6,leading=13.25,font='Serif',color=INK):
    if font.startswith('Serif'):
        missing={ch for ch in text if ord(ch)>127 and ord(ch) not in pdfmetrics.getFont(font).face.charWidths}
        for ch in missing:
            assert ord(ch) in pdfmetrics.getFont('Body').face.charWidths, repr(ch)
            text=text.replace(ch,'<font name="Body">'+ch+'</font>')
    p=Paragraph(safe(text),ParagraphStyle('p',fontName=font,fontSize=size,leading=leading,textColor=color,allowWidows=0,allowOrphans=0))
    p.wrap(width,H*2)
    return p
def paint(p,x,y,width,draw,tag='text'):
    _,height=p.wrap(width,H*2)
    if draw:
        p.drawOn(c,x,H-y-height)
        layout.append({'page':c.getPageNumber(),'kind':tag,'top':round(y,2),'bottom':round(y+height,2),'left':round(x,2),'right':round(x+width,2)})
    return y+height
def furniture(number,label):
    c.setFillColor(TEAL);c.rect(M,H-28,22,2.3,fill=1,stroke=0)
    paint(para("IASEAI'27  /  TECHNICAL SUPPORTING STATEMENT",CW,7.4,10,'BodyBold',MUTED),M+32,21,CW-32,True,'furniture')
    c.setStrokeColor(LINE);c.setLineWidth(.6);c.line(M,42,W-M,42)
    paint(para('YONGXU REN  /  '+label,CW,7.1,10,'Body',MUTED),M,H-31,CW-40,True,'furniture')
    paint(para(f'{number} / {len(doc["pages"])}',35,7.5,10,'Body',MUTED),W-M-25,H-31,30,True,'furniture')
def page_body(page,s,draw=False):
    size=10.2*s;lead=13.0*s;gap=5.5*s;y=53
    if page['title'] is None:
        y=paint(para(doc['title'],CW,26,31,'SerifBold'),M,y,CW,draw)
        y=paint(para(doc['subtitle'],CW,14,19),M,y+5,CW,draw)
        y=paint(para(doc['author']+'  |  '+doc['date'],CW,8.6,12,color=MUTED),M,y+7,CW,draw)+15
    else:y=paint(para(page['title'],CW,19.5,24.5,'SerifBold'),M,y,CW,draw)+14
    for b in page['blocks']:
        k=b['kind']
        if k=='p':y=paint(para(b['text'],CW,size,lead),M,y,CW,draw)+gap
        elif k=='h':y=paint(para(b['text'],CW,10.6*s,14.1*s,'BodyBold'),M,y+3*s,CW,draw)+5*s
        elif k=='note':y=paint(para(b['text'],CW,8.6*s,11.4*s,color=MUTED),M,y+2*s,CW,draw)+gap
        elif k=='eq':
            ps=[para(line,CW-24,10.2*s,14.5*s,'Body') for line in b['lines']]
            bh=sum(p.wrap(CW-24,H)[1] for p in ps)+12*s
            if draw:
                c.setFillColor(PALE);c.roundRect(M,H-y-bh,CW,bh,3,fill=1,stroke=0)
            yy=y+6*s
            for p in ps:yy=paint(p,M+12,yy,CW-24,draw,'equation')
            y+=bh+gap
        elif k=='box':
            pt=para(b['title'],CW-24,9.2*s,12.7*s,'BodyBold');pb=para(b['text'],CW-24,9.7*s,12.9*s)
            bh=pt.wrap(CW-24,H)[1]+pb.wrap(CW-24,H)[1]+24*s
            if draw:
                c.setFillColor(PALE);c.roundRect(M,H-y-bh,CW,bh,3,fill=1,stroke=0)
                c.setFillColor(TEAL);c.rect(M,H-y-bh,2,bh,fill=1,stroke=0)
            yy=paint(pt,M+12,y+9*s,CW-24,draw,'box')+5*s
            paint(pb,M+12,yy,CW-24,draw,'box');y+=bh+gap
        elif k=='table':
            ws=[CW*x for x in b['widths']]
            data=[[para(txt,ws[i]-14,8.6*s,11.6*s,'BodyBold' if n==0 else 'Body',white if n==0 else INK) for i,txt in enumerate(row)] for n,row in enumerate([b['headers']]+b['rows'])]
            t=Table(data,colWidths=ws,hAlign='LEFT')
            t.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BACKGROUND',(0,0),(-1,0),TEAL),('ROWBACKGROUNDS',(0,1),(-1,-1),[PALE,white]),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),4*s),('BOTTOMPADDING',(0,0),(-1,-1),4*s),('LINEBELOW',(0,-1),(-1,-1),.5,LINE)]))
            _,bh=t.wrap(CW,H*2)
            if draw:
                t.drawOn(c,M,H-y-bh)
                layout.append({'page':c.getPageNumber(),'kind':'table','top':round(y,2),'bottom':round(y+bh,2),'left':M,'right':W-M})
            y+=bh+gap
        elif k=='plot':
            bh=222*s
            if draw:
                # Exact analytic curves: log(gain(t)/gain(0))=(0.10-2*rate)*t.
                gx=M+43;gy=H-y-180*s;gw=CW-162;gh=148*s
                lo,hi=math.log(.2),math.log(25)
                def py(v):return gy+(math.log(v)-lo)/(hi-lo)*gh
                c.setFont('Body',7.5*s)
                for v in [.25,1,4,16]:
                    yy=py(v);c.setStrokeColor(LINE);c.setLineWidth(.5);c.line(gx,yy,gx+gw,yy)
                    c.setFillColor(MUTED);c.drawRightString(gx-7,yy-2.5,str(v))
                for t in [0,10,20,30]:
                    xx=gx+gw*t/30;c.setFillColor(MUTED);c.drawCentredString(xx,gy-12*s,str(t))
                c.setStrokeColor(MUTED);c.line(gx,gy,gx+gw,gy);c.line(gx,gy,gx,gy+gh)
                c.setFillColor(INK);c.setFont('BodyBold',8*s);c.drawString(M,H-y-12*s,'Cultivated gain / initial cultivated gain (log scale)')
                c.setFont('Body',7.5*s);c.drawCentredString(gx+gw/2,gy-26*s,'Time (arbitrary units)')
                colors=['#AD5439','#B08A3A','#177D78','#607D94']
                for n,(rate,col) in enumerate(zip([0,.025,.05,.075],colors)):
                    c.setStrokeColor(HexColor(col));c.setLineWidth(1.6)
                    path=c.beginPath()
                    for step in range(121):
                        t=step/4;xx=gx+gw*t/30;yy=py(math.exp((.1-2*rate)*t))
                        if step==0:path.moveTo(xx,yy)
                        else:path.lineTo(xx,yy)
                    c.drawPath(path)
                    yy=gy+gh-20*n*s;c.line(gx+gw+15,yy,gx+gw+29,yy)
                    c.setFillColor(INK);c.setFont('Body',7.7*s)
                    c.drawString(gx+gw+34,yy-2.5,'αcor = '+format(rate,'.3f'))
                layout.append({'page':c.getPageNumber(),'kind':'plot','top':round(y,2),'bottom':round(y+bh,2),'left':M,'right':W-M})
            y+=bh
            y=paint(para(b['caption'],CW,8.5*s,11.3*s,color=MUTED),M,y,CW,draw)+gap
        elif k=='refs':
            for txt,url in b['items']:
                linked=f'<link href="{escape(url,quote=True)}" color="#17313B">{safe(txt)}</link>'
                y=paint(para(linked,CW,8.3*s,10.9*s),M,y,CW,draw,'reference')+3*s
            y+=3*s
        else:raise ValueError(k)
    return y
metrics=[]
print('Layout measurements:',[(i+1,round(page_body(p,1.0),1),round(page_body(p,.95),1)) for i,p in enumerate(doc['pages'])])
for number,page in enumerate(doc['pages'],1):
    s=1.0
    while page_body(page,s)>LIMIT and s>.93:s=round(s-.01,2)
    bottom=page_body(page,s)
    if bottom>LIMIT:raise ValueError(f'Page {number} needs editing: bottom {bottom:.1f}, limit {LIMIT:.1f}, scale {s}')
    furniture(number,page['label']);actual=page_body(page,s,True)
    metrics.append({'page':number,'body_font_pt':round(10.2*s,2),'content_bottom':round(actual,2)})
    c.showPage()
c.save()
manifest={'title':doc['title']+': '+doc['subtitle'],'author':doc['author'],'date':'2026-10-06','edition':doc['edition'],'language':'English only','provenance':"AI-assisted editorial synthesis prepared at Ren's request; does not change the research-completion ledger.",'pdf':str(PDF.relative_to(ROOT)),'content_source':str(SOURCE.relative_to(ROOT)),'pdf_sha256':sha256(PDF.read_bytes()).hexdigest(),'content_sha256':sha256(SOURCE.read_bytes()).hexdigest(),'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in doc['sources']},'external_references':[url for page in doc['pages'] for b in page['blocks'] if b['kind']=='refs' for _,url in b['items']],'pages':len(doc['pages']),'page_metrics':metrics,'layout':layout,'previous_edition_source':'archive/build_supporting_pdf.py.english-overview'}
(HERE/'provenance.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'pdf':str(PDF),'sha256':manifest['pdf_sha256'],'metrics':metrics},indent=2))
