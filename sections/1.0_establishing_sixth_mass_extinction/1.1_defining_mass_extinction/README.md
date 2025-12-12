<!--
================================================================================
Title:              Section 1.1 README
File Name:          README.md
Relative Path:      sections/1.0.../1.1.../README.md
Artifact Type:      Documentation
Version:            0.1 (Template)
Date:               2025-12-12
Author:             Dennis 'dnoice' Smaltz
Signature:          ︻デ═—··· 🎯 = Aim Twice, Shoot Once!
================================================================================
-->

# Section 1.1: Defining Mass Extinction

## Overview

This section establishes the scientific foundation for the Sixth Mass Extinction series by:

1. Defining what constitutes a "mass extinction" event
2. Calculating current extinction rates
3. Comparing current rates to historical mass extinctions (the "Big Five")
4. Addressing the quantitative thresholds for declaring a sixth mass extinction

## Directory Structure

```
1.1_defining_mass_extinction/
├── README.md                           # This file
├── article/                            # Final article and summaries
│   ├── article_1.1_defining_mass_extinction.md
│   ├── article_summary.md
│   └── key_findings.md
├── notebooks/                          # Jupyter notebooks (minimum 3)
│   ├── 01_data_acquisition.ipynb       # Data sourcing and validation
│   ├── 02_analysis_core.ipynb          # Rate calculations and comparisons
│   └── 03_visualization.ipynb          # Figure generation
├── figures/                            # Publication-quality figures
│   ├── fig_1.1_01_extinction_rate_comparison.png
│   ├── fig_1.1_01_extinction_rate_comparison.svg
│   ├── fig_1.1_02_mass_extinction_timeline.png
│   ├── fig_1.1_02_mass_extinction_timeline.svg
│   ├── fig_1.1_03_rate_uncertainty_comparison.png
│   ├── fig_1.1_03_rate_uncertainty_comparison.svg
│   └── FIGURE_MANIFEST.json
├── data/
│   ├── raw/                            # Original source data
│   │   ├── iucn_summary_2025-2.json
│   │   ├── big_five_mass_extinctions.csv
│   │   ├── modern_extinctions_since_1500.json
│   │   ├── background_extinction_rates.csv
│   │   └── DATA_MANIFEST.json
│   ├── processed/                      # Cleaned data
│   └── derived/                        # Novel datasets
│       ├── extinction_rate_calculations.csv
│       ├── rate_comparison_big_five.csv
│       ├── sensitivity_analysis.csv
│       └── key_findings.json
├── uncertainty_documentation.md        # Uncertainty quantification
├── methods_original_analysis.md        # Detailed methodology
└── technical_supplement.md             # Extended technical details
```

## Key Questions Addressed

1. **What quantitative thresholds define a mass extinction?**
   - Species loss >75% in geologically short time (<2 MY)
   - Extinction rate significantly above background

2. **What is the background extinction rate?**
   - Approximately 0.1-2.0 E/MSY (extinctions per million species-years)
   - Commonly cited as ~1 E/MSY for vertebrates

3. **How does the current rate compare to the Big Five?**
   - Current rate: ~10-1,000× background (depending on methodology)
   - Comparable to early stages of major mass extinctions

4. **Are we in a sixth mass extinction?**
   - Quantitative analysis suggests we are in the early stages
   - Rate comparison supports the designation

## Data Sources

| Source ID | Name | Used For |
|-----------|------|----------|
| DS-PA-001 | IUCN Red List v2025-2 | Current extinction counts, threat status |
| DS-PA-002 | IUCN Guidelines v16 | Methodology understanding |
| DS-PR-001 | Barnosky et al. 2011 | Big Five comparisons, rate calculations |
| DS-PR-002 | Ceballos et al. 2015 | Modern extinction rate methodology |

## Reproduction Instructions

### 1. Environment Setup

```bash
cd sections/1.0_establishing_sixth_mass_extinction/1.1_defining_mass_extinction/

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r ../../../requirements.txt
```

### 2. Run Notebooks in Order

```bash
cd notebooks/

# Step 1: Acquire data
jupyter notebook 01_data_acquisition.ipynb

# Step 2: Run analysis
jupyter notebook 02_analysis_core.ipynb

# Step 3: Generate figures
jupyter notebook 03_visualization.ipynb
```

### 3. Expected Outputs

After running all notebooks:
- `data/raw/`: 4 data files + manifest
- `data/derived/`: 4 derived datasets
- `figures/`: 3 figures (PNG + SVG) + manifest

## Status

| Deliverable | Status |
|-------------|--------|
| Article | ⬜ Not Started |
| Notebook 01 | ⬜ Template |
| Notebook 02 | ⬜ Template |
| Notebook 03 | ⬜ Template |
| Figures | ⬜ Template |
| Uncertainty Doc | ⬜ Template |
| Methods Doc | ⬜ Template |
| Technical Supplement | ⬜ Template |

## Key Findings (Preview)

- Current vertebrate extinction rate: **~100× background** (conservative estimate)
- Uncertainty range: **10-1,000× background** depending on methodology
- This rate is comparable to the early stages of previous mass extinctions
- The "sixth mass extinction" designation is scientifically supported

## References

1. Barnosky, A.D., et al. (2011). Has the Earth's sixth mass extinction already arrived? *Nature*, 471(7336), 51-57.

2. Ceballos, G., et al. (2015). Accelerated modern human-induced species losses: Entering the sixth mass extinction. *Science Advances*, 1(5), e1400253.

3. IUCN (2025). The IUCN Red List of Threatened Species. Version 2025-2.

4. De Vos, J.M., et al. (2015). Estimating the normal background rate of species extinction. *Conservation Biology*, 29(2), 452-462.

---

*︻デ═—··· 🎯 = Aim Twice, Shoot Once!*
