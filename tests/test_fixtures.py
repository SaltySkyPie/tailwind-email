"""Tests using HTML fixtures for input/output validation."""

from tailwind_email import convert


class TestEmailTemplates:
    """Tests for common email template patterns."""

    def test_simple_button(self) -> None:
        """Test converting a simple button."""
        input_html = """
        <a href="#" class="bg-blue-500 text-white py-3 px-6 rounded-lg font-semibold text-center inline-block">
            Click Me
        </a>
        """
        output = convert(input_html)

        # Verify essential styles
        assert "background-color: #3b82f6" in output
        assert "color: #ffffff" in output
        assert "font-weight: 600" in output
        assert "border-radius: 8px" in output
        assert "display: inline-block" in output

    def test_card_component(self) -> None:
        """Test converting a card component."""
        input_html = """
        <div class="bg-white rounded-lg shadow-md p-6 max-w-md">
            <h2 class="text-xl font-bold text-gray-900 mb-2">Card Title</h2>
            <p class="text-gray-600 text-sm">Card description goes here.</p>
            <a href="#" class="mt-4 inline-block text-blue-500 underline">Learn more</a>
        </div>
        """
        output = convert(input_html)

        # Card container
        assert "background-color: #ffffff" in output
        assert "border-radius: 8px" in output
        assert "padding: 24px" in output
        assert "max-width: 448px" in output

        # Title
        assert "font-size: 20px" in output
        assert "font-weight: 700" in output
        assert "color: #111827" in output

        # Description
        assert "color: #4b5563" in output
        assert "font-size: 14px" in output

        # Link
        assert "color: #3b82f6" in output
        assert "text-decoration: underline" in output

    def test_email_header(self) -> None:
        """Test converting an email header."""
        input_html = """
        <table class="w-full bg-gray-100">
            <tr>
                <td class="p-6 text-center">
                    <img src="logo.png" alt="Logo" class="h-8 w-auto mx-auto">
                </td>
            </tr>
        </table>
        """
        output = convert(input_html)

        assert "width: 100%" in output
        assert "background-color: #f3f4f6" in output
        assert "padding: 24px" in output
        assert "text-align: center" in output
        assert "height: 32px" in output
        assert "width: auto" in output

    def test_email_footer(self) -> None:
        """Test converting an email footer."""
        input_html = """
        <table class="w-full bg-gray-800">
            <tr>
                <td class="p-8 text-center">
                    <p class="text-gray-400 text-sm mb-4">
                        You received this email because you subscribed.
                    </p>
                    <a href="#" class="text-white underline text-sm">Unsubscribe</a>
                </td>
            </tr>
        </table>
        """
        output = convert(input_html)

        assert "background-color: #1f2937" in output
        assert "padding: 32px" in output
        assert "text-align: center" in output
        assert "color: #9ca3af" in output
        assert "font-size: 14px" in output
        assert "color: #ffffff" in output
        assert "text-decoration: underline" in output

    def test_product_listing(self) -> None:
        """Test converting a product listing."""
        input_html = """
        <table class="w-full">
            <tr>
                <td class="w-1/3 p-4 align-top">
                    <img src="product.jpg" alt="Product" class="w-full rounded-md">
                </td>
                <td class="w-2/3 p-4 align-top">
                    <h3 class="text-lg font-bold text-gray-900">Product Name</h3>
                    <p class="text-gray-600 mt-2">Product description.</p>
                    <p class="text-2xl font-bold text-green-600 mt-4">$99.99</p>
                </td>
            </tr>
        </table>
        """
        output = convert(input_html)

        # Table structure
        assert "width: 100%" in output
        assert "width: 33.333333%" in output
        assert "width: 66.666667%" in output
        assert "padding: 16px" in output
        assert "vertical-align: top" in output

        # Product details
        assert "font-size: 18px" in output
        assert "color: #111827" in output
        assert "color: #4b5563" in output
        assert "font-size: 24px" in output
        assert "color: #16a34a" in output  # green-600

    def test_notification_banner(self) -> None:
        """Test converting a notification banner."""
        input_html = """
        <div class="bg-yellow-100 border-l-4 border-yellow-500 p-4">
            <div class="flex">
                <p class="text-yellow-700 font-medium">
                    Warning! Please verify your email address.
                </p>
            </div>
        </div>
        """
        output = convert(input_html)

        assert "background-color: #fef9c3" in output  # yellow-100
        assert "border-left-width: 4px" in output
        assert "border-color: #eab308" in output  # yellow-500
        assert "padding: 16px" in output
        assert "color: #a16207" in output  # yellow-700
        assert "font-weight: 500" in output

        # Flex should not appear
        assert "display: flex" not in output

    def test_social_links(self) -> None:
        """Test converting social media links."""
        input_html = """
        <table class="w-full">
            <tr>
                <td class="text-center p-4">
                    <a href="#" class="inline-block mx-2">
                        <img src="facebook.png" alt="Facebook" class="w-8 h-8">
                    </a>
                    <a href="#" class="inline-block mx-2">
                        <img src="twitter.png" alt="Twitter" class="w-8 h-8">
                    </a>
                    <a href="#" class="inline-block mx-2">
                        <img src="instagram.png" alt="Instagram" class="w-8 h-8">
                    </a>
                </td>
            </tr>
        </table>
        """
        output = convert(input_html)

        assert "text-align: center" in output
        assert "display: inline-block" in output
        assert "width: 32px" in output
        assert "height: 32px" in output

    def test_pricing_table(self) -> None:
        """Test converting a pricing table cell."""
        input_html = """
        <td class="bg-white rounded-lg shadow-lg p-6 text-center border-2 border-blue-500">
            <h3 class="text-gray-500 text-sm uppercase tracking-widest">Pro Plan</h3>
            <p class="text-4xl font-extrabold text-gray-900 mt-4">$29</p>
            <p class="text-gray-500 mt-1">/month</p>
            <ul class="mt-6 text-left text-gray-600">
                <li class="py-2">Feature one</li>
                <li class="py-2">Feature two</li>
            </ul>
            <a href="#" class="mt-6 block bg-blue-500 text-white py-3 rounded-lg font-bold">
                Get Started
            </a>
        </td>
        """
        output = convert(input_html)

        # Container styling
        assert "background-color: #ffffff" in output
        assert "border-radius: 8px" in output
        assert "padding: 24px" in output
        assert "text-align: center" in output
        assert "border-width: 2px" in output
        assert "border-color: #3b82f6" in output

        # Plan name
        assert "color: #6b7280" in output
        assert "font-size: 14px" in output
        assert "text-transform: uppercase" in output
        assert "letter-spacing: 1.6px" in output

        # Price
        assert "font-size: 36px" in output
        assert "font-weight: 800" in output

        # Button
        assert "display: block" in output
        assert "font-weight: 700" in output


