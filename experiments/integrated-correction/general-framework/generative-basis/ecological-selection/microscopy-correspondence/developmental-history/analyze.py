#!/usr/bin/env python3
"""Exploratory region trajectories with fixed detection and matching sensitivity."""
import csv
from datetime import datetime
import hashlib
import json
from pathlib import Path
import sys
import numpy as np
from scipy import ndimage
from scipy.optimize import linear_sum_assignment
import scipy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import acquire


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def detect(image,k):
    smooth=ndimage.gaussian_filter(image.astype(float),1)
    residual=smooth-ndimage.gaussian_filter(smooth,16)
    median=np.median(residual)
    scale=max(1.,float(1.4826*np.median(np.abs(residual-median))))
    labels,n=ndimage.label(residual>median+k*scale,structure=np.ones((3,3)))
    regions=[]
    for label,sl in enumerate(ndimage.find_objects(labels),1):
        if sl is None:continue
        yy,xx=sl
        if yy.start==0 or xx.start==0 or yy.stop==image.shape[0] or xx.stop==image.shape[1]:continue
        mask=labels[sl]==label
        area=int(mask.sum())
        if area<9:continue
        y,x=np.nonzero(mask)
        regions.append({'label':label,'area_px':area,'y_px':float(np.mean(y)+yy.start),
                        'x_px':float(np.mean(x)+xx.start),'peak_residual':float(residual[sl][mask].max())})
    return regions,residual,scale,median


def match(previous,current,limit_um,scale_um):
    n,m=len(previous),len(current)
    if n==0 or m==0:return [],np.zeros((n,m),dtype=bool)
    p=np.array([[r['x_px'],r['y_px']] for r in previous])
    q=np.array([[r['x_px'],r['y_px']] for r in current])
    distance=np.sqrt(((p[:,None]-q[None,:])**2).sum(axis=2))*scale_um
    ratio=np.array([r['area_px'] for r in current])[None,:]/np.array([r['area_px'] for r in previous])[:,None]
    allowed=(distance<=limit_um)&(ratio>=.25)&(ratio<=4)
    # Large unmatched cost prioritizes maximum cardinality at this small field
    # size, then distance. Dummy assignments permit both births and losses.
    assert n+m<10000
    cost=np.full((n+m,n+m),1.e12)
    cost[:n,:m]=np.where(allowed,distance,1.e12)
    cost[:n,m:]=1.e6
    cost[n:,:m]=1.e6
    cost[n:,m:]=0
    left,right=linear_sum_assignment(cost)
    matches=[(int(i),int(j),float(distance[i,j]),bool(allowed[i].sum()>1 or allowed[:,j].sum()>1))
             for i,j in zip(left,right) if i<n and j<m and allowed[i,j]]
    return matches,allowed


def write_csv(path,rows,fields):
    with path.open('w',newline='') as out:
        w=csv.DictWriter(out,fieldnames=fields);w.writeheader();w.writerows(rows)


