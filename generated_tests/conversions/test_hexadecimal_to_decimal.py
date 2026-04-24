import pytest
from conversions.hexadecimal_to_decimal import hex_to_decimal

@pytest.mark.parametrize("hex_input, expected_decimal", [
    ("A1", 161),  # Simple case with two characters
    ("1AC", 428),  # Mixed-case input
    ("0", 0),  # Single zero
    ("F", 15),  # Single digit
    ("10", 16),  # Power of 16
    ("FFFF", 65535),  # Max 4-character hex
    ("7FFFFFFF", 2147483647)  # Max positive int value
])
def test_valid_hex_to_decimal(hex_input, expected_decimal):
    assert hex_to_decimal(hex_input) == expected_decimal

@pytest.mark.parametrize("invalid_hex", [
    "G",  # Invalid character
    "1Z",  # Mixed invalid input
    "123G",  # Valid prefix with invalid character
    "#$%"  # Non-hexadecimal symbols
])
def test_invalid_hex_to_decimal(invalid_hex):
    with pytest.raises(ValueError):
        hex_to_decimal(invalid_hex)