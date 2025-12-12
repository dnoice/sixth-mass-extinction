#!/usr/bin/env python3
"""
================================================================================
Title:              Subsection Scaffolding Script
File Name:          scaffold_subsections.py
Relative Path:      scripts/scaffold_subsections.py
Artifact Type:      Script/Automation
Version:            1.0
Date:               2025-12-12
Author:             Dennis 'dnoice' Smaltz
A.I. Acknowledgement: Claude Opus 4
Signature:          ︻デ═—··· 🎯 = Aim Twice, Shoot Once!
================================================================================

DESCRIPTION:
Generates all required template files for each subsection in the SME project.
Creates: README.md, 5 notebooks, uncertainty_documentation.md,
methods_original_analysis.md, technical_supplement.md

USAGE:
    python scripts/scaffold_subsections.py

================================================================================
"""

import os
from pathlib import Path
from datetime import datetime
import json

# Project root
PROJECT_ROOT = Path(__file__).parent.parent

# All sections and subsections
SECTIONS = {
    "1.0_establishing_sixth_mass_extinction": {
        "title": "Establishing the Sixth Mass Extinction",
        "subsections": {
            "1.1_defining_mass_extinction": "Defining Mass Extinction",
            "1.2_iucn_red_list": "IUCN Red List Deep Dive",
            "1.3_living_planet_index": "Living Planet Index",
            "1.4_defaunation": "Defaunation: Empty Forest Syndrome",
            "1.5_skeptics_challenge": "The Skeptics' Challenge"
        }
    },
    "2.0_five_horsemen_drivers": {
        "title": "The Five Horsemen: Primary Drivers",
        "subsections": {
            "2.1_habitat_loss": "Habitat Loss",
            "2.2_invasive_species": "Invasive Species",
            "2.3_pollution": "Pollution",
            "2.4_overexploitation": "Overexploitation",
            "2.5_climate_change": "Climate Change"
        }
    },
    "3.0_taxonomic_deep_dives": {
        "title": "Taxonomic Deep Dives",
        "subsections": {
            "3.1_amphibians": "Amphibian Apocalypse",
            "3.2_insect_decline": "The Insect Decline",
            "3.3_ocean_giants": "Ocean Giants: Sharks and Rays",
            "3.4_global_tree_crisis": "The Global Tree Crisis",
            "3.5_coral_catastrophe": "The Coral Catastrophe"
        }
    },
    "4.0_biome_breakdown": {
        "title": "Biome Breakdown",
        "subsections": {
            "4.1_tropical_rainforest": "Tropical Rainforest",
            "4.2_freshwater": "Freshwater Ecosystems",
            "4.3_islands": "Islands: Extinction Laboratories",
            "4.4_grasslands": "Grasslands: The Invisible Loss"
        }
    },
    "5.0_human_fingerprint": {
        "title": "The Human Fingerprint",
        "subsections": {
            "5.1_agricultural_expansion": "Agricultural Expansion",
            "5.2_urbanization": "Urbanization",
            "5.3_industrial_fishing": "Industrial Fishing",
            "5.4_wildlife_trade": "The Wildlife Trade"
        }
    },
    "6.0_cascading_consequences": {
        "title": "Cascading Consequences",
        "subsections": {
            "6.1_trophic_cascades": "Trophic Cascades",
            "6.2_pollinator_collapse": "Pollinator Collapse",
            "6.3_seed_dispersers": "Seed Dispersers",
            "6.4_ecosystem_engineers": "Ecosystem Engineers"
        }
    },
    "7.0_economic_reckoning": {
        "title": "Economic Reckoning",
        "subsections": {
            "7.1_ecosystem_services": "Ecosystem Services",
            "7.2_agriculture_at_risk": "Agriculture at Risk",
            "7.3_pharmaceutical_pipeline": "The Pharmaceutical Pipeline",
            "7.4_financial_risk": "Financial Risk"
        }
    },
    "8.0_conservation_frontlines": {
        "title": "Conservation Frontlines",
        "subsections": {
            "8.1_protected_areas": "Protected Areas",
            "8.2_species_recovery": "Species Recovery",
            "8.3_ex_situ_conservation": "Ex Situ Conservation",
            "8.4_community_conservation": "Community Conservation"
        }
    },
    "9.0_future_projections": {
        "title": "Future Projections",
        "subsections": {
            "9.1_extinction_debt": "Extinction Debt",
            "9.2_tipping_points": "Tipping Points",
            "9.3_climate_scenarios": "Climate Scenarios",
            "9.4_scenario_modeling": "Scenario Modeling"
        }
    },
    "10.0_solutions_synthesis": {
        "title": "Solutions and Synthesis",
        "subsections": {
            "10.1_bending_the_curve": "Bending the Curve",
            "10.2_policy_levers": "Policy Levers",
            "10.3_technology_innovation": "Technology and Innovation",
            "10.4_economic_transformation": "Economic Transformation",
            "10.5_final_synthesis": "The Final Synthesis"
        }
    }
}

