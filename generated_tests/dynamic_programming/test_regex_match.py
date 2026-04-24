import pytest
from dynamic_programming.regex_match import recursive_match, dp_match

@pytest.mark.parametrize("text, pattern, expected", [
    ("aa", "*", True),
    ("aa", "a*", True),
    ("aa", "a", False),
    ("cb", "?b", True),
    ("cb", "?a", False),
    ("adceb", "*a*b", True),
    ("acdcb", "a*c?b", False),
    ("", "*", True),
    ("", "", True),
])
def test_recursive_match(text, pattern, expected):
    assert recursive_match(text, pattern) == expected

@pytest.mark.parametrize("text, pattern, expected", [
    ("aa", "*", True),
    ("aa", "a*", True),
    ("aa", "a", False),
    ("cb", "?b", True),
    ("cb", "?a", False),
    ("adceb", "*a*b", True),
    ("acdcb", "a*c?b", False),
    ("", "*", True),
    ("", "", True),
])
def test_dp_match(text, pattern, expected):
    assert dp_match(text, pattern) == expected