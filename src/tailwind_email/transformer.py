"""
CSS transformer that converts Tailwind classes to inline CSS.
"""

import re
from typing import Optional

from tailwind_email.mappings.borders import (
    BORDER_RADIUS_CLASSES,
    BORDER_STYLE_CLASSES,
    BORDER_WIDTH_CLASSES,
)
from tailwind_email.mappings.colors import parse_color_with_opacity
from tailwind_email.mappings.effects import (
    BACKGROUND_POSITION_CLASSES,
    BACKGROUND_REPEAT_CLASSES,
    BACKGROUND_SIZE_CLASSES,
    BOX_SHADOW_CLASSES,
    CLEAR_CLASSES,
    DISPLAY_CLASSES,
    FLOAT_CLASSES,
    OPACITY_CLASSES,
    OVERFLOW_CLASSES,
    VISIBILITY_CLASSES,
)
from tailwind_email.mappings.sizing import (
    HEIGHT_CLASSES,
    MAX_HEIGHT_CLASSES,
    MAX_WIDTH_CLASSES,
    MIN_HEIGHT_CLASSES,
    MIN_WIDTH_CLASSES,
    WIDTH_CLASSES,
)
from tailwind_email.mappings.spacing import (
    MARGIN_CLASSES,
    PADDING_CLASSES,
    get_spacing_value,
)
from tailwind_email.mappings.typography import (
    EMAIL_SAFE_FONTS,
    FONT_SIZE_CLASSES,
    FONT_STYLE_CLASSES,
    FONT_WEIGHT_CLASSES,
    LETTER_SPACING_PX,
    LINE_HEIGHT_CLASSES,
    TEXT_ALIGN_CLASSES,
    TEXT_DECORATION_CLASSES,
    TEXT_TRANSFORM_CLASSES,
    VERTICAL_ALIGN_CLASSES,
    WHITE_SPACE_CLASSES,
    WORD_BREAK_CLASSES,
)
from tailwind_email.utils import convert_to_px, hex_to_rgba


