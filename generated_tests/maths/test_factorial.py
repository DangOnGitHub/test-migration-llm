import pytest
from maths.factorial import factorial

EXCEPTION_MESSAGE_NEGATIVE = "factorial() not defined for negative values"
EXCEPTION_MESSAGE_NON_INTEGRAL = "factorial() only accepts integral values"

def test_when_invalid_input_provided_should_throw_exception():
    with pytest.raises(ValueError, match=EXCEPTION_MESSAGE_NEGATIVE):
        factorial(-1)
    with pytest.raises(ValueError, match=EXCEPTION_MESSAGE_NON_INTEGRAL):
        factorial(0.1)

def test_correct_factorial_calculation():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800