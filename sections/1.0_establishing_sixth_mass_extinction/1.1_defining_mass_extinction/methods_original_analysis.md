<!--
================================================================================
Title:              Methods - Original Analysis - Section 1.1
File Name:          methods_original_analysis.md
Relative Path:      sections/1.0.../1.1.../methods_original_analysis.md
Artifact Type:      Documentation/Methodology
Version:            0.1 (Template)
Date:               2025-12-12
Update:             Initial Template Creation
Author:             Dennis 'dnoice' Smaltz
A.I. Acknowledgement: Claude Opus 4
Signature:          ︻デ═—··· 🎯 = Aim Twice, Shoot Once!
================================================================================

DESCRIPTION:
Detailed methodology documentation for all original analyses conducted in
Section 1.1: Defining Mass Extinction. This document provides full
reproducibility by describing data sources, processing steps, analytical
methods, and validation approaches.

KEY FEATURES:
1. Complete data provenance documentation
2. Step-by-step analytical methodology
3. Statistical methods and justification
4. Validation and quality control procedures
5. Reproducibility instructions

USAGE:
- Reference when reviewing/auditing analysis
- Follow for exact reproduction of results
- Update when methodology changes

================================================================================
-->

# METHODS: ORIGINAL ANALYSIS
## Section 1.1: Defining Mass Extinction

---

## OVERVIEW

### Analysis Objectives

1. **Primary Objective**: [e.g., Calculate current extinction rate and compare to Big Five events]
2. **Secondary Objective**: [e.g., Establish quantitative threshold for mass extinction designation]
3. **Novel Contribution**: [e.g., Unified rate comparison across paleontological and modern data]

### Key Outputs

| Output | Description | Location |
|--------|-------------|----------|
| Dataset 1 | [Description] | `data/derived/[filename]` |
| Figure 1 | [Description] | `figures/fig_1.1_01_[name].png` |
| [Add more] | | |

---

## 1. DATA SOURCES AND ACQUISITION

### 1.1 Primary Data Sources

#### Source 1: IUCN Red List (DS-PA-001)

| Attribute | Value |
|-----------|-------|
| **Access Method** | API / Bulk Download |
| **Access Date** | YYYY-MM-DD |
| **Version** | v2025-2 |
| **Query Parameters** | [Specify] |
| **Records Retrieved** | [N records] |
| **Storage Location** | `data/raw/iucn/` |

**Acquisition Code**:
```python
# Reference notebook: 01_data_acquisition.ipynb, Cell [X]
# [Brief code description or link]
```

---

#### Source 2: [Paleontological Extinction Database]

| Attribute | Value |
|-----------|-------|
| **Access Method** | [Method] |
| **Access Date** | YYYY-MM-DD |
| **Citation** | [Full citation] |
| **Records Retrieved** | [N records] |
| **Storage Location** | `data/raw/paleo/` |

---

### 1.2 Data Quality Checks

| Check | Method | Pass Criteria | Result |
|-------|--------|---------------|--------|
| Completeness | [Method] | [Criteria] | ⬜ Pass / ⬜ Fail |
| Accuracy | [Method] | [Criteria] | ⬜ Pass / ⬜ Fail |
| Consistency | [Method] | [Criteria] | ⬜ Pass / ⬜ Fail |
| Timeliness | [Method] | [Criteria] | ⬜ Pass / ⬜ Fail |

---

## 2. DATA PROCESSING

### 2.1 Data Cleaning

**Notebook Reference**: `02_analysis_core.ipynb`, Cells [X-Y]

#### Step 1: [Data Cleaning Step]
- **Input**: `data/raw/[filename]`
- **Output**: `data/processed/[filename]`
- **Operations**:
  1. [Operation 1]
  2. [Operation 2]
  3. [Operation 3]
- **Records Removed**: [N] ([X]% of total)
- **Removal Justification**: [Explanation]

#### Step 2: [Data Transformation Step]
- **Input**: `data/processed/[filename]`
- **Output**: `data/processed/[filename]`
- **Operations**:
  1. [Transformation 1]
  2. [Transformation 2]

---

### 2.2 Data Integration

**Combining Multiple Sources**

| Source A | Source B | Join Method | Join Key | Match Rate |
|----------|----------|-------------|----------|------------|
| [Source] | [Source] | [Inner/Left/etc.] | [Key] | [X]% |

**Harmonization Steps**:
1. [Taxonomic standardization approach]
2. [Temporal alignment approach]
3. [Unit conversion if applicable]

---

## 3. ANALYTICAL METHODS

### 3.1 Background Extinction Rate Calculation

**Method Name**: [e.g., Fossil Record-Based E/MSY Estimation]

**Justification**: [Why this method was chosen]

**Mathematical Formulation**:

$$
E_{background} = \frac{E_{observed}}{N_{species} \times T_{period}}
$$

Where:
- $E_{observed}$ = Number of observed extinctions in fossil record
- $N_{species}$ = Estimated species richness during period
- $T_{period}$ = Time period in millions of years

**Parameters Used**:

| Parameter | Value | Source | Uncertainty |
|-----------|-------|--------|-------------|
| [Param 1] | [Value] | [Source] | ± [Range] |
| [Param 2] | [Value] | [Source] | ± [Range] |

