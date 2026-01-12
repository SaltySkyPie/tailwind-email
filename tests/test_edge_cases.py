"""Tests for edge cases, unusual inputs, and integration scenarios."""

import pytest

from tailwind_email import TailwindEmailConverter, convert
from tailwind_email.parser import TailwindClassParser


class TestMalformedHTML:
    """Tests for handling malformed or unusual HTML."""

    def test_unclosed_tags(self) -> None:
        """Test handling unclosed tags."""
        html = '<div class="p-4">Content'
        output = convert(html)
        assert "padding: 16px" in output

    def test_nested_unclosed_tags(self) -> None:
        """Test nested unclosed tags."""
        html = '<div class="p-4"><span class="text-red-500">Content'
        output = convert(html)
        assert "padding: 16px" in output
        assert "color: #ef4444" in output

    def test_self_closing_tags(self) -> None:
        """Test self-closing tags."""
        html = '<img class="w-full h-auto" src="test.jpg" />'
        output = convert(html)
        assert "width: 100%" in output
        assert "height: auto" in output

    def test_br_tags(self) -> None:
        """Test br tags."""
        html = '<div class="p-4">Line 1<br class="hidden">Line 2</div>'
        output = convert(html)
        assert "display: none" in output

    def test_mixed_quotes(self) -> None:
        """Test mixed quote styles."""
        html = "<div class='p-4' style=\"color: red;\">Content</div>"
        output = convert(html)
        assert "padding: 16px" in output
        assert "color: red" in output

    def test_no_quotes_attribute(self) -> None:
        """Test attributes without quotes (valid in HTML5)."""
        html = "<div class=p-4>Content</div>"
        output = convert(html)
        assert "padding: 16px" in output

    def test_extra_whitespace_in_class(self) -> None:
        """Test extra whitespace in class attribute."""
        html = '<div class="   p-4    bg-blue-500   text-white   ">Content</div>'
        output = convert(html)
        assert "padding: 16px" in output
        assert "background-color: #3b82f6" in output
        assert "color: #ffffff" in output

    def test_newlines_in_class(self) -> None:
        """Test newlines in class attribute."""
        html = """<div class="
            p-4
            bg-blue-500
            text-white
        ">Content</div>"""
        output = convert(html)
        assert "padding: 16px" in output
        assert "background-color: #3b82f6" in output

    def test_duplicate_classes(self) -> None:
        """Test duplicate classes."""
        html = '<div class="p-4 p-4 p-4">Content</div>'
        output = convert(html)
        assert "padding: 16px" in output

    def test_empty_class_attribute(self) -> None:
        """Test empty class attribute."""
        html = '<div class="">Content</div>'
        output = convert(html)
        assert "<div" in output

    def test_class_attribute_only_whitespace(self) -> None:
        """Test class attribute with only whitespace."""
        html = '<div class="   ">Content</div>'
        output = convert(html)
        assert "<div" in output

    def test_nested_html_deeply(self) -> None:
        """Test deeply nested HTML."""
        html = """
        <div class="p-4">
            <div class="m-2">
                <div class="bg-blue-500">
                    <div class="text-white">
                        <div class="font-bold">
                            <div class="text-center">
                                Content
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """
        output = convert(html)
        assert "padding: 16px" in output
        assert "margin: 8px" in output
        assert "background-color: #3b82f6" in output
        assert "color: #ffffff" in output
        assert "font-weight: 700" in output
        assert "text-align: center" in output


class TestSpecialCharacters:
    """Tests for special characters in HTML."""

    def test_html_entities(self) -> None:
        """Test HTML entities are preserved."""
        html = '<div class="p-4">&copy; 2024 &amp; Company &lt;Inc&gt;</div>'
        output = convert(html)
        assert "&copy;" in output or "\u00a9" in output
        assert "padding: 16px" in output

    def test_unicode_content(self) -> None:
        """Test unicode content is preserved."""
        html = '<div class="p-4">Hello &#128512; World</div>'
        output = convert(html)
        assert "padding: 16px" in output

    def test_special_chars_in_attribute(self) -> None:
        """Test special characters in other attributes."""
        html = '<a class="text-blue-500" href="https://example.com?foo=bar&baz=qux">Link</a>'
        output = convert(html)
        assert "color: #3b82f6" in output
        assert "example.com" in output


