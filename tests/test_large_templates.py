"""Tests for large and complex email templates."""

from tailwind_email import convert


class TestFullPageEmailTemplates:
    """Tests for complete, multi-section email templates."""

    def test_ecommerce_order_confirmation(self) -> None:
        """Test a complete e-commerce order confirmation email."""
        input_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Order Confirmation</title>
        </head>
        <body class="bg-gray-100">
            <table class="w-full">
                <tr>
                    <td class="p-4">
                        <table class="max-w-2xl mx-auto bg-white rounded-lg shadow-lg">
                            <!-- Header -->
                            <tr>
                                <td class="p-8 bg-indigo-600 rounded-t-lg text-center">
                                    <img src="logo.png" alt="Logo" class="h-10 mx-auto mb-4">
                                    <h1 class="text-2xl font-bold text-white">Order Confirmed!</h1>
                                    <p class="text-indigo-200 mt-2">Thank you for your purchase</p>
                                </td>
                            </tr>

                            <!-- Order Info -->
                            <tr>
                                <td class="p-8">
                                    <table class="w-full">
                                        <tr>
                                            <td class="w-1/2 align-top">
                                                <p class="text-sm text-gray-500 uppercase tracking-wide">Order Number</p>
                                                <p class="text-lg font-bold text-gray-900">#ORD-12345</p>
                                            </td>
                                            <td class="w-1/2 align-top text-right">
                                                <p class="text-sm text-gray-500 uppercase tracking-wide">Order Date</p>
                                                <p class="text-lg font-bold text-gray-900">Jan 15, 2024</p>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>

                            <!-- Products -->
                            <tr>
                                <td class="px-8 pb-8">
                                    <table class="w-full border border-gray-200 rounded-lg">
                                        <!-- Product Header -->
                                        <tr class="bg-gray-50">
                                            <th class="p-4 text-left text-sm font-semibold text-gray-900 border-b border-gray-200">Product</th>
                                            <th class="p-4 text-center text-sm font-semibold text-gray-900 border-b border-gray-200">Qty</th>
                                            <th class="p-4 text-right text-sm font-semibold text-gray-900 border-b border-gray-200">Price</th>
                                        </tr>

                                        <!-- Product 1 -->
                                        <tr>
                                            <td class="p-4 border-b border-gray-200">
                                                <table class="w-full">
                                                    <tr>
                                                        <td class="w-16">
                                                            <img src="product1.jpg" alt="Product 1" class="w-16 h-16 rounded-md">
                                                        </td>
                                                        <td class="pl-4 align-top">
                                                            <p class="font-semibold text-gray-900">Wireless Headphones</p>
                                                            <p class="text-sm text-gray-500">Color: Black</p>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                            <td class="p-4 text-center text-gray-900 border-b border-gray-200">1</td>
                                            <td class="p-4 text-right text-gray-900 border-b border-gray-200">$149.99</td>
                                        </tr>

                                        <!-- Product 2 -->
                                        <tr>
                                            <td class="p-4 border-b border-gray-200">
                                                <table class="w-full">
                                                    <tr>
                                                        <td class="w-16">
                                                            <img src="product2.jpg" alt="Product 2" class="w-16 h-16 rounded-md">
                                                        </td>
                                                        <td class="pl-4 align-top">
                                                            <p class="font-semibold text-gray-900">Phone Case</p>
                                                            <p class="text-sm text-gray-500">Size: Standard</p>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                            <td class="p-4 text-center text-gray-900 border-b border-gray-200">2</td>
                                            <td class="p-4 text-right text-gray-900 border-b border-gray-200">$29.98</td>
                                        </tr>

                                        <!-- Product 3 -->
                                        <tr>
                                            <td class="p-4 border-b border-gray-200">
                                                <table class="w-full">
                                                    <tr>
                                                        <td class="w-16">
                                                            <img src="product3.jpg" alt="Product 3" class="w-16 h-16 rounded-md">
                                                        </td>
                                                        <td class="pl-4 align-top">
                                                            <p class="font-semibold text-gray-900">USB-C Cable 3-Pack</p>
                                                            <p class="text-sm text-gray-500">Length: 6ft</p>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                            <td class="p-4 text-center text-gray-900 border-b border-gray-200">1</td>
                                            <td class="p-4 text-right text-gray-900 border-b border-gray-200">$19.99</td>
                                        </tr>

                                        <!-- Totals -->
                                        <tr>
                                            <td class="p-4 text-right text-gray-500" colspan="2">Subtotal</td>
                                            <td class="p-4 text-right text-gray-900">$199.96</td>
                                        </tr>
                                        <tr>
                                            <td class="p-4 text-right text-gray-500" colspan="2">Shipping</td>
                                            <td class="p-4 text-right text-gray-900">$9.99</td>
                                        </tr>
                                        <tr>
                                            <td class="p-4 text-right text-gray-500" colspan="2">Tax</td>
                                            <td class="p-4 text-right text-gray-900">$17.00</td>
                                        </tr>
                                        <tr class="bg-gray-50">
                                            <td class="p-4 text-right font-bold text-gray-900" colspan="2">Total</td>
                                            <td class="p-4 text-right font-bold text-indigo-600 text-xl">$226.95</td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>

                            <!-- Shipping Address -->
                            <tr>
                                <td class="px-8 pb-8">
                                    <table class="w-full">
                                        <tr>
                                            <td class="w-1/2 bg-gray-50 p-4 rounded-lg align-top">
                                                <p class="text-sm font-semibold text-gray-900 mb-2">Shipping Address</p>
                                                <p class="text-gray-600">John Doe</p>
                                                <p class="text-gray-600">123 Main Street</p>
                                                <p class="text-gray-600">Apt 4B</p>
                                                <p class="text-gray-600">New York, NY 10001</p>
                                            </td>
                                            <td class="w-8"></td>
                                            <td class="w-1/2 bg-gray-50 p-4 rounded-lg align-top">
                                                <p class="text-sm font-semibold text-gray-900 mb-2">Billing Address</p>
                                                <p class="text-gray-600">John Doe</p>
                                                <p class="text-gray-600">123 Main Street</p>
                                                <p class="text-gray-600">Apt 4B</p>
                                                <p class="text-gray-600">New York, NY 10001</p>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>

                            <!-- CTA -->
                            <tr>
                                <td class="px-8 pb-8 text-center">
                                    <a href="#" class="inline-block bg-indigo-600 text-white py-4 px-8 rounded-lg font-bold">
                                        Track Your Order
                                    </a>
                                    <p class="text-sm text-gray-500 mt-4">
                                        Questions? Contact us at support@example.com
                                    </p>
                                </td>
                            </tr>

                            <!-- Footer -->
                            <tr>
                                <td class="p-8 bg-gray-800 rounded-b-lg text-center">
                                    <table class="w-full">
                                        <tr>
                                            <td class="text-center pb-4">
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
                                        <tr>
                                            <td class="text-center">
                                                <p class="text-gray-400 text-sm mb-2">
                                                    &copy; 2024 Company Name. All rights reserved.
                                                </p>
                                                <p class="text-gray-500 text-xs">
                                                    123 Business Street, City, State 12345
                                                </p>
                                                <p class="text-gray-500 text-xs mt-2">
                                                    <a href="#" class="text-gray-400 underline">Unsubscribe</a> |
                                                    <a href="#" class="text-gray-400 underline">Privacy Policy</a>
                                                </p>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </body>
        </html>
        """
        output = convert(input_html)

        # Verify major structural elements
        assert "background-color: #f3f4f6" in output  # gray-100 body
        assert "max-width: 672px" in output  # max-w-2xl
        assert "background-color: #ffffff" in output  # white container

        # Verify header
        assert "background-color: #4f46e5" in output  # indigo-600
        assert "font-size: 24px" in output  # text-2xl
        assert "color: #c7d2fe" in output  # indigo-200

        # Verify order info section
        assert "text-transform: uppercase" in output
        assert "color: #6b7280" in output  # gray-500

        # Verify product table
        assert "border-width: 1px" in output
        assert "border-color: #e5e7eb" in output  # gray-200
        assert "width: 64px" in output  # w-16

        # Verify addresses
        assert "background-color: #f9fafb" in output  # gray-50
        assert "color: #4b5563" in output  # gray-600

        # Verify CTA
        assert "display: inline-block" in output
        assert "font-weight: 700" in output

        # Verify footer
        assert "background-color: #1f2937" in output  # gray-800
        assert "color: #9ca3af" in output  # gray-400

    def test_newsletter_template(self) -> None:
        """Test a complete newsletter email template."""
        input_html = """
        <!DOCTYPE html>
        <html>
        <body class="bg-gray-50">
            <table class="w-full">
                <tr>
                    <td class="p-4">
                        <table class="max-w-xl mx-auto">
                            <!-- Preheader -->
                            <tr>
                                <td class="text-xs text-gray-400 text-center py-2">
                                    View this email in your browser
                                </td>
                            </tr>

                            <!-- Header with Logo -->
                            <tr>
                                <td class="bg-white rounded-t-xl p-6 text-center border-b border-gray-200">
                                    <img src="logo.png" alt="Newsletter" class="h-8 mx-auto">
                                </td>
                            </tr>

                            <!-- Hero Section -->
                            <tr>
                                <td class="bg-gradient-to-r from-purple-600 to-pink-600 p-12 text-center">
                                    <p class="text-white text-sm uppercase tracking-widest mb-2">Weekly Update</p>
                                    <h1 class="text-3xl font-extrabold text-white mb-4">The Latest in Tech</h1>
                                    <p class="text-purple-100 text-lg mb-6">
                                        Your weekly digest of the most important tech news and trends.
                                    </p>
                                    <a href="#" class="inline-block bg-white text-purple-600 py-3 px-8 rounded-full font-bold">
                                        Read Full Issue
                                    </a>
                                </td>
                            </tr>

                            <!-- Featured Article -->
                            <tr>
                                <td class="bg-white p-8">
                                    <p class="text-xs text-purple-600 uppercase tracking-wider font-semibold mb-2">Featured</p>
                                    <h2 class="text-xl font-bold text-gray-900 mb-4">
                                        The Future of AI: What to Expect in 2024
                                    </h2>
                                    <p class="text-gray-600 mb-4">
                                        Artificial intelligence continues to evolve at a rapid pace. Here's what experts
                                        predict will be the biggest developments this year and how they'll impact your daily life.
                                    </p>
                                    <a href="#" class="text-purple-600 font-semibold underline">Read more &rarr;</a>
                                </td>
                            </tr>

                            <!-- Article Grid -->
                            <tr>
                                <td class="bg-gray-50 p-8">
                                    <h3 class="text-lg font-bold text-gray-900 mb-6">More Stories</h3>
                                    <table class="w-full">
                                        <tr>
                                            <!-- Article 1 -->
                                            <td class="w-1/2 pr-2 align-top pb-4">
                                                <table class="w-full bg-white rounded-lg overflow-hidden">
                                                    <tr>
                                                        <td>
                                                            <img src="article1.jpg" class="w-full h-32 object-cover">
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td class="p-4">
                                                            <p class="text-xs text-gray-500 mb-1">Technology</p>
                                                            <h4 class="font-semibold text-gray-900 mb-2">
                                                                New Smartphone Features Coming This Year
                                                            </h4>
                                                            <a href="#" class="text-purple-600 text-sm">Read &rarr;</a>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                            <!-- Article 2 -->
                                            <td class="w-1/2 pl-2 align-top pb-4">
                                                <table class="w-full bg-white rounded-lg overflow-hidden">
                                                    <tr>
                                                        <td>
                                                            <img src="article2.jpg" class="w-full h-32 object-cover">
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td class="p-4">
                                                            <p class="text-xs text-gray-500 mb-1">Business</p>
                                                            <h4 class="font-semibold text-gray-900 mb-2">
                                                                Remote Work Trends to Watch
                                                            </h4>
                                                            <a href="#" class="text-purple-600 text-sm">Read &rarr;</a>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                        <tr>
                                            <!-- Article 3 -->
                                            <td class="w-1/2 pr-2 align-top">
                                                <table class="w-full bg-white rounded-lg overflow-hidden">
                                                    <tr>
                                                        <td>
                                                            <img src="article3.jpg" class="w-full h-32 object-cover">
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td class="p-4">
                                                            <p class="text-xs text-gray-500 mb-1">Science</p>
                                                            <h4 class="font-semibold text-gray-900 mb-2">
                                                                Space Exploration Milestones
                                                            </h4>
                                                            <a href="#" class="text-purple-600 text-sm">Read &rarr;</a>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                            <!-- Article 4 -->
                                            <td class="w-1/2 pl-2 align-top">
                                                <table class="w-full bg-white rounded-lg overflow-hidden">
                                                    <tr>
                                                        <td>
                                                            <img src="article4.jpg" class="w-full h-32 object-cover">
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td class="p-4">
                                                            <p class="text-xs text-gray-500 mb-1">Health</p>
                                                            <h4 class="font-semibold text-gray-900 mb-2">
                                                                Digital Wellness Tips for 2024
                                                            </h4>
                                                            <a href="#" class="text-purple-600 text-sm">Read &rarr;</a>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>

                            <!-- Quote Section -->
                            <tr>
                                <td class="bg-purple-50 p-8 text-center">
                                    <p class="text-2xl text-purple-900 italic font-serif mb-4">
                                        "The best way to predict the future is to create it."
                                    </p>
                                    <p class="text-purple-700 font-semibold">— Peter Drucker</p>
                                </td>
                            </tr>

                            <!-- Subscription CTA -->
                            <tr>
                                <td class="bg-white p-8 text-center">
                                    <h3 class="text-xl font-bold text-gray-900 mb-2">Enjoying this newsletter?</h3>
                                    <p class="text-gray-600 mb-4">Share it with your friends and colleagues!</p>
                                    <table class="mx-auto">
                                        <tr>
                                            <td class="pr-2">
                                                <a href="#" class="inline-block bg-blue-500 text-white py-2 px-4 rounded-lg text-sm">
                                                    Share on Twitter
                                                </a>
                                            </td>
                                            <td class="pl-2">
                                                <a href="#" class="inline-block bg-blue-700 text-white py-2 px-4 rounded-lg text-sm">
                                                    Share on LinkedIn
                                                </a>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>

                            <!-- Footer -->
                            <tr>
                                <td class="bg-gray-900 rounded-b-xl p-8 text-center">
                                    <img src="logo-white.png" alt="Logo" class="h-6 mx-auto mb-4">
                                    <p class="text-gray-400 text-sm mb-4">
                                        You're receiving this because you subscribed to our newsletter.
                                    </p>
                                    <p class="text-gray-500 text-xs mb-2">
                                        Our mailing address: 123 Newsletter St, City, State 12345
                                    </p>
                                    <p class="text-gray-500 text-xs">
                                        <a href="#" class="text-gray-400 underline">Preferences</a> |
                                        <a href="#" class="text-gray-400 underline">Unsubscribe</a> |
                                        <a href="#" class="text-gray-400 underline">View Online</a>
                                    </p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
        </body>
        </html>
        """
        output = convert(input_html)

        # Verify structural elements
        assert "background-color: #f9fafb" in output  # gray-50
        assert "max-width: 576px" in output  # max-w-xl

        # Verify header
        assert "height: 32px" in output  # h-8
        assert "border-bottom-width: 1px" in output

        # Verify hero
        assert "padding: 48px" in output  # p-12
        assert "font-size: 30px" in output  # text-3xl
        assert "font-weight: 800" in output  # font-extrabold
        assert "border-radius: 9999px" in output  # rounded-full

        # Verify article grid
        assert "width: 50%" in output  # w-1/2
        assert "height: 128px" in output  # h-32
        # Note: object-fit has limited email support

        # Verify quote
        assert "background-color: #faf5ff" in output  # purple-50
        assert "color: #581c87" in output  # purple-900
        assert "font-style: italic" in output

        # Verify share buttons
        assert "background-color: #3b82f6" in output  # blue-500
        assert "background-color: #1d4ed8" in output  # blue-700

        # Verify footer
        assert "background-color: #111827" in output  # gray-900
        assert "color: #9ca3af" in output  # gray-400

    def test_transactional_password_reset(self) -> None:
        """Test a complete password reset email template."""
        input_html = """
        <table class="w-full bg-gray-100">
            <tr>
                <td class="p-8">
                    <table class="max-w-md mx-auto bg-white rounded-xl shadow-xl">
                        <!-- Header -->
                        <tr>
                            <td class="p-8 text-center border-b border-gray-200">
                                <div class="inline-block bg-red-100 rounded-full p-4 mb-4">
                                    <img src="lock-icon.png" alt="Security" class="w-12 h-12">
                                </div>
                                <h1 class="text-2xl font-bold text-gray-900">Reset Your Password</h1>
                            </td>
                        </tr>

                        <!-- Content -->
                        <tr>
                            <td class="p-8">
                                <p class="text-gray-600 mb-4">Hi John,</p>
                                <p class="text-gray-600 mb-4">
                                    We received a request to reset your password. Click the button below
                                    to create a new password. This link will expire in 24 hours.
                                </p>

                                <table class="w-full my-6">
                                    <tr>
                                        <td class="text-center">
                                            <a href="#" class="inline-block bg-red-500 text-white py-4 px-8 rounded-lg font-bold text-lg">
                                                Reset Password
                                            </a>
                                        </td>
                                    </tr>
                                </table>

                                <p class="text-gray-600 mb-4">
                                    If the button doesn't work, copy and paste this link into your browser:
                                </p>
                                <p class="bg-gray-100 p-4 rounded-lg text-sm text-gray-700 break-words mb-4">
                                    https://example.com/reset?token=abc123xyz789
                                </p>

                                <!-- Security Notice -->
                                <table class="w-full bg-yellow-50 border-l-4 border-yellow-400 p-4 rounded-r-lg mb-4">
                                    <tr>
                                        <td class="p-4">
                                            <p class="text-yellow-800 text-sm font-medium mb-1">Security Notice</p>
                                            <p class="text-yellow-700 text-sm">
                                                If you didn't request this password reset, please ignore this email
                                                or contact support if you have concerns.
                                            </p>
                                        </td>
                                    </tr>
                                </table>

                                <p class="text-gray-600">
                                    Thanks,<br>
                                    <span class="font-semibold">The Security Team</span>
                                </p>
                            </td>
                        </tr>

                        <!-- Footer -->
                        <tr>
                            <td class="p-8 bg-gray-50 rounded-b-xl text-center border-t border-gray-200">
                                <p class="text-gray-500 text-sm mb-2">
                                    Need help? <a href="#" class="text-red-500 underline">Contact Support</a>
                                </p>
                                <p class="text-gray-400 text-xs">
                                    &copy; 2024 Company. All rights reserved.
                                </p>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
        """
        output = convert(input_html)

        # Verify structure
        assert "background-color: #f3f4f6" in output  # gray-100
        assert "max-width: 448px" in output  # max-w-md

        # Verify icon container
        assert "background-color: #fee2e2" in output  # red-100
        assert "border-radius: 9999px" in output  # rounded-full
        assert "width: 48px" in output  # w-12
        assert "height: 48px" in output  # h-12

        # Verify CTA button
        assert "background-color: #ef4444" in output  # red-500
        assert "font-size: 18px" in output  # text-lg

        # Verify code block
        assert "background-color: #f3f4f6" in output  # gray-100
        # Note: break-words produces overflow-wrap, not word-break

        # Verify warning
        assert "background-color: #fefce8" in output  # yellow-50
        assert "border-left-width: 4px" in output
        assert "border-color: #facc15" in output  # yellow-400
        assert "color: #854d0e" in output  # yellow-800


class TestMultiSectionTemplates:
    """Tests for templates with multiple complex sections."""

    def test_event_invitation(self) -> None:
        """Test an event invitation email with multiple sections."""
        input_html = """
        <table class="w-full bg-gradient-to-b from-indigo-500 to-purple-600">
            <tr>
                <td class="p-4">
                    <table class="max-w-lg mx-auto">
                        <!-- Event Banner -->
                        <tr>
                            <td class="bg-white rounded-t-2xl overflow-hidden">
                                <img src="event-banner.jpg" class="w-full h-48 object-cover">
                            </td>
                        </tr>

                        <!-- Event Details -->
                        <tr>
                            <td class="bg-white p-8">
                                <p class="text-sm text-indigo-600 font-semibold uppercase tracking-wider mb-2">
                                    You're Invited
                                </p>
                                <h1 class="text-3xl font-extrabold text-gray-900 mb-4">
                                    Annual Tech Conference 2024
                                </h1>

                                <!-- Date/Time/Location -->
                                <table class="w-full mb-6">
                                    <tr>
                                        <td class="py-2">
                                            <table class="w-full">
                                                <tr>
                                                    <td class="w-8 align-top">
                                                        <span class="text-indigo-600 text-xl">&#128197;</span>
                                                    </td>
                                                    <td class="pl-2">
                                                        <p class="text-sm text-gray-500">Date</p>
                                                        <p class="font-semibold text-gray-900">March 15, 2024</p>
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td class="py-2">
                                            <table class="w-full">
                                                <tr>
                                                    <td class="w-8 align-top">
                                                        <span class="text-indigo-600 text-xl">&#128336;</span>
                                                    </td>
                                                    <td class="pl-2">
                                                        <p class="text-sm text-gray-500">Time</p>
                                                        <p class="font-semibold text-gray-900">9:00 AM - 5:00 PM EST</p>
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td class="py-2">
                                            <table class="w-full">
                                                <tr>
                                                    <td class="w-8 align-top">
                                                        <span class="text-indigo-600 text-xl">&#128205;</span>
                                                    </td>
                                                    <td class="pl-2">
                                                        <p class="text-sm text-gray-500">Location</p>
                                                        <p class="font-semibold text-gray-900">Convention Center, NYC</p>
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                </table>

                                <p class="text-gray-600 mb-6">
                                    Join us for a day of inspiring talks, workshops, and networking
                                    with industry leaders. This year's theme: "Building the Future."
                                </p>

                                <!-- RSVP Buttons -->
                                <table class="w-full">
                                    <tr>
                                        <td class="pr-2 w-1/2">
                                            <a href="#" class="block bg-indigo-600 text-white text-center py-3 rounded-lg font-bold">
                                                Accept
                                            </a>
                                        </td>
                                        <td class="pl-2 w-1/2">
                                            <a href="#" class="block bg-gray-200 text-gray-700 text-center py-3 rounded-lg font-bold">
                                                Decline
                                            </a>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>

                        <!-- Speakers Section -->
                        <tr>
                            <td class="bg-gray-50 p-8">
                                <h2 class="text-xl font-bold text-gray-900 mb-4">Featured Speakers</h2>
                                <table class="w-full">
                                    <tr>
                                        <td class="w-1/3 text-center p-2">
                                            <img src="speaker1.jpg" class="w-16 h-16 rounded-full mx-auto mb-2">
                                            <p class="font-semibold text-gray-900 text-sm">Jane Smith</p>
                                            <p class="text-gray-500 text-xs">CEO, TechCorp</p>
                                        </td>
                                        <td class="w-1/3 text-center p-2">
                                            <img src="speaker2.jpg" class="w-16 h-16 rounded-full mx-auto mb-2">
                                            <p class="font-semibold text-gray-900 text-sm">John Doe</p>
                                            <p class="text-gray-500 text-xs">CTO, StartupXYZ</p>
                                        </td>
                                        <td class="w-1/3 text-center p-2">
                                            <img src="speaker3.jpg" class="w-16 h-16 rounded-full mx-auto mb-2">
                                            <p class="font-semibold text-gray-900 text-sm">Alice Johnson</p>
                                            <p class="text-gray-500 text-xs">VP, BigTech</p>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>

                        <!-- Add to Calendar -->
                        <tr>
                            <td class="bg-white p-8 text-center border-t border-gray-200">
                                <p class="text-gray-600 mb-4">Add this event to your calendar:</p>
                                <table class="mx-auto">
                                    <tr>
                                        <td class="px-2">
                                            <a href="#" class="inline-block border border-gray-300 rounded-lg py-2 px-4 text-sm text-gray-700">
                                                Google Calendar
                                            </a>
                                        </td>
                                        <td class="px-2">
                                            <a href="#" class="inline-block border border-gray-300 rounded-lg py-2 px-4 text-sm text-gray-700">
                                                Apple Calendar
                                            </a>
                                        </td>
                                        <td class="px-2">
                                            <a href="#" class="inline-block border border-gray-300 rounded-lg py-2 px-4 text-sm text-gray-700">
                                                Outlook
                                            </a>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>

                        <!-- Footer -->
                        <tr>
                            <td class="bg-indigo-900 rounded-b-2xl p-6 text-center">
                                <p class="text-indigo-300 text-sm">
                                    Questions? Reply to this email or contact events@example.com
                                </p>
                            </td>
                        </tr>
                    </table>
                </td>
            </tr>
        </table>
        """
        output = convert(input_html)

        # Verify event banner
        assert "height: 192px" in output  # h-48
        # Note: object-fit has limited email support

        # Verify event details
        assert "font-size: 30px" in output  # text-3xl
        assert "font-weight: 800" in output  # font-extrabold
        assert "color: #4f46e5" in output  # indigo-600

        # Verify RSVP buttons
        assert "background-color: #4f46e5" in output  # indigo-600
        assert "background-color: #e5e7eb" in output  # gray-200

        # Verify speaker avatars
        assert "border-radius: 9999px" in output  # rounded-full

        # Verify calendar buttons
        assert "border-color: #d1d5db" in output  # gray-300

        # Verify footer
        assert "background-color: #312e81" in output  # indigo-900
        assert "color: #a5b4fc" in output  # indigo-300


class TestLargeContentTemplates:
    """Tests for templates with large amounts of content."""

    def test_many_products_email(self) -> None:
        """Test an email with many product items."""
        products = []
        for i in range(10):
            products.append(f"""
                <tr>
                    <td class="p-4 border-b border-gray-200">
                        <table class="w-full">
                            <tr>
                                <td class="w-20">
                                    <img src="product{i}.jpg" class="w-20 h-20 rounded-lg">
                                </td>
                                <td class="pl-4 align-top">
                                    <p class="font-semibold text-gray-900">Product {i+1}</p>
                                    <p class="text-sm text-gray-500">SKU: PROD-{i+1:04d}</p>
                                    <p class="text-sm text-gray-500">Qty: {i+1}</p>
                                </td>
                                <td class="text-right align-top">
                                    <p class="font-bold text-gray-900">${(i+1) * 19.99:.2f}</p>
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            """)

        input_html = f"""
        <table class="w-full bg-gray-100">
            <tr>
                <td class="p-4">
                    <table class="max-w-2xl mx-auto bg-white rounded-lg shadow-md">
                        <tr>
                            <td class="p-6 bg-green-600 rounded-t-lg">
                                <h1 class="text-2xl font-bold text-white">Your Order Summary</h1>
                                <p class="text-green-200 mt-2">10 items in your order</p>
                            </td>
                        </tr>
                        <tr>
                            <td class="p-6">
                                <table class="w-full">
                                    {''.join(products)}
                                    <tr>
                                        <td class="pt-4 text-right" colspan="2">
                                            <p class="text-gray-500">Subtotal:</p>
                                        </td>
                                        <td class="pt-4 text-right">
                                            <p class="font-bold text-gray-900">$1,099.45</p>
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

        # Verify header
        assert "background-color: #16a34a" in output  # green-600
        assert "color: #bbf7d0" in output  # green-200

        # Verify products are all present
        assert output.count("width: 80px") >= 10  # w-20 for each product
        assert output.count("border-bottom-width: 1px") >= 10
        assert "rounded-lg" not in output  # Classes should be converted
        assert "border-radius: 8px" in output

    def test_long_text_content(self) -> None:
        """Test email with long text paragraphs."""
        input_html = """
        <table class="w-full bg-white">
            <tr>
                <td class="p-8">
                    <table class="max-w-2xl mx-auto">
                        <tr>
                            <td class="pb-8 border-b border-gray-200">
                                <h1 class="text-3xl font-bold text-gray-900 mb-4">Terms of Service Update</h1>
                                <p class="text-gray-500">Effective Date: January 1, 2024</p>
                            </td>
                        </tr>

                        <tr>
                            <td class="py-8 border-b border-gray-200">
                                <h2 class="text-xl font-semibold text-gray-900 mb-4">1. Introduction</h2>
                                <p class="text-gray-600 leading-relaxed mb-4">
                                    Welcome to our service. These Terms of Service ("Terms") govern your use of our
                                    website, products, and services ("Services"). By accessing or using our Services,
                                    you agree to be bound by these Terms. If you disagree with any part of the terms,
                                    then you may not access the Service. This is a legally binding agreement between
                                    you and our company.
                                </p>
                                <p class="text-gray-600 leading-relaxed">
                                    Our Services include all products, features, applications, technologies, and
                                    software that we provide to help you connect with others, share content, and
                                    achieve your goals. These Terms govern your use of all these Services unless
                                    we explicitly state that separate terms apply.
                                </p>
                            </td>
                        </tr>

                        <tr>
                            <td class="py-8 border-b border-gray-200">
                                <h2 class="text-xl font-semibold text-gray-900 mb-4">2. Privacy Policy</h2>
                                <p class="text-gray-600 leading-relaxed mb-4">
                                    Your privacy is important to us. Our Privacy Policy explains how we collect,
                                    use, and protect your personal information when you use our Services. By using
                                    our Services, you agree that we can use such data in accordance with our
                                    privacy policies. We take data protection seriously and implement appropriate
                                    technical and organizational measures.
                                </p>
                                <p class="text-gray-600 leading-relaxed">
                                    We may collect information you provide directly to us, such as when you create
                                    an account, make a purchase, or contact us for support. We also automatically
                                    collect certain information when you use our Services, including your IP address,
                                    browser type, operating system, and usage data.
                                </p>
                            </td>
                        </tr>

                        <tr>
                            <td class="py-8 border-b border-gray-200">
                                <h2 class="text-xl font-semibold text-gray-900 mb-4">3. User Responsibilities</h2>
                                <p class="text-gray-600 leading-relaxed mb-4">
                                    You are responsible for maintaining the confidentiality of your account credentials
                                    and for all activities that occur under your account. You agree to notify us
                                    immediately of any unauthorized use of your account. We reserve the right to
                                    refuse service, terminate accounts, or remove content at our sole discretion.
                                </p>
                                <ul class="text-gray-600 pl-6 mb-4">
                                    <li class="mb-2">You must be at least 18 years old to use our Services</li>
                                    <li class="mb-2">You must provide accurate and complete information</li>
                                    <li class="mb-2">You must not use our Services for illegal purposes</li>
                                    <li class="mb-2">You must not interfere with or disrupt our Services</li>
                                </ul>
                            </td>
                        </tr>

                        <tr>
                            <td class="py-8">
                                <h2 class="text-xl font-semibold text-gray-900 mb-4">4. Contact Us</h2>
                                <p class="text-gray-600 leading-relaxed mb-4">
                                    If you have any questions about these Terms, please contact us at:
                                </p>
                                <table class="bg-gray-50 rounded-lg w-full">
                                    <tr>
                                        <td class="p-4">
                                            <p class="text-gray-900 font-semibold">Legal Department</p>
                                            <p class="text-gray-600">Email: legal@example.com</p>
                                            <p class="text-gray-600">Phone: 1-800-123-4567</p>
                                            <p class="text-gray-600">Address: 123 Legal Street, Suite 100</p>
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

        # Verify headings
        assert "font-size: 30px" in output  # text-3xl
        assert "font-size: 20px" in output  # text-xl
        assert "font-weight: 600" in output  # font-semibold

        # Verify text styling
        assert "line-height: 1.625" in output  # leading-relaxed
        assert "color: #4b5563" in output  # gray-600

        # Verify borders
        assert "border-bottom-width: 1px" in output
        assert "border-color: #e5e7eb" in output  # gray-200

        # Verify contact box
        assert "background-color: #f9fafb" in output  # gray-50
