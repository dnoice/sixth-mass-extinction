<!--
✒ Metadata
    - Title: Research Stacks Master Index (SME Edition - v1.0)
    - File Name: README.md
    - Relative Path: research-stacks/README.md
    - Artifact Type: docs
    - Version: 1.0.0
    - Date: 2026-01-04
    - Update: Saturday, January 04, 2026
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Anthropic - Claude Opus 4.5
    - Signature: ︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!

✒ Description:
    Master index for the Research Stacks directory - the working space for all
    data acquisition, analysis, visualization, and article creation for the
    Sixth Mass Extinction 10-part documentary series with 32 episodes.

✒ Key Features:
    - Feature 1: 10 parent sections mirroring research blueprints
    - Feature 2: 32 sub-section "episodes" with complete workflows
    - Feature 3: Standardized internal structure for each episode
    - Feature 4: Shared templates and utilities
    - Feature 5: Integrated data → analysis → visualization → article pipeline

✒ Other Important Information:
    - Dependencies: Python 3.9+, Jupyter, pandas, matplotlib, plotly
    - Related: docs/project-blueprints/research-blueprints/
    - Workflow: Blueprint → Data → Notebook → Visualization → Article
---------
-->

# Research Stacks

## Sixth Mass Extinction - 10-Part Series Production Hub

> **Purpose:** Working directory for data acquisition, analysis, visualization, and article creation. Each sub-section produces one "episode" in the 10-part documentary series.

---

## Series Overview

| Series | Title | Episodes | Focus |
| ------ | ----- | -------- | ----- |
| **1.0** | Establishing the Crisis | 4 | Extinction rates, magnitude, hotspots, history |
| **2.0** | Primary Drivers | 6 | Habitat, extraction, climate, pollution, exploitation, invasives |
| **3.0** | Ecological Collapse | 3 | Trophic cascades, ecosystem services, homogenization |
| **4.0** | Economic Systems | 4 | Capitalism, corporate power, government, consumption |
| **5.0** | Environmental Justice | 2 | Indigenous peoples, frontline communities |
| **6.0** | What We're Losing | 3 | Functional diversity, coextinction, evolution |
| **7.0** | Tipping Points | 2 | Planetary boundaries, irreversible losses |
| **8.0** | Failed Solutions | 2 | Tech optimism, conservation limits |
| **9.0** | Timeline & Urgency | 2 | Acceleration, thresholds |
| **10.0** | Synthesis | 4 | Systemic causes, survival, requirements, conclusion |
| | **TOTAL** | **32 Episodes** | |

---

## Directory Structure

```tree
research-stacks/
├── README.md                           # This file
├── _templates/                         # Reusable templates
│   ├── notebook_template.ipynb         # Standard notebook structure
│   ├── article_template.md             # Article format template
│   └── data_manifest_template.md       # Data documentation template
│
├── _shared/                            # Cross-section resources
│   ├── data/                           # Common datasets (IUCN, LPI, etc.)
│   ├── utils/                          # Shared Python utilities
│   └── styles/                         # Visualization style configs
│
├── 1.0-establishing-crisis/            # Series 1
│   ├── README.md                       # Section overview
│   ├── 1.1-extinction-rates/           # Episode 1.1
│   │   ├── README.md                   # Episode overview
│   │   ├── data/                       # Episode data
│   │   │   ├── raw/                    # Original source data
│   │   │   ├── processed/              # Cleaned data
│   │   │   └── metadata/               # Data documentation
│   │   ├── notebooks/                  # Jupyter notebooks
│   │   ├── visualizations/             # Charts and figures
│   │   │   ├── figures/                # Static (PNG, SVG)
│   │   │   ├── interactive/            # Interactive (HTML, Plotly)
│   │   │   └── exports/                # Publication-ready
│   │   ├── article/                    # Written content
│   │   │   ├── draft.md                # Working draft
│   │   │   └── assets/                 # Article media
│   │   └── scripts/                    # Python scripts
│   ├── 1.2-magnitude-of-risk/
│   ├── 1.3-geographic-hotspots/
│   └── 1.4-previous-extinctions/
│
├── 2.0-primary-drivers/                # Series 2 (6 episodes)
├── 3.0-ecological-collapse/            # Series 3 (3 episodes)
├── 4.0-economic-systems/               # Series 4 (4 episodes)
├── 5.0-environmental-justice/          # Series 5 (2 episodes)
├── 6.0-what-were-losing/               # Series 6 (3 episodes)
├── 7.0-tipping-points/                 # Series 7 (2 episodes)
├── 8.0-failed-solutions/               # Series 8 (2 episodes)
├── 9.0-timeline-urgency/               # Series 9 (2 episodes)
└── 10.0-synthesis/                     # Series 10 (4 episodes)
```

