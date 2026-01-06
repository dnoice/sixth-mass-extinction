"""
✒ Metadata
    - Title: SME Color Palettes (SME Edition - v1.0)
    - File Name: color_palettes.py
    - Relative Path: research-stacks/_shared/styles/color_palettes.py
    - Artifact Type: library
    - Version: 1.0.0
    - Date: 2026-01-04
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Anthropic - Claude Opus 4.5
    - Signature: ︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!

✒ Description:
    Standard color palettes for visualizations in the Sixth Mass Extinction
    project. Ensures visual consistency across all 32 episodes.
"""

# =============================================================================
# PRIMARY PALETTE - Main visualization colors
# =============================================================================

# Crisis/Danger - For extinction data, threats, decline
CRISIS_RED = "#d32f2f"
CRISIS_DARK = "#b71c1c"
CRISIS_LIGHT = "#ef5350"

# Warning - For thresholds, risks, projections
WARNING_ORANGE = "#f57c00"
WARNING_DARK = "#e65100"
WARNING_LIGHT = "#ffb74d"

# Data/Neutral - For baseline data, measurements
DATA_BLUE = "#1976d2"
DATA_DARK = "#0d47a1"
DATA_LIGHT = "#64b5f6"

# Hope/Conservation - For protected areas, recovery
HOPE_GREEN = "#388e3c"
HOPE_DARK = "#1b5e20"
HOPE_LIGHT = "#81c784"

# Systemic - For economic/political analysis
SYSTEMIC_PURPLE = "#7b1fa2"
SYSTEMIC_DARK = "#4a148c"
SYSTEMIC_LIGHT = "#ba68c8"

# =============================================================================
# SECONDARY PALETTE - Supporting colors
# =============================================================================

SECONDARY = {
    "pink": "#c2185b",
    "teal": "#0097a7",
    "lime": "#689f38",
    "amber": "#ffa000",
    "indigo": "#303f9f",
    "brown": "#5d4037",
}

# =============================================================================
# SEQUENTIAL PALETTES - For continuous data
# =============================================================================

# Red sequential (extinction rates, species loss)
SEQ_RED = ["#ffcdd2", "#ef9a9a", "#e57373", "#ef5350", "#f44336", "#e53935", "#d32f2f", "#c62828", "#b71c1c"]

# Blue sequential (data density, counts)
SEQ_BLUE = ["#bbdefb", "#90caf9", "#64b5f6", "#42a5f5", "#2196f3", "#1e88e5", "#1976d2", "#1565c0", "#0d47a1"]

# Green sequential (conservation, recovery)
SEQ_GREEN = ["#c8e6c9", "#a5d6a7", "#81c784", "#66bb6a", "#4caf50", "#43a047", "#388e3c", "#2e7d32", "#1b5e20"]

# =============================================================================
# DIVERGING PALETTES - For data with meaningful center
# =============================================================================

# Red-Blue diverging (decline vs. growth)
DIV_RED_BLUE = ["#b71c1c", "#d32f2f", "#ef5350", "#ffcdd2", "#f5f5f5", "#bbdefb", "#64b5f6", "#1976d2", "#0d47a1"]

# Red-Green diverging (threat vs. conservation)
DIV_RED_GREEN = ["#b71c1c", "#d32f2f", "#ef5350", "#ffcdd2", "#f5f5f5", "#c8e6c9", "#81c784", "#388e3c", "#1b5e20"]

# =============================================================================
# CATEGORICAL PALETTES - For distinct categories
# =============================================================================

# IUCN threat categories
IUCN_COLORS = {
    "EX": "#000000",      # Extinct - Black
    "EW": "#3d0c02",      # Extinct in Wild - Dark brown
    "CR": "#d32f2f",      # Critically Endangered - Red
    "EN": "#f57c00",      # Endangered - Orange
    "VU": "#ffc107",      # Vulnerable - Yellow
    "NT": "#8bc34a",      # Near Threatened - Light green
    "LC": "#4caf50",      # Least Concern - Green
    "DD": "#9e9e9e",      # Data Deficient - Gray
    "NE": "#e0e0e0",      # Not Evaluated - Light gray
}

# Taxonomic groups
TAXA_COLORS = {
    "mammals": "#d32f2f",
    "birds": "#1976d2",
    "reptiles": "#388e3c",
    "amphibians": "#f57c00",
    "fish": "#0097a7",
    "invertebrates": "#7b1fa2",
    "plants": "#689f38",
    "fungi": "#5d4037",
}

# Primary drivers (HIPPO)
DRIVER_COLORS = {
    "habitat": "#d32f2f",
    "invasives": "#7b1fa2",
    "pollution": "#5d4037",
    "population": "#f57c00",
    "overexploitation": "#1976d2",
    "climate": "#0097a7",
}

# Geographic regions
REGION_COLORS = {
    "tropical": "#d32f2f",
    "temperate": "#1976d2",
    "polar": "#64b5f6",
    "marine": "#0097a7",
    "freshwater": "#00bcd4",
}

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def get_palette(name: str, n_colors: int = None):
    """Get a color palette by name.

    Args:
        name: Palette name ('red', 'blue', 'green', 'iucn', 'taxa', etc.)
        n_colors: Number of colors needed (for sequential palettes)

    Returns:
        List of hex color codes
    """
    palettes = {
        "red": SEQ_RED,
        "blue": SEQ_BLUE,
        "green": SEQ_GREEN,
        "div_rb": DIV_RED_BLUE,
        "div_rg": DIV_RED_GREEN,
        "iucn": list(IUCN_COLORS.values()),
        "taxa": list(TAXA_COLORS.values()),
        "drivers": list(DRIVER_COLORS.values()),
        "regions": list(REGION_COLORS.values()),
    }

    palette = palettes.get(name, SEQ_BLUE)

    if n_colors and n_colors < len(palette):
        # Subsample evenly
        step = len(palette) // n_colors
        return palette[::step][:n_colors]

    return palette


def get_crisis_gradient(n_colors: int = 5):
    """Get a red gradient for crisis/danger visualizations."""
    return SEQ_RED[-n_colors:]


def get_hope_gradient(n_colors: int = 5):
    """Get a green gradient for conservation/hope visualizations."""
    return SEQ_GREEN[-n_colors:]
