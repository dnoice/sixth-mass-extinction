"""
Generate Phase 2 Visualizations for Episode 1.1
Uses SME Vintage matplotlib style
"""
import sys
from pathlib import Path
import json

# Paths
NOTEBOOK_DIR = Path(__file__).parent
STYLE_PATH = NOTEBOOK_DIR.parents[3] / 'bonus-material' / 'mini-series' / 'assets' / 'styles' / 'sme_vintage.mplstyle'
DUMP_DIR = NOTEBOOK_DIR.parent / 'sources' / 'dump'
FIGURES_DIR = NOTEBOOK_DIR.parent / 'figures'
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

# Imports
import polars as pl
import matplotlib.pyplot as plt
import numpy as np

# Load SME style
plt.style.use(str(STYLE_PATH))
print(f'Loaded style: {STYLE_PATH.name}')

# Load data
IUCN_FULL = DUMP_DIR / 'iucn-species-exports' / 'full-export' / 'simple_summary.csv'
df = pl.read_csv(IUCN_FULL)

# Filter vertebrates
VERTEBRATE_CLASSES = ['MAMMALIA', 'AVES', 'REPTILIA', 'AMPHIBIA', 'ACTINOPTERYGII', 'CHONDRICHTHYES']
vertebrates = df.filter(pl.col('className').is_in(VERTEBRATE_CLASSES))
extinct = vertebrates.filter(pl.col('redlistCategory').is_in(['Extinct', 'Extinct in the Wild']))

# E/MSY calculation
TIME_PERIOD = 124

def calc_emsy(ext, spp, yrs):
    return (ext / (spp * yrs)) * 1_000_000

# Calculate by taxa
taxa_data = []
TAXA_LABELS = {
    'MAMMALIA': 'Mammals',
    'AVES': 'Birds',
    'REPTILIA': 'Reptiles',
    'AMPHIBIA': 'Amphibians',
    'ACTINOPTERYGII': 'Bony Fish',
    'CHONDRICHTHYES': 'Sharks & Rays'
}

for taxon in VERTEBRATE_CLASSES:
    t_df = vertebrates.filter(pl.col('className') == taxon)
    t_ext = extinct.filter(pl.col('className') == taxon)
    n_spp = len(t_df)
    n_ext = len(t_ext)
    if n_spp > 0:
        emsy = calc_emsy(n_ext, n_spp, TIME_PERIOD)
        taxa_data.append({
            'taxon': TAXA_LABELS[taxon],
            'extinctions': n_ext,
            'species': n_spp,
            'emsy': emsy,
            'multiplier': emsy / 1.0
        })

taxa_data.sort(key=lambda x: x['emsy'], reverse=True)

# ============================================================
# FIGURE 1: E/MSY by Taxa
# ============================================================
print('Generating Figure 1: E/MSY by Taxa...')
fig, ax = plt.subplots(figsize=(12, 7))

taxa = [d['taxon'] for d in taxa_data]
emsy_vals = [d['emsy'] for d in taxa_data]

bars = ax.barh(taxa, emsy_vals, color='#97613B', alpha=0.85, edgecolor='#3B3527', linewidth=1.2)

# Background rate reference lines
ax.axvline(x=0.1, color='#254340', linestyle='--', linewidth=2, label='Background 0.1 E/MSY (Pimm)')
ax.axvline(x=1.0, color='#B08E42', linestyle='--', linewidth=2, label='Background 1.0 E/MSY (Traditional)')
ax.axvline(x=2.0, color='#8C5A24', linestyle='--', linewidth=2, label='Background 2.0 E/MSY (De Vos)')

ax.set_xlabel('E/MSY (Extinctions per Million Species-Years)', fontsize=12)
ax.set_title('Modern Vertebrate Extinction Rates by Taxonomic Class\n1900-2024 vs Background Rates', fontsize=14, fontweight='bold')
ax.legend(loc='lower right', fontsize=9)

# Value labels
for bar, val in zip(bars, emsy_vals):
    ax.text(val + 2, bar.get_y() + bar.get_height()/2, f'{val:.1f}', va='center', fontsize=10, color='#3B3527')

