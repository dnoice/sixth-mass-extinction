<!--
✒ Metadata
    - Title: Episode 1.1 Component Roadmap (SME Edition - v1.0)
    - File Name: ROADMAP.md
    - Relative Path: research-stacks/1.0-establishing-crisis/1.1-extinction-rates/ROADMAP.md
    - Artifact Type: docs
    - Version: 1.0.0
    - Date: 2026-01-07
    - Update: Tuesday, January 07, 2026
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Anthropic - Claude Opus 4.5
    - Signature: ︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!

✒ Description:
    Component roadmap for Episode 1.1 (Baseline vs. Current Extinction Rates).
    Maps the purpose, deliverables, and workflow for each directory in the
    research stack. This is the operational guide for production execution.

✒ Key Features:
    - Feature 1: Directory-by-directory purpose documentation
    - Feature 2: Deliverable specifications for each component
    - Feature 3: Workflow dependencies and sequencing
    - Feature 4: File naming conventions
    - Feature 5: Quality checkpoints

✒ Other Important Information:
    - Blueprint Reference: docs/project-blueprints/research-blueprints/1.0/RESEARCH_BLUEPRINT_MB_SS-1.1_EXTINCTION_RATES.md
    - Target Output: 5,000-7,000 word article, 50+ citations, 5-7 visualizations
    - Core Thesis: Modern extinction rates are 100-1,000x background levels
---------
-->

# Episode 1.1 Component Roadmap

## Baseline vs. Current Extinction Rates

---

**Episode ID:** MB_SS-1.1
**Parent Section:** 1.0 Establishing the Crisis
**Status:** Ready for Production
**Blueprint:** `docs/project-blueprints/research-blueprints/1.0/RESEARCH_BLUEPRINT_MB_SS-1.1_EXTINCTION_RATES.md`

---

## Directory Structure Overview

```
1.1-extinction-rates/
├── ROADMAP.md              ← YOU ARE HERE
├── article/                 # Final written deliverable
│   └── assets/             # Article-specific media
├── bibliography/           # Citation management
├── data/                   # Raw and processed datasets
│   ├── raw/               # Untouched source data
│   ├── processed/         # Cleaned/transformed data
│   └── metadata/          # Data documentation
├── methodology/            # Methods documentation
├── notebooks/              # Jupyter analysis notebooks
├── scripts/                # Standalone Python utilities
├── sources/                # Archived source documents
│   ├── tier-1_authoritative/
│   ├── tier-2_peer-reviewed/
│   ├── tier-3_government/
│   └── tier-4_ngo-verified/
└── visualizations/         # Generated figures
    ├── exports/           # Publication-ready outputs
    ├── figures/           # Working figure files
    └── interactive/       # Interactive viz (HTML/JS)
```

---

## Component Breakdown

### 1. `sources/` — Source Archive

**Purpose:** Archive all source documents used in this episode, organized by trust tier.

| Subdirectory | What Goes Here | Examples |
|--------------|----------------|----------|
| `tier-1_authoritative/` | IPBES, IPCC, FAO, IUCN reports | IPBES_2019_SPM.pdf, IUCN_RedList_Summary.pdf |
| `tier-2_peer-reviewed/` | Journal articles | Ceballos_2015_ScienceAdvances.pdf, Barnosky_2011_Nature.pdf |
| `tier-3_government/` | Government agency reports | NOAA_reports, EPA_data |
| `tier-4_ngo-verified/` | NGO reports, databases | WWF_LPI_2024.pdf, WRI_reports |

**Deliverables:**

- [ ] README.md documenting archive contents
- [ ] 30+ source PDFs organized by tier
- [ ] Citation tracking spreadsheet

**File Naming Convention:** `AuthorLastName_Year_ShortTitle.pdf`

---

### 2. `bibliography/` — Citation Management

**Purpose:** Centralized citation database and formatted reference list.

**Deliverables:**

- [ ] `BIBLIOGRAPHY.md` — Full annotated bibliography
- [ ] `references.bib` — BibTeX format for tools
- [ ] `citation_tracker.csv` — Tracks where each source is used

**Template:** Copy from `_templates/bibliography_template.md`

**Key Sources for 1.1:**

| Citation ID | Author | Year | Title | Tier |
|-------------|--------|------|-------|------|
| S1 | IPBES | 2019 | Global Assessment SPM | 1 |
| S2 | Ceballos et al. | 2015 | Accelerated modern human-induced species losses | 2 |
| S3 | Ceballos et al. | 2017 | Biological annihilation | 2 |
| NEW | Barnosky et al. | 2011 | Has the Earth's sixth mass extinction already arrived? | 2 |
| S12 | Luedtke et al. | 2023 | Ongoing declines for the world's amphibians | 2 |

---

### 3. `data/` — Data Management

**Purpose:** Store, process, and document all datasets used in analysis.

#### `data/raw/`

**What Goes Here:** Untouched source data exactly as downloaded.

