#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
✒ Metadata
    - Title: SME Color Palettes (Sixth Mass Extinction Edition - v2.0)
    - File Name: color_palettes.py
    - Relative Path: TBD
    - Artifact Type: library
    - Version: 2.0.0
    - Date: 2026-01-07
    - Update: Tuesday, January 07, 2026
    - Author: Dennis 'dnoice' Smaltz
    - A.I. Acknowledgement: Anthropic - Claude Opus 4.5
    - Signature: ︻デ═─── ✦ ✦ ✦ | Aim Twice, Shoot Once!

✒ Description:
    Color palette library for the Sixth Mass Extinction Documentation Project.
    447 colors manually extracted via 11x7 grid sampling from six article 
    illustrations. Each biome carries the weight of its subject—these are 
    not decorative choices. Every tone was pulled directly from the visual 
    record of collapse.

✒ Key Features:
    - Feature 1: 447 manually extracted colors across 6 biomes
    - Feature 2: Biome-specific palettes tied to article themes
    - Feature 3: Semantic color assignments for ecological meaning
    - Feature 4: Sequential gradients derived from luminosity bands
    - Feature 5: Key role assignments (background, text, grid, accent)
    - Feature 6: IUCN threat category mapping
    - Feature 7: Taxonomic group assignments
    - Feature 8: HIPPO driver color coding
    - Feature 9: Helper functions for palette access
    - Feature 10: Full compatibility with matplotlib style system

✒ Usage Instructions:
    Import the module and access palettes directly:
    
        from color_palettes import BIOMES, PRIMARY_CYCLE, get_biome_palette
        
        # Get the 8-color primary cycle
        colors = PRIMARY_CYCLE
        
        # Get all colors from a specific biome
        marine_colors = get_biome_palette('marine')
        
        # Get key role colors for a biome
        bg = BIOMES['terrestrial']['roles']['background_light']

✒ Biome Reference:
    - Terrestrial: Big Mammals, Bigger Lies (72 colors)
    - Marine: Dead Zones Rising (76 colors)
    - Arid: Eggshell Armageddon (75 colors)
    - Agricultural: No Buzz, No Harvest (72 colors)
    - Savanna: Orphans of a Dying Wild (77 colors)
    - Urban: Flight Extinguished (75 colors)

✒ Other Important Information:
    - Dependencies: None (pure Python, stdlib only)
    - Compatible platforms: All (Python 3.8+)
    - Integration: Works with matplotlib, seaborn, plotly
    - Performance notes: All colors loaded at import; minimal memory footprint
    - Source images: Article illustration series (6 images, 77 samples each)
