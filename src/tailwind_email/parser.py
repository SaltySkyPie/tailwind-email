"""
HTML parser for extracting and processing Tailwind classes.
"""

from collections.abc import Iterator

from bs4 import BeautifulSoup, Tag


class TailwindClassParser:
    """Parser for extracting Tailwind classes from HTML elements."""

    # Responsive prefixes to strip (not applicable in email)
    RESPONSIVE_PREFIXES = frozenset(["sm:", "md:", "lg:", "xl:", "2xl:"])

    # State prefixes to strip (not applicable in email)
    STATE_PREFIXES = frozenset(
        [
            "hover:",
            "focus:",
            "active:",
            "visited:",
            "disabled:",
            "first:",
            "last:",
            "odd:",
            "even:",
            "group-hover:",
            "focus-within:",
            "focus-visible:",
            "motion-safe:",
            "motion-reduce:",
            "dark:",
            "print:",
            "portrait:",
            "landscape:",
        ]
    )

    # Classes that are not supported in email and should be skipped
    UNSUPPORTED_CLASSES = frozenset(
        [
            # Flexbox (poor email support)
            "flex",
            "inline-flex",
            "flex-row",
            "flex-row-reverse",
            "flex-col",
            "flex-col-reverse",
            "flex-wrap",
            "flex-wrap-reverse",
            "flex-nowrap",
            "flex-1",
            "flex-auto",
            "flex-initial",
            "flex-none",
            "grow",
            "grow-0",
            "shrink",
            "shrink-0",
            "justify-start",
            "justify-end",
            "justify-center",
            "justify-between",
            "justify-around",
            "justify-evenly",
            "justify-stretch",
            "items-start",
            "items-end",
            "items-center",
            "items-baseline",
            "items-stretch",
            "self-auto",
            "self-start",
            "self-end",
            "self-center",
            "self-stretch",
            "self-baseline",
            "content-start",
            "content-end",
            "content-center",
            "content-between",
            "content-around",
            "content-evenly",
            "content-stretch",
            # Grid (poor email support)
            "grid",
            "inline-grid",
            "contents",
            "flow-root",
            # Gap (requires flex/grid)
            "gap-0",
            "gap-1",
            "gap-2",
            "gap-3",
            "gap-4",
            "gap-5",
            "gap-6",
            "gap-7",
            "gap-8",
            "gap-9",
            "gap-10",
            "gap-11",
            "gap-12",
            # Transforms (46% email support)
            "transform",
            "transform-gpu",
            "transform-none",
            # Transitions/Animations (not applicable in email)
            "transition",
            "transition-all",
            "transition-colors",
            "transition-opacity",
            "transition-shadow",
            "transition-transform",
            "duration-75",
            "duration-100",
            "duration-150",
            "duration-200",
            "duration-300",
            "duration-500",
            "duration-700",
            "duration-1000",
            "ease-linear",
            "ease-in",
            "ease-out",
            "ease-in-out",
            "animate-none",
            "animate-spin",
            "animate-ping",
            "animate-pulse",
            "animate-bounce",
            # Backdrop filters (limited email support)
            "backdrop-blur",
            "backdrop-brightness",
            "backdrop-contrast",
            "backdrop-grayscale",
            "backdrop-hue-rotate",
            "backdrop-invert",
            "backdrop-opacity",
            "backdrop-saturate",
            "backdrop-sepia",
            # Filters (limited email support)
            "blur",
            "blur-sm",
            "blur-md",
            "blur-lg",
            "blur-xl",
            "blur-2xl",
            "blur-3xl",
            "brightness-0",
            "brightness-50",
            "brightness-75",
            "brightness-90",
            "brightness-95",
            "brightness-100",
            "brightness-105",
            "brightness-110",
            "brightness-125",
            "brightness-150",
            "brightness-200",
            "contrast-0",
            "contrast-50",
            "contrast-75",
            "contrast-100",
            "contrast-125",
            "contrast-150",
            "contrast-200",
            "grayscale",
            "grayscale-0",
            "hue-rotate-0",
            "hue-rotate-15",
            "hue-rotate-30",
            "hue-rotate-60",
            "hue-rotate-90",
            "hue-rotate-180",
            "invert",
            "invert-0",
            "saturate-0",
            "saturate-50",
            "saturate-100",
            "saturate-150",
            "saturate-200",
            "sepia",
            "sepia-0",
            "drop-shadow",
            "drop-shadow-sm",
            "drop-shadow-md",
            "drop-shadow-lg",
            "drop-shadow-xl",
            "drop-shadow-2xl",
            "drop-shadow-none",
            # Screen reader (semantic, no visual output)
            "sr-only",
            "not-sr-only",
            # Scroll behavior (not applicable in email)
            "scroll-auto",
            "scroll-smooth",
            "scroll-m-0",
            "scroll-m-1",
            "scroll-p-0",
            "scroll-p-1",
            "snap-start",
            "snap-end",
            "snap-center",
            "snap-align-none",
            "snap-normal",
            "snap-always",
            "snap-mandatory",
            "snap-proximity",
            "snap-none",
            "snap-x",
            "snap-y",
            "snap-both",
            # Touch action (not applicable in email)
            "touch-auto",
            "touch-none",
            "touch-pan-x",
            "touch-pan-left",
            "touch-pan-right",
            "touch-pan-y",
            "touch-pan-up",
            "touch-pan-down",
            "touch-pinch-zoom",
            "touch-manipulation",
            # User select (limited email support)
            "select-none",
            "select-text",
            "select-all",
            "select-auto",
            # Resize (not applicable in email)
            "resize-none",
            "resize-y",
            "resize-x",
            "resize",
            # Will change (not applicable in email)
            "will-change-auto",
            "will-change-scroll",
            "will-change-contents",
            "will-change-transform",
            # Container queries (not supported in email)
            "container",
            # Aspect ratio (limited email support)
            "aspect-auto",
            "aspect-square",
            "aspect-video",
            # Columns (limited email support)
            "columns-1",
            "columns-2",
            "columns-3",
            "columns-4",
            "columns-5",
            "columns-6",
            "columns-7",
            "columns-8",
            "columns-9",
            "columns-10",
            "columns-11",
            "columns-12",
            "columns-auto",
            "columns-3xs",
            "columns-2xs",
            "columns-xs",
            "columns-sm",
            "columns-md",
            "columns-lg",
            "columns-xl",
            "columns-2xl",
            "columns-3xl",
            "columns-4xl",
            "columns-5xl",
            "columns-6xl",
            "columns-7xl",
            # Break utilities (limited email support)
            "break-after-auto",
            "break-after-avoid",
            "break-after-all",
            "break-after-avoid-page",
            "break-after-page",
            "break-after-left",
            "break-after-right",
            "break-after-column",
            "break-before-auto",
            "break-before-avoid",
            "break-before-all",
            "break-before-avoid-page",
            "break-before-page",
            "break-before-left",
            "break-before-right",
            "break-before-column",
            "break-inside-auto",
            "break-inside-avoid",
            "break-inside-avoid-page",
            "break-inside-avoid-column",
            # Box decoration break
            "box-decoration-clone",
            "box-decoration-slice",
            # Isolation
            "isolate",
            "isolation-auto",
            # Mix blend mode (limited email support)
            "mix-blend-normal",
            "mix-blend-multiply",
            "mix-blend-screen",
            "mix-blend-overlay",
            "mix-blend-darken",
            "mix-blend-lighten",
            "mix-blend-color-dodge",
            "mix-blend-color-burn",
            "mix-blend-hard-light",
            "mix-blend-soft-light",
            "mix-blend-difference",
            "mix-blend-exclusion",
            "mix-blend-hue",
            "mix-blend-saturation",
            "mix-blend-color",
            "mix-blend-luminosity",
            "mix-blend-plus-darker",
            "mix-blend-plus-lighter",
            # Background blend mode
            "bg-blend-normal",
            "bg-blend-multiply",
            "bg-blend-screen",
            "bg-blend-overlay",
            "bg-blend-darken",
            "bg-blend-lighten",
            "bg-blend-color-dodge",
            "bg-blend-color-burn",
            "bg-blend-hard-light",
            "bg-blend-soft-light",
            "bg-blend-difference",
            "bg-blend-exclusion",
            "bg-blend-hue",
            "bg-blend-saturation",
            "bg-blend-color",
            "bg-blend-luminosity",
            # Background attachment (limited email support)
            "bg-fixed",
            "bg-local",
            "bg-scroll",
            # Background clip (limited email support)
            "bg-clip-border",
            "bg-clip-padding",
            "bg-clip-content",
            "bg-clip-text",
            # Background origin
            "bg-origin-border",
            "bg-origin-padding",
            "bg-origin-content",
            # Pointer events (limited email support)
            "pointer-events-none",
            "pointer-events-auto",
            # Place utilities (requires grid)
            "place-content-center",
            "place-content-start",
            "place-content-end",
            "place-content-between",
            "place-content-around",
            "place-content-evenly",
            "place-content-baseline",
            "place-content-stretch",
            "place-items-start",
            "place-items-end",
            "place-items-center",
            "place-items-baseline",
            "place-items-stretch",
            "place-self-auto",
            "place-self-start",
            "place-self-end",
            "place-self-center",
            "place-self-stretch",
            # Order (requires flex/grid)
            "order-1",
            "order-2",
            "order-3",
            "order-4",
            "order-5",
            "order-6",
            "order-7",
            "order-8",
            "order-9",
            "order-10",
            "order-11",
            "order-12",
            "order-first",
            "order-last",
            "order-none",
            # Appearance
            "appearance-none",
            "appearance-auto",
            # Accent color (form elements)
            "accent-auto",
            # Caret color (limited email support)
            "caret-inherit",
            "caret-current",
            "caret-transparent",
        ]
    )

    def __init__(self) -> None:
        """Initialize the parser."""
        pass

    def parse_html(self, html: str) -> BeautifulSoup:
        """
        Parse HTML string into BeautifulSoup object.

        Args:
            html: HTML string to parse

        Returns:
            BeautifulSoup object
        """
        return BeautifulSoup(html, "lxml")

    def get_elements_with_classes(self, soup: BeautifulSoup) -> Iterator[Tag]:
        """
        Get all elements that have class attributes.

        Args:
            soup: BeautifulSoup object

        Yields:
            Elements with class attributes
        """
        for element in soup.find_all(class_=True):
            if isinstance(element, Tag):
                yield element

    def extract_classes(self, element: Tag) -> list[str]:
        """
        Extract classes from an element.

        Args:
            element: BeautifulSoup Tag element

        Returns:
            List of class names
        """
        classes = element.get("class")
        if classes is None:
            return []
        if isinstance(classes, str):
            return classes.split()
        return list(classes)

    def filter_supported_classes(self, classes: list[str]) -> list[str]:
        """
        Filter out unsupported and responsive/state-prefixed classes.

        Args:
            classes: List of class names

        Returns:
            Filtered list of supported classes
        """
        result = []

        for cls in classes:
            # Skip responsive prefixes
            if any(cls.startswith(prefix) for prefix in self.RESPONSIVE_PREFIXES):
                continue

            # Skip state prefixes
            if any(cls.startswith(prefix) for prefix in self.STATE_PREFIXES):
                continue

            # Skip explicitly unsupported classes
            if cls in self.UNSUPPORTED_CLASSES:
                continue

            # Skip classes starting with unsupported patterns
            if self._is_unsupported_pattern(cls):
                continue

            result.append(cls)

        return result

    def _is_unsupported_pattern(self, cls: str) -> bool:
        """
        Check if a class matches unsupported patterns.

        Args:
            cls: Class name to check

        Returns:
            True if class matches unsupported pattern
        """
        # Gap classes
        if cls.startswith("gap-"):
            return True

        # Grid column/row classes
        if cls.startswith(("grid-cols-", "grid-rows-", "col-", "row-")):
            return True

        # Rotate/scale/translate classes
        if cls.startswith(("rotate-", "scale-", "translate-", "skew-")):
            return True

        # Negative margins (not supported)
        # Patterns: -m-4, -mx-4, -my-4, -mt-4, -mr-4, -mb-4, -ml-4, -ms-4, -me-4
        if cls.startswith("-m"):
            rest = cls[2:]
            # Check for patterns like -m-4, -mx-4, etc.
            if rest.startswith("-") or rest.startswith(
                ("x-", "y-", "t-", "r-", "b-", "l-", "s-", "e-")
            ):
                return True

        # Order classes
        if cls.startswith("order-"):
            return True

        # Ring classes (not well supported)
        if cls.startswith("ring"):
            return True

        # Divide classes (requires adjacent sibling selector)
        if cls.startswith("divide-"):
            return True

        # Space between classes (requires adjacent sibling selector)
        if cls.startswith("space-"):
            return True

        return False

    def is_tailwind_class(self, cls: str) -> bool:
        """
        Check if a class looks like a Tailwind class.

        Args:
            cls: Class name to check

        Returns:
            True if class appears to be a Tailwind class
        """
        # Tailwind classes typically follow these patterns:
        # - Single keyword: block, hidden, flex, etc.
        # - Prefix-value: p-4, text-lg, bg-blue-500
        # - Prefix-modifier-value: text-blue-500/50

        # Single-word Tailwind classes
        single_words = {
            "block",
            "inline",
            "inline-block",
            "hidden",
            "visible",
            "invisible",
            "flex",
            "inline-flex",
            "grid",
            "inline-grid",
            "contents",
            "flow-root",
            "static",
            "fixed",
            "absolute",
            "relative",
            "sticky",
            "italic",
            "not-italic",
            "underline",
            "overline",
            "line-through",
            "no-underline",
            "uppercase",
            "lowercase",
            "capitalize",
            "normal-case",
            "truncate",
            "antialiased",
            "subpixel-antialiased",
            "table",
            "table-caption",
            "table-cell",
            "table-column",
            "table-column-group",
            "table-footer-group",
            "table-header-group",
            "table-row-group",
            "table-row",
            "list-item",
            "border",
            "border-collapse",
            "border-separate",
            "rounded",
            "container",
        }

        if cls in single_words:
            return True

        # Arbitrary value syntax
        if "[" in cls and "]" in cls:
            return True

        # For prefix-based classes, we need to be more careful
        # The pattern should be: prefix + (number | keyword | color | arbitrary)
        # Not just any string that happens to start with the prefix

        # Common Tailwind prefixes with their expected value patterns
        prefix_patterns = [
            # Spacing prefixes - expect number, px, auto, or arbitrary
            ("p-", r"^p-(\d+\.?\d*|px|auto|\[.+\])$"),
            ("px-", r"^px-(\d+\.?\d*|px|auto|\[.+\])$"),
            ("py-", r"^py-(\d+\.?\d*|px|auto|\[.+\])$"),
            ("pt-", r"^pt-(\d+\.?\d*|px|auto|\[.+\])$"),
            ("pr-", r"^pr-(\d+\.?\d*|px|auto|\[.+\])$"),
            ("pb-", r"^pb-(\d+\.?\d*|px|auto|\[.+\])$"),
            ("pl-", r"^pl-(\d+\.?\d*|px|auto|\[.+\])$"),
            ("m-", r"^m-(\d+\.?\d*|px|auto|\[.+\])$"),
            ("mx-", r"^mx-(\d+\.?\d*|px|auto|\[.+\])$"),
            ("my-", r"^my-(\d+\.?\d*|px|auto|\[.+\])$"),
            ("mt-", r"^mt-(\d+\.?\d*|px|auto|\[.+\])$"),
            ("mr-", r"^mr-(\d+\.?\d*|px|auto|\[.+\])$"),
            ("mb-", r"^mb-(\d+\.?\d*|px|auto|\[.+\])$"),
            ("ml-", r"^ml-(\d+\.?\d*|px|auto|\[.+\])$"),
        ]

        # Check spacing patterns strictly
        for prefix, pattern in prefix_patterns:
            if cls.startswith(prefix):
                import re

                if re.match(pattern, cls):
                    return True
                return False

        # Other prefixes that are less ambiguous
        safe_prefixes = (
            "w-",
            "h-",
            "min-w-",
            "max-w-",
            "min-h-",
            "max-h-",
            "text-",
            "font-",
            "leading-",
            "tracking-",
            "bg-",
            "border-",
            "rounded-",
            "shadow-",
            "opacity-",
            "z-",
            "top-",
            "right-",
            "bottom-",
            "left-",
            "overflow-",
            "object-",
            "list-",
            "decoration-",
            "outline-",
            "cursor-",
            "resize-",
            "appearance-",
            "inset-",
            "size-",
            "basis-",
            "aspect-",
            "align-",
            "whitespace-",
            "float-",
            "clear-",
        )

        if cls.startswith(safe_prefixes):
            return True

        return False