class TestComplexScenarios:
    """Tests for complex HTML structures."""

    def test_nested_tables(self) -> None:
        """Test deeply nested table structures."""
        input_html = """
        <table class="w-full bg-gray-100">
            <tr>
                <td class="p-4">
                    <table class="w-full bg-white rounded-lg">
                        <tr>
                            <td class="p-6">
                                <table class="w-full">
                                    <tr>
                                        <td class="text-center">
                                            <p class="text-gray-900 font-bold">Nested Content</p>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
        """
        output = convert(input_html)

        # All width: 100% should be present (3 tables)
        assert output.count("width: 100%") >= 3

        # All backgrounds present
        assert "background-color: #f3f4f6" in output
        assert "background-color: #ffffff" in output

        # Text styling at deepest level
        assert "color: #111827" in output
        assert "font-weight: 700" in output

    def test_two_column_layout(self) -> None:
        """Test two-column layout pattern."""
        input_html = """
        <table class="w-full max-w-2xl mx-auto">
            <tr>
                <td class="w-1/2 p-4 bg-blue-50 align-top">
                    <h3 class="text-lg font-bold text-blue-900">Column 1</h3>
                    <p class="text-blue-700 mt-2">Content for the first column.</p>
                </td>
                <td class="w-1/2 p-4 bg-green-50 align-top">
                    <h3 class="text-lg font-bold text-green-900">Column 2</h3>
                    <p class="text-green-700 mt-2">Content for the second column.</p>
                </td>
            </tr>
        </table>
        """
        output = convert(input_html)

        # Layout
        assert "max-width: 672px" in output
        assert "width: 50%" in output
        assert "vertical-align: top" in output

        # Column 1 colors
        assert "background-color: #eff6ff" in output  # blue-50
        assert "color: #1e3a8a" in output  # blue-900
        assert "color: #1d4ed8" in output  # blue-700

        # Column 2 colors
        assert "background-color: #f0fdf4" in output  # green-50
        assert "color: #14532d" in output  # green-900
        assert "color: #15803d" in output  # green-700

    def test_hero_section(self) -> None:
        """Test hero section pattern."""
        input_html = """
        <table class="w-full bg-gradient-to-r from-blue-500 to-purple-600">
            <tr>
                <td class="p-12 text-center">
                    <h1 class="text-4xl font-extrabold text-white mb-4">Welcome!</h1>
                    <p class="text-xl text-blue-100 mb-8">Start your journey today.</p>
                    <a href="#" class="bg-white text-blue-600 py-3 px-8 rounded-full font-bold inline-block">
                        Get Started
                    </a>
                </td>
            </tr>
        </table>
        """
        output = convert(input_html)

        # Note: gradient classes won't convert, but other styles should
        assert "padding: 48px" in output
        assert "text-align: center" in output

        # Title
        assert "font-size: 36px" in output
        assert "font-weight: 800" in output
        assert "color: #ffffff" in output

        # Subtitle
        assert "font-size: 20px" in output
        assert "color: #dbeafe" in output  # blue-100

        # Button
        assert "background-color: #ffffff" in output
        assert "color: #2563eb" in output  # blue-600
        assert "border-radius: 9999px" in output

    def test_receipt_table(self) -> None:
        """Test receipt/invoice table pattern."""
        input_html = """
        <table class="w-full border border-gray-200">
            <tr class="bg-gray-50">
                <th class="p-3 text-left text-sm font-semibold text-gray-900 border-b border-gray-200">Item</th>
                <th class="p-3 text-right text-sm font-semibold text-gray-900 border-b border-gray-200">Price</th>
            </tr>
            <tr>
                <td class="p-3 text-left text-gray-700 border-b border-gray-200">Product A</td>
                <td class="p-3 text-right text-gray-700 border-b border-gray-200">$10.00</td>
            </tr>
            <tr>
                <td class="p-3 text-left text-gray-700 border-b border-gray-200">Product B</td>
                <td class="p-3 text-right text-gray-700 border-b border-gray-200">$20.00</td>
            </tr>
            <tr class="bg-gray-100">
                <td class="p-3 text-left font-bold text-gray-900">Total</td>
                <td class="p-3 text-right font-bold text-gray-900">$30.00</td>
            </tr>
        </table>
        """
        output = convert(input_html)

        # Table styling
        assert "border-width: 1px" in output
        assert "border-color: #e5e7eb" in output  # gray-200

        # Header row
        assert "background-color: #f9fafb" in output  # gray-50
        assert "text-align: left" in output
        assert "font-weight: 600" in output
        assert "font-size: 14px" in output
        assert "color: #111827" in output  # gray-900

        # Data rows
        assert "color: #374151" in output  # gray-700
        assert "text-align: right" in output

        # Total row
        assert "background-color: #f3f4f6" in output  # gray-100
        assert "font-weight: 700" in output