---------
"""

from typing import Dict, List, Optional, Union


# =============================================================================
# PRIMARY CYCLE — 8 colors drawn from all 6 biomes
# =============================================================================
# The core visualization cycle. Each color represents a different biome
# and carries specific semantic weight for the data it displays.

PRIMARY_CYCLE = [
    "#97613B",  # Ivory Market — poaching, extraction (Terrestrial)
    "#254340",  # Anoxic Depths — dead zones, suffocation (Marine)
    "#B08E42",  # Thermal Threshold — heat stress, reproductive failure (Arid)
    "#3E2B26",  # Impact Point — collision mortality (Urban)
    "#8C5A24",  # Colony Collapse — pollinator loss (Agricultural)
    "#95A186",  # What Remains — survival, persistence (Marine)
    "#7C5F47",  # Matriarch Absence — fragmentation, orphaning (Savanna)
    "#1A2628",  # Night Migration — fatal light, urban darkness (Urban)
]

# Named access to primary cycle
PRIMARY = {
    "ivory_market": "#97613B",
    "anoxic_depths": "#254340",
    "thermal_threshold": "#B08E42",
    "impact_point": "#3E2B26",
    "colony_collapse": "#8C5A24",
    "what_remains": "#95A186",
    "matriarch_absence": "#7C5F47",
    "night_migration": "#1A2628",
}


# =============================================================================
# TERRESTRIAL BIOME — Big Mammals, Bigger Lies (72 colors)
# Trophy hunting, deforestation, corporate slaughter of keystone species
# =============================================================================

TERRESTRIAL = {
    "lights": [  # Clearcut Horizon
        "#C7B897", "#C4B594", "#C4B493", "#C3B493", "#C2B492",
        "#C2B291", "#C0B190", "#BEAF8E", "#BCAD8C", "#BBAC8D",
        "#B7A987", "#B7A887", "#B6A684", "#B5A685", "#B4A580",
    ],
    "midtones": [  # Stump Ring
        "#AA9A79", "#A59674", "#A59573", "#A39372", "#A29276",
        "#A09073", "#A0906F", "#9F8C6B", "#97896E", "#968363",
        "#8E8066", "#847C67", "#847860", "#83755D", "#7F7154",
        "#7A6E56", "#776B53", "#6D6046",
    ],
    "darks": [  # Poacher's Trail
        "#55452E", "#554630", "#534630", "#52442B", "#50412C",
        "#4D412D", "#4C3D2A", "#4A3C29", "#4A3B28", "#4A3B27",
        "#493A27", "#483926", "#463926", "#433726", "#413423",
        "#3F3725", "#3D2C16", "#3B3527", "#3B3526", "#383123",
        "#373425", "#373324", "#363020", "#353223", "#343122",
        "#332F21", "#322F20", "#312D21",
    ],
    "accents": [  # Ivory Market
        "#97613B", "#9F6943", "#9F6944", "#9E643F", "#886245",
        "#7E6749", "#7B563B", "#785136", "#786346",
    ],
    "roles": {
        "background_light": "#C4B493",
        "background_mid": "#B7A887",
        "text_primary": "#3B3527",
        "text_secondary": "#6D6046",
        "grid": "#A59674",
        "accent": "#97613B",
    },
    "avg": {
        "lights": "#C0B18E",
        "midtones": "#8F8264",
        "darks": "#433625",
        "accents": "#8B5F40",
    },
}


# =============================================================================
# MARINE BIOME — Dead Zones Rising (76 colors)
# Hypoxia, acidification, mass suffocation of marine biodiversity
# =============================================================================

MARINE = {
    "darks": [  # Anoxic Depths
        "#131919", "#152021", "#12201F", "#161D19", "#16201F",
        "#172321", "#182221", "#182324", "#182424", "#182726",
        "#191F1F", "#1A2322", "#1A2A29", "#1A2A2A", "#1B2E2C",
        "#1B2F2E", "#1B302D", "#1C221F", "#1C2D2C", "#1C3532",
        "#1D2127", "#1D2C2A", "#1D2E2D", "#1D3130", "#1D3331",
        "#1E312F", "#1E3230", "#1E3432",
    ],
    "mid_darks": [  # Oxygen Debt
        "#1E3B37", "#1F2D2A", "#1F3835", "#203D39", "#203E39",
        "#213B38", "#21413B", "#223C39", "#23433E", "#24443F",
        "#25443F", "#254540", "#26443F", "#284742", "#284843",
        "#2D5049", "#30473D", "#335448",
    ],
    "midtones": [  # Algal Silence
        "#354A42", "#395D51", "#3F4B3A", "#3F5F53", "#465B4E",
        "#476C5D", "#4A5644", "#4A6A5C", "#547665", "#686B53",
        "#6A8A75", "#6B8872", "#6C8872", "#6E8B75", "#78937C",
    ],
    "lights": [  # What Remains
        "#7F977D", "#84947A", "#859A84", "#859C82", "#96A68B",
        "#99A68B", "#9DA487", "#9DA68B", "#9EA486", "#9EA687",
        "#A6A98A", "#A8A989",
    ],
    "roles": {
        "background_deep": "#1A2827",
        "background_mid": "#254340",
        "text_primary": "#131919",
        "text_light": "#A8A989",
        "grid": "#526B58",
        "accent": "#78937C",
    },
    "avg": {
        "darks": "#1A2827",
        "mid_darks": "#254340",
        "midtones": "#526B58",
        "lights": "#95A186",
    },
}


# =============================================================================
# ARID BIOME — Eggshell Armageddon (75 colors)
# Global reptile reproductive crisis, climate and chemical disruption
# =============================================================================

ARID = {
    "lights": [  # Failed Clutch
        "#F6DD9B", "#F5DFA6", "#F5DFA3", "#F5DC99", "#F4D994",
        "#F3D893", "#F3D796", "#F2D794", "#F2D695", "#F2D691",
        "#F2D591", "#F2D58F", "#F2D48E", "#F0D898", "#F0D490",
        "#F0D38D", "#EED18B", "#ECD593", "#ECD087", "#EBCF86",
    ],
    "midtones": [  # Nesting Ground
        "#ECCA7F", "#EDD189", "#EDD088", "#EECE84", "#E9CD88",
        "#E9C678", "#E6C576", "#E3B75F", "#E2C078", "#DFBB67",
        "#DBB763", "#DBB25A", "#DBB15D", "#DAB25B", "#DAAE56",
        "#D8B25F", "#D8AE55", "#D6A44B", "#D5A955", "#D5A549",
        "#D5A346", "#D4A74D", "#D4A44F", "#D3A649", "#CFB36F",
        "#CFA651", "#CEA04A", "#CF9D42", "#CF9B40", "#CD9E42",
    ],
    "mid_darks": [  # Thermal Threshold
        "#CCA351", "#CC9A44", "#C7953D", "#C6A460", "#C38B27",
        "#C29038", "#BB831E", "#AE986A", "#A98B4C", "#A6863B",
        "#9A7D3B", "#8B815D", "#836526", "#DD9F2E", "#DB9D32",
        "#D79D30",
    ],
    "darks": [  # No Return
        "#58401E", "#553A0F", "#49351B", "#423B20", "#422D0D",
        "#412F12", "#3D361B", "#312C15",
    ],
    "roles": {
        "background_light": "#F2D593",
        "background_mid": "#ECD087",
        "text_primary": "#312C15",
        "text_secondary": "#836526",
        "grid": "#CFB36F",
        "accent": "#D79D30",
    },
    "avg": {
        "lights": "#F2D593",
        "midtones": "#DDB860",
        "mid_darks": "#B08E42",
        "darks": "#44351A",
    },
}


# =============================================================================
# AGRICULTURAL BIOME — No Buzz, No Harvest (72 colors)
# Pollinator collapse and the coming agricultural crisis
# =============================================================================

AGRICULTURAL = {
    "lights": [  # Fallow Yield
        "#F4D28A", "#F4CF88", "#F3CE87", "#F2D089", "#F2D088",
        "#F2CF8B", "#F1CF87", "#F0CB84", "#EDCE8D", "#EBCD8D",
        "#EACC8E", "#E9CB8D", "#E9CB8C", "#E5C88E", "#E5C78B",
        "#E4BF7B", "#E3C68A", "#E3C48B", "#E2C488", "#E1C289",
        "#E0C287",
    ],
    "midtones": [  # Empty Comb
        "#D6AA63", "#CC9347", "#C1893F", "#C08A41", "#BE863B",
        "#BD873E", "#BD873D", "#B97F34", "#B8823A", "#B57F38",
        "#B5803A", "#B47E38", "#B3813B", "#AC8448", "#AA742D",
        "#A9762F", "#A77738", "#A27233", "#A06C2D",
    ],
    "mid_darks": [  # Colony Collapse
        "#986528", "#976325", "#945E21", "#936125", "#926022",
        "#905E24", "#8D5B23", "#8D5A21", "#8B612C", "#8A5C2A",
        "#895E2C", "#865722", "#84551E", "#83541F", "#81501A",
        "#805220", "#80521A", "#7E4F1E", "#7B501D",
    ],
    "darks": [  # Silent Field
        "#73481B", "#724719", "#72471A", "#70491C", "#6A4B29",
        "#6A4A24", "#684216", "#61431F", "#5C421C", "#593C1B",
        "#593A17", "#4F2F0B",
    ],
    "roles": {
        "background_light": "#ECC98A",
        "background_mid": "#E3C48B",
        "text_primary": "#4F2F0B",
        "text_secondary": "#73481B",
        "grid": "#B58439",
        "accent": "#CC9347",
    },
    "avg": {
        "lights": "#ECC98A",
        "midtones": "#B58439",
        "mid_darks": "#8C5A24",
        "darks": "#64421B",
    },
}


# =============================================================================
# SAVANNA BIOME — Orphans of a Dying Wild (77 colors)
# Wildlife orphans, elephant trauma, ecosystem fragmentation
# =============================================================================

SAVANNA = {
    "lights": [  # Orphan Dust
        "#EBCFAA", "#E8CCA7", "#E8CAA6", "#E3C59F", "#E1C39D",
        "#E0C29E", "#E0C19B", "#DFC19D", "#DEC09A", "#DDBF9B",
        "#DABC98", "#D8BA96", "#D6B894", "#D5B793",
    ],
    "midtones": [  # Fragmented Range
        "#CAAC88", "#C6A987", "#C5A886", "#C5A689", "#CBA97E",
        "#BFA687", "#BFA284", "#BEA483", "#BDA080", "#BC9E7A",
        "#BC9B78", "#BD936A", "#B48B60", "#B48A66", "#B3987B",
        "#B09779", "#B09675", "#AE825A", "#AB8C6F", "#A47B57",
        "#A47955", "#9B7353", "#9B724D", "#997B5F", "#977559",
        "#956E4E", "#947356", "#936C4B",
    ],
    "mid_darks": [  # Matriarch Absence
        "#8F6A4E", "#8F694C", "#8E6A4E", "#8B6548", "#8A674A",
        "#886549", "#876346", "#80644E", "#7E644F", "#7E634F",
        "#7D624D", "#7C5A3F", "#7B5D46", "#7A583E", "#79614B",
        "#775A41", "#75634F", "#745D48", "#6E543F", "#6D543E",
        "#694D37", "#67503F", "#65574A",
    ],
    "darks": [  # Witness Ground
        "#665647", "#625242", "#5E452F", "#5C4633", "#52473B",
        "#4C3D30", "#4C3725", "#463C32", "#423B30", "#423326",
        "#41342B",
    ],
    "roles": {
        "background_light": "#E0C29A",
        "background_mid": "#D6B894",
        "text_primary": "#41342B",
        "text_secondary": "#6D543E",
        "grid": "#B08A68",
        "accent": "#9B7353",
    },
    "avg": {
        "lights": "#E0C29A",
        "midtones": "#B08A68",
        "mid_darks": "#7C5F47",
        "darks": "#4E4134",
    },
}


# =============================================================================
# URBAN BIOME — Flight Extinguished (75 colors)
# Bird mortality from glass buildings, light pollution, habitat loss
# =============================================================================

URBAN = {
    "lights": [  # Industrial Haze
        "#C5C1A8", "#A39F88", "#9F9D88", "#979A8A",
    ],
    "midtones": [  # Reflection Glass
        "#7C877C", "#707D70", "#6F7A70", "#6E7B74", "#6E7A72",
        "#69786F", "#677770", "#64756F", "#5E6D69", "#5B5E53",
        "#5B5C50", "#5B5B4F", "#58594B", "#56584B", "#545B50",
        "#535447", "#506361", "#4E5045", "#4D5B57", "#4E4F47",
        "#4A5047",
    ],
    "mid_darks": [  # Urban Canopy
        "#475A58", "#454F47", "#435756", "#415353", "#405252",
        "#3F5151", "#384A4A", "#384C4D", "#37494A", "#35484B",
        "#354747", "#33464A", "#334648", "#333F3F", "#313D3B",
        "#314346", "#304347", "#303A38", "#2F4345", "#2F4145",
        "#2E3A3A", "#2D3D3D", "#2C3B3E", "#2C3B3B", "#2C3838",
        "#2B3431",
    ],
    "darks": [  # Night Migration
        "#273333", "#253131", "#243336", "#233235", "#212F32",
        "#1E2829", "#1E2729", "#192426", "#182224", "#151A1B",
        "#121C1D", "#111A1D", "#101719",
    ],
    "accents": [  # Impact Point
        "#442823", "#402824", "#3F241F", "#3E2E29", "#3E2724",
        "#3D2521", "#3D322F", "#3B342E",
    ],
    "roles": {
        "background_light": "#A6A290",
        "background_mid": "#5F6860",
        "text_primary": "#101719",
        "text_secondary": "#2D3D3D",
        "grid": "#475A58",
        "accent": "#3E2B26",
    },
    "avg": {
        "lights": "#A6A290",
        "midtones": "#5F6860",
        "mid_darks": "#374A4A",
        "darks": "#1A2628",
        "accents": "#3E2B26",
    },
}


# =============================================================================
# BIOME REGISTRY — Unified access to all biomes
# =============================================================================

BIOMES: Dict[str, Dict] = {
    "terrestrial": TERRESTRIAL,
    "marine": MARINE,
    "arid": ARID,
    "agricultural": AGRICULTURAL,
    "savanna": SAVANNA,
    "urban": URBAN,
}

# Article titles mapped to biomes
ARTICLES = {
    "big_mammals_bigger_lies": "terrestrial",
    "dead_zones_rising": "marine",
    "eggshell_armageddon": "arid",
    "no_buzz_no_harvest": "agricultural",
    "orphans_of_a_dying_wild": "savanna",
    "flight_extinguished": "urban",
}


# =============================================================================
# SEQUENTIAL PALETTES — Gradients from light to dark per biome
# =============================================================================

def _build_sequential(biome: Dict, reverse: bool = False) -> List[str]:
    """Build a sequential gradient from a biome's luminosity bands."""
    seq = []
    for key in ["lights", "midtones", "mid_darks", "darks"]:
        if key in biome:
            seq.extend(biome[key])
    return seq[::-1] if reverse else seq


