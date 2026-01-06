<!--
✒ Metadata
    - Title: Bibliography Template (SME Edition - v1.0)
    - File Name: bibliography_template.md
    - Relative Path: research-stacks/_templates/bibliography_template.md
    - Artifact Type: docs
    - Version: 1.0.0
    - Date: 2026-01-05
    - Update: Sunday, January 05, 2026
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Anthropic - Claude Opus 4.5
    - Signature: ︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!

✒ Description:
    Template for episode bibliography files providing comprehensive source
    documentation with tiered classification, annotations, and usage tracking.

✒ Key Features:
    - Feature 1: Four-tier source classification system
    - Feature 2: Annotated bibliography entries
    - Feature 3: Citation usage tracking
    - Feature 4: DOI and URL preservation
    - Feature 5: Access date documentation
    - Feature 6: Source reliability assessment
    - Feature 7: Cross-reference to article sections
    - Feature 8: BibTeX export compatibility

✒ Usage Instructions:
    Copy to episode bibliography/ directory:
        cp _templates/bibliography_template.md X.X-episode/bibliography/BIBLIOGRAPHY.md

✒ Other Important Information:
    - Dependencies: None (documentation only)
    - Citation style: APA 7th edition (adapted)
    - Source documents: Archived in ../sources/
---------
-->

# Bibliography

## Episode {X.X}: {Episode Title}

> **Total Sources:** {N}
>
> **Tier Distribution:** Tier 1: {N} | Tier 2: {N} | Tier 3: {N} | Tier 4: {N}
>
> **Last Updated:** {YYYY-MM-DD}

---

## Table of Contents

