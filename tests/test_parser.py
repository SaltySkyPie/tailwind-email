"""Tests for the HTML parser module."""

import pytest
from bs4 import BeautifulSoup

from tailwind_email.parser import TailwindClassParser


class TestTailwindClassParser:
    """Tests for TailwindClassParser class."""

    @pytest.fixture
    def parser(self) -> TailwindClassParser:
        """Create a parser instance for testing."""
        return TailwindClassParser()

    def test_parse_html(self, parser: TailwindClassParser) -> None:
        """Test parsing HTML into BeautifulSoup."""
        html = "<div>Content</div>"
        soup = parser.parse_html(html)
        assert isinstance(soup, BeautifulSoup)
        assert soup.find("div") is not None

    def test_get_elements_with_classes(self, parser: TailwindClassParser) -> None:
        """Test finding elements with class attributes."""
        html = """
        <div class="test">One</div>
        <span>Two</span>
        <p class="another">Three</p>
        """
        soup = parser.parse_html(html)
        elements = list(parser.get_elements_with_classes(soup))
        assert len(elements) == 2

    def test_extract_classes(self, parser: TailwindClassParser) -> None:
        """Test extracting classes from an element."""
        soup = parser.parse_html('<div class="one two three">Content</div>')
        element = soup.find("div")
        classes = parser.extract_classes(element)
        assert classes == ["one", "two", "three"]

    def test_extract_empty_classes(self, parser: TailwindClassParser) -> None:
        """Test extracting from element with no classes."""
        soup = parser.parse_html("<div>Content</div>")
        element = soup.find("div")
        classes = parser.extract_classes(element)
        assert classes == []

    def test_filter_responsive_prefixes(self, parser: TailwindClassParser) -> None:
        """Test filtering out responsive prefixes."""
        classes = ["p-4", "md:p-8", "lg:p-12", "text-center"]
        filtered = parser.filter_supported_classes(classes)
        assert "p-4" in filtered
        assert "text-center" in filtered
        assert "md:p-8" not in filtered
        assert "lg:p-12" not in filtered

    def test_filter_state_prefixes(self, parser: TailwindClassParser) -> None:
        """Test filtering out state prefixes."""
        classes = ["bg-blue-500", "hover:bg-blue-600", "focus:ring-2"]
        filtered = parser.filter_supported_classes(classes)
        assert "bg-blue-500" in filtered
        assert "hover:bg-blue-600" not in filtered
        assert "focus:ring-2" not in filtered

    def test_filter_unsupported_classes(self, parser: TailwindClassParser) -> None:
        """Test filtering out unsupported classes."""
        classes = ["flex", "justify-center", "items-center", "p-4"]
        filtered = parser.filter_supported_classes(classes)
        assert "p-4" in filtered
        assert "flex" not in filtered
        assert "justify-center" not in filtered
        assert "items-center" not in filtered

    def test_filter_grid_classes(self, parser: TailwindClassParser) -> None:
        """Test filtering out grid classes."""
        classes = ["grid", "grid-cols-3", "gap-4", "p-4"]
        filtered = parser.filter_supported_classes(classes)
        assert "p-4" in filtered
        assert "grid" not in filtered
        assert "grid-cols-3" not in filtered
        assert "gap-4" not in filtered

    def test_filter_negative_margins(self, parser: TailwindClassParser) -> None:
        """Test filtering out negative margins."""
        classes = ["m-4", "-m-4", "-mt-2", "-mx-8"]
        filtered = parser.filter_supported_classes(classes)
        assert "m-4" in filtered
        assert "-m-4" not in filtered
        assert "-mt-2" not in filtered
        assert "-mx-8" not in filtered

    def test_filter_transform_classes(self, parser: TailwindClassParser) -> None:
        """Test filtering out transform classes."""
        classes = ["rotate-45", "scale-150", "translate-x-4", "skew-y-3"]
        filtered = parser.filter_supported_classes(classes)
        assert len(filtered) == 0

    def test_is_tailwind_class_prefixes(self, parser: TailwindClassParser) -> None:
        """Test detecting Tailwind classes by prefix."""
        assert parser.is_tailwind_class("p-4")
        assert parser.is_tailwind_class("bg-blue-500")
        assert parser.is_tailwind_class("text-lg")
        assert parser.is_tailwind_class("rounded-lg")

    def test_is_tailwind_class_single_words(self, parser: TailwindClassParser) -> None:
        """Test detecting single-word Tailwind classes."""
        assert parser.is_tailwind_class("block")
        assert parser.is_tailwind_class("hidden")
        assert parser.is_tailwind_class("underline")
        assert parser.is_tailwind_class("italic")

    def test_is_tailwind_class_arbitrary(self, parser: TailwindClassParser) -> None:
        """Test detecting arbitrary value syntax."""
        assert parser.is_tailwind_class("w-[200px]")
        assert parser.is_tailwind_class("p-[1rem]")
        assert parser.is_tailwind_class("[color:red]")

    def test_is_not_tailwind_class(self, parser: TailwindClassParser) -> None:
        """Test non-Tailwind classes return False."""
        assert not parser.is_tailwind_class("my-custom-class")
        assert not parser.is_tailwind_class("custom-component")
        assert not parser.is_tailwind_class("some-random-class")

    def test_mixed_classes(self, parser: TailwindClassParser) -> None:
        """Test mixed Tailwind and non-Tailwind classes."""
        classes = ["my-class", "p-4", "custom-style", "bg-blue-500"]
        filtered = parser.filter_supported_classes(classes)
        assert "p-4" in filtered
        assert "bg-blue-500" in filtered
        # Non-Tailwind classes pass through filter
        # (they're not in unsupported list, just won't convert)
        assert "my-class" in filtered

    def test_dark_mode_prefix(self, parser: TailwindClassParser) -> None:
        """Test dark mode prefix is filtered."""
        classes = ["bg-white", "dark:bg-gray-900"]
        filtered = parser.filter_supported_classes(classes)
        assert "bg-white" in filtered
        assert "dark:bg-gray-900" not in filtered

    def test_animation_classes(self, parser: TailwindClassParser) -> None:
        """Test animation classes are filtered."""
        classes = ["animate-spin", "animate-pulse", "duration-300"]
        filtered = parser.filter_supported_classes(classes)
        assert len(filtered) == 0

    def test_transition_classes(self, parser: TailwindClassParser) -> None:
        """Test transition classes are filtered."""
        classes = ["transition", "transition-all", "ease-in-out"]
        filtered = parser.filter_supported_classes(classes)
        assert len(filtered) == 0


