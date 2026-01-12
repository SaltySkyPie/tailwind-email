"""
tailwind-email: Transform HTML with Tailwind CSS classes into email-client-compatible HTML.
"""

from tailwind_email.converter import TailwindEmailConverter, convert

__version__ = "0.1.0"
__all__ = ["convert", "TailwindEmailConverter"]
