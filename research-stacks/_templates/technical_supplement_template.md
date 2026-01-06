<!--
✒ Metadata
    - Title: Technical Supplement Template (SME Edition - v1.0)
    - File Name: technical_supplement_template.md
    - Relative Path: research-stacks/_templates/technical_supplement_template.md
    - Artifact Type: docs
    - Version: 1.0.0
    - Date: 2026-01-05
    - Update: Sunday, January 05, 2026
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Anthropic - Claude Opus 4.5
    - Signature: ︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!

✒ Description:
    Template for TECHNICAL_SUPPLEMENT_X.X_METHODOLOGY.md files providing
    extended technical specifications beyond the main methods document.
    Contains mathematical derivations, code implementations, and detailed
    parameter specifications.

✒ Key Features:
    - Feature 1: Mathematical derivations with step-by-step proofs
    - Feature 2: Complete code implementations for all methods
    - Feature 3: Parameter sensitivity specifications
    - Feature 4: Computational complexity analysis
    - Feature 5: Extended validation results
    - Feature 6: Edge case handling documentation
    - Feature 7: Performance benchmarks
    - Feature 8: Alternative implementation options

✒ Usage Instructions:
    Copy to episode methodology/ directory:
        cp _templates/technical_supplement_template.md \
           X.X-episode/methodology/TECHNICAL_SUPPLEMENT_X.X_METHODOLOGY.md

✒ Other Important Information:
    - Dependencies: None (documentation only)
    - Companion to: METHODS_X.X_ORIGINAL_ANALYSIS.md
---------
-->

# Technical Supplement: Methodology

## Episode {X.X}: {Episode Title}

> **Document Type:** Technical Supplement
>
> **Main Methods Document:** [METHODS_{X.X}_ORIGINAL_ANALYSIS.md](METHODS_{X.X}_ORIGINAL_ANALYSIS.md)
>
> **Uncertainty Documentation:** [UNCERTAINTY_DOCUMENTATION.md](UNCERTAINTY_DOCUMENTATION.md)

---

## Table of Contents

