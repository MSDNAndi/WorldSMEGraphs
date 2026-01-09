"""
Shared Constants for Workflow Validation
=========================================

Common constants used across workflow validation tools to ensure
consistent validation criteria.

Author: WorldSMEGraphs Image Generation Specialist
Version: 1.1.0
Created: 2026-01-08
Updated: 2026-01-09 (Added multi-panel and image filename patterns)
"""

# Placeholder keywords that indicate incomplete prompts
PLACEHOLDER_KEYWORDS = [
    "PLACEHOLDER",
    "TODO",
    "TBD",
    "FIXME",
    "XXX",
    "[insert",
    "[add",
    "[describe",
    "[fill in",
    "Apply STYLE BASE",
    "Use style from",
    "See style guide",
]

# External reference patterns (regex)
EXTERNAL_REFERENCE_PATTERNS = [
    r"refer to\s+\w+",
    r"see\s+(the\s+)?style\s+guide",
    r"as described in",
    r"use\s+the\s+style\s+from",
    r"apply\s+(the\s+)?style",
    r"consult\s+the",
]

# Prompt length thresholds (characters)
MIN_LENGTH = 1000  # Absolute minimum
RECOMMENDED_LENGTH = 5000  # Recommended minimum
TARGET_MIN_LENGTH = 8000  # Target minimum
TARGET_MAX_LENGTH = 20000  # Target maximum

# Indicators of super explicit prompts (good)
EXPLICIT_INDICATORS = [
    "LEFT TO RIGHT",
    "clockwise",
    "counterclockwise",
    "from left to right",
    "from top to bottom",
    r"#[0-9A-Fa-f]{6}",  # Hex color codes
    r"\d+\s*px",  # Pixel measurements
    r"\d+\s*%",  # Percentage measurements
    "explicitly",
    "specific",
    "exact",
    r"at\s+x=\d+",  # Position coordinates
    r"centered at",
]

# Multi-panel prompt file patterns (regex)
# Used to detect and parse files with === PANEL XX === delimiters
PANEL_DELIMITER_DETECT = r'(?:^|\n)={3,}.*PANEL\s*\d+'
PANEL_DELIMITER_SPLIT = r'(?:^|\n)={3,}\s*PANEL\s*(\d+).*?(?:={3,})?\s*(?:\n|$)'

# Image filename patterns (regex)
# Standard format: image_XXX_YYYYMMDD_HHMMSS_HASHCODE.png
IMAGE_FILENAME_PATTERN = r'image_(\d+)_(\d{8}_\d{6})_([a-f0-9]+)\.png'
IMAGE_HASH_EXTRACT = r'image_\d+_\d{8}_\d{6}_([a-f0-9]+)'
