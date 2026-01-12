"""
Fallback generators for email client compatibility.

Provides VML (Vector Markup Language) fallbacks for Outlook
and other Microsoft-specific workarounds.
"""

from typing import Optional

from tailwind_email.utils import generate_vml_rounded_rect, generate_vml_rounded_rect_end


class FallbackGenerator:
    """Generates fallback markup for limited email client support."""

    def __init__(self, include_vml: bool = True) -> None:
        """
        Initialize the fallback generator.

        Args:
            include_vml: Whether to generate VML fallbacks for Outlook
        """
        self.include_vml = include_vml

    def generate_rounded_button_vml(
        self,
        width: str,
        height: str,
        radius: str,
        background_color: str,
        text_color: str,
        href: Optional[str] = None,
        border_color: Optional[str] = None,
        border_width: str = "0",
    ) -> tuple[str, str]:
        """
        Generate VML markup for a rounded button in Outlook.

        Args:
            width: Button width in pixels
            height: Button height in pixels
            radius: Border radius in pixels
            background_color: Background color (hex)
            text_color: Text color (hex)
            href: Optional link URL
            border_color: Optional border color (hex)
            border_width: Border width in pixels

        Returns:
            Tuple of (opening VML markup, closing VML markup)
        """
        if not self.include_vml:
            return ("", "")

        opening = generate_vml_rounded_rect(
            width=width,
            height=height,
            radius=radius,
            background_color=background_color,
            border_color=border_color,
            border_width=border_width,
        )

        closing = generate_vml_rounded_rect_end()

        return (opening, closing)

    def generate_mso_padding_table(
        self,
        padding_top: str = "0",
        padding_right: str = "0",
        padding_bottom: str = "0",
        padding_left: str = "0",
        content: str = "",
    ) -> str:
        """
        Generate a table-based padding structure for Outlook.

        Outlook desktop doesn't support padding on divs, only on table cells.
        This generates a table structure to simulate padding.

        Args:
            padding_top: Top padding in pixels
            padding_right: Right padding in pixels
            padding_bottom: Bottom padding in pixels
            padding_left: Left padding in pixels
            content: Inner content HTML

        Returns:
            Table-based HTML structure
        """
        return f"""<!--[if mso]>
<table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
<tr>
<td style="padding-top:{padding_top};padding-right:{padding_right};padding-bottom:{padding_bottom};padding-left:{padding_left};">
<![endif]-->
{content}
<!--[if mso]>
</td>
</tr>
</table>
<![endif]-->"""

    def generate_mso_width_wrapper(
        self,
        width: str,
        content: str = "",
    ) -> str:
        """
        Generate a width-constrained wrapper for Outlook.

        Outlook may not respect max-width on certain elements.
        This generates a table structure to constrain width.

        Args:
            width: Width in pixels
            content: Inner content HTML

        Returns:
            Table-based HTML structure
        """
        # Remove 'px' suffix if present
        width_value = width.replace("px", "")

        return f"""<!--[if mso]>
<table role="presentation" cellspacing="0" cellpadding="0" border="0" width="{width_value}">
<tr>
<td>
<![endif]-->
{content}
<!--[if mso]>
</td>
</tr>
</table>
<![endif]-->"""

    def generate_mso_line_height_fix(self, line_height: str) -> str:
        """
        Generate MSO-specific line-height fix.

        Args:
            line_height: Line height value

        Returns:
            CSS property string
        """
        return f"mso-line-height-rule: exactly; line-height: {line_height};"

    def wrap_with_mso_conditional(
        self,
        mso_content: str,
        non_mso_content: str,
    ) -> str:
        """
        Wrap content with MSO conditional comments.

        Shows different content for Outlook vs other clients.

        Args:
            mso_content: Content to show in Outlook
            non_mso_content: Content to show in other clients

        Returns:
            Conditionally wrapped HTML
        """
        return f"""<!--[if mso]>
{mso_content}
<![endif]-->
<!--[if !mso]><!-->
{non_mso_content}
<!--<![endif]-->"""

    def generate_spacer(
        self,
        height: str,
        width: str = "100%",
    ) -> str:
        """
        Generate an email-safe spacer element.

        Uses a table-based approach for maximum compatibility.

        Args:
            height: Spacer height in pixels
            width: Spacer width (default: 100%)

        Returns:
            Spacer HTML
        """
        height.replace("px", "")

        return f"""<table role="presentation" border="0" cellpadding="0" cellspacing="0" width="{width}" style="width: {width};">
<tr>
<td style="font-size: 1px; line-height: {height}; height: {height};">&nbsp;</td>
</tr>
</table>"""

    def generate_divider(
        self,
        color: str = "#e5e7eb",
        thickness: str = "1px",
        width: str = "100%",
    ) -> str:
        """
        Generate an email-safe horizontal divider.

        Args:
            color: Divider color (hex)
            thickness: Divider thickness in pixels
            width: Divider width

        Returns:
            Divider HTML
        """
        return f"""<table role="presentation" border="0" cellpadding="0" cellspacing="0" width="{width}" style="width: {width};">
<tr>
<td style="font-size: 1px; line-height: {thickness}; height: {thickness}; background-color: {color};">&nbsp;</td>
</tr>
</table>"""


# Pre-configured fallback generator instance
default_fallback_generator = FallbackGenerator(include_vml=True)
