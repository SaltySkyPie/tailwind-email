"""
Utility functions for the tailwind-email converter.
"""

import re
from typing import Optional


def convert_to_px(value: str, base_font_size: int = 16) -> str:
    """
    Convert CSS value to pixels.

    Args:
        value: CSS value like '1rem', '16px', '1.5em', '50%'
        base_font_size: Base font size for rem/em conversion

    Returns:
        Value in pixels (or original if percentage/other unit)
    """
    value = value.strip()

    # Already px
    if value.endswith("px"):
        return value

    # Convert rem to px
    if value.endswith("rem"):
        try:
            num = float(value[:-3])
            return f"{int(num * base_font_size)}px"
        except ValueError:
            return value

    # Convert em to px
    if value.endswith("em"):
        try:
            num = float(value[:-2])
            return f"{int(num * base_font_size)}px"
        except ValueError:
            return value

    # Keep percentages and other values as-is
    return value


def parse_arbitrary_value(value: str) -> Optional[str]:
    """
    Parse Tailwind arbitrary value syntax [value].

    Args:
        value: String that may contain arbitrary value like '[20px]'

    Returns:
        The inner value or None if not arbitrary syntax
    """
    if value.startswith("[") and value.endswith("]"):
        return value[1:-1]
    return None


def hex_to_rgba(hex_color: str, opacity: float = 1.0) -> str:
    """
    Convert hex color to rgba with opacity.

    Args:
        hex_color: Hex color like '#3b82f6'
        opacity: Opacity value 0-1

    Returns:
        RGBA color string
    """
    hex_color = hex_color.lstrip("#")

    if len(hex_color) == 3:
        hex_color = "".join(c * 2 for c in hex_color)

    try:
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)

        if opacity < 1.0:
            return f"rgba({r}, {g}, {b}, {opacity})"
        return f"rgb({r}, {g}, {b})"
    except (ValueError, IndexError):
        return hex_color


def split_classes(class_string: str) -> list[str]:
    """
    Split a class string into individual classes.

    Args:
        class_string: Space-separated class string

    Returns:
        List of individual class names
    """
    if not class_string:
        return []
    return class_string.split()


def merge_styles(existing: str, new: str) -> str:
    """
    Merge two CSS style strings.

    Args:
        existing: Existing style string
        new: New styles to add

    Returns:
        Merged style string
    """
    if not existing:
        return new
    if not new:
        return existing

    # Parse existing styles into dict
    styles: dict[str, str] = {}

    for style in existing.split(";"):
        style = style.strip()
        if ":" in style:
            prop, val = style.split(":", 1)
            styles[prop.strip()] = val.strip()

    # Add new styles (overwriting existing)
    for style in new.split(";"):
        style = style.strip()
        if ":" in style:
            prop, val = style.split(":", 1)
            styles[prop.strip()] = val.strip()

    # Reconstruct style string
    return "; ".join(f"{k}: {v}" for k, v in styles.items())


def is_valid_hex_color(value: str) -> bool:
    """
    Check if a string is a valid hex color.

    Args:
        value: String to check

    Returns:
        True if valid hex color
    """
    pattern = r"^#([A-Fa-f0-9]{3}|[A-Fa-f0-9]{6})$"
    return bool(re.match(pattern, value))


def escape_css_value(value: str) -> str:
    """
    Escape special characters in CSS values.

    Args:
        value: CSS value to escape

    Returns:
        Escaped value
    """
    # Escape quotes and backslashes
    return value.replace("\\", "\\\\").replace('"', '\\"').replace("'", "\\'")


def generate_vml_rounded_rect(
    width: str,
    height: str,
    radius: str,
    background_color: str,
    border_color: Optional[str] = None,
    border_width: str = "0",
) -> str:
    """
    Generate VML roundrect for Outlook compatibility.

    Args:
        width: Width in pixels
        height: Height in pixels
        radius: Border radius in pixels
        background_color: Background color (hex)
        border_color: Border color (hex) or None
        border_width: Border width in pixels

    Returns:
        VML markup string
    """
    # Convert radius to VML arc size (0-1 scale based on smaller dimension)
    try:
        r = int(radius.replace("px", ""))
        w = int(width.replace("px", ""))
        h = int(height.replace("px", ""))
        min_dim = min(w, h)
        arc_size = min(r / (min_dim / 2), 1) if min_dim > 0 else 0
    except (ValueError, ZeroDivisionError):
        arc_size = 0.1

    stroke_attrs = ""
    if border_color and border_width != "0":
        stroke_attrs = f' strokecolor="{border_color}" strokeweight="{border_width}"'
    else:
        stroke_attrs = ' stroked="false"'

    vml = f"""<!--[if mso]>
<v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" style="width:{width};height:{height}" arcsize="{arc_size:.0%}" fillcolor="{background_color}"{stroke_attrs}>
<w:anchorlock/>
<center>
<![endif]-->"""

    return vml


def generate_vml_rounded_rect_end() -> str:
    """
    Generate VML roundrect closing tags.

    Returns:
        VML closing markup
    """
    return """<!--[if mso]>
</center>
</v:roundrect>
<![endif]-->"""


def generate_mso_line_height(line_height: str) -> str:
    """
    Generate MSO-specific line-height rule.

    Args:
        line_height: Line height value

    Returns:
        MSO line-height CSS property
    """
    return "mso-line-height-rule: exactly"


def camel_to_kebab(name: str) -> str:
    """
    Convert camelCase to kebab-case.

    Args:
        name: camelCase string

    Returns:
        kebab-case string
    """
    return re.sub(r"([a-z])([A-Z])", r"\1-\2", name).lower()


def kebab_to_camel(name: str) -> str:
    """
    Convert kebab-case to camelCase.

    Args:
        name: kebab-case string

    Returns:
        camelCase string
    """
    parts = name.split("-")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])