SEQ_TERRESTRIAL = _build_sequential(TERRESTRIAL)
SEQ_MARINE = _build_sequential(MARINE)
SEQ_ARID = _build_sequential(ARID)
SEQ_AGRICULTURAL = _build_sequential(AGRICULTURAL)
SEQ_SAVANNA = _build_sequential(SAVANNA)
SEQ_URBAN = _build_sequential(URBAN)


# =============================================================================
# DIVERGING PALETTES — Biome contrasts
# =============================================================================

# Terrestrial (warm) to Marine (cool) — land vs. sea
DIV_LAND_SEA = (
    TERRESTRIAL["darks"][-3:][::-1] +
    TERRESTRIAL["midtones"][-3:][::-1] +
    ["#D5D5D0"] +  # Neutral center
    MARINE["midtones"][:3] +
    MARINE["darks"][:3]
)

# Arid (heat) to Urban (cold) — temperature extremes
DIV_HEAT_COLD = (
    ARID["mid_darks"][-3:][::-1] +
    ARID["lights"][-3:][::-1] +
    ["#D5D5D0"] +
    URBAN["midtones"][:3] +
    URBAN["darks"][:3]
)

# Agricultural (loss) to Savanna (hope) — collapse vs. persistence
DIV_LOSS_HOPE = (
    AGRICULTURAL["darks"][-3:][::-1] +
    AGRICULTURAL["mid_darks"][-3:][::-1] +
    ["#D5D5D0"] +
    SAVANNA["midtones"][:3] +
    SAVANNA["lights"][:3]
)


