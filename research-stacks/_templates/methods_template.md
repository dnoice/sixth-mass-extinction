<!--
✒ Metadata
    - Title: Methods Documentation Template (SME Edition - v1.0)
    - File Name: methods_template.md
    - Relative Path: research-stacks/_templates/methods_template.md
    - Artifact Type: docs
    - Version: 1.0.0
    - Date: 2026-01-05
    - Update: Sunday, January 05, 2026
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Anthropic - Claude Opus 4.5
    - Signature: ︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!

✒ Description:
    Template for METHODS_X.X_ORIGINAL_ANALYSIS.md documentation files.
    Provides comprehensive methodological transparency for all original
    analyses conducted in each SME episode's research stack.

✒ Key Features:
    - Feature 1: Complete data source documentation with tiered attribution
    - Feature 2: Statistical methodology specifications
    - Feature 3: Calculation procedures with worked examples
    - Feature 4: Assumption documentation and justification
    - Feature 5: Validation and verification procedures
    - Feature 6: Reproducibility specifications
    - Feature 7: Software and version requirements
    - Feature 8: Quality assurance protocols

✒ Usage Instructions:
    Copy to episode methodology/ directory:
        cp _templates/methods_template.md X.X-episode/methodology/METHODS_X.X_ORIGINAL_ANALYSIS.md

    Fill all sections with episode-specific methodological details.

✒ Other Important Information:
    - Dependencies: None (documentation only)
    - Compatible platforms: All markdown renderers
    - Related templates: technical_supplement_template.md, uncertainty_template.md
---------
-->

# Methods: Original Analysis

## Episode {X.X}: {Episode Title}

> **Document Type:** Methodological Documentation
>
> **Companion Article:** [ARTICLE_{X.X}.md](../article/ARTICLE_{X.X}.md)
>
> **Technical Supplement:** [TECHNICAL_SUPPLEMENT_{X.X}_METHODOLOGY.md](TECHNICAL_SUPPLEMENT_{X.X}_METHODOLOGY.md)

---

## Table of Contents