---

## Quick Navigation

### Series 1: Establishing the Crisis

| Episode | Title | Status |
| ------- | ----- | ------ |
| [1.1](./1.0-establishing-crisis/1.1-extinction-rates/) | Extinction Rates | Not Started |
| [1.2](./1.0-establishing-crisis/1.2-magnitude-of-risk/) | Magnitude of Risk | Not Started |
| [1.3](./1.0-establishing-crisis/1.3-geographic-hotspots/) | Geographic Hotspots | Not Started |
| [1.4](./1.0-establishing-crisis/1.4-previous-extinctions/) | Previous Extinctions | Not Started |

### Series 2: Primary Drivers

| Episode | Title | Status |
| ------- | ----- | ------ |
| [2.1](./2.0-primary-drivers/2.1-habitat-destruction/) | Habitat Destruction | Not Started |
| [2.2](./2.0-primary-drivers/2.2-resource-extraction/) | Resource Extraction | Not Started |
| [2.3](./2.0-primary-drivers/2.3-climate-change/) | Climate Change | Not Started |
| [2.4](./2.0-primary-drivers/2.4-pollution/) | Pollution | Not Started |
| [2.5](./2.0-primary-drivers/2.5-overexploitation/) | Overexploitation | Not Started |
| [2.6](./2.0-primary-drivers/2.6-invasive-species/) | Invasive Species | Not Started |

### Series 3: Ecological Collapse

| Episode | Title | Status |
| ------- | ----- | ------ |
| [3.1](./3.0-ecological-collapse/3.1-trophic-cascades/) | Trophic Cascades | Not Started |
| [3.2](./3.0-ecological-collapse/3.2-ecosystem-service-failures/) | Ecosystem Service Failures | Not Started |
| [3.3](./3.0-ecological-collapse/3.3-biotic-homogenization/) | Biotic Homogenization | Not Started |

### Series 4: Economic Systems

| Episode | Title | Status |
| ------- | ----- | ------ |
| [4.1](./4.0-economic-systems/4.1-capitalism-infinite-growth/) | Capitalism & Infinite Growth | Not Started |
| [4.2](./4.0-economic-systems/4.2-corporate-power/) | Corporate Power | Not Started |
| [4.3](./4.0-economic-systems/4.3-governmental-failure/) | Governmental Failure | Not Started |
| [4.4](./4.0-economic-systems/4.4-consumption-inequality/) | Consumption Inequality | Not Started |

### Series 5: Environmental Justice

| Episode | Title | Status |
| ------- | ----- | ------ |
| [5.1](./5.0-environmental-justice/5.1-indigenous-peoples/) | Indigenous Peoples | Not Started |
| [5.2](./5.0-environmental-justice/5.2-frontline-communities/) | Frontline Communities | Not Started |

### Series 6: What We're Losing

| Episode | Title | Status |
| ------- | ----- | ------ |
| [6.1](./6.0-what-were-losing/6.1-functional-diversity/) | Functional Diversity | Not Started |
| [6.2](./6.0-what-were-losing/6.2-coextinction/) | Coextinction | Not Started |
| [6.3](./6.0-what-were-losing/6.3-evolutionary-potential/) | Evolutionary Potential | Not Started |

### Series 7: Tipping Points

