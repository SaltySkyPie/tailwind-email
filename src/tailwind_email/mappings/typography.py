"""
Tailwind CSS typography utilities.
"""

# Font size classes with (font-size, line-height) in pixels
FONT_SIZE_CLASSES: dict[str, tuple[str, str]] = {
    "text-xs": ("12px", "16px"),
    "text-sm": ("14px", "20px"),
    "text-base": ("16px", "24px"),
    "text-lg": ("18px", "28px"),
    "text-xl": ("20px", "28px"),
    "text-2xl": ("24px", "32px"),
    "text-3xl": ("30px", "36px"),
    "text-4xl": ("36px", "40px"),
    "text-5xl": ("48px", "48px"),
    "text-6xl": ("60px", "60px"),
    "text-7xl": ("72px", "72px"),
    "text-8xl": ("96px", "96px"),
    "text-9xl": ("128px", "128px"),
}

# Font weight classes
FONT_WEIGHT_CLASSES: dict[str, str] = {
    "font-thin": "100",
    "font-extralight": "200",
    "font-light": "300",
    "font-normal": "400",
    "font-medium": "500",
    "font-semibold": "600",
    "font-bold": "700",
    "font-extrabold": "800",
    "font-black": "900",
}

# Line height classes (converted to unitless or px)
LINE_HEIGHT_CLASSES: dict[str, str] = {
    "leading-none": "1",
    "leading-tight": "1.25",
    "leading-snug": "1.375",
    "leading-normal": "1.5",
    "leading-relaxed": "1.625",
    "leading-loose": "2",
    # Numeric line heights (in spacing units -> px)
    "leading-3": "12px",
    "leading-4": "16px",
    "leading-5": "20px",
    "leading-6": "24px",
    "leading-7": "28px",
    "leading-8": "32px",
    "leading-9": "36px",
    "leading-10": "40px",
}

# Letter spacing classes
LETTER_SPACING_CLASSES: dict[str, str] = {
    "tracking-tighter": "-0.05em",
    "tracking-tight": "-0.025em",
    "tracking-normal": "0em",
    "tracking-wide": "0.025em",
    "tracking-wider": "0.05em",
    "tracking-widest": "0.1em",
}

# Convert em to px for letter-spacing (at 16px base)
LETTER_SPACING_PX: dict[str, str] = {
    "tracking-tighter": "-0.8px",
    "tracking-tight": "-0.4px",
    "tracking-normal": "0px",
    "tracking-wide": "0.4px",
    "tracking-wider": "0.8px",
    "tracking-widest": "1.6px",
}

# Text alignment classes
TEXT_ALIGN_CLASSES: dict[str, str] = {
    "text-left": "left",
    "text-center": "center",
    "text-right": "right",
    "text-justify": "justify",
    "text-start": "left",  # Fallback for email (start -> left for LTR)
    "text-end": "right",  # Fallback for email (end -> right for LTR)
}

# Text decoration classes
TEXT_DECORATION_CLASSES: dict[str, str] = {
    "underline": "underline",
    "overline": "overline",
    "line-through": "line-through",
    "no-underline": "none",
}

# Text transform classes
TEXT_TRANSFORM_CLASSES: dict[str, str] = {
    "uppercase": "uppercase",
    "lowercase": "lowercase",
    "capitalize": "capitalize",
    "normal-case": "none",
}

# Font style classes
FONT_STYLE_CLASSES: dict[str, str] = {
    "italic": "italic",
    "not-italic": "normal",
}

# Vertical align classes
VERTICAL_ALIGN_CLASSES: dict[str, str] = {
    "align-baseline": "baseline",
    "align-top": "top",
    "align-middle": "middle",
    "align-bottom": "bottom",
    "align-text-top": "text-top",
    "align-text-bottom": "text-bottom",
    "align-sub": "sub",
    "align-super": "super",
}

# White space classes
WHITE_SPACE_CLASSES: dict[str, str] = {
    "whitespace-normal": "normal",
    "whitespace-nowrap": "nowrap",
    "whitespace-pre": "pre",
    "whitespace-pre-line": "pre-line",
    "whitespace-pre-wrap": "pre-wrap",
    "whitespace-break-spaces": "break-spaces",
}

# Word break classes
WORD_BREAK_CLASSES: dict[str, str] = {
    "break-normal": "normal",
    "break-words": "break-word",  # Uses overflow-wrap
    "break-all": "break-all",
    "break-keep": "keep-all",
}

# Font family classes (common email-safe stacks)
FONT_FAMILY_CLASSES: dict[str, str] = {
    "font-sans": "ui-sans-serif, system-ui, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji'",
    "font-serif": "ui-serif, Georgia, Cambria, 'Times New Roman', Times, serif",
    "font-mono": "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace",
}

# Email-safe font family fallbacks
EMAIL_SAFE_FONTS: dict[str, str] = {
    "font-sans": "Arial, Helvetica, sans-serif",
    "font-serif": "Georgia, 'Times New Roman', Times, serif",
    "font-mono": "'Courier New', Courier, monospace",
}
