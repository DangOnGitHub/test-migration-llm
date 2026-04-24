import pytest
from maths.perfect_number import perfect

def test_perfect_number():
    true_test_cases = [6, 28, 496, 8128, 33550336]
    false_test_cases = [-6, 0, 1, 9, 123]
    
    for n in true_test_cases:
        assert perfect(n)
    
    for n in false_test_cases:
        assert not perfect(n)