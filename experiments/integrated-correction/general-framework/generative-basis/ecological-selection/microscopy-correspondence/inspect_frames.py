#!/usr/bin/env python3
"""Decode predetermined first/last high-resolution fields; no event selection or fit."""
import argparse
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import inspect_czi as own
import check_reader as audit


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--fetch',action='store_true');args=parser.parse_args()
    key='collapse-20231123'
    result=json.loads((own.HERE/f'{key}.json').read_text())
    blocks=[b for b in result['selected_subblocks'] if b['scene']==0]
    assert [b['t'] for b in blocks]==[0,90]
    reader=own.Ranges(key,result['archive_path'],result['file_bytes'],args.fetch)
    arrays=[];records=[]
    for b in blocks:
        pieces=[]
        for offset in range(0,b['data_bytes'],4*1024*1024):
            pieces.append(reader.read(b['data_offset']+offset,min(4*1024*1024,b['data_bytes']-offset),'pixel-data'))
        raw=b''.join(pieces)
        assert len(raw)==2752*2208*2
        arr=np.frombuffer(raw,dtype='<u2').reshape(2208,2752)
        arrays.append(arr)
        records.append({'scene':0,'scene_name':'P6','t':b['t'],'pixel_bytes':len(raw),
                        'pixel_sha256':own.digest(raw),'min':int(arr.min()),'max':int(arr.max()),
                        'capture_utc':audit.tags(b)['AcquisitionTime'],
                        'directory_position':b['position']})
    lib=audit.load_reader()
    with lib.CziFile(audit.SavedRanges(own.RAW/key)) as czi:
        for b,arr in zip(blocks,arrays):
            decoded=lib.CziSegment(czi,b['position']).data().data().squeeze()
            assert decoded.shape==arr.shape and np.array_equal(decoded,arr)
    # Identical display limits for both fields; unmodified arrays remain in the
    # original range bodies. These panels are qualitative, not segmentation.
    limits=np.percentile(np.concatenate([a.ravel() for a in arrays]),[1,99.9]).tolist()
    fig,axes=plt.subplots(1,2,figsize=(12,5.5))
    scale=float(next(v['value'] for v in result['metadata_leaves'] if '/Scaling/Items/Distance[Id=X]/Value' in v['path']))*1e6
    for ax,arr,rec in zip(axes,arrays,records):
        ax.imshow(arr,cmap='gray',vmin=limits[0],vmax=limits[1],interpolation='nearest')
        ax.plot([120,120+500/scale],[2050,2050],color='white',lw=3)
        ax.text(120,2000,'500 µm',color='white',fontsize=10)
        ax.set_title(f"Scene 0 / P6 — T={rec['t']}\n{rec['capture_utc'][:19]} UTC",fontsize=10)
        ax.axis('off')
    fig.suptitle('Original collapse-acquisition fields: first and last capture',fontsize=13)
    fig.text(.5,.04,'Shared intensity window; recorded scale 1.419 µm/pixel. Two fields do not identify collapse events or descendants.',ha='center',fontsize=9)
    fig.tight_layout(rect=[0,.08,1,.93]);fig.savefig(own.HERE/'selected-fields.png',dpi=150);plt.close(fig)
    output={'checks_passed':True,'scope':'Predetermined first/last scene; exact all-pixel comparison with unmodified czifile. No event detection, segmentation, growth estimate or culture endpoint score.',
            'script_sha256':own.digest(Path(__file__).read_bytes()),'reader_version':lib.__version__,
            'numpy_version':np.__version__,'matplotlib_version':matplotlib.__version__,
            'frames':records,'display_percentiles':[1,99.9],'display_limits':limits,
            'figure_sha256':own.digest((own.HERE/'selected-fields.png').read_bytes())}
    (own.HERE/'frame-verification.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))


if __name__=='__main__':main()
