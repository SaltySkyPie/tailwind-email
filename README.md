# tailwind-email

Transform HTML with Tailwind CSS classes into email-client-compatible HTML with inline styles.

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

`tailwind-email` is a Python library that converts Tailwind CSS utility classes in your HTML to inline styles that work across all major email clients. It's designed to help developers build beautiful email templates using familiar Tailwind CSS syntax while ensuring maximum compatibility.

### Key Features

- **Full Tailwind v4 Support**: Supports the complete Tailwind CSS v4 color palette and utility classes
- **Email-Safe CSS**: Automatically converts modern CSS to email-compatible inline styles
- **Smart Filtering**: Removes unsupported classes (flexbox, grid, transforms) that don't work in emails
- **MSO Properties**: Includes Microsoft Office-specific properties for Outlook compatibility
- **VML Fallbacks**: Generates VML markup for border-radius support in Outlook
- **Unit Conversion**: Converts rem/em units to pixels for consistent rendering
- **Color Conversion**: Converts all color formats (including OKLCH) to hex values
- **Zero JS Dependencies**: Pure Python implementation with no Node.js required

## Installation

```bash
pip install tailwind-email
```

Or install from source:

```bash
git clone https://github.com/tailwind-email/tailwind-email.git
cd tailwind-email
pip install -e .
```

## Quick Start

### Basic Usage

```python
from tailwind_email import convert

html_input = """
<div class="bg-blue-500 p-4 text-white rounded-lg">
    <h1 class="text-2xl font-bold">Hello World</h1>
    <p class="mt-2 text-sm">This is an email-safe component.</p>
</div>
"""

html_output = convert(html_input)
print(html_output)
```

### Output

```html
<div style="background-color: #3b82f6; padding: 16px; color: #ffffff; border-radius: 8px;">
    <h1 style="font-size: 24px; line-height: 32px; mso-line-height-rule: exactly; font-weight: 700;">Hello World</h1>
    <p style="margin-top: 8px; font-size: 14px; line-height: 20px; mso-line-height-rule: exactly;">This is an email-safe component.</p>
</div>
```

### Using the Converter Class

For multiple conversions or custom options, use the `TailwindEmailConverter` class:

```python
from tailwind_email import TailwindEmailConverter
from tailwind_email.converter import ConversionOptions

# Create converter with custom options
options = ConversionOptions(
    base_font_size=16,
    include_mso_properties=True,
    include_vml_fallbacks=True,
    preserve_classes=False,
)
converter = TailwindEmailConverter(options)

# Convert multiple templates
html1 = converter.convert('<div class="p-4">First</div>')
html2 = converter.convert('<div class="m-4">Second</div>')
```

## Configuration Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `base_font_size` | int | 16 | Base font size in pixels for rem/em conversion |
| `include_mso_properties` | bool | True | Include Microsoft Office properties for Outlook |
| `include_vml_fallbacks` | bool | True | Generate VML fallbacks for border-radius in Outlook |
| `preserve_classes` | bool | False | Keep original Tailwind classes in output |
| `preserve_unsupported_classes` | bool | True | Keep non-Tailwind classes (e.g., custom classes) |
| `compatibility` | str | "strict" | Compatibility mode: "strict" or "modern" |

### Example with Options

```python
from tailwind_email import convert

# Disable MSO properties for non-Outlook targeting
html = '<div class="text-lg leading-relaxed">Content</div>'
output = convert(html, {
    "include_mso_properties": False,
    "base_font_size": 18,
})
```

## Supported Tailwind Classes

### Fully Supported (95%+ Email Client Compatibility)

#### Spacing
| Class Pattern | CSS Property | Example |
|---------------|--------------|---------|
| `p-{size}` | `padding` | `p-4` → `padding: 16px` |
| `px-{size}` | `padding-left`, `padding-right` | `px-4` → 16px horizontal |
| `py-{size}` | `padding-top`, `padding-bottom` | `py-4` → 16px vertical |
| `pt-{size}`, `pr-{size}`, `pb-{size}`, `pl-{size}` | Individual padding | `pt-2` → `padding-top: 8px` |
| `m-{size}` | `margin` | `m-4` → `margin: 16px` |
| `mx-{size}`, `my-{size}` | Horizontal/vertical margin | `mx-auto` → auto centering |
| `mt-{size}`, `mr-{size}`, `mb-{size}`, `ml-{size}` | Individual margin | `mt-2` → `margin-top: 8px` |

