<!--
✒ Metadata
    - Title: Source Archive README (MB_SS-1.1 Edition - v1.0)
    - File Name: README.md
    - Relative Path: research-stacks/1.0-establishing-crisis/1.1-extinction-rates/sources/README.md
    - Artifact Type: docs
    - Version: 1.0.0
    - Date: 2026-01-07
    - Update: Tuesday, January 07, 2026
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Anthropic - Claude Opus 4.5
    - Signature: ︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!

✒ Description:
    Source archive documentation and research ledger for Episode 1.1 (Baseline vs.
    Current Extinction Rates). Maps every source to blueprint requirements, research
    questions, and intended analytical use. Tracks acquisition status.

✒ Key Features:
    - Feature 1: 4-tier source organization (Authoritative → NGO)
    - Feature 2: Research ledger with source-to-requirement mapping
    - Feature 3: Acquisition status tracking
    - Feature 4: Dependency logging for blocked sources
    - Feature 5: File naming conventions

✒ Other Important Information:
    - Blueprint Reference: RESEARCH_BLUEPRINT_MB_SS-1.1_EXTINCTION_RATES.md
    - Ground Rule: If it isn't archived, documented, and reproducible, it does not exist
---------
-->

# Source Archive: MB_SS-1.1

## Baseline vs. Current Extinction Rates

---

**Episode:** 1.1
**Status:** Phase 1 - Source Collection (SUBSTANTIALLY COMPLETE)
**Last Updated:** 2026-01-07

---

## Tier System

| Tier | Authority Level | Source Type | Trust Level |
|------|-----------------|-------------|-------------|
| **1** | Intergovernmental | IPBES, IPCC, FAO, IUCN | Highest |
| **2** | Peer-Reviewed | Nature, Science, PNAS, specialty journals | High |
| **3** | Government | NOAA, USGS, EPA, national agencies | Medium-High |
| **4** | NGO/Database | WWF, WRI, research databases | Medium |

---

## Research Ledger

### Tier 1: Authoritative Sources

| ID | Source | Blueprint Requirement | Research Question | Analytical Use | Status |
|----|--------|----------------------|-------------------|----------------|--------|
| S1 | IPBES Global Assessment SPM (2019) | Primary source for consensus rates | What is the authoritative consensus on extinction rate multipliers? | Extract "tens to hundreds of times higher" claim basis, confidence levels | ✅ ACQUIRED |
| — | IUCN Red List Summary Statistics (2025-2) | Data source for current extinctions | How many species are documented extinct? | Calculate current E/MSY rates by taxa | ✅ ACQUIRED |
| — | IUCN Red List Table 7 (2007-2024) | Historical category changes | Which species moved to Extinct? | Track documented modern extinctions | ✅ ACQUIRED |
| — | IUCN Species Data Export (CR-Decreasing) | Current threat data | What species are on extinction trajectory? | Identify highest-risk cohort | ✅ ACQUIRED |

### Tier 2: Peer-Reviewed Sources

| ID | Source | Blueprint Requirement | Research Question | Analytical Use | Status |
|----|--------|----------------------|-------------------|----------------|--------|
| S2 | Ceballos, Ehrlich & Dirzo (2015) Science Advances | Core methodology source | How is E/MSY calculated? What are background rates? | Extract methodology, replicate calculations | ✅ ACQUIRED |
| S3 | Ceballos et al. (2017) PNAS | Population decline data | What is "biological annihilation"? | Distinguish extinctions from population declines | ✅ ACQUIRED |
| NEW | Barnosky et al. (2011) Nature | Mass extinction criteria | What defines a mass extinction? | 75% threshold, comparison to Big Five | ✅ ACQUIRED |
| NEW | Ceballos et al. (2023) PNAS | Genus-level extinction | How do genus extinctions compare? | Updated extinction analysis | ✅ ACQUIRED |
| S12 | Luedtke et al. (2023) Nature | Amphibian-specific rates | What is current amphibian threat level? | 41% threatened statistic, methodology | ✅ ACQUIRED |
| — | Pimm et al. (2014) Science | E/MSY methodology | Alternative background rate calculations | Cross-validate Ceballos methodology | ✅ ACQUIRED |
| — | De Vos et al. (2015) Conservation Biology | Background rate estimates | What are alternative baseline estimates? | Establish 0.1-1 E/MSY range | ✅ ACQUIRED |
| — | Alroy (2008) PNAS | Fossil record methodology | How are background rates derived from fossils? | Validate paleontological baselines | ✅ ACQUIRED |
| — | Harnik et al. (2012) TREE | Marine extinction rates | How do marine rates compare? | Extend analysis beyond terrestrial vertebrates | ✅ ACQUIRED |
| — | Raup & Sepkoski (1982) Science | Historical mass extinctions | What are the Big Five patterns? | Establish comparison framework | ⏳ PENDING |
| — | Jablonski (1994) | Fossil record extinctions | How reliable is fossil extinction detection? | Assess background rate uncertainty | ⏳ PENDING |

