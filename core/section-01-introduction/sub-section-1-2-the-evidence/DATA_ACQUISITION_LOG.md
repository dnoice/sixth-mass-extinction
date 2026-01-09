<!--
✒ Metadata
    - Title: Data Acquisition Log - Subsection 1.2 (SME Edition - v1.0)
    - File Name: DATA_ACQUISITION_LOG.md
    - Relative Path: core/section-01-introduction/sub-section-1-2-the-evidence/DATA_ACQUISITION_LOG.md
    - Artifact Type: log
    - Version: 1.0.0
    - Date: 2026-01-09
    - Update: Friday, January 09, 2026
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Google - Gemini 2.0 Flash
    - Signature: ︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!

✒ Description:
    A living document tracking the identification, acquisition, validation, and
    processing of raw data sources required for Subsection 1.2.
    Adheres strictly to Hard Rule 3 (No Simulated Data).

✒ Key Features:
    - Feature 1: Status tracking (Pending -> Acquired -> Validated -> Processed)
    - Feature 2: Source of Truth URLs for all external data
    - Feature 3: Obstacle and Blocker tracking

✒ Usage Instructions:
    Update this log immediately upon changing the state of any dataset.
---------
-->

# 📋 Data Acquisition Log: Subsection 1.2

## 1. Target Datasets (Foundation)

| ID | Dataset Name | Source / Authority | Target Location | Status | Last Updated |
| ---- | -------------- | -------------------- | ----------------- | -------- | -------------- |
| **DS-1.2-001** | IUCN Red List Summary (Table 1) | IUCN (Grab-Bag) | `core/grab-bag/raw/datasets/iucn_table_1...` | 🟡 In Progress | 2026-01-09 |
| **DS-1.2-002** | Living Planet Index (LPI) 2022/24 | WWF / ZSL | `core/grab-bag/raw/datasets/lpi_summary.csv` | 🔴 Pending | 2026-01-09 |
| **DS-1.2-003** | IPBES 1 Million Species Math | IPBES Global Assessment | `core/grab-bag/raw/documents/ipbes_summary.pdf` | 🔴 Pending | 2026-01-09 |

## 2. Acquisition & Processing Log

### 2026-01-09

- **Action:** Initialized log.

- **Next Step:** Find direct download or summary text for LPI 69% decline.

## 3. Manual Acquisition Instructions (Blockers)

### For DS-1.2-002: Living Planet Index

1. **Navigate:** <https://livingplanetindex.org/data_portal>
1. **Locate:** Download the "LPI Public Data" or the summary table from the 2022/2024 Report.
1. **Move:** Place in `core/grab-bag/raw/datasets/` as `lpi_data.csv`.

---
> *Status Key:* 🔴 Pending | 🟡 In Progress | 🟢 Validated | 🔵 Archived
