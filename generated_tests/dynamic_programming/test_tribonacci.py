import pytest
from dynamic_programming.tribonacci import tribonacci

def test_known_values():
    assert tribonacci(1) == [0], "The 0th Tribonacci should be [0]."
    assert tribonacci(2) == [0, 0], "The 1st Tribonacci should be [0, 0]."
    assert tribonacci(3) == [0, 0, 1], "The 2nd Tribonacci should be [0, 0, 1]."
    assert tribonacci(4) == [0, 0, 1, 1], "The 3rd Tribonacci should be [0, 0, 1, 1]."
    assert tribonacci(5) == [0, 0, 1, 1, 2], "The 4th Tribonacci should be [0, 0, 1, 1, 2]."
    assert tribonacci(6) == [0, 0, 1, 1, 2, 4], "The 5th Tribonacci should be [0, 0, 1, 1, 2, 4]."