class CSSTransformer:
    """Transforms Tailwind classes into inline CSS properties."""

    def __init__(self, base_font_size: int = 16, include_mso: bool = True) -> None:
        """
        Initialize the transformer.

        Args:
            base_font_size: Base font size for rem/em conversion
            include_mso: Include MSO-specific properties for Outlook
        """
        self.base_font_size = base_font_size
        self.include_mso = include_mso

    def transform_class(self, cls: str) -> Optional[dict[str, str]]:
        """
        Transform a single Tailwind class to CSS properties.

        Args:
            cls: Tailwind class name

        Returns:
            Dictionary of CSS property -> value, or None if not recognized
        """
        # Try each transformer in order
        result = (
            self._transform_spacing(cls)
            or self._transform_sizing(cls)
            or self._transform_typography(cls)
            or self._transform_colors(cls)
            or self._transform_borders(cls)
            or self._transform_effects(cls)
            or self._transform_display(cls)
            or self._transform_background(cls)
            or self._transform_arbitrary(cls)
        )

        return result

    def transform_classes(self, classes: list[str]) -> dict[str, str]:
        """
        Transform multiple Tailwind classes to CSS properties.

        Args:
            classes: List of Tailwind class names

        Returns:
            Combined dictionary of CSS properties
        """
        result: dict[str, str] = {}

        for cls in classes:
            props = self.transform_class(cls)
            if props:
                result.update(props)

        return result

    def to_style_string(self, properties: dict[str, str]) -> str:
        """
        Convert CSS properties dict to inline style string.

        Args:
            properties: Dictionary of CSS property -> value

        Returns:
            Inline style string
        """
        return "; ".join(f"{k}: {v}" for k, v in properties.items())

    def _transform_spacing(self, cls: str) -> Optional[dict[str, str]]:
        """Transform padding/margin classes."""
        # Padding classes
        for prefix, prop in PADDING_CLASSES.items():
            if cls.startswith(f"{prefix}-"):
                value_part = cls[len(prefix) + 1 :]
                px_value = get_spacing_value(value_part, self.base_font_size)
                if px_value:
                    if ";" in prop:
                        # px or py - need to set both properties
                        props = prop.split(";")
                        return {p.strip(): px_value for p in props}
                    return {prop: px_value}

        # Margin classes
        for prefix, prop in MARGIN_CLASSES.items():
            if cls.startswith(f"{prefix}-"):
                value_part = cls[len(prefix) + 1 :]
                px_value = get_spacing_value(value_part, self.base_font_size)
                if px_value:
                    if ";" in prop:
                        props = prop.split(";")
                        return {p.strip(): px_value for p in props}
                    return {prop: px_value}

        return None

    def _transform_sizing(self, cls: str) -> Optional[dict[str, str]]:
        """Transform width/height classes."""
        # Direct width classes
        if cls in WIDTH_CLASSES:
            return {"width": WIDTH_CLASSES[cls]}

        # Direct height classes
        if cls in HEIGHT_CLASSES:
            return {"height": HEIGHT_CLASSES[cls]}

        # Max-width classes
        if cls in MAX_WIDTH_CLASSES:
            return {"max-width": MAX_WIDTH_CLASSES[cls]}

        # Min-width classes
        if cls in MIN_WIDTH_CLASSES:
            return {"min-width": MIN_WIDTH_CLASSES[cls]}

        # Max-height classes
        if cls in MAX_HEIGHT_CLASSES:
            return {"max-height": MAX_HEIGHT_CLASSES[cls]}

        # Min-height classes
        if cls in MIN_HEIGHT_CLASSES:
            return {"min-height": MIN_HEIGHT_CLASSES[cls]}

        # Handle arbitrary width/height
        if cls.startswith("w-[") and cls.endswith("]"):
            value = convert_to_px(cls[3:-1], self.base_font_size)
            return {"width": value}

        if cls.startswith("h-[") and cls.endswith("]"):
            value = convert_to_px(cls[3:-1], self.base_font_size)
            return {"height": value}

        if cls.startswith("max-w-[") and cls.endswith("]"):
            value = convert_to_px(cls[7:-1], self.base_font_size)
            return {"max-width": value}

        if cls.startswith("min-w-[") and cls.endswith("]"):
            value = convert_to_px(cls[7:-1], self.base_font_size)
            return {"min-width": value}

        # Size utility (width + height)
        if cls.startswith("size-"):
            size_part = cls[5:]
            # Try width classes with 'w-' prefix
            width_cls = f"w-{size_part}"
            if width_cls in WIDTH_CLASSES:
                value = WIDTH_CLASSES[width_cls]
                return {"width": value, "height": value}
            # Arbitrary value
            if size_part.startswith("[") and size_part.endswith("]"):
                value = convert_to_px(size_part[1:-1], self.base_font_size)
                return {"width": value, "height": value}

        return None

    def _transform_typography(self, cls: str) -> Optional[dict[str, str]]:
        """Transform typography classes."""
        # Font size classes
        if cls in FONT_SIZE_CLASSES:
            font_size, line_height = FONT_SIZE_CLASSES[cls]
            result = {
                "font-size": font_size,
                "line-height": line_height,
            }
            if self.include_mso:
                result["mso-line-height-rule"] = "exactly"
            return result

        # Font weight classes
        if cls in FONT_WEIGHT_CLASSES:
            return {"font-weight": FONT_WEIGHT_CLASSES[cls]}

        # Line height classes
        if cls in LINE_HEIGHT_CLASSES:
            line_height_result: dict[str, str] = {"line-height": LINE_HEIGHT_CLASSES[cls]}
            if self.include_mso:
                line_height_result["mso-line-height-rule"] = "exactly"
            return line_height_result

        # Letter spacing classes
        if cls in LETTER_SPACING_PX:
            return {"letter-spacing": LETTER_SPACING_PX[cls]}

        # Text align classes
        if cls in TEXT_ALIGN_CLASSES:
            return {"text-align": TEXT_ALIGN_CLASSES[cls]}

        # Text decoration classes
        if cls in TEXT_DECORATION_CLASSES:
            return {"text-decoration": TEXT_DECORATION_CLASSES[cls]}

        # Text transform classes
        if cls in TEXT_TRANSFORM_CLASSES:
            return {"text-transform": TEXT_TRANSFORM_CLASSES[cls]}

        # Font style classes
        if cls in FONT_STYLE_CLASSES:
            return {"font-style": FONT_STYLE_CLASSES[cls]}

        # Vertical align classes
        if cls in VERTICAL_ALIGN_CLASSES:
            return {"vertical-align": VERTICAL_ALIGN_CLASSES[cls]}

        # White space classes
        if cls in WHITE_SPACE_CLASSES:
            return {"white-space": WHITE_SPACE_CLASSES[cls]}

        # Word break classes
        if cls in WORD_BREAK_CLASSES:
            if cls == "break-words":
                return {"overflow-wrap": "break-word"}
            return {"word-break": WORD_BREAK_CLASSES[cls]}

        # Font family classes (email-safe versions)
        if cls in EMAIL_SAFE_FONTS:
            return {"font-family": EMAIL_SAFE_FONTS[cls]}

        # Truncate utility
        if cls == "truncate":
            return {
                "overflow": "hidden",
                "text-overflow": "ellipsis",
                "white-space": "nowrap",
            }

        # Antialiased
        if cls == "antialiased":
            return {
                "-webkit-font-smoothing": "antialiased",
                "-moz-osx-font-smoothing": "grayscale",
            }

        if cls == "subpixel-antialiased":
            return {
                "-webkit-font-smoothing": "auto",
                "-moz-osx-font-smoothing": "auto",
            }

        return None

    def _transform_colors(self, cls: str) -> Optional[dict[str, str]]:
        """Transform color classes."""
        # Text color: text-{color}-{shade} or text-{color}-{shade}/{opacity}
        if cls.startswith("text-") and not cls.startswith(
            (
                "text-left",
                "text-center",
                "text-right",
                "text-justify",
                "text-start",
                "text-end",
                "text-xs",
                "text-sm",
                "text-base",
                "text-lg",
                "text-xl",
                "text-2xl",
                "text-3xl",
                "text-4xl",
                "text-5xl",
                "text-6xl",
                "text-7xl",
                "text-8xl",
                "text-9xl",
            )
        ):
            color_part = cls[5:]  # Remove 'text-'
            color, opacity = parse_color_with_opacity(color_part)
            if color:
                if opacity is not None and color.startswith("#"):
                    return {"color": hex_to_rgba(color, opacity)}
                return {"color": color}

        # Background color: bg-{color}-{shade}
        if cls.startswith("bg-") and not cls.startswith(
            (
                "bg-auto",
                "bg-cover",
                "bg-contain",
                "bg-fixed",
                "bg-local",
                "bg-scroll",
                "bg-clip-",
                "bg-origin-",
                "bg-repeat",
                "bg-no-repeat",
                "bg-repeat-",
                "bg-gradient-",
                "bg-none",
                "bg-bottom",
                "bg-center",
                "bg-left",
                "bg-right",
                "bg-top",
                "bg-blend-",
            )
        ):
            color_part = cls[3:]  # Remove 'bg-'
            color, opacity = parse_color_with_opacity(color_part)
            if color:
                if opacity is not None and color.startswith("#"):
                    return {"background-color": hex_to_rgba(color, opacity)}
                return {"background-color": color}

        # Border color: border-{color}-{shade}
        # Need to be careful not to match border-t-2, border-solid, etc.
        if cls.startswith("border-"):
            # Non-color border classes that should be excluded
            non_color_prefixes = (
                "border-0",
                "border-2",
                "border-4",
                "border-8",
                "border-t-",
                "border-r-",
                "border-b-",
                "border-l-",
                "border-x-",
                "border-y-",
                "border-t$",
                "border-r$",
                "border-b$",
                "border-l$",
                "border-x$",
                "border-y$",
            )
            non_color_exact = {
                "border-t",
                "border-r",
                "border-b",
                "border-l",
                "border-x",
                "border-y",
                "border-solid",
                "border-dashed",
                "border-dotted",
                "border-double",
                "border-hidden",
                "border-none",
                "border-collapse",
                "border-separate",
            }

            # Check if it's a non-color class
            is_non_color = cls in non_color_exact
            if not is_non_color:
                for prefix in non_color_prefixes:
                    if prefix.endswith("$"):
                        if cls == prefix[:-1]:
                            is_non_color = True
                            break
                    elif cls.startswith(prefix):
                        is_non_color = True
                        break

            if not is_non_color:
                color_part = cls[7:]  # Remove 'border-'
                color, opacity = parse_color_with_opacity(color_part)
                if color:
                    if opacity is not None and color.startswith("#"):
                        return {"border-color": hex_to_rgba(color, opacity)}
                    return {"border-color": color}

        # Outline color: outline-{color}-{shade}
        if cls.startswith("outline-") and not cls.startswith(
            (
                "outline-0",
                "outline-1",
                "outline-2",
                "outline-4",
                "outline-8",
                "outline-none",
                "outline-solid",
                "outline-dashed",
                "outline-dotted",
                "outline-double",
                "outline-offset",
            )
        ):
            color_part = cls[8:]  # Remove 'outline-'
            color, opacity = parse_color_with_opacity(color_part)
            if color:
                if opacity is not None and color.startswith("#"):
                    return {"outline-color": hex_to_rgba(color, opacity)}
                return {"outline-color": color}

        return None

    def _transform_borders(self, cls: str) -> Optional[dict[str, str]]:
        """Transform border classes."""
        # Simple border class (no width specified)
        if cls == "border":
            return {"border-width": "1px", "border-style": "solid"}

        # Border width classes
        if cls in BORDER_WIDTH_CLASSES:
            width = BORDER_WIDTH_CLASSES[cls]
            # Determine which property to set
            if cls.startswith("border-t"):
                return {"border-top-width": width, "border-top-style": "solid"}
            elif cls.startswith("border-r"):
                return {"border-right-width": width, "border-right-style": "solid"}
            elif cls.startswith("border-b"):
                return {"border-bottom-width": width, "border-bottom-style": "solid"}
            elif cls.startswith("border-l"):
                return {"border-left-width": width, "border-left-style": "solid"}
            elif cls.startswith("border-x"):
                return {
                    "border-left-width": width,
                    "border-right-width": width,
                    "border-left-style": "solid",
                    "border-right-style": "solid",
                }
            elif cls.startswith("border-y"):
                return {
                    "border-top-width": width,
                    "border-bottom-width": width,
                    "border-top-style": "solid",
                    "border-bottom-style": "solid",
                }
            else:
                return {"border-width": width, "border-style": "solid"}

        # Border radius classes
        if cls in BORDER_RADIUS_CLASSES:
            radius = BORDER_RADIUS_CLASSES[cls]
            # Determine which corners to set - check most specific patterns first
            if cls.startswith("rounded-tl-") or cls == "rounded-tl":
                return {"border-top-left-radius": radius}
            elif cls.startswith("rounded-tr-") or cls == "rounded-tr":
                return {"border-top-right-radius": radius}
            elif cls.startswith("rounded-bl-") or cls == "rounded-bl":
                return {"border-bottom-left-radius": radius}
            elif cls.startswith("rounded-br-") or cls == "rounded-br":
                return {"border-bottom-right-radius": radius}
            elif cls.startswith("rounded-t-") or cls == "rounded-t":
                return {
                    "border-top-left-radius": radius,
                    "border-top-right-radius": radius,
                }
            elif cls.startswith("rounded-b-") or cls == "rounded-b":
                return {
                    "border-bottom-left-radius": radius,
                    "border-bottom-right-radius": radius,
                }
            elif cls.startswith("rounded-l-") or cls == "rounded-l":
                return {
                    "border-top-left-radius": radius,
                    "border-bottom-left-radius": radius,
                }
            elif cls.startswith("rounded-r-") or cls == "rounded-r":
                return {
                    "border-top-right-radius": radius,
                    "border-bottom-right-radius": radius,
                }
            else:
                # This handles: rounded, rounded-none, rounded-sm, rounded-md, rounded-lg,
                # rounded-xl, rounded-2xl, rounded-3xl, rounded-4xl, rounded-full
                return {"border-radius": radius}

        # Border style classes
        if cls in BORDER_STYLE_CLASSES:
            return {"border-style": BORDER_STYLE_CLASSES[cls]}

        return None

    def _transform_effects(self, cls: str) -> Optional[dict[str, str]]:
        """Transform effects classes (shadows, opacity, etc.)."""
        # Box shadow classes
        if cls in BOX_SHADOW_CLASSES:
            return {"box-shadow": BOX_SHADOW_CLASSES[cls]}

        # Opacity classes
        if cls in OPACITY_CLASSES:
            return {"opacity": OPACITY_CLASSES[cls]}

        # Overflow classes
        if cls in OVERFLOW_CLASSES:
            value = OVERFLOW_CLASSES[cls]
            if cls.startswith("overflow-x"):
                return {"overflow-x": value}
            elif cls.startswith("overflow-y"):
                return {"overflow-y": value}
            else:
                return {"overflow": value}

        # Visibility classes
        if cls in VISIBILITY_CLASSES:
            return {"visibility": VISIBILITY_CLASSES[cls]}

        # Float classes
        if cls in FLOAT_CLASSES:
            return {"float": FLOAT_CLASSES[cls]}

        # Clear classes
        if cls in CLEAR_CLASSES:
            return {"clear": CLEAR_CLASSES[cls]}

        return None

    def _transform_display(self, cls: str) -> Optional[dict[str, str]]:
        """Transform display classes."""
        if cls in DISPLAY_CLASSES:
            return {"display": DISPLAY_CLASSES[cls]}

        return None

    def _transform_background(self, cls: str) -> Optional[dict[str, str]]:
        """Transform background-related classes."""
        # Background size
        if cls in BACKGROUND_SIZE_CLASSES:
            return {"background-size": BACKGROUND_SIZE_CLASSES[cls]}

        # Background position
        if cls in BACKGROUND_POSITION_CLASSES:
            return {"background-position": BACKGROUND_POSITION_CLASSES[cls]}

        # Background repeat
        if cls in BACKGROUND_REPEAT_CLASSES:
            return {"background-repeat": BACKGROUND_REPEAT_CLASSES[cls]}

        # Background none
        if cls == "bg-none":
            return {"background-image": "none"}

        return None

    def _transform_arbitrary(self, cls: str) -> Optional[dict[str, str]]:
        """Transform arbitrary value classes like [property:value]."""
        # Arbitrary property syntax: [property:value]
        if cls.startswith("[") and cls.endswith("]") and ":" in cls:
            inner = cls[1:-1]
            if ":" in inner:
                prop, value = inner.split(":", 1)
                # Convert camelCase to kebab-case if needed
                prop = re.sub(r"([a-z])([A-Z])", r"\1-\2", prop).lower()
                # Convert value units if needed
                value = convert_to_px(value, self.base_font_size)
                return {prop: value}

        return None