| Episode | Title | Status |
| ------- | ----- | ------ |
| [7.1](./7.0-tipping-points/7.1-planetary-boundaries/) | Planetary Boundaries | Not Started |
| [7.2](./7.0-tipping-points/7.2-irreversible-losses/) | Irreversible Losses | Not Started |

### Series 8: Failed Solutions

| Episode | Title | Status |
| ------- | ----- | ------ |
| [8.1](./8.0-failed-solutions/8.1-technological-optimism/) | Technological Optimism | Not Started |
| [8.2](./8.0-failed-solutions/8.2-conservation-insufficiency/) | Conservation Insufficiency | Not Started |

### Series 9: Timeline & Urgency

| Episode | Title | Status |
| ------- | ----- | ------ |
| [9.1](./9.0-timeline-urgency/9.1-extinction-acceleration/) | Extinction Acceleration | Not Started |
| [9.2](./9.0-timeline-urgency/9.2-irreversible-thresholds/) | Irreversible Thresholds | Not Started |

### Series 10: Synthesis

| Episode | Title | Status |
| ------- | ----- | ------ |
| [10.1](./10.0-synthesis/10.1-systemic-causation/) | Systemic Causation | Not Started |
| [10.2](./10.0-synthesis/10.2-survival-question/) | Survival Question | Not Started |
| [10.3](./10.0-synthesis/10.3-what-actually-required/) | What's Actually Required | Not Started |
| [10.4](./10.0-synthesis/10.4-tragic-conclusion/) | Tragic Conclusion | Not Started |

---

## Workflow per Episode

```mermaid
flowchart LR
    A[Blueprint] --> B[Data Acquisition]
    B --> C[Data Processing]
    C --> D[Analysis Notebook]
    D --> E[Visualizations]
    E --> F[Article Draft]
    F --> G[Final Article]

    style A fill:#e1f5fe
    style G fill:#c8e6c9
```

### 1. Blueprint Reference

- Read corresponding blueprint from `docs/project-blueprints/research-blueprints/`
- Extract required data sources, key statistics, visualization targets

### 2. Data Acquisition

- Download/acquire raw data to `data/raw/`
- Document sources in `data/metadata/`
- Use SOURCE_MATRIX.md citations

### 3. Data Processing

- Clean and transform data in `notebooks/01-acquisition.ipynb`
- Save processed data to `data/processed/`

### 4. Analysis

- Perform analysis in `notebooks/02-analysis.ipynb`
- Calculate key statistics
- Identify patterns and insights

### 5. Visualization

- Create visualizations in `notebooks/03-visualization.ipynb`
- Export static figures to `visualizations/figures/`
- Export interactive charts to `visualizations/interactive/`
- Create publication-ready versions in `visualizations/exports/`

### 6. Article Creation

- Write draft in `article/draft.md`
- Follow article template structure
- Integrate visualizations and statistics

---

## Deliverable Targets

| Deliverable | Target per Episode |
| ----------- | ------------------ |
| **Article Length** | 8,000-10,000 words |
| **Visualizations** | 10-12 figures |
| **Data Sources** | 8+ foundational, 50-70 supporting |
| **Interactive Elements** | 2-3 per episode |
| **Total Project** | 256,000-320,000 words |

---

## Templates

| Template | Purpose | Location |
| -------- | ------- | -------- |
| Notebook Template | Standard notebook structure | `_templates/notebook_template.ipynb` |
| Article Template | Article markdown format | `_templates/article_template.md` |
| Data Manifest | Data documentation | `_templates/data_manifest_template.md` |

---

## Shared Resources

| Resource | Purpose | Location |
| -------- | ------- | -------- |
| Common Data | IUCN, LPI, IPBES datasets | `_shared/data/` |
| Utilities | Python helper functions | `_shared/utils/` |
| Styles | Visualization configs | `_shared/styles/` |

---

## Getting Started

### Prerequisites

```bash
# Python environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install dependencies
pip install pandas numpy matplotlib seaborn plotly jupyter rich
```

### Starting a New Episode

1. Navigate to the episode directory
2. Read the corresponding blueprint
3. Copy templates from `_templates/`
4. Follow the workflow: Data → Notebook → Viz → Article

---

> **︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!**