1. [Citation Guide](#citation-guide)
2. [Tier 1: Authoritative International Assessments](#tier-1-authoritative-international-assessments)
3. [Tier 2: Peer-Reviewed Literature](#tier-2-peer-reviewed-literature)
4. [Tier 3: Government and Institutional Sources](#tier-3-government-and-institutional-sources)
5. [Tier 4: Verified NGO and Monitoring Data](#tier-4-verified-ngo-and-monitoring-data)
6. [Datasets](#datasets)
7. [Citation Index](#citation-index)

---

## Citation Guide

### Tier System

| Tier | Source Type | Authority Level | Verification |
| ---- | ----------- | --------------- | ------------ |
| **Tier 1** | IPBES, IPCC, IUCN, UN agencies | Highest | Intergovernmental review |
| **Tier 2** | Peer-reviewed journals | High | Peer review process |
| **Tier 3** | Government agencies, universities | Medium-High | Institutional review |
| **Tier 4** | NGOs, monitoring programs | Medium | Cross-verification required |

### Citation Format

```text
[ID] Author(s). (Year). Title. Source. DOI/URL.
     > Annotation: Brief description of content and relevance.
     > Used in: Article sections where cited.
     > Archived: Location in sources/ directory.
```

---

## Tier 1: Authoritative International Assessments

### IPBES Sources

**[T1-01]** IPBES. (2019). *Global Assessment Report on Biodiversity and Ecosystem Services*. IPBES Secretariat, Bonn, Germany.
<https://doi.org/10.5281/zenodo.6417333>

> **Annotation:** Comprehensive global assessment of biodiversity status and trends. Primary source for extinction risk statistics and driver attribution.
>
> **Used in:** Sections 1, 3, 5, 10, 14
>
> **Archived:** `../sources/tier-1_authoritative/IPBES_2019_Global_Assessment.pdf`

**[T1-02]** {Additional IPBES source}

### IPCC Sources

**[T1-03]** IPCC. (2022). *Climate Change 2022: Impacts, Adaptation and Vulnerability*. Cambridge University Press.
<https://doi.org/10.1017/9781009325844>

> **Annotation:** {Description}
>
> **Used in:** {Sections}
>
> **Archived:** `../sources/tier-1_authoritative/{filename}`

### IUCN Sources

**[T1-04]** IUCN. (2024). *The IUCN Red List of Threatened Species*. Version 2024-1.
<https://www.iucnredlist.org>

> **Annotation:** Primary database for species extinction risk assessments. Updated quarterly.
>
> **Used in:** {Sections}
>
> **Archived:** `../sources/tier-1_authoritative/IUCN_RedList_2024-1_export.csv`

**[T1-05]** {Additional IUCN source}

### Other UN/Intergovernmental Sources

**[T1-06]** {Source}

---

## Tier 2: Peer-Reviewed Literature

### Primary Research Articles

**[T2-01]** {Author, A. A., Author, B. B., & Author, C. C.}. ({Year}). {Article title}. *{Journal Name}*, {Volume}({Issue}), {Pages}. <https://doi.org/{DOI}>

> **Annotation:** {Brief description of the study and its relevance to this episode.}
>
> **Key Findings:** {1-2 sentence summary of relevant findings.}
>
> **Used in:** {Article sections}
>
> **Archived:** `../sources/tier-2_peer-reviewed/{filename}.pdf`

**[T2-02]** {Second peer-reviewed source}

**[T2-03]** {Third peer-reviewed source}

**[T2-04]** {Fourth peer-reviewed source}

**[T2-05]** {Fifth peer-reviewed source}

### Review Articles and Meta-Analyses

**[T2-06]** {Review article}

> **Annotation:** {Description}
>
> **Scope:** {What the review covers}
>
> **Used in:** {Sections}

**[T2-07]** {Meta-analysis}

### Methodological References

**[T2-08]** {Methodological paper}

> **Annotation:** Reference for {specific method used}.
>
> **Used in:** Methods documentation

---

## Tier 3: Government and Institutional Sources

### Government Agency Reports

**[T3-01]** {Agency Name}. ({Year}). *{Report Title}*. {Location}: {Publisher}.
{URL}

> **Annotation:** {Description}
>
> **Geographic Scope:** {Country/Region}
>
> **Used in:** {Sections}
>
> **Archived:** `../sources/tier-3_government/{filename}`

**[T3-02]** {Second government source}

### University and Research Institution Reports

**[T3-03]** {Institution}. ({Year}). *{Report Title}*.
{URL}

> **Annotation:** {Description}
>
> **Used in:** {Sections}

**[T3-04]** {Second institutional source}

### National Databases

**[T3-05]** {Database name and description}

---

## Tier 4: Verified NGO and Monitoring Data

### Conservation NGO Reports

**[T4-01]** {Organization}. ({Year}). *{Report Title}*.
{URL}

> **Annotation:** {Description}
>
> **Verification:** {How data was verified/cross-checked}
>
> **Used in:** {Sections}
>
> **Archived:** `../sources/tier-4_ngo-verified/{filename}`

**[T4-02]** {Second NGO source}

### Monitoring Programs

**[T4-03]** {Monitoring Program}. ({Year}). *{Dataset/Report}*.
{URL}

> **Annotation:** {Description}
>
> **Data Period:** {Time range}
>
> **Used in:** {Sections}

**[T4-04]** {Second monitoring source}

### Citizen Science Data

**[T4-05]** {Citizen science program}

> **Annotation:** {Description}
>
> **Quality Control:** {How data quality was ensured}
>
> **Used in:** {Sections}

---

## Datasets

### Primary Datasets Used

| ID | Name | Source | Format | Access | Archived |
| -- | ---- | ------ | ------ | ------ | -------- |
| D1 | {Dataset name} | {Source} | {CSV/JSON/etc.} | {Open/Restricted} | `../data/raw/{file}` |
| D2 | {Dataset name} | {Source} | {Format} | {Access} | `../data/raw/{file}` |
| D3 | {Dataset name} | {Source} | {Format} | {Access} | `../data/raw/{file}` |

### Derived Datasets

| ID | Name | Derived From | Description | Location |
| -- | ---- | ------------ | ----------- | -------- |
| DD1 | {Name} | D1, D2 | {How derived} | `../data/processed/{file}` |
| DD2 | {Name} | {Sources} | {How derived} | `../data/processed/{file}` |

---

## Citation Index

### By Article Section

| Section | Citations |
| ------- | --------- |
| 1. Introduction | T1-01, T2-01, T2-02 |
| 2. Historical Context | T2-03, T3-01 |
| 3. Current State | T1-01, T1-04, T2-04 |
| 4. Methods | T2-08 |
| 5. Primary Analysis | T1-01, T2-01, T2-05, D1 |
| 6. Secondary Analysis | T2-02, T2-06, D2 |
| 7. Case Studies | T3-01, T3-02, T4-01 |
| 8. Taxonomic Patterns | T1-04, T2-04 |
| 9. Temporal Dynamics | T2-01, T2-05, D1 |
| 10. Causal Mechanisms | T1-01, T2-03, T2-06 |
| 11. Interactions | T2-06, T2-07 |
| 12. Projections | T1-03, T2-07 |
| 13. Uncertainty | T2-08 |
| 14. Implications | T1-01, T1-03 |
| 15. Conclusions | T1-01, T2-01 |

### By Citation Frequency

| Rank | Citation | Count | Sections |
| ---- | -------- | ----- | -------- |
| 1 | T1-01 | {N} | 1, 3, 5, 10, 14, 15 |
| 2 | T2-01 | {N} | 1, 5, 9, 15 |
| 3 | T1-04 | {N} | 3, 8 |
| ... | ... | ... | ... |

---

## BibTeX Export

```bibtex
@report{IPBES2019,
  author = {{IPBES}},
  title = {Global Assessment Report on Biodiversity and Ecosystem Services},
  year = {2019},
  institution = {IPBES Secretariat},
  address = {Bonn, Germany},
  doi = {10.5281/zenodo.6417333}
}

@article{Author2024,
  author = {Author, A. A. and Author, B. B.},
  title = {Article Title},
  journal = {Journal Name},
  year = {2024},
  volume = {XX},
  number = {X},
  pages = {XX--XX},
  doi = {XX.XXXX/XXXXXXX}
}

% Add additional BibTeX entries as needed
```

---

## Source Archive Structure

```text
sources/
├── tier-1_authoritative/
│   ├── IPBES_2019_Global_Assessment.pdf
│   ├── IPCC_2022_AR6_WGII.pdf
│   └── IUCN_RedList_2024-1_export.csv
├── tier-2_peer-reviewed/
│   ├── Author2024_ArticleTitle.pdf
│   └── ...
├── tier-3_government/
│   ├── AgencyReport2023.pdf
│   └── ...
└── tier-4_ngo-verified/
    ├── NGOReport2024.pdf
    └── ...
```

---

## Document Metadata

| Field | Value |
| ----- | ----- |
| **Episode** | {X.X} - {Episode Name} |
| **Total Citations** | {N} |
| **Citation Style** | APA 7th (adapted) |
| **Last Verified** | {YYYY-MM-DD} |
| **Version** | 1.0.0 |

---

> **︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!**
