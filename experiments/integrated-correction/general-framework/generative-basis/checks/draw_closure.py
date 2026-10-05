"""Export a schematic of the checked dependency closure, not an empirical plot."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'figures'
OUT.mkdir(exist_ok=True)
plt.rcParams.update({'font.family': 'DejaVu Sans', 'pdf.fonttype': 42})
fig, ax = plt.subplots(figsize=(15, 7.6), dpi=170)
fig.patch.set_facecolor('#F7F8FA')
ax.set_facecolor('#F7F8FA')
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
ink, muted = '#182B3A', '#4C6170'

ax.text(.025, .955, 'Tracing the conditions of conditions', fontsize=24,
        fontweight='bold', color=ink, va='top')
ax.text(.025, .884, 'Exact closure in the supplied ten-coordinate mechanism network',
        fontsize=13, color=muted)

xs = [.025, .272, .519, .766]
width = .208
cards = [
    ('STARTING QUESTION', '3', 'Burden\nVeto\nEligibility', '#DCE8F0', '#335C78'),
    ('FIRST EXPANSION', '7', 'Add circumstance, response,\nmaintenance and capacity', '#DCEAE5', '#286553'),
    ('CLOSED BASELINE', '9', 'Add record and authority\n\nBadge can be omitted', '#DCEAE5', '#286553'),
    ('NEW AUTHORITY RULE', '10', 'Authority now reads badge\n\nBadge must be included\nin this coordinate closure', '#F2E7D5', '#8A6126'),
]
for x, (title, count, body, fill, edge) in zip(xs, cards):
    ax.add_patch(FancyBboxPatch((x, .405), width, .414,
                  boxstyle='round,pad=0.010,rounding_size=0.018',
                  linewidth=1.2, edgecolor=edge, facecolor=fill))
    ax.text(x+width/2, .779, title, fontsize=10, color=edge,
            ha='center', fontweight='bold')
    ax.text(x+width/2, .694, count, fontsize=39, color=ink,
            ha='center', va='center', fontweight='bold')
    ax.text(x+width/2, .622, 'retained coordinates', fontsize=10,
            color=muted, ha='center')
    ax.text(x+width/2, .560, body, fontsize=11, color=ink,
            ha='center', va='top', linespacing=1.5)
for i in range(3):
    ax.add_patch(FancyArrowPatch((xs[i]+width+.013, .67), (xs[i+1]-.015, .67),
                  arrowstyle='-|>', mutation_scale=15, linewidth=1.3,
                  color=muted))

panels = [
    (.025, .457, 'Omitting a genuine condition fails',
     'Same starting burden, veto and eligibility; different maintenance.',
     'Next burden probability:  0  vs  1/4'),
    (.519, .455, 'A new rule changes what must be represented',
     'Different badge values reach the original protected burden.',
     'Three-step burden probability:  3/8  vs  13/16'),
]
for x, w, title, body, result in panels:
    ax.add_patch(FancyBboxPatch((x, .13), w, .211,
                  boxstyle='round,pad=0.01,rounding_size=0.013',
                  linewidth=.8, edgecolor='#CAD3D9', facecolor='white'))
    ax.text(x+.016, .303, title, color=ink, fontsize=12, fontweight='bold', va='top')
    ax.text(x+.016, .25, body, color=muted, fontsize=10, va='top')
    ax.text(x+.016, .193, result, color='#335C78', fontsize=13, fontweight='bold', va='top')

ax.text(.025, .075, 'Constructed example • exact joint-noise calculations • sufficient coordinate closure, not semantic minimality',
        fontsize=10, color=muted)
ax.text(.025, .033, 'A faithful model can still describe harmful dynamics. Representation closure does not prove desirable persistence.',
        fontsize=10, color=muted)
fig.subplots_adjust(left=.025, right=.99, top=.98, bottom=.03)
for extension in ('png', 'pdf'):
    fig.savefig(OUT/f'closure.{extension}', facecolor=fig.get_facecolor(), bbox_inches='tight')
plt.close(fig)
print(str(OUT/'closure.png'))
