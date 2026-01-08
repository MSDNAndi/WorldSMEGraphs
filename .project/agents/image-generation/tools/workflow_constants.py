"""
Shared Constants for Workflow Validation
=========================================

Common constants used across workflow validation tools to ensure
consistent validation criteria.

Author: WorldSMEGraphs Image Generation Specialist
Version: 1.0.0
Created: 2026-01-08
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
