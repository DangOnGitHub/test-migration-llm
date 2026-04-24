import pytest
from dynamic_programming.wildcard_matching import is_match

def test_matching_pattern():
    assert is_match("aa", "a*") is True
    assert is_match("adceb", "*a*b") is True

def test_non_matching_pattern():
    assert is_match("cb", "?a") is False
    assert is_match("acdcb", "a*c?b") is False
    assert is_match("mississippi", "m*issi*iss?*i") is False

def test_empty_pattern():
    assert is_match("", "") is True
    assert is_match("abc", "") is False

if __name__ == "__main__":
    pytest.main()