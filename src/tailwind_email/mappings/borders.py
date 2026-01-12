"""
Tailwind CSS border utilities.
"""

# Border width classes
BORDER_WIDTH_CLASSES: dict[str, str] = {
    "border": "1px",
    "border-0": "0px",
    "border-2": "2px",
    "border-4": "4px",
    "border-8": "8px",  # Max recommended for Outlook
    # Individual sides
    "border-t": "1px",
    "border-t-0": "0px",
    "border-t-2": "2px",
    "border-t-4": "4px",
    "border-t-8": "8px",
    "border-r": "1px",
    "border-r-0": "0px",
    "border-r-2": "2px",
    "border-r-4": "4px",
    "border-r-8": "8px",
    "border-b": "1px",
    "border-b-0": "0px",
    "border-b-2": "2px",
    "border-b-4": "4px",
    "border-b-8": "8px",
    "border-l": "1px",
    "border-l-0": "0px",
    "border-l-2": "2px",
    "border-l-4": "4px",
    "border-l-8": "8px",
    # Horizontal/Vertical
    "border-x": "1px",
    "border-x-0": "0px",
    "border-x-2": "2px",
    "border-x-4": "4px",
    "border-x-8": "8px",
    "border-y": "1px",
    "border-y-0": "0px",
    "border-y-2": "2px",
    "border-y-4": "4px",
    "border-y-8": "8px",
}

# Border radius classes (in pixels)
BORDER_RADIUS_CLASSES: dict[str, str] = {
    "rounded-none": "0px",
    "rounded-sm": "2px",
    "rounded": "4px",
    "rounded-md": "6px",
    "rounded-lg": "8px",
    "rounded-xl": "12px",
    "rounded-2xl": "16px",
    "rounded-3xl": "24px",
    "rounded-4xl": "32px",
    "rounded-full": "9999px",
    # Top corners
    "rounded-t-none": "0px",
    "rounded-t-sm": "2px",
    "rounded-t": "4px",
    "rounded-t-md": "6px",
    "rounded-t-lg": "8px",
    "rounded-t-xl": "12px",
    "rounded-t-2xl": "16px",
    "rounded-t-3xl": "24px",
    "rounded-t-full": "9999px",
    # Bottom corners
    "rounded-b-none": "0px",
    "rounded-b-sm": "2px",
    "rounded-b": "4px",
    "rounded-b-md": "6px",
    "rounded-b-lg": "8px",
    "rounded-b-xl": "12px",
    "rounded-b-2xl": "16px",
    "rounded-b-3xl": "24px",
    "rounded-b-full": "9999px",
    # Left corners
    "rounded-l-none": "0px",
    "rounded-l-sm": "2px",
    "rounded-l": "4px",
    "rounded-l-md": "6px",
    "rounded-l-lg": "8px",
    "rounded-l-xl": "12px",
    "rounded-l-2xl": "16px",
    "rounded-l-3xl": "24px",
    "rounded-l-full": "9999px",
    # Right corners
    "rounded-r-none": "0px",
    "rounded-r-sm": "2px",
    "rounded-r": "4px",
    "rounded-r-md": "6px",
    "rounded-r-lg": "8px",
    "rounded-r-xl": "12px",
    "rounded-r-2xl": "16px",
    "rounded-r-3xl": "24px",
    "rounded-r-full": "9999px",
    # Individual corners
    "rounded-tl-none": "0px",
    "rounded-tl-sm": "2px",
    "rounded-tl": "4px",
    "rounded-tl-md": "6px",
    "rounded-tl-lg": "8px",
    "rounded-tl-xl": "12px",
    "rounded-tl-2xl": "16px",
    "rounded-tl-3xl": "24px",
    "rounded-tl-full": "9999px",
    "rounded-tr-none": "0px",
    "rounded-tr-sm": "2px",
    "rounded-tr": "4px",
    "rounded-tr-md": "6px",
    "rounded-tr-lg": "8px",
    "rounded-tr-xl": "12px",
    "rounded-tr-2xl": "16px",
    "rounded-tr-3xl": "24px",
    "rounded-tr-full": "9999px",
    "rounded-bl-none": "0px",
    "rounded-bl-sm": "2px",
    "rounded-bl": "4px",
    "rounded-bl-md": "6px",
    "rounded-bl-lg": "8px",
    "rounded-bl-xl": "12px",
    "rounded-bl-2xl": "16px",
    "rounded-bl-3xl": "24px",
    "rounded-bl-full": "9999px",
    "rounded-br-none": "0px",
    "rounded-br-sm": "2px",
    "rounded-br": "4px",
    "rounded-br-md": "6px",
    "rounded-br-lg": "8px",
    "rounded-br-xl": "12px",
    "rounded-br-2xl": "16px",
    "rounded-br-3xl": "24px",
    "rounded-br-full": "9999px",
}

# Border style classes
BORDER_STYLE_CLASSES: dict[str, str] = {
    "border-solid": "solid",
    "border-dashed": "dashed",
    "border-dotted": "dotted",
    "border-double": "double",
    "border-hidden": "hidden",
    "border-none": "none",
}

# Outline width classes
OUTLINE_WIDTH_CLASSES: dict[str, str] = {
    "outline": "2px",
    "outline-0": "0px",
    "outline-1": "1px",
    "outline-2": "2px",
    "outline-4": "4px",
    "outline-8": "8px",
}

# Outline style classes
OUTLINE_STYLE_CLASSES: dict[str, str] = {
    "outline-solid": "solid",
    "outline-dashed": "dashed",
    "outline-dotted": "dotted",
    "outline-double": "double",
    "outline-none": "none",
}

# Outline offset classes
OUTLINE_OFFSET_CLASSES: dict[str, str] = {
    "outline-offset-0": "0px",
    "outline-offset-1": "1px",
    "outline-offset-2": "2px",
    "outline-offset-4": "4px",
    "outline-offset-8": "8px",
}
