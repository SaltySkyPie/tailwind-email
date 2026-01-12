"""Tests for the main converter module."""

from tailwind_email import TailwindEmailConverter, convert
from tailwind_email.converter import ConversionOptions


class TestConvertFunction:
    """Tests for the convert() function."""

    def test_basic_padding(self) -> None:
        """Test basic padding conversion."""
        html = '<div class="p-4">Content</div>'
        result = convert(html)
        assert "padding: 16px" in result

    def test_padding_variants(self) -> None:
        """Test various padding variants."""
        html = '<div class="px-4 py-2">Content</div>'
        result = convert(html)
        # px-4 = 16px horizontal, py-2 = 8px vertical
        assert "padding-left: 16px" in result
        assert "padding-right: 16px" in result
        assert "padding-top: 8px" in result
        assert "padding-bottom: 8px" in result

    def test_individual_padding(self) -> None:
        """Test individual padding sides."""
        html = '<div class="pt-2 pr-4 pb-6 pl-8">Content</div>'
        result = convert(html)
        assert "padding-top: 8px" in result
        assert "padding-right: 16px" in result
        assert "padding-bottom: 24px" in result
        assert "padding-left: 32px" in result

    def test_margin(self) -> None:
        """Test margin conversion."""
        html = '<div class="m-4">Content</div>'
        result = convert(html)
        assert "margin: 16px" in result

    def test_margin_auto(self) -> None:
        """Test margin auto."""
        html = '<div class="mx-auto">Content</div>'
        result = convert(html)
        assert "margin-left: auto" in result
        assert "margin-right: auto" in result

    def test_background_color(self) -> None:
        """Test background color conversion."""
        html = '<div class="bg-blue-500">Content</div>'
        result = convert(html)
        assert "background-color: #3b82f6" in result

    def test_text_color(self) -> None:
        """Test text color conversion."""
        html = '<div class="text-white">Content</div>'
        result = convert(html)
        assert "color: #ffffff" in result

    def test_font_size(self) -> None:
        """Test font size conversion."""
        html = '<div class="text-lg">Content</div>'
        result = convert(html)
        assert "font-size: 18px" in result
        assert "line-height: 28px" in result

    def test_font_weight(self) -> None:
        """Test font weight conversion."""
        html = '<div class="font-bold">Content</div>'
        result = convert(html)
        assert "font-weight: 700" in result

    def test_text_align(self) -> None:
        """Test text alignment conversion."""
        html = '<div class="text-center">Content</div>'
        result = convert(html)
        assert "text-align: center" in result

    def test_border_radius(self) -> None:
        """Test border radius conversion."""
        html = '<div class="rounded-lg">Content</div>'
        result = convert(html)
        assert "border-radius: 8px" in result

    def test_width(self) -> None:
        """Test width conversion."""
        html = '<div class="w-64">Content</div>'
        result = convert(html)
        assert "width: 256px" in result

    def test_width_percentage(self) -> None:
        """Test percentage width conversion."""
        html = '<div class="w-1/2">Content</div>'
        result = convert(html)
        assert "width: 50%" in result

    def test_max_width(self) -> None:
        """Test max-width conversion."""
        html = '<div class="max-w-lg">Content</div>'
        result = convert(html)
        assert "max-width: 512px" in result

    def test_height(self) -> None:
        """Test height conversion."""
        html = '<div class="h-32">Content</div>'
        result = convert(html)
        assert "height: 128px" in result

    def test_combined_classes(self) -> None:
        """Test combining multiple classes."""
        html = '<div class="p-4 bg-blue-500 text-white rounded-lg">Content</div>'
        result = convert(html)
        assert "padding: 16px" in result
        assert "background-color: #3b82f6" in result
        assert "color: #ffffff" in result
        assert "border-radius: 8px" in result

    def test_border_width(self) -> None:
        """Test border width conversion."""
        html = '<div class="border-2">Content</div>'
        result = convert(html)
        assert "border-width: 2px" in result
        assert "border-style: solid" in result

    def test_border_color(self) -> None:
        """Test border color conversion."""
        html = '<div class="border border-gray-300">Content</div>'
        result = convert(html)
        assert "border-color: #d1d5db" in result

    def test_opacity(self) -> None:
        """Test opacity conversion."""
        html = '<div class="opacity-50">Content</div>'
        result = convert(html)
        assert "opacity: 0.5" in result

    def test_box_shadow(self) -> None:
        """Test box shadow conversion."""
        html = '<div class="shadow-lg">Content</div>'
        result = convert(html)
        assert "box-shadow:" in result

    def test_display_block(self) -> None:
        """Test display block conversion."""
        html = '<span class="block">Content</span>'
        result = convert(html)
        assert "display: block" in result

    def test_display_hidden(self) -> None:
        """Test display none conversion."""
        html = '<div class="hidden">Content</div>'
        result = convert(html)
        assert "display: none" in result

    def test_flex_classes_removed(self) -> None:
        """Test that flex classes are not converted (unsupported in email)."""
        html = '<div class="flex justify-center items-center">Content</div>'
        result = convert(html)
        # Flex properties should not appear in output
        assert "display: flex" not in result
        assert "justify-content" not in result
        assert "align-items" not in result

    def test_responsive_classes_removed(self) -> None:
        """Test that responsive prefixes are stripped."""
        html = '<div class="p-4 md:p-8">Content</div>'
        result = convert(html)
        # Only the non-prefixed p-4 should be converted
        assert "padding: 16px" in result
        # md:p-8 should not appear as 32px
        assert "padding: 32px" not in result

    def test_hover_classes_removed(self) -> None:
        """Test that hover states are stripped."""
        html = '<div class="bg-blue-500 hover:bg-blue-600">Content</div>'
        result = convert(html)
        # Only bg-blue-500 should be converted
        assert "#3b82f6" in result
        # hover:bg-blue-600 should not add the 600 shade
        assert "#2563eb" not in result

    def test_preserve_existing_styles(self) -> None:
        """Test that existing inline styles are preserved."""
        html = '<div class="p-4" style="color: red;">Content</div>'
        result = convert(html)
        assert "color: red" in result
        assert "padding: 16px" in result

    def test_preserve_non_tailwind_classes(self) -> None:
        """Test that non-Tailwind classes are preserved by default."""
        html = '<div class="my-custom-class p-4">Content</div>'
        result = convert(html)
        assert "my-custom-class" in result

    def test_remove_all_classes_option(self) -> None:
        """Test removing all classes when option is set."""
        html = '<div class="my-custom-class p-4">Content</div>'
        result = convert(html, {"preserve_unsupported_classes": False})
        assert "my-custom-class" not in result
        assert 'class="' not in result

    def test_nested_elements(self) -> None:
        """Test conversion of nested elements."""
        html = """
        <div class="p-4 bg-gray-100">
            <h1 class="text-2xl font-bold">Title</h1>
            <p class="mt-2 text-gray-600">Description</p>
        </div>
        """
        result = convert(html)
        assert "padding: 16px" in result
        assert "background-color: #f3f4f6" in result
        assert "font-size: 24px" in result
        assert "font-weight: 700" in result
        assert "margin-top: 8px" in result
        assert "color: #4b5563" in result

    def test_arbitrary_values(self) -> None:
        """Test arbitrary value syntax."""
        html = '<div class="w-[200px]">Content</div>'
        result = convert(html)
        assert "width: 200px" in result

    def test_arbitrary_rem_values(self) -> None:
        """Test arbitrary rem values are converted to px."""
        html = '<div class="p-[2rem]">Content</div>'
        result = convert(html)
        assert "padding: 32px" in result

    def test_empty_html(self) -> None:
        """Test empty HTML input."""
        result = convert("")
        assert result == ""

    def test_no_classes(self) -> None:
        """Test HTML without any classes."""
        html = "<div>Content</div>"
        result = convert(html)
        assert "<div>Content</div>" in result

    def test_letter_spacing(self) -> None:
        """Test letter spacing conversion."""
        html = '<div class="tracking-wide">Content</div>'
        result = convert(html)
        assert "letter-spacing: 0.4px" in result

    def test_line_height(self) -> None:
        """Test line height conversion."""
        html = '<div class="leading-relaxed">Content</div>'
        result = convert(html)
        assert "line-height: 1.625" in result

    def test_text_decoration(self) -> None:
        """Test text decoration conversion."""
        html = '<a class="underline">Link</a>'
        result = convert(html)
        assert "text-decoration: underline" in result

    def test_text_transform(self) -> None:
        """Test text transform conversion."""
        html = '<div class="uppercase">Content</div>'
        result = convert(html)
        assert "text-transform: uppercase" in result

    def test_size_utility(self) -> None:
        """Test size utility (width + height)."""
        html = '<div class="size-16">Content</div>'
        result = convert(html)
        assert "width: 64px" in result
        assert "height: 64px" in result

    def test_special_colors(self) -> None:
        """Test special color keywords."""
        html = '<div class="bg-transparent text-current">Content</div>'
        result = convert(html)
        assert "background-color: transparent" in result
        assert "color: currentColor" in result