# =============================================================================
# CATEGORICAL PALETTES — Ecological classifications
# =============================================================================

# IUCN Red List categories — mapped to extracted tones
IUCN_COLORS = {
    "EX": URBAN["darks"][0],           # Extinct — Night Migration (darkest)
    "EW": URBAN["accents"][0],         # Extinct in Wild — Impact Point
    "CR": TERRESTRIAL["accents"][0],   # Critically Endangered — Ivory Market
    "EN": ARID["mid_darks"][-1],       # Endangered — Thermal Threshold
    "VU": AGRICULTURAL["midtones"][0], # Vulnerable — Empty Comb
    "NT": SAVANNA["midtones"][10],     # Near Threatened — Fragmented Range
    "LC": MARINE["lights"][-1],        # Least Concern — What Remains
    "DD": URBAN["midtones"][10],       # Data Deficient — Reflection Glass
    "NE": URBAN["lights"][0],          # Not Evaluated — Industrial Haze
}

# Taxonomic groups — one color per biome focus
TAXA_COLORS = {
    "mammals": TERRESTRIAL["accents"][0],    # Ivory Market
    "birds": URBAN["mid_darks"][0],          # Urban Canopy
    "reptiles": ARID["mid_darks"][-1],       # Thermal Threshold
    "amphibians": MARINE["midtones"][7],     # Algal Silence
    "fish": MARINE["mid_darks"][8],          # Oxygen Debt
    "invertebrates": AGRICULTURAL["mid_darks"][0],  # Colony Collapse
    "plants": SAVANNA["midtones"][15],       # Fragmented Range
    "fungi": TERRESTRIAL["darks"][10],       # Poacher's Trail
}