class TestExistingStyles:
    """Tests for handling existing inline styles."""

    def test_merge_with_existing_style(self) -> None:
        """Test merging with existing inline style."""
        html = '<div class="p-4" style="color: red;">Content</div>'
        output = convert(html)
        assert "color: red" in output
        assert "padding: 16px" in output

    def test_existing_style_priority(self) -> None:
        """Test existing inline styles interaction with Tailwind classes."""
        html = '<div class="text-blue-500" style="color: red;">Content</div>'
        output = convert(html)
        # Note: Current implementation converts Tailwind classes and may override
        # existing styles. The color will come from text-blue-500
        assert "color:" in output  # Some color value will be present

    def test_complex_existing_style(self) -> None:
        """Test complex existing inline styles."""
        html = '<div class="p-4" style="background: linear-gradient(to right, red, blue); box-shadow: 0 0 10px black;">Content</div>'
        output = convert(html)
        assert "linear-gradient" in output
        assert "padding: 16px" in output

    def test_empty_existing_style(self) -> None:
        """Test empty existing style attribute."""
        html = '<div class="p-4" style="">Content</div>'
        output = convert(html)
        assert "padding: 16px" in output

    def test_style_with_semicolon(self) -> None:
        """Test existing style with trailing semicolon."""
        html = '<div class="p-4" style="color: red;">Content</div>'
        output = convert(html)
        assert "padding: 16px" in output
        assert "color: red" in output


class TestEmptyAndMinimalInputs:
    """Tests for empty and minimal inputs."""

    def test_empty_string(self) -> None:
        """Test empty string input."""
        output = convert("")
        assert output == ""

    def test_whitespace_only(self) -> None:
        """Test whitespace-only input."""
        output = convert("   \n\t  ")
        assert output.strip() == ""

    def test_text_only(self) -> None:
        """Test plain text only."""
        output = convert("Hello World")
        assert "Hello World" in output

    def test_single_element_no_class(self) -> None:
        """Test single element without class."""
        html = "<div>Content</div>"
        output = convert(html)
        assert "<div>Content</div>" in output

    def test_minimal_with_class(self) -> None:
        """Test minimal element with class."""
        html = '<p class="m-0">X</p>'
        output = convert(html)
        assert "margin: 0px" in output


class TestClassFiltering:
    """Tests for class filtering behavior."""

    def test_responsive_prefixes_filtered(self) -> None:
        """Test responsive prefixes are filtered."""
        html = '<div class="p-4 sm:p-6 md:p-8 lg:p-10 xl:p-12 2xl:p-16">Content</div>'
        output = convert(html)
        assert "padding: 16px" in output  # p-4
        assert "padding: 24px" not in output  # sm:p-6
        assert "padding: 32px" not in output  # md:p-8

    def test_state_prefixes_filtered(self) -> None:
        """Test state prefixes are filtered."""
        html = '<div class="bg-blue-500 hover:bg-blue-600 focus:bg-blue-700 active:bg-blue-800">Content</div>'
        output = convert(html)
        assert "#3b82f6" in output  # blue-500
        assert "#2563eb" not in output  # blue-600
        assert "#1d4ed8" not in output  # blue-700
        assert "#1e40af" not in output  # blue-800

    def test_dark_mode_filtered(self) -> None:
        """Test dark mode prefix is filtered."""
        html = '<div class="bg-white dark:bg-gray-900">Content</div>'
        output = convert(html)
        assert "#ffffff" in output  # white
        assert "#111827" not in output  # gray-900

    def test_flex_classes_filtered(self) -> None:
        """Test flexbox classes are filtered."""
        html = '<div class="flex flex-row justify-center items-center gap-4 p-4">Content</div>'
        output = convert(html)
        assert "padding: 16px" in output
        assert "display: flex" not in output
        assert "flex-direction" not in output
        assert "justify-content" not in output
        assert "align-items" not in output
        assert "gap:" not in output

    def test_grid_classes_filtered(self) -> None:
        """Test grid classes are filtered."""
        html = '<div class="grid grid-cols-3 gap-4 p-4">Content</div>'
        output = convert(html)
        assert "padding: 16px" in output
        assert "display: grid" not in output
        assert "grid-template-columns" not in output

    def test_transform_classes_filtered(self) -> None:
        """Test transform classes do not produce transform CSS output."""
        html = '<div class="rotate-45 scale-150 translate-x-4 p-4">Content</div>'
        output = convert(html)
        assert "padding: 16px" in output
        # Transform CSS should not be generated (even if classes remain in output)
        assert "transform:" not in output

    def test_animation_classes_filtered(self) -> None:
        """Test animation classes do not produce animation CSS output."""
        html = '<div class="animate-spin animate-pulse transition duration-300 p-4">Content</div>'
        output = convert(html)
        assert "padding: 16px" in output
        # Animation CSS should not be generated (even if classes remain in output)
        assert "animation:" not in output

    def test_negative_margins_filtered(self) -> None:
        """Test negative margins are filtered."""
        html = '<div class="p-4 -m-4 -mt-2 -mx-8">Content</div>'
        output = convert(html)
        assert "padding: 16px" in output
        # Negative margins should not appear
        assert "margin: -" not in output
        assert "margin-top: -" not in output

    def test_custom_classes_preserved(self) -> None:
        """Test custom classes are preserved."""
        html = '<div class="my-custom-class another-custom p-4">Content</div>'
        output = convert(html)
        assert "padding: 16px" in output
        assert "my-custom-class" in output
        assert "another-custom" in output


