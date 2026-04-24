import pytest
from conversions.decimal_to_binary import decimal_to_binary_iterative, decimal_to_binary_recursive

@pytest.mark.parametrize("decimal, expected_binary", 
                         [(0, "0b0"), 
                          (1, "0b1"), 
                          (2, "0b10"), 
                          (5, "0b101"), 
                          (10, "0b1010"), 
                          (15, "0b1111"), 
                          (100, "0b1100100")])
def test_decimal_to_binary_iterative(decimal, expected_binary):
    assert decimal_to_binary_iterative(decimal) == expected_binary

@pytest.mark.parametrize("decimal, expected_binary", 
                         [(0, "0b0"), 
                          (1, "0b1"), 
                          (2, "0b10"), 
                          (5, "0b101"), 
                          (10, "0b1010"), 
                          (15, "0b1111"), 
                          (100, "0b1100100")])
def test_decimal_to_binary_recursive(decimal, expected_binary):
    assert decimal_to_binary_recursive(decimal) == expected_binary