class TestParserIntegration:
    """Integration tests for parser with HTML."""

    @pytest.fixture
    def parser(self) -> TailwindClassParser:
        """Create a parser instance for testing."""
        return TailwindClassParser()

    def test_complex_html(self, parser: TailwindClassParser) -> None:
        """Test parsing complex HTML structure."""
        html = """
        <div class="container mx-auto p-4">
            <header class="bg-blue-600 text-white py-4">
                <h1 class="text-2xl font-bold">Title</h1>
            </header>
            <main class="mt-8">
                <article class="bg-white rounded-lg shadow-lg p-6">
                    <h2 class="text-xl mb-4">Article</h2>
                    <p class="text-gray-600">Content</p>
                </article>
            </main>
        </div>
        """
        soup = parser.parse_html(html)
        elements = list(parser.get_elements_with_classes(soup))

        # Should find all elements with classes
        # div, header, h1, main, article, h2, p = 7 elements
        assert len(elements) == 7

    def test_inline_elements(self, parser: TailwindClassParser) -> None:
        """Test parsing inline elements."""
        html = '<p>This is <span class="font-bold">bold</span> and <span class="italic">italic</span>.</p>'
        soup = parser.parse_html(html)
        elements = list(parser.get_elements_with_classes(soup))
        assert len(elements) == 2

    def test_form_elements(self, parser: TailwindClassParser) -> None:
        """Test parsing form elements."""
        html = """
        <form class="space-y-4">
            <input type="text" class="border rounded-md p-2 w-full">
            <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded-lg">Submit</button>
        </form>
        """
        soup = parser.parse_html(html)
        elements = list(parser.get_elements_with_classes(soup))
        # Note: space-y-4 is filtered as unsupported
        assert len(elements) == 3