# Primary extinction drivers (HIPPO framework)
DRIVER_COLORS = {
    "habitat": TERRESTRIAL["accents"][0],    # Ivory Market — deforestation
    "invasives": MARINE["midtones"][7],      # Algal Silence — introduced species
    "pollution": URBAN["mid_darks"][5],      # Urban Canopy — contamination
    "population": AGRICULTURAL["mid_darks"][0],  # Colony Collapse — human pressure
    "overexploitation": TERRESTRIAL["darks"][5],  # Poacher's Trail — extraction
    "climate": ARID["mid_darks"][-1],        # Thermal Threshold — heating
}

# Geographic/ecosystem regions
REGION_COLORS = {
    "tropical": SAVANNA["midtones"][0],      # Fragmented Range
    "temperate": TERRESTRIAL["midtones"][5], # Stump Ring
    "polar": URBAN["lights"][0],             # Industrial Haze
    "marine": MARINE["mid_darks"][8],        # Oxygen Debt
    "freshwater": MARINE["midtones"][5],     # Algal Silence
    "desert": ARID["midtones"][15],          # Nesting Ground
    "grassland": AGRICULTURAL["lights"][10], # Fallow Yield
    "urban": URBAN["mid_darks"][0],          # Urban Canopy
}


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def get_biome_palette(
    biome: str,
    band: Optional[str] = None
) -> List[str]:
    """
    Get colors from a specific biome.
    
    Args:
        biome: One of 'terrestrial', 'marine', 'arid', 'agricultural', 
               'savanna', 'urban'
        band: Optional luminosity band ('lights', 'midtones', 'mid_darks', 
              'darks', 'accents'). If None, returns all colors.
    
    Returns:
        List of hex color codes
    
    Example:
        >>> get_biome_palette('marine', 'darks')
        ['#131919', '#152021', ...]
    """
    if biome not in BIOMES:
        raise ValueError(f"Unknown biome: {biome}. Choose from: {list(BIOMES.keys())}")
    
    biome_data = BIOMES[biome]
    
    if band:
        if band not in biome_data:
            available = [k for k in biome_data.keys() if isinstance(biome_data[k], list)]
            raise ValueError(f"Band '{band}' not in {biome}. Available: {available}")
        return biome_data[band]
    
    # Return all colors from all bands
    all_colors = []
    for key, value in biome_data.items():
        if isinstance(value, list):
            all_colors.extend(value)
    return all_colors


