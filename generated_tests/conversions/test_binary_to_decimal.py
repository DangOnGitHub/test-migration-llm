import pytest
from conversions.binary_to_decimal import bin_to_decimal

# Test converting binary to decimal
def test_bin_to_decimal():
    assert bin_to_decimal("0") == 0
    assert bin_to_decimal("1") == 1
    assert bin_to_decimal("101") == 5
    assert bin_to_decimal("111111") == 63
    assert bin_to_decimal("1000000000") == 512

# Test converting negative binary numbers
def test_negative_bin_to_decimal():
    assert bin_to_decimal("-1") == -1
    assert bin_to_decimal("-101010") == -42

# Test converting binary numbers with large values
def test_large_bin_to_decimal():
    assert bin_to_decimal("1000000000000000000") == 262144
    assert bin_to_decimal("1111111111111111111") == 524287

@pytest.mark.parametrize("bin_string", ["2", "1234", "11112", "101021", "a", ""])
def test_not_correct_binary_input(bin_string):
    with pytest.raises(ValueError):
        bin_to_decimal(bin_string)