import pytest
from maths.binomial_coefficient import binomial_coefficient

def test_binomial_coefficient():
    assert binomial_coefficient(20, 2) == 190
    assert binomial_coefficient(12, 5) == 792
    assert binomial_coefficient(9, 3) == 84
    assert binomial_coefficient(17, 17) == 1
