#!/usr/bin/env python3
"""Preserve post-inspection diagnostics without changing the prospective detector."""
import csv
import hashlib
import json
import math
from pathlib import Path
import numpy as np
from scipy import ndimage
import analyze

HERE=Path(__file__).resolve().parent


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    tracks=json.loads((HERE/'longest-diagnostic-tracks.json').read_text())
    rows=list(csv.DictReader((HERE/'regions.csv').open()))
    reviews=[]
    visual={
        9:'The small feature near the last assigned center remains weakly visible; this ending is not certified local structural loss.',
        2:'A large bright structure is visible through T48 and absent from the same local window at T49 and T50. This is abrupt local image loss, not a demonstrated vertical collapse or loss of viable cells.',
        3:'The large structure is still visible at T47 after its assigned track ends at T46. At T47 its thresholded region touches the right crop boundary and is excluded by the declared detector. It is absent from the displayed local window at T48.',
        10:'A large bright structure is visible through T45 and absent from the same local window at T46 and T47. Motion out of the plane or field, dispersal and collapse require further discrimination.'}
    for track in tracks:
        last=track['observations'][-1];measurements=[]
        for k in [4,6,8]:
            candidates=[r for r in rows if int(r['threshold'])==k and int(r['t'])==last['t']]
            r=min(candidates,key=lambda r:math.hypot(float(r['x_px'])-last['x_px'],float(r['y_px'])-last['y_px']))
            distance=math.hypot(float(r['x_px'])-last['x_px'],float(r['y_px'])-last['y_px'])
            measurements.append({'threshold':k,'nearest_center_distance_px':distance,
                                 'within_post_inspection_five_pixel_gate':distance<=5,
                                 'diameter_um':float(r['diameter_um']) if distance<=5 else None})
        reviews.append({'track':track['track'],'last_assigned_t':last['t'],
                        'last_region_threshold_sensitivity':measurements,'visual_assessment':visual[track['track']]})
    receipt=json.loads((HERE/'acquisition-verification.json').read_text())
    images=np.load(receipt['cache_path'])['images']
    _,residual,noise,median=analyze.detect(images[47],6)
    labels,n=ndimage.label(residual>median+6*noise,structure=np.ones((3,3)))
    boundary=[]
    for label,sl in enumerate(ndimage.find_objects(labels),1):
        if sl and sl[1].stop==512 and sl[0].start<150 and sl[0].stop>90:
            boundary.append({'label':label,'box_yx':[[s.start,s.stop] for s in sl],
                             'area_px':int((labels[sl]==label).sum()),'touches_right_boundary':True})
    assert boundary==[{'label':7,'box_yx':[[85,134],[468,512]],'area_px':1622,'touches_right_boundary':True}]
    result={'scope':'AI visual assessment and post-inspection numerical diagnostics for the four longest assigned tracks; no new confirmatory dataset or biological event-rate estimate.',
            'selection':'Four longest tracks in the prospective threshold-6 / 40-micrometer matching analysis; ties ordered by track number.',
            'reviews':reviews,'track_3_boundary_diagnostic_at_t47':boundary,
            'script_sha256':sha(Path(__file__)),'analyze_sha256':sha(HERE/'analyze.py'),
            'endpoint_figure_sha256':sha(HERE/'endpoint-inspection.png'),
            'track_record_sha256':sha(HERE/'longest-diagnostic-tracks.json')}
    (HERE/'endpoint-review.json').write_text(json.dumps(result,indent=2)+'\n')
    print('Preserved four visual assessments, threshold sensitivity and the checked boundary exclusion.')


if __name__=='__main__':main()