1. [Overview](#1-overview)
2. [Data Sources](#2-data-sources)
3. [Data Processing](#3-data-processing)
4. [Analytical Methods](#4-analytical-methods)
5. [Key Calculations](#5-key-calculations)
6. [Assumptions](#6-assumptions)
7. [Validation](#7-validation)
8. [Reproducibility](#8-reproducibility)
9. [Limitations](#9-limitations)
10. [References](#10-references)

---

## 1. Overview

### 1.1 Purpose

This document provides complete methodological documentation for all original analyses presented in Episode {X.X}: {Episode Title}. It enables:

- Full reproducibility of results
- Methodological transparency
- Critical evaluation of findings
- Extension and refinement by other researchers

### 1.2 Scope

| Aspect | Coverage |
| ------ | -------- |
| **Primary Analysis** | {Description of main analysis} |
| **Secondary Analysis** | {Description of supporting analyses} |
| **Time Period** | {Start year} - {End year} |
| **Geographic Scope** | {Global / Regional / Local} |
| **Taxonomic Scope** | {All taxa / Specific groups} |

### 1.3 Research Questions Addressed

- **Q1:** {Primary research question}
- **Q2:** {Secondary research question}
- **Q3:** {Tertiary research question}

---

## 2. Data Sources

### 2.1 Primary Data Sources

#### Tier 1: Authoritative International Assessments

| Source | Dataset | Version | Access Date | Citation |
| ------ | ------- | ------- | ----------- | -------- |
| {Source} | {Dataset name} | {Version} | {YYYY-MM-DD} | {Citation} |

**Data Description:**

{Detailed description of the data, including variables used, units, and any preprocessing applied by the source.}

#### Tier 2: Peer-Reviewed Literature

| Source | Dataset | DOI | Access Date |
| ------ | ------- | --- | ----------- |
| {Author et al. Year} | {Dataset} | {DOI} | {YYYY-MM-DD} |

#### Tier 3: Government and Institutional Sources

| Source | Dataset | URL | Access Date |
| ------ | ------- | --- | ----------- |
| {Agency} | {Dataset} | {URL} | {YYYY-MM-DD} |

#### Tier 4: Verified NGO and Monitoring Data

| Source | Dataset | Verification Method | Access Date |
| ------ | ------- | ------------------- | ----------- |
| {Organization} | {Dataset} | {How verified} | {YYYY-MM-DD} |

### 2.2 Data Selection Criteria

Data were selected based on the following criteria:

1. **Temporal Coverage:** {Minimum years of data required}
2. **Spatial Coverage:** {Geographic requirements}
3. **Quality Standards:** {Minimum quality thresholds}
4. **Accessibility:** {Open access requirements}

### 2.3 Data Exclusions

The following data were excluded:

| Exclusion | Reason | Impact on Analysis |
| --------- | ------ | ------------------ |
| {Data type} | {Reason for exclusion} | {How this affects results} |

---

## 3. Data Processing

### 3.1 Data Cleaning

**Missing Data Handling:**

| Variable | Missing Rate | Treatment | Justification |
| -------- | ------------ | --------- | ------------- |
| {Variable} | {X%} | {Method} | {Why this approach} |

**Outlier Treatment:**

- Detection method: {IQR / Z-score / Domain knowledge}
- Treatment: {Removal / Winsorization / Robust methods}
- Threshold: {Specific values}

### 3.2 Data Transformation

| Variable | Original Unit | Transformed | Transformation | Reason |
| -------- | ------------- | ----------- | -------------- | ------ |
| {Var} | {Unit} | {New unit} | {log / sqrt / etc.} | {Why} |

### 3.3 Data Integration

**Temporal Alignment:**

{How data from different sources with different temporal resolutions were aligned.}

**Spatial Harmonization:**

{How data from different spatial scales or coordinate systems were harmonized.}

**Taxonomic Standardization:**

{How taxonomic names were standardized across sources (e.g., using ITIS, GBIF Backbone).}

---

## 4. Analytical Methods

### 4.1 Statistical Framework

**Primary Statistical Approach:**

{Description of the overall statistical framework (frequentist / Bayesian / other).}

**Software Environment:**

| Software | Version | Purpose |
| -------- | ------- | ------- |
| Python | {X.X.X} | Primary analysis |
| pandas | {X.X.X} | Data manipulation |
| numpy | {X.X.X} | Numerical operations |
| scipy | {X.X.X} | Statistical tests |
| matplotlib | {X.X.X} | Visualization |

### 4.2 Method 1: {Method Name}

**Purpose:** {What this method accomplishes}

**Mathematical Formulation:**

```math
{LaTeX formula}
```

**Implementation:**

```python
# Pseudocode or actual code
def method_name(data):
    """Implementation of Method 1."""
    # Step 1: {Description}
    result = operation(data)
    # Step 2: {Description}
    return result
```

**Parameters:**

| Parameter | Value | Justification |
| --------- | ----- | ------------- |
| {Param 1} | {Value} | {Why this value} |
| {Param 2} | {Value} | {Why this value} |

### 4.3 Method 2: {Method Name}

**Purpose:** {What this method accomplishes}

**Mathematical Formulation:**

```math
{LaTeX formula}
```

**Implementation:**

{Code or detailed description}

### 4.4 Method 3: {Method Name}

**Purpose:** {What this method accomplishes}

**Mathematical Formulation:**

```math
{LaTeX formula}
```

---

## 5. Key Calculations

### 5.1 Calculation 1: {Name}

**Definition:**

{Clear definition of what is being calculated.}

**Formula:**

```math
{LaTeX formula}
```

**Worked Example:**

Given:

- {Input 1} = {Value}
- {Input 2} = {Value}

Calculation:

```text
Step 1: {Calculation} = {Result}
Step 2: {Calculation} = {Result}
Final: {Answer}
```

**Interpretation:**

{How to interpret the calculated value.}

### 5.2 Calculation 2: {Name}

{Same structure as above}

### 5.3 Calculation 3: {Name}

{Same structure as above}

---

## 6. Assumptions

### 6.1 Data Assumptions

| Assumption | Basis | Sensitivity | Validation |
| ---------- | ----- | ----------- | ---------- |
| {Assumption 1} | {Why assumed} | {High/Medium/Low} | {How validated} |
| {Assumption 2} | {Why assumed} | {High/Medium/Low} | {How validated} |

### 6.2 Model Assumptions

| Assumption | Required For | Tested | Result |
| ---------- | ------------ | ------ | ------ |
| {Normality} | {Method X} | {Test used} | {Pass/Fail} |
| {Independence} | {Method Y} | {Test used} | {Pass/Fail} |
| {Linearity} | {Method Z} | {Test used} | {Pass/Fail} |

### 6.3 Interpretation Assumptions

{List assumptions made when interpreting results.}

---

## 7. Validation

### 7.1 Internal Validation

**Cross-Validation:**

{Description of cross-validation approach if applicable.}

**Sensitivity Analysis:**

| Parameter/Assumption | Variation | Impact on Results |
| -------------------- | --------- | ----------------- |
| {Item} | {Range tested} | {Quantitative impact} |

### 7.2 External Validation

**Comparison with Published Estimates:**

| Metric | This Analysis | Published Estimate | Source | Agreement |
| ------ | ------------- | ------------------ | ------ | --------- |
| {Metric} | {Value} | {Value} | {Citation} | {Yes/No/Partial} |

**Expert Review:**

{If applicable, describe any expert review or consultation.}

### 7.3 Robustness Checks

| Check | Alternative Approach | Result Comparison |
| ----- | -------------------- | ----------------- |
| {Check 1} | {Alternative} | {Consistent/Differs} |
| {Check 2} | {Alternative} | {Consistent/Differs} |

---

## 8. Reproducibility

### 8.1 Code Availability

| Component | Location | Format |
| --------- | -------- | ------ |
| Data processing | `../notebooks/01-data-acquisition.ipynb` | Jupyter |
| Analysis | `../notebooks/02-primary-analysis.ipynb` | Jupyter |
| Visualization | `../notebooks/03-visualization.ipynb` | Jupyter |
| Utility functions | `../scripts/` | Python |

### 8.2 Data Availability

| Dataset | Location | Access |
| ------- | -------- | ------ |
| Raw data | `../data/raw/` | {Open/Restricted} |
| Processed data | `../data/processed/` | Open |
| Metadata | `../data/metadata/MANIFEST.md` | Open |

### 8.3 Environment Specification

**Requirements:**

```text
# requirements.txt
pandas>=2.0.0
numpy>=1.24.0
scipy>=1.10.0
matplotlib>=3.7.0
seaborn>=0.12.0
plotly>=5.14.0
```

**Reproduction Steps:**

1. Clone repository
2. Create virtual environment: `python -m venv .venv`
3. Activate environment
4. Install dependencies: `pip install -r requirements.txt`
5. Run notebooks in sequence (01 → 02 → 03)

---

## 9. Limitations

### 9.1 Data Limitations

- **{Limitation 1}:** {Description and impact on analysis}
- **{Limitation 2}:** {Description and impact on analysis}
- **{Limitation 3}:** {Description and impact on analysis}

### 9.2 Methodological Limitations

- **{Limitation 1}:** {Description and impact on conclusions}
- **{Limitation 2}:** {Description and impact on conclusions}

### 9.3 Scope Limitations

- **{Limitation 1}:** {What is not covered and why}
- **{Limitation 2}:** {What is not covered and why}

---

## 10. References

### Methods References

1. {Reference for Method 1}
2. {Reference for Method 2}
3. {Reference for statistical approach}

### Data References

4. {Primary data source citation}
5. {Secondary data source citation}

### Software References

6. {Key software citations}

---

## Document Metadata

| Field | Value |
| ----- | ----- |
| **Episode** | {X.X} - {Episode Name} |
| **Version** | 1.0.0 |
| **Created** | {YYYY-MM-DD} |
| **Last Updated** | {YYYY-MM-DD} |
| **Author** | {Author} |
| **Reviewed By** | {Reviewer if applicable} |

---

> **︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!**
