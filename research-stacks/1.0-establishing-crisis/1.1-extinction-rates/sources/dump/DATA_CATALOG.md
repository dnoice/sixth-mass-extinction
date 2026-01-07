<!--
✒ Metadata
    - Title: Data Catalog (MB_SS-1.1 Source Archive - v1.0)
    - File Name: DATA_CATALOG.md
    - Relative Path: research-stacks/1.0-establishing-crisis/1.1-extinction-rates/sources/dump/DATA_CATALOG.md
    - Artifact Type: docs
    - Version: 1.0.0
    - Date: 2026-01-07
    - Update: Tuesday, January 07, 2026
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Anthropic - Claude Opus 4.5
    - Signature: Aim Twice, Shoot Once!

✒ Description:
    Comprehensive catalog of all source materials in the dump directory.
    Documents provenance, structure, and cross-contamination opportunities
    for multi-system analysis across SME episodes.

✒ Key Features:
    - Complete inventory with file sizes and record counts
    - Data structure documentation for each dataset
    - Cross-contamination matrix for novel analyses
    - Episode mapping for source reuse
    - Acquisition provenance tracking
---------
-->

# Data Catalog: Episode 1.1 Source Archive

**Location:** `research-stacks/1.0-establishing-crisis/1.1-extinction-rates/sources/dump/`
**Total Size:** ~1.1 GB
**Last Updated:** 2026-01-07

---

## Directory Structure

```
dump/
├── README.md                      # Original paper documentation
├── DATA_CATALOG.md                # THIS FILE
│
├── papers/
│   ├── tier-1/                    # Authoritative sources (IPBES, WWF)
│   ├── tier-2/                    # Peer-reviewed papers
│   └── meta/                      # SHA256 verification files
│
├── iucn-red-list-summary/         # IUCN summary statistics (PDFs)
│   └── Table_7_2007-2024/         # 18 years of category change data
│
├── iucn-species-exports/          # IUCN Red List data exports
│   ├── cr-decreasing-2020-2025/   # Critically Endangered filter
│   ├── cr-decreasing-root/        # Duplicate of above (convenience)
│   └── full-export/               # Complete IUCN database (~900MB)
│
└── rli-timeseries/                # Red List Index time series
    ├── global/                    # Ecosystem-specific RLI trends
    └── regional-sdg/              # SDG regional breakdowns
```

---

## 1. Papers (`papers/`)

### Tier 1: Authoritative Sources

| File | Size | Source | DOI |
|------|------|--------|-----|
| `ipbes_2019_spm.pdf` | 15 MB | IPBES Secretariat | 10.5281/zenodo.3553579 |
| `lpr_2022_full_report smaller.pdf` | 9.9 MB | WWF International | — |

**Use Cases:**
- IPBES: "1 million species at risk" claim, 100-1000x rate multiplier
- LPR: 69% vertebrate population decline, Living Planet Index methodology

### Tier 2: Peer-Reviewed Papers

| File | Size | Citation | DOI |
|------|------|----------|-----|
| `barnosky_2011_sixth_extinction.pdf` | 604 KB | Barnosky et al. 2011, Nature | 10.1038/nature09678 |
| `ceballos_2015_main_paper.pdf` | 214 KB | Ceballos et al. 2015, Sci Adv | 10.1126/sciadv.1400253 |
| `ceballos_2017_biological_annihilation.pdf` | 2.0 MB | Ceballos et al. 2017, PNAS | 10.1073/pnas.1704949114 |
| `ceballos_2023_genus_extinction.pdf` | 3.5 MB | Ceballos & Ehrlich 2023, PNAS | 10.1073/pnas.2306987120 |
| `ceballos_2023_genus_extinction_summary.pdf` | 711 KB | Summary/Press release | — |
| `devos_2015_background_rate.pdf` | 1.3 MB | De Vos et al. 2015, Cons Biol | 10.1111/cobi.12380 |
| `pimm_et_al_2014.pdf` | 3.9 MB | Pimm et al. 2014, Science | 10.1126/science.1246752 |

**Key Contributions:**
- **Ceballos 2015**: E/MSY methodology, 100x rate calculation
- **Ceballos 2017**: Population-level "biological annihilation"
- **Ceballos 2023**: Genus-level extinction (35x acceleration)
- **Barnosky 2011**: Mass extinction criteria (75% threshold)
- **De Vos 2015**: Background rate refinement (0.1 E/MSY)
- **Pimm 2014**: Comprehensive E/MSY review

### Meta Files (`papers/meta/`)

SHA256 checksums for provenance verification:
- `barnosky_2011_sixth_extinction.pdf.meta`
- `ceballos_2015_main_paper.pdf.meta`
- `ceballos_2017_biological_annihilation.pdf.meta`
- `ipbes_2019_spm.pdf.meta`

---

