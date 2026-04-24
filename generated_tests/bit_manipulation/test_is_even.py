import pytest
from bit_manipulation.is_even import is_even

def test_is_even():
    assert is_even(0) == True
    assert is_even(2) == True
    assert is_even(-12) == True
    assert is_even(21) == False
    assert is_even(-1) == False

if __name__ == "__main__":
    pytest.main()