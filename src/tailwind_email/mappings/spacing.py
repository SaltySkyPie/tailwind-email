"""
Tailwind CSS spacing scale mappings.

Tailwind v4 uses a spacing multiplier where 1 unit = 0.25rem = 4px (at 16px base).
"""


# Default spacing scale in pixels (1 unit = 4px)
# Based on Tailwind's default spacing scale
SPACING_SCALE: dict[str, str] = {
    "0": "0px",
    "px": "1px",
    "0.5": "2px",
    "1": "4px",
    "1.5": "6px",
    "2": "8px",
    "2.5": "10px",
    "3": "12px",
    "3.5": "14px",
    "4": "16px",
    "5": "20px",
    "6": "24px",
    "7": "28px",
    "8": "32px",
    "9": "36px",
    "10": "40px",
    "11": "44px",
    "12": "48px",
    "14": "56px",
    "16": "64px",
    "20": "80px",
    "24": "96px",
    "28": "112px",
    "32": "128px",
    "36": "144px",
    "40": "160px",
    "44": "176px",
    "48": "192px",
    "52": "208px",
    "56": "224px",
    "60": "240px",
    "64": "256px",
    "72": "288px",
    "80": "320px",
    "96": "384px",
}

# Special spacing values
SPACING_SPECIAL: dict[str, str] = {
    "auto": "auto",
}


def get_spacing_value(value: str, base_font_size: int = 16) -> str | None:
    """
    Get pixel value for a spacing value.

    Handles:
    - Numeric values from the scale (e.g., '4' -> '16px')
    - 'px' for 1px
    - 'auto' for auto
    - Arbitrary values like '[20px]' or '[1.5rem]'

    Args:
        value: The spacing value from the class
        base_font_size: Base font size for rem conversion

    Returns:
        CSS value string or None if invalid
    """
    # Check scale first
    if value in SPACING_SCALE:
        return SPACING_SCALE[value]

    # Check special values
    if value in SPACING_SPECIAL:
        return SPACING_SPECIAL[value]

    # Handle arbitrary values [value]
    if value.startswith("[") and value.endswith("]"):
        arbitrary = value[1:-1]
        return convert_to_px(arbitrary, base_font_size)

    # Try to interpret as a number (for extended scales)
    try:
        num = float(value)
        # 1 unit = 4px
        return f"{int(num * 4)}px"
    except ValueError:
        pass

    return None


def convert_to_px(value: str, base_font_size: int = 16) -> str:
    """
    Convert a CSS value to pixels.

    Args:
        value: CSS value like '1rem', '16px', '1.5em'
        base_font_size: Base font size for rem/em conversion

    Returns:
        Value in pixels
    """
    value = value.strip()

    if value.endswith("rem"):
        try:
            num = float(value[:-3])
            return f"{int(num * base_font_size)}px"
        except ValueError:
            return value

    if value.endswith("em"):
        try:
            num = float(value[:-2])
            return f"{int(num * base_font_size)}px"
        except ValueError:
            return value

    # Already in px or other unit
    return value


# Padding class patterns
PADDING_CLASSES: dict[str, str] = {
    "p": "padding",
    "px": "padding-left; padding-right",  # Will be split
    "py": "padding-top; padding-bottom",  # Will be split
    "pt": "padding-top",
    "pr": "padding-right",
    "pb": "padding-bottom",
    "pl": "padding-left",
    "ps": "padding-inline-start",  # Not well supported in email
    "pe": "padding-inline-end",  # Not well supported in email
}

# Margin class patterns
MARGIN_CLASSES: dict[str, str] = {
    "m": "margin",
    "mx": "margin-left; margin-right",  # Will be split
    "my": "margin-top; margin-bottom",  # Will be split
    "mt": "margin-top",
    "mr": "margin-right",
    "mb": "margin-bottom",
    "ml": "margin-left",
    "ms": "margin-inline-start",  # Not well supported in email
    "me": "margin-inline-end",  # Not well supported in email
}
