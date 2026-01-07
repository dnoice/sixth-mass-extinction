"""
Temporal Pattern Analysis for Episode 1.1
Analyzes extinction patterns across 5 historical epochs
"""
import polars as pl
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from collections import defaultdict

# Paths
NOTEBOOK_DIR = Path(__file__).parent
STYLE_PATH = NOTEBOOK_DIR.parents[3] / 'bonus-material' / 'mini-series' / 'assets' / 'styles' / 'sme_vintage.mplstyle'
DUMP_DIR = NOTEBOOK_DIR.parent / 'sources' / 'dump'
FIGURES_DIR = NOTEBOOK_DIR.parent / 'figures'
EXPORTS_DIR = NOTEBOOK_DIR.parent / 'data' / 'processed'

# Load style
plt.style.use(str(STYLE_PATH))

# Define epochs per blueprint
EPOCHS = {
    'Pre-1500': (0, 1499),
    '1500-1900\nColonial Expansion': (1500, 1899),
    '1900-1950\nEarly Industrial': (1900, 1949),
    '1950-2000\nGreat Acceleration': (1950, 1999),
    '2000-Present\nPlanetary Emergency': (2000, 2025)
}

EPOCH_NAMES = list(EPOCHS.keys())
EPOCH_RANGES = list(EPOCHS.values())

# Load data
print('Loading IUCN assessment data...')
assessments = pl.read_csv(DUMP_DIR / 'iucn-species-exports' / 'full-export' / 'assessments.csv')
simple_summary = pl.read_csv(DUMP_DIR / 'iucn-species-exports' / 'full-export' / 'simple_summary.csv')

# Join to get taxonomy
extinct_assessments = assessments.filter(
    pl.col('redlistCategory').is_in(['Extinct', 'Extinct in the Wild'])
)

# Get className from simple_summary
taxonomy = simple_summary.select(['internalTaxonId', 'className', 'kingdomName'])
extinct_with_class = extinct_assessments.join(taxonomy, on='internalTaxonId', how='left')

print(f'Total extinct assessments: {len(extinct_with_class)}')

# Filter to valid yearLastSeen
extinct_dated = extinct_with_class.filter(
    pl.col('yearLastSeen').is_not_null() &
    (pl.col('yearLastSeen').cast(str).str.len_chars() == 4)
).with_columns(
    pl.col('yearLastSeen').cast(pl.Int64).alias('year')
)

print(f'Extinct species with valid yearLastSeen: {len(extinct_dated)}')

# Classify by epoch
def get_epoch(year):
    for i, (start, end) in enumerate(EPOCH_RANGES):
        if start <= year <= end:
            return i
    return None

epoch_counts = defaultdict(int)
epoch_by_class = defaultdict(lambda: defaultdict(int))
epoch_by_kingdom = defaultdict(lambda: defaultdict(int))

for row in extinct_dated.iter_rows(named=True):
    year = row['year']
    epoch_idx = get_epoch(year)
    if epoch_idx is not None:
        epoch_name = EPOCH_NAMES[epoch_idx]
        epoch_counts[epoch_name] += 1

        cls = row['className'] or 'Unknown'
        kingdom = row['kingdomName'] or 'Unknown'
        epoch_by_class[epoch_name][cls] += 1
        epoch_by_kingdom[epoch_name][kingdom] += 1

# Print summary
print('\n=== EXTINCTION BY EPOCH ===')
for epoch in EPOCH_NAMES:
    count = epoch_counts[epoch]
    years = EPOCH_RANGES[EPOCH_NAMES.index(epoch)]
    duration = years[1] - years[0] + 1
    rate = count / duration if duration > 0 else 0
    print(f'{epoch.replace(chr(10), " ")}: {count} extinctions ({rate:.2f}/year)')

# ============================================================
# FIGURE 6: Extinctions by Epoch
# ============================================================
print('\nGenerating Figure 6: Extinctions by Epoch...')
fig, ax = plt.subplots(figsize=(12, 7))

counts = [epoch_counts[e] for e in EPOCH_NAMES]
colors = ['#95A186', '#B08E42', '#8C5A24', '#97613B', '#3E2B26']

bars = ax.bar(range(len(EPOCH_NAMES)), counts, color=colors, alpha=0.85,
              edgecolor='#3B3527', linewidth=1.5, width=0.7)

ax.set_xticks(range(len(EPOCH_NAMES)))
ax.set_xticklabels(EPOCH_NAMES, fontsize=10)
ax.set_ylabel('Number of Documented Extinctions', fontsize=12)
ax.set_title('Documented Extinctions by Historical Epoch\nIUCN Red List (species with yearLastSeen data)',
             fontsize=14, fontweight='bold')

# Add value labels
for bar, val in zip(bars, counts):
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 5,
            str(val), ha='center', fontsize=11, color='#3B3527', fontweight='bold')

plt.tight_layout()
plt.savefig(FIGURES_DIR / '06_extinctions_by_epoch.png', dpi=300)
plt.close()
print('  Saved: 06_extinctions_by_epoch.png')

# ============================================================
# FIGURE 7: Extinction Rate by Epoch (per decade)
# ============================================================
print('Generating Figure 7: Extinction Rate by Epoch...')
fig, ax = plt.subplots(figsize=(12, 7))

durations = [(e[1] - e[0] + 1) / 10 for e in EPOCH_RANGES]  # decades
rates = [epoch_counts[e] / d if d > 0 else 0 for e, d in zip(EPOCH_NAMES, durations)]

bars = ax.bar(range(len(EPOCH_NAMES)), rates, color=colors, alpha=0.85,
              edgecolor='#3B3527', linewidth=1.5, width=0.7)

