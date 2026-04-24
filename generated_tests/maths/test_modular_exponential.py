import pytest
from maths.modular_exponential import modular_exponential

def test_small_numbers():
    assert modular_exponential(2, 10, 10000) == 1024, "2^10 mod 10000 should be 1024"
    assert modular_exponential(3, 4, 1000) == 81, "3^4 mod 1000 should be 81"

def test_with_modulo():
    assert modular_exponential(2, 10, 1000) == 24, "2^10 mod 1000 should be 24"
    assert modular_exponential(10, 5, 10) == 0, "10^5 mod 10 should be 0"

def test_base_cases():
    assert modular_exponential(2, 0, 1000) == 1, "Any number raised to the power 0 mod anything should be 1"
    assert modular_exponential(0, 10, 1000) == 0, "0 raised to any power should be 0"
    assert modular_exponential(0, 0, 1000) == 1, "0^0 is usually considered as 1"

def test_negative_base():
    assert modular_exponential(-5, 10, 1000000007) == 9765625, "-5^10 mod 1000000007 should be 9765625"

def test_negative_exponent():
    with pytest.raises(ValueError):
        modular_exponential(2, -5, 1000)

def test_invalid_modulus():
    with pytest.raises(ValueError):
        modular_exponential(2, 5, 0)