ax.set_xlim(0, max(emsy_vals) * 1.15)
plt.tight_layout()
plt.savefig(FIGURES_DIR / '01_emsy_by_taxa.png', dpi=300)
plt.close()
print(f'  Saved: 01_emsy_by_taxa.png')

# ============================================================
# FIGURE 2: Rate Multipliers
# ============================================================
print('Generating Figure 2: Rate Multipliers...')
fig, ax = plt.subplots(figsize=(12, 7))

multipliers = [d['multiplier'] for d in taxa_data]

# Color by severity
colors = ['#3E2B26' if m > 100 else '#97613B' if m > 50 else '#B08E42' for m in multipliers]
bars = ax.barh(taxa, multipliers, color=colors, alpha=0.85, edgecolor='#3B3527', linewidth=1.2)

ax.axvline(x=1, color='#6D6046', linestyle='-', linewidth=1.5, label='1x (No elevation)')
ax.axvline(x=10, color='#B08E42', linestyle='--', linewidth=1.5, label='10x background')
ax.axvline(x=100, color='#8C5A24', linestyle='--', linewidth=1.5, label='100x background')

ax.set_xlabel('Rate Multiplier (vs 1.0 E/MSY background)', fontsize=12)
ax.set_title('How Many Times Above Background Rate?\nVertebrate Extinction 1900-2024', fontsize=14, fontweight='bold')
ax.legend(loc='lower right', fontsize=9)
ax.set_xscale('log')

for bar, val in zip(bars, multipliers):
    ax.text(val * 1.1, bar.get_y() + bar.get_height()/2, f'{val:.0f}x', va='center', fontsize=10, color='#3B3527')

plt.tight_layout()
plt.savefig(FIGURES_DIR / '02_rate_multipliers.png', dpi=300)
plt.close()
print(f'  Saved: 02_rate_multipliers.png')

# ============================================================
# FIGURE 3: Category Distribution (Threat Pyramid)
# ============================================================
print('Generating Figure 3: Category Distribution...')
fig, ax = plt.subplots(figsize=(10, 8))

cats = vertebrates.group_by('redlistCategory').agg(pl.len().alias('count')).sort('count', descending=True)

# Define order and colors (IUCN-inspired but SME palette)
cat_order = ['Least Concern', 'Data Deficient', 'Near Threatened', 'Vulnerable', 'Endangered', 'Critically Endangered', 'Extinct in the Wild', 'Extinct']
cat_colors = {
    'Least Concern': '#95A186',       # What Remains (survival)
    'Data Deficient': '#7C5F47',      # Matriarch Absence (unknown)
    'Near Threatened': '#B08E42',     # Thermal Threshold
    'Vulnerable': '#8C5A24',          # Colony Collapse
    'Endangered': '#97613B',          # Ivory Market
    'Critically Endangered': '#3E2B26', # Impact Point
    'Extinct in the Wild': '#254340', # Anoxic Depths
    'Extinct': '#1A2628'              # Night Migration
}

# Filter to existing categories
cat_data = []
for cat in cat_order:
    row = cats.filter(pl.col('redlistCategory') == cat)
    if len(row) > 0:
        cat_data.append({'cat': cat, 'count': row['count'][0]})

categories = [d['cat'] for d in cat_data]
counts = [d['count'] for d in cat_data]
colors = [cat_colors.get(c, '#6D6046') for c in categories]

bars = ax.barh(categories, counts, color=colors, alpha=0.85, edgecolor='#3B3527', linewidth=1.2)

ax.set_xlabel('Number of Species', fontsize=12)
ax.set_title('IUCN Red List Category Distribution\nVertebrates (n={:,})'.format(sum(counts)), fontsize=14, fontweight='bold')

for bar, val in zip(bars, counts):
    ax.text(val + 200, bar.get_y() + bar.get_height()/2, f'{val:,}', va='center', fontsize=9, color='#3B3527')