**Expected Datasets:**

- [ ] IUCN Red List exports (species assessments)
- [ ] Paleobiology Database extracts (fossil extinction rates)
- [ ] Living Planet Index data (population trends)
- [ ] GBIF occurrence data (if needed)

**Naming Convention:** `source_datatype_YYYYMMDD.csv`
Example: `iucn_extinctions_20260107.csv`

#### `data/processed/`

**What Goes Here:** Cleaned, transformed, analysis-ready data.

**Expected Outputs:**

- [ ] Extinction rates by taxa (E/MSY calculations)
- [ ] Temporal series (rates by time period)
- [ ] Background rate comparisons
- [ ] Merged/joined datasets

**Naming Convention:** `analysis_description_vX.csv`
Example: `extinction_rates_by_taxa_v1.csv`

#### `data/metadata/`

**What Goes Here:** Data documentation and manifests.

**Deliverables:**

- [ ] `MANIFEST.md` — Documents all datasets (template available)
- [ ] Data dictionaries for each dataset
- [ ] Processing logs

---

### 4. `notebooks/` — Analysis Notebooks

**Purpose:** Reproducible Jupyter notebooks for all data analysis.

**Notebook Sequence:**

| # | Notebook | Purpose | Inputs | Outputs |
|---|----------|---------|--------|---------|
| 01 | `01-data-acquisition.ipynb` | Download and archive source data | APIs, downloads | `data/raw/` files |
| 02 | `02-primary-analysis.ipynb` | E/MSY calculations, rate comparisons | `data/raw/` | `data/processed/`, stats |
| 03 | `03-visualization.ipynb` | Generate all figures | `data/processed/` | `visualizations/` |
| 04 | `04-uncertainty-analysis.ipynb` | Confidence intervals, sensitivity | `data/processed/` | Uncertainty tables |
| 05 | `05-temporal-acceleration.ipynb` | Rate changes over time | `data/processed/` | Acceleration curves |
| 06 | `06-replication-validation.ipynb` | Replicate Ceballos et al. methods | Primary sources | Validation report |

**Template:** Copy from `_templates/notebook_template.ipynb`

**Standards:**

- Each notebook is self-contained and runnable
- Clear markdown headers for each section
- All outputs saved to appropriate directories
- Version-controlled with git

---

### 5. `scripts/` — Utility Scripts

**Purpose:** Standalone Python scripts for reusable operations.

**Expected Scripts:**

- [ ] `iucn_api_client.py` — IUCN Red List API wrapper
- [ ] `emsy_calculator.py` — E/MSY calculation functions
- [ ] `data_cleaning.py` — Common data transformations
- [ ] `visualization_utils.py` — Standard figure functions

**Standards:**

- Docstrings following project standards
- Type hints
- Can be imported into notebooks

---

### 6. `methodology/` — Methods Documentation

**Purpose:** Complete methodological documentation for reproducibility.

**Deliverables:**

| Document | Purpose | Template |
|----------|---------|----------|
| `METHODS_1.1_ORIGINAL_ANALYSIS.md` | Full methodology for original calculations | `methods_template.md` |
| `TECHNICAL_SUPPLEMENT_1.1_METHODOLOGY.md` | Extended technical details | `technical_supplement_template.md` |
| `UNCERTAINTY_DOCUMENTATION.md` | Uncertainty analysis framework | `uncertainty_template.md` |

**Key Methodological Questions to Document:**

1. How is E/MSY calculated? (step-by-step)
1. What background rate baseline is used and why?
1. How are current rates derived from IUCN data?
1. What are the uncertainty ranges?
1. How does this compare to Ceballos et al. methodology?

---

### 7. `visualizations/` — Figure Generation

**Purpose:** All visual outputs for the article.

#### `visualizations/figures/`

**What Goes Here:** Working figure files (editable formats).

**Expected Figures (5-7 minimum):**

| # | Figure | Description | Type |
|---|--------|-------------|------|
| 1 | `fig_background_vs_current.png` | Side-by-side rate comparison | Bar chart |
| 2 | `fig_temporal_acceleration.png` | Rates by time period (1500-present) | Line chart |
| 3 | `fig_taxa_comparison.png` | Rate multipliers by taxonomic group | Grouped bars |
| 4 | `fig_extinction_timeline.png` | Documented extinctions over time | Timeline |
| 5 | `fig_uncertainty_ranges.png` | Conservative to realistic estimates | Range plot |
| 6 | `fig_big_five_comparison.png` | Current vs. historical mass extinctions | Comparison |
| 7 | `fig_emsy_explanation.png` | Visual explanation of E/MSY concept | Infographic |

#### `visualizations/exports/`

**What Goes Here:** Publication-ready exports (PNG, SVG, PDF).

**Naming Convention:** `fig_XX_description_vX.png`
**Formats:** PNG (300 DPI), SVG (vector), PDF (print)

#### `visualizations/interactive/`

