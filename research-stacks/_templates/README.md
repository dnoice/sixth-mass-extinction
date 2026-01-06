<!--
✒ Metadata
    - Title: Research Stack Templates README (SME Edition - v1.0)
    - File Name: README.md
    - Relative Path: research-stacks/_templates/README.md
    - Artifact Type: docs
    - Version: 1.0.0
    - Date: 2026-01-05
    - Update: Sunday, January 05, 2026
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Anthropic - Claude Opus 4.5
    - Signature: ︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!

✒ Description:
    Master documentation for all reusable templates in the SME research stacks.
    Templates ensure consistent structure, documentation standards, and
    reproducibility across all 32 episode research deliverables.

✒ Key Features:
    - Feature 1: Article template with 18-section comprehensive structure
    - Feature 2: Jupyter notebook template with SME styling integration
    - Feature 3: Methods documentation template for original analyses
    - Feature 4: Technical supplement for mathematical derivations
    - Feature 5: Uncertainty documentation framework
    - Feature 6: Bibliography template with tiered source system
    - Feature 7: Sources README for archive organization
    - Feature 8: Data manifest for dataset documentation

✒ Usage Instructions:
    Copy templates to episode directories and customize for specific content.
    See individual template files for detailed usage instructions.

✒ Other Important Information:
    - Dependencies: None (documentation only)
    - All templates follow DOCSTRING_STANDARDS.md and MARKDOWN_STANDARDS.md
---------
-->

# Research Stack Templates

> **Purpose:** Standardized templates ensuring consistent structure, documentation,
> and reproducibility across all 32 SME episode research deliverables.
>
> **Total Templates:** 8
>
> **Last Updated:** 2026-01-05

---

## Table of Contents

