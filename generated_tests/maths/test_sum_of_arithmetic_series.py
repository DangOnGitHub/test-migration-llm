import pytest
from maths.sum_of_arithmetic_series import sum_of_series

def test_sum_from_1_to_10():
    assert sum_of_series(1, 1, 10) == 55.0

def test_sum_of_odd_numbers_1_to_19():
    assert sum_of_series(1, 2, 10) == 100.0

def test_a():
    assert sum_of_series(1, 10, 10) == 460.0

def test_b():
    assert sum_of_series(0.1, 0.1, 10) == 5.5

def test_c():
    assert sum_of_series(1, 10, 100) == 49600.0

def test_for_zero_terms():
    assert sum_of_series(1, 100, 0) == 0.0

def test_if_throws_exception_for_negative_number_of_terms():
    with pytest.raises(ValueError) as excinfo:
        sum_of_series(1, 1, -1)
    assert str(excinfo.value) == "num_of_terms nonnegative."

def test_with_single_term():
    assert sum_of_series(123, 5, 1) == 123.0

def test_with_zero_common_diff():
    assert sum_of_series(1, 0, 100) == 100.0