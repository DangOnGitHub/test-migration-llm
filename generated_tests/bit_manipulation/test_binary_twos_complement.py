import pytest
from bit_manipulation.binary_twos_complement import twos_complement


def test_twos_complement():
    # Test for all zeroes
    assert twos_complement(0) == '0b0'

    # Test for all ones (invalid for our python implementation as it throws ValueError)
    with pytest.raises(ValueError):
        twos_complement(1)

    # Test for mixed bits
    assert twos_complement(-1) == '0b11'
    assert twos_complement(-5) == '0b1011'
    assert twos_complement(-17) == '0b101111'
    assert twos_complement(-207) == '0b100110001'

    # Test for invalid positive input
    with pytest.raises(ValueError):
        twos_complement(5)

    # Test for invalid non-integer inputs
    with pytest.raises(TypeError):
        twos_complement('abc')

    # Test for negative single bit
    assert twos_complement(-1) == '0b11'

    # Edge case: test for zero
    assert twos_complement(0) == '0b0'