import pytest
from bit_manipulation.largest_pow_of_two_le_num import largest_pow_of_two_le_num

def test_largest_pow_of_two_le_num():
    assert largest_pow_of_two_le_num(19) == 16  # next lower power of two is 16
    assert largest_pow_of_two_le_num(1) == 1  # next lower power of two is 1
    assert largest_pow_of_two_le_num(9) == 8  # next lower power of two is 8
    assert largest_pow_of_two_le_num(15) == 8  # next lower power of two is 8
    assert largest_pow_of_two_le_num(8) == 8  # next lower power of two is 8

def test_largest_pow_of_two_le_num_invalid_type():
    with pytest.raises(TypeError):
        largest_pow_of_two_le_num(99.9)