DATE = datetime.now().strftime("%Y-%m-%d")
HEADER_TEMPLATE = """<!--
================================================================================
Title:              {title}
File Name:          {filename}
Relative Path:      {rel_path}
Artifact Type:      {artifact_type}
Version:            0.1 (Template)
Date:               {date}
Update:             Initial Template Creation
Author:             Dennis 'dnoice' Smaltz
A.I. Acknowledgement: Claude Opus 4
Signature:          ︻デ═—··· 🎯 = Aim Twice, Shoot Once!
================================================================================

DESCRIPTION:
{description}

================================================================================
-->

"""


def create_readme(subsection_path: Path, section_num: str, subsection_num: str,
                  section_title: str, subsection_title: str):
    """Create README.md for a subsection."""
    content = HEADER_TEMPLATE.format(
        title=f"Section {subsection_num} README",
        filename="README.md",
        rel_path=f"sections/{subsection_path.parent.name}/{subsection_path.name}/README.md",
        artifact_type="Documentation",
        date=DATE,
        description=f"Overview and reproduction instructions for Section {subsection_num}: {subsection_title}"
    )

    content += f"""# Section {subsection_num}: {subsection_title}

## Overview

*Part of {section_num}: {section_title}*

[Add section overview here]

## Directory Structure

```
{subsection_path.name}/
├── README.md
├── article/
│   ├── article_{subsection_num}_[title].md
│   ├── article_summary.md
│   └── key_findings.md
├── notebooks/
│   ├── 01_data_acquisition.ipynb
│   ├── 02_analysis_core.ipynb
│   ├── 03_visualization.ipynb
│   ├── 04_novel_synthesis.ipynb
│   └── 05_sensitivity_analysis.ipynb
├── figures/
├── data/
│   ├── raw/
│   ├── processed/
│   └── derived/
├── uncertainty_documentation.md
├── methods_original_analysis.md
└── technical_supplement.md
```

## Key Questions

1. [Question 1]
2. [Question 2]
3. [Question 3]

## Data Sources

| Source ID | Name | Used For |
|-----------|------|----------|
| DS-XX-XXX | [Source] | [Purpose] |

## Status

| Deliverable | Status |
|-------------|--------|
| Article | ⬜ Not Started |
| Notebooks (5) | ⬜ Template |
| Figures | ⬜ Not Started |
| Documentation | ⬜ Template |

---

*︻デ═—··· 🎯 = Aim Twice, Shoot Once!*
"""

    readme_path = subsection_path / "README.md"
    if not readme_path.exists():
        readme_path.write_text(content)
        print(f"  Created: {readme_path.name}")


