"""Package the verified atlas and self-contained reading alternatives for sharing."""
from pathlib import Path
import json,hashlib,zipfile,re
R=Path(__file__).resolve().parent
OUT=R/'output/share/friends-worldbook-v5.zip';OUT.parent.mkdir(parents=True,exist_ok=True)
start='''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Worlds we can inhabit — Edition 05</title><style>body{max-width:42rem;margin:8vh auto;padding:1.5rem;background:#f5f1e8;color:#203c32;font:1.15rem/1.65 system-ui,sans-serif}h1{font-family:Georgia,serif;font-weight:400;line-height:1.2}a{color:#203c32;text-underline-offset:.2em}li{margin:.9rem 0}a:focus-visible{outline:3px solid #ab593a;outline-offset:4px}</style></head><body><main><p>REN · DEVELOPED WITH AI · EDITION 05</p><h1>Worlds we can inhabit</h1><p>An illustrated exploration of how automation, shared means and a generative understanding could support different ways of living.</p><ul><li><a href="worlds-we-can-inhabit-v5.pdf">Open the 34-page illustrated atlas</a></li><li><a href="reader-v5.html">Read the complete text with image and diagram descriptions</a></li><li><a href="reader-v5.md">Open the Markdown text</a></li></ul><p>These are proposed futures with explicit assumptions and linked technical sources. The text reader works offline; external references need an internet connection.</p></main></body></html>'''
files={'worlds-we-can-inhabit-v5.pdf':(R/'output/pdf/worlds-we-can-inhabit-v5.pdf').read_bytes(),'reader-v5.html':(R/'reader-v5.html').read_bytes(),'reader-v5.md':(R/'reader-v5.md').read_bytes(),'START-HERE.html':start.encode(),'README.txt':b'Worlds we can inhabit / Edition 05\nA worldbuilding project by Ren, developed with AI\n7 September 2026\n\nExtract this entire ZIP into one folder, then open START-HERE.html.\nThe PDF, HTML reader and Markdown reader can also be opened directly.\nThe HTML reader contains full copy, illustration descriptions and sources.\nNo installation or account is required. External sources require internet access.\nThe PDF is selectable and bookmarked, but is not a tagged PDF.\n'}
assert all(target in files for target in re.findall('href="([^"]+)"',start))
manifest={n:hashlib.sha256(data).hexdigest() for n,data in files.items()}
files['SHA256.json']=(json.dumps(manifest,indent=2)+'\n').encode()
with zipfile.ZipFile(OUT,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for name,data in files.items():z.writestr(name,data)
with zipfile.ZipFile(OUT) as z:
 assert z.testzip() is None
 for name,digest in manifest.items():assert hashlib.sha256(z.read(name)).hexdigest()==digest
report={'package':str(OUT.relative_to(R)),'bytes':OUT.stat().st_size,'sha256':hashlib.sha256(OUT.read_bytes()).hexdigest(),'members':manifest,'archive_integrity':True,'start_page_links_resolve_inside_package':True}
(R/'package-report-v5.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report))
