import pytest
from conversions.octal_to_binary import octal_to_binary

def test_octal_to_binary():
    assert octal_to_binary("5") == "101"
    assert octal_to_binary("11") == "001001"
    assert octal_to_binary("52") == "101010"
    assert octal_to_binary("6") == "110"

def test_octal_to_binary_single_digit():
    assert octal_to_binary("0") == "000"
    assert octal_to_binary("1") == "001"
    assert octal_to_binary("7") == "111"

def test_octal_to_binary_multiple_digits():
    assert octal_to_binary("467") == "100110111"
    assert octal_to_binary("75") == "111101"
    assert octal_to_binary("745") == "111100101"

def test_octal_to_binary_with_zero_padding():
    assert octal_to_binary("412") == "100001010"
    assert octal_to_binary("556") == "101101110"

def test_octal_to_binary_invalid_input():
    with pytest.raises(ValueError, match="Non-octal value was passed to the function"):
        octal_to_binary("Av")
    with pytest.raises(ValueError, match="Non-octal value was passed to the function"):
        octal_to_binary("@#")
    with pytest.raises(ValueError, match="Empty string was passed to the function"):
        octal_to_binary("")