<!--
================================================================================
Title:              Technical Supplement - Section 1.1
File Name:          technical_supplement.md
Relative Path:      sections/1.0.../1.1.../technical_supplement.md
Artifact Type:      Documentation/Technical Reference
Version:            0.1 (Template)
Date:               2025-12-12
Update:             Initial Template Creation
Author:             Dennis 'dnoice' Smaltz
A.I. Acknowledgement: Claude Opus 4
Signature:          ︻デ═—··· 🎯 = Aim Twice, Shoot Once!
================================================================================

DESCRIPTION:
Extended technical documentation for Section 1.1: Defining Mass Extinction.
Contains detailed mathematical derivations, extended data tables, supplementary
figures, code documentation, and additional technical context not suitable
for the main article.

KEY FEATURES:
1. Complete mathematical derivations
2. Extended data tables
3. Supplementary figures and analyses
4. Detailed code documentation
5. Glossary of technical terms

USAGE:
- Reference for deep technical understanding
- Support document for peer review
- Resource for reproducing and extending analysis

================================================================================
-->

# TECHNICAL SUPPLEMENT
## Section 1.1: Defining Mass Extinction

---

## TABLE OF CONTENTS

1. [Mathematical Foundations](#1-mathematical-foundations)
2. [Extended Data Tables](#2-extended-data-tables)
3. [Supplementary Figures](#3-supplementary-figures)
4. [Code Documentation](#4-code-documentation)
5. [Glossary](#5-glossary)
6. [References](#6-references)

---

## 1. MATHEMATICAL FOUNDATIONS

### 1.1 Extinction Rate Metrics

#### 1.1.1 E/MSY (Extinctions per Million Species-Years)

**Definition**: The number of extinctions expected per million species over one million years.

**Standard Formulation**:

$$
E/MSY = \frac{E}{N \times T}
$$

Where:
- $E$ = Number of extinctions observed
- $N$ = Number of species in the taxon
- $T$ = Time period in millions of years

**Alternative Formulation** (for short time periods):

$$
E/MSY = \frac{E \times 10^6}{N \times T_{years}}
$$

Where $T_{years}$ is the time period in years.

---

#### 1.1.2 Background Extinction Rate Estimation

**Fossil Record Approach**:

The background extinction rate is typically estimated from the fossil record using:

$$
\mu_{background} = \frac{1}{D}
$$

Where $D$ is the average species duration in millions of years.

**Empirical Estimates**:

| Taxon | Average Duration (MY) | Implied E/MSY |
|-------|----------------------|---------------|
| Marine invertebrates | 5-10 | 0.1-0.2 |
| Mammals | 1-2 | 0.5-1.0 |
| Birds | 2-3 | 0.33-0.5 |
| All taxa (average) | 1-10 | 0.1-1.0 |

**Consensus Estimate**: 0.1-1.0 E/MSY (often cited as ~1 E/MSY for vertebrates)

---

#### 1.1.3 Current Extinction Rate Calculation

**Documented Extinctions Method**:

$$
E_{current} = \frac{E_{documented}}{N_{assessed}} \times \frac{10^6}{T_{years}}
$$

**Example Calculation** (vertebrates since 1900):
- $E_{documented}$ = ~477 species (IUCN documented)
- $N_{assessed}$ = ~80,000 vertebrate species
- $T_{years}$ = 125 years (1900-2025)

$$
E_{current} = \frac{477}{80,000} \times \frac{10^6}{125} = 47.7 \text{ E/MSY}
$$

---

### 1.2 Mass Extinction Thresholds

#### 1.2.1 Historical Mass Extinction Metrics

| Event | Age (Ma) | Duration (MY) | Species Loss (%) | E/MSY (estimated) |
|-------|----------|---------------|------------------|-------------------|
| End-Ordovician | 443 | ~1-2 | 85% | ~100-200 |
| Late Devonian | 372-359 | ~10-15 | 75% | ~20-50 |
| End-Permian | 252 | ~0.06-0.2 | 96% | ~1,000-10,000 |
| End-Triassic | 201 | ~0.1-0.6 | 76% | ~200-1,000 |
| End-Cretaceous | 66 | ~0.001-0.1 | 76% | ~1,000-100,000 |

**Note**: E/MSY estimates for past events are highly uncertain due to incomplete fossil record and dating uncertainties.

---

#### 1.2.2 Threshold Definitions

**Raup & Sepkoski (1982)** threshold for "mass extinction":
- Loss of >75% of species
- Occurring in geologically "short" time (<2 MY)

**Barnosky et al. (2011)** modern comparison criteria:
- Rate comparison: Modern rate exceeding 80× Big Five background
- Cumulative loss: Trajectory toward 75% loss within 300-3,000 years

---

### 1.3 Species-Area Relationships and Extinction Prediction

#### 1.3.1 Classic Species-Area Relationship

$$
S = cA^z
$$

Where:
- $S$ = Number of species
- $A$ = Area
- $c$ = Constant (varies by taxon and region)
- $z$ = Exponent (typically 0.15-0.35)

#### 1.3.2 Extinction from Habitat Loss

**First-order approximation**:

$$
S_{remaining} = S_{original} \times \left(\frac{A_{remaining}}{A_{original}}\right)^z
$$

**Extinction fraction**:

$$
E_{fraction} = 1 - \left(\frac{A_{remaining}}{A_{original}}\right)^z
$$

**Example**: If 90% of habitat is lost and z = 0.25:

$$
E_{fraction} = 1 - (0.1)^{0.25} = 1 - 0.562 = 0.438 = 43.8\%
$$

---

### 1.4 Extinction Debt Calculation

**Concept**: Species that are "committed to extinction" due to habitat loss but haven't yet gone extinct.

**Relaxation Time Model**:

$$
S(t) = S_{equilibrium} + (S_{initial} - S_{equilibrium}) \times e^{-t/\tau}
$$

Where:
- $S(t)$ = Species at time $t$
- $S_{equilibrium}$ = Ultimate species number at new habitat level
- $S_{initial}$ = Species at time of habitat loss
- $\tau$ = Relaxation time constant

**Extinction Debt**:

$$
D = S_{initial} - S_{equilibrium}
$$

---

### 1.5 Population Viability and Extinction Probability

#### 1.5.1 Minimum Viable Population (MVP)

**Definition**: Smallest population size with >95% probability of surviving 100 years.

**Empirical estimates**: Typically 500-5,000 individuals depending on taxon.

#### 1.5.2 Extinction Probability Models

**Simple exponential model**:

$$
P_{extinction}(t) = 1 - e^{-\lambda t}
$$

Where $\lambda$ is the extinction rate parameter.

**Population-dependent model** (stochastic):

$$
P_{extinction}(t) \approx 1 - \left(1 - \frac{1}{N}\right)^{r \cdot t}
$$

Where:
- $N$ = Population size
- $r$ = Intrinsic growth rate
- $t$ = Time

---

## 2. EXTENDED DATA TABLES

### Table S1: Comprehensive Extinction Rate Estimates from Literature

| Study | Taxa | Time Period | Rate (E/MSY) | Method | Notes |
|-------|------|-------------|--------------|--------|-------|
| Pimm et al. 1995 | Birds | 1600-1994 | 100 | Documented | |
| May et al. 1995 | All species | Current | 100-1,000 | Estimated | |
| Barnosky et al. 2011 | Vertebrates | Since 1500 | 24-100 | Documented | Conservative |
| Ceballos et al. 2015 | Vertebrates | Since 1900 | 100 | Documented | Conservative |
| De Vos et al. 2015 | Vertebrates | Current | 1,000 | Modeled | Higher estimate |
| Pimm et al. 2014 | All species | Current | 1,000 | Estimated | |

---

### Table S2: Big Five Mass Extinctions - Detailed Metrics

| Event | Start (Ma) | End (Ma) | Duration (MY) | Marine Loss (%) | Terrestrial Loss (%) | Primary Cause(s) |
|-------|------------|----------|---------------|-----------------|---------------------|------------------|
| End-Ordovician | 445 | 443 | ~2 | 85 | N/A | Glaciation, anoxia |
| Late Devonian | 375 | 359 | ~16 | 75 | ~70 | Anoxia, climate |
| End-Permian | 252.2 | 252.0 | 0.06-0.2 | 96 | 70 | Volcanism, warming |
| End-Triassic | 201.5 | 201.4 | ~0.1 | 76 | 50 | Volcanism, CO₂ |
| End-Cretaceous | 66.04 | 66.00 | ~0.04 | 76 | 75 | Asteroid, volcanism |

---

### Table S3: IUCN Red List Category Quantitative Thresholds

| Category | Population Decline (A) | Range Size (B) | Population Size (C) | Quantitative Analysis (E) |
|----------|------------------------|----------------|---------------------|---------------------------|
| **Critically Endangered** | ≥80-90% in 10 yrs/3 gen | EOO <100 km², AOO <10 km² | <250 mature individuals | >50% in 10 yrs/3 gen |
| **Endangered** | ≥50-70% in 10 yrs/3 gen | EOO <5,000 km², AOO <500 km² | <2,500 mature individuals | >20% in 20 yrs/5 gen |
| **Vulnerable** | ≥30-50% in 10 yrs/3 gen | EOO <20,000 km², AOO <2,000 km² | <10,000 mature individuals | >10% in 100 yrs |

---

### Table S4: Taxonomic Coverage in IUCN Red List (v2025-2)

| Taxonomic Group | Species Described | Species Assessed | % Assessed | Threatened | % Threatened |
|-----------------|-------------------|------------------|------------|------------|--------------|
| Mammals | ~6,500 | 6,025 | 93% | 1,625 | 27% |
| Birds | ~11,200 | 11,185 | 99.9% | 1,286 | 11.5% |
| Reptiles | ~12,000 | 10,196 | 85% | 2,141 | 21% |
| Amphibians | ~8,500 | 8,009 | 94% | 3,284 | 41% |
| Fishes | ~35,000 | 25,000+ | ~71% | 6,250+ | 25%+ |
| Insects | ~1,000,000 | ~12,000 | ~1.2% | ~5,000 | ~40% |
| Plants | ~400,000 | ~60,000 | ~15% | ~25,000 | ~42% |

---

## 3. SUPPLEMENTARY FIGURES

### Figure S1: [Placeholder - Extinction Rate Through Time]

**Description**: Time series showing extinction rates from Cambrian to present, with Big Five events marked.

**Data Source**: Paleobiology Database, IUCN Red List

**File**: `figures/fig_1.1_S01_extinction_rate_timeseries.png`

---

### Figure S2: [Placeholder - Rate Comparison Across Methods]

**Description**: Comparison of extinction rate estimates using different methodologies.

**File**: `figures/fig_1.1_S02_method_comparison.png`

---

### Figure S3: [Placeholder - Sensitivity Analysis Results]

**Description**: Tornado plot showing sensitivity of extinction rate estimates to key parameters.

**File**: `figures/fig_1.1_S03_sensitivity_tornado.png`

---

## 4. CODE DOCUMENTATION

### 4.1 Core Functions

#### `calculate_extinction_rate()`

```python
def calculate_extinction_rate(
    extinctions: int,
    species_count: float,
    time_period: float,
    time_unit: str = 'years'
) -> float:
    """
    Calculate extinction rate in E/MSY.

    Parameters
    ----------
    extinctions : int
        Number of documented extinctions
    species_count : float
        Total species in taxon/region
    time_period : float
        Duration of observation period
    time_unit : str
        'years' or 'million_years'

    Returns
    -------
    float
        Extinction rate in E/MSY (extinctions per million species-years)

    Examples
    --------
    >>> calculate_extinction_rate(477, 80000, 125, 'years')
    47.7

    >>> calculate_extinction_rate(477, 80000, 0.000125, 'million_years')
    47.7
    """
    if time_unit == 'years':
        time_my = time_period / 1e6
    else:
        time_my = time_period

    return extinctions / (species_count * time_my)
```

---

#### `compare_to_background()`

```python
def compare_to_background(
    current_rate: float,
    background_rate: float = 1.0
) -> dict:
    """
    Compare current extinction rate to background rate.

    Parameters
    ----------
    current_rate : float
        Current extinction rate in E/MSY
    background_rate : float
        Background extinction rate in E/MSY (default: 1.0)

    Returns
    -------
    dict
        Dictionary with comparison metrics

    Examples
    --------
    >>> compare_to_background(100, 1.0)
    {'ratio': 100.0, 'excess': 99.0, 'description': '100x background'}
    """
    ratio = current_rate / background_rate
    excess = current_rate - background_rate

    return {
        'ratio': ratio,
        'excess': excess,
        'description': f'{ratio:.0f}x background'
    }
```

---

### 4.2 Data Processing Pipeline

```python
# Pipeline overview (see notebooks for full implementation)

# Step 1: Load raw data
raw_iucn = load_iucn_data('data/raw/iucn/')
raw_paleo = load_paleo_data('data/raw/paleo/')

# Step 2: Clean and validate
clean_iucn = clean_iucn_data(raw_iucn)
clean_paleo = clean_paleo_data(raw_paleo)

# Step 3: Calculate rates
modern_rate = calculate_modern_extinction_rate(clean_iucn)
paleo_rates = calculate_paleo_extinction_rates(clean_paleo)

# Step 4: Compare and synthesize
comparison = compare_rates(modern_rate, paleo_rates)

# Step 5: Generate outputs
generate_figures(comparison, output_dir='figures/')
export_results(comparison, output_dir='data/derived/')
```

---

## 5. GLOSSARY

### Key Terms

| Term | Definition |
|------|------------|
| **AOO** | Area of Occupancy - the area within a species' extent of occurrence that is actually occupied |
| **Background extinction** | The normal, continuous rate of species extinction that occurs in absence of mass extinction events |
| **E/MSY** | Extinctions per Million Species-Years - standard metric for comparing extinction rates |
| **EOO** | Extent of Occurrence - the smallest area that encompasses all known occurrences of a species |
| **Extinction debt** | Future extinctions that are committed due to past habitat loss but haven't yet occurred |
| **Functional extinction** | When a species population is too small to perform its ecological role, even if not technically extinct |
| **Mass extinction** | A widespread and rapid decrease in biodiversity, typically defined as >75% species loss in geological "short" time |
| **MVP** | Minimum Viable Population - smallest population size with acceptable probability of survival |
| **Relaxation time** | Time required for an ecosystem to reach new equilibrium after disturbance |

### Abbreviations

| Abbreviation | Full Term |
|--------------|-----------|
| CR | Critically Endangered (IUCN category) |
| EN | Endangered (IUCN category) |
| EW | Extinct in the Wild (IUCN category) |
| EX | Extinct (IUCN category) |
| GBIF | Global Biodiversity Information Facility |
| IUCN | International Union for Conservation of Nature |
| LPI | Living Planet Index |
| Ma | Millions of years ago |
| MY | Million years |
| VU | Vulnerable (IUCN category) |

---

## 6. REFERENCES

### Primary Sources

1. Barnosky, A.D., et al. (2011). Has the Earth's sixth mass extinction already arrived? *Nature*, 471(7336), 51-57. https://doi.org/10.1038/nature09678

2. Ceballos, G., et al. (2015). Accelerated modern human-induced species losses: Entering the sixth mass extinction. *Science Advances*, 1(5), e1400253. https://doi.org/10.1126/sciadv.1400253

3. IUCN (2025). The IUCN Red List of Threatened Species. Version 2025-2. https://www.iucnredlist.org

4. Pimm, S.L., et al. (2014). The biodiversity of species and their rates of extinction, distribution, and protection. *Science*, 344(6187), 1246752. https://doi.org/10.1126/science.1246752

5. Raup, D.M., & Sepkoski, J.J. (1982). Mass extinctions in the marine fossil record. *Science*, 215(4539), 1501-1503.

### Methodology References

6. IUCN Standards and Petitions Committee (2024). Guidelines for Using the IUCN Red List Categories and Criteria. Version 16. https://www.iucnredlist.org/resources/redlistguidelines

7. De Vos, J.M., et al. (2015). Estimating the normal background rate of species extinction. *Conservation Biology*, 29(2), 452-462.

---

## VERSION HISTORY

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 0.1 | 2025-12-12 | Initial template | Dennis 'dnoice' Smaltz |

---

*︻デ═—··· 🎯 = Aim Twice, Shoot Once!*