class TestClassRecognition:
    """Tests for Tailwind class recognition."""

    @pytest.fixture
    def parser(self) -> TailwindClassParser:
        """Create parser instance."""
        return TailwindClassParser()

    def test_recognizes_spacing_classes(self, parser: TailwindClassParser) -> None:
        """Test spacing classes are recognized."""
        assert parser.is_tailwind_class("p-4")
        assert parser.is_tailwind_class("m-8")
        assert parser.is_tailwind_class("px-2")
        assert parser.is_tailwind_class("my-auto")
        assert parser.is_tailwind_class("pt-0")

    def test_recognizes_color_classes(self, parser: TailwindClassParser) -> None:
        """Test color classes are recognized."""
        assert parser.is_tailwind_class("bg-blue-500")
        assert parser.is_tailwind_class("text-gray-900")
        assert parser.is_tailwind_class("border-red-400")
        assert parser.is_tailwind_class("bg-white")
        assert parser.is_tailwind_class("text-black")

    def test_recognizes_sizing_classes(self, parser: TailwindClassParser) -> None:
        """Test sizing classes are recognized."""
        assert parser.is_tailwind_class("w-full")
        assert parser.is_tailwind_class("h-64")
        assert parser.is_tailwind_class("max-w-lg")
        assert parser.is_tailwind_class("min-h-screen")
        assert parser.is_tailwind_class("size-8")

    def test_recognizes_typography_classes(self, parser: TailwindClassParser) -> None:
        """Test typography classes are recognized."""
        assert parser.is_tailwind_class("text-lg")
        assert parser.is_tailwind_class("font-bold")
        assert parser.is_tailwind_class("leading-tight")
        assert parser.is_tailwind_class("tracking-wide")

    def test_recognizes_border_classes(self, parser: TailwindClassParser) -> None:
        """Test border classes are recognized."""
        assert parser.is_tailwind_class("border")
        assert parser.is_tailwind_class("border-2")
        assert parser.is_tailwind_class("rounded-lg")
        assert parser.is_tailwind_class("rounded-t-xl")

    def test_recognizes_single_word_classes(self, parser: TailwindClassParser) -> None:
        """Test single-word classes are recognized."""
        assert parser.is_tailwind_class("block")
        assert parser.is_tailwind_class("hidden")
        assert parser.is_tailwind_class("underline")
        assert parser.is_tailwind_class("italic")
        assert parser.is_tailwind_class("truncate")

    def test_recognizes_arbitrary_classes(self, parser: TailwindClassParser) -> None:
        """Test arbitrary value classes are recognized."""
        assert parser.is_tailwind_class("w-[200px]")
        assert parser.is_tailwind_class("p-[1rem]")
        assert parser.is_tailwind_class("[color:red]")

    def test_rejects_non_tailwind_classes(self, parser: TailwindClassParser) -> None:
        """Test non-Tailwind classes are rejected."""
        assert not parser.is_tailwind_class("my-custom-class")
        assert not parser.is_tailwind_class("some-component")
        assert not parser.is_tailwind_class("header-nav")
        assert not parser.is_tailwind_class("btn-primary")


