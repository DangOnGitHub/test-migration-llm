import pytest
from maths.is_int_palindrome import is_int_palindrome

def test_numbers_are_palindromes():
    assert is_int_palindrome(0) is True
    assert is_int_palindrome(1) is True
    assert is_int_palindrome(2332) is True
    assert is_int_palindrome(12321) is True

def test_numbers_are_not_palindromes():
    assert is_int_palindrome(12) is False
    assert is_int_palindrome(990) is False
    assert is_int_palindrome(1234) is False

def test_negative_input():
    with pytest.raises(ValueError) as excinfo:
        is_int_palindrome(-1)
    assert str(excinfo.value) == "Input parameter must not be negative!"