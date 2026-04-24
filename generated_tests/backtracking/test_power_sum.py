import pytest
from backtracking.power_sum import solve

def test_number_zero_and_power_zero():
    with pytest.raises(ValueError):
        solve(0, 0)

def test_number_hundred_and_power_two():
    result = solve(100, 2)
    assert result == 3

def test_number_hundred_and_power_three():
    result = solve(100, 3)
    assert result == 1