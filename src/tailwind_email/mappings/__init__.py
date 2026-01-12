"""
Tailwind CSS class to inline CSS mappings.
"""

from tailwind_email.mappings.borders import (
    BORDER_RADIUS_CLASSES,
    BORDER_STYLE_CLASSES,
    BORDER_WIDTH_CLASSES,
)
from tailwind_email.mappings.colors import COLOR_PALETTE
from tailwind_email.mappings.effects import (
    BOX_SHADOW_CLASSES,
    OPACITY_CLASSES,
)
from tailwind_email.mappings.sizing import (
    HEIGHT_CLASSES,
    MAX_WIDTH_CLASSES,
    MIN_WIDTH_CLASSES,
    WIDTH_CLASSES,
)
from tailwind_email.mappings.spacing import SPACING_SCALE, get_spacing_value
from tailwind_email.mappings.typography import (
    FONT_SIZE_CLASSES,
    FONT_WEIGHT_CLASSES,
    LETTER_SPACING_CLASSES,
    LINE_HEIGHT_CLASSES,
    TEXT_ALIGN_CLASSES,
    TEXT_DECORATION_CLASSES,
    TEXT_TRANSFORM_CLASSES,
)

__all__ = [
    "COLOR_PALETTE",
    "SPACING_SCALE",
    "get_spacing_value",
    "WIDTH_CLASSES",
    "HEIGHT_CLASSES",
    "MAX_WIDTH_CLASSES",
    "MIN_WIDTH_CLASSES",
    "FONT_SIZE_CLASSES",
    "FONT_WEIGHT_CLASSES",
    "LINE_HEIGHT_CLASSES",
    "LETTER_SPACING_CLASSES",
    "TEXT_ALIGN_CLASSES",
    "TEXT_DECORATION_CLASSES",
    "TEXT_TRANSFORM_CLASSES",
    "BORDER_WIDTH_CLASSES",
    "BORDER_RADIUS_CLASSES",
    "BORDER_STYLE_CLASSES",
    "BOX_SHADOW_CLASSES",
    "OPACITY_CLASSES",
]