def create_notebook(subsection_path: Path, notebook_num: str, notebook_name: str,
                    purpose: str, subsection_num: str, subsection_title: str):
    """Create a Jupyter notebook template."""
    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    f"# {notebook_num} - {notebook_name}\n",
                    f"## Section {subsection_num}: {subsection_title}\n",
                    "\n",
                    "---\n",
                    "\n",
                    f"**Notebook Purpose**: {purpose}\n",
                    "\n",
                    "**Author**: Dennis 'dnoice' Smaltz  \n",
                    "**AI Acknowledgement**: Claude Opus 4  \n",
                    "**Version**: 0.1 (Template)  \n",
                    f"**Date**: {DATE}  \n",
                    "**Signature**: ︻デ═—··· 🎯 = Aim Twice, Shoot Once!\n",
                    "\n",
                    "---"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## 1. Environment Setup"]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Standard imports\n",
                    "import json\n",
                    "import logging\n",
                    "from pathlib import Path\n",
                    "\n",
                    "import numpy as np\n",
                    "import pandas as pd\n",
                    "\n",
                    "# Configuration\n",
                    "logging.basicConfig(level=logging.INFO)\n",
                    "logger = logging.getLogger(__name__)\n",
                    "\n",
                    "# Paths\n",
                    "SECTION_PATH = Path('../').resolve()\n",
                    "RAW_DATA_PATH = SECTION_PATH / 'data' / 'raw'\n",
                    "PROCESSED_DATA_PATH = SECTION_PATH / 'data' / 'processed'\n",
                    "DERIVED_DATA_PATH = SECTION_PATH / 'data' / 'derived'\n",
                    "FIGURES_PATH = SECTION_PATH / 'figures'\n",
                    "\n",
                    "# Ensure directories exist\n",
                    "for path in [RAW_DATA_PATH, PROCESSED_DATA_PATH, DERIVED_DATA_PATH, FIGURES_PATH]:\n",
                    "    path.mkdir(parents=True, exist_ok=True)\n",
                    "\n",
                    "print(f\"Working on: {SECTION_PATH.name}\")"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## 2. [Next Section]\n\n[Add analysis here]"]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": ["# [Add code here]"]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "---\n",
                    "\n",
                    "*︻デ═—··· 🎯 = Aim Twice, Shoot Once!*"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.10.0"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }

    notebooks_path = subsection_path / "notebooks"
    notebooks_path.mkdir(parents=True, exist_ok=True)

    filename = f"{notebook_num}_{notebook_name.lower().replace(' ', '_')}.ipynb"
    filepath = notebooks_path / filename

    if not filepath.exists():
        with open(filepath, 'w') as f:
            json.dump(notebook, f, indent=1)
        print(f"  Created: notebooks/{filename}")


def create_documentation_file(subsection_path: Path, filename: str, title: str,
                              description: str, subsection_num: str):
    """Create a documentation markdown file."""
    content = HEADER_TEMPLATE.format(
        title=f"{title} - Section {subsection_num}",
        filename=filename,
        rel_path=f"sections/.../{subsection_path.name}/{filename}",
        artifact_type="Documentation",
        date=DATE,
        description=description
    )

    if "uncertainty" in filename:
        content += f"""# UNCERTAINTY DOCUMENTATION
## Section {subsection_num}

---

## 1. KEY CLAIMS AND CONFIDENCE LEVELS

### Claim {subsection_num}.1: [Primary Claim]

| Aspect | Assessment |
|--------|------------|
| **Claim Statement** | [Exact claim text] |
| **Confidence Level** | ⬜ Very High / ⬜ High / ⬜ Medium / ⬜ Low / ⬜ Very Low |
| **Uncertainty Range** | [e.g., 95% CI: X to Y] |
| **Supporting Evidence** | [List of sources] |

---

## 2. DATA QUALITY ASSESSMENT

| Source ID | Source Name | Quality Score | Key Limitations |
|-----------|-------------|---------------|-----------------|
| DS-XX-XXX | [Source] | [1-5] | [Limitations] |

---

## 3. SENSITIVITY ANALYSIS SUMMARY

[See notebook 05_sensitivity_analysis.ipynb]

---

*︻デ═—··· 🎯 = Aim Twice, Shoot Once!*
"""
    elif "methods" in filename:
        content += f"""# METHODS: ORIGINAL ANALYSIS
## Section {subsection_num}

---

## 1. DATA SOURCES AND ACQUISITION

### Primary Data Sources

| Source | Access Method | Date | Records |
|--------|---------------|------|---------|
| [Source] | [Method] | [Date] | [N] |

---

## 2. DATA PROCESSING

### 2.1 Data Cleaning

[Describe cleaning steps]

---

## 3. ANALYTICAL METHODS

### 3.1 [Method Name]

**Method**: [Description]

**Mathematical Formulation**:
[Add equations]

---

## 4. REPRODUCIBILITY

```bash
# Run notebooks in order
jupyter notebook 01_data_acquisition.ipynb
jupyter notebook 02_analysis_core.ipynb
# ... etc
```

---

*︻デ═—··· 🎯 = Aim Twice, Shoot Once!*
"""
    else:  # technical supplement
        content += f"""# TECHNICAL SUPPLEMENT
## Section {subsection_num}

---

## 1. MATHEMATICAL FOUNDATIONS

[Add detailed derivations]

---

## 2. EXTENDED DATA TABLES

[Add supplementary tables]

---

## 3. SUPPLEMENTARY FIGURES

[List supplementary figures]

---

## 4. CODE DOCUMENTATION

[Document key functions]

---

## 5. GLOSSARY

| Term | Definition |
|------|------------|
| [Term] | [Definition] |

---

## 6. REFERENCES

[Add references]

---

*︻デ═—··· 🎯 = Aim Twice, Shoot Once!*
"""

    filepath = subsection_path / filename
    if not filepath.exists():
        filepath.write_text(content)
        print(f"  Created: {filename}")


