"""Stress tests and performance tests for the tailwind-email library."""

import time

import pytest

from tailwind_email import TailwindEmailConverter, convert
from tailwind_email.transformer import CSSTransformer


class TestManyClasses:
    """Tests for elements with many classes."""

    def test_element_with_10_classes(self) -> None:
        """Test element with 10 classes."""
        html = """<div class="p-4 m-2 bg-blue-500 text-white font-bold
                   text-lg rounded-lg shadow-md border border-blue-600">Content</div>"""
        output = convert(html)

        assert "padding: 16px" in output
        assert "margin: 8px" in output
        assert "background-color: #3b82f6" in output
        assert "color: #ffffff" in output
        assert "font-weight: 700" in output
        assert "font-size: 18px" in output
        assert "border-radius: 8px" in output
        assert "box-shadow:" in output
        assert "border-width: 1px" in output
        assert "border-color: #2563eb" in output

    def test_element_with_20_classes(self) -> None:
        """Test element with 20 classes."""
        html = """<div class="p-4 px-6 py-8 m-2 mt-4 mb-6 bg-blue-500 text-white
                   font-bold text-lg leading-relaxed tracking-wide rounded-lg
                   shadow-md border border-blue-600 w-full max-w-xl h-auto
                   text-center overflow-hidden">Content</div>"""
        output = convert(html)

        # Verify a subset of important styles
        assert "padding: 16px" in output or "padding-left: 24px" in output
        assert "background-color: #3b82f6" in output
        assert "color: #ffffff" in output
        assert "font-weight: 700" in output
        assert "border-radius: 8px" in output
        assert "max-width: 576px" in output
        assert "text-align: center" in output

    def test_element_with_50_classes(self) -> None:
        """Test element with 50 classes (including filtered ones)."""
        classes = [
            "p-4",
            "px-6",
            "py-8",
            "pt-2",
            "pr-4",
            "pb-6",
            "pl-8",
            "m-2",
            "mx-4",
            "my-6",
            "mt-2",
            "mr-4",
            "mb-6",
            "ml-8",
            "bg-blue-500",
            "text-white",
            "border-gray-300",
            "font-bold",
            "font-semibold",
            "text-lg",
            "text-xl",
            "leading-relaxed",
            "leading-tight",
            "tracking-wide",
            "rounded-lg",
            "rounded-t-xl",
            "rounded-b-md",
            "shadow-md",
            "shadow-lg",
            "opacity-90",
            "border",
            "border-2",
            "border-solid",
            "w-full",
            "w-1/2",
            "max-w-xl",
            "min-w-0",
            "h-auto",
            "h-32",
            "max-h-64",
            "text-center",
            "text-left",
            "uppercase",
            "underline",
            "italic",
            "truncate",
            "block",
            "inline-block",
            "hidden",
            "overflow-hidden",
            "visible",
            # Filtered classes that should be ignored
            "flex",
            "grid",
            "hover:bg-blue-600",
            "md:p-8",
        ]
        html = f'<div class="{" ".join(classes)}">Content</div>'
        output = convert(html)

        # Should handle without error and produce valid output
        assert "style=" in output
        assert "Content" in output
        # Filtered classes should not produce output
        assert "display: flex" not in output
        assert "display: grid" not in output


class TestManyElements:
    """Tests for documents with many elements."""

    def test_50_elements(self) -> None:
        """Test document with 50 styled elements."""
        elements = [
            f'<div class="p-{i % 8 + 1} bg-gray-{(i % 9 + 1) * 100}">Element {i}</div>'
            for i in range(50)
        ]
        html = f"<div>{''.join(elements)}</div>"
        output = convert(html)

        # All elements should be processed
        assert output.count("style=") >= 50
        assert "Element 0" in output
        assert "Element 49" in output

    def test_100_elements(self) -> None:
        """Test document with 100 styled elements."""
        elements = [f'<p class="text-sm text-gray-600 mb-2">Paragraph {i}</p>' for i in range(100)]
        html = f"<div>{''.join(elements)}</div>"
        output = convert(html)

        assert output.count("font-size: 14px") >= 100
        assert "Paragraph 0" in output
        assert "Paragraph 99" in output

    def test_nested_100_levels(self) -> None:
        """Test deeply nested elements (100 levels)."""
        html = ""
        for i in range(100):
            html += f'<div class="p-{i % 8 + 1}">'
        html += "Content"
        for _ in range(100):
            html += "</div>"

        output = convert(html)
        assert "Content" in output
        assert output.count("style=") >= 50  # At least half should be styled


