import pytest
from maths.sieve_of_eratosthenes import prime_sieve

def test_primes_up_to_10():
    expected = [2, 3, 5, 7]
    assert prime_sieve(10) == expected

def test_primes_up_to_30():
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert prime_sieve(30) == expected

def test_primes_up_to_2():
    expected = [2]
    assert prime_sieve(2) == expected

def test_primes_up_to_1():
    assert prime_sieve(1) == []

def test_primes_up_to_0():
    with pytest.raises(ValueError):
        prime_sieve(0)

def test_negative_input():
    with pytest.raises(ValueError):
        prime_sieve(-1)

def test_large_number():
    primes = prime_sieve(1000)
    assert len(primes) == 168
    assert primes[0] == 2
    assert primes[-1] == 997