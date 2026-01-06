# Data Manifest

## Episode X.X: {Episode Title}

> **Purpose:** Document all data sources, acquisition methods, and processing steps for reproducibility.

---

## Data Sources

### Primary Datasets

| Dataset | Source | URL | Access Date | Format |
| ------- | ------ | --- | ----------- | ------ |
| {Name} | {Organization} | {URL} | {YYYY-MM-DD} | {CSV/JSON/etc} |

### Secondary Datasets

| Dataset | Source | URL | Access Date | Format |
| ------- | ------ | --- | ----------- | ------ |
| {Name} | {Organization} | {URL} | {YYYY-MM-DD} | {CSV/JSON/etc} |

---

## Raw Data Files

| File | Description | Size | Checksum (SHA256) |
| ---- | ----------- | ---- | ----------------- |
| `raw/{filename}` | {Description} | {Size} | {Checksum} |

---

## Processed Data Files

| File | Description | Source | Processing |
| ---- | ----------- | ------ | ---------- |
| `processed/{filename}` | {Description} | {Raw source} | {Processing steps} |

---

## Data Processing Pipeline

### Step 1: Acquisition

```bash
# Commands or scripts used to acquire data
python scripts/acquire.py --source {source}
```

### Step 2: Cleaning

```python
# Key transformations applied
- Removed null values in columns: {columns}
- Standardized date format to: ISO 8601
- Filtered to date range: {start} - {end}
```

### Step 3: Transformation

```python
# Aggregations, calculations, merges performed
- Calculated extinction rate per E/MSY
- Merged with geographic coordinates
- Aggregated by taxonomic group
```

---

## Data Quality Notes

### Known Issues

- {Issue 1 and how handled}
- {Issue 2 and how handled}

### Limitations

- {Limitation 1}
- {Limitation 2}

### Coverage Gaps

- {Gap 1: e.g., "No data for invertebrates before 2000"}
- {Gap 2}

---

## Citation Requirements

### How to Cite Original Data

```text
{Original citation format required by data provider}
```

### Project Citation

```text
Smaltz, D. (2026). Sixth Mass Extinction Documentation Project.
Episode X.X Data Package. https://github.com/{repo}
```

---

## Reproducibility

### Environment

```yaml
python: 3.9+
pandas: 2.0+
numpy: 1.24+
```

### Reproduce Pipeline

```bash
cd research-stacks/X.0-section/X.X-episode
python scripts/pipeline.py --all
```

---

## Version History

| Version | Date | Changes |
| ------- | ---- | ------- |
| 1.0.0 | {Date} | Initial data acquisition |

---

> **︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!**