class TestConversionOptions:
    """Tests for ConversionOptions."""

    def test_custom_base_font_size(self) -> None:
        """Test custom base font size for rem conversion."""
        html = '<div class="p-[1rem]">Content</div>'
        result = convert(html, {"base_font_size": 20})
        assert "padding: 20px" in result

    def test_mso_properties_included(self) -> None:
        """Test MSO properties are included by default."""
        html = '<div class="text-lg">Content</div>'
        result = convert(html)
        assert "mso-line-height-rule: exactly" in result

    def test_mso_properties_disabled(self) -> None:
        """Test MSO properties can be disabled."""
        html = '<div class="text-lg">Content</div>'
        result = convert(html, {"include_mso_properties": False})
        assert "mso-line-height-rule" not in result

    def test_preserve_all_classes(self) -> None:
        """Test preserving all original classes."""
        html = '<div class="p-4 bg-blue-500">Content</div>'
        result = convert(html, {"preserve_classes": True})
        assert "p-4" in result
        assert "bg-blue-500" in result


class TestTailwindEmailConverter:
    """Tests for TailwindEmailConverter class."""

    def test_instance_creation(self) -> None:
        """Test creating converter instance."""
        converter = TailwindEmailConverter()
        assert converter is not None

    def test_instance_with_options(self) -> None:
        """Test creating converter with custom options."""
        options = ConversionOptions(
            base_font_size=20,
            include_vml_fallbacks=False,
        )
        converter = TailwindEmailConverter(options)
        assert converter.options.base_font_size == 20
        assert converter.options.include_vml_fallbacks is False

    def test_reusable_converter(self) -> None:
        """Test converter can be reused for multiple conversions."""
        converter = TailwindEmailConverter()

        html1 = '<div class="p-4">First</div>'
        html2 = '<div class="m-4">Second</div>'

        result1 = converter.convert(html1)
        result2 = converter.convert(html2)

        assert "padding: 16px" in result1
        assert "margin: 16px" in result2


