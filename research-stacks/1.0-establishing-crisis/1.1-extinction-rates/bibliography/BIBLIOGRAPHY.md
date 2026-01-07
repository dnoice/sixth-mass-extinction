<!--
✒ Metadata
    - Title: Bibliography (MB_SS-1.1 Edition - v1.0)
    - File Name: BIBLIOGRAPHY.md
    - Relative Path: research-stacks/1.0-establishing-crisis/1.1-extinction-rates/bibliography/BIBLIOGRAPHY.md
    - Artifact Type: docs
    - Version: 1.0.0
    - Date: 2026-01-07
    - Update: Tuesday, January 07, 2026
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Anthropic - Claude Opus 4.5
    - Signature: ︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!

✒ Description:
    Comprehensive annotated bibliography for Episode 1.1 (Baseline vs. Current
    Extinction Rates). Documents all sources with tiered classification,
    annotations, and usage tracking.

✒ Key Features:
    - Feature 1: Four-tier source classification system
    - Feature 2: Full citation with DOI/URL
    - Feature 3: Acquisition status tracking
    - Feature 4: Blueprint requirement mapping
    - Feature 5: BibTeX export format

✒ Other Important Information:
    - Citation style: APA 7th edition (adapted)
    - Source documents: Archived in ../sources/
    - Blueprint Reference: RESEARCH_BLUEPRINT_MB_SS-1.1_EXTINCTION_RATES.md
---------
-->

# Bibliography

## Episode 1.1: Baseline vs. Current Extinction Rates

> **Total Sources:** 14 (identified) | 10 (ready for acquisition)
>
> **Tier Distribution:** Tier 1: 3 | Tier 2: 9 | Tier 3: 1 | Tier 4: 1
>
> **Status:** Phase 1 - Source Collection (IN PROGRESS)
>
> **Last Updated:** 2026-01-07

---

## Table of Contents

