import pytest
from strings.palindrome import is_palindrome, is_palindrome_recursive, is_palindrome_traversal, is_palindrome_slice

@pytest.mark.parametrize("input, expected", [
    (None, True),
    ("", True),
    ("aba", True),
    ("123321", True),
    ("kayak", True),
    ("abb", False),
    ("abc", False),
    ("abc123", False),
    ("kayaks", False)
])
def test_palindrome(input, expected):
    if input is None:
        assert True == expected  # skip for None as Python functions assume non-null input
    else:
        assert is_palindrome(input) == expected
        assert is_palindrome_recursive(input) == expected
        assert is_palindrome_traversal(input) == expected
        assert is_palindrome_slice(input) == expected