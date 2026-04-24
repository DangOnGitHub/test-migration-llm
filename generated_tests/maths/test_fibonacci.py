import pytest
from maths.fibonacci import fib_matrix_np

def test_fibonacci_value_at_zero():
    assert fib_matrix_np(0) == 0

def test_fibonacci_value_at_one():
    assert fib_matrix_np(1) == 1

def test_fibonacci_value_at_two():
    assert fib_matrix_np(2) == 1

def test_fibonacci_recurrence_relation():
    for i in range(100):
        assert fib_matrix_np(i + 2) == fib_matrix_np(i + 1) + fib_matrix_np(i)

def test_fibonacci_negative_input():
    with pytest.raises(ValueError):
        fib_matrix_np(-1)