#### Sizing
| Class Pattern | CSS Property | Example |
|---------------|--------------|---------|
| `w-{size}` | `width` | `w-64` → `width: 256px` |
| `w-{fraction}` | `width` (percentage) | `w-1/2` → `width: 50%` |
| `w-full` | `width: 100%` | Full width |
| `h-{size}` | `height` | `h-32` → `height: 128px` |
| `max-w-{size}` | `max-width` | `max-w-lg` → `max-width: 512px` |
| `min-w-{size}` | `min-width` | `min-w-0` → `min-width: 0px` |
| `size-{size}` | `width` + `height` | `size-16` → 64px both |

#### Colors
| Class Pattern | CSS Property | Example |
|---------------|--------------|---------|
| `bg-{color}-{shade}` | `background-color` | `bg-blue-500` → `#3b82f6` |
| `text-{color}-{shade}` | `color` | `text-gray-600` → `#4b5563` |
| `border-{color}-{shade}` | `border-color` | `border-red-500` → `#ef4444` |
| `bg-white`, `bg-black` | Special colors | `#ffffff`, `#000000` |
| `bg-transparent` | `transparent` | Transparent background |
| `text-current` | `currentColor` | Inherit color |

##### Color Opacity
```python
# Color with opacity modifier
'<div class="bg-blue-500/50">...</div>'
# → background-color: rgba(59, 130, 246, 0.5)
```

#### Typography
| Class Pattern | CSS Property | Example |
|---------------|--------------|---------|
| `text-xs` to `text-9xl` | `font-size`, `line-height` | `text-lg` → 18px/28px |
| `font-thin` to `font-black` | `font-weight` | `font-bold` → 700 |
| `text-left`, `text-center`, `text-right` | `text-align` | Alignment |
| `leading-{value}` | `line-height` | `leading-relaxed` → 1.625 |
| `tracking-{value}` | `letter-spacing` | `tracking-wide` → 0.4px |
| `underline`, `line-through` | `text-decoration` | Text decoration |
| `uppercase`, `lowercase`, `capitalize` | `text-transform` | Text case |
| `italic`, `not-italic` | `font-style` | Italics |
| `font-sans`, `font-serif`, `font-mono` | `font-family` | Font stack |

#### Borders
| Class Pattern | CSS Property | Example |
|---------------|--------------|---------|
| `border`, `border-{width}` | `border-width` | `border-2` → 2px |
| `border-{side}`, `border-{side}-{width}` | Side borders | `border-t-2` → top 2px |
| `border-solid`, `border-dashed`, `border-dotted` | `border-style` | Style |
| `rounded-{size}` | `border-radius` | `rounded-lg` → 8px |
| `rounded-{corner}-{size}` | Corner radius | `rounded-tl-lg` → top-left 8px |

### Supported with Limitations (60-80% Compatibility)

| Category | Classes | Notes |
|----------|---------|-------|
| **Border Radius** | `rounded-*` | VML fallback for Outlook |
| **Box Shadow** | `shadow-*` | Not supported in Outlook desktop |
| **Opacity** | `opacity-*` | Limited support in some clients |
| **Overflow** | `overflow-*` | May not work in all clients |

### Not Supported (Filtered Out)

These classes are automatically removed as they have poor email client support:

| Category | Classes | Reason |
|----------|---------|--------|
| **Flexbox** | `flex`, `flex-row`, `flex-col`, `justify-*`, `items-*`, `gap-*` | ~60% support |
| **Grid** | `grid`, `grid-cols-*`, `col-span-*`, `gap-*` | ~55% support |
| **Transform** | `rotate-*`, `scale-*`, `translate-*`, `skew-*` | ~46% support |
| **Negative Margin** | `-m-*`, `-mt-*`, `-mx-*`, etc. | Not supported |
| **Animations** | `animate-*`, `transition-*`, `duration-*` | Not supported |
| **Responsive** | `sm:*`, `md:*`, `lg:*`, `xl:*` | No media query support |
| **Dark Mode** | `dark:*` | No color scheme support |
| **Hover/Focus** | `hover:*`, `focus:*`, `active:*` | No pseudo-class support |

## Email Client Compatibility

