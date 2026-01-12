"""
Tailwind CSS sizing utilities (width, height, max-width, min-width).
"""


# Width classes with direct CSS values
WIDTH_CLASSES: dict[str, str] = {
    # Pixel values (based on spacing scale * 4)
    "w-0": "0px",
    "w-px": "1px",
    "w-0.5": "2px",
    "w-1": "4px",
    "w-1.5": "6px",
    "w-2": "8px",
    "w-2.5": "10px",
    "w-3": "12px",
    "w-3.5": "14px",
    "w-4": "16px",
    "w-5": "20px",
    "w-6": "24px",
    "w-7": "28px",
    "w-8": "32px",
    "w-9": "36px",
    "w-10": "40px",
    "w-11": "44px",
    "w-12": "48px",
    "w-14": "56px",
    "w-16": "64px",
    "w-20": "80px",
    "w-24": "96px",
    "w-28": "112px",
    "w-32": "128px",
    "w-36": "144px",
    "w-40": "160px",
    "w-44": "176px",
    "w-48": "192px",
    "w-52": "208px",
    "w-56": "224px",
    "w-60": "240px",
    "w-64": "256px",
    "w-72": "288px",
    "w-80": "320px",
    "w-96": "384px",

    # Fractional widths
    "w-1/2": "50%",
    "w-1/3": "33.333333%",
    "w-2/3": "66.666667%",
    "w-1/4": "25%",
    "w-2/4": "50%",
    "w-3/4": "75%",
    "w-1/5": "20%",
    "w-2/5": "40%",
    "w-3/5": "60%",
    "w-4/5": "80%",
    "w-1/6": "16.666667%",
    "w-2/6": "33.333333%",
    "w-3/6": "50%",
    "w-4/6": "66.666667%",
    "w-5/6": "83.333333%",
    "w-1/12": "8.333333%",
    "w-2/12": "16.666667%",
    "w-3/12": "25%",
    "w-4/12": "33.333333%",
    "w-5/12": "41.666667%",
    "w-6/12": "50%",
    "w-7/12": "58.333333%",
    "w-8/12": "66.666667%",
    "w-9/12": "75%",
    "w-10/12": "83.333333%",
    "w-11/12": "91.666667%",

    # Container sizes (rem values converted to px)
    "w-3xs": "256px",  # 16rem
    "w-2xs": "288px",  # 18rem
    "w-xs": "320px",  # 20rem
    "w-sm": "384px",  # 24rem
    "w-md": "448px",  # 28rem
    "w-lg": "512px",  # 32rem
    "w-xl": "576px",  # 36rem
    "w-2xl": "672px",  # 42rem
    "w-3xl": "768px",  # 48rem
    "w-4xl": "896px",  # 56rem
    "w-5xl": "1024px",  # 64rem
    "w-6xl": "1152px",  # 72rem
    "w-7xl": "1280px",  # 80rem

    # Special values
    "w-auto": "auto",
    "w-full": "100%",
    "w-screen": "100vw",  # May not work in all email clients
    "w-min": "min-content",  # Limited email support
    "w-max": "max-content",  # Limited email support
    "w-fit": "fit-content",  # Limited email support
}

# Height classes
HEIGHT_CLASSES: dict[str, str] = {
    # Pixel values
    "h-0": "0px",
    "h-px": "1px",
    "h-0.5": "2px",
    "h-1": "4px",
    "h-1.5": "6px",
    "h-2": "8px",
    "h-2.5": "10px",
    "h-3": "12px",
    "h-3.5": "14px",
    "h-4": "16px",
    "h-5": "20px",
    "h-6": "24px",
    "h-7": "28px",
    "h-8": "32px",
    "h-9": "36px",
    "h-10": "40px",
    "h-11": "44px",
    "h-12": "48px",
    "h-14": "56px",
    "h-16": "64px",
    "h-20": "80px",
    "h-24": "96px",
    "h-28": "112px",
    "h-32": "128px",
    "h-36": "144px",
    "h-40": "160px",
    "h-44": "176px",
    "h-48": "192px",
    "h-52": "208px",
    "h-56": "224px",
    "h-60": "240px",
    "h-64": "256px",
    "h-72": "288px",
    "h-80": "320px",
    "h-96": "384px",

    # Fractional heights
    "h-1/2": "50%",
    "h-1/3": "33.333333%",
    "h-2/3": "66.666667%",
    "h-1/4": "25%",
    "h-2/4": "50%",
    "h-3/4": "75%",
    "h-1/5": "20%",
    "h-2/5": "40%",
    "h-3/5": "60%",
    "h-4/5": "80%",
    "h-1/6": "16.666667%",
    "h-2/6": "33.333333%",
    "h-3/6": "50%",
    "h-4/6": "66.666667%",
    "h-5/6": "83.333333%",

    # Special values
    "h-auto": "auto",
    "h-full": "100%",
    "h-screen": "100vh",  # May not work in all email clients
    "h-min": "min-content",  # Limited email support
    "h-max": "max-content",  # Limited email support
    "h-fit": "fit-content",  # Limited email support
}

# Max-width classes
MAX_WIDTH_CLASSES: dict[str, str] = {
    "max-w-0": "0px",
    "max-w-px": "1px",
    "max-w-none": "none",

    # Container sizes
    "max-w-3xs": "256px",
    "max-w-2xs": "288px",
    "max-w-xs": "320px",
    "max-w-sm": "384px",
    "max-w-md": "448px",
    "max-w-lg": "512px",
    "max-w-xl": "576px",
    "max-w-2xl": "672px",
    "max-w-3xl": "768px",
    "max-w-4xl": "896px",
    "max-w-5xl": "1024px",
    "max-w-6xl": "1152px",
    "max-w-7xl": "1280px",

    # Special values
    "max-w-full": "100%",
    "max-w-min": "min-content",
    "max-w-max": "max-content",
    "max-w-fit": "fit-content",
    "max-w-prose": "65ch",  # May not work well in email
    "max-w-screen-sm": "640px",
    "max-w-screen-md": "768px",
    "max-w-screen-lg": "1024px",
    "max-w-screen-xl": "1280px",
    "max-w-screen-2xl": "1536px",
}

# Min-width classes
MIN_WIDTH_CLASSES: dict[str, str] = {
    "min-w-0": "0px",
    "min-w-px": "1px",
    "min-w-full": "100%",
    "min-w-min": "min-content",
    "min-w-max": "max-content",
    "min-w-fit": "fit-content",

    # Container sizes
    "min-w-3xs": "256px",
    "min-w-2xs": "288px",
    "min-w-xs": "320px",
    "min-w-sm": "384px",
    "min-w-md": "448px",
    "min-w-lg": "512px",
    "min-w-xl": "576px",
    "min-w-2xl": "672px",
    "min-w-3xl": "768px",
    "min-w-4xl": "896px",
    "min-w-5xl": "1024px",
    "min-w-6xl": "1152px",
    "min-w-7xl": "1280px",
}

# Max-height classes
MAX_HEIGHT_CLASSES: dict[str, str] = {
    "max-h-0": "0px",
    "max-h-px": "1px",
    "max-h-none": "none",
    "max-h-full": "100%",
    "max-h-screen": "100vh",
    "max-h-min": "min-content",
    "max-h-max": "max-content",
    "max-h-fit": "fit-content",
}

# Min-height classes
MIN_HEIGHT_CLASSES: dict[str, str] = {
    "min-h-0": "0px",
    "min-h-px": "1px",
    "min-h-full": "100%",
    "min-h-screen": "100vh",
    "min-h-min": "min-content",
    "min-h-max": "max-content",
    "min-h-fit": "fit-content",
}