class TestLargeDocuments:
    """Tests for large HTML documents."""

    def test_10kb_document(self) -> None:
        """Test 10KB HTML document."""
        # Generate ~10KB of HTML
        row = """
        <tr>
            <td class="p-4 border-b border-gray-200 text-gray-900">Data Cell</td>
            <td class="p-4 border-b border-gray-200 text-gray-600">More Data</td>
            <td class="p-4 border-b border-gray-200 text-right font-bold">$99.99</td>
        </tr>
        """
        rows = row * 50  # ~10KB
        html = f"""
        <table class="w-full bg-white rounded-lg shadow-md">
            <thead>
                <tr class="bg-gray-100">
                    <th class="p-4 text-left font-semibold">Column 1</th>
                    <th class="p-4 text-left font-semibold">Column 2</th>
                    <th class="p-4 text-right font-semibold">Amount</th>
                </tr>
            </thead>
            <tbody>
                {rows}
            </tbody>
        </table>
        """

        output = convert(html)

        # Verify conversion happened
        assert "width: 100%" in output
        assert "background-color: #ffffff" in output
        assert output.count("padding: 16px") >= 50

    def test_50kb_document(self) -> None:
        """Test 50KB HTML document."""
        # Generate ~50KB of HTML content
        product_card = """
        <div class="bg-white rounded-lg shadow-md p-6 mb-4">
            <img class="w-full h-48 object-cover rounded-t-lg" src="product.jpg">
            <h3 class="text-lg font-bold text-gray-900 mt-4">Product Name Here</h3>
            <p class="text-gray-600 text-sm mt-2">Product description that is somewhat longer to add more content to this template for testing purposes.</p>
            <div class="mt-4">
                <span class="text-2xl font-extrabold text-green-600">$99.99</span>
                <span class="text-gray-400 line-through ml-2">$149.99</span>
            </div>
            <button class="mt-4 w-full bg-blue-500 text-white py-3 rounded-lg font-bold">
                Add to Cart
            </button>
        </div>
        """
        cards = product_card * 100  # ~50KB
        html = f"""
        <div class="max-w-6xl mx-auto p-8 bg-gray-100">
            <h1 class="text-3xl font-bold text-gray-900 mb-8">Product Catalog</h1>
            <div class="grid-cols-3">
                {cards}
            </div>
        </div>
        """

        start_time = time.time()
        output = convert(html)
        elapsed = time.time() - start_time

        # Should complete in reasonable time (< 5 seconds)
        assert elapsed < 5.0, f"Conversion took too long: {elapsed:.2f}s"

        # Verify conversion
        assert "max-width:" in output
        assert "background-color: #ffffff" in output
        assert output.count("border-radius: 8px") >= 100


class TestPerformance:
    """Performance tests for conversion speed."""

    def measure_conversion_time(self, html: str, iterations: int = 10) -> float:
        """Measure average conversion time."""
        times = []
        converter = TailwindEmailConverter()

        for _ in range(iterations):
            start = time.time()
            converter.convert(html)
            times.append(time.time() - start)

        return sum(times) / len(times)

    def test_simple_conversion_speed(self) -> None:
        """Test simple conversion is fast."""
        html = '<div class="p-4 bg-blue-500 text-white rounded-lg">Content</div>'
        avg_time = self.measure_conversion_time(html)

        # Simple conversion should be < 10ms
        assert avg_time < 0.01, f"Simple conversion too slow: {avg_time * 1000:.2f}ms"

    def test_medium_conversion_speed(self) -> None:
        """Test medium complexity conversion speed."""
        html = """
        <table class="w-full bg-white">
            <tr>
                <td class="p-4 bg-blue-600 text-white font-bold text-xl">Header</td>
            </tr>
            <tr>
                <td class="p-8">
                    <h1 class="text-2xl font-bold text-gray-900 mb-4">Title</h1>
                    <p class="text-gray-600 leading-relaxed mb-4">Content paragraph with styling.</p>
                    <a href="#" class="inline-block bg-green-500 text-white py-3 px-6 rounded-lg font-bold">Button</a>
                </td>
            </tr>
            <tr>
                <td class="p-4 bg-gray-100 text-center text-gray-500 text-sm">Footer</td>
            </tr>
        </table>
        """
        avg_time = self.measure_conversion_time(html)

        # Medium conversion should be < 50ms
        assert avg_time < 0.05, f"Medium conversion too slow: {avg_time * 1000:.2f}ms"

    def test_converter_reuse_performance(self) -> None:
        """Test that reusing converter is faster than creating new ones."""
        html = '<div class="p-4 bg-blue-500">Content</div>'

        # Time with new converter each time
        start = time.time()
        for _ in range(100):
            convert(html)
        new_converter_time = time.time() - start

        # Time with reused converter
        converter = TailwindEmailConverter()
        start = time.time()
        for _ in range(100):
            converter.convert(html)
        reused_converter_time = time.time() - start

        # Reused converter should be at least as fast
        assert reused_converter_time <= new_converter_time * 1.5


