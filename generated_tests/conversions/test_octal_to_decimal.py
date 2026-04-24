import pytest
from conversions.octal_to_decimal import oct_to_decimal

@pytest.mark.parametrize("input_octal, expected_hex", [
    ("0", 0), 
    ("7", 7), 
    ("10", 8), 
    ("17", 15), 
    ("20", 16), 
    ("777", 511), 
    ("1234", 668), 
    ("752", 490), 
    ("536", 350)
])
def test_correct_inputs(input_octal, expected_hex):
    decimal = oct_to_decimal(input_octal)
    assert decimal == expected_hex

@pytest.mark.parametrize("input_octal, expected_message", [
    ("", "Empty string was passed to the function"),
    ("8", "Non-octal value was passed to the function"),
    ("19", "Non-octal value was passed to the function")
])
def test_incorrect_inputs(input_octal, expected_message):
    with pytest.raises(ValueError) as excinfo:
        oct_to_decimal(input_octal)
    assert str(excinfo.value) == expected_message