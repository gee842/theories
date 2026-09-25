import sys,zipfile,struct,re,os

def snappy_decompress(data):
    # minimal Snappy raw block decompressor
    def varint(b,i):
        v=0;s=0
        while True:
            c=b[i];i+=1;v|=(c&0x7f)<<s
            if not c&0x80: return v,i
            s+=7
    ulen,i=varint(data,0)
    out=bytearray()
    while i<len(data):
        tag=data[i]; i+=1
        t=tag&0x03
        if t==0:
            ln=tag>>2
            if ln<60: n=ln+1
            elif ln==60: n=data[i]+1; i+=1
            elif ln==61: n=int.from_bytes(data[i:i+2],'little')+1; i+=2
            elif ln==62: n=int.from_bytes(data[i:i+3],'little')+1; i+=3
            else: n=int.from_bytes(data[i:i+4],'little')+1; i+=4
            out+=data[i:i+n]; i+=n
        else:
            if t==1:
                n=4+((tag>>2)&0x7); off=((tag>>5)<<8)|data[i]; i+=1
            elif t==2:
                n=(tag>>2)+1; off=int.from_bytes(data[i:i+2],'little'); i+=2
            else:
                n=(tag>>2)+1; off=int.from_bytes(data[i:i+4],'little'); i+=4
            if off==0 or off>len(out): raise ValueError('bad offset')
            start=len(out)-off
            for k in range(n): out.append(out[start+k])
    return bytes(out)

def iwa_chunks(raw):
    out=bytearray(); i=0
    while i+4<=len(raw):
        ln=raw[i+1]|(raw[i+2]<<8)|(raw[i+3]<<16)
        chunk=raw[i+4:i+4+ln]
        if not chunk: break
        try: out+=snappy_decompress(chunk)
        except Exception: pass
        i+=4+ln
    return bytes(out)

def strings(buf, minlen=2):
    res=[]; 
    # protobuf length-delimited UTF-8 strings
    i=0
    while i < len(buf):
        b=buf[i]
        if (b & 0x07) == 2:
            j=i+1; ln=0; sh=0; ok=True
            for _ in range(5):
                if j>=len(buf): ok=False;break
                c=buf[j]; j+=1; ln |= (c&0x7f)<<sh
                if not c&0x80: break
                sh+=7
            else: ok=False
            if ok and 0 < ln < 200000 and j+ln <= len(buf):
                s=buf[j:j+ln]
                try:
                    t=s.decode('utf-8')
                    if len(t)>=minlen and sum(1 for ch in t if ch.isprintable() or ch in '\n\r\t')/len(t) > 0.95:
                        res.append(t); i=j+ln; continue
                except UnicodeDecodeError: pass
        i+=1
    return res

path=sys.argv[1]
z=zipfile.ZipFile(path)
names=[n for n in z.namelist() if n.endswith('.iwa')]
allt=[]
for n in sorted(names):
    buf=iwa_chunks(z.read(n))
    for s in strings(buf):
        allt.append(s)
seen=set(); out=[]
for s in allt:
    if s in seen: continue
    seen.add(s)
    if re.fullmatch(r'[\x00-\x1f]*', s): continue
    out.append(s)
print('\n'.join(out))