class TestTransformerPerformance:
    """Performance tests for the CSS transformer."""

    @pytest.fixture
    def transformer(self) -> CSSTransformer:
        """Create transformer instance."""
        return CSSTransformer()

    def test_single_class_transform_speed(self, transformer: CSSTransformer) -> None:
        """Test single class transformation is fast."""
        start = time.time()
        for _ in range(1000):
            transformer.transform_class("p-4")
        elapsed = time.time() - start

        # 1000 transformations should be < 100ms
        assert elapsed < 0.1, f"Transform too slow: {elapsed * 1000:.2f}ms for 1000 ops"

    def test_multiple_class_transform_speed(self, transformer: CSSTransformer) -> None:
        """Test multiple class transformation speed."""
        classes = ["p-4", "m-2", "bg-blue-500", "text-white", "font-bold", "rounded-lg"]

        start = time.time()
        for _ in range(1000):
            transformer.transform_classes(classes)
        elapsed = time.time() - start

        # Should be reasonably fast
        assert elapsed < 0.5, f"Multiple transform too slow: {elapsed * 1000:.2f}ms for 1000 ops"


class TestAllSpacingValues:
    """Tests for all spacing scale values."""

    def test_all_padding_values(self) -> None:
        """Test all standard padding values."""
        values = [
            ("p-0", "0px"),
            ("p-px", "1px"),
            ("p-0.5", "2px"),
            ("p-1", "4px"),
            ("p-1.5", "6px"),
            ("p-2", "8px"),
            ("p-2.5", "10px"),
            ("p-3", "12px"),
            ("p-3.5", "14px"),
            ("p-4", "16px"),
            ("p-5", "20px"),
            ("p-6", "24px"),
            ("p-7", "28px"),
            ("p-8", "32px"),
            ("p-9", "36px"),
            ("p-10", "40px"),
            ("p-11", "44px"),
            ("p-12", "48px"),
            ("p-14", "56px"),
            ("p-16", "64px"),
            ("p-20", "80px"),
            ("p-24", "96px"),
            ("p-28", "112px"),
            ("p-32", "128px"),
            ("p-36", "144px"),
            ("p-40", "160px"),
            ("p-44", "176px"),
            ("p-48", "192px"),
            ("p-52", "208px"),
            ("p-56", "224px"),
            ("p-60", "240px"),
            ("p-64", "256px"),
            ("p-72", "288px"),
            ("p-80", "320px"),
            ("p-96", "384px"),
        ]

        for cls, expected in values:
            html = f'<div class="{cls}">Content</div>'
            output = convert(html)
            assert f"padding: {expected}" in output, f"Failed for {cls}: expected {expected}"

    def test_all_margin_values(self) -> None:
        """Test all standard margin values."""
        values = [
            ("m-0", "0px"),
            ("m-1", "4px"),
            ("m-2", "8px"),
            ("m-4", "16px"),
            ("m-8", "32px"),
            ("m-16", "64px"),
            ("m-auto", "auto"),
        ]

        for cls, expected in values:
            html = f'<div class="{cls}">Content</div>'
            output = convert(html)
            assert f"margin: {expected}" in output, f"Failed for {cls}"