1. [Citation Guide](#citation-guide)
1. [Tier 1: Authoritative International Assessments](#tier-1-authoritative-international-assessments)
1. [Tier 2: Peer-Reviewed Literature](#tier-2-peer-reviewed-literature)
1. [Tier 3: Government and Institutional Sources](#tier-3-government-and-institutional-sources)
1. [Tier 4: Verified NGO and Monitoring Data](#tier-4-verified-ngo-and-monitoring-data)
1. [Datasets](#datasets)
1. [BibTeX Export](#bibtex-export)

---

## Citation Guide

### Tier System

| Tier | Source Type | Authority Level | Verification |
| ---- | ----------- | --------------- | ------------ |
| **Tier 1** | IPBES, IPCC, IUCN, UN agencies | Highest | Intergovernmental review |
| **Tier 2** | Peer-reviewed journals | High | Peer review process |
| **Tier 3** | Government agencies, databases | Medium-High | Institutional review |
| **Tier 4** | NGOs, monitoring programs | Medium | Cross-verification required |

### Citation Format

```text
[ID] Author(s). (Year). Title. Source. DOI/URL.
     > Annotation: Brief description of content and relevance.
     > Blueprint Use: How it maps to research blueprint requirements.
     > Status: Acquisition status.
     > Archived: Location in sources/ directory.
```

---

## Tier 1: Authoritative International Assessments

### IPBES Sources

**[T1-01]** IPBES. (2019). *Summary for policymakers of the global assessment report on biodiversity and ecosystem services*. IPBES Secretariat, Bonn, Germany.
<https://doi.org/10.5281/zenodo.3553579>

> **Annotation:** Comprehensive global assessment establishing scientific consensus on biodiversity status. Primary source for "tens to hundreds of times higher" extinction rate claim.
>
> **Blueprint Use:** Primary source for consensus rates; extract confidence levels and rate multiplier language.
>
> **Key Extractions Needed:**
>
> - Exact language on extinction rate multipliers
> - Assessment methodology (literature synthesis)
> - Confidence levels assigned to claims
> - Attribution to human drivers
>
> **Status:** 🔄 READY FOR DOWNLOAD
>
> **Archived:** `../sources/tier-1_authoritative/IPBES_2019_GlobalAssessmentSPM.pdf`

---

### IUCN Sources

**[T1-02]** IUCN. (2024-2025). *The IUCN Red List of Threatened Species*. Version 2024-2.
<https://www.iucnredlist.org>

> **Annotation:** Primary database for species extinction risk assessments. Updated quarterly. Required for current E/MSY calculations.
>
> **Blueprint Use:** Data source for current extinctions; calculate E/MSY rates by taxa.
>
> **Key Data Needed:**
>
> - Complete species assessments by taxa
> - Extinction dates (Extinct, Extinct in Wild categories)
> - Threat status trends over time
> - Assessment coverage statistics
>
> **Status:** 🔒 BLOCKED - Requires human registration at <https://api.iucnredlist.org/users/sign_up>
>
> **API Notes:** v4 API required (v3 deprecated March 2025)
>
> **Archived:** `../sources/tier-1_authoritative/IUCN_RedList_2024-2_export.csv` (pending)

**[T1-03]** IUCN. (2024). *IUCN Red List Categories and Criteria*. Version 3.1. IUCN, Gland, Switzerland.
<https://www.iucnredlist.org/resources/categories-and-criteria>

> **Annotation:** Official methodology documentation for Red List assessments.
>
> **Blueprint Use:** Document data quality and assessment limitations.
>
> **Status:** 🔒 BLOCKED - Pending API registration
>
> **Archived:** `../sources/tier-1_authoritative/IUCN_Criteria_v3.1.pdf` (pending)

---

## Tier 2: Peer-Reviewed Literature

### Core Methodology Papers

**[T2-01]** Ceballos, G., Ehrlich, P. R., Barnosky, A. D., García, A., Pringle, R. M., & Palmer, T. M. (2015). Accelerated modern human–induced species losses: Entering the sixth mass extinction. *Science Advances*, 1(5), e1400253. <https://doi.org/10.1126/sciadv.1400253>

> **Annotation:** Foundational paper establishing E/MSY methodology and calculating modern vertebrate extinction rates. Core source for 100-1000x background rate claim.
>
> **Blueprint Use:** Core methodology source; extract exact E/MSY methodology, background rate calculations (0.1-2 E/MSY), vertebrate extinction data (1900-2014).
>
> **Key Extractions Needed:**
>
> - E/MSY calculation method (step-by-step)
> - Background rate range and justification
> - Current rate calculations by taxa
> - Conservative vs. elevated estimates
> - Methodological limitations acknowledged
>
> **Status:** 🔄 READY FOR DOWNLOAD (CC-BY-NC Open Access)
>
> **Archived:** `../sources/tier-2_peer-reviewed/Ceballos_2015_AcceleratedSpeciesLosses.pdf`

**[T2-02]** Ceballos, G., Ehrlich, P. R., & Dirzo, R. (2017). Biological annihilation via the ongoing sixth mass extinction signaled by vertebrate population losses and declines. *PNAS*, 114(30), E6089-E6096. <https://doi.org/10.1073/pnas.1704949114>

> **Annotation:** Extends analysis from species extinctions to population-level declines. Introduces "biological annihilation" concept. Documents 32% of vertebrate species declining.
>
> **Blueprint Use:** Population decline data; distinguish between extinction counts and population declines.
>
> **Key Extractions Needed:**
>
> - "32% of vertebrates declining" methodology
> - Geographic patterns of population loss
> - Relationship between extinction and defaunation
> - Abundance decline measurements
>
> **Status:** 🔄 READY FOR DOWNLOAD (Open Access)
>
> **Archived:** `../sources/tier-2_peer-reviewed/Ceballos_2017_BiologicalAnnihilation.pdf`

**[T2-03]** Barnosky, A. D., Matzke, N., Tomiya, S., Wogan, G. O. U., Swartz, B., Quental, T. B., Marshall, C., McGuire, J. L., Lindsey, E. L., Maguire, K. C., Mersey, B., & Ferrer, E. A. (2011). Has the Earth's sixth mass extinction already arrived? *Nature*, 471(7336), 51-57. <https://doi.org/10.1038/nature09678>

> **Annotation:** Establishes criteria for defining mass extinction (75% species loss threshold). Compares current rates to "Big Five" historical events.
>
> **Blueprint Use:** Mass extinction criteria; 75% threshold, comparison framework to Big Five, projection scenarios.
>
> **Key Extractions Needed:**
>
> - Historical mass extinction criteria
> - Comparison framework to Big Five
> - Time-to-threshold calculations
> - Conservative vs. realistic scenarios
>
> **Status:** 🔄 READY FOR DOWNLOAD (via CiteSeerX)
>
> **Archived:** `../sources/tier-2_peer-reviewed/Barnosky_2011_SixthMassExtinction.pdf`

---

### Background Rate Methodology

**[T2-04]** Pimm, S. L., Jenkins, C. N., Abell, R., Brooks, T. M., Gittleman, J. L., Joppa, L. N., Raven, P. H., Roberts, C. M., & Sexton, J. O. (2014). The biodiversity of species and their rates of extinction, distribution, and protection. *Science*, 344(6187), 1246752. <https://doi.org/10.1126/science.1246752>

> **Annotation:** Comprehensive review establishing current extinction rates at 1000x background. Alternative E/MSY methodology.
>
> **Blueprint Use:** Cross-validate Ceballos methodology; alternative background rate calculations.
>
> **Key Finding:** "Current rates of extinction are about 1000 times the likely background rate of extinction."
>
> **Status:** 🔄 READY FOR DOWNLOAD (Open Access)
>
> **Archived:** `../sources/tier-2_peer-reviewed/Pimm_2014_BiodiversityExtinctionRates.pdf`

**[T2-05]** De Vos, J. M., Joppa, L. N., Gittleman, J. L., Stephens, P. R., & Pimm, S. L. (2015). Estimating the normal background rate of species extinction. *Conservation Biology*, 29(2), 452-462. <https://doi.org/10.1111/cobi.12380>

> **Annotation:** Rigorous analysis establishing background rate closer to 0.1 E/MSY rather than 1 E/MSY. Critical for rate multiplier calculations.
>
> **Blueprint Use:** Establish 0.1-1 E/MSY range; alternative baseline estimates.
>
> **Key Finding:** "Typical rates of background extinction may be closer to 0.1 E/MSY. Thus, current extinction rates are 1,000 times higher than natural background rates."
>
> **Status:** 🔄 READY FOR DOWNLOAD (Open Access)
>
> **Archived:** `../sources/tier-2_peer-reviewed/DeVos_2015_BackgroundExtinctionRate.pdf`

---

### Taxonomic-Specific Studies

**[T2-06]** Luedtke, J. A., et al. (2023). Ongoing declines for the world's amphibians in the face of emerging threats. *Nature*, 622(7982), 308-314. <https://doi.org/10.1038/s41586-023-06578-4>

> **Annotation:** Second Global Amphibian Assessment. Establishes 40.7% of amphibian species globally threatened - the most threatened vertebrate class.
>
> **Blueprint Use:** Amphibian-specific rates; 41% threatened statistic, methodology.
>
> **Key Finding:** "Amphibians are the most threatened vertebrate class (40.7% of species are globally threatened)."
>
> **Status:** 🔄 READY FOR DOWNLOAD (Open Access via CITES)
>
> **Archived:** `../sources/tier-2_peer-reviewed/Luedtke_2023_AmphibianDeclines.pdf`

---

### Fossil Record & Paleontology

**[T2-07]** Alroy, J. (2008). Dynamics of origination and extinction in the marine fossil record. *PNAS*, 105(Supplement 1), 11536-11542.

> **Annotation:** Marine fossil record methodology for background rate estimation.
>
> **Blueprint Use:** Validate paleontological baselines; fossil-derived background rates.
>
> **Status:** ⏳ PENDING - Need to locate open access version
>
> **Archived:** `../sources/tier-2_peer-reviewed/Alroy_2008_MarineFossilRecord.pdf` (pending)

**[T2-08]** Raup, D. M., & Sepkoski, J. J. (1982). Mass extinctions in the marine fossil record. *Science*, 215(4539), 1501-1503. <https://doi.org/10.1126/science.215.4539.1501>

> **Annotation:** Foundational paper identifying the "Big Five" mass extinction events.
>
> **Blueprint Use:** Establish comparison framework for historical mass extinctions.
>
> **Status:** ⏳ PENDING - Historical paper, may require library access
>
> **Archived:** `../sources/tier-2_peer-reviewed/Raup_1982_MassExtinctions.pdf` (pending)

**[T2-09]** Jablonski, D. (1994). Extinctions in the fossil record. *Philosophical Transactions of the Royal Society B*, 344(1307), 11-17. <https://doi.org/10.1098/rstb.1994.0045>

> **Annotation:** Methodology for detecting extinctions from fossil record.
>
> **Blueprint Use:** Assess background rate uncertainty; fossil extinction detection reliability.
>
> **Status:** ⏳ PENDING - Need to locate open access version
>
> **Archived:** `../sources/tier-2_peer-reviewed/Jablonski_1994_FossilExtinctions.pdf` (pending)

---

## Tier 3: Government and Institutional Sources

### Paleobiology Database

**[T3-01]** Paleobiology Database (PBDB). (2024). *Extinction data from the fossil record*.
<https://paleobiodb.org/>

> **Annotation:** Open database of fossil occurrences and extinction events. Primary source for paleontological background rate calculations.
>
> **Blueprint Use:** Fossil extinction data; calculate E/MSY from geological record.
>
> **Data Access:** Open API at <https://paleobiodb.org/data1.2/>
>
> **Status:** 🔄 READY FOR DATA EXTRACTION
>
> **Archived:** Data extracts to be stored in `../data/raw/pbdb_*`

---

## Tier 4: Verified NGO and Monitoring Data

### Living Planet Index

**[T4-01]** WWF. (2024). *Living Planet Report 2024 - A System in Peril*. WWF, Gland, Switzerland.
<https://livingplanet.panda.org/>

> **Annotation:** Documents 73% decline in monitored wildlife populations since 1970. Supplementary context for extinction data.
>
> **Blueprint Use:** Population trend context; supplement extinctions with population data.
>
> **Key Finding:** "Over the past 50 years (1970–2020), the average size of monitored wildlife populations has shrunk by 73%."
>
> **Status:** 🔄 READY FOR DOWNLOAD (Open Access)
>
> **Archived:** `../sources/tier-4_ngo-verified/WWF_2024_LivingPlanetReport.pdf`

---

## Datasets

### Primary Datasets Required

| ID | Name | Source | Format | Access | Status |
| -- | ---- | ------ | ------ | ------ | ------ |
| D1 | IUCN Red List Export | IUCN API v4 | CSV/JSON | Registration Required | 🔒 BLOCKED |
| D2 | PBDB Extinction Data | Paleobiology Database | CSV | Open | 🔄 READY |
| D3 | Living Planet Index | WWF/ZSL | CSV | Open | 🔄 READY |

### Data Acquisition Notes

**D1 (IUCN):** Critical for E/MSY calculations. Requires human registration at <https://api.iucnredlist.org/users/sign_up>. This is a **blocking dependency** for Phase 2 data acquisition.

---

## BibTeX Export

```bibtex
@report{IPBES2019,
  author = {{IPBES}},
  title = {Summary for policymakers of the global assessment report on biodiversity and ecosystem services},
  year = {2019},
  institution = {IPBES Secretariat},
  address = {Bonn, Germany},
  doi = {10.5281/zenodo.3553579}
}

@article{Ceballos2015,
  author = {Ceballos, Gerardo and Ehrlich, Paul R. and Barnosky, Anthony D. and García, Andrés and Pringle, Robert M. and Palmer, Todd M.},
  title = {Accelerated modern human–induced species losses: Entering the sixth mass extinction},
  journal = {Science Advances},
  year = {2015},
  volume = {1},
  number = {5},
  pages = {e1400253},
  doi = {10.1126/sciadv.1400253}
}

@article{Ceballos2017,
  author = {Ceballos, Gerardo and Ehrlich, Paul R. and Dirzo, Rodolfo},
  title = {Biological annihilation via the ongoing sixth mass extinction signaled by vertebrate population losses and declines},
  journal = {PNAS},
  year = {2017},
  volume = {114},
  number = {30},
  pages = {E6089-E6096},
  doi = {10.1073/pnas.1704949114}
}

@article{Barnosky2011,
  author = {Barnosky, Anthony D. and Matzke, Nicholas and Tomiya, Susumu and Wogan, Guinevere O. U. and Swartz, Brian and Quental, Tiago B. and Marshall, Charles and McGuire, Jenny L. and Lindsey, Emily L. and Maguire, Kaitlin C. and Mersey, Ben and Ferrer, Elizabeth A.},
  title = {Has the Earth's sixth mass extinction already arrived?},
  journal = {Nature},
  year = {2011},
  volume = {471},
  number = {7336},
  pages = {51-57},
  doi = {10.1038/nature09678}
}

@article{Pimm2014,
  author = {Pimm, S. L. and Jenkins, C. N. and Abell, R. and Brooks, T. M. and Gittleman, J. L. and Joppa, L. N. and Raven, P. H. and Roberts, C. M. and Sexton, J. O.},
  title = {The biodiversity of species and their rates of extinction, distribution, and protection},
  journal = {Science},
  year = {2014},
  volume = {344},
  number = {6187},
  pages = {1246752},
  doi = {10.1126/science.1246752}
}

@article{DeVos2015,
  author = {De Vos, Jurriaan M. and Joppa, Lucas N. and Gittleman, John L. and Stephens, Patrick R. and Pimm, Stuart L.},
  title = {Estimating the normal background rate of species extinction},
  journal = {Conservation Biology},
  year = {2015},
  volume = {29},
  number = {2},
  pages = {452-462},
  doi = {10.1111/cobi.12380}
}

@article{Luedtke2023,
  author = {Luedtke, Jennifer A. and others},
  title = {Ongoing declines for the world's amphibians in the face of emerging threats},
  journal = {Nature},
  year = {2023},
  volume = {622},
  number = {7982},
  pages = {308-314},
  doi = {10.1038/s41586-023-06578-4}
}

@report{WWF2024,
  author = {{WWF}},
  title = {Living Planet Report 2024 - A System in Peril},
  year = {2024},
  institution = {WWF},
  address = {Gland, Switzerland},
  url = {https://livingplanet.panda.org/}
}
```

---

## Document Metadata

| Field | Value |
| ----- | ----- |
| **Episode** | 1.1 - Baseline vs. Current Extinction Rates |
| **Total Citations** | 14 (identified) |
| **Ready for Acquisition** | 10 |
| **Blocked** | 2 (IUCN API registration) |
| **Pending Investigation** | 2 (historical papers) |
| **Citation Style** | APA 7th (adapted) |
| **Last Verified** | 2026-01-07 |
| **Version** | 1.0.0 |

---

## Blocking Dependencies

| Source | Barrier | Required Human Action | Impact |
|--------|---------|----------------------|--------|
| IUCN Red List API | Registration required | Register at <https://api.iucnredlist.org/users/sign_up> | **BLOCKS** Phase 2 data acquisition |

---

> **︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!**
