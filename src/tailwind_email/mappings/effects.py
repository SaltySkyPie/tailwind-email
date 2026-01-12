"""
Tailwind CSS effects utilities (shadows, opacity, etc.).

Note: These have limited email client support (~60-70%).
"""


# Box shadow classes
# These may not work in all email clients (especially Outlook desktop)
BOX_SHADOW_CLASSES: dict[str, str] = {
    "shadow-sm": "0 1px 2px 0 rgba(0, 0, 0, 0.05)",
    "shadow": "0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px -1px rgba(0, 0, 0, 0.1)",
    "shadow-md": "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -2px rgba(0, 0, 0, 0.1)",
    "shadow-lg": "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1)",
    "shadow-xl": "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1)",
    "shadow-2xl": "0 25px 50px -12px rgba(0, 0, 0, 0.25)",
    "shadow-inner": "inset 0 2px 4px 0 rgba(0, 0, 0, 0.05)",
    "shadow-none": "none",
}

# Opacity classes
OPACITY_CLASSES: dict[str, str] = {
    "opacity-0": "0",
    "opacity-5": "0.05",
    "opacity-10": "0.1",
    "opacity-15": "0.15",
    "opacity-20": "0.2",
    "opacity-25": "0.25",
    "opacity-30": "0.3",
    "opacity-35": "0.35",
    "opacity-40": "0.4",
    "opacity-45": "0.45",
    "opacity-50": "0.5",
    "opacity-55": "0.55",
    "opacity-60": "0.6",
    "opacity-65": "0.65",
    "opacity-70": "0.7",
    "opacity-75": "0.75",
    "opacity-80": "0.8",
    "opacity-85": "0.85",
    "opacity-90": "0.9",
    "opacity-95": "0.95",
    "opacity-100": "1",
}

# Display classes that are safe for email
DISPLAY_CLASSES: dict[str, str] = {
    "block": "block",
    "inline": "inline",
    "inline-block": "inline-block",
    "hidden": "none",

    # Table displays (well supported in email)
    "table": "table",
    "table-caption": "table-caption",
    "table-cell": "table-cell",
    "table-column": "table-column",
    "table-column-group": "table-column-group",
    "table-footer-group": "table-footer-group",
    "table-header-group": "table-header-group",
    "table-row-group": "table-row-group",
    "table-row": "table-row",

    # These have poor email support and will be stripped or ignored:
    # "flex", "inline-flex", "grid", "inline-grid", "contents", "flow-root"
}

# Overflow classes
OVERFLOW_CLASSES: dict[str, str] = {
    "overflow-auto": "auto",
    "overflow-hidden": "hidden",
    "overflow-clip": "clip",
    "overflow-visible": "visible",
    "overflow-scroll": "scroll",

    "overflow-x-auto": "auto",
    "overflow-x-hidden": "hidden",
    "overflow-x-clip": "clip",
    "overflow-x-visible": "visible",
    "overflow-x-scroll": "scroll",

    "overflow-y-auto": "auto",
    "overflow-y-hidden": "hidden",
    "overflow-y-clip": "clip",
    "overflow-y-visible": "visible",
    "overflow-y-scroll": "scroll",
}

# Visibility classes
VISIBILITY_CLASSES: dict[str, str] = {
    "visible": "visible",
    "invisible": "hidden",
    "collapse": "collapse",
}

# Cursor classes (limited email support, but may work in webmail)
CURSOR_CLASSES: dict[str, str] = {
    "cursor-auto": "auto",
    "cursor-default": "default",
    "cursor-pointer": "pointer",
    "cursor-wait": "wait",
    "cursor-text": "text",
    "cursor-move": "move",
    "cursor-help": "help",
    "cursor-not-allowed": "not-allowed",
    "cursor-none": "none",
    "cursor-progress": "progress",
    "cursor-cell": "cell",
    "cursor-crosshair": "crosshair",
    "cursor-grab": "grab",
    "cursor-grabbing": "grabbing",
}

# Z-index classes (limited email support)
Z_INDEX_CLASSES: dict[str, str] = {
    "z-0": "0",
    "z-10": "10",
    "z-20": "20",
    "z-30": "30",
    "z-40": "40",
    "z-50": "50",
    "z-auto": "auto",
}

# Position classes (limited email support)
POSITION_CLASSES: dict[str, str] = {
    "static": "static",
    "fixed": "fixed",  # Poor email support
    "absolute": "absolute",  # Poor email support
    "relative": "relative",
    "sticky": "sticky",  # Poor email support
}

# Float classes
FLOAT_CLASSES: dict[str, str] = {
    "float-start": "left",  # Fallback for LTR
    "float-end": "right",  # Fallback for LTR
    "float-right": "right",
    "float-left": "left",
    "float-none": "none",
}

# Clear classes
CLEAR_CLASSES: dict[str, str] = {
    "clear-start": "left",  # Fallback for LTR
    "clear-end": "right",  # Fallback for LTR
    "clear-left": "left",
    "clear-right": "right",
    "clear-both": "both",
    "clear-none": "none",
}

# Object fit classes (for images, limited email support)
OBJECT_FIT_CLASSES: dict[str, str] = {
    "object-contain": "contain",
    "object-cover": "cover",
    "object-fill": "fill",
    "object-none": "none",
    "object-scale-down": "scale-down",
}

# Background size classes
BACKGROUND_SIZE_CLASSES: dict[str, str] = {
    "bg-auto": "auto",
    "bg-cover": "cover",
    "bg-contain": "contain",
}

# Background position classes
BACKGROUND_POSITION_CLASSES: dict[str, str] = {
    "bg-bottom": "bottom",
    "bg-center": "center",
    "bg-left": "left",
    "bg-left-bottom": "left bottom",
    "bg-left-top": "left top",
    "bg-right": "right",
    "bg-right-bottom": "right bottom",
    "bg-right-top": "right top",
    "bg-top": "top",
}

# Background repeat classes
BACKGROUND_REPEAT_CLASSES: dict[str, str] = {
    "bg-repeat": "repeat",
    "bg-no-repeat": "no-repeat",
    "bg-repeat-x": "repeat-x",
    "bg-repeat-y": "repeat-y",
    "bg-repeat-round": "round",
    "bg-repeat-space": "space",
}