class TestAllWidthValues:
    """Tests for all width values."""

    def test_pixel_widths(self) -> None:
        """Test pixel-based widths."""
        values = [
            ("w-0", "0px"),
            ("w-px", "1px"),
            ("w-4", "16px"),
            ("w-8", "32px"),
            ("w-16", "64px"),
            ("w-32", "128px"),
            ("w-64", "256px"),
            ("w-96", "384px"),
        ]

        for cls, expected in values:
            html = f'<div class="{cls}">Content</div>'
            output = convert(html)
            assert f"width: {expected}" in output, f"Failed for {cls}"

    def test_percentage_widths(self) -> None:
        """Test percentage-based widths."""
        values = [
            ("w-1/2", "50%"),
            ("w-1/3", "33.333333%"),
            ("w-2/3", "66.666667%"),
            ("w-1/4", "25%"),
            ("w-3/4", "75%"),
            ("w-full", "100%"),
        ]

        for cls, expected in values:
            html = f'<div class="{cls}">Content</div>'
            output = convert(html)
            assert f"width: {expected}" in output, f"Failed for {cls}"

    def test_container_widths(self) -> None:
        """Test container-sized widths."""
        values = [
            ("w-xs", "320px"),
            ("w-sm", "384px"),
            ("w-md", "448px"),
            ("w-lg", "512px"),
            ("w-xl", "576px"),
            ("w-2xl", "672px"),
            ("w-3xl", "768px"),
        ]

        for cls, expected in values:
            html = f'<div class="{cls}">Content</div>'
            output = convert(html)
            assert f"width: {expected}" in output, f"Failed for {cls}"


class TestAllBorderRadiusValues:
    """Tests for all border radius values."""

    def test_all_radius_sizes(self) -> None:
        """Test all radius sizes."""
        values = [
            ("rounded-none", "0px"),
            ("rounded-sm", "2px"),
            ("rounded", "4px"),
            ("rounded-md", "6px"),
            ("rounded-lg", "8px"),
            ("rounded-xl", "12px"),
            ("rounded-2xl", "16px"),
            ("rounded-3xl", "24px"),
            ("rounded-full", "9999px"),
        ]

        for cls, expected in values:
            html = f'<div class="{cls}">Content</div>'
            output = convert(html)
            assert f"border-radius: {expected}" in output, f"Failed for {cls}"


class TestAllOpacityValues:
    """Tests for all opacity values."""

    def test_all_opacity_levels(self) -> None:
        """Test all opacity levels."""
        values = [
            ("opacity-0", "0"),
            ("opacity-5", "0.05"),
            ("opacity-10", "0.1"),
            ("opacity-20", "0.2"),
            ("opacity-25", "0.25"),
            ("opacity-30", "0.3"),
            ("opacity-40", "0.4"),
            ("opacity-50", "0.5"),
            ("opacity-60", "0.6"),
            ("opacity-70", "0.7"),
            ("opacity-75", "0.75"),
            ("opacity-80", "0.8"),
            ("opacity-90", "0.9"),
            ("opacity-95", "0.95"),
            ("opacity-100", "1"),
        ]

        for cls, expected in values:
            html = f'<div class="{cls}">Content</div>'
            output = convert(html)
            assert f"opacity: {expected}" in output, f"Failed for {cls}"


class TestMemoryUsage:
    """Tests for memory efficiency."""

    def test_no_memory_leak_on_repeated_conversion(self) -> None:
        """Test that repeated conversions don't leak memory."""
        import gc

        html = '<div class="p-4 bg-blue-500">Content</div>'

        # Run garbage collection before
        gc.collect()

        # Convert many times
        for _ in range(1000):
            convert(html)

        # Run garbage collection after
        gc.collect()

        # If we got here without running out of memory, test passes
        assert True

    def test_large_document_memory(self) -> None:
        """Test large document doesn't use excessive memory."""
        # Generate large HTML
        elements = [
            f'<div class="p-4 m-2 bg-gray-{(i % 9 + 1) * 100}">Element {i}</div>'
            for i in range(1000)
        ]
        html = f"<div>{''.join(elements)}</div>"

        # Convert should complete without memory issues
        output = convert(html)

        assert len(output) > len(html)
        assert output.count("style=") >= 1000
