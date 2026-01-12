"""Tests for the CSS transformer module."""

import pytest

from tailwind_email.transformer import CSSTransformer


class TestCSSTransformer:
    """Tests for CSSTransformer class."""

    @pytest.fixture
    def transformer(self) -> CSSTransformer:
        """Create a transformer instance for testing."""
        return CSSTransformer()

    @pytest.fixture
    def transformer_no_mso(self) -> CSSTransformer:
        """Create a transformer without MSO properties."""
        return CSSTransformer(include_mso=False)

    def test_transform_padding(self, transformer: CSSTransformer) -> None:
        """Test padding transformation."""
        result = transformer.transform_class("p-4")
        assert result == {"padding": "16px"}

    def test_transform_padding_x(self, transformer: CSSTransformer) -> None:
        """Test horizontal padding transformation."""
        result = transformer.transform_class("px-4")
        assert result is not None
        assert "padding-left" in result
        assert "padding-right" in result

    def test_transform_padding_y(self, transformer: CSSTransformer) -> None:
        """Test vertical padding transformation."""
        result = transformer.transform_class("py-4")
        assert result is not None
        assert "padding-top" in result
        assert "padding-bottom" in result

    def test_transform_individual_padding(self, transformer: CSSTransformer) -> None:
        """Test individual padding sides."""
        assert transformer.transform_class("pt-4") == {"padding-top": "16px"}
        assert transformer.transform_class("pr-4") == {"padding-right": "16px"}
        assert transformer.transform_class("pb-4") == {"padding-bottom": "16px"}
        assert transformer.transform_class("pl-4") == {"padding-left": "16px"}

    def test_transform_margin(self, transformer: CSSTransformer) -> None:
        """Test margin transformation."""
        result = transformer.transform_class("m-4")
        assert result == {"margin": "16px"}

    def test_transform_margin_auto(self, transformer: CSSTransformer) -> None:
        """Test margin auto transformation."""
        result = transformer.transform_class("mx-auto")
        assert result is not None
        assert result.get("margin-left") == "auto"
        assert result.get("margin-right") == "auto"

    def test_transform_width(self, transformer: CSSTransformer) -> None:
        """Test width transformation."""
        assert transformer.transform_class("w-64") == {"width": "256px"}
        assert transformer.transform_class("w-full") == {"width": "100%"}
        assert transformer.transform_class("w-1/2") == {"width": "50%"}

    def test_transform_height(self, transformer: CSSTransformer) -> None:
        """Test height transformation."""
        assert transformer.transform_class("h-32") == {"height": "128px"}
        assert transformer.transform_class("h-full") == {"height": "100%"}
        assert transformer.transform_class("h-auto") == {"height": "auto"}

    def test_transform_max_width(self, transformer: CSSTransformer) -> None:
        """Test max-width transformation."""
        assert transformer.transform_class("max-w-lg") == {"max-width": "512px"}
        assert transformer.transform_class("max-w-full") == {"max-width": "100%"}

    def test_transform_background_color(self, transformer: CSSTransformer) -> None:
        """Test background color transformation."""
        result = transformer.transform_class("bg-blue-500")
        assert result == {"background-color": "#3b82f6"}

    def test_transform_background_special(self, transformer: CSSTransformer) -> None:
        """Test special background colors."""
        assert transformer.transform_class("bg-white") == {"background-color": "#ffffff"}
        assert transformer.transform_class("bg-black") == {"background-color": "#000000"}
        assert transformer.transform_class("bg-transparent") == {"background-color": "transparent"}

    def test_transform_text_color(self, transformer: CSSTransformer) -> None:
        """Test text color transformation."""
        result = transformer.transform_class("text-blue-500")
        assert result == {"color": "#3b82f6"}

    def test_transform_text_special(self, transformer: CSSTransformer) -> None:
        """Test special text colors."""
        assert transformer.transform_class("text-white") == {"color": "#ffffff"}
        assert transformer.transform_class("text-current") == {"color": "currentColor"}

    def test_transform_font_size(self, transformer: CSSTransformer) -> None:
        """Test font size transformation."""
        result = transformer.transform_class("text-lg")
        assert result is not None
        assert result["font-size"] == "18px"
        assert result["line-height"] == "28px"

    def test_transform_font_size_with_mso(self, transformer: CSSTransformer) -> None:
        """Test font size includes MSO properties."""
        result = transformer.transform_class("text-lg")
        assert "mso-line-height-rule" in result

    def test_transform_font_size_without_mso(self, transformer_no_mso: CSSTransformer) -> None:
        """Test font size without MSO properties."""
        result = transformer_no_mso.transform_class("text-lg")
        assert "mso-line-height-rule" not in result

    def test_transform_font_weight(self, transformer: CSSTransformer) -> None:
        """Test font weight transformation."""
        assert transformer.transform_class("font-bold") == {"font-weight": "700"}
        assert transformer.transform_class("font-normal") == {"font-weight": "400"}
        assert transformer.transform_class("font-semibold") == {"font-weight": "600"}

    def test_transform_text_align(self, transformer: CSSTransformer) -> None:
        """Test text alignment transformation."""
        assert transformer.transform_class("text-left") == {"text-align": "left"}
        assert transformer.transform_class("text-center") == {"text-align": "center"}
        assert transformer.transform_class("text-right") == {"text-align": "right"}

    def test_transform_border_width(self, transformer: CSSTransformer) -> None:
        """Test border width transformation."""
        result = transformer.transform_class("border")
        assert result is not None
        assert result["border-width"] == "1px"
        assert result["border-style"] == "solid"

    def test_transform_border_width_variants(self, transformer: CSSTransformer) -> None:
        """Test border width variants."""
        result = transformer.transform_class("border-2")
        assert result["border-width"] == "2px"

    def test_transform_border_sides(self, transformer: CSSTransformer) -> None:
        """Test individual border sides."""
        result = transformer.transform_class("border-t-2")
        assert result is not None
        assert "border-top-width" in result

        result = transformer.transform_class("border-r-2")
        assert "border-right-width" in result

    def test_transform_border_radius(self, transformer: CSSTransformer) -> None:
        """Test border radius transformation."""
        assert transformer.transform_class("rounded-lg") == {"border-radius": "8px"}
        assert transformer.transform_class("rounded-full") == {"border-radius": "9999px"}
        assert transformer.transform_class("rounded-none") == {"border-radius": "0px"}

    def test_transform_border_radius_corners(self, transformer: CSSTransformer) -> None:
        """Test individual corner border radius."""
        result = transformer.transform_class("rounded-tl-lg")
        assert result == {"border-top-left-radius": "8px"}

        result = transformer.transform_class("rounded-t-lg")
        assert "border-top-left-radius" in result
        assert "border-top-right-radius" in result

    def test_transform_border_color(self, transformer: CSSTransformer) -> None:
        """Test border color transformation."""
        result = transformer.transform_class("border-gray-300")
        assert result == {"border-color": "#d1d5db"}

    def test_transform_opacity(self, transformer: CSSTransformer) -> None:
        """Test opacity transformation."""
        assert transformer.transform_class("opacity-50") == {"opacity": "0.5"}
        assert transformer.transform_class("opacity-100") == {"opacity": "1"}
        assert transformer.transform_class("opacity-0") == {"opacity": "0"}

    def test_transform_box_shadow(self, transformer: CSSTransformer) -> None:
        """Test box shadow transformation."""
        result = transformer.transform_class("shadow-lg")
        assert result is not None
        assert "box-shadow" in result

    def test_transform_display(self, transformer: CSSTransformer) -> None:
        """Test display transformation."""
        assert transformer.transform_class("block") == {"display": "block"}
        assert transformer.transform_class("inline-block") == {"display": "inline-block"}
        assert transformer.transform_class("hidden") == {"display": "none"}

    def test_transform_text_decoration(self, transformer: CSSTransformer) -> None:
        """Test text decoration transformation."""
        assert transformer.transform_class("underline") == {"text-decoration": "underline"}
        assert transformer.transform_class("line-through") == {"text-decoration": "line-through"}
        assert transformer.transform_class("no-underline") == {"text-decoration": "none"}

    def test_transform_text_transform(self, transformer: CSSTransformer) -> None:
        """Test text transform transformation."""
        assert transformer.transform_class("uppercase") == {"text-transform": "uppercase"}
        assert transformer.transform_class("lowercase") == {"text-transform": "lowercase"}
        assert transformer.transform_class("capitalize") == {"text-transform": "capitalize"}

    def test_transform_line_height(self, transformer: CSSTransformer) -> None:
        """Test line height transformation."""
        result = transformer.transform_class("leading-relaxed")
        assert result is not None
        assert result["line-height"] == "1.625"

    def test_transform_letter_spacing(self, transformer: CSSTransformer) -> None:
        """Test letter spacing transformation."""
        assert transformer.transform_class("tracking-wide") == {"letter-spacing": "0.4px"}
        assert transformer.transform_class("tracking-tight") == {"letter-spacing": "-0.4px"}

    def test_transform_arbitrary_width(self, transformer: CSSTransformer) -> None:
        """Test arbitrary width value."""
        result = transformer.transform_class("w-[200px]")
        assert result == {"width": "200px"}

    def test_transform_arbitrary_rem(self, transformer: CSSTransformer) -> None:
        """Test arbitrary rem value conversion."""
        result = transformer.transform_class("p-[2rem]")
        assert result == {"padding": "32px"}

    def test_transform_arbitrary_property(self, transformer: CSSTransformer) -> None:
        """Test arbitrary property:value syntax."""
        result = transformer.transform_class("[color:red]")
        assert result == {"color": "red"}

    def test_transform_unrecognized_class(self, transformer: CSSTransformer) -> None:
        """Test unrecognized class returns None."""
        result = transformer.transform_class("unknown-class")
        assert result is None

    def test_transform_multiple_classes(self, transformer: CSSTransformer) -> None:
        """Test transforming multiple classes."""
        classes = ["p-4", "bg-blue-500", "text-white", "rounded-lg"]
        result = transformer.transform_classes(classes)

        assert result["padding"] == "16px"
        assert result["background-color"] == "#3b82f6"
        assert result["color"] == "#ffffff"
        assert result["border-radius"] == "8px"

    def test_to_style_string(self, transformer: CSSTransformer) -> None:
        """Test converting properties to style string."""
        properties = {
            "padding": "16px",
            "color": "#ffffff",
            "background-color": "#3b82f6",
        }
        result = transformer.to_style_string(properties)

        assert "padding: 16px" in result
        assert "color: #ffffff" in result
        assert "background-color: #3b82f6" in result

    def test_color_with_opacity(self, transformer: CSSTransformer) -> None:
        """Test color with opacity modifier."""
        result = transformer.transform_class("bg-blue-500/50")
        assert result is not None
        # Should be rgba
        assert "rgba" in result["background-color"]
        assert "0.5" in result["background-color"]

    def test_size_utility(self, transformer: CSSTransformer) -> None:
        """Test size utility."""
        result = transformer.transform_class("size-16")
        assert result is not None
        assert result["width"] == "64px"
        assert result["height"] == "64px"

    def test_truncate_utility(self, transformer: CSSTransformer) -> None:
        """Test truncate utility."""
        result = transformer.transform_class("truncate")
        assert result is not None
        assert result["overflow"] == "hidden"
        assert result["text-overflow"] == "ellipsis"
        assert result["white-space"] == "nowrap"

    def test_vertical_align(self, transformer: CSSTransformer) -> None:
        """Test vertical alignment."""
        assert transformer.transform_class("align-middle") == {"vertical-align": "middle"}
        assert transformer.transform_class("align-top") == {"vertical-align": "top"}

    def test_overflow(self, transformer: CSSTransformer) -> None:
        """Test overflow properties."""
        assert transformer.transform_class("overflow-hidden") == {"overflow": "hidden"}
        assert transformer.transform_class("overflow-auto") == {"overflow": "auto"}

    def test_float(self, transformer: CSSTransformer) -> None:
        """Test float properties."""
        assert transformer.transform_class("float-left") == {"float": "left"}
        assert transformer.transform_class("float-right") == {"float": "right"}

    def test_visibility(self, transformer: CSSTransformer) -> None:
        """Test visibility properties."""
        assert transformer.transform_class("visible") == {"visibility": "visible"}
        assert transformer.transform_class("invisible") == {"visibility": "hidden"}

    def test_custom_base_font_size(self) -> None:
        """Test custom base font size affects rem conversion."""
        transformer = CSSTransformer(base_font_size=20)
        result = transformer.transform_class("p-[1rem]")
        assert result == {"padding": "20px"}


class TestTransformerColorPalette:
    """Tests for color palette coverage."""

    @pytest.fixture
    def transformer(self) -> CSSTransformer:
        """Create a transformer instance for testing."""
        return CSSTransformer()

    def test_all_gray_scales(self, transformer: CSSTransformer) -> None:
        """Test gray scale colors."""
        for scale in ["slate", "gray", "zinc", "neutral", "stone"]:
            for shade in [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950]:
                cls = f"bg-{scale}-{shade}"
                result = transformer.transform_class(cls)
                assert result is not None, f"Failed for {cls}"
                assert "background-color" in result

    def test_all_color_scales(self, transformer: CSSTransformer) -> None:
        """Test main color scales."""
        colors = [
            "red",
            "orange",
            "amber",
            "yellow",
            "lime",
            "green",
            "emerald",
            "teal",
            "cyan",
            "sky",
            "blue",
            "indigo",
            "violet",
            "purple",
            "fuchsia",
            "pink",
            "rose",
        ]
        for color in colors:
            for shade in [50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950]:
                cls = f"text-{color}-{shade}"
                result = transformer.transform_class(cls)
                assert result is not None, f"Failed for {cls}"
                assert "color" in result
