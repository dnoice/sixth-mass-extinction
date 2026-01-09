<!--
✒ Metadata
    - Title: Subsection 1.2 Blueprint: The Evidence (SME Edition - v1.0)
    - File Name: INTRODUCTION_1.2_BLUEPRINT.md
    - Relative Path: core/section-01-introduction/sub-section-1-2-the-evidence/INTRODUCTION_1.2_BLUEPRINT.md
    - Artifact Type: docs
    - Version: 1.0.0
    - Date: 2026-01-09
    - Update: Friday, January 09, 2026
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Google - Gemini 2.0 Flash
    - Signature: ︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!

✒ Description:
    The authoritative scope and roadmap for Subsection 1.2. This sub-section
    moves from the definition of the crisis (1.1) to the specific "smoking gun"
    evidence. It focuses on the global patterns found in the IUCN Red List,
    the WWF Living Planet Index, and the IPBES Global Assessment.

✒ Key Features:
    - Feature 1: The "Threatened" spectrum (CR, EN, VU classifications)
    - Feature 2: Analysis of Population Trends (The Living Planet Index)
    - Feature 3: Taxonomic gaps in the evidence (The "Unknown" biosphere)
    - Feature 4: Geographic hotspots of loss
    - Feature 5: Validation of the IPBES "1 Million Species" claim

✒ Usage Instructions:
    This document governs the development of Subsection 1.2.
    All outputs in the 'outputs/' directory must align with the objectives defined here.

✒ Other Important Information:
    - Dependencies: core/grab-bag/ (IUCN, WWF, IPBES data)
    - Related documents: MASTER_BLUEPRINT.md, INTRODUCTION_1.1_BLUEPRINT.md
---------
-->

# ⚖️ Subsection 1.2 Blueprint: The Evidence

> **Objective:** To present the irrefutable "Body of Evidence" supporting the Sixth Mass Extinction, moving from raw extinction counts to the broader spectrum of decline and population collapse.

---

## 1. Scope & Boundaries

### In Scope
- **The Red List Spectrum:** Explaining CR, EN, VU, NT, LC categories.
- **Population Decline:** Analysis of the Living Planet Index (LPI) metrics.
- **Biogeographic Patterns:** Identifying where the most intense losses are occurring.
- **Comparison:** Contrasting documented extinctions with the vast number of "Threatened" species.

### Out of Scope
- **Specific Drivers:** (Reserved for Section 4.0).
- **Physical Science:** (Reserved for Section 3.0).
- **Extinction Rates:** (Calculated in 1.1, used as a reference point here).

---

## 2. Deliverables (Outputs)

All final artifacts are stored in `outputs/`.

### 📄 Documentation
- [ ] **ARTICLE_1.2_THE_RED_LIST_REALITY.md**: The narrative deep-dive.
- [ ] **TECHNICAL_SUPPLEMENT_1.2_METHODOLOGY.md**: Methodology for LPI and Red List parsing.
- [ ] **METHODS_1.2_ORIGINAL_ANALYSIS.md**: Documentation of exploratory pattern matching.
- [ ] **UNCERTAINTY_DOCUMENTATION.md**: Gaps in global monitoring coverage.
- [ ] **SOURCES_AND_CITATIONS.md**: Bibliography.

### 📓 Notebooks (Reproducible Science)
*Located in `outputs/notebooks/`*

**Validation (Reproducing Established Science):**
1. [ ] `1.2_validate_red_list_summary.ipynb`: Aggregating threatened counts by taxonomic group.
2. [ ] `1.2_validate_living_planet_index.ipynb`: Reproducing the "69% decline" statistic.
3. [ ] `1.2_validate_ipbes_one_million_claim.ipynb`: Checking the math on the 1-million-species-at-risk projection.

**Exploration (Novel Insights):**
1. [ ] `1.2_explore_threat_overlap.ipynb`: Correlation between group size and threat level.
2. [ ] `1.2_explore_geographic_bias.ipynb`: Mapping the density of monitoring vs. the intensity of threat.
3. [ ] `1.2_explore_category_velocity.ipynb`: Analyzing the speed at which species move from 'Vulnerable' to 'Critically Endangered'.

---

## 3. Data Strategy

- **Raw Data Source:** `core/grab-bag/raw/datasets/iucn_table_1...`, `lpi_2022_summary.csv`.
- **Local Data:** `outputs/notebooks/data/` (Subsection-specific subsets).

---

> *Status:* 🟡 In Progress | *Last Updated:* Friday, January 09, 2026