**Implementation**:
```python
# Reference: 02_analysis_core.ipynb, Cell [X]
def calculate_background_rate(extinctions, species_count, time_period):
    """
    Calculate background extinction rate in E/MSY.

    Parameters:
    -----------
    extinctions : int
        Number of observed extinctions
    species_count : float
        Estimated species richness
    time_period : float
        Time period in millions of years

    Returns:
    --------
    float : Extinction rate in E/MSY
    """
    return extinctions / (species_count * time_period)
```

---

### 3.2 Current Extinction Rate Calculation

**Method Name**: [e.g., Documented Extinctions Since 1500]

**Justification**: [Why this method and time period]

**Mathematical Formulation**:

$$
E_{current} = \frac{E_{documented}}{N_{assessed} \times T_{modern}}
$$

**Assumptions**:
1. [Assumption 1]
2. [Assumption 2]
3. [Assumption 3]

**Alternative Calculations** (for sensitivity analysis):
- Conservative: [Method]
- Liberal: [Method]

---

### 3.3 Big Five Comparison Analysis

**Method Name**: [e.g., Rate-Normalized Mass Extinction Comparison]

**Challenge Addressed**: [e.g., Comparing rates across different timescales and taxonomic scopes]

**Approach**:
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Normalization Method**: [Description]

---

### 3.4 Novel Synthesis: [Title of Novel Analysis]

**What Makes This Original**: [Explanation of novel contribution]

**Methodology**:

[Detailed description of the novel analytical approach]

**Validation**: [How we validated this new approach]

---

## 4. STATISTICAL METHODS

### 4.1 Uncertainty Quantification

**Method**: [e.g., Monte Carlo simulation, Bootstrap, Bayesian credible intervals]

**Parameters**:
- Number of iterations: [N]
- Random seed: [X] (for reproducibility)
- Confidence level: [95%]

**Implementation**:
```python
# Reference: 02_analysis_core.ipynb, Cell [X]
# [Code snippet or description]
```

---

### 4.2 Sensitivity Analysis

**Parameters Varied**:

| Parameter | Base Value | Range Tested | Step Size |
|-----------|------------|--------------|-----------|
| [Param 1] | [X] | [Y to Z] | [S] |
| [Param 2] | [X] | [Y to Z] | [S] |

**Method**: [One-at-a-time / Full factorial / Latin hypercube]

---

### 4.3 Statistical Tests Used

| Test | Purpose | Assumptions | Result Interpretation |
|------|---------|-------------|----------------------|
| [Test 1] | [Purpose] | [Assumptions] | [How to interpret] |
| [Test 2] | [Purpose] | [Assumptions] | [How to interpret] |

---

## 5. VISUALIZATION METHODS

### 5.1 Figure Generation

**Notebook Reference**: `03_visualization.ipynb`

#### Figure 1.1.01: [Title]

| Attribute | Value |
|-----------|-------|
| **Type** | [Bar chart / Line plot / etc.] |
| **Data Source** | `data/derived/[filename]` |
| **Tools Used** | [matplotlib, seaborn, etc.] |
| **Resolution** | 300 DPI |
| **Dimensions** | [W × H] inches |
| **Color Palette** | [Palette name - colorblind safe] |

---

## 6. VALIDATION AND QUALITY CONTROL

### 6.1 Internal Validation

| Validation Check | Method | Result |
|-----------------|--------|--------|
| Calculation verification | [Method] | ⬜ Pass / ⬜ Fail |
| Edge case testing | [Method] | ⬜ Pass / ⬜ Fail |
| Cross-validation | [Method] | ⬜ Pass / ⬜ Fail |

---

### 6.2 External Validation

| Comparison | Our Result | Published Result | Agreement |
|------------|------------|------------------|-----------|
| [Study 1] | [X] | [Y] | [Yes/No/Partial] |
| [Study 2] | [X] | [Y] | [Yes/No/Partial] |

**Discrepancy Explanations**: [If any]

---

## 7. REPRODUCIBILITY INSTRUCTIONS

### 7.1 Environment Setup

```bash
# Python version
python --version  # Requires Python 3.X+

# Create virtual environment
python -m venv sme_env
source sme_env/bin/activate  # Linux/Mac
# or
sme_env\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### 7.2 Required Dependencies

```
# requirements.txt for Section 1.1
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.12.0
scipy>=1.10.0
requests>=2.28.0
jupyter>=1.0.0
```

### 7.3 Execution Order

1. `01_data_acquisition.ipynb` - Fetch and store raw data
2. `02_analysis_core.ipynb` - Process and analyze
3. `03_visualization.ipynb` - Generate figures

### 7.4 Expected Outputs

| Output | Expected Location | Verification |
|--------|-------------------|--------------|
| [Dataset] | `data/derived/[name]` | [Checksum/size] |
| [Figure] | `figures/fig_1.1_01_[name].png` | [Dimensions] |

---

## 8. LIMITATIONS AND CAVEATS

### 8.1 Methodological Limitations

1. **[Limitation 1]**: [Description and impact]
2. **[Limitation 2]**: [Description and impact]
3. **[Limitation 3]**: [Description and impact]

### 8.2 Data Limitations

1. **[Limitation 1]**: [Description and impact]
2. **[Limitation 2]**: [Description and impact]

### 8.3 Interpretation Caveats

- [Caveat 1]
- [Caveat 2]

---

## 9. CHANGELOG

| Date | Change | Justification |
|------|--------|---------------|
| YYYY-MM-DD | [Change description] | [Why] |

---

## VERSION HISTORY

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 0.1 | 2025-12-12 | Initial template | Dennis 'dnoice' Smaltz |

---

*︻デ═—··· 🎯 = Aim Twice, Shoot Once!*
