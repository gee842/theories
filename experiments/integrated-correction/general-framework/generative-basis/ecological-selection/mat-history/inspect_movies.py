#!/usr/bin/env python3
"""Inspect preserved published movies. Playback times are NOT acquisition times.

Creates selected-frame sheets and checks RGB pixels against a separate complete
framemd5 decode. This checks extraction, not biological interpretations or rates.
Run with Python + Pillow and ffmpeg/ffprobe on PATH. Originals are never edited.
"""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import subprocess

from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / 'RESEARCH.md').exists())
SOURCE = ROOT / 'sources/evolutionary-selection/ferguson-2013'

VIEWS = {
    's1-overview': ('S1', [0, 200, 400, 600, 800, 1000, 1100, 1197], None, 2),
    's1-detail': ('S1', list(range(972, 1105, 12)), [160, 175, 465, 455], 3),
    's4-overview': ('S4', [0, 200, 400, 600, 800, 1000, 1200, 1418], None, 2),
    's5-overview': ('S5', [0, 90, 180, 270, 360, 450, 540, 640], None, 2),
    's6-overview': ('S6', [0, 400, 600, 800, 1000, 1200, 1400, 1536], None, 2),
}


def run(args):
    return subprocess.run(args, check=True, stdout=subprocess.PIPE).stdout


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    manifest = json.loads((SOURCE / 'manifest.json').read_text())
    metadata = json.loads((SOURCE / 'biostudies.json').read_text())
    listed = {f['path']: f['size'] for f in metadata['section']['files']}
    for f in manifest['files']:
        p = SOURCE / f['file']
        assert p.stat().st_size == f['bytes'] and sha(p) == f['sha256']
        if f['file'] in listed:
            assert p.stat().st_size == listed[f['file']]
    figures = HERE / 'figures'
    figures.mkdir(exist_ok=True)
    decoded = {}
    report = {
        'scope': 'Original binding, encoded timestamps and RGB extraction only; no biological clock, counts, event rates or genotype validation.',
        'source_manifest_sha256': sha(SOURCE / 'manifest.json'),
        'script_sha256': sha(Path(__file__)),
        'ffmpeg': run(['ffmpeg', '-version']).decode().splitlines()[0],
        'ffprobe': run(['ffprobe', '-version']).decode().splitlines()[0],
        'movies': {}, 'views': {},
    }
    for f in manifest['files']:
        if 'supplement_label' not in f:
            continue
        label = f['supplement_label']
        p = SOURCE / f['file']
        info = json.loads(run(['ffprobe', '-v', 'error', '-select_streams', 'v:0',
                              '-show_streams', '-show_frames', '-of', 'json', str(p)]))
        stream = info['streams'][0]
        frames = info['frames']
        n = int(stream['nb_frames'])
        assert len(frames) == n
        w, h = stream['width'], stream['height']
        pts = [Fraction(frame['best_effort_timestamp']) * Fraction(stream['time_base'])
               for frame in frames]
        assert all(a < b for a, b in zip(pts, pts[1:]))
        selected = sorted({i for lab, indices, _, _ in VIEWS.values() if lab == label for i in indices})
        assert all(0 <= i < n for i in selected)
        filt = 'select=' + '+'.join('eq(n\\,%d)' % i for i in selected)
        pixels = run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-i', str(p),
                      '-map', '0:v:0', '-vf', filt, '-vsync', '0', '-pix_fmt', 'rgb24',
                      '-f', 'rawvideo', 'pipe:1'])
        stride = w * h * 3
        assert len(pixels) == stride * len(selected)
        # Independent selection path: decode ALL frames and read the hash row at
        # each selected ordinal, rather than reuse the select filter's indices.
        md5text = run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-i', str(p),
                       '-map', '0:v:0', '-vsync', '0', '-pix_fmt', 'rgb24', '-f', 'framemd5', 'pipe:1']).decode()
        hashes = [line.split(',')[-1].strip() for line in md5text.splitlines()
                  if line and not line.startswith('#')]
        assert len(hashes) == n
        record = {'source_file': f['file'], 'source_sha256': f['sha256'],
                  'width': w, 'height': h, 'encoded_frames': n,
                  'frame_rate': stream['avg_frame_rate'], 'time_base': stream['time_base'],
                  'video_duration_playback_seconds': stream['duration'],
                  'legend_span_hours': f['legend_span_hours'],
                  'acquisition_time_mapping_verified': False, 'selected': []}
        decoded[label] = {}
        for ordinal, frame_index in enumerate(selected):
            raw = pixels[ordinal * stride:(ordinal + 1) * stride]
            assert hashlib.md5(raw).hexdigest() == hashes[frame_index]
            decoded[label][frame_index] = (Image.frombytes('RGB', (w, h), raw), pts[frame_index])
            record['selected'].append({'encoded_frame': frame_index,
                                      'playback_pts': str(pts[frame_index]),
                                      'rgb_sha256': hashlib.sha256(raw).hexdigest(),
                                      'full_decode_md5_match': True})
        report['movies'][label] = record
    for name, (label, indices, crop, columns) in VIEWS.items():
        panels = []
        for idx in indices:
            im, pts = decoded[label][idx]
            im = im.crop(crop) if crop else im.copy()
            if not crop:
                im = im.resize((480, 360), Image.Resampling.LANCZOS)
            band = Image.new('RGB', (im.width, im.height + 30), 'white')
            band.paste(im, (0, 0))
            ImageDraw.Draw(band).text((5, im.height + 8),
                                     f'{label} encoded frame {idx}; playback {float(pts):.3f} s', fill='black')
            panels.append(band)
        width, height = panels[0].size
        sheet = Image.new('RGB', (columns * width, ((len(panels) + columns - 1) // columns) * height), 'white')
        for j, panel in enumerate(panels):
            sheet.paste(panel, ((j % columns) * width, (j // columns) * height))
        target = figures / (name + '.png')
        sheet.save(target)
        report['views'][name] = {'source_label': label, 'encoded_frames': indices,
                                 'crop_original_pixels': crop, 'file': str(target.relative_to(HERE)),
                                 'sha256': sha(target)}
    report['selected_unique_frames'] = sum(len(m['selected']) for m in report['movies'].values())
    report['all_decoded_frames'] = sum(m['encoded_frames'] for m in report['movies'].values())
    report['checks_passed'] = True
    (HERE / 'verification.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in ['checks_passed', 'selected_unique_frames', 'all_decoded_frames']}))


if __name__ == '__main__':
    main()
