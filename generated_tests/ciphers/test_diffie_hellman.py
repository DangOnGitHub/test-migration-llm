import pytest
from ciphers.diffie_hellman import DiffieHellman

@pytest.mark.parametrize("base, secret, prime, expected_public_value, expected_shared_secret", [
    (5, 6, 23, 8, 13),
    (2, 5, 13, 6, 2),
])
def test_calculate_public_value(base, secret, prime, expected_public_value, expected_shared_secret):
    dh = DiffieHellman()
    dh.prime = prime
    dh.generator = base
    dh._DiffieHellman__private_key = secret
    assert int(dh.generate_public_key(), 16) == expected_public_value

@pytest.mark.parametrize("base, secret, prime, expected_public_value, expected_shared_secret", [
    (5, 6, 23, 8, 13),
    (2, 5, 13, 6, 2),
])
def test_calculate_shared_secret(base, secret, prime, expected_public_value, expected_shared_secret):
    dh = DiffieHellman()
    dh.prime = prime
    dh.generator = base
    dh._DiffieHellman__private_key = secret
    assert int(DiffieHellman.generate_shared_key_static(hex(secret)[2:], hex(expected_public_value)[2:], group=14), 16) == expected_shared_secret