### Tier 3: Government Sources

| ID | Source | Blueprint Requirement | Research Question | Analytical Use | Status |
|----|--------|----------------------|-------------------|----------------|--------|
| — | Paleobiology Database (PBDB) | Fossil extinction data | What are fossil-derived background rates? | Calculate E/MSY from geological record | 🔄 READY |

### Tier 4: NGO/Database Sources

| ID | Source | Blueprint Requirement | Research Question | Analytical Use | Status |
|----|--------|----------------------|-------------------|----------------|--------|
| — | Living Planet Report (2024) | Population trend context | How are vertebrate populations changing? | Supplement extinctions with population data | 🔄 READY |
| — | GBIF Species Data | Occurrence/distribution | What is species detection coverage? | Assess taxonomic completeness | ⏳ PENDING |

---

## Acquisition Status Key

| Symbol | Status | Meaning |
|--------|--------|---------|
| ✅ | ACQUIRED | Source archived in appropriate tier directory |
| ⏳ | PENDING | Acquisition not yet attempted |
| 🔄 | IN PROGRESS | Acquisition underway |
| 🔒 | BLOCKED | Requires human intervention (paywall, registration) |
| ❌ | UNAVAILABLE | Cannot be obtained; logged as dependency |

---

## Source Acquisition Paths

### Tier 1: Authoritative Sources

#### IPBES Global Assessment SPM (2019) — ✅ OPEN ACCESS

| Attribute | Value |
|-----------|-------|
| **Full Title** | Summary for policymakers of the global assessment report on biodiversity and ecosystem services |
| **DOI** | 10.5281/zenodo.3553579 |
| **Primary URL** | <https://files.ipbes.net/ipbes-web-prod-public-files/inline/files/ipbes_global_assessment_report_summary_for_policymakers.pdf> |
| **Backup URL** | <https://zenodo.org/records/3553579> |
| **Mirror** | <https://www.biologicaldiversity.org/programs/biodiversity/pdfs/Summary-for-Policymakers-IPBES-Global-Assessment.pdf> |
| **File Name** | `IPBES_2019_GlobalAssessmentSPM.pdf` |
| **Status** | 🔄 READY FOR DOWNLOAD |

#### IUCN Red List Data (2024-2025) — ✅ OPEN ACCESS (API)

| Attribute | Value |
|-----------|-------|
| **API Endpoint** | <https://api.iucnredlist.org/> |
| **API Docs** | <https://api.iucnredlist.org/api-docs/index.html> |
| **Note** | v4 API required (v3 deprecated March 2025) |
| **Registration** | <https://api.iucnredlist.org/users/sign_up> |
| **Python Package** | `IUCN-API` on PyPI |
| **Status** | 🔒 REQUIRES REGISTRATION (human action needed) |

---

### Tier 2: Peer-Reviewed Sources

#### Ceballos et al. (2015) Science Advances — ✅ OPEN ACCESS (CC-BY-NC)

| Attribute | Value |
|-----------|-------|
| **Full Title** | Accelerated modern human-induced species losses: Entering the sixth mass extinction |
| **DOI** | 10.1126/sciadv.1400253 |
| **Primary URL** | <https://www.science.org/doi/10.1126/sciadv.1400253> |
| **PMC** | <https://pmc.ncbi.nlm.nih.gov/articles/PMC4640606/> |
| **Direct PDF** | <https://pringle.princeton.edu/wp-content/uploads/sites/798/2020/10/2015_Ceballos-et-al.-Science-Advances.pdf> |
| **File Name** | `Ceballos_2015_AcceleratedSpeciesLosses.pdf` |
| **Status** | 🔄 READY FOR DOWNLOAD |

#### Ceballos et al. (2017) PNAS — ✅ OPEN ACCESS

| Attribute | Value |
|-----------|-------|
| **Full Title** | Biological annihilation via the ongoing sixth mass extinction signaled by vertebrate population losses and declines |
| **DOI** | 10.1073/pnas.1704949114 |
| **Primary URL** | <https://www.pnas.org/doi/10.1073/pnas.1704949114> |
| **Direct PDF** | <https://www.cbd.int/financial/2017docs/ceballos-sixth2017.pdf> |
| **PMC** | <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5544311/> |
| **File Name** | `Ceballos_2017_BiologicalAnnihilation.pdf` |
| **Status** | 🔄 READY FOR DOWNLOAD |

#### Barnosky et al. (2011) Nature — ⚠️ PARTIALLY OPEN

