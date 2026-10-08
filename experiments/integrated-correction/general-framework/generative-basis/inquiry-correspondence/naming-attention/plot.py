"""Plot the recorded gaze categories without converting them into learning labels."""
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
data = json.loads((HERE / 'results.json').read_text())['windows']
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11,
                     'axes.spines.top': False, 'axes.spines.right': False,
                     'axes.spines.left': False})
fig, ax = plt.subplots(figsize=(10, 6.2))
fig.subplots_adjust(left=.16, right=.98, top=.89, bottom=.31)
left = np.zeros(len(data))
for key, label, color in [
    ('target_positive', 'Some recorded target gaze', '#387B79'),
    ('zero_target_other_positive', 'Other-object gaze, zero target gaze', '#BC6444'),
    ('both_zero', 'Zero gaze at any coded object', '#D3D6D9'),
]:
    values = np.array([100*x[key]['event_fraction'] for x in data])
    bars = ax.barh(np.arange(len(data)), values, left=left, color=color, label=label, height=.66)
    if key != 'both_zero':
        ax.bar_label(bars, labels=[f'{x:.1f}%' for x in values], label_type='center', color='white', fontsize=10)
    left += values
ax.set_yticks(np.arange(len(data)), [f"{x['window_seconds']:g} s" + ('  (primary)' if x['window_seconds']==3 else '') for x in data])
ax.invert_yaxis()
ax.set_xlim(0,100)
ax.set_xticks([0,25,50,75,100], ['0%','25%','50%','75%','100%'])
ax.set_xlabel('Share of naming events in each nominal window')
ax.tick_params(axis='y', length=0)
ax.set_title('Naming does not guarantee recorded gaze at the target', loc='left', fontsize=16, pad=18)
fig.legend(*ax.get_legend_handles_labels(), loc='lower left', bbox_to_anchor=(.15,.08), ncols=1, frameon=False, fontsize=10)
fig.text(.015,.015, 'Same 1,508 events from 36 infants across all windows. Gaze categories are not learning outcomes.\nPublic OSF mvz78 records, Yu et al. (2021); our descriptive reanalysis. Some exported windows are shorter than nominal.', fontsize=9, color='#444444')
for ext in ['png','svg']:
    fig.savefig(HERE / f'naming-gaze-coverage.{ext}', dpi=180, bbox_inches='tight')
