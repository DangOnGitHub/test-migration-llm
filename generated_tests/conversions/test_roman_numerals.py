import pytest
from conversions.roman_numerals import roman_to_int

def test_valid_roman_to_integer():
    assert roman_to_int("MCMXCIV") == 1994
    assert roman_to_int("LVIII") == 58
    assert roman_to_int("MDCCCIV") == 1804
    assert roman_to_int("IX") == 9
    assert roman_to_int("IV") == 4
    assert roman_to_int("MMM") == 3000

def test_lowercase_input():
    assert roman_to_int("mcmxciv") == 1994
    assert roman_to_int("lviii") == 58

def test_invalid_roman_numerals():
    with pytest.raises(KeyError):
        roman_to_int("Z")
    with pytest.raises(KeyError):
        roman_to_int("MZI")
    with pytest.raises(KeyError):
        roman_to_int("MMMO")

def test_empty_and_null_input():
    assert roman_to_int("") == 0
    with pytest.raises(TypeError):
        roman_to_int(None)