| Attribute | Value |
|-----------|-------|
| **Full Title** | Has the Earth's sixth mass extinction already arrived? |
| **DOI** | 10.1038/nature09678 |
| **PubMed** | <https://pubmed.ncbi.nlm.nih.gov/21368823/> |
| **CiteSeerX PDF** | <https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=de1c27c86753cbcb5ed8d6e520e3ac79dff02ff9> |
| **File Name** | `Barnosky_2011_SixthMassExtinction.pdf` |
| **Status** | 🔄 READY FOR DOWNLOAD (via CiteSeerX) |

#### Luedtke et al. (2023) Nature — ✅ OPEN ACCESS

| Attribute | Value |
|-----------|-------|
| **Full Title** | Ongoing declines for the world's amphibians in the face of emerging threats |
| **DOI** | 10.1038/s41586-023-06578-4 |
| **Direct PDF** | <https://cites.org/sites/default/files/common/docs/meeting_info/amphibians/s41586-023-06578-4_Global%20assessment.pdf> |
| **IUCN Resources** | <https://www.iucnredlist.org/resources/luedtkeetal2023> |
| **File Name** | `Luedtke_2023_AmphibianDeclines.pdf` |
| **Status** | 🔄 READY FOR DOWNLOAD |

#### Pimm et al. (2014) Science — ✅ OPEN ACCESS

| Attribute | Value |
|-----------|-------|
| **Full Title** | The biodiversity of species and their rates of extinction, distribution, and protection |
| **DOI** | 10.1126/science.1246752 |
| **Direct PDF** | <https://senate.ucsd.edu/media/206192/science-2014-pimm-extinction-review.pdf> |
| **Duke Repository** | <https://dukespace.lib.duke.edu/items/e1b04bf7-8fdd-4ee3-b0c8-1176e1f7066f> |
| **File Name** | `Pimm_2014_BiodiversityExtinctionRates.pdf` |
| **Status** | 🔄 READY FOR DOWNLOAD |

#### De Vos et al. (2015) Conservation Biology — ✅ OPEN ACCESS

| Attribute | Value |
|-----------|-------|
| **Full Title** | Estimating the normal background rate of species extinction |
| **DOI** | 10.1111/cobi.12380 |
| **Wiley ePDF** | <https://conbio.onlinelibrary.wiley.com/doi/epdf/10.1111/cobi.12380> |
| **Duke Repository** | <https://dukespace.lib.duke.edu/items/9067212b-1e6f-4ed2-be4a-2febb133b3ed> |
| **Semantic Scholar** | <https://www.semanticscholar.org/paper/18720e1f36fe3e081933ca677227c4616473df28> |
| **File Name** | `DeVos_2015_BackgroundExtinctionRate.pdf` |
| **Status** | 🔄 READY FOR DOWNLOAD |

#### Alroy (2008) PNAS — 🔒 REQUIRES INVESTIGATION

| Attribute | Value |
|-----------|-------|
| **Full Title** | Dynamics of origination and extinction in the marine fossil record |
| **Status** | ⏳ PENDING - Need to locate open access version |

#### Raup & Sepkoski (1982) Science — 🔒 REQUIRES INVESTIGATION

| Attribute | Value |
|-----------|-------|
| **Full Title** | Mass extinctions in the marine fossil record |
| **Status** | ⏳ PENDING - Historical paper, may require library access |

---

### Tier 3: Government/Database Sources

#### Paleobiology Database (PBDB) — ✅ OPEN ACCESS

| Attribute | Value |
|-----------|-------|
| **URL** | <https://paleobiodb.org/> |
| **API** | <https://paleobiodb.org/data1.2/> |
| **Status** | 🔄 READY FOR DATA EXTRACTION |

---

### Tier 4: NGO Sources

#### WWF Living Planet Report (2024) — ✅ OPEN ACCESS

| Attribute | Value |
|-----------|-------|
| **Full Title** | Living Planet Report 2024 - A System in Peril |
| **Full Report PDF** | <https://www.wwf.org.uk/sites/default/files/2024-10/living-planet-report-2024.pdf> |
| **Executive Summary** | <https://wwflpr.awsassets.panda.org/downloads/2024-lpr-executive-summary.pdf> |
| **Key Findings** | <https://wwflpr.awsassets.panda.org/downloads/lpr24_key-findings.pdf> |
| **File Name** | `WWF_2024_LivingPlanetReport.pdf` |
| **Status** | 🔄 READY FOR DOWNLOAD |

---

## Blocked Source Dependencies

Sources that cannot be automatically acquired are logged here with exact acquisition steps.