1. [Template Overview](#template-overview)
2. [Core Deliverable Templates](#core-deliverable-templates)
3. [Methodology Templates](#methodology-templates)
4. [Source Documentation Templates](#source-documentation-templates)
5. [Quick Start Guide](#quick-start-guide)
6. [Template Workflow](#template-workflow)

---

## Template Overview

### Complete Template Inventory

| Template | Lines | Purpose | Target Location |
| -------- | ----- | ------- | --------------- |
| `article_template.md` | ~840 | Comprehensive 18-section article | `article/ARTICLE_X.X.md` |
| `notebook_template.ipynb` | ~200 | Standard Jupyter notebook | `notebooks/*.ipynb` |
| `methods_template.md` | ~450 | Original analysis methodology | `methodology/METHODS_X.X_ORIGINAL_ANALYSIS.md` |
| `technical_supplement_template.md` | ~540 | Extended technical specifications | `methodology/TECHNICAL_SUPPLEMENT_X.X_METHODOLOGY.md` |
| `uncertainty_template.md` | ~400 | Uncertainty analysis framework | `methodology/UNCERTAINTY_DOCUMENTATION.md` |
| `bibliography_template.md` | ~360 | Tiered source bibliography | `bibliography/BIBLIOGRAPHY.md` |
| `sources_readme_template.md` | ~220 | Source archive documentation | `sources/README.md` |
| `data_manifest_template.md` | ~150 | Dataset documentation | `data/metadata/MANIFEST.md` |

---

## Core Deliverable Templates

### Article Template

**File:** `article_template.md`

**Purpose:** Comprehensive deep-dive article covering all aspects of the episode topic.

**Structure (18 Sections):**

1. Executive Summary
2. Historical Context
3. Current State of Knowledge
4. Data and Methodology
5. Primary Analysis
6. Secondary Analysis
7. Case Studies
8. Taxonomic Patterns
9. Temporal Dynamics
10. Causal Mechanisms
11. Interaction Effects
12. Future Projections
13. Uncertainty Analysis
14. Implications
15. Conclusions
16. Glossary
17. References
18. Appendices

**Usage:**

```bash
cp _templates/article_template.md X.X-episode/article/ARTICLE_X.X.md
```

### Notebook Template

**File:** `notebook_template.ipynb`

**Purpose:** Standardized Jupyter notebook with SME styling and structure.

**Structure (8 Sections):**

1. Setup and Configuration
2. Data Acquisition
3. Data Processing
4. Exploratory Analysis
5. Statistical Analysis
6. Visualizations
7. Key Findings Summary
8. Export and Documentation

**Features:**

- SME color palette integration
- Proper docstring header
- Consistent cell organization
- Export-ready visualization settings

**Usage:**

```bash
# Article-aligned notebooks (prefix with 01-, 02-, 03-)
cp _templates/notebook_template.ipynb X.X-episode/notebooks/01-data-acquisition.ipynb
cp _templates/notebook_template.ipynb X.X-episode/notebooks/02-primary-analysis.ipynb
cp _templates/notebook_template.ipynb X.X-episode/notebooks/03-visualization.ipynb

# Novel analysis notebooks (prefix with 04-, 05-, 06-)
cp _templates/notebook_template.ipynb X.X-episode/notebooks/04-novel-analysis-a.ipynb
cp _templates/notebook_template.ipynb X.X-episode/notebooks/05-novel-analysis-b.ipynb
cp _templates/notebook_template.ipynb X.X-episode/notebooks/06-novel-analysis-c.ipynb
```

---

## Methodology Templates

### Methods Documentation

**File:** `methods_template.md`

**Purpose:** Complete methodological documentation enabling reproducibility.

**Structure (10 Sections):**

1. Overview
2. Data Sources (tiered attribution)
3. Data Processing
4. Analytical Methods
5. Key Calculations (with worked examples)
6. Assumptions
7. Validation
8. Reproducibility
9. Limitations
10. References

**Usage:**

```bash
cp _templates/methods_template.md X.X-episode/methodology/METHODS_X.X_ORIGINAL_ANALYSIS.md
```

### Technical Supplement

**File:** `technical_supplement_template.md`

**Purpose:** Extended technical specifications beyond main methods document.

**Structure (8 Sections):**

1. Mathematical Derivations
2. Algorithm Specifications
3. Code Implementations
4. Parameter Specifications
5. Computational Details
6. Extended Validation
7. Edge Cases
8. Alternative Approaches

**Usage:**

```bash
cp _templates/technical_supplement_template.md X.X-episode/methodology/TECHNICAL_SUPPLEMENT_X.X_METHODOLOGY.md
```

### Uncertainty Documentation

**File:** `uncertainty_template.md`

**Purpose:** Comprehensive uncertainty analysis and confidence assessment.

**Structure (9 Sections):**

1. Overview
2. Uncertainty Sources (Aleatory, Epistemic, Model, Scenario)
3. Quantification Methods
4. Sensitivity Analysis
5. Uncertainty Propagation
6. Robustness Checks
7. Confidence Assessment
8. Known Unknowns
9. Recommendations

**Confidence Levels:**

| Level | Evidence | Agreement |
| ----- | -------- | --------- |
| Very High | Robust | High |
| High | Medium-Robust | Medium-High |
| Medium | Limited-Medium | Medium |
| Low | Limited | Low |
| Very Low | Minimal | Low |

**Usage:**

```bash
cp _templates/uncertainty_template.md X.X-episode/methodology/UNCERTAINTY_DOCUMENTATION.md
```

---

## Source Documentation Templates

### Bibliography Template

**File:** `bibliography_template.md`

**Purpose:** Tiered source bibliography with annotations and usage tracking.

**Tier System:**

| Tier | Source Type | Authority Level |
| ---- | ----------- | --------------- |
| Tier 1 | IPBES, IPCC, IUCN, UN | Highest (Intergovernmental) |
| Tier 2 | Peer-reviewed journals | High (Peer review) |
| Tier 3 | Government, universities | Medium-High (Institutional) |
| Tier 4 | NGOs, monitoring programs | Medium (Cross-verification) |

**Features:**

- Annotated bibliography entries
- Citation usage tracking by article section
- BibTeX export compatibility
- Source archive cross-references

**Usage:**

```bash
cp _templates/bibliography_template.md X.X-episode/bibliography/BIBLIOGRAPHY.md
```

### Sources README

**File:** `sources_readme_template.md`

**Purpose:** Documentation for the tiered source archive directory.

**Structure:**

- Tiered source system explanation
- Directory structure documentation
- File naming conventions
- Source archival guidelines
- Citation linking instructions

**Usage:**

```bash
cp _templates/sources_readme_template.md X.X-episode/sources/README.md
```

### Data Manifest

**File:** `data_manifest_template.md`

**Purpose:** Dataset documentation and provenance tracking.

**Usage:**

```bash
cp _templates/data_manifest_template.md X.X-episode/data/metadata/MANIFEST.md
```

---

## Quick Start Guide

### Setting Up a New Episode

```bash
# Navigate to episode directory
cd research-stacks/X.0-section/X.X-episode

# Copy all templates
cp ../../_templates/article_template.md article/ARTICLE_X.X.md
cp ../../_templates/methods_template.md methodology/METHODS_X.X_ORIGINAL_ANALYSIS.md
cp ../../_templates/technical_supplement_template.md methodology/TECHNICAL_SUPPLEMENT_X.X_METHODOLOGY.md
cp ../../_templates/uncertainty_template.md methodology/UNCERTAINTY_DOCUMENTATION.md
cp ../../_templates/bibliography_template.md bibliography/BIBLIOGRAPHY.md
cp ../../_templates/sources_readme_template.md sources/README.md
cp ../../_templates/data_manifest_template.md data/metadata/MANIFEST.md

# Copy notebook templates (6 total)
cp ../../_templates/notebook_template.ipynb notebooks/01-data-acquisition.ipynb
cp ../../_templates/notebook_template.ipynb notebooks/02-primary-analysis.ipynb
cp ../../_templates/notebook_template.ipynb notebooks/03-visualization.ipynb
cp ../../_templates/notebook_template.ipynb notebooks/04-novel-analysis-a.ipynb
cp ../../_templates/notebook_template.ipynb notebooks/05-novel-analysis-b.ipynb
cp ../../_templates/notebook_template.ipynb notebooks/06-novel-analysis-c.ipynb
```

### Customization Checklist

After copying templates:

- [ ] Replace `{X.X}` with episode number (e.g., `1.1`)
- [ ] Replace `{Episode Title}` with actual title
- [ ] Update dates to current date
- [ ] Update version numbers if needed
- [ ] Reference corresponding research blueprint
- [ ] Customize section content for specific topic

---

## Template Workflow

### Recommended Order

```text
1. Sources & Bibliography First
   └── Gather sources → Archive in tiers → Document in bibliography

2. Data Processing
   └── Acquire data → Process → Document in manifest

3. Analysis Notebooks
   └── 01-data-acquisition → 02-primary-analysis → 03-visualization
   └── 04-06: Novel analyses as insights emerge

4. Methodology Documentation
   └── METHODS → TECHNICAL_SUPPLEMENT → UNCERTAINTY

5. Article Synthesis
   └── Integrate findings from all notebooks into article
```

### Episode Directory Structure

```text
X.X-episode/
├── article/
│   └── ARTICLE_X.X.md
├── notebooks/
│   ├── 01-data-acquisition.ipynb
│   ├── 02-primary-analysis.ipynb
│   ├── 03-visualization.ipynb
│   ├── 04-novel-analysis-a.ipynb
│   ├── 05-novel-analysis-b.ipynb
│   └── 06-novel-analysis-c.ipynb
├── methodology/
│   ├── METHODS_X.X_ORIGINAL_ANALYSIS.md
│   ├── TECHNICAL_SUPPLEMENT_X.X_METHODOLOGY.md
│   └── UNCERTAINTY_DOCUMENTATION.md
├── bibliography/
│   └── BIBLIOGRAPHY.md
├── sources/
│   ├── README.md
│   ├── tier-1_authoritative/
│   ├── tier-2_peer-reviewed/
│   ├── tier-3_government/
│   └── tier-4_ngo-verified/
├── data/
│   ├── raw/
│   ├── processed/
│   └── metadata/
│       └── MANIFEST.md
└── visualizations/
    └── exports/
```

---

## Related Documentation

- **Docstring Standards:** [docs/standards/DOCSTRING_STANDARDS.md](../../docs/standards/DOCSTRING_STANDARDS.md)
- **Markdown Standards:** [docs/standards/MARKDOWN_STANDARDS.md](../../docs/standards/MARKDOWN_STANDARDS.md)
- **Source Matrix:** [docs/SOURCE_MATRIX.md](../../docs/SOURCE_MATRIX.md)
- **Master Blueprint:** [docs/MASTER_BLUEPRINT.md](../../docs/MASTER_BLUEPRINT.md)

---

> **︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!**