Based on [Can I Email](https://www.caniemail.com/) data:

| Client | Compatibility | Notes |
|--------|---------------|-------|
| **Apple Mail (macOS/iOS)** | Excellent | Full CSS support |
| **Gmail (Web)** | Good | Some limitations on embedded styles |
| **Gmail (App)** | Good | Similar to web |
| **Outlook 365 (Web)** | Good | Modern CSS support |
| **Outlook (Desktop)** | Moderate | MSO properties and VML needed |
| **Outlook (Mobile)** | Good | Better than desktop |
| **Yahoo Mail** | Good | Generally good support |
| **Thunderbird** | Excellent | Full CSS support |
| **Samsung Email** | Good | Generally good support |

## Advanced Usage

### Arbitrary Values

Use Tailwind's arbitrary value syntax for custom values:

```python
# Arbitrary pixel values
'<div class="w-[200px] h-[100px]">...</div>'
# → width: 200px; height: 100px

# Arbitrary rem values (converted to px)
'<div class="p-[2rem]">...</div>'
# → padding: 32px (at 16px base)

# Arbitrary properties
'<div class="[line-height:1.8]">...</div>'
# → line-height: 1.8
```

### Preserving Custom Classes

If you have custom CSS classes you want to keep:

```python
html = '<div class="my-custom-class p-4 bg-blue-500">Content</div>'

# Default: preserves non-Tailwind classes
output = convert(html)
# → class="my-custom-class" style="padding: 16px; background-color: #3b82f6;"

# Remove all classes
output = convert(html, {"preserve_unsupported_classes": False})
# → style="padding: 16px; background-color: #3b82f6;"
```

### Handling Existing Inline Styles

Existing inline styles are preserved and merged with converted styles:

```python
html = '<div class="p-4" style="color: red;">Content</div>'
output = convert(html)
# → style="color: red; padding: 16px;"
```

### Email Template Patterns

#### Centered Container

```html
<table class="w-full">
    <tr>
        <td>
            <table class="max-w-xl mx-auto bg-white">
                <tr>
                    <td class="p-8">
                        <!-- Content -->
                    </td>
                </tr>
            </table>
        </td>
    </tr>
</table>
```

#### Email-Safe Button

```html
<table>
    <tr>
        <td class="bg-blue-600 rounded-lg">
            <a href="#" class="block py-3 px-6 text-white font-bold text-center">
                Click Here
            </a>
        </td>
    </tr>
</table>
```

#### Two-Column Layout

```html
<table class="w-full">
    <tr>
        <td class="w-1/2 p-4 align-top">
            <!-- Column 1 -->
        </td>
        <td class="w-1/2 p-4 align-top">
            <!-- Column 2 -->
        </td>
    </tr>
</table>
```

## API Reference

### `convert(html: str, options: dict = None) -> str`

Converts HTML with Tailwind classes to email-compatible HTML.

**Parameters:**
- `html` (str): Input HTML string with Tailwind CSS classes
- `options` (dict, optional): Configuration options

**Returns:**
- `str`: Converted HTML with inline styles

### `TailwindEmailConverter`

Class for creating reusable converter instances.

**Methods:**
- `__init__(options: ConversionOptions = None)`: Create converter with options
- `convert(html: str) -> str`: Convert HTML string

### `ConversionOptions`

Dataclass for configuration options.

**Attributes:**
- `base_font_size: int = 16`
- `include_mso_properties: bool = True`
- `include_vml_fallbacks: bool = True`
- `preserve_classes: bool = False`
- `preserve_unsupported_classes: bool = True`
- `compatibility: str = "strict"`

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/tailwind-email/tailwind-email.git
cd tailwind-email

# Install with development dependencies
pip install -e ".[dev]"

# Or use requirements files
pip install -r requirements-dev.txt
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=tailwind_email --cov-report=html

# Run specific test file
pytest tests/test_converter.py

# Run tests matching pattern
pytest -k "test_padding"

# Run with verbose output
pytest -v
```

### Code Quality

```bash
# Lint with ruff
ruff check src tests

# Format with ruff
ruff format src tests

# Type check with mypy
mypy src
```

## Comparison with Alternatives

| Feature | tailwind-email | maizzle | mjml |
|---------|---------------|---------|------|
| Language | Python | Node.js | Node.js |
| Tailwind Support | v4 | v3 | Limited |
| Template Syntax | HTML | Blade | MJML |
| Inlining | Built-in | Built-in | Built-in |
| Dependencies | 2 | Many | Many |
| Learning Curve | Low | Medium | Medium |

## Contributing

Contributions are welcome! Please read our contributing guidelines and submit pull requests.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

MIT License - see [LICENSE](LICENSE) for details.

## Acknowledgments

- [Tailwind CSS](https://tailwindcss.com/) for the utility-first CSS framework
- [Can I Email](https://www.caniemail.com/) for email client compatibility data
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for HTML parsing
