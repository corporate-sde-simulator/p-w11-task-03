"""Security utility — input sanitization helpers. Clean file."""
import re

def is_safe_input(value):
    dangerous = ["'", '"', ';', '--', 'DROP', 'DELETE', 'INSERT', 'UPDATE']
    return not any(d.lower() in str(value).lower() for d in dangerous)