class TestEdgeCases:
    """Tests for edge cases and special scenarios."""

    def test_malformed_html(self) -> None:
        """Test handling of malformed HTML."""
        html = '<div class="p-4">Unclosed div'
        result = convert(html)
        # Should still process the class
        assert "padding: 16px" in result

    def test_multiple_same_properties(self) -> None:
        """Test when multiple classes set the same property."""
        html = '<div class="p-4 p-8">Content</div>'
        result = convert(html)
        # Last value should win
        assert "padding: 32px" in result

    def test_whitespace_handling(self) -> None:
        """Test handling of extra whitespace in class attribute."""
        html = '<div class="  p-4   bg-blue-500  ">Content</div>'
        result = convert(html)
        assert "padding: 16px" in result
        assert "background-color: #3b82f6" in result

    def test_table_elements(self) -> None:
        """Test conversion works on table elements."""
        html = """
        <table class="w-full">
            <tr class="bg-gray-100">
                <td class="p-4 text-center">Cell</td>
            </tr>
        </table>
        """
        result = convert(html)
        assert "width: 100%" in result
        assert "background-color: #f3f4f6" in result
        assert "padding: 16px" in result
        assert "text-align: center" in result

    def test_image_elements(self) -> None:
        """Test conversion works on image elements."""
        html = '<img class="w-full h-auto rounded-lg" src="image.jpg" alt="Test">'
        result = convert(html)
        assert "width: 100%" in result
        assert "height: auto" in result
        assert "border-radius: 8px" in result

    def test_link_elements(self) -> None:
        """Test conversion works on link elements."""
        html = '<a class="text-blue-500 underline" href="#">Link</a>'
        result = convert(html)
        assert "color: #3b82f6" in result
        assert "text-decoration: underline" in result

    def test_button_styling(self) -> None:
        """Test typical button styling conversion."""
        html = '<a class="bg-blue-500 text-white py-2 px-4 rounded-lg font-bold">Button</a>'
        result = convert(html)
        assert "background-color: #3b82f6" in result
        assert "color: #ffffff" in result
        assert "border-radius: 8px" in result
        assert "font-weight: 700" in result

    def test_color_with_opacity(self) -> None:
        """Test color with opacity modifier."""
        html = '<div class="bg-blue-500/50">Content</div>'
        result = convert(html)
        # Should contain rgba with 0.5 opacity
        assert "rgba(59, 130, 246, 0.5)" in result

    def test_vertical_align(self) -> None:
        """Test vertical alignment conversion."""
        html = '<td class="align-middle">Content</td>'
        result = convert(html)
        assert "vertical-align: middle" in result

    def test_white_space(self) -> None:
        """Test white-space conversion."""
        html = '<div class="whitespace-nowrap">Content</div>'
        result = convert(html)
        assert "white-space: nowrap" in result

    def test_overflow(self) -> None:
        """Test overflow conversion."""
        html = '<div class="overflow-hidden">Content</div>'
        result = convert(html)
        assert "overflow: hidden" in result

    def test_truncate_utility(self) -> None:
        """Test truncate utility expands to multiple properties."""
        html = '<div class="truncate">Content</div>'
        result = convert(html)
        assert "overflow: hidden" in result
        assert "text-overflow: ellipsis" in result
        assert "white-space: nowrap" in result