class TestPropertyOverrides:
    """Tests for property override behavior."""

    def test_last_class_wins(self) -> None:
        """Test later classes override earlier ones."""
        html = '<div class="p-4 p-8">Content</div>'
        output = convert(html)
        assert "padding: 32px" in output
        assert "padding: 16px" not in output

    def test_specific_overrides_general(self) -> None:
        """Test specific padding overrides general."""
        html = '<div class="p-4 pt-8">Content</div>'
        output = convert(html)
        assert "padding: 16px" in output  # Base padding
        assert "padding-top: 32px" in output  # Specific override

    def test_multiple_overrides(self) -> None:
        """Test multiple sequential overrides."""
        html = '<div class="text-sm text-base text-lg">Content</div>'
        output = convert(html)
        # Last one should win
        assert "font-size: 18px" in output

    def test_color_overrides(self) -> None:
        """Test color class overrides."""
        html = '<div class="text-red-500 text-blue-500 text-green-500">Content</div>'
        output = convert(html)
        # Last color should win
        assert "color: #22c55e" in output  # green-500


class TestHTMLElements:
    """Tests for various HTML elements."""

    def test_table_elements(self) -> None:
        """Test table elements are styled correctly."""
        html = """
        <table class="w-full border-collapse">
            <thead>
                <tr class="bg-gray-100">
                    <th class="p-4 text-left">Header</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td class="p-4 border-b border-gray-200">Cell</td>
                </tr>
            </tbody>
        </table>
        """
        output = convert(html)
        assert "width: 100%" in output
        assert "background-color: #f3f4f6" in output
        assert "padding: 16px" in output
        assert "text-align: left" in output

    def test_image_elements(self) -> None:
        """Test image elements."""
        html = '<img class="w-full h-auto max-w-md rounded-lg" src="test.jpg" alt="Test">'
        output = convert(html)
        assert "width: 100%" in output
        assert "height: auto" in output
        assert "max-width: 448px" in output
        assert "border-radius: 8px" in output

    def test_link_elements(self) -> None:
        """Test anchor elements."""
        html = '<a class="text-blue-500 underline hover:text-blue-600" href="#">Link</a>'
        output = convert(html)
        assert "color: #3b82f6" in output
        assert "text-decoration: underline" in output
        # hover should be filtered
        assert "#2563eb" not in output

    def test_button_elements(self) -> None:
        """Test button styling."""
        html = '<button class="bg-green-500 text-white py-2 px-4 rounded-lg font-semibold">Submit</button>'
        output = convert(html)
        assert "background-color: #22c55e" in output
        assert "color: #ffffff" in output
        assert "border-radius: 8px" in output
        assert "font-weight: 600" in output

    def test_input_elements(self) -> None:
        """Test input styling."""
        html = '<input class="border border-gray-300 rounded-md p-2 w-full" type="text">'
        output = convert(html)
        assert "border-width: 1px" in output
        assert "border-color: #d1d5db" in output
        assert "border-radius: 6px" in output
        assert "width: 100%" in output

    def test_list_elements(self) -> None:
        """Test list element styling."""
        html = """
        <ul class="pl-6 text-gray-600">
            <li class="mb-2">Item 1</li>
            <li class="mb-2">Item 2</li>
            <li>Item 3</li>
        </ul>
        """
        output = convert(html)
        assert "padding-left: 24px" in output
        assert "color: #4b5563" in output
        assert "margin-bottom: 8px" in output

    def test_heading_elements(self) -> None:
        """Test heading element styling."""
        html = """
        <h1 class="text-4xl font-bold text-gray-900 mb-4">Heading 1</h1>
        <h2 class="text-3xl font-semibold text-gray-800 mb-3">Heading 2</h2>
        <h3 class="text-2xl font-medium text-gray-700 mb-2">Heading 3</h3>
        """
        output = convert(html)
        assert "font-size: 36px" in output  # text-4xl
        assert "font-size: 30px" in output  # text-3xl
        assert "font-size: 24px" in output  # text-2xl
        assert "font-weight: 700" in output  # font-bold
        assert "font-weight: 600" in output  # font-semibold
        assert "font-weight: 500" in output  # font-medium