def main():
    receipt=json.loads((HERE/'acquisition-verification.json').read_text())
    cache=Path(receipt['cache_path']);assert sha(cache)==receipt['cache_sha256']
    images=np.load(cache)['images'];assert images.shape==(91,512,512) and images.dtype==np.uint16
    records=[json.loads((HERE/f'frame-{t:03d}.json').read_text()) for t in range(91)]
    for t,(rec,image) in enumerate(zip(records,images)):
        assert sha(HERE/f'frame-{t:03d}.json')==receipt['frame_record_sha256'][f'frame-{t:03d}.json']
        assert hashlib.sha256(image.tobytes()).hexdigest()==rec['crop_sha256']
    source=json.loads((HERE.parent/'collapse-20231123.json').read_text())
    scale_um=float(next(r['value'] for r in source['metadata_leaves'] if '/Scaling/Items/Distance[Id=X]/Value' in r['path']))*1e6
    captures=[datetime.fromisoformat(r['capture_utc'].replace('Z','+00:00')) for r in records]
    hours=np.array([(t-captures[0]).total_seconds()/3600 for t in captures])
    assert np.all(np.diff(hours)>0)
    tagsets=[{r['path']:r['value'] for r in rec['metadata_leaves']} for rec in records]
    variable={key:sorted(set(tags.get(key,'MISSING') for tags in tagsets)) for key in set().union(*tagsets)}
    variable={key:values for key,values in variable.items() if len(values)>1}
    acquisition_fields={key:sorted(set(tags.get(key,'MISSING') for tags in tagsets)) for key in set().union(*tagsets)
                        if any(s in key.lower() for s in ['stage','focus','exposure','illum','gain','validbits'])}
    region_lists={};all_regions=[];frame_rows=[];residuals=[]
    for t,image in enumerate(images):
        for k in [4,6,8]:
            regions,residual,noise,median=detect(image,k)
            region_lists[k,t]=regions
            for region in regions:
                region['diameter_um']=float(2*np.sqrt(region['area_px']/np.pi)*scale_um)
                all_regions.append({'threshold':k,'t':t,'hours':float(hours[t]),**region})
            frame_rows.append({'threshold':k,'t':t,'hours':float(hours[t]),'regions':len(regions),
                               'median_raw':float(np.median(image)),'q999_raw':float(np.quantile(image,.999)),
                               'residual_mad_scale':noise,'median_residual':float(median),
                               'region_area_fraction':sum(r['area_px'] for r in regions)/image.size})
            if k==6:residuals.append((residual,noise,median))
    all_matches=[];summaries=[];diagnostic_tracks={}
    for k,bound in [(4,40),(6,40),(8,40),(6,20),(6,80)]:
        trajectories={};active={};next_id=0;unmatched_old=0;unmatched_new=0;ambiguous=0;matched_total=0
        for j in range(len(region_lists[k,0])):
            active[j]=next_id;trajectories[next_id]=[(0,j)];next_id+=1
        for t in range(90):
            previous,current=region_lists[k,t],region_lists[k,t+1]
            links,candidates=match(previous,current,bound,scale_um)
            matched_total+=len(links);ambiguous+=sum(item[3] for item in links)
            unmatched_old+=len(previous)-len(links);unmatched_new+=len(current)-len(links)
            after={}
            for i,j,distance,uncertain in links:
                track=active[i];after[j]=track;trajectories[track].append((t+1,j))
                all_matches.append({'threshold':k,'bound_um':bound,'t':t,'source_label':previous[i]['label'],
                                    'target_label':current[j]['label'],'distance_um':distance,'ambiguous':int(uncertain),
                                    'dt_seconds':float((hours[t+1]-hours[t])*3600),'track':track})
            for j in range(len(current)):
                if j not in after:
                    after[j]=next_id;trajectories[next_id]=[(t+1,j)];next_id+=1
            active=after
        lengths=[len(t) for t in trajectories.values()]
        summaries.append({'threshold':k,'bound_um':bound,'region_instances':sum(len(region_lists[k,t]) for t in range(91)),
                          'matched_pairs':matched_total,'ambiguous_matched_pairs':ambiguous,'unmatched_previous':unmatched_old,
                          'unmatched_next':unmatched_new,'tracks':len(lengths),'one_frame_tracks':sum(n==1 for n in lengths),
                          'tracks_at_least_three_frames':sum(n>=3 for n in lengths),'longest_track_frames':max(lengths,default=0)})
        if (k,bound)==(6,40):diagnostic_tracks=trajectories
    write_csv(HERE/'regions.csv',all_regions,['threshold','t','hours','label','area_px','y_px','x_px','peak_residual','diameter_um'])
    write_csv(HERE/'frame-summaries.csv',frame_rows,list(frame_rows[0]))
    write_csv(HERE/'adjacent-matches.csv',all_matches,list(all_matches[0]) if all_matches else ['threshold','bound_um','t'])
    # Evenly spaced frames were chosen in the protocol; both shared raw display
    # and threshold-standardized local contrast are shown without pixel editing.
    times=list(range(0,91,10));lo,hi=np.quantile(images,[.01,.999])
    fig,axes=plt.subplots(2,5,figsize=(14,7.4))
    for ax,t in zip(axes.flat,times):
        ax.imshow(images[t],cmap='gray',vmin=lo,vmax=hi,interpolation='nearest')
        ax.set_title(f'{hours[t]:.2f} h · T={t}',fontsize=10);ax.axis('off')
        if t==0:ax.plot([30,30+100/scale_um],[475,475],color='white',lw=2);ax.text(30,453,'100 µm',color='white',fontsize=8)
    fig.suptitle('One fixed field through 15 hours of original imaging',fontsize=14)
    fig.text(.5,.015,'Karita et al. · S-BIAD2117 · scene 0/P6 · central 512 × 512 pixels · shared intensity window',ha='center',fontsize=9)
    fig.subplots_adjust(left=.02,right=.98,bottom=.09,top=.90,hspace=.32,wspace=.03)
    fig.savefig(HERE/'raw-history.png',dpi=150);plt.close(fig)
    fig,axes=plt.subplots(2,5,figsize=(14,7.4))
    for ax,t in zip(axes.flat,times):
        residual,noise,median=residuals[t]
        ax.imshow((residual-median)/noise,cmap='gray',vmin=0,vmax=12,interpolation='nearest')
        regions=region_lists[6,t]
        for r in regions:
            ax.add_patch(plt.Circle((r['x_px'],r['y_px']),np.sqrt(r['area_px']/np.pi),fill=False,ec='#fca636',lw=.6))
        ax.set_title(f'{hours[t]:.2f} h · {len(regions)} regions',fontsize=10);ax.axis('off')
    fig.suptitle('Local contrast and detected regions are measurement choices',fontsize=14)
    fig.text(.5,.015,'Display: residual / robust noise · circles: equivalent area at threshold 6 · regions are not verified colonies',ha='center',fontsize=9)
    fig.subplots_adjust(left=.02,right=.98,bottom=.09,top=.90,hspace=.32,wspace=.03)
    fig.savefig(HERE/'region-history.png',dpi=150);plt.close(fig)
    fig,axes=plt.subplots(1,3,figsize=(13,3.7))
    for k in [4,6,8]:
        rows=[r for r in frame_rows if r['threshold']==k]
        axes[0].plot(hours,[r['regions'] for r in rows],label=f'{k} × robust noise',lw=1.1)
    axes[0].set(xlabel='Hours from first capture',ylabel='Resolved regions');axes[0].legend(fontsize=7)
    mid=[r for r in frame_rows if r['threshold']==6]
    axes[1].plot(hours,[r['median_raw'] for r in mid]);axes[1].set(xlabel='Hours from first capture',ylabel='Median recorded intensity')
    cats=[f'{s["threshold"]}σ / {s["bound_um"]}µm' for s in summaries]
    axes[2].bar(cats,[s['matched_pairs'] for s in summaries],label='All assigned links')
    axes[2].bar(cats,[s['ambiguous_matched_pairs'] for s in summaries],label='With alternative partner')
    axes[2].tick_params(axis='x',rotation=45,labelsize=7);axes[2].set(ylabel='Adjacent-frame assignments');axes[2].legend(fontsize=7)
    fig.suptitle('Detection and identity sensitivity in one field',fontsize=13)
    fig.tight_layout();fig.savefig(HERE/'measurement-sensitivity.png',dpi=170);plt.close(fig)
    selected=sorted(diagnostic_tracks.items(),key=lambda item:(-len(item[1]),item[0]))[:4]
    track_records=[]
    for identity,path in selected:
        track_records.append({'track':identity,'observations':[{'t':t,**region_lists[6,t][j]} for t,j in path]})
    (HERE/'longest-diagnostic-tracks.json').write_text(json.dumps(track_records,indent=2)+'\n')
    fig,axes=plt.subplots(4,5,figsize=(12,10))
    for row,track in enumerate(track_records):
        last=track['observations'][-1];tend=last['t']
        x0=int(np.clip(round(last['x_px'])-48,0,416));y0=int(np.clip(round(last['y_px'])-48,0,416))
        selected_times=[max(0,min(90,tend+d)) for d in [-2,-1,0,1,2]]
        fields=images[selected_times,y0:y0+96,x0:x0+96]
        vlo,vhi=np.quantile(fields,[.01,.999])
        for col,(t,field) in enumerate(zip(selected_times,fields)):
            ax=axes[row,col];ax.imshow(field,cmap='gray',vmin=vlo,vmax=vhi,interpolation='nearest')
            ax.plot(last['x_px']-x0,last['y_px']-y0,'+',color='#fca636',ms=9,mew=1)
            ax.set_title(f'T={t} · {hours[t]:.2f} h',fontsize=9);ax.set_xticks([]);ax.set_yticks([])
            if col==0:ax.set_ylabel(f'Track {track["track"]}\n{len(track["observations"])} frames',fontsize=9)
        track['endpoint_inspection']={'times':selected_times,'crop_xywh':[x0,y0,96,96],
                                      'display_limits':[float(vlo),float(vhi)],'last_position_marked':True}
    fig.suptitle('Endpoints of the four longest assigned trajectories',fontsize=14)
    fig.text(.5,.015,'Each row uses one fixed window and intensity range. Cross: last assigned center. Assignment ending is not biological collapse.',ha='center',fontsize=9)
    fig.subplots_adjust(left=.09,right=.98,bottom=.06,top=.91,hspace=.28,wspace=.06)
    fig.savefig(HERE/'endpoint-inspection.png',dpi=150);plt.close(fig)
    (HERE/'longest-diagnostic-tracks.json').write_text(json.dumps(track_records,indent=2)+'\n')
    summary={'status':'passed','scope':'Exploratory image-region measurements and assignment sensitivity in one preselected field; not validated colony identity, collapse events, culture outcome or descendants.',
             'frames':91,'pixel_scale_um':scale_um,'field_side_um':scale_um*512,'duration_hours':float(hours[-1]),
             'dt_seconds_min_max':[float(np.diff(hours).min()*3600),float(np.diff(hours).max()*3600)],
             'acquisition_fields':acquisition_fields,'variable_metadata_fields':variable,
             'frame_count_ranges':{str(k):[min(len(region_lists[k,t]) for t in range(91)),max(len(region_lists[k,t]) for t in range(91))] for k in [4,6,8]},
             'sensitivity':summaries,'display_raw_limits':[float(lo),float(hi)],
             'versions':{'numpy':np.__version__,'scipy':scipy.__version__,'matplotlib':matplotlib.__version__},
             'script_sha256':sha(Path(__file__)),'acquisition_receipt_sha256':sha(HERE/'acquisition-verification.json'),
             'output_sha256':{name:sha(HERE/name) for name in ['regions.csv','frame-summaries.csv','adjacent-matches.csv','raw-history.png','region-history.png','measurement-sensitivity.png','endpoint-inspection.png','longest-diagnostic-tracks.json']}}
    (HERE/'results.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps({key:summary[key] for key in ['status','frames','duration_hours','frame_count_ranges','sensitivity']},indent=2))


if __name__=='__main__':main()
