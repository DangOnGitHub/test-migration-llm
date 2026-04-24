import pytest
from maths.collatz_sequence import collatz_sequence

def test_next_number_from_even_number():
    generator = collatz_sequence(50)
    next(generator)
    assert next(generator) == 25

def test_next_number_from_odd_number():
    generator = collatz_sequence(51)
    next(generator)
    assert next(generator) == 154

def test_collatz_conjecture():
    expected = (35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1)
    result = tuple(collatz_sequence(35))
    assert result == expected

def test_sequence_of_not_natural_first_number():
    with pytest.raises(Exception, match='Sequence only defined for positive integers'):
        tuple(collatz_sequence(0))
    with pytest.raises(Exception, match='Sequence only defined for positive integers'):
        tuple(collatz_sequence(-1))