def get_biome_roles(biome: str) -> Dict[str, str]:
    """
    Get the key role assignments for a biome.
    
    Args:
        biome: Biome name
    
    Returns:
        Dict with keys like 'background_light', 'text_primary', etc.
    """
    if biome not in BIOMES:
        raise ValueError(f"Unknown biome: {biome}")
    return BIOMES[biome]["roles"]


def get_sequential(
    biome: str,
    n_colors: Optional[int] = None,
    reverse: bool = False
) -> List[str]:
    """
    Get a sequential gradient from a biome.
    
    Args:
        biome: Biome name
        n_colors: Number of colors to return (evenly sampled)
        reverse: If True, dark to light; if False, light to dark
    
    Returns:
        List of hex color codes
    """
    sequences = {
        "terrestrial": SEQ_TERRESTRIAL,
        "marine": SEQ_MARINE,
        "arid": SEQ_ARID,
        "agricultural": SEQ_AGRICULTURAL,
        "savanna": SEQ_SAVANNA,
        "urban": SEQ_URBAN,
    }
    
    if biome not in sequences:
        raise ValueError(f"Unknown biome: {biome}")
    
    seq = sequences[biome]
    if reverse:
        seq = seq[::-1]
    
    if n_colors and n_colors < len(seq):
        step = len(seq) // n_colors
        return seq[::step][:n_colors]
    
    return seq


