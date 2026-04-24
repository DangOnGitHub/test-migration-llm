import pytest
from maths.persistence import multiplicative_persistence, additive_persistence

@pytest.mark.parametrize("input, expected", [
    (0, 0),
    (7, 0),
    (217, 2),
    (39, 3),
    (999, 4),
])
def test_multiplicative_persistence_valid(input, expected):
    assert multiplicative_persistence(input) == expected

@pytest.mark.parametrize("input", [-1, -100, -9999])
def test_multiplicative_persistence_negative(input):
    with pytest.raises(ValueError) as exception_info:
        multiplicative_persistence(input)
    assert str(exception_info.value) == "multiplicative_persistence() does not accept negative values"

@pytest.mark.parametrize("input, expected", [
    (0, 0),
    (5, 0),
    (199, 3),
    (999, 2),
    (1234, 2),
])
def test_additive_persistence_valid(input, expected):
    assert additive_persistence(input) == expected

@pytest.mark.parametrize("input", [-1, -100, -9999])
def test_additive_persistence_negative(input):
    with pytest.raises(ValueError) as exception_info:
        additive_persistence(input)
    assert str(exception_info.value) == "additive_persistence() does not accept negative values"