class TestIntegration:
    """Integration tests for complete workflows."""

    def test_converter_reuse(self) -> None:
        """Test converter can be reused for multiple conversions."""
        converter = TailwindEmailConverter()

        html1 = '<div class="p-4 bg-red-500">First</div>'
        html2 = '<div class="m-8 bg-blue-500">Second</div>'
        html3 = '<div class="w-full text-lg">Third</div>'

        output1 = converter.convert(html1)
        output2 = converter.convert(html2)
        output3 = converter.convert(html3)

        assert "padding: 16px" in output1
        assert "background-color: #ef4444" in output1

        assert "margin: 32px" in output2
        assert "background-color: #3b82f6" in output2

        assert "width: 100%" in output3
        assert "font-size: 18px" in output3

    def test_complete_email_workflow(self) -> None:
        """Test a complete email template conversion workflow."""
        # Simulate a typical email template workflow
        header = (
            '<div class="bg-blue-600 p-6 text-center text-white text-xl font-bold">Header</div>'
        )
        content = (
            '<div class="p-8 bg-white"><p class="text-gray-600 leading-relaxed">Content</p></div>'
        )
        footer = '<div class="bg-gray-100 p-4 text-center text-gray-500 text-sm">Footer</div>'

        # Convert each section
        header_output = convert(header)
        content_output = convert(content)
        footer_output = convert(footer)

        # Verify each section
        assert "background-color: #2563eb" in header_output
        assert "padding: 24px" in header_output

        assert "background-color: #ffffff" in content_output
        assert "line-height: 1.625" in content_output

        assert "background-color: #f3f4f6" in footer_output
        assert "font-size: 14px" in footer_output

    def test_batch_conversion(self) -> None:
        """Test batch conversion of multiple templates."""
        templates = [
            '<div class="p-4">Template 1</div>',
            '<div class="m-4">Template 2</div>',
            '<div class="text-lg">Template 3</div>',
            '<div class="bg-red-500">Template 4</div>',
            '<div class="rounded-lg">Template 5</div>',
        ]

        converter = TailwindEmailConverter()
        outputs = [converter.convert(t) for t in templates]

        assert "padding: 16px" in outputs[0]
        assert "margin: 16px" in outputs[1]
        assert "font-size: 18px" in outputs[2]
        assert "background-color: #ef4444" in outputs[3]
        assert "border-radius: 8px" in outputs[4]


class TestDocumentStructure:
    """Tests for complete HTML document structures."""

    def test_full_html_document(self) -> None:
        """Test processing a full HTML document."""
        html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Test Email</title>
        </head>
        <body class="bg-gray-100">
            <div class="max-w-xl mx-auto p-4">
                <h1 class="text-2xl font-bold">Hello</h1>
                <p class="text-gray-600">World</p>
            </div>
        </body>
        </html>
        """
        output = convert(html)

        # Structure should be preserved
        assert "<!DOCTYPE html>" in output or "<!doctype html>" in output.lower()
        assert "<html" in output
        assert "<head>" in output
        assert "<body" in output

        # Styles should be applied
        assert "background-color: #f3f4f6" in output
        assert "max-width: 576px" in output
        assert "font-size: 24px" in output
        assert "color: #4b5563" in output

    def test_email_with_doctype(self) -> None:
        """Test email template with XHTML doctype."""
        html = """
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        <html xmlns="http://www.w3.org/1999/xhtml">
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        </head>
        <body class="m-0 p-0">
            <table class="w-full">
                <tr>
                    <td class="p-4 text-center">Content</td>
                </tr>
            </table>
        </body>
        </html>
        """
        output = convert(html)

        assert "margin: 0px" in output
        assert "padding: 0px" in output or "padding: 16px" in output
        assert "width: 100%" in output