def scaffold_subsection(section_path: Path, subsection_dir: str,
                        section_num: str, section_title: str,
                        subsection_num: str, subsection_title: str):
    """Create all template files for a subsection."""
    subsection_path = section_path / subsection_dir

    # Ensure all directories exist
    for subdir in ["article", "notebooks", "figures", "data/raw", "data/processed", "data/derived"]:
        (subsection_path / subdir).mkdir(parents=True, exist_ok=True)

    print(f"\n📁 {subsection_num}: {subsection_title}")

    # Create README
    create_readme(subsection_path, section_num, subsection_num, section_title, subsection_title)

    # Create all 5 notebooks
    notebooks = [
        ("01", "Data Acquisition", "Data sourcing, cleaning, and validation"),
        ("02", "Analysis Core", "Primary statistical and analytical work"),
        ("03", "Visualization", "Figure generation and visual analysis"),
        ("04", "Novel Synthesis", "Original cross-dataset analysis and insight generation"),
        ("05", "Sensitivity Analysis", "Uncertainty quantification and robustness testing")
    ]

    for num, name, purpose in notebooks:
        create_notebook(subsection_path, num, name, purpose, subsection_num, subsection_title)

    # Create documentation files
    create_documentation_file(
        subsection_path, "uncertainty_documentation.md",
        "Uncertainty Documentation",
        f"Quantified uncertainties, data gaps, and limitations for Section {subsection_num}",
        subsection_num
    )

    create_documentation_file(
        subsection_path, "methods_original_analysis.md",
        "Methods - Original Analysis",
        f"Detailed methodology for novel analysis in Section {subsection_num}",
        subsection_num
    )

    create_documentation_file(
        subsection_path, "technical_supplement.md",
        "Technical Supplement",
        f"Extended technical details, equations, and code for Section {subsection_num}",
        subsection_num
    )


def main():
    """Scaffold all subsections."""
    print("=" * 60)
    print("SCAFFOLDING SME SUBSECTIONS")
    print("=" * 60)

    sections_path = PROJECT_ROOT / "sections"
    sections_path.mkdir(exist_ok=True)

    total_created = 0

    for section_dir, section_info in SECTIONS.items():
        section_path = sections_path / section_dir
        section_path.mkdir(exist_ok=True)

        section_num = section_dir.split("_")[0]
        section_title = section_info["title"]

        print(f"\n{'='*60}")
        print(f"SECTION {section_num}: {section_title}")
        print("=" * 60)

        for subsection_dir, subsection_title in section_info["subsections"].items():
            subsection_num = subsection_dir.split("_")[0]
            scaffold_subsection(
                section_path, subsection_dir,
                section_num, section_title,
                subsection_num, subsection_title
            )
            total_created += 1

    print("\n" + "=" * 60)
    print(f"COMPLETE! Scaffolded {total_created} subsections.")
    print("=" * 60)


if __name__ == "__main__":
    main()
