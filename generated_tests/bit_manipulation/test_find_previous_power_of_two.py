import pytest
from bit_manipulation.find_previous_power_of_two import find_previous_power_of_two

def test_find_previous_power_of_two():
    assert find_previous_power_of_two(19) == 16  # next lower power of two is 16
    assert find_previous_power_of_two(1) == 1  # next lower power of two is 1
    assert find_previous_power_of_two(9) == 8  # next lower power of two is 8
    assert find_previous_power_of_two(15) == 8  # next lower power of two is 8
    assert find_previous_power_of_two(8) == 8  # next lower power of two is 8

def test_find_previous_power_of_two_invalid_inputs():
    with pytest.raises(ValueError):
        find_previous_power_of_two(-5)
    with pytest.raises(ValueError):
        find_previous_power_of_two(10.5)