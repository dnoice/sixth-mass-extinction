<!--
✒ Metadata
    - Title: Major & Minor Mathematical Models Reference (SME Edition - v2.1)
    - File Name: major_minor_mathematical_models.md
    - Relative Path: docs/references/major_minor_mathematical_models.md
    - Artifact Type: docs
    - Version: 2.1.0
    - Date: 2025-01-04
    - Update: Saturday, January 04, 2025
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Anthropic - Claude Opus 4.5
    - Signature:  ︻デ═—··· 🎯 = Aim Twice, Shoot Once!
    - Research Verification: Methodology confirmed against IUCN Guidelines v16 (March 2024) and foundational literature

✒ Description:
    Comprehensive reference document covering the mathematical and statistical foundations
    of extinction science. Includes extinction rate calculations, population viability
    analysis, species-area relationships, island biogeography theory, population dynamics
    models, Red List Index methodology, projection methods, and uncertainty quantification.
    Essential resource for quantitative biodiversity research and extinction risk modeling.

✒ Key Features:
    - Feature 1: Extinction rate calculations and E/MSY metric
    - Feature 2: Background extinction rate estimation methods
    - Feature 3: Species-area relationship models and applications
    - Feature 4: Population viability analysis (PVA) frameworks
    - Feature 5: Minimum viable population (MVP) theory
    - Feature 6: IUCN Red List criteria mathematical basis
    - Feature 7: Red List Index calculation methodology
    - Feature 8: Species distribution modeling approaches
    - Feature 9: Projection models and uncertainty quantification
    - Feature 10: Statistical methods for biodiversity assessment

✒ Usage Instructions:
    This document serves as the quantitative reference for mathematical
    approaches within the Sixth Mass Extinction (SME) research framework.

    How to use:
        1. Navigate via Table of Contents to specific mathematical topics
        2. Reference formulas for extinction rate calculations
        3. Apply species-area relationships for habitat analysis
        4. Use PVA frameworks for conservation planning
        5. Understand Red List criteria quantitative thresholds
        6. Apply projection methods for future scenarios

✒ Examples:
    - Example 1: Calculate extinction rate from fossil data → Section 2.2
    - Example 2: Estimate species loss from habitat reduction → Section 3
    - Example 3: Assess population viability → Section 5
    - Example 4: Understand Red List criteria → Section 6
    - Example 5: Apply species distribution modeling → Section 7
    - Example 6: Project future extinctions → Section 8

✒ Other Important Information:
    - Dependencies: None (standalone reference document)
    - Compatible platforms: Any Markdown renderer (LaTeX formulas may need extension)
    - Related documents: major_minor_extinction_events.md, major_minor_current_status.md
    - Data sources: Conservation biology literature, IUCN methodology documents,
                    population biology textbooks, ecological modeling papers
    - Update frequency: As new methodologies are developed
    - Mathematical notation: Standard LaTeX-style where possible
    - Complexity note: Some sections require background in statistics/ecology
---------
-->

# 📐 Major & Minor Mathematical Models Reference

## Sixth Mass Extinction (SME) Project - Quantitative Foundations of Extinction Science