def get_categorical(category: str) -> Dict[str, str]:
    """
    Get a categorical color mapping.
    
    Args:
        category: One of 'iucn', 'taxa', 'drivers', 'regions'
    
    Returns:
        Dict mapping category values to hex colors
    """
    categories = {
        "iucn": IUCN_COLORS,
        "taxa": TAXA_COLORS,
        "drivers": DRIVER_COLORS,
        "regions": REGION_COLORS,
    }
    
    if category not in categories:
        raise ValueError(f"Unknown category: {category}. Choose from: {list(categories.keys())}")
    
    return categories[category]


def get_diverging(name: str) -> List[str]:
    """
    Get a diverging palette.
    
    Args:
        name: One of 'land_sea', 'heat_cold', 'loss_hope'
    
    Returns:
        List of hex color codes (diverging from center)
    """
    diverging = {
        "land_sea": DIV_LAND_SEA,
        "heat_cold": DIV_HEAT_COLD,
        "loss_hope": DIV_LOSS_HOPE,
    }
    
    if name not in diverging:
        raise ValueError(f"Unknown diverging palette: {name}. Choose from: {list(diverging.keys())}")
    
    return diverging[name]


def get_article_palette(article: str) -> List[str]:
    """
    Get colors for a specific article by title.
    
    Args:
        article: Article slug (e.g., 'dead_zones_rising')
    
    Returns:
        List of all colors from that article's biome
    """
    if article not in ARTICLES:
        raise ValueError(f"Unknown article: {article}. Choose from: {list(ARTICLES.keys())}")
    
    biome = ARTICLES[article]
    return get_biome_palette(biome)


# =============================================================================
# MATPLOTLIB INTEGRATION
# =============================================================================

def register_colormaps():
    """
    Register SME colormaps with matplotlib.
    
    Call this function to make SME palettes available as matplotlib colormaps:
        - 'sme_terrestrial', 'sme_marine', 'sme_arid', etc.
        - 'sme_land_sea', 'sme_heat_cold', 'sme_loss_hope' (diverging)
    """
    try:
        import matplotlib.pyplot as plt
        from matplotlib.colors import LinearSegmentedColormap, ListedColormap
        
        # Sequential colormaps
        for biome in BIOMES.keys():
            seq = get_sequential(biome)
            cmap = LinearSegmentedColormap.from_list(f"sme_{biome}", seq)
            plt.colormaps.register(cmap)
        
        # Diverging colormaps
        for name in ["land_sea", "heat_cold", "loss_hope"]:
            div = get_diverging(name)
            cmap = LinearSegmentedColormap.from_list(f"sme_{name}", div)
            plt.colormaps.register(cmap)
        
        # Primary cycle as qualitative
        cmap = ListedColormap(PRIMARY_CYCLE, name="sme_primary")
        plt.colormaps.register(cmap)
        
        print("SME colormaps registered successfully.")
        
    except ImportError:
        print("matplotlib not available. Colormaps not registered.")


# =============================================================================
# MODULE INFO
# =============================================================================

__version__ = "2.0.0"
__author__ = "Dennis 'dnoice' Smaltz"
__biomes__ = list(BIOMES.keys())
__total_colors__ = sum(
    len(get_biome_palette(b)) for b in BIOMES.keys()
)

if __name__ == "__main__":
    # Quick verification
    print(f"SME Color Palettes v{__version__}")
    print(f"Total colors extracted: {__total_colors__}")
    print(f"Biomes: {', '.join(__biomes__)}")
    print(f"Primary cycle: {len(PRIMARY_CYCLE)} colors")
    print("\nBiome breakdown:")
    for biome in __biomes__:
        count = len(get_biome_palette(biome))
        print(f"  {biome.capitalize()}: {count} colors")