## 2. IUCN Red List Summary Tables (`iucn-red-list-summary/`)

### Current Release (2025-2)

| File | Contents |
|------|----------|
| `2025-2_RL_Table1a.pdf` | Described vs Assessed species |
| `2025-2_RL_Table1b.pdf` | Threatened species 1996-2025 |
| `2025-2_RL_Table2.pdf` | Category changes over time |
| `2025-2_RL_Table7.pdf` | **Category changes with reasons** |
| `2025-2_RL_Table8a-d.pdf` | Endemic species by country |
| `Table 3-6*.pdf` | Taxonomic and geographic breakdowns |

### Historical Table 7 Archive (`Table_7_2007-2024/`)

**18 years of extinction tracking:**

| Year | File |
|------|------|
| 2007 | `2007RL_Stats_Table_7.pdf` |
| 2008 | `2008RL_Stats_Table_7.pdf` |
| 2009 | `2009RL_Stats_Table_7.pdf` |
| 2010 | `2010_4RL_Stats_Table_7.pdf` |
| 2011 | `2011_2_RL_Stats_Table7.pdf` |
| 2012 | `2012_2_RL_Stats_Table_7.pdf` |
| 2013 | `2013_2_RL_Stats_Table7_edited.pdf` |
| 2014 | `2014_3_RL_Stats_Table_7.pdf` |
| 2015 | `2015_4_RL_Stats_Table_7.pdf` |
| 2016 | `2016_3_RL_Stats_Table_7.pdf` |
| 2017 | `2017_3_RL_Stats_Table_7.pdf` |
| 2018 | `2018_2_RL_Stats_Table_7_new.pdf` |
| 2019 | `2019_3_RL_Stats_Table_7.pdf` |
| 2020 | `2020-3_RL_Stats_Table7.pdf` |
| 2021 | `2021-3_RL_Stats_Table_7.pdf` |
| 2022 | `2022-2_RL_Stats_Table_7.pdf` |
| 2023 | `2023-1_RL_Stats_Table_7.pdf` |
| 2024 | `2024-1_RL_Table_7_corrected_20240916.pdf`, `2024-2_RL_Table_7.pdf` |

**Critical Use:** Track species moving TO Extinct (EX) or Extinct in Wild (EW) status.

### Documentation

| File | Purpose |
|------|---------|
| `iucn-red-list-summary.md` | Comprehensive interpretation guide |

---

## 3. IUCN Species Data Exports (`iucn-species-exports/`)

### Full Database Export (`full-export/`)

**Size:** ~900 MB total
**Filter:** All assessed species

| File | Size | Records | Description |
|------|------|---------|-------------|
| `simple_summary.csv` | 29 MB | ~160,000 | Basic assessment data |
| `assessments.csv` | 391 MB | ~160,000 | Full assessment text |
| `assessments_with_html.csv` | 434 MB | ~160,000 | With HTML formatting |
| `taxonomy.csv` | 35 MB | ~160,000 | Taxonomic hierarchy |
| `taxonomy_with_html.csv` | 37 MB | ~160,000 | With HTML formatting |
| `common_names.csv` | 11 MB | varies | Vernacular names |
| `synonyms.csv` | 14 MB | varies | Scientific name synonyms |

**Key Fields:**
- `assessmentId`: Unique assessment identifier
- `internalTaxonId`: Species identifier (join key)
- `redlistCategory`: CR, EN, VU, NT, LC, DD, EX, EW
- `redlistCriteria`: IUCN criteria (e.g., A2cd+4cd)
- `populationTrend`: Decreasing, Stable, Increasing, Unknown
- `possiblyExtinct`: Boolean flag for CR(PE) species

### CR-Decreasing Filter (`cr-decreasing-2020-2025/`)

**Filter:** Critically Endangered + Decreasing + Animalia + 2020-2025
**Records:** ~1,232 species

Same file structure as full export but filtered to highest-risk cohort.

### Convenience Copy (`cr-decreasing-root/`)

Duplicate of CR-decreasing data at more accessible location.

---

## 4. Red List Index Time Series (`rli-timeseries/`)

### Global Ecosystem Trends (`global/`)

| File | Ecosystem/Category | Years |
|------|-------------------|-------|
| `global_aggregated.csv` | All species | 1993-2020+ |
| `global_aggregated_forest.csv` | Forest-dependent | 1995-2020 |
| `global_aggregated_freshwater.csv` | Freshwater | 1993-2020 |
| `global_aggregated_marine.csv` | Marine | 1993-2020 |
| `global_aggregated_terrestrial.csv` | Terrestrial | 1993-2020 |
| `global_aggregated_wetland.csv` | Wetland | 1993-2020 |
| `global_aggregated_fisheries.csv` | Commercial fisheries | 1993-2020 |
| `global_aggregated_IAS.csv` | Invasive Alien Species impact | 1993-2020 |
| `global_aggregated_pollution.csv` | Pollution-affected | 1993-2020 |
| `global_aggregated_migratory.csv` | Migratory species | 1993-2020 |
| `global_aggregated_medicine.csv` | Medicinal use | 1993-2020 |
| `global_aggregated_utilisation.csv` | Harvested species | 1993-2020 |
| `global_aggregated_internationallytraded.csv` | CITES-traded | 1993-2020 |