class TestRealWorldEmails:
    """Tests for real-world email template patterns."""

    def test_welcome_email(self) -> None:
        """Test a complete welcome email template."""
        input_html = """
        <table class="w-full max-w-xl mx-auto bg-white">
            <tr>
                <td class="p-8 text-center bg-blue-600">
                    <img src="logo.png" alt="Logo" class="h-12 mx-auto">
                </td>
            </tr>
            <tr>
                <td class="p-8">
                    <h1 class="text-2xl font-bold text-gray-900 mb-4">Welcome to Our Service!</h1>
                    <p class="text-gray-600 mb-6">
                        We're excited to have you on board. Let's get started.
                    </p>
                    <a href="#" class="block w-full bg-blue-600 text-white text-center py-4 rounded-lg font-bold mb-6">
                        Verify Your Email
                    </a>
                    <p class="text-sm text-gray-500">
                        If you didn't create an account, you can ignore this email.
                    </p>
                </td>
            </tr>
            <tr>
                <td class="p-6 bg-gray-100 text-center">
                    <p class="text-sm text-gray-500">
                        &copy; 2024 Company Name. All rights reserved.
                    </p>
                </td>
            </tr>
        </table>
        """
        output = convert(input_html)

        # Basic structure
        assert "max-width: 576px" in output
        assert "background-color: #ffffff" in output

        # Header
        assert "background-color: #2563eb" in output  # blue-600
        assert "height: 48px" in output

        # Content
        assert "font-size: 24px" in output
        assert "font-weight: 700" in output
        assert "color: #111827" in output

        # Button
        assert "display: block" in output
        assert "width: 100%" in output

        # Footer
        assert "background-color: #f3f4f6" in output  # gray-100