**What Goes Here:** Interactive visualizations (HTML/JavaScript).

**Potential Interactives:**

- Extinction rate explorer by taxa/time
- Zoomable timeline of documented extinctions

---

### 8. `article/` — Final Deliverable

**Purpose:** The completed article and supporting materials.

**Deliverables:**

| File | Description | Word Count |
|------|-------------|------------|
| `ARTICLE_1.1.md` | Full article (Markdown) | 5,000-7,000 |
| `ARTICLE_1.1_EXECUTIVE_SUMMARY.md` | Standalone summary | 300-500 |
| `GLOSSARY_1.1.md` | Technical terms defined | ~50 terms |

#### `article/assets/`

**What Goes Here:** Final versions of images embedded in article.

**Article Structure (from Blueprint):**

1. **Introduction** (800-1000 words)
1. **Understanding Background Extinction** (1200-1500 words)
1. **Measuring Current Extinction Rates** (1500-1800 words)
1. **The Comparison: 100-1000x Background** (1200-1500 words)
1. **Addressing Uncertainties and Debates** (800-1000 words)
1. **What Makes This a Mass Extinction** (600-800 words)
1. **Implications and Conclusions** (400-600 words)

---

## Production Workflow

### Recommended Sequence

```
PHASE 1: SOURCE COLLECTION
├── 1. Gather sources → sources/tier-X/
├── 2. Create bibliography → bibliography/BIBLIOGRAPHY.md
└── 3. Document sources → sources/README.md

PHASE 2: DATA ACQUISITION
├── 4. Run 01-data-acquisition.ipynb
├── 5. Document datasets → data/metadata/MANIFEST.md
└── 6. Archive raw data → data/raw/

PHASE 3: ANALYSIS
├── 7. Run 02-primary-analysis.ipynb (E/MSY calculations)
├── 8. Run 04-uncertainty-analysis.ipynb
├── 9. Run 05-temporal-acceleration.ipynb
├── 10. Run 06-replication-validation.ipynb
└── 11. Document methodology → methodology/METHODS_1.1_ORIGINAL_ANALYSIS.md

PHASE 4: VISUALIZATION
├── 12. Run 03-visualization.ipynb
├── 13. Export figures → visualizations/exports/
└── 14. Create interactives (if applicable)

PHASE 5: COMPOSITION
├── 15. Write article draft → article/ARTICLE_1.1.md
├── 16. Write executive summary
├── 17. Create glossary
├── 18. Quality control pass
└── 19. Final review and sign-off
```

---

## Quality Checkpoints

### Before Moving to Next Phase

**After Phase 1 (Sources):**

- [ ] 30+ sources archived and organized
- [ ] All Tier-1 sources obtained
- [ ] Bibliography template populated
- [ ] Sources README documents archive

**After Phase 2 (Data):**

- [ ] IUCN data successfully retrieved
- [ ] Paleobiology data obtained
- [ ] All datasets documented in MANIFEST.md
- [ ] Data quality checked

**After Phase 3 (Analysis):**

- [ ] E/MSY calculations complete
- [ ] Background rates established
- [ ] Current rates calculated
- [ ] Uncertainty ranges quantified
- [ ] Methodology fully documented

**After Phase 4 (Visualization):**

- [ ] 5-7 figures completed
- [ ] All figures exported at 300 DPI
- [ ] Figures captioned and labeled
- [ ] Color palette consistent (use SME palette)

**After Phase 5 (Composition):**

- [ ] Article 5,000-7,000 words
- [ ] Every claim cited
- [ ] All figures integrated
- [ ] Glossary complete
- [ ] Executive summary written
- [ ] Quality control checklist passed

---

## Key Metrics for Episode 1.1

| Metric | Target | Source |
|--------|--------|--------|
| Background Extinction Rate | 0.1-2 E/MSY | Ceballos et al. (2015), Pimm et al. (2014) |
| Current Rate Multiplier | 100-1000x background | IPBES (2019), Ceballos et al. (2015) |
| Vertebrate Extinctions (1900-2014) | ~477 species | Ceballos et al. (2015) |
| Species at Risk | 1 million+ | IPBES (2019) |
| Mass Extinction Threshold | 75% species loss | Barnosky et al. (2011) |

---

## Integration Points

**This Episode Establishes:**

- Empirical foundation for extinction crisis
- E/MSY methodology for later episodes
- Rate baseline for comparisons

**Feeds Into:**

- Episode 1.2 (Magnitude of Risk) — uses rate calculations
- Episode 1.3 (Geographic Hotspots) — uses geographic data
- Episode 1.4 (Previous Extinctions) — uses comparison framework
- Section 2.0 (Primary Drivers) — explains WHY rates are elevated

---

## Ready for Production

This roadmap is complete. The 1.1 research stack is ready for content generation.

**First Step:** Begin with Phase 1 — Source Collection.

**Ground Rules:** [Awaiting user specification before proceeding]

---

> ︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!
