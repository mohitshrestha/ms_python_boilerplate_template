"""Text utilities: formatting, cleaning, and conversions."""

import re

# -------------------------
# Case Conversions
# -------------------------
def snake_to_camel(text: str) -> str:
    """Convert snake_case to camelCase."""
    parts = text.split("_")
    return parts[0] + "".join(x.title() for x in parts[1:])

def camel_to_snake(text: str) -> str:
    """Convert CamelCase to snake_case."""
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def to_upper(text: str) -> str:
    """Convert text to uppercase."""
    return text.upper()

def to_lower(text: str) -> str:
    """Convert text to lowercase."""
    return text.lower()

def to_title(text: str) -> str:
    """Convert text to title case."""
    return text.title()

# -------------------------
# Clean / Remove
# -------------------------
def remove_blanks(text: str) -> str:
    """Remove all spaces."""
    return text.replace(" ", "")

def remove_dashes(text: str) -> str:
    """Remove all dashes."""
    return text.replace("-", "")

def remove_special_chars(text: str) -> str:
    """Remove all non-alphanumeric/underscore characters."""
    return re.sub(r'[^A-Za-z0-9_]', '', text)

# -------------------------
# Format Conversions
# -------------------------
def to_snake(text: str) -> str:
    """Convert to snake_case safely."""
    return camel_to_snake(text).replace("-", "_").replace(" ", "_")

def to_kebab(text: str) -> str:
    """Convert to kebab-case safely."""
    return camel_to_snake(text).replace("_", "-").replace(" ", "-")

def to_reverse(text: str) -> str:
    """Reverse the text."""
    return text[::-1]

# -------------------------
# Example Usage
# -------------------------
if __name__ == "__main__":
    sample = "hello_world-example"
    print("Original:", sample)
    print("CamelCase:", snake_to_camel(sample))
    print("SnakeCase:", to_snake(sample))
    print("KebabCase:", to_kebab(sample))
    print("Reversed:", to_reverse(sample))
    print("Upper:", to_upper(sample))
    print("Lower:", to_lower(sample))
    print("Title:", to_title(sample))
    print("Removed spaces:", remove_blanks(sample))
    print("Removed dashes:", remove_dashes(sample))
    print("Removed special chars:", remove_special_chars(sample))
