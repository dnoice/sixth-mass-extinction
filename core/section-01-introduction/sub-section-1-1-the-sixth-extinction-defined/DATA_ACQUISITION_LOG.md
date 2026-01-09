<!--
✒ Metadata
    - Title: Data Acquisition Log - Subsection 1.1 (SME Edition - v1.0)
    - File Name: DATA_ACQUISITION_LOG.md
    - Relative Path: core/section-01-introduction/sub-section-1-1-the-sixth-extinction-defined/DATA_ACQUISITION_LOG.md
    - Artifact Type: log
    - Version: 1.0.0
    - Date: 2026-01-09
    - Update: Friday, January 09, 2026
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Google - Gemini 2.0 Flash
    - Signature: ︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!

✒ Description:
    A living document tracking the identification, acquisition, validation, and
    processing of raw data sources required for Subsection 1.1.
    Adheres strictly to Hard Rule 3 (No Simulated Data).

✒ Key Features:
    - Feature 1: Status tracking (Pending -> Acquired -> Validated -> Processed)
    - Feature 2: Source of Truth URLs for all external data
    - Feature 3: Hash/Checksum verification (where applicable)
    - Feature 4: Obstacle and Blocker tracking

✒ Usage Instructions:
    Update this log immediately upon changing the state of any dataset.
    Do not proceed to analysis until all required 'Foundation' datasets are marked 'Validated'.

✒ Other Important Information:
    - Dependencies: core/grab-bag/
    - Related documents: INTRODUCTION_1.1_BLUEPRINT.md
---------
-->

# 📋 Data Acquisition Log: Subsection 1.1

## 1. Target Datasets (Foundation)

| ID | Dataset Name | Source / Authority | Target Location | Status | Last Updated |
| ---- | -------------- | -------------------- | ----------------- | -------- | -------------- |
| **DS-1.1-001** | IUCN Red List Summary Statistics (v2024-2) | IUCN Red List Website | `core/grab-bag/raw/datasets/iucn_table_3_species_by_kingdom_class.csv` | 🟢 Validated | 2026-01-09 |
| **DS-1.1-002** | Ceballos et al. (2015) Supp. Tables (S1, S2) | Science Advances (DOI: 10.1126/sciadv.1400253) | `core/grab-bag/raw/datasets/ceballos_2015_transcribed.csv` | 🟢 Validated | 2026-01-09 |
| **DS-1.1-003** | Barnosky et al. (2011) Background Rates | Nature (DOI: 10.1038/nature09678) | `core/grab-bag/raw/documents/41586_2011_BFnature09678_MOESM2_ESM.ppt` | 🟡 Acquired (PPT) | 2026-01-09 |

## 2. Acquisition & Processing Log

### 2026-01-09

- **Action:** Initialized log.

- **Research:** Identified primary URLs for all three targets.
  - **IUCN:** `https://www.iucnredlist.org/resources/summary-statistics` (Specifically "Table 7")
  - **Ceballos (2015):** `https://www.science.org/doi/suppl/10.1126/sciadv.1400253`
  - **Barnosky (2011):** `https://www.nature.com/articles/nature09678` (Supplementary Information)
- **Blocker:** Direct file downloads (zip/pdf) require navigation.
- **Next Step:** See "Manual Acquisition Instructions" below.

## 3. Manual Acquisition Instructions (Blockers)

*Use these steps when automated fetching fails due to 403/Login walls.*

### For DS-1.1-001: IUCN Red List Summary Stats

1. **Navigate:** Go to <https://www.iucnredlist.org/resources/summary-statistics>
1. **Locate:** Find the link for "Summary Statistics Tables" (usually a large ZIP download).
1. **Download:** Save the ZIP file to your local machine.
1. **Extract:** Open the ZIP and find **Table 1** (Threatened Species by Group) and **Table 2** (Changes in Numbers).
1. **Rename & Move:**
    - Rename Table 1 to `iucn_2024_2_table_1.csv`
    - Rename Table 2 to `iucn_2024_2_table_2.csv`
    - Move both files to: `core/grab-bag/raw/`
1. **Update Log:** Change status of DS-1.1-001 to 🟢 Validated.

### For DS-1.1-003: Barnosky et al. (2011) Supplementary Info

1. **Navigate:** Go to <https://www.nature.com/articles/nature09678>
1. **Locate:** Click on "Supplementary Information" (right sidebar or bottom).
1. **Download:** Download the `Supplementary Information` (often a PDF or Excel).
1. **Move:** Place the file in `core/grab-bag/raw/` as `barnosky_2011_SI.pdf`.
1. **Update Log:** Change status of DS-1.1-003 to 🟢 Validated.

## 4. Validation Rules (Pre-Analysis)

Before any notebook execution, the following must be true:

1. [ ] **DS-1.1-001** must contain recent counts for Mammals, Birds, Reptiles, Amphibians, and Fishes.
1. [ ] **DS-1.1-002** must match the printed values in Ceballos (2015) Table S2.
1. [ ] **DS-1.1-003** must explicitly state the 2 E/MSY (conservative) vs. High E/MSY background rate values.

---
> *Status Key:* 🔴 Pending | 🟡 In Progress | 🟢 Validated | 🔵 Archived