ax.set_xlim(0, max(counts) * 1.12)
plt.tight_layout()
plt.savefig(FIGURES_DIR / '03_category_distribution.png', dpi=300)
plt.close()
print(f'  Saved: 03_category_distribution.png')

# ============================================================
# FIGURE 4: Extinction Counts by Class (Stacked)
# ============================================================
print('Generating Figure 4: Extinction Counts...')
fig, ax = plt.subplots(figsize=(10, 6))

ext_data = []
for taxon in VERTEBRATE_CLASSES:
    t_ext_ex = extinct.filter((pl.col('className') == taxon) & (pl.col('redlistCategory') == 'Extinct'))
    t_ext_ew = extinct.filter((pl.col('className') == taxon) & (pl.col('redlistCategory') == 'Extinct in the Wild'))
    ext_data.append({
        'taxon': TAXA_LABELS[taxon],
        'EX': len(t_ext_ex),
        'EW': len(t_ext_ew)
    })

ext_data.sort(key=lambda x: x['EX'] + x['EW'], reverse=True)
taxa_ext = [d['taxon'] for d in ext_data]
ex_counts = [d['EX'] for d in ext_data]
ew_counts = [d['EW'] for d in ext_data]

x = np.arange(len(taxa_ext))
width = 0.6

bars1 = ax.bar(x, ex_counts, width, label='Extinct (EX)', color='#1A2628', edgecolor='#3B3527', linewidth=1)
bars2 = ax.bar(x, ew_counts, width, bottom=ex_counts, label='Extinct in Wild (EW)', color='#254340', edgecolor='#3B3527', linewidth=1)

ax.set_ylabel('Number of Species', fontsize=12)
ax.set_title('Documented Vertebrate Extinctions by Class\nIUCN Red List 2025', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(taxa_ext, rotation=45, ha='right')
ax.legend(loc='upper right')

# Total labels
for i, (ex, ew) in enumerate(zip(ex_counts, ew_counts)):
    total = ex + ew
    ax.text(i, total + 2, str(total), ha='center', fontsize=10, color='#3B3527', fontweight='bold')

plt.tight_layout()
plt.savefig(FIGURES_DIR / '04_extinction_counts.png', dpi=300)
plt.close()
print(f'  Saved: 04_extinction_counts.png')

# ============================================================
# FIGURE 5: Rate Comparison Summary
# ============================================================
print('Generating Figure 5: Rate Comparison...')
fig, ax = plt.subplots(figsize=(10, 6))

# Overall vertebrate rate
total_ext = len(extinct)
total_spp = len(vertebrates)
current_emsy = calc_emsy(total_ext, total_spp, TIME_PERIOD)

rates = ['Background\n(Conservative)', 'Background\n(Traditional)', 'Background\n(Upper)', 'Current\nVertebrate Rate']
values = [0.1, 1.0, 2.0, current_emsy]
colors_bar = ['#95A186', '#B08E42', '#8C5A24', '#3E2B26']

bars = ax.bar(rates, values, color=colors_bar, alpha=0.85, edgecolor='#3B3527', linewidth=1.5, width=0.6)

ax.set_ylabel('E/MSY', fontsize=12)
ax.set_title('Background vs Current Extinction Rates\nVertebrates 1900-2024', fontsize=14, fontweight='bold')
ax.set_yscale('log')

for bar, val in zip(bars, values):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height * 1.15, f'{val:.1f}', ha='center', fontsize=11, color='#3B3527', fontweight='bold')

# Add multiplier annotation
ax.annotate(f'{current_emsy/1.0:.0f}x higher', xy=(3, current_emsy), xytext=(2.2, current_emsy*0.25),
            fontsize=12, color='#3E2B26', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#3E2B26', lw=1.5))

plt.tight_layout()
plt.savefig(FIGURES_DIR / '05_rate_comparison.png', dpi=300)
plt.close()
print(f'  Saved: 05_rate_comparison.png')

print('\n=== All 5 figures generated with SME Vintage style ===')
print(f'Output directory: {FIGURES_DIR}')
