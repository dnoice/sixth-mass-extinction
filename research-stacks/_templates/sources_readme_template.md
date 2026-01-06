<!--
✒ Metadata
    - Title: Sources Directory README Template (SME Edition - v1.0)
    - File Name: sources_readme_template.md
    - Relative Path: research-stacks/_templates/sources_readme_template.md
    - Artifact Type: docs
    - Version: 1.0.0
    - Date: 2026-01-05
    - Update: Sunday, January 05, 2026
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Anthropic - Claude Opus 4.5
    - Signature: ︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!

✒ Description:
    Template for README files in episode sources/ directories explaining
    the tiered source system and directory structure.

✒ Key Features:
    - Feature 1: Tiered source system explanation
    - Feature 2: Directory structure documentation
    - Feature 3: File naming conventions
    - Feature 4: Source archival guidelines
    - Feature 5: Citation linking instructions

✒ Usage Instructions:
    Copy to episode sources/ directory:
        cp _templates/sources_readme_template.md X.X-episode/sources/README.md
---------
-->

# Sources Archive

## Episode {X.X}: {Episode Title}

> **Purpose:** Archived source documents supporting the analysis and article.
>
> **Total Documents:** {N}
>
> **Last Updated:** {YYYY-MM-DD}

---

## Tiered Source System

The SME project uses a four-tier source classification system to ensure transparency about source authority and reliability.

### Tier 1: Authoritative International Assessments

**Directory:** `tier-1_authoritative/`

**Sources Include:**

- IPBES (Intergovernmental Science-Policy Platform on Biodiversity and Ecosystem Services)
- IPCC (Intergovernmental Panel on Climate Change)
- IUCN (International Union for Conservation of Nature)
- UN Environment Programme reports
- Convention on Biological Diversity assessments

**Authority Level:** Highest - Intergovernmental review processes

**Verification:** Multi-government approval, extensive peer review

### Tier 2: Peer-Reviewed Literature

**Directory:** `tier-2_peer-reviewed/`

**Sources Include:**

- Journal articles from peer-reviewed scientific publications
- Review articles and meta-analyses
- Peer-reviewed books and book chapters

**Authority Level:** High - Peer review process

**Verification:** Anonymous peer review, editorial oversight

### Tier 3: Government and Institutional Sources

**Directory:** `tier-3_government/`

**Sources Include:**

- National government agency reports
- State/provincial environmental assessments
- University research reports (non-peer-reviewed)
- National museum and herbarium data
- Government statistical databases

**Authority Level:** Medium-High - Institutional review

**Verification:** Internal agency review, professional standards

### Tier 4: Verified NGO and Monitoring Data

**Directory:** `tier-4_ngo-verified/`

**Sources Include:**

- Conservation NGO reports (WWF, Conservation International, etc.)
- Long-term monitoring program data
- Citizen science datasets (with quality controls)
- Industry association reports (verified)

**Authority Level:** Medium - Requires cross-verification

**Verification:** Cross-checked against Tier 1-3 sources where possible

---

## Directory Structure

```text
sources/
├── README.md                    # This file
├── tier-1_authoritative/
│   ├── .gitkeep
│   └── {source_documents}
├── tier-2_peer-reviewed/
│   ├── .gitkeep
│   └── {source_documents}
├── tier-3_government/
│   ├── .gitkeep
│   └── {source_documents}
└── tier-4_ngo-verified/
    ├── .gitkeep
    └── {source_documents}
```

---

## File Naming Convention

### Format

```text
{AuthorOrOrg}_{Year}_{ShortTitle}.{ext}
```

### Examples

- `IPBES_2019_GlobalAssessment.pdf`
- `Smith_2023_ExtinctionRates.pdf`
- `USFWS_2024_EndangeredSpeciesList.xlsx`
- `WWF_2022_LivingPlanetReport.pdf`

### Guidelines

- Use underscores, not spaces
- Keep short title to 3-4 words maximum
- Include year of publication
- Use standard file extensions (.pdf, .xlsx, .csv, .json)

---

## Source Document Contents

### Tier 1: Authoritative International Assessments

| File | Source | Description | Citation ID |
| ---- | ------ | ----------- | ----------- |
| {filename} | {Source} | {Brief description} | T1-{XX} |

### Tier 2: Peer-Reviewed Literature

| File | Source | Description | Citation ID |
| ---- | ------ | ----------- | ----------- |
| {filename} | {Journal} | {Brief description} | T2-{XX} |

### Tier 3: Government and Institutional Sources

| File | Source | Description | Citation ID |
| ---- | ------ | ----------- | ----------- |
| {filename} | {Agency} | {Brief description} | T3-{XX} |

### Tier 4: Verified NGO and Monitoring Data

| File | Source | Description | Citation ID |
| ---- | ------ | ----------- | ----------- |
| {filename} | {Organization} | {Brief description} | T4-{XX} |

---

## Usage Guidelines

### Adding New Sources

1. Determine appropriate tier based on source type
2. Download/obtain source document
3. Rename following naming convention
4. Place in appropriate tier directory
5. Add entry to BIBLIOGRAPHY.md with citation ID
6. Update this README with file listing

### Citing Sources

When citing in the article:

```markdown
The IPBES Global Assessment (2019) reports that... [T1-01]
```

Link citations to BIBLIOGRAPHY.md entries using citation IDs.

### Large Files

For files >50MB:

- Store externally (institutional repository, Zenodo, etc.)
- Include URL in BIBLIOGRAPHY.md
- Note external storage in this README

---

## Related Documentation

- **Bibliography:** [../bibliography/BIBLIOGRAPHY.md](../bibliography/BIBLIOGRAPHY.md)
- **Data Manifest:** [../data/metadata/MANIFEST.md](../data/metadata/MANIFEST.md)
- **Methods:** [../methodology/METHODS_{X.X}_ORIGINAL_ANALYSIS.md](../methodology/METHODS_{X.X}_ORIGINAL_ANALYSIS.md)

---

> **︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!**
