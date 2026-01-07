<!--
✒ Metadata
    - Title: Factual Accuracy Audit - Flight Extinguished (SME Edition - v1.0)
    - File Name: AUDIT_flight_extinguished_2026-01-06.md
    - Relative Path: audit-reports/AUDIT_flight_extinguished_2026-01-06.md
    - Artifact Type: docs
    - Version: 1.0.0
    - Date: 2026-01-06
    - Update: Monday, January 06, 2026
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Anthropic - Claude Opus 4.5
    - Signature: ︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!

✒ Description:
    Comprehensive factual accuracy audit for "Flight Extinguished" article.
    Verifies scientific claims about bird mortality, population decline,
    and anthropogenic threats against peer-reviewed literature.

✒ Key Features:
    - Feature 1: Verification against Rosenberg et al. 2019 (Science)
    - Feature 2: Cross-reference with Loss et al. studies on mortality sources
    - Feature 3: IUCN/BirdLife State of World's Birds 2022 verification
    - Feature 4: Ecosystem service value verification

✒ Other Important Information:
    - Audit Standard: All scientific claims verified against Tier 1-2 sources
    - Reference Sources: Science, Nature Communications, PLOS ONE, BirdLife International
---------
-->

# Factual Accuracy Audit

> **Article:** Flight Extinguished: Glass, Gas, and Watch Them Crash
>
> **Audit Date:** 2026-01-06
>
> **Status:** CORRECTIONS APPLIED

---

## Executive Summary

The article "Flight Extinguished" presents a comprehensive account of anthropogenic bird mortality. The core claims about the 2.9 billion bird decline are well-supported by Rosenberg et al. (2019). However, several specific mortality figures contain numerical errors when compared to their source studies, and some claims could not be verified or appear conflated from different sources.

**Issues Found:** 0 Critical | 5 Errors | 3 Caution | 2 Minor

---

## Verified Claims (Accurate)

### Population Decline (Rosenberg et al. 2019)

| Claim | Line | Verification | Source |
|-------|------|--------------|--------|
| 2.9 billion birds lost in North America | 19 | ✓ VERIFIED | Rosenberg et al. 2019, Science |
| 29% of breeding birds lost | 21 | ✓ VERIFIED | Rosenberg et al. 2019 |
| Grassland species down 53% | 23 | ✓ VERIFIED | Rosenberg et al. 2019 |
| 700+ million grassland birds lost | 23 | ✓ VERIFIED | Rosenberg et al. 2019 |
| Forest birds: billion lost | 23 | ✓ VERIFIED | Rosenberg et al. 2019 |
| Shorebirds declined 37% | 23 | ✓ VERIFIED | Rosenberg et al. 2019 |

### Window Collisions (Loss et al. 2014)

| Claim | Line | Verification | Source |
|-------|------|--------------|--------|
| 365 million to 1 billion window deaths annually | 39 | ✓ VERIFIED | Loss et al. 2014, Condor |
| Residential: 253-988 million | 41 | ✓ VERIFIED | Loss et al. 2014 |
| Low-rise commercial: 339-976 million | 41 | ✓ VERIFIED | Loss et al. 2014 |
| High-rise: 16-42 million | 41 | ✓ VERIFIED | Loss et al. 2014 |

### Light Pollution

| Claim | Line | Verification | Source |
|-------|------|--------------|--------|
| 83% of world population under light-polluted skies | 73 | ✓ VERIFIED | Falchi et al. 2016, Science Advances |
| 9/11 Tribute in Light affects 160,000 birds/year | 79 | ✓ VERIFIED | Van Doren et al. 2017, PNAS |
| Communication towers: 6.8 million deaths | 77 | ✓ VERIFIED* | Longcore et al. 2012, PLOS ONE |

### Other Verified Claims

| Claim | Line | Verification | Source |
|-------|------|--------------|--------|
| McCormick Place: 40,000+ birds 1978-present | 41 | ✓ VERIFIED | Field Museum records |
| Deepwater Horizon: ~800,000 birds killed | 63 | ✓ VERIFIED | Haney et al. 2014 |
| 35% global wetland loss since 1970 | 91 | ✓ VERIFIED | Ramsar Convention |
| 150 million years of bird evolution | 35, 149 | ✓ VERIFIED | Paleontological record |
| Red knot depends on Delaware Bay horseshoe crabs | 95 | ✓ VERIFIED | Well-documented |
| 90% tropical trees depend on animal dispersers | 125 | ✓ VERIFIED | Multiple studies |

---

## Issues Identified

### ERROR-001: Cat Predation Numbers

**Location:** Line 107

**Current Text:**
> "Domestic and feral cats kill between 1.4 and 4.4 billion birds in the United States annually."

**Problem:**
The Loss et al. 2013 study in Nature Communications states **1.3–4.0 billion birds**, not 1.4–4.4 billion.