ax.set_xticks(range(len(EPOCH_NAMES)))
ax.set_xticklabels(EPOCH_NAMES, fontsize=10)
ax.set_ylabel('Extinctions per Decade', fontsize=12)
ax.set_title('Extinction Rate by Historical Epoch\n(normalized by epoch duration)',
             fontsize=14, fontweight='bold')

for bar, val in zip(bars, rates):
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.5,
            f'{val:.1f}', ha='center', fontsize=11, color='#3B3527', fontweight='bold')

plt.tight_layout()
plt.savefig(FIGURES_DIR / '07_extinction_rate_by_epoch.png', dpi=300)
plt.close()
print('  Saved: 07_extinction_rate_by_epoch.png')

# ============================================================
# FIGURE 8: Extinction Timeline (Cumulative)
# ============================================================
print('Generating Figure 8: Cumulative Extinction Timeline...')
fig, ax = plt.subplots(figsize=(14, 7))

# Get years and sort
years = sorted(extinct_dated['year'].to_list())
cumulative = list(range(1, len(years) + 1))

ax.fill_between(years, cumulative, alpha=0.3, color='#97613B')
ax.plot(years, cumulative, color='#3E2B26', linewidth=2.5)

# Add epoch markers
epoch_boundaries = [1500, 1900, 1950, 2000]
for boundary in epoch_boundaries:
    ax.axvline(x=boundary, color='#6D6046', linestyle='--', linewidth=1.5, alpha=0.7)

# Annotate epochs
ax.annotate('Colonial\nExpansion', xy=(1700, 50), fontsize=9, color='#6D6046', ha='center')
ax.annotate('Early\nIndustrial', xy=(1925, 150), fontsize=9, color='#6D6046', ha='center')
ax.annotate('Great\nAcceleration', xy=(1975, 400), fontsize=9, color='#6D6046', ha='center')
ax.annotate('Planetary\nEmergency', xy=(2012, 700), fontsize=9, color='#3E2B26', ha='center', fontweight='bold')

ax.set_xlabel('Year Last Seen', fontsize=12)
ax.set_ylabel('Cumulative Extinctions', fontsize=12)
ax.set_title('Cumulative Documented Extinctions Over Time\n(IUCN Red List species with yearLastSeen)',
             fontsize=14, fontweight='bold')
ax.set_xlim(1500, 2025)

plt.tight_layout()
plt.savefig(FIGURES_DIR / '08_cumulative_extinctions.png', dpi=300)
plt.close()
print('  Saved: 08_cumulative_extinctions.png')

# ============================================================
# FIGURE 9: Extinction by Decade (1800-2020)
# ============================================================
print('Generating Figure 9: Extinctions by Decade...')
fig, ax = plt.subplots(figsize=(14, 6))

# Count by decade (1800+)
decade_counts = defaultdict(int)
for year in years:
    if year >= 1800:
        decade = (year // 10) * 10
        decade_counts[decade] += 1

decades = sorted(decade_counts.keys())
counts_by_decade = [decade_counts[d] for d in decades]

# Color gradient by severity
max_count = max(counts_by_decade)
colors_decade = [plt.cm.YlOrBr(c / max_count * 0.8 + 0.2) for c in counts_by_decade]

bars = ax.bar(decades, counts_by_decade, width=8, color=colors_decade,
              edgecolor='#3B3527', linewidth=0.8)

ax.set_xlabel('Decade', fontsize=12)
ax.set_ylabel('Number of Extinctions', fontsize=12)
ax.set_title('Documented Extinctions by Decade (1800-2020)\nIUCN Red List',
             fontsize=14, fontweight='bold')

# Highlight peak decades
peak_idx = counts_by_decade.index(max(counts_by_decade))
ax.annotate(f'Peak: {decades[peak_idx]}s\n({max_count} extinctions)',
            xy=(decades[peak_idx], max_count),
            xytext=(decades[peak_idx] + 30, max_count + 10),
            fontsize=10, color='#3E2B26', fontweight='bold',
            arrowprops=dict(arrowstyle='->', color='#3E2B26', lw=1.5))

plt.tight_layout()
plt.savefig(FIGURES_DIR / '09_extinctions_by_decade.png', dpi=300)
plt.close()
print('  Saved: 09_extinctions_by_decade.png')

# ============================================================
# Summary Statistics
# ============================================================
print('\n=== TEMPORAL ANALYSIS SUMMARY ===')
print(f'Total species with yearLastSeen: {len(extinct_dated)}')
print(f'Earliest documented extinction: {min(years)}')
print(f'Most recent documented extinction: {max(years)}')
print(f'\nPeak decade: {decades[peak_idx]}s with {max_count} extinctions')

# Calculate acceleration
pre_1900 = sum(1 for y in years if y < 1900)
post_1900 = sum(1 for y in years if y >= 1900)
acceleration = post_1900 / pre_1900 if pre_1900 > 0 else float('inf')
print(f'\nPre-1900 extinctions: {pre_1900}')
print(f'Post-1900 extinctions: {post_1900}')
print(f'Acceleration factor: {acceleration:.1f}x')

# Great Acceleration analysis
pre_1950 = sum(1 for y in years if y < 1950)
post_1950 = sum(1 for y in years if y >= 1950)
great_accel = post_1950 / ((2024-1950)/100) / (pre_1950 / ((1950-1500)/100))
print(f'\nGreat Acceleration (post-1950 rate / pre-1950 rate): {great_accel:.1f}x')

print('\n=== Figures 6-9 generated with SME Vintage style ===')