1. [Mathematical Derivations](#1-mathematical-derivations)
2. [Algorithm Specifications](#2-algorithm-specifications)
3. [Code Implementations](#3-code-implementations)
4. [Parameter Specifications](#4-parameter-specifications)
5. [Computational Details](#5-computational-details)
6. [Extended Validation](#6-extended-validation)
7. [Edge Cases](#7-edge-cases)
8. [Alternative Approaches](#8-alternative-approaches)

---

## 1. Mathematical Derivations

### 1.1 Derivation of {Primary Metric}

**Starting Point:**

{State the initial equation or principle}

```math
{Initial equation}
```

**Step 1: {Description}**

{Explanation of this step}

```math
{Intermediate result}
```

**Step 2: {Description}**

{Explanation of this step}

```math
{Intermediate result}
```

**Final Result:**

```math
{Final derived equation}
```

**Interpretation:**

{What this derivation shows and how to interpret the result}

### 1.2 Derivation of {Secondary Metric}

{Same structure as above}

### 1.3 Derivation of Confidence Intervals

**For {Metric}:**

```math
CI_{95\%} = \hat{\theta} \pm z_{0.975} \cdot SE(\hat{\theta})
```

Where:

- $\hat{\theta}$ = point estimate
- $z_{0.975}$ = 1.96 (standard normal quantile)
- $SE(\hat{\theta})$ = standard error of estimate

**Standard Error Calculation:**

```math
SE(\hat{\theta}) = \sqrt{\frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n(n-1)}}
```

---

## 2. Algorithm Specifications

### 2.1 Algorithm 1: {Name}

**Purpose:** {Brief description}

**Input:** {Specification of inputs}

**Output:** {Specification of outputs}

**Pseudocode:**

```text
ALGORITHM: {Name}
INPUT: data D = {x_1, x_2, ..., x_n}
OUTPUT: result R

1. Initialize variables
2. FOR each element x in D:
   a. Process x
   b. Update running totals
3. Calculate final result
4. RETURN R
```

**Complexity Analysis:**

- Time: O({complexity})
- Space: O({complexity})

### 2.2 Algorithm 2: {Name}

{Same structure}

---

## 3. Code Implementations

### 3.1 Core Functions

```python
"""
Core analysis functions for Episode {X.X}.

These functions implement the primary calculations described in
METHODS_{X.X}_ORIGINAL_ANALYSIS.md.
"""

import numpy as np
import pandas as pd
from scipy import stats
from typing import Tuple, Optional


def calculate_primary_metric(
    data: pd.DataFrame,
    value_col: str,
    group_col: Optional[str] = None
) -> Tuple[float, float, float]:
    """
    Calculate the primary metric with confidence interval.

    Args:
        data: Input DataFrame with analysis data
        value_col: Column name containing values
        group_col: Optional column for grouping

    Returns:
        Tuple of (estimate, lower_ci, upper_ci)

    Example:
        >>> result = calculate_primary_metric(df, 'extinction_rate')
        >>> print(f"Estimate: {result[0]:.4f} [{result[1]:.4f}, {result[2]:.4f}]")
    """
    values = data[value_col].dropna()

    estimate = values.mean()
    se = stats.sem(values)
    ci = stats.t.interval(0.95, len(values)-1, loc=estimate, scale=se)

    return estimate, ci[0], ci[1]


def calculate_trend(
    x: np.ndarray,
    y: np.ndarray
) -> dict:
    """
    Calculate linear trend with full statistics.

    Args:
        x: Independent variable (typically time)
        y: Dependent variable

    Returns:
        Dictionary with slope, intercept, r_squared, p_value, std_err
    """
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

    return {
        'slope': slope,
        'intercept': intercept,
        'r_squared': r_value ** 2,
        'p_value': p_value,
        'std_err': std_err,
        'slope_ci_lower': slope - 1.96 * std_err,
        'slope_ci_upper': slope + 1.96 * std_err
    }


def calculate_e_msy(
    extinctions: int,
    species_count: int,
    years: float
) -> float:
    """
    Calculate extinction rate in E/MSY (extinctions per million species-years).

    Args:
        extinctions: Number of documented extinctions
        species_count: Number of species in assessment
        years: Time period in years

    Returns:
        E/MSY rate

    Note:
        Background rate is approximately 0.1-1 E/MSY.
        Current rates are estimated at 100-1000x background.
    """
    species_years = species_count * years
    return extinctions / species_years * 1_000_000
```

### 3.2 Data Processing Functions

```python
"""
Data processing functions for Episode {X.X}.
"""

def clean_dataset(
    df: pd.DataFrame,
    required_cols: list,
    date_cols: Optional[list] = None
) -> pd.DataFrame:
    """
    Clean and validate dataset.

    Args:
        df: Raw input DataFrame
        required_cols: Columns that must be present and non-null
        date_cols: Columns to convert to datetime

    Returns:
        Cleaned DataFrame
    """
    # Remove rows with missing required columns
    df_clean = df.dropna(subset=required_cols)

    # Convert date columns
    if date_cols:
        for col in date_cols:
            df_clean[col] = pd.to_datetime(df_clean[col])

    # Remove duplicates
    df_clean = df_clean.drop_duplicates()

    return df_clean


def aggregate_by_period(
    df: pd.DataFrame,
    date_col: str,
    value_col: str,
    period: str = 'Y'
) -> pd.DataFrame:
    """
    Aggregate data by time period.

    Args:
        df: Input DataFrame
        date_col: Column with dates
        value_col: Column to aggregate
        period: Pandas period string ('Y', 'M', 'Q', etc.)

    Returns:
        Aggregated DataFrame
    """
    df = df.copy()
    df['period'] = df[date_col].dt.to_period(period)

    return df.groupby('period').agg({
        value_col: ['sum', 'mean', 'count', 'std']
    }).reset_index()
```

### 3.3 Visualization Functions

```python
"""
Visualization functions for Episode {X.X}.
"""

import matplotlib.pyplot as plt

# SME Color Palette
CRISIS_RED = '#d32f2f'
DATA_BLUE = '#1976d2'
HOPE_GREEN = '#388e3c'


def plot_trend(
    x: np.ndarray,
    y: np.ndarray,
    trend_stats: dict,
    title: str,
    xlabel: str,
    ylabel: str,
    save_path: Optional[str] = None
) -> plt.Figure:
    """
    Create trend plot with regression line and confidence band.
    """
    fig, ax = plt.subplots(figsize=(12, 6))

    # Scatter plot
    ax.scatter(x, y, color=DATA_BLUE, alpha=0.6, label='Observed')

    # Trend line
    x_line = np.linspace(x.min(), x.max(), 100)
    y_line = trend_stats['slope'] * x_line + trend_stats['intercept']
    ax.plot(x_line, y_line, color=CRISIS_RED, linewidth=2, label='Trend')

    # Confidence band
    y_upper = (trend_stats['slope_ci_upper'] * x_line +
               trend_stats['intercept'])
    y_lower = (trend_stats['slope_ci_lower'] * x_line +
               trend_stats['intercept'])
    ax.fill_between(x_line, y_lower, y_upper, color=CRISIS_RED, alpha=0.2)

    # Labels
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend()

    # Stats annotation
    stats_text = (f"Slope: {trend_stats['slope']:.4f}/year\n"
                  f"R² = {trend_stats['r_squared']:.4f}\n"
                  f"p = {trend_stats['p_value']:.2e}")
    ax.text(0.02, 0.98, stats_text, transform=ax.transAxes,
            verticalalignment='top', fontfamily='monospace',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=300, bbox_inches='tight')

    return fig
```

---

## 4. Parameter Specifications

### 4.1 Model Parameters

| Parameter | Symbol | Value | Units | Source | Sensitivity |
| --------- | ------ | ----- | ----- | ------ | ----------- |
| {Param 1} | {α} | {0.05} | {-} | {Citation} | {High} |
| {Param 2} | {β} | {1.0} | {per year} | {Derived} | {Medium} |
| {Param 3} | {γ} | {100} | {species} | {IUCN} | {Low} |

### 4.2 Threshold Values

| Threshold | Value | Basis | Reference |
| --------- | ----- | ----- | --------- |
| {Threshold 1} | {Value} | {How determined} | {Citation} |
| {Threshold 2} | {Value} | {How determined} | {Citation} |

### 4.3 Hyperparameter Selection

**Cross-validation approach:**

{Description of how hyperparameters were selected}

**Selected values:**

| Hyperparameter | Search Range | Selected Value | Selection Criterion |
| -------------- | ------------ | -------------- | ------------------- |
| {Hyperparam 1} | [{min}, {max}] | {value} | {Min MSE / Max R² / etc.} |

---

## 5. Computational Details

### 5.1 Runtime Estimates

| Analysis | Dataset Size | Runtime | Hardware |
| -------- | ------------ | ------- | -------- |
| Data processing | {N rows} | {X minutes} | {Specs} |
| Primary analysis | {N rows} | {X minutes} | {Specs} |
| Visualization | {N figures} | {X minutes} | {Specs} |

### 5.2 Memory Requirements

| Component | Peak Memory | Note |
| --------- | ----------- | ---- |
| Raw data loading | {X GB} | {Context} |
| Analysis | {X GB} | {Context} |
| Total | {X GB} | {Recommended minimum} |

### 5.3 Parallel Processing

{If applicable, describe parallel processing approach}

---

## 6. Extended Validation

### 6.1 Bootstrap Results

**Bootstrap Configuration:**

- Number of iterations: {N}
- Sample size: {N}
- Sampling method: {With/Without replacement}

**Results:**

| Statistic | Point Estimate | Bootstrap Mean | Bootstrap SE | 95% CI |
| --------- | -------------- | -------------- | ------------ | ------ |
| {Stat 1} | {Value} | {Value} | {Value} | [{Low}, {High}] |

### 6.2 Cross-Validation Results

| Fold | Training Score | Validation Score |
| ---- | -------------- | ---------------- |
| 1 | {Score} | {Score} |
| 2 | {Score} | {Score} |
| 3 | {Score} | {Score} |
| 4 | {Score} | {Score} |
| 5 | {Score} | {Score} |
| **Mean** | {Score} | {Score} |
| **Std** | {Score} | {Score} |

### 6.3 Residual Diagnostics

{Description and results of residual analysis}

---

## 7. Edge Cases

### 7.1 Missing Data Handling

| Scenario | Frequency | Handling | Justification |
| -------- | --------- | -------- | ------------- |
| {Scenario 1} | {X%} | {Method} | {Reason} |
| {Scenario 2} | {X%} | {Method} | {Reason} |

### 7.2 Extreme Values

| Case | Detection | Treatment | Impact |
| ---- | --------- | --------- | ------ |
| {Case 1} | {How detected} | {How handled} | {Effect on results} |

### 7.3 Special Cases

{Document any special cases that required custom handling}

---

## 8. Alternative Approaches

### 8.1 Alternative Method 1: {Name}

**Description:** {Brief description}

**Comparison:**

| Aspect | Primary Method | Alternative |
| ------ | -------------- | ----------- |
| Assumptions | {List} | {List} |
| Result | {Value} | {Value} |
| Advantages | {List} | {List} |
| Disadvantages | {List} | {List} |

**Why Not Selected:** {Reason for preferring primary method}

### 8.2 Alternative Method 2: {Name}

{Same structure}

---

## Document Metadata

| Field | Value |
| ----- | ----- |
| **Episode** | {X.X} - {Episode Name} |
| **Version** | 1.0.0 |
| **Last Updated** | {YYYY-MM-DD} |

---

> **︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!**