**Data Structure:**
```
country,group,year,rli,qn05,qn95,n_sp,n_gen_changes
"",aggregated,1995,0.7397,0.7370,0.7432,,
```

- `rli`: Red List Index (1.0 = all LC, 0.0 = all EX)
- `qn05`, `qn95`: 5th/95th percentile confidence bounds
- Decreasing RLI = deteriorating conservation status

### Regional SDG Breakdowns (`regional-sdg/`)

**SDG Regions (7 files):**
- Central Asia + Southern Asia
- Eastern Asia + South-eastern Asia
- Latin America and Caribbean
- Northern America + Europe
- Oceania
- Sub-Saharan Africa
- Western Asia + Northern Africa

**SDG Subregions (10 files):**
- Australia/New Zealand, Central Asia, Eastern Asia, Europe
- Northern Africa, Northern America, Oceania (excl. Aus/NZ)
- South-eastern Asia, Southern Asia, Western Asia

**Development Categories (3 files):**
- LDC (Least Developed Countries)
- LLDC (Landlocked Developing Countries)
- SIDS (Small Island Developing States)

---

## 5. Cross-Contamination Opportunities

### Episode Connections

| Dataset | Primary Episode | Cross-Contamination Potential |
|---------|-----------------|-------------------------------|
| Ceballos papers | 1.1 (Extinction Rates) | 1.4 (Mass Extinction), 7.1 (Tipping Points) |
| IUCN species data | 1.1 | 2.x (Habitat), 3.x (Drivers), 4.x (Climate) |
| RLI time series | 1.1 | 5.x (Oceans), 6.x (Food Systems) |
| Table 7 archive | 1.1 | 9.1 (Trajectories), 10.1 (Synthesis) |
| LPR 2022 | 1.1 | 1.2 (Population Decline), 6.2 (Wildlife Trade) |

### Novel Analysis Opportunities

| Analysis | Datasets to Combine | Hypothesis |
|----------|---------------------|------------|
| **Taxa-specific acceleration** | Table 7 series + taxonomy.csv | Which taxa show steepest extinction acceleration? |
| **Geographic hotspots** | Regional RLI + IUCN country data | Where is RLI declining fastest? |
| **Threat-response lag** | RLI ecosystem CSVs + external climate data | Do ecosystem RLIs respond to climate with lag? |
| **ENSO extinction pulses** | Table 7 + El Nino dates | Do extinctions cluster after El Nino events? |
| **Trade-driven decline** | `internationallytraded.csv` + CITES data | Quantify trade impact on RLI |
| **Freshwater vs marine** | Ecosystem RLIs | Compare decline rates by realm |

### Proven Cross-Contamination (Completed)

| Notebook | Datasets Combined | Finding |
|----------|-------------------|---------|
| `elnino_lag_analysis.ipynb` | Amazon PRODES + Coral DHW | 14-month teleconnection lag (r=0.44, p<0.001) |

---

## 6. Data Quality Notes

### IUCN Data Caveats

1. **Assessment bias**: Well-studied taxa overrepresented
2. **Temporal gaps**: Not all species reassessed annually
3. **DD uncertainty**: Data Deficient species create bounds
4. **HTML formatting**: Some CSV fields contain HTML tags

### RLI Interpretation

1. **Genuine vs non-genuine changes**: Table 7 distinguishes these
2. **Taxonomic revisions**: Can cause non-genuine category shifts
3. **New assessments**: Expanding Red List affects baselines

### File Encoding

All CSVs are **UTF-8 encoded**. Import with:
- Excel: Data > From Text/CSV > File Origin: 65001 (UTF-8)
- Python: `pd.read_csv(file, encoding='utf-8')`
- Polars: `pl.read_csv(file)` (auto-detects)

---

## 7. Attribution Requirements

### IUCN Red List

```
IUCN 2025. The IUCN Red List of Threatened Species. Version 2025-2.
https://www.iucnredlist.org. Downloaded on [DATE].
```

### Papers

See individual DOIs in Section 1 for citation requirements.

---

## 8. Maintenance Log

| Date | Action | Notes |
|------|--------|-------|
| 2025-12-01 | Initial collection | Papers acquired |
| 2025-12-01 | IUCN exports | CR-decreasing filter applied |
| 2026-01-07 | Directory reorganization | Created subdirectory structure |
| 2026-01-07 | Catalog created | This document |

---

> **Aim Twice, Shoot Once!**
