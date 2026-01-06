<!--
✒ Metadata
    - Title: Data Sources Attributes Matrix (SME Edition - v1.0)
    - File Name: DATA_SOURCES_ATTRIBUTES_MATRIX.md
    - Relative Path: docs/data-sources-matrix/DATA_SOURCES_ATTRIBUTES_MATRIX.md
    - Artifact Type: docs
    - Version: 1.0.0
    - Date: 2025-12-12
    - Update: Thursday, December 12, 2025
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Anthropic - Claude Opus 4.5
    - Signature: ︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!

✒ Description:
    Master matrix tracking all data sources used across the Sixth Mass Extinction
    (SME) article series. This document provides comprehensive metadata for every
    data source including provenance, quality attributes, access methods, update
    frequencies, and usage tracking across sections.

✒ Key Features:
    - Feature 1: Complete source catalog with unique identifiers (DS-XX-###)
    - Feature 2: Quality assessment scoring for each source (1-5 scale)
    - Feature 3: Access method documentation (API, download, request)
    - Feature 4: Update frequency and currency tracking
    - Feature 5: Section usage mapping (which sections use which sources)
    - Feature 6: Citation format templates for proper attribution
    - Feature 7: Data license and usage rights documentation
    - Feature 8: Known limitations and caveats for each source

✒ Usage Instructions:
    Reference this matrix when working with data sources in the SME project.

    How to use:
        1. Reference DS-XXX codes when citing sources in articles/notebooks
        2. Check currency dates before using data
        3. Follow access protocols for each source type
        4. Update LAST_VERIFIED when re-checking sources
        5. Consult quality scores when prioritizing sources

✒ Other Important Information:
    - Dependencies: None (documentation only)
    - Compatible platforms: Universal (all text editors, IDEs)
    - Scope: All SME article series data sources
    - Update frequency: As new sources are added or verified
---------
-->

# DATA SOURCES ATTRIBUTES MATRIX

## Sixth Mass Extinction Article Series

---

## TABLE OF CONTENTS

1. [Matrix Overview](#matrix-overview)
2. [Quality Assessment Framework](#quality-assessment-framework)
3. [Primary Authoritative Sources](#primary-authoritative-sources)
4. [Secondary Research Sources](#secondary-research-sources)
5. [Derived Datasets](#derived-datasets)
6. [Source-to-Section Mapping](#source-to-section-mapping)
7. [Data Currency Log](#data-currency-log)
8. [Access Protocols](#access-protocols)

---

## MATRIX OVERVIEW

### Source Identification System

Each data source receives a unique identifier:

| Prefix | Category | Example |
| ------ | -------- | ------- |
| DS-PA | Primary Authoritative | DS-PA-001 (IUCN Red List) |
| DS-PR | Peer-Reviewed Research | DS-PR-001 (Barnosky 2011) |
| DS-GD | Government/Institutional Data | DS-GD-001 (NOAA) |
| DS-NG | NGO/Conservation Data | DS-NG-001 (WWF LPI) |
| DS-DD | Derived Dataset (our creation) | DS-DD-001 |

### Attribute Definitions

| Attribute | Description |
| --------- | ----------- |
| **SOURCE_ID** | Unique identifier (DS-XX-###) |
| **NAME** | Official source name |
| **PUBLISHER** | Publishing organization |
| **TYPE** | Database, Report, Paper, Dataset, API |
| **SCOPE** | Geographic and taxonomic coverage |
| **TEMPORAL** | Time period covered |
| **UPDATE_FREQ** | How often source is updated |
| **LAST_VERIFIED** | When we last confirmed currency |
| **ACCESS** | API, Download, Request, Subscription |
| **URL** | Primary access point |
| **LICENSE** | Usage rights and restrictions |
| **QUALITY_SCORE** | Our assessment (1-5 scale) |
| **SECTIONS_USED** | Which article sections reference this |
| **CITATION** | Proper citation format |
| **NOTES** | Known limitations, caveats |

---

## QUALITY ASSESSMENT FRAMEWORK

### Scoring Criteria (1-5 Scale)

| Score | Authority | Methodology | Coverage | Currency | Reproducibility |
| ----- | --------- | ----------- | -------- | -------- | --------------- |
| **5** | Gold standard (IUCN, IPCC) | Peer-reviewed, transparent | Global, comprehensive | Updated <1 year | Full data access |
| **4** | Authoritative institution | Documented methodology | Near-global, most taxa | Updated 1-2 years | Partial data access |
| **3** | Reputable organization | Some documentation | Regional or taxon-limited | Updated 2-3 years | Aggregated data only |
| **2** | Single research group | Limited documentation | Localized | Updated 3-5 years | Limited access |
| **1** | Unverified/uncertain | Unclear methods | Highly limited | >5 years old | No access |

### Composite Quality Score

```text
QUALITY_SCORE = (Authority + Methodology + Coverage + Currency + Reproducibility) / 5
```

---

## PRIMARY AUTHORITATIVE SOURCES

### DS-PA-001: IUCN Red List of Threatened Species

| Attribute | Value |
| --------- | ----- |
| **SOURCE_ID** | DS-PA-001 |
| **NAME** | IUCN Red List of Threatened Species |
| **PUBLISHER** | International Union for Conservation of Nature |
| **TYPE** | Database + API |
| **SCOPE** | Global; 169,420 species assessed (v2025-2) |
| **TEMPORAL** | 1964-present (continuous updates) |
| **UPDATE_FREQ** | 3× per year (typically) |
| **LAST_VERIFIED** | 2025-12-12 |
| **ACCESS** | API (token required), Web interface, Bulk download |
| **URL** | <https://www.iucnredlist.org> |
| **API_DOCS** | <https://apiv3.iucnredlist.org/api/v3/docs> |
| **LICENSE** | CC BY-NC-SA 4.0 (commercial use requires license) |
| **QUALITY_SCORE** | 5.0 |
| **SECTIONS_USED** | 1.1, 1.2, 1.3, 1.5, 2.x, 3.x, 4.x, 8.x, 9.x |
| **CITATION** | IUCN (2025). The IUCN Red List of Threatened Species. Version 2025-2. <https://www.iucnredlist.org> |
| **NOTES** | Taxonomic bias toward vertebrates and plants; invertebrate/fungi coverage improving but incomplete. Assessment lag can mean recent declines not captured. |

#### Key Statistics (v2025-2)

- Total species assessed: 169,420
- Threatened species: 47,187 (27.8%)
- Critically Endangered: ~9,800
- Endangered: ~16,500
- Vulnerable: ~20,900
- Extinct: 943+
- Extinct in Wild: 90+

---

### DS-PA-002: IUCN Red List Guidelines

| Attribute | Value |
| --------- | ----- |
| **SOURCE_ID** | DS-PA-002 |
| **NAME** | Guidelines for Using the IUCN Red List Categories and Criteria |
| **PUBLISHER** | IUCN Standards and Petitions Committee |
| **TYPE** | Methodology Document |
| **VERSION** | Version 16 (March 2024) |
| **LAST_VERIFIED** | 2025-12-12 |
| **ACCESS** | PDF Download (free) |
| **URL** | <https://www.iucnredlist.org/resources/redlistguidelines> |
| **LICENSE** | Open access |
| **QUALITY_SCORE** | 5.0 |
| **SECTIONS_USED** | 1.1, 1.2, 1.5, methods documentation |
| **CITATION** | IUCN Standards and Petitions Committee (2024). Guidelines for Using the IUCN Red List Categories and Criteria. Version 16. |
| **NOTES** | Essential for understanding category thresholds and assessment methodology |

---

### DS-PA-003: Living Planet Report / Living Planet Index

| Attribute | Value |
| --------- | ----- |
| **SOURCE_ID** | DS-PA-003 |
| **NAME** | Living Planet Report & Living Planet Index |
| **PUBLISHER** | World Wildlife Fund (WWF) & Zoological Society of London (ZSL) |
| **TYPE** | Report + Database |
| **SCOPE** | Global; ~35,000 populations of 5,495 vertebrate species |
| **TEMPORAL** | 1970-2020 (LPI 2024) |
| **UPDATE_FREQ** | Biennial (every 2 years) |
| **LAST_VERIFIED** | 2025-12-12 |
| **ACCESS** | Report: Free download; Database: Request access |
| **URL** | <https://livingplanet.panda.org> |
| **DATABASE_URL** | <https://livingplanetindex.org/data_portal> |
| **LICENSE** | Report: Open; Database: Academic use on request |
| **QUALITY_SCORE** | 4.8 |
| **SECTIONS_USED** | 1.3, 1.4, 2.x, 3.x, 6.x |
| **CITATION** | WWF (2024). Living Planet Report 2024 – A System in Peril. WWF, Gland, Switzerland. |
| **NOTES** | Measures population abundance, not extinction. Geographic and taxonomic biases (more European/N. American data). 73% average decline headline figure. |

#### Key Metrics

- Global LPI decline (1970-2020): 73% average
- Freshwater LPI decline: 85%
- Latin America & Caribbean: 95% decline
- Terrestrial: 69% decline
- Marine: 56% decline

---

### DS-PA-004: IPBES Global Assessment

| Attribute | Value |
| --------- | ----- |
| **SOURCE_ID** | DS-PA-004 |
| **NAME** | IPBES Global Assessment Report on Biodiversity and Ecosystem Services |
| **PUBLISHER** | Intergovernmental Science-Policy Platform on Biodiversity and Ecosystem Services |
| **TYPE** | Assessment Report |
| **SCOPE** | Global, comprehensive |
| **DATE** | 2019 (summary); Full report 2019 |
| **UPDATE_FREQ** | Major assessment every ~5-7 years |
| **LAST_VERIFIED** | 2025-12-12 |
| **ACCESS** | Free download |
| **URL** | <https://ipbes.net/global-assessment> |
| **LICENSE** | Open access |
| **QUALITY_SCORE** | 5.0 |
| **SECTIONS_USED** | 1.x, 2.x, 5.x, 6.x, 7.x, 9.x, 10.x |
| **CITATION** | IPBES (2019). Global assessment report on biodiversity and ecosystem services. IPBES secretariat, Bonn, Germany. |
| **NOTES** | Landmark synthesis; "1 million species threatened" headline. Some projections now outdated. |

#### Key Findings

- ~1 million species threatened with extinction
- Nature declining at unprecedented rates
- 5 direct drivers: land/sea use change, exploitation, climate, pollution, invasive species
- 75% land surface significantly altered
- 66% marine environment impacted

---

### DS-PA-005: IPCC Assessment Reports

| Attribute | Value |
| --------- | ----- |
| **SOURCE_ID** | DS-PA-005 |
| **NAME** | IPCC Assessment Reports (AR6, special reports) |
| **PUBLISHER** | Intergovernmental Panel on Climate Change |
| **TYPE** | Assessment Reports |
| **SCOPE** | Global climate and impacts |
| **DATE** | AR6: 2021-2023; SR1.5: 2018; SROCC: 2019 |
| **UPDATE_FREQ** | Major assessment every ~7 years |
| **LAST_VERIFIED** | 2025-12-12 |
| **ACCESS** | Free download |
| **URL** | <https://www.ipcc.ch/reports/> |
| **LICENSE** | Open access |
| **QUALITY_SCORE** | 5.0 |
| **SECTIONS_USED** | 2.5, 4.x, 5.x, 6.x, 9.x |
| **CITATION** | IPCC (2023). Climate Change 2023: Synthesis Report. |
| **NOTES** | Gold standard for climate science; biodiversity sections in WGII |

---

### DS-PA-006: Global Biodiversity Information Facility (GBIF)

| Attribute | Value |
| --------- | ----- |
| **SOURCE_ID** | DS-PA-006 |
| **NAME** | Global Biodiversity Information Facility |
| **PUBLISHER** | GBIF Secretariat |
| **TYPE** | Database / Data Portal |
| **SCOPE** | >2.4 billion occurrence records; all taxa |
| **TEMPORAL** | Historical to present |
| **UPDATE_FREQ** | Continuous |
| **LAST_VERIFIED** | 2025-12-12 |
| **ACCESS** | API, Web interface, Bulk download |
| **URL** | <https://www.gbif.org> |
| **API_DOCS** | <https://www.gbif.org/developer/summary> |
| **LICENSE** | Varies by dataset (CC0, CC-BY, CC-BY-NC) |
| **QUALITY_SCORE** | 4.5 |
| **SECTIONS_USED** | 3.x, 4.x, species distribution modeling |
| **CITATION** | GBIF.org (2025). GBIF Occurrence Download [DOI]. |
| **NOTES** | Massive scale but quality varies; spatial biases toward developed countries |

---

### DS-PA-007: Global Forest Watch

| Attribute | Value |
| --------- | ----- |
| **SOURCE_ID** | DS-PA-007 |
| **NAME** | Global Forest Watch |
| **PUBLISHER** | World Resources Institute |
| **TYPE** | Platform + Data |
| **SCOPE** | Global forest cover and loss |
| **TEMPORAL** | 2000-present (annual) |
| **UPDATE_FREQ** | Annual |
| **LAST_VERIFIED** | 2025-12-12 |
| **ACCESS** | API, Web interface, Download |
| **URL** | <https://www.globalforestwatch.org> |
| **DATA_URL** | <https://data.globalforestwatch.org> |
| **LICENSE** | CC-BY 4.0 |
| **QUALITY_SCORE** | 4.8 |
| **SECTIONS_USED** | 2.1, 4.1, 5.1, 5.2 |
| **CITATION** | Global Forest Watch (2025). [Dataset name]. World Resources Institute. |
| **NOTES** | Based on Hansen et al. Landsat analysis; tree cover ≠ forest (plantations included) |

#### Key Datasets

- Tree Cover Loss (annual, 30m resolution)
- Primary Forest Loss
- Fire Alerts (VIIRS, near real-time)
- Deforestation Drivers

---

### DS-PA-008: NOAA Coral Reef Watch

| Attribute | Value |
| --------- | ----- |
| **SOURCE_ID** | DS-PA-008 |
| **NAME** | NOAA Coral Reef Watch |
| **PUBLISHER** | National Oceanic and Atmospheric Administration |
| **TYPE** | Monitoring System + Data |
| **SCOPE** | Global coral reefs |
| **TEMPORAL** | 1985-present |
| **UPDATE_FREQ** | Daily (satellite); periodic reports |
| **LAST_VERIFIED** | 2025-12-12 |
| **ACCESS** | Free download, API |
| **URL** | <https://coralreefwatch.noaa.gov> |
| **LICENSE** | Public domain (U.S. government) |
| **QUALITY_SCORE** | 5.0 |
| **SECTIONS_USED** | 3.5, 4.x, 9.x |
| **CITATION** | NOAA Coral Reef Watch (2025). [Product name]. |
| **NOTES** | 4th global bleaching event (2023-2025) tracking; Alert Level 3-5 scale expansion |

---

### DS-PA-009: FAO Fisheries and Aquaculture Data

| Attribute | Value |
| --------- | ----- |
| **SOURCE_ID** | DS-PA-009 |
| **NAME** | FAO Fisheries and Aquaculture Statistics |
| **PUBLISHER** | Food and Agriculture Organization of the United Nations |
| **TYPE** | Database |
| **SCOPE** | Global fisheries |
| **TEMPORAL** | 1950-present |
| **UPDATE_FREQ** | Annual |
| **LAST_VERIFIED** | 2025-12-12 |
| **ACCESS** | Free download, API |
| **URL** | <https://www.fao.org/fishery/statistics> |
| **LICENSE** | Open access |
| **QUALITY_SCORE** | 4.5 |
| **SECTIONS_USED** | 2.4, 3.3, 5.3 |
| **CITATION** | FAO (2025). Fisheries and Aquaculture Statistics. |
| **NOTES** | Relies on national reporting; IUU fishing underreported |

---

### DS-PA-010: CITES Trade Database

| Attribute | Value |
| --------- | ----- |
| **SOURCE_ID** | DS-PA-010 |
| **NAME** | CITES Trade Database |
| **PUBLISHER** | UNEP-WCMC on behalf of CITES Secretariat |
| **TYPE** | Database |
| **SCOPE** | International wildlife trade (CITES-listed species) |
| **TEMPORAL** | 1975-present |
| **UPDATE_FREQ** | Annual |
| **LAST_VERIFIED** | 2025-12-12 |
| **ACCESS** | Free (web query), Bulk download (request) |
| **URL** | <https://trade.cites.org> |
| **LICENSE** | Open access (citation required) |
| **QUALITY_SCORE** | 4.3 |
| **SECTIONS_USED** | 2.4, 5.4 |
| **CITATION** | CITES (2025). CITES Trade Database. |
| **NOTES** | Legal trade only; illegal trade vastly underrepresented |

---

## SECONDARY RESEARCH SOURCES

### DS-PR-001: Barnosky et al. (2011) - Mass Extinction Threshold

| Attribute | Value |
| --------- | ----- |
| **SOURCE_ID** | DS-PR-001 |
| **NAME** | Has the Earth's sixth mass extinction already arrived? |
| **AUTHORS** | Barnosky, A.D., et al. |
| **JOURNAL** | Nature |
| **YEAR** | 2011 |
| **DOI** | 10.1038/nature09678 |
| **TYPE** | Peer-reviewed research |
| **QUALITY_SCORE** | 5.0 |
| **SECTIONS_USED** | 1.1, 1.5 |
| **CITATION** | Barnosky, A.D., et al. (2011). Has the Earth's sixth mass extinction already arrived? Nature, 471(7336), 51-57. |
| **NOTES** | Foundational paper comparing current to historical mass extinctions |

---

### DS-PR-002: Ceballos et al. (2015) - Accelerated Modern Extinction

| Attribute | Value |
| --------- | ----- |
| **SOURCE_ID** | DS-PR-002 |
| **NAME** | Accelerated modern human-induced species losses |
| **AUTHORS** | Ceballos, G., Ehrlich, P.R., et al. |
| **JOURNAL** | Science Advances |
| **YEAR** | 2015 |
| **DOI** | 10.1126/sciadv.1400253 |
| **TYPE** | Peer-reviewed research |
| **QUALITY_SCORE** | 5.0 |
| **SECTIONS_USED** | 1.1, 1.4, 1.5 |
| **CITATION** | Ceballos, G., et al. (2015). Accelerated modern human-induced species losses: Entering the sixth mass extinction. Science Advances, 1(5), e1400253. |
| **NOTES** | 100× background extinction rate estimate; conservative methodology |

---

### DS-PR-003: Ceballos et al. (2017) - Biological Annihilation

| Attribute | Value |
| --------- | ----- |
| **SOURCE_ID** | DS-PR-003 |
| **NAME** | Biological annihilation via the ongoing sixth mass extinction |
| **AUTHORS** | Ceballos, G., Ehrlich, P.R., Dirzo, R. |
| **JOURNAL** | PNAS |
| **YEAR** | 2017 |
| **DOI** | 10.1073/pnas.1704949114 |
| **TYPE** | Peer-reviewed research |
| **QUALITY_SCORE** | 4.8 |
| **SECTIONS_USED** | 1.1, 1.4 |
| **CITATION** | Ceballos, G., et al. (2017). Biological annihilation via the ongoing sixth mass extinction signaled by vertebrate population losses and declines. PNAS, 114(30), E6089-E6096. |
| **NOTES** | Expanded analysis to population declines; "biological annihilation" framing |

---

### DS-PR-004: Dirzo et al. (2014) - Defaunation in the Anthropocene

| Attribute | Value |
| --------- | ----- |
| **SOURCE_ID** | DS-PR-004 |
| **NAME** | Defaunation in the Anthropocene |
| **AUTHORS** | Dirzo, R., et al. |
| **JOURNAL** | Science |
| **YEAR** | 2014 |
| **DOI** | 10.1126/science.1251817 |
| **TYPE** | Peer-reviewed research |
| **QUALITY_SCORE** | 5.0 |
| **SECTIONS_USED** | 1.4, 3.2, 6.x |
| **CITATION** | Dirzo, R., et al. (2014). Defaunation in the Anthropocene. Science, 345(6195), 401-406. |
| **NOTES** | Defines defaunation concept; invertebrate declines highlighted |

---

### DS-PR-005: Bar-On et al. (2018) - Biomass Distribution

| Attribute | Value |
| --------- | ----- |
| **SOURCE_ID** | DS-PR-005 |
| **NAME** | The biomass distribution on Earth |
| **AUTHORS** | Bar-On, Y.M., Phillips, R., Milo, R. |
| **JOURNAL** | PNAS |
| **YEAR** | 2018 |
| **DOI** | 10.1073/pnas.1711842115 |
| **TYPE** | Peer-reviewed research |
| **QUALITY_SCORE** | 5.0 |
| **SECTIONS_USED** | 1.4, 5.x |
| **CITATION** | Bar-On, Y.M., et al. (2018). The biomass distribution on Earth. PNAS, 115(25), 6506-6511. |
| **NOTES** | 83% wild mammal biomass lost; humans + livestock dominate |

---

### DS-PR-006: Hallmann et al. (2017) - German Insect Biomass Decline

| Attribute | Value |
| --------- | ----- |
| **SOURCE_ID** | DS-PR-006 |
| **NAME** | More than 75 percent decline over 27 years in total flying insect biomass |
| **AUTHORS** | Hallmann, C.A., et al. |
| **JOURNAL** | PLoS ONE |
| **YEAR** | 2017 |
| **DOI** | 10.1371/journal.pone.0185809 |
| **TYPE** | Peer-reviewed research |
| **QUALITY_SCORE** | 4.5 |
| **SECTIONS_USED** | 3.2, 6.2 |
| **CITATION** | Hallmann, C.A., et al. (2017). More than 75 percent decline over 27 years in total flying insect biomass in protected areas. PLoS ONE, 12(10), e0185809. |
| **NOTES** | Launched "insect apocalypse" discourse; methodology debates exist |

---

### DS-PR-007: Sánchez-Bayo & Wyckhuys (2019) - Worldwide Insect Decline

| Attribute | Value |
| --------- | ----- |
| **SOURCE_ID** | DS-PR-007 |
| **NAME** | Worldwide decline of the entomofauna: A review of its drivers |
| **AUTHORS** | Sánchez-Bayo, F., Wyckhuys, K.A.G. |
| **JOURNAL** | Biological Conservation |
| **YEAR** | 2019 |
| **DOI** | 10.1016/j.biocon.2019.01.020 |
| **TYPE** | Peer-reviewed review |
| **QUALITY_SCORE** | 4.3 |
| **SECTIONS_USED** | 3.2 |
| **CITATION** | Sánchez-Bayo, F., & Wyckhuys, K.A.G. (2019). Worldwide decline of the entomofauna: A review of its drivers. Biological Conservation, 232, 8-27. |
| **NOTES** | 40% insect species declining; controversial methodology criticisms |

---

### DS-PR-008: Global Tree Assessment (2024)

| Attribute | Value |
| --------- | ----- |
| **SOURCE_ID** | DS-PR-008 |
| **NAME** | State of the World's Trees Report / Global Tree Assessment |
| **AUTHORS** | Botanic Gardens Conservation International (BGCI), IUCN |
| **YEAR** | 2024 |
| **TYPE** | Assessment Report |
| **QUALITY_SCORE** | 5.0 |
| **SECTIONS_USED** | 3.4 |
| **URL** | <https://www.bgci.org/resources/bgci-tools-and-resources/state-of-the-worlds-trees/> |
| **CITATION** | BGCI (2024). State of the World's Trees. |
| **NOTES** | 38% of 47,282 tree species threatened—more than all threatened vertebrates |

---

### DS-PR-009: Hansen et al. (2013) - Global Forest Change

| Attribute | Value |
| --------- | ----- |
| **SOURCE_ID** | DS-PR-009 |
| **NAME** | High-Resolution Global Maps of 21st-Century Forest Cover Change |
| **AUTHORS** | Hansen, M.C., et al. |
| **JOURNAL** | Science |
| **YEAR** | 2013 |
| **DOI** | 10.1126/science.1244693 |
| **TYPE** | Peer-reviewed research + Dataset |
| **QUALITY_SCORE** | 5.0 |
| **SECTIONS_USED** | 2.1, 4.1 |
| **DATA_URL** | <https://glad.umd.edu/dataset/global-forest-change> |
| **CITATION** | Hansen, M.C., et al. (2013). High-Resolution Global Maps of 21st-Century Forest Cover Change. Science, 342(6160), 850-853. |
| **NOTES** | Foundation for Global Forest Watch; Landsat-based 30m resolution |

---

### DS-PR-010: Costanza et al. (2014) - Ecosystem Services Valuation

| Attribute | Value |
| --------- | ----- |
| **SOURCE_ID** | DS-PR-010 |
| **NAME** | Changes in the global value of ecosystem services |
| **AUTHORS** | Costanza, R., et al. |
| **JOURNAL** | Global Environmental Change |
| **YEAR** | 2014 |
| **DOI** | 10.1016/j.gloenvcha.2014.04.002 |
| **TYPE** | Peer-reviewed research |
| **QUALITY_SCORE** | 4.5 |
| **SECTIONS_USED** | 7.1 |
| **CITATION** | Costanza, R., et al. (2014). Changes in the global value of ecosystem services. Global Environmental Change, 26, 152-158. |
| **NOTES** | $125-145 trillion annual ecosystem services value; methodology debates |

---

## DERIVED DATASETS

### DS-DD-001: Unified Extinction Rate Comparison

| Attribute | Value |
| --------- | ----- |
| **SOURCE_ID** | DS-DD-001 |
| **NAME** | Unified Extinction Rate Comparison Dataset |
| **CREATED_BY** | SME Project |
| **STATUS** | Planned |
| **DESCRIPTION** | Synthesized dataset comparing modern extinction rates to Big Five events |
| **INPUT_SOURCES** | DS-PA-001, DS-PR-001, DS-PR-002, paleontological databases |
| **SECTIONS_USED** | 1.1 |
| **METHODOLOGY** | See methods_original_analysis.md in 1.1 |
| **LOCATION** | sections/1.0.../1.1.../data/derived/ |

---

### DS-DD-002: Integrated Defaunation Index

| Attribute | Value |
| --------- | ----- |
| **SOURCE_ID** | DS-DD-002 |
| **NAME** | Global Defaunation Index |
| **CREATED_BY** | SME Project |
| **STATUS** | Planned |
| **DESCRIPTION** | Novel index combining population decline, range contraction, and functional loss |
| **INPUT_SOURCES** | DS-PA-003, DS-PR-004, DS-PR-005, camera trap meta-analyses |
| **SECTIONS_USED** | 1.4 |
| **METHODOLOGY** | See methods_original_analysis.md in 1.4 |
| **LOCATION** | sections/1.0.../1.4.../data/derived/ |

---

### DS-DD-003: Driver Attribution Matrix

| Attribute | Value |
| --------- | ----- |
| **SOURCE_ID** | DS-DD-003 |
| **NAME** | Extinction Driver Attribution Matrix |
| **CREATED_BY** | SME Project |
| **STATUS** | Planned |
| **DESCRIPTION** | Quantified attribution of extinction risk to 5 primary drivers by taxon |
| **INPUT_SOURCES** | DS-PA-001, DS-PA-004, literature review |
| **SECTIONS_USED** | 2.x |
| **METHODOLOGY** | See methods_original_analysis.md in 2.x |
| **LOCATION** | sections/2.0.../data/derived/ |

---

## SOURCE-TO-SECTION MAPPING

### Matrix: Which Sources for Which Sections

| Section | Primary Sources | Secondary Sources | Derived Data |
| ------- | --------------- | ----------------- | ------------ |
| **1.1** | DS-PA-001, DS-PA-002 | DS-PR-001, DS-PR-002 | DS-DD-001 |
| **1.2** | DS-PA-001, DS-PA-002 | - | - |
| **1.3** | DS-PA-003 | DS-PR-003 | - |
| **1.4** | DS-PA-003 | DS-PR-004, DS-PR-005 | DS-DD-002 |
| **1.5** | DS-PA-001 | DS-PR-001, DS-PR-002 | - |
| **2.1** | DS-PA-007 | DS-PR-009 | - |
| **2.2** | DS-PA-001, GISD | - | - |
| **2.3** | UNEP data | Various pollution studies | - |
| **2.4** | DS-PA-009, DS-PA-010 | - | - |
| **2.5** | DS-PA-005 | Climate-extinction literature | - |
| **3.1** | DS-PA-001, AmphibiaWeb | Bd-Maps | - |
| **3.2** | - | DS-PR-006, DS-PR-007 | - |
| **3.3** | DS-PA-001 | IUCN Shark Specialist Group | - |
| **3.4** | DS-PA-001 | DS-PR-008 | - |
| **3.5** | DS-PA-008 | GCRMN | - |
| **4.1** | DS-PA-007 | DS-PR-009 | - |
| **4.2** | DS-PA-003 | Freshwater assessments | - |
| **4.3** | DS-PA-001, DS-PA-006 | Island extinction databases | - |
| **4.4** | Land cover data | Grassland assessments | - |
| **5.x** | Various per topic | Various per topic | - |
| **6.x** | Ecological literature | Case studies | - |
| **7.x** | DS-PA-004 | DS-PR-010 | - |
| **8.x** | WDPA, conservation literature | Case studies | - |
| **9.x** | DS-PA-005 | Modeling literature | - |
| **10.x** | Synthesis of all | Policy literature | - |

---

## DATA CURRENCY LOG

### Verification Schedule

| Source ID | Source Name | Last Verified | Next Check | Status |
| --------- | ----------- | ------------- | ---------- | ------ |
| DS-PA-001 | IUCN Red List | 2025-12-12 | 2026-01-15 | Current |
| DS-PA-002 | IUCN Guidelines | 2025-12-12 | 2026-06-01 | Current |
| DS-PA-003 | Living Planet Index | 2025-12-12 | 2026-10-01 | Current |
| DS-PA-004 | IPBES Global | 2025-12-12 | 2026-12-01 | Current |
| DS-PA-005 | IPCC AR6 | 2025-12-12 | 2027-01-01 | Current |
| DS-PA-006 | GBIF | 2025-12-12 | 2026-01-15 | Current |
| DS-PA-007 | Global Forest Watch | 2025-12-12 | 2026-01-15 | Current |
| DS-PA-008 | Coral Reef Watch | 2025-12-12 | 2026-01-15 | Current |
| DS-PA-009 | FAO Fisheries | 2025-12-12 | 2026-01-15 | Current |
| DS-PA-010 | CITES Trade | 2025-12-12 | 2026-01-15 | Current |

---

## ACCESS PROTOCOLS

### API Access Configuration

```yaml
# IUCN Red List API
iucn:
  base_url: "https://apiv3.iucnredlist.org/api/v3"
  auth: "token"
  rate_limit: "100 requests/day (basic)"
  docs: "https://apiv3.iucnredlist.org/api/v3/docs"

# GBIF API
gbif:
  base_url: "https://api.gbif.org/v1"
  auth: "optional (higher limits with account)"
  rate_limit: "varies"
  docs: "https://www.gbif.org/developer/summary"

# Global Forest Watch
gfw:
  base_url: "https://data-api.globalforestwatch.org"
  auth: "API key"
  docs: "https://www.globalforestwatch.org/help/developers/"
```

### Data Download Locations

| Source | Download Method | Storage Location |
| ------ | --------------- | ---------------- |
| IUCN bulk | Request via website | `/data/external/iucn/` |
| LPI database | Request form | `/data/external/lpi/` |
| GBIF | DOI-citable downloads | `/data/external/gbif/` |
| GFW | Direct download | `/data/external/gfw/` |
| Research papers | PDF + supplementary | `/data/external/papers/` |

---

## VERSION HISTORY

| Version | Date | Changes | Author |
| ------- | ---- | ------- | ------ |
| 1.0 | 2025-12-12 | Initial creation with 10 primary, 10 research sources | Dennis 'dnoice' Smaltz |

---

> **︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!**