> **Mathematical Context:** The assertion that we are in a mass extinction relies on rigorous
> quantification—comparing current extinction rates to historical baselines, projecting
> future losses from habitat relationships, and modeling population trajectories. This
> document provides the mathematical foundations underlying extinction science.

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Extinction Rate Calculations](#2-extinction-rate-calculations)
   - [2.1 Defining Extinction Rate](#21-defining-extinction-rate)
   - [2.2 Background Extinction Rate](#22-background-extinction-rate)
   - [2.3 Current Rate Estimation](#23-current-rate-estimation)
   - [2.4 Rate Comparison Methods](#24-rate-comparison-methods)
3. [Species-Area Relationships](#3-species-area-relationships)
   - [3.1 Classic Power Law Model](#31-classic-power-law-model)
   - [3.2 Parameter Estimation](#32-parameter-estimation)
   - [3.3 Extinction Debt](#33-extinction-debt)
   - [3.4 Applications and Limitations](#34-applications-and-limitations)
4. [Island Biogeography Theory](#4-island-biogeography-theory)
   - [4.1 MacArthur-Wilson Model](#41-macarthur-wilson-model)
   - [4.2 Equilibrium Theory](#42-equilibrium-theory)
   - [4.3 Applications to Habitat Fragments](#43-applications-to-habitat-fragments)
5. [Population Viability Analysis](#5-population-viability-analysis)
   - [5.1 Minimum Viable Population (MVP)](#51-minimum-viable-population-mvp)
   - [5.2 Population Growth Models](#52-population-growth-models)
   - [5.3 Stochastic Models](#53-stochastic-models)
   - [5.4 PVA Software and Methods](#54-pva-software-and-methods)
6. [IUCN Red List Criteria](#6-iucn-red-list-criteria)
   - [6.1 Quantitative Thresholds](#61-quantitative-thresholds)
   - [6.2 Criterion A: Population Reduction](#62-criterion-a-population-reduction)
   - [6.3 Criterion B: Geographic Range](#63-criterion-b-geographic-range)
   - [6.4 Criterion C: Small Population](#64-criterion-c-small-population)
   - [6.5 Criterion D: Very Small Population](#65-criterion-d-very-small-population)
   - [6.6 Criterion E: Quantitative Analysis](#66-criterion-e-quantitative-analysis)
7. [Red List Index](#7-red-list-index)
   - [7.1 Index Calculation](#71-index-calculation)
   - [7.2 Interpretation](#72-interpretation)
   - [7.3 Disaggregated Indices](#73-disaggregated-indices)
8. [Species Distribution Modeling](#8-species-distribution-modeling)
   - [8.1 Ecological Niche Models](#81-ecological-niche-models)
   - [8.2 Climate Envelope Models](#82-climate-envelope-models)
   - [8.3 Model Validation](#83-model-validation)
9. [Projection Methods](#9-projection-methods)
   - [9.1 Scenario-Based Projections](#91-scenario-based-projections)
   - [9.2 Time-to-Extinction Models](#92-time-to-extinction-models)
   - [9.3 Uncertainty Quantification](#93-uncertainty-quantification)
10. [Statistical Methods](#10-statistical-methods)
    - [10.1 Biodiversity Metrics](#101-biodiversity-metrics)
    - [10.2 Trend Detection](#102-trend-detection)
    - [10.3 Sampling and Extrapolation](#103-sampling-and-extrapolation)
11. [Key Formulas Reference](#11-key-formulas-reference)
12. [Data Sources & References](#12-data-sources--references)

---

## 1. Executive Summary

### Core Mathematical Findings

| Calculation | Result | Confidence |
|-------------|--------|------------|
| **Background extinction rate** | 0.1–2.0 E/MSY | Moderate |
| **Current extinction rate** | 100–1,000 E/MSY | High |
| **Rate multiple** | 100–1,000× background | High |
| **Species-area exponent (z)** | 0.15–0.35 | Well-established |
| **MVP (general)** | 500–5,000 individuals | Context-dependent |
| **Time to 75% loss (BAU)** | 240–540 years | Model-dependent |

### Key Mathematical Relationships

**Extinction Rate (E/MSY):**

```math
E/MSY = (Extinctions / Total Species) × 1,000,000 / Time (years)
```

**Species-Area Relationship:**

```math
S = cA^z
```

**Where**

```math
S = species, A = area, c = constant, z = 0.15–0.35
```

**Population Growth (Exponential):**

```math
N(t) = N₀ × e^(rt)
```

**Where**

```math
N = population, r = growth rate, t = time
```

---

## 2. Extinction Rate Calculations

### 2.1 Defining Extinction Rate

#### Basic Metrics

**Absolute Extinction Rate:**

```math
E_abs = Number of extinctions / Time interval
```

**Proportional Extinction Rate:**

```math
E_prop = (Number of extinctions / Total species) × 100%
```

**Per-Species Rate (instantaneous):**

```math
μ = -ln(1 - E_prop) / t
```

#### Standard Metric: E/MSY

**Extinctions per Million Species-Years (E/MSY):**

```math
E/MSY = (E / S) × 10⁶ / t
```

**Where**

```math
E = number of extinctions
S = total species (at start or average)
t = time in years
10⁶ = scaling to per-million
```

**Example Calculation:**

```math
If 100 extinctions occur among 10,000 species over 100 years:
```

```math
E/MSY = (100 / 10,000) × 10⁶ / 100
      = 0.01 × 10⁶ / 100
      = 100 E/MSY
```

### 2.2 Background Extinction Rate

#### Fossil Record Estimates

**Method 1: Marine Invertebrate Fossils (Sepkoski)**

| Era | Duration (Myr) | Families | Extinction Rate |
| ----- | ---------------- | ---------- | ----------------- |
| Cambrian | 54 | Variable | 4.6 families/Myr |
| Ordovician | 43 | Variable | 2.7 families/Myr |
| Silurian | 24 | Variable | 1.7 families/Myr |
| Average Phanerozoic | — | — | 2–5 families/Myr |

**Species-to-Family Conversion:**

Using ~100 species per family:

```math
Background = 2–5 families/Myr × 100 species/family / 10⁶ species
           = 0.2–0.5 E/MSY (at family level extrapolated)
```

**Method 2: Mammal Fossil Record**

| Metric | Value |
|--------|-------|
| Average mammal species lifespan | 1–2 million years |
| Background rate | 0.5–2.0 E/MSY |
| Best estimate | ~0.25 E/MSY for mammals |

**Method 3: Modern Lineage Analysis**

Using molecular clocks and species lifespan estimates:

```math
Background ≈ 0.1–1.0 E/MSY
```

**Consensus Background Rate:**

```math
0.1–2.0 E/MSY (typically ~1 E/MSY cited)
```

### 2.3 Current Rate Estimation

#### Method 1: Direct Documentation

**Known Extinctions Since 1900:**

| Group | Documented Extinctions | Species | E/MSY |
|-------|----------------------|---------|-------|
| Mammals | 80+ | 6,000 | 100+ |
| Birds | 150+ | 10,000 | 120+ |
| Amphibians | 35+ | 8,000 | 35+ |
| Fish | 70+ | 35,000 | 16+ |
| Plants | 570+ | 400,000 | 11+ |

**Note:** Documented extinctions are severe undercounts

#### Method 2: Species-Area Extrapolation

**Habitat Loss Approach:**

**Using**

```math
S = cA^z
```

**with**

```math
z = 0.25:
```

```math
Species lost = S_original × [1 - (A_remaining/A_original)^z]
```

**Tropical Forest Example:**

If 50% of tropical forest lost:

```math
Relative species remaining = (0.5)^0.25 = 0.84
Species lost ≈ 16%
```

Applied to estimated species:

```math
If tropical forests hold 5 million species:
Species lost ≈ 800,000 (over deforestation period)
```

#### Method 3: Red List Extrapolation

**From IUCN Assessments:**

```math
Extinction probability per year =
  Σ (species in category × probability) / total species
```

**Where probability by category:**

```math
CR: 0.01–0.10 per year
EN: 0.001–0.01 per year
VU: 0.0001–0.001 per year
```

**Estimated Current Rate:**

```math
100–1,000 E/MSY (depending on taxonomic group and method)
```

### 2.4 Rate Comparison Methods

#### Rate Ratio

**Current/Background Ratio:**

```math
R = E_current / E_background
  = (100–1,000 E/MSY) / (0.1–2.0 E/MSY)
  = 100–1,000×
```

#### Statistical Significance Testing

**Null Hypothesis:**

```math
H₀: Current rate = background rate
```

**Test:** Poisson or negative binomial regression comparing observed vs. expected extinctions

**Result:**

```math
p << 0.001 (highly significant difference)
```

#### Confidence Intervals

**Bootstrap Method:**

1. Resample extinction data
2. Recalculate rate each iteration
3. Determine 95% CI from distribution

**Typical CI:**

```math
Current rate: 100–1,000× background (95% CI)
```

---

## 3. Species-Area Relationships

### 3.1 Classic Power Law Model

#### The Equation

**Power Law (Arrhenius, 1921):**

```math
S = cA^z
```

**Where**

```math
S = number of species
A = area
c = constant (varies by taxon/region)
z = exponent (typically 0.15–0.35)
```

**Log-Linear Form:**

```math
log(S) = log(c) + z × log(A)
```

This linearizes the relationship for regression analysis.

#### The z-Value

**Typical Values:**

| Context | z-Value | Notes |
|---------|---------|-------|
| Oceanic islands | 0.25–0.35 | Higher isolation |
| Continental regions | 0.10–0.20 | Connected landscapes |
| Habitat fragments | 0.20–0.30 | Depends on isolation |
| Global synthesis | ~0.25 | Commonly used default |

#### Biological Interpretation

- **z < 0.15:** Low turnover between areas; species shared widely
- **z = 0.25:** Typical island pattern; moderate isolation
- **z > 0.35:** High turnover; strong isolation effects

### 3.2 Parameter Estimation

#### Regression Method

**Ordinary Least Squares (log-log):**

```math
log(S_i) = a + z × log(A_i) + ε_i
```

**Where**

```math
a = log(c)
z = slope
ε = error term
```

**Parameter Estimates:**

```math
z = Σ[(log(A_i) - mean(log(A))) × (log(S_i) - mean(log(S)))] /
    Σ[(log(A_i) - mean(log(A)))²]
```

```math
c = exp[mean(log(S)) - z × mean(log(A))]
```

#### Maximum Likelihood

**Assuming Poisson-distributed species counts:**

```math
L(c, z | data) = Π P(S_i | cA_i^z)
```

Maximize log-likelihood for parameter estimates.

#### Bayesian Approaches

**Prior distributions:**

```math
z ~ Normal(0.25, 0.1)  [informed prior]
c ~ Lognormal(μ, σ)    [taxon-specific]
```

**Posterior inference** via MCMC sampling.

### 3.3 Extinction Debt

#### Concept

Species loss from habitat reduction occurs with a time lag—the **extinction debt**.

**Relaxation Model:**

```math
S(t) = S_final + (S_initial - S_final) × e^(-t/τ)
```

**Where**

```math
S_initial = species immediately after habitat loss
S_final = equilibrium species for new area
τ = relaxation time constant (often decades to centuries)
```

#### Calculating Extinction Debt

**Debt = Species present - Equilibrium species**

```math
Debt = S_observed - cA_current^z
```

**Example:**

If a 1000 km² forest is reduced to 100 km²:

```math
Original: S₁ = c × 1000^0.25
Equilibrium: S₂ = c × 100^0.25
Ratio: S₂/S₁ = (100/1000)^0.25 = 0.56
```

So 44% of species eventually lost, but many persist initially.

#### Relaxation Time Estimates

| Taxon | Relaxation Time |
|-------|-----------------|
| Insects | Years–decades |
| Birds | Decades |
| Plants | Decades–centuries |
| Trees | Centuries |

### 3.4 Applications and Limitations

#### Applications

1. **Predicting extinction from habitat loss**
2. **Reserve design** (SLOSS debate)
3. **Estimating regional biodiversity**
4. **Climate change projections**

#### Limitations

| Limitation | Impact |
|------------|--------|
| Assumes equilibrium | May not apply during rapid change |
| Scale-dependent | z varies with scale of analysis |
| Ignores habitat quality | Area ≠ carrying capacity |
| Edge effects | Fragments differ from intact areas |
| Dispersal limitation | Isolation effects vary |

#### Improved Models

**Endemic-Area Relationship:**

```math
E = cA^z_E
```

**Where**

```math
E = endemic species, z_E < z (endemics more sensitive)
```

**Countryside SAR:**
Incorporates matrix quality between habitat patches

---

## 4. Island Biogeography Theory

### 4.1 MacArthur-Wilson Model

#### Core Concept

Species richness on islands determined by balance between:
- **Immigration (I):** colonization of new species
- **Extinction (E):** local extinction on island

#### Immigration Rate

```math
I = I_max × (1 - S/P)
```

**Where**

```math
I_max = maximum immigration rate (when S = 0)
S = current species on island
P = mainland species pool
```

Immigration decreases as more species present (fewer new colonizers possible)

#### Extinction Rate

```math
E = E_max × (S/P)
```

**Where**

```math
E_max = maximum extinction rate (when S = P)
```

Extinction increases with more species (smaller populations each)

### 4.2 Equilibrium Theory

#### Equilibrium Species Richness

At equilibrium: I = E

**Solving:**

```math
I_max × (1 - S*/P) = E_max × (S*/P)
```

```math
S* = P × I_max / (I_max + E_max)
```

#### Island Size Effect

**Larger islands:**
- Lower extinction rates (larger populations)
- Higher equilibrium S*

**Mathematical form:**

```math
E_max ∝ A^(-α)
```

**Where**

```math
extinction decreases with area
```

#### Distance Effect

**More isolated islands:**
- Lower immigration rates
- Lower equilibrium S*

**Mathematical form:**

```math
I_max ∝ D^(-β)
```

**Where**

```math
immigration decreases with distance
```

### 4.3 Applications to Habitat Fragments

#### Fragments as Islands

**Key insight:** Habitat fragments in a developed matrix behave like islands.

**Matrix effects:**
- Hostile matrix = greater isolation
- Permeable matrix = more connectivity

#### Metapopulation Extensions

**Levins Metapopulation Model:**

```math
dp/dt = cp(1 - p) - ep
```

**Where**

```math
p = proportion of patches occupied
c = colonization rate
e = extinction rate
```

**Equilibrium:**

```math
p* = 1 - e/c
```

If e > c, metapopulation goes extinct.

---

## 5. Population Viability Analysis

### 5.1 Minimum Viable Population (MVP)

#### Definition

**MVP:** Smallest population with acceptable probability of persistence over a defined time horizon.

**Standard Criteria:**
- 99% probability of persistence for 100 years
- 95% probability of persistence for 40 generations
- Various other definitions used

#### Classic Estimates

**Franklin's Rule (1980):**

```math
N_e = 50 (avoid inbreeding depression)
N_e = 500 (maintain evolutionary potential)
```

**Where**

```math
N_e = effective population size
```

**Effective-to-Census Ratio:**

```math
N_e ≈ 0.10–0.25 × N
```

So census population needs:

```math
N = 200–500 for short-term (from N_e = 50)
N = 2,000–5,000 for long-term (from N_e = 500)
```

#### Modern MVP Analysis

**Meta-analysis (Traill et al. 2007):**

```math
Median MVP ≈ 4,169 individuals
Range: 1,000–10,000+ depending on species
```

**Factors Affecting MVP:**

| Factor | Effect on MVP |
|--------|---------------|
| Reproductive rate | Higher r → lower MVP |
| Environmental variance | Higher σ² → higher MVP |
| Catastrophe frequency | More frequent → higher MVP |
| Generation time | Longer → higher MVP |
| Body size | Larger → higher MVP |
| Habitat specialization | More specialized → higher MVP |

### 5.2 Population Growth Models

#### Exponential Growth

**Basic Model:**

```math
dN/dt = rN
```

**Solution:**

```math
N(t) = N₀e^(rt)
```

**Where**

```math
N = population size
r = intrinsic growth rate
r = b - d (births - deaths)
```

#### Logistic Growth

**Density-Dependent Model:**

```math
dN/dt = rN(1 - N/K)
```

**Solution:**

```math
N(t) = K / [1 + ((K-N₀)/N₀)e^(-rt)]
```

**Where**

```math
K = carrying capacity
```

Population approaches K asymptotically.

#### Discrete Time Models

**Geometric Growth:**

```math
N(t+1) = λN(t)
```

**Solution:**

```math
N(t) = N₀λ^t
```

**Where**

```math
λ = finite rate of increase = e^r
```

**Ricker Model:**

```math
N(t+1) = N(t) × exp[r(1 - N(t)/K)]
```

### 5.3 Stochastic Models

#### Demographic Stochasticity

**Variance in vital rates from random individual events:**

```math
Var(N(t+1) | N(t)) ∝ N(t)
```

Most important when N is small.

**Extinction Probability (Birth-Death Process):**

```math
P(extinction) = (d/b)^N₀ if d < b
              = 1 if d ≥ b
```

#### Environmental Stochasticity

**Year-to-year variation in vital rates:**

```math
r(t) ~ Normal(r̄, σ_e²)
```

**Log-Population Dynamics:**

```math
ln(N(t+1)) = ln(N(t)) + r̄ - σ_e²/2 + ε(t)
```

This is a random walk with drift.

**Mean Time to Extinction:**

```math
T_e ≈ (2 ln(N₀) + ln(N₀)/r̄) / σ_e²
```

**Note:** This is an approximation.

#### Catastrophes

**Incorporated as occasional large negative events:**

```math
With probability p_cat per year:
  N → N × (1 - severity)
```

**Effect:** Dramatically reduces persistence probability

#### Combined Model

**VORTEX-style simulation incorporates:**
- Demographic stochasticity
- Environmental stochasticity
- Catastrophes
- Inbreeding depression
- Density dependence
- Harvest/supplementation

### 5.4 PVA Software and Methods

#### Major Software

| Software | Type | Key Features |
|----------|------|--------------|
| **VORTEX** | Individual-based | Comprehensive genetics |
| **RAMAS** | Stage-structured | Spatial metapopulations |
| **ALEX** | Individual-based | Landscape genetics |
| **ULM** | Matrix models | Age/stage structure |
| **R packages** | Various | Flexible customization |

#### Model Outputs

**Key Metrics:**

1. **Probability of extinction** P(E) over time T
2. **Mean time to extinction** (T_E)
3. **Population trajectory** with confidence intervals
4. **Genetic diversity** retention (H, A)
5. **Quasi-extinction risk** P(N < threshold)

#### PVA Uncertainty

**Sources:**
- Parameter uncertainty
- Model structure uncertainty
- Stochastic variation
- Environmental unpredictability

**Addressing Uncertainty:**
- Sensitivity analysis
- Scenario analysis
- Ensemble modeling
- Bayesian approaches

---

## 6. IUCN Red List Criteria

### 6.1 Quantitative Thresholds

#### Category Summary

| Category | Code | Risk Level | Color |
|----------|------|------------|-------|
| Least Concern | LC | Low | Green |
| Near Threatened | NT | Approaching | Yellow-green |
| Vulnerable | VU | High | Yellow |
| Endangered | EN | Very High | Orange |
| Critically Endangered | CR | Extremely High | Red |
| Extinct in Wild | EW | Only captive | Black |
| Extinct | EX | Gone | Black |

#### Five Criteria

| Criterion | Basis | Key Metric |
|-----------|-------|------------|
| **A** | Population reduction | % decline over time |
| **B** | Geographic range | EOO or AOO |
| **C** | Small population size | Number + decline |
| **D** | Very small/restricted | Number or area |
| **E** | Quantitative analysis | Extinction probability |

### 6.2 Criterion A: Population Reduction

#### Thresholds

| Reduction over 10 years/3 generations | Category |
|---------------------------------------|----------|
| ≥90% | CR (A1 if reversible, understood) |
| ≥80% | CR (A2-4) |
| ≥70% | EN (A1) |
| ≥50% | EN (A2-4) |
| ≥50% | VU (A1) |
| ≥30% | VU (A2-4) |

**Sub-criteria distinguish:**
- A1: Reduction ceased, causes understood and reversed
- A2: Reduction ongoing or cause not understood
- A3: Projected future reduction
- A4: Reduction includes past and future

#### Calculation

**From census data:**

```math
% decline = ((N_initial - N_current) / N_initial) × 100
```

**From population models:**

```math
% decline = (1 - λ^t) × 100
```

**Where**

```math
λ < 1 indicates decline
```

### 6.3 Criterion B: Geographic Range

#### Extent of Occurrence (EOO)

**Definition:** Minimum convex polygon containing all occurrences

**Calculation:**
- Map all known localities
- Draw minimum convex hull
- Calculate area (km²)

**Thresholds:**

| EOO | Category |
|-----|----------|
| <100 km² | CR |
| <5,000 km² | EN |
| <20,000 km² | VU |

#### Area of Occupancy (AOO)

**Definition:** Area within EOO actually occupied (using standard grid)

**Standard grid:**

```math
2 km × 2 km = 4 km² cells
```

**Thresholds:**

| AOO | Category |
|-----|----------|
| <10 km² | CR |
| <500 km² | EN |
| <2,000 km² | VU |

#### Additional Requirements (B1/B2)

Must also meet at least 2 of:
- **(a)** Severely fragmented OR few locations
- **(b)** Continuing decline
- **(c)** Extreme fluctuations

### 6.4 Criterion C: Small Population Size + Decline

#### Thresholds

| Mature individuals | + Decline condition | Category |
|--------------------|---------------------|----------|
| <250 | C1 or C2 | CR |
| <2,500 | C1 or C2 | EN |
| <10,000 | C1 or C2 | VU |

**C1:** Continuing decline at specified rates
**C2:** Continuing decline + fragmented/fluctuating/few subpopulations

### 6.5 Criterion D: Very Small or Restricted

#### Criterion D1/D2

| Metric | CR | EN | VU |
|--------|----|----|-------|
| Population (D) | <50 | <250 | <1,000 |
| AOO (D2) | — | — | <20 km² |
| Locations (D2) | — | — | ≤5 |

Criterion D requires no decline—just very small size or range

### 6.6 Criterion E: Quantitative Analysis

**Thresholds Based on Extinction Probability:**

| P(extinction) over time | Category |
|-------------------------|----------|
| ≥50% in 10 years/3 generations | CR |
| ≥20% in 20 years/5 generations | EN |
| ≥10% in 100 years | VU |

**This directly uses PVA results.**

---

## 7. Red List Index

### 7.1 Index Calculation

#### Basic Formula

**Red List Index (RLI):**

```math
RLI(t) = 1 - Σ W_c × N_c(t) / (W_max × N)
```

**Where**

```math
W_c = weight for category c
N_c(t) = number of species in category c at time t
W_max = maximum weight (typically 5 for EX)
N = total species assessed (excluding DD)
```

**Category Weights:**

| Category | Weight (W) |
|----------|-----------|
| LC | 0 |
| NT | 1 |
| VU | 2 |
| EN | 3 |
| CR | 4 |
| EX/EW | 5 |

#### Example Calculation

If at time t:
- 100 species assessed
- 40 LC, 20 NT, 15 VU, 10 EN, 10 CR, 5 EX

```math
RLI = 1 - [(0×40 + 1×20 + 2×15 + 3×10 + 4×10 + 5×5) / (5×100)]
    = 1 - [(0 + 20 + 30 + 30 + 40 + 25) / 500]
    = 1 - (145/500)
    = 1 - 0.29
    = 0.71
```

### 7.2 Interpretation

**RLI Values:**

```math
RLI = 1.0: All species Least Concern
RLI = 0.5: Average category is between VU and EN
RLI = 0.0: All species Extinct
```

**Trend:**
- Decreasing RLI: Conservation status worsening
- Stable RLI: Status unchanged
- Increasing RLI: Conservation improvements

### 7.3 Disaggregated Indices

#### By Taxonomic Group

Calculate RLI separately for:
- Mammals
- Birds
- Amphibians
- etc.

#### By Region

Calculate RLI for species within geographic regions.

#### By Threat Type

Weight contributions by primary threat driver.

---

## 8. Species Distribution Modeling

### 8.1 Ecological Niche Models

#### Concept

**Fundamental Niche:** Environmental conditions where species can survive
**Realized Niche:** Actual distribution (subset due to competition, barriers)

**SDM Goal:** Model realized niche from occurrence + environmental data

#### MAXENT Algorithm

**Maximum Entropy Approach:**

```math
Maximize entropy of distribution subject to constraints:
  E[f_j(x)] = Σ f_j(x_i) / n
```

**Where**

```math
f_j are environmental feature functions
[match feature means]
```

**Output:**

```math
P(x) = Probability of presence at location x
```

### 8.2 Climate Envelope Models

#### BIOCLIM

**Method:**
1. Extract climate values at occurrence points
2. Define envelope as range or percentiles
3. Project to new climate scenarios

**Variables:**
- Temperature (annual mean, seasonality, extremes)
- Precipitation (annual, seasonality, extremes)
- 19 standard BIOCLIM variables

#### Ensemble Approaches

**Combine multiple algorithms:**
- MAXENT
- GLM
- GAM
- Random Forest
- BRT
- etc.

**Ensemble prediction:** Weighted average or majority vote

### 8.3 Model Validation

#### Cross-Validation

**k-fold:**
1. Divide data into k groups
2. Train on k-1, test on 1
3. Repeat k times
4. Average performance

#### Performance Metrics

**AUC (Area Under ROC Curve):**

```math
0.5 = random
0.7–0.8 = acceptable
0.8–0.9 = good
>0.9 = excellent
```

**TSS (True Skill Statistic):**

```math
TSS = Sensitivity + Specificity - 1
```

**Where**

```math
Range: -1 to +1 (0 = random)
```

---

## 9. Projection Methods

### 9.1 Scenario-Based Projections

#### IPCC/IPBES Scenarios

**SSP (Shared Socioeconomic Pathways):**

| SSP | Description | Biodiversity Impact |
|-----|-------------|---------------------|
| SSP1 | Sustainability | Lower impact |
| SSP2 | Middle of road | Moderate |
| SSP3 | Regional rivalry | Higher impact |
| SSP4 | Inequality | High impact |
| SSP5 | Fossil-fueled | Very high |

**Combined with RCP (Representative Concentration Pathways):**

```math
RCP2.6: <2°C warming
RCP4.5: ~2.5°C warming
RCP6.0: ~3°C warming
RCP8.5: ~4.5°C warming
```

### 9.2 Time-to-Extinction Models

#### Barnosky Projection

**Method:**
If current trends continue, time to 75% species loss:

```math
T_75 = 0.75 / current_rate × million_years
```

**Calculation:**

```math
Current rate ≈ 100 E/MSY
```

```math
T_75 = (0.75 × 10⁶) / 100 = 7,500 years [lower bound]
     = (0.75 × 10⁶) / 1,000 = 750 years [upper bound]
```

**Refined estimate:**

```math
240–540 years (Barnosky et al. 2011)
```

#### Climate-Extinction Projections

**Thomas et al. 2004 Framework:**

For each climate scenario:
1. Project future climate
2. Model species range shifts
3. Calculate committed extinctions

**Results:**

```math
1.5°C: 6–8% species committed to extinction
2.0°C: 16–18% species committed
3.0°C: 26–37% species committed
4.0°C+: 40–50%+ species committed
```

### 9.3 Uncertainty Quantification

#### Sources of Uncertainty

1. **Parametric:** Uncertainty in model parameters
2. **Structural:** Choice of model form
3. **Scenario:** Future conditions unknown
4. **Data:** Incomplete observations

#### Monte Carlo Methods

**Propagating Uncertainty:**
1. Define parameter distributions
2. Sample parameters randomly
3. Run model with each sample
4. Analyze output distribution

```python
# Pseudo-code
for i in range(n_iterations):
    params = sample_from_distributions()
    result[i] = run_model(params)

CI_95 = percentile(result, [2.5, 97.5])
```

#### Bayesian Approaches

**Posterior prediction:**

```math
P(future | data) = ∫ P(future | θ) × P(θ | data) dθ
```

Integrates over parameter uncertainty.

---

## 10. Statistical Methods

### 10.1 Biodiversity Metrics

#### Alpha Diversity (Within-Sample)

**Species Richness (S):** Simple count

**Shannon Index (H'):**

```math
H' = -Σ p_i × ln(p_i)
```

**Where**

```math
p_i = proportion of species i
```

**Simpson Index (D):**

```math
D = 1 - Σ p_i²
```

**Effective Number of Species:**

```math
exp(H')  [Shannon]
1/Σp_i²  [Simpson, Hill's N2]
```

#### Beta Diversity (Between-Sample)

**Jaccard Similarity:**

```math
J = |A ∩ B| / |A ∪ B|
```

**Sørensen Similarity:**

```math
S = 2|A ∩ B| / (|A| + |B|)
```

**Bray-Curtis Dissimilarity:**

```math
BC = Σ |x_ij - x_ik| / Σ (x_ij + x_ik)
```

#### Gamma Diversity

**Regional diversity:**

```math
γ = α × β [multiplicative]
γ = α + β [additive]
```

### 10.2 Trend Detection

#### Population Trend Analysis

**Linear Regression on Log-Counts:**

```math
ln(N(t)) = a + bt + ε
```

**Where**

```math
b = annual rate of change
```

**Testing for Decline:**

```math
H₀: b = 0 (no trend)
H₁: b < 0 (decline)
```

Use t-test on slope.

#### Living Planet Index Method

**Geometric Mean of Relative Abundance:**

```math
LPI(t) = exp[Σ ln(N_i(t)/N_i(1970)) / n]
```

Normalized so LPI(1970) = 1.0

#### Generalized Additive Models

**For Non-Linear Trends:**

```math
E[Y] = f(time) + covariates
```

**Where**

```math
f() is a smooth function
```

### 10.3 Sampling and Extrapolation

#### Rarefaction

**Comparing Richness at Equal Effort:**

```math
E[S_n] = S - Σ C(N-N_i, n) / C(N, n)
```

**Where**

```math
C(a,b) = combinations
```

#### Extrapolation (Chao Estimators)

**Chao1 (Abundance-Based):**

```math
S_est = S_obs + f₁²/(2f₂)
```

**Where**

```math
f₁ = singletons, f₂ = doubletons
```

**Chao2 (Incidence-Based):**

```math
S_est = S_obs + Q₁²/(2Q₂)
```

**Where**

```math
Q₁ = uniques, Q₂ = duplicates
```

#### Occupancy Modeling

**Accounting for Imperfect Detection:**

```math
P(detection) = P(occupied) × P(detected | occupied)
```

**Occupancy (ψ) and Detection (p) estimated jointly**

---

## 11. Key Formulas Reference

### Quick Reference Table

| Application | Formula | Variables |
|-------------|---------|-----------|
| Extinction rate | E/MSY = (E/S) × 10⁶/t | E=extinctions, S=species, t=years |
| Species-area | S = cA^z | S=species, A=area, z≈0.25 |
| Exponential growth | N(t) = N₀e^(rt) | N=population, r=growth rate |
| Logistic growth | dN/dt = rN(1-N/K) | K=carrying capacity |
| MVP (rough) | N ≈ 5,000 | Long-term viability |
| Shannon index | H' = -Σ pᵢ ln(pᵢ) | pᵢ=species proportion |
| Red List Index | RLI = 1 - ΣWᶜNᶜ/(W_max × N) | W=weight, N=count |
| Extinction debt | Debt = S_obs - cA^z | Current vs. equilibrium |

### Unit Conversions

| From | To | Conversion |
|------|-----|------------|
| % decline/year | λ (finite rate) | λ = 1 - (decline/100) |
| λ | r (intrinsic rate) | r = ln(λ) |
| r | doubling time | T_d = ln(2)/r |
| r | halving time | T_h = ln(2)/\|r\| (for r<0) |

---

## 12. Data Sources & References

### Primary Sources (Verified 2024-2025)

**Extinction Rate Methods:**

- Pimm, S.L., et al. 2014. The biodiversity of species and their rates of extinction. Science. **[Foundational]**
- Barnosky, A.D., et al. 2011. Has the Earth's sixth mass extinction already arrived? Nature. **[Foundational]**
- De Vos, J.M., et al. 2015. Estimating the normal background rate of species extinction. Conservation Biology. **[0.1 E/MSY estimate]**
- **Ceballos, G., et al. 2015.** Accelerated modern human–induced species losses. Science Advances. **[Landmark 100× background rate study; uses conservative 2 E/MSY background]**

**Species-Area Relationships:**

- Rosenzweig, M.L. 1995. Species Diversity in Space and Time. **[Classic text]**
- Connor, E.F. & McCoy, E.D. 1979. The statistics and biology of the species-area relationship. American Naturalist.
- Triantis, K.A., et al. 2012. The island species–area relationship: biology and statistics. Journal of Biogeography.

**Population Viability:**

- Traill, L.W., et al. 2007. Minimum viable population size: A meta-analysis of 30 years of published estimates. Biological Conservation.
- Reed, D.H., et al. 2003. Estimates of minimum viable population sizes for vertebrates. Biological Conservation.
- Morris, W.F. & Doak, D.F. 2002. Quantitative Conservation Biology.

**IUCN Methodology:**

- **IUCN Standards and Petitions Committee. 2024.** Guidelines for Using the IUCN Red List Categories and Criteria. **Version 16 (March 2024).** **[Current authoritative version]**
- Butchart, S.H.M., et al. 2007. Improvements to the Red List Index. PLoS ONE.
- **IUCN. 2024.** Guidelines for the Application of IUCN Red List of Ecosystems Categories and Criteria. **Version 2.0.** **[Updated ecosystem assessment methodology]**

**Species Distribution Modeling:**

- Elith, J. & Leathwick, J.R. 2009. Species distribution models. Annual Review of Ecology.
- Phillips, S.J., et al. 2006. Maximum entropy modeling of species geographic distributions. Ecological Modelling.

### Software References

- **VORTEX:** Lacy, R.C. & Pollak, J.P. VORTEX: A Stochastic Simulation of the Extinction Process.
- **MAXENT:** Phillips, S.J. et al. Maximum Entropy Modeling.
- **R packages:** vegan, dismo, popbio, unmarked

### Methodological Notes

**Background Extinction Rate Debate:**

The choice of background extinction rate significantly affects calculated rate multiples:
- **Conservative estimate (2 E/MSY):** Yields ~100× current excess (Ceballos et al. 2015)
- **Lower estimate (0.1 E/MSY):** Yields ~1,000× current excess (De Vos et al. 2015)
- Both estimates support the conclusion of mass extinction-level rates

**IUCN Guidelines Currency:**

IUCN Red List Guidelines are regularly updated. Version 16 (March 2024) is current as of this document. Users should verify they are using the latest version at: www.iucnredlist.org/resources/redlistguidelines

### Gaps and Uncertainties

**Known Methodological Limitations:**

1. **Species-area relationship:** z-values vary significantly by taxon and region (0.15-0.35)
2. **MVP estimates:** Range from 500-5,000+ depending on species and definition (50-year vs. 100-year persistence)
3. **Background rate uncertainty:** Order-of-magnitude debate (0.1-2.0 E/MSY) affects rate multiple calculations
4. **Projection models:** High sensitivity to input parameters and scenarios
5. **Extinction lag:** Species-area models may underestimate extinction debt

---

> **Document Status:** Version 2.1 - Math Code Block Formatting Standardized
> **Last Updated:** Saturday, January 04, 2025
> **Verification Date:** December 2025 (against IUCN Guidelines v16 and foundational literature)
> **Next Review:** As new methods are developed; check for IUCN Guidelines updates
> **Cross-References:** major_minor_extinction_events.md, major_minor_current_status.md

---

### Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-12-12 | Initial comprehensive document |
| 2.0 | 2025-12-12 | Research verification: Updated IUCN Guidelines reference to v16 (March 2024), added Ceballos et al. 2015 landmark study, added methodological notes on background rate debate, added Red List of Ecosystems v2.0, added uncertainty clauses |
| 2.1 | 2025-01-04 | Standardized all math code blocks to use ```math syntax with separate **Where** blocks for variable definitions |

---

> *Document compiled and verified: Saturday, January 04, 2025*
> *Methodology sources: IUCN, Science, Nature, Science Advances, Conservation Biology*

---

> **︻デ═—··· 🎯 = Aim Twice, Shoot Once!**
