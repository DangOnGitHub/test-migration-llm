import pytest
from bit_manipulation.reverse_bits import reverse_bit

@pytest.mark.parametrize("input_value, expected", [
    (0, 0),
    (2550136831, -1),  # Equivalent of the Java -1 in reverse in Python (32-bit all bits 1 excluding sign).
    (43261596, 964176192),
    (0x7FFFFFFF, -2),  # Maximum positive value for 32-bit integer
    (0x80000000, 1),   # Minimum value (all bits 1 except the sign bit)
    (1, 0x80000000),   # Single bit set (2^0 = 1)
    (0xAAAAAAAA, 0x55555555),  # Alternating bits 0b101010...10
])
def test_reverse_bit(input_value, expected):
    assert reverse_bit(input_value) == expected

def test_reverse_bit_exceptions():
    with pytest.raises(ValueError):
        reverse_bit(-1)
    with pytest.raises(TypeError):
        reverse_bit(1.1)
    with pytest.raises(TypeError):
        reverse_bit("0")