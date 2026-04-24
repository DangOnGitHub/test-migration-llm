import pytest
from strings.is_pangram import (
    is_pangram,
    is_pangram_faster,
    is_pangram_fastest,
)

def test_is_pangram():
    assert is_pangram("The quick brown fox jumps over the lazy dog")
    assert not is_pangram("The quick brown fox jumps over the azy dog")  # L is missing
    assert not is_pangram("+-1234 This string is not alphabetical")
    assert not is_pangram("\u0000/\\ Invalid characters are alright too")

def test_is_pangram_faster():
    assert is_pangram_faster("The quick brown fox jumps over the lazy dog")
    assert not is_pangram_faster("The quick brown fox jumps over the azy dog")  # L is missing
    assert not is_pangram_faster("+-1234 This string is not alphabetical")
    assert not is_pangram_faster("\u0000/\\ Invalid characters are alright too")

def test_is_pangram_fastest():
    assert is_pangram_fastest("The quick brown fox jumps over the lazy dog")
    assert not is_pangram_fastest("The quick brown fox jumps over the azy dog")  # L is missing
    assert not is_pangram_fastest("+-1234 This string is not alphabetical")
    assert not is_pangram_fastest("\u0000/\\ Invalid characters are alright too")

if __name__ == "__main__":
    pytest.main()