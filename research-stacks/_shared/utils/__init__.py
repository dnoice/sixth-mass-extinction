"""
✒ Metadata
    - Title: SME Shared Utilities (SME Edition - v1.0)
    - File Name: __init__.py
    - Relative Path: research-stacks/_shared/utils/__init__.py
    - Artifact Type: library
    - Version: 1.0.0
    - Date: 2026-01-04
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Anthropic - Claude Opus 4.5
    - Signature: ︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!

✒ Description:
    Shared utility functions for the Sixth Mass Extinction research stacks.
    Provides common data processing, visualization, and statistical functions.
"""

from pathlib import Path

# Project root paths
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent
RESEARCH_STACKS = PROJECT_ROOT / "research-stacks"
DOCS = PROJECT_ROOT / "docs"
REFERENCES = DOCS / "references"

# Common data paths
SHARED_DATA = Path(__file__).parent.parent / "data"


def get_episode_path(section: str, episode: str) -> Path:
    """Get the path to a specific episode directory.

    Args:
        section: Section number (e.g., "1.0", "2.0")
        episode: Episode number (e.g., "1.1", "2.3")

    Returns:
        Path to the episode directory

    Example:
        >>> path = get_episode_path("2.0", "2.3")
        >>> print(path)
        research-stacks/2.0-primary-drivers/2.3-climate-change
    """
    section_map = {
        "1.0": "establishing-crisis",
        "2.0": "primary-drivers",
        "3.0": "ecological-collapse",
        "4.0": "economic-systems",
        "5.0": "environmental-justice",
        "6.0": "what-were-losing",
        "7.0": "tipping-points",
        "8.0": "failed-solutions",
        "9.0": "timeline-urgency",
        "10.0": "synthesis",
    }

    episode_map = {
        "1.1": "extinction-rates",
        "1.2": "magnitude-of-risk",
        "1.3": "geographic-hotspots",
        "1.4": "previous-extinctions",
        "2.1": "habitat-destruction",
        "2.2": "resource-extraction",
        "2.3": "climate-change",
        "2.4": "pollution",
        "2.5": "overexploitation",
        "2.6": "invasive-species",
        "3.1": "trophic-cascades",
        "3.2": "ecosystem-service-failures",
        "3.3": "biotic-homogenization",
        "4.1": "capitalism-infinite-growth",
        "4.2": "corporate-power",
        "4.3": "governmental-failure",
        "4.4": "consumption-inequality",
        "5.1": "indigenous-peoples",
        "5.2": "frontline-communities",
        "6.1": "functional-diversity",
        "6.2": "coextinction",
        "6.3": "evolutionary-potential",
        "7.1": "planetary-boundaries",
        "7.2": "irreversible-losses",
        "8.1": "technological-optimism",
        "8.2": "conservation-insufficiency",
        "9.1": "extinction-acceleration",
        "9.2": "irreversible-thresholds",
        "10.1": "systemic-causation",
        "10.2": "survival-question",
        "10.3": "what-actually-required",
        "10.4": "tragic-conclusion",
    }

    section_name = section_map.get(section, "unknown")
    episode_name = episode_map.get(episode, "unknown")

    return RESEARCH_STACKS / f"{section}-{section_name}" / f"{episode}-{episode_name}"
