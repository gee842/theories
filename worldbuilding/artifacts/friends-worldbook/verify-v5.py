#!/usr/bin/env python3
"""Inspect the actual atlas export; visual review remains a separate human/model step."""
from pathlib import Path
import hashlib,json,re
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parent
book=json.loads((ROOT/'content-v5.json').read_text());pdf=ROOT/'output/pdf/worlds-we-can-inhabit-v5.pdf';reader=PdfReader(pdf)
placements=json.loads((ROOT/'image-placements-v5.json').read_text())
def norm(s):
    return re.sub(r'\s+','',s.replace('\u2011','-').replace('\u2013','-').replace('\u2014','-')).casefold()
def leaves(value):
    if isinstance(value,str):
        if not value.startswith('https://'):yield value
    elif isinstance(value,list):
        for v in value:yield from leaves(v)
    elif isinstance(value,dict):
        for k,v in value.items():
            if k not in ['id','layout','image','pins','url']:yield from leaves(v)
checks=[];images=[];fonts={};links=[];texts=[]
assert len(reader.pages)==len(book['pages'])==34
assert len(reader.outline)==34
for n,(page,copy) in enumerate(zip(reader.pages,book['pages']),1):
    text=page.extract_text();texts.append(f'PAGE {n:02d} / {copy["id"]}\n\n{text}')
    expected=list(leaves(copy))
    if copy['layout']=='evidence':expected+=list(leaves(book['evidence']))
    for value in expected:assert norm(value) in norm(text),(n,value)
    checks.append(dict(page=n,id=copy['id'],copy_complete=True,selectable_characters=len(text)))
    resources=page['/Resources'];fmap=resources.get('/Font',{});xmap=resources.get('/XObject',{})
    for operands,op in page.get_contents().operations:
        if op==b'Tf':
            f=fmap[operands[0]].get_object();name=str(f.get('/BaseFont'))
            if name=='/Helvetica':continue # Canvas initialization uses no text in this default font.
            desc=f.get('/FontDescriptor');embedded=False
            if desc:embedded=any(k in desc.get_object() for k in ['/FontFile','/FontFile2','/FontFile3'])
            fonts[name]=embedded
        if op==b'Do':
            obj=xmap[operands[0]].get_object();assert obj['/Subtype']=='/Image'
            images.append(dict(page=n,sha256=hashlib.sha256(obj.get_data()).hexdigest(),width=obj['/Width'],height=obj['/Height']))
    for ann in page.get('/Annots',[]):
        a=ann.get_object().get('/A',{})
        if a.get('/URI'):links.append(str(a['/URI']))
assert len(images)==len(placements)==25
assert len({x['sha256'] for x in images})==len({x['sha256'] for x in placements})==25
assert [x['page'] for x in images]==[x['page'] for x in placements]
for p in placements:
    assert hashlib.sha256((ROOT/p['path']).read_bytes()).hexdigest()==p['sha256']
    assert p['crop']=='none'
assert sum(p['path'].startswith('assets-v5/') for p in placements)==8
assert len(fonts)==5 and all(fonts.values()),fonts
expected_urls={e['url'] for e in book['evidence']}|{url for label,url in book['pages'][-1]['references']}
assert set(links)==expected_urls
alltext='\n\n'.join(texts)
assert '生生不息' in alltext and 'π0.5' in alltext
assert norm(book['credit']) in norm(texts[0])
(ROOT/'reader-text-v5.txt').write_text(alltext+'\n')
old=json.loads((ROOT/'qa-report-v4.json').read_text())
assert hashlib.sha256((ROOT/old['pdf']).read_bytes()).hexdigest()==old['sha256']
renderfiles=sorted((ROOT/'tmp/pdfs-v5').glob('page-*.png'));assert len(renderfiles)==34
report=dict(edition='05',date='2026-09-07',pdf=str(pdf.relative_to(ROOT)),sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),bytes=pdf.stat().st_size,pages=34,bookmarks=34,link_annotations=len(links),unique_source_links=sorted(set(links)),fonts_used_for_text=fonts,copy_checks=checks,image_source_manifest='image-placements-v5.json',actual_pdf_image_draws=images,unique_source_images=25,unique_pdf_images=25,repeated_image_placements=0,new_source_images=8,uncropped_images=25,render_long_edge_pixels=1200,render_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in renderfiles},previous_edition_04_hash_preserved=old['sha256'])
review_path=ROOT/'visual-review-v5.json'
if review_path.exists():
    review=json.loads(review_path.read_text())
    if review.get('reviewed_pdf_sha256')==report['sha256']:report.update(review)
(ROOT/'qa-report-v5.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:report[k] for k in ['pages','bytes','bookmarks','link_annotations','unique_source_images','unique_pdf_images','uncropped_images']}))
