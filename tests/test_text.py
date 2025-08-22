import pytest
from shared.src.shared.utils import text

# -------------------------
# Case Conversion Tests
# -------------------------
def test_snake_to_camel():
    assert text.snake_to_camel("hello_world") == "helloWorld"
    assert text.snake_to_camel("") == ""

def test_camel_to_snake():
    assert text.camel_to_snake("HelloWorld") == "hello_world"
    assert text.camel_to_snake("helloWorldExample") == "hello_world_example"

def test_to_upper_lower_title():
    sample = "hello world"
    assert text.to_upper(sample) == "HELLO WORLD"
    assert text.to_lower(sample) == "hello world"
    assert text.to_title(sample) == "Hello World"

# -------------------------
# Cleaning Tests
# -------------------------
def test_remove_blanks():
    assert text.remove_blanks("a b c") == "abc"
    assert text.remove_blanks("") == ""

def test_remove_dashes():
    assert text.remove_dashes("a-b-c") == "abc"

def test_remove_special_chars():
    assert text.remove_special_chars("a!@#b$%^c") == "abc"
    assert text.remove_special_chars("123_abc") == "123_abc"

# -------------------------
# Format Conversions
# -------------------------
def test_to_snake_and_to_kebab():
    assert text.to_snake("HelloWorld-Test") == "hello_world_test"
    assert text.to_kebab("HelloWorld_Test") == "hello-world-test"

def test_to_reverse():
    assert text.to_reverse("abc") == "cba"
    assert text.to_reverse("") == ""