**Source:** [Loss et al. 2013, Nature Communications](https://www.nature.com/articles/ncomms2380)

**Recommended Correction:**
> "Domestic and feral cats kill between 1.3 and 4.0 billion birds in the United States annually."

---

### ERROR-002: Vehicle Collision Lower Bound

**Location:** Line 113

**Current Text:**
> "Add vehicle collisions: 200 to 340 million annually."

**Problem:**
The Loss et al. 2014 study states **89–340 million**, not 200–340 million. The lower bound is significantly overstated.

**Source:** [Loss et al. 2014, Journal of Wildlife Management](https://wildlife.onlinelibrary.wiley.com/doi/10.1002/jwmg.721)

**Recommended Correction:**
> "Add vehicle collisions: 89 to 340 million annually."

---

### ERROR-003: Power Line Mortality Misattribution

**Location:** Line 113

**Current Text:**
> "Power line electrocutions: 8 to 57 million."

**Problem:**
The 8–57 million figure refers to **collision** mortality at power lines, not electrocution. The actual electrocution estimate is **0.9–11.6 million**. Total power line mortality (collision + electrocution) is 12–64 million.

**Source:** [Loss et al. 2014, PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0101565)

**Recommended Correction:**
> "Power line collisions and electrocutions: 12 to 64 million."

OR if specifying both:
> "Power line collisions: 8 to 57 million. Power line electrocutions: 0.9 to 11.6 million."

---

### ERROR-004: Southeast Asian Rainforest Loss

**Location:** Line 91

**Current Text:**
> "Eighty percent of Southeast Asian rainforests have been logged."

**Problem:**
This figure could not be verified and appears overstated. Available data suggests:

- ~50% of original forest cover lost in region
- 90%+ of Philippine old-growth rainforests cut
- 50% of Bornean rainforest lost 1973-2015
- The 80% figure may conflate "logged" (including selective logging) with "deforested"

**Source:** Multiple sources including Earth.org, GRID-Arendal

**Recommended Correction:**
> "More than half of Southeast Asian rainforests have been logged or degraded, with some areas like the Philippines losing over ninety percent of old-growth forest."

---

### ERROR-005: Guam Bird Extinction Count

**Location:** Line 127

**Current Text:**
> "it eliminated twelve of the island's thirteen native forest bird species"

**Problem:**
Sources indicate Guam had **12 native forest bird species** (not 13), of which **10 are extinct** and **2 are functionally extinct**. The "12 of 13" formulation doesn't match available data.

**Source:** [NSF](https://www.nsf.gov/news/guams-birds-gone-can-forest-survive), [University of Washington](https://www.washington.edu/news/2008/08/21/brown-tree-snake-could-mean-guam-will-lose-more-than-its-birds-2/)

**Recommended Correction:**
> "it eliminated ten of the island's twelve native forest bird species, with the remaining two now functionally extinct"

OR:
> "it eliminated virtually all of Guam's native forest birds"

---

### CAUTION-001: Single Tower Mortality Range

**Location:** Line 77

**Current Text:**
> "A single tower can kill between five thousand and fifty thousand birds per year."

**Problem:**
This specific per-tower range could not be verified in peer-reviewed literature. Studies focus on aggregate mortality (6.8 million total) and tower height correlations, but specific "5,000-50,000 per tower" figures were not found.

**Source:** Longcore et al. 2012 does not provide this specific per-tower range

**Recommendation:** Verify source or revise to: "Individual tall towers can kill thousands of birds annually, with the tallest towers responsible for the majority of mortality."

---

### CAUTION-002: McCormick Place Peak Night Mortality

**Location:** Line 41

**Current Text:**
> "On peak nights during migration, volunteers collected over fifteen hundred bodies from a single building."

**Problem:**
Field Museum records indicate the highest single-night mortality at McCormick Place was:

- **961 birds** on October 4-5, 2023 (described as "by far the most")
- Prior record was "around 200" per night

The "fifteen hundred" figure could not be verified.

**Source:** [CBS Chicago](https://www.cbsnews.com/chicago/news/nearly-1000-migrating-birds-killed-after-crashing-into-mccormick-place/), [Axios Chicago](https://www.axios.com/local/chicago/2025/01/10/mccormick-place-bird-collisions-95-percent-decline)

**Recommendation:** Verify source or revise to: "On peak nights during migration, volunteers have collected nearly a thousand bodies from a single building."

---

### CAUTION-003: Bird Pest Suppression Economic Value

**Location:** Line 125

**Current Text:**
> "the ecosystem service of pest suppression provided by birds is valued at four to five billion dollars annually in the United States alone"

**Problem:**
This specific figure could not be verified for birds. The $4.5 billion figure commonly cited is for **native insects** providing pest control (Losey & Vaughan 2006). Bird-specific pest suppression is typically cited as "millions of dollars" in aggregate, not billions.

**Source:** Xerces Society cites $4.5 billion for insect pest control; bird-specific figures are lower

**Recommendation:** Verify source or revise to attribute appropriately, or soften to: "Birds provide pest suppression services worth hundreds of millions of dollars annually."

---

### MINOR-001: IUCN Declining Percentage

**Location:** Line 25

**Current Text:**
> "forty-eight percent of all bird species worldwide are declining"

**Issue:** The 2022 State of the World's Birds report states **49%** declining, not 48%.

**Source:** [BirdLife International 2022](https://www.birdlife.org/news/2022/09/28/state-of-the-worlds-birds-2022-paints-most-concerning-picture-for-nature-yet/)

**Recommendation:** Update to "forty-nine percent"

---

### MINOR-002: Communication Tower Geographic Scope

**Location:** Line 77

**Current Text:**
> "Across the United States, communication towers account for approximately 6.8 million bird deaths annually."

**Issue:** The Longcore et al. 2012 figure of 6.8 million covers the **United States and Canada**, not the United States alone.

**Source:** [Longcore et al. 2012, PLOS ONE](https://pmc.ncbi.nlm.nih.gov/articles/PMC3338802/)

**Recommendation:** Revise to: "Across the United States and Canada, communication towers account for approximately 6.8 million bird deaths annually."

---

## Internal Consistency Check

| Check | Result |
|-------|--------|
| Mathematical calculations | ✓ Consistent |
| Timeline references | ✓ Accurate |
| Source attributions | ⚠ Some figures don't match cited studies |
| Internal cross-references | ✓ Consistent |

---

## Summary of Findings

| Severity | Count | Action Required |
|----------|-------|-----------------|
| CRITICAL | 0 | — |
| ERROR | 5 | Correct figures to match source studies |
| CAUTION | 3 | Verify sources or add qualifiers |
| MINOR | 2 | Optional refinement |

---

## Assessment

This article is **well-researched** with strong foundational claims from landmark studies (Rosenberg et al. 2019, Loss et al. 2013/2014). The 2.9 billion bird decline and window collision mortality are accurately reported. However, several specific mortality figures contain numerical errors when transcribed from their source studies. The errors are not egregious but should be corrected for scientific accuracy.

**Recommendation:** Corrections required before publication. Most issues involve updating numbers to match their source studies exactly.

---

## Quick Reference: Corrections Needed

| Line | Current | Correct |
|------|---------|---------|
| 107 | 1.4–4.4 billion (cats) | 1.3–4.0 billion |
| 113 | 200–340 million (vehicles) | 89–340 million |
| 113 | 8–57 million (electrocution) | 12–64 million (total) OR 0.9–11.6 million (electrocution only) |
| 91 | 80% SE Asian rainforests | ~50% or "more than half" |
| 127 | 12 of 13 Guam birds | 10 of 12 (+ 2 functionally extinct) |
| 25 | 48% declining | 49% declining |
| 77 | United States (towers) | United States and Canada |

---

## Source References

### Primary Studies Verified

1. **Rosenberg et al. (2019)** - "Decline of the North American avifauna." *Science* 366: 120-124. [DOI](https://www.science.org/doi/10.1126/science.aaw1313)

1. **Loss et al. (2013)** - "The impact of free-ranging domestic cats on wildlife of the United States." *Nature Communications* 4: 1396. [DOI](https://www.nature.com/articles/ncomms2380)

1. **Loss et al. (2014a)** - "Bird–building collisions in the United States." *The Condor* 116(1): 8-23. [DOI](https://academic.oup.com/condor/article/116/1/8/5153098)

1. **Loss et al. (2014b)** - "Estimation of bird-vehicle collision mortality on U.S. roads." *Journal of Wildlife Management* 78(5): 763-771.

1. **Loss et al. (2014c)** - "Refining estimates of bird collision and electrocution mortality at power lines." *PLOS ONE* 9(7): e101565. [DOI](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0101565)

1. **Longcore et al. (2012)** - "An estimate of avian mortality at communication towers." *PLOS ONE* 7(4): e34025. [DOI](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0034025)

1. **BirdLife International (2022)** - State of the World's Birds 2022. [Link](https://www.birdlife.org/wp-content/uploads/2022/09/SOWB2022_EN_compressed.pdf)

1. **Haney et al. (2014)** - "Bird mortality from the Deepwater Horizon oil spill." *Marine Ecology Progress Series* 513: 239-252.

---

## Corrections Applied

| Issue ID | Status | Date |
|----------|--------|------|
| ERROR-001 | CORRECTED | 2026-01-06 |
| ERROR-002 | CORRECTED | 2026-01-06 |
| ERROR-003 | CORRECTED | 2026-01-06 |
| ERROR-004 | CORRECTED | 2026-01-06 |
| ERROR-005 | CORRECTED | 2026-01-06 |
| CAUTION-001 | CORRECTED | 2026-01-06 |
| CAUTION-002 | CORRECTED | 2026-01-06 |
| CAUTION-003 | CORRECTED | 2026-01-06 |
| MINOR-001 | CORRECTED | 2026-01-06 |
| MINOR-002 | CORRECTED | 2026-01-06 |

---

## Audit Sign-Off

**Audit Completed:** 2026-01-06
**Corrections Applied:** 2026-01-06
**Overall Quality:** Strong - well-researched with transcription errors in mortality figures
**Next Review Recommended:** Publication ready
**Auditor:** Claude Opus 4.5 (AI-Assisted)
**Reviewed By:** Dennis 'dnoice' Smaltz

---

> **︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!**
