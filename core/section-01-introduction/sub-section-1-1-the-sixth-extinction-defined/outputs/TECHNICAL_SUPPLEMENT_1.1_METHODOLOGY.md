<!--
✒ Metadata
    - Title: Technical Supplement 1.1: Methodology (SME Edition - v1.0)
    - File Name: TECHNICAL_SUPPLEMENT_1.1_METHODOLOGY.md
    - Relative Path: core/section-01-introduction/sub-section-1-1-the-sixth-extinction-defined/outputs/TECHNICAL_SUPPLEMENT_1.1_METHODOLOGY.md
    - Artifact Type: docs
    - Version: 1.1.0
    - Date: 2026-01-09
    - Update: Friday, January 09, 2026
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Google - Gemini 2.0 Flash
    - Signature: ︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!

✒ Description:
    Detailed explanation of the mathematical formulas, data processing methods,
    and assumptions used to calculate E/MSY (Extinctions per Million Species-Years)
    in Subsection 1.1. This document serves as the mathematical proof for the
    analysis notebooks.

✒ Key Features:
    - Feature 1: Formal definition and derivation of E/MSY
    - Feature 2: Justification for the 1500-2026 time interval
    - Feature 3: Definitions of "Conservative" vs "High" extinction scenarios
    - Feature 4: Handling of IUCN "Data Deficient" (DD) and "Evaluated" counts

✒ Usage Instructions:
    Refer to this document when auditing the formulas in `1.1_validate_current_vertebrate_rates.ipynb`.

✒ Other Important Information:
    - Dependencies: None
    - Related documents: ARTICLE_1.1_THE_SIXTH_EXTINCTION_DEFINED.md
---------
-->

# 🧮 Technical Supplement: E/MSY Methodology

## 1. The Metric: Extinctions per Million Species-Years (E/MSY)

To compare extinction events across geological time (which spans millions of years) with the Anthropocene (which spans centuries), we must normalize the data. The standard metric in paleobiology and conservation science is **E/MSY**.

### 1.1 Formula
The formula calculates the rate at which species go extinct per million years.

$$ E/MSY = \left( \frac{\text{Extinctions}}{\text{Assessed Species} \times \text{Time Interval}} \right) \times 1,000,000 $$

Where:
*   **Extinctions:** The count of species classified as extinct during the interval.
*   **Assessed Species:** The total pool of species monitored (the denominator).
*   **Time Interval:** The duration in years over which the extinctions were recorded.
*   **1,000,000:** The normalization factor to standard "Million Species-Years".

### 1.2 Application in Subsection 1.1
For our analysis of the Sixth Mass Extinction:
*   **Time Interval ($t$):** 526 years (1500 AD to 2026 AD). This aligns with the start of modern records in the IUCN database.
*   **Assessed Species ($S$):** The total count of species evaluated by the IUCN in a specific group (e.g., Mammals, Birds). We do *not* use the estimated total number of species on Earth, only those we have actually checked.

## 2. Scenarios & Assumptions

We present two scenarios to bracket the uncertainty of the current crisis. This prevents alarmism while demonstrating that even the "best case" is catastrophic.

### 2.1 Conservative Scenario (Lower Bound)
*   **Definition:** Only species formally classified as **Extinct (EX)** by the IUCN are counted.
*   **Assumption:** This assumes that all species listed as "Extinct in the Wild" (EW) or "Critically Endangered (Possibly Extinct)" are actually still alive and will recover. This is a highly optimistic biological assumption.

$$ \text{Extinctions}_{conservative} = \text{Count}(EX) $$

### 2.2 High Scenario (Realistic/Upper Bound)
*   **Definition:** Includes **Extinct (EX)**, **Extinct in the Wild (EW)**, and **Possibly Extinct (PE)**.
*   **Justification:** Biologically, a species that exists only in a zoo (EW) or hasn't been seen in 50 years (PE) is functionally extinct in terms of its ecological role. Excluding them artificially lowers the extinction rate.

$$ \text{Extinctions}_{high} = \text{Count}(EX) + \text{Count}(EW) + \text{Count}(PE) $$

## 3. Background Rate Baseline

To determine if the current rate is "high," we compare it to the background rate.

*   **Standard Background Rate:** 1.0 E/MSY (One extinction per million species-years).
*   **Conservative Background Rate:** 2.0 E/MSY (Used by Barnosky et al. 2011).

In our analysis, we compare against **2.0 E/MSY**. This means we are comparing a *Conservative* modern estimate against a *High* background estimate. If the modern rate is still higher, the conclusion is statistically robust.

## 4. Data Handling & Cleaning

### 4.1 IUCN Data Structure
The analysis uses `iucn_table_3_species_by_kingdom_class.csv`.
*   **Parsing:** Numbers in the IUCN CSVs often contain comma separators (e.g., "1,234"). These are stripped during ingestion.
*   **Grouping:** We filter by Class (e.g., `MAMMALIA`, `AMPHIBIA`) to ensure taxonomic precision.

### 4.2 Handling Data Deficient (DD) Species
In this analysis, Data Deficient species are included in the "Total Assessed" count (the denominator) but never in the "Extinct" count (the numerator).
*   **Effect:** This effectively treats all Data Deficient species as "Surviving," which lowers the calculated E/MSY. This is another conservative bias built into our methodology.