| Source | Barrier | Required Action | Priority | Blocking |
|--------|---------|-----------------|----------|----------|
| IUCN Red List API | Registration required | Human must register at <https://api.iucnredlist.org/users/sign_up> | HIGH | Yes - blocks data acquisition |
| Alroy (2008) | Not yet located | Search for open access version or request via library | MEDIUM | No - supplementary source |
| Raup & Sepkoski (1982) | Historical paper | May require library access or JSTOR | MEDIUM | No - supplementary source |

---

## File Naming Convention

```
AuthorLastName_Year_ShortTitle.pdf
```

**Examples:**

- `Ceballos_2015_AcceleratedSpeciesLosses.pdf`
- `IPBES_2019_GlobalAssessmentSPM.pdf`
- `Barnosky_2011_SixthMassExtinction.pdf`

---

## Directory Structure

```
sources/
├── README.md                    ← YOU ARE HERE
├── tier-1_authoritative/
│   └── (IPBES, IUCN reports)
├── tier-2_peer-reviewed/
│   └── (Journal articles)
├── tier-3_government/
│   └── (Agency reports, databases)
└── tier-4_ngo-verified/
    └── (NGO reports, datasets)
```

---

## Acquisition Log

| Date | Source | Action | Result | Notes |
|------|--------|--------|--------|-------|
| 2026-01-07 | — | Phase 1 initiated | ✅ | Research ledger created |
| 2026-01-07 | IPBES 2019 | URL verification | ✅ | Open access confirmed, 3 mirrors identified |
| 2026-01-07 | Ceballos 2015 | URL verification | ✅ | CC-BY-NC, PMC and direct PDF available |
| 2026-01-07 | Ceballos 2017 | URL verification | ✅ | Open access, CBD mirror available |
| 2026-01-07 | Barnosky 2011 | URL verification | ✅ | Available via CiteSeerX |
| 2026-01-07 | Luedtke 2023 | URL verification | ✅ | CITES.org hosts PDF |
| 2026-01-07 | Pimm 2014 | URL verification | ✅ | UCSD and Duke repositories |
| 2026-01-07 | De Vos 2015 | URL verification | ✅ | Multiple open access paths |
| 2026-01-07 | WWF LPR 2024 | URL verification | ✅ | Full report, summary, and key findings available |
| 2026-01-07 | IUCN API | Registration check | 🔒 | Human registration required at api.iucnredlist.org |
| 2026-01-07 | PBDB | API verification | ✅ | Open API, no registration required |
| 2026-01-07 | IPBES 2019 | **ACQUIRED** | ✅ | Archived to tier-1_authoritative/ |
| 2026-01-07 | Ceballos 2015 | **ACQUIRED** | ✅ | Archived to tier-2_peer-reviewed/ |
| 2026-01-07 | Ceballos 2017 | **ACQUIRED** | ✅ | Archived to tier-2_peer-reviewed/ |
| 2026-01-07 | Ceballos 2023 | **ACQUIRED** | ✅ | Genus extinction paper added |
| 2026-01-07 | Barnosky 2011 | **ACQUIRED** | ✅ | Archived to tier-2_peer-reviewed/ |
| 2026-01-07 | Pimm 2014 | **ACQUIRED** | ✅ | Archived to tier-2_peer-reviewed/ |
| 2026-01-07 | De Vos 2015 | **ACQUIRED** | ✅ | Archived to tier-2_peer-reviewed/ |
| 2026-01-07 | IUCN Summary Tables | **ACQUIRED** | ✅ | 18 years Table 7 (2007-2024) + 2025-2 full set |
| 2026-01-07 | IUCN Species Export | **ACQUIRED** | ✅ | 1,232 CR-Decreasing Animalia records |
| 2026-01-07 | RLI Time Series | **ACQUIRED** | ✅ | 13 global + regional CSVs (1993-2020+) |
| 2026-01-07 | Luedtke 2023 | **ACQUIRED** | ✅ | Downloaded from CITES.org (4.9 MB) |
| 2026-01-07 | Alroy 2008 | **ACQUIRED** | ✅ | Phanerozoic marine fossil trends (166 KB) |
| 2026-01-07 | Harnik 2012 | **ACQUIRED** | ✅ | Marine extinction risk from STRI (859 KB) |

---

## Verification Checklist

Phase 1 is complete when:

- [x] All Tier-1 authoritative sources acquired or logged as blocked
- [x] Core Tier-2 papers (Ceballos 2015, 2017; Barnosky 2011) acquired
- [x] E/MSY methodology sources obtained (Ceballos, Pimm, De Vos)
- [x] IUCN data access confirmed (via direct exports, bypassed API)
- [x] All blocked sources have documented acquisition paths
- [x] Research ledger fully populated with analytical use mapping

**Phase 1 Status: ✅ SUBSTANTIALLY COMPLETE**

Remaining optional sources (Luedtke 2023, Alroy 2008, historical papers) are supplementary and can be acquired during Phase 3 if needed.

---

> ︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!
