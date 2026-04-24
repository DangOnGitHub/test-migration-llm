import pytest
from bit_manipulation.highest_set_bit import get_highest_set_bit_position

def test_highest_set_bit():
    assert get_highest_set_bit_position(0) == 0
    assert get_highest_set_bit_position(1) == 1
    assert get_highest_set_bit_position(2) == 2
    assert get_highest_set_bit_position(3) == 2
    assert get_highest_set_bit_position(4) == 3
    assert get_highest_set_bit_position(5) == 3
    assert get_highest_set_bit_position(7) == 3
    assert get_highest_set_bit_position(8) == 4
    assert get_highest_set_bit_position(9) == 4
    assert get_highest_set_bit_position(15) == 4
    assert get_highest_set_bit_position(16) == 5
    assert get_highest_set_bit_position(17) == 5
    assert get_highest_set_bit_position(31) == 5
    assert get_highest_set_bit_position(32) == 6
    assert get_highest_set_bit_position(33) == 6
    assert get_highest_set_bit_position(255) == 8
    assert get_highest_set_bit_position(256) == 9
    assert get_highest_set_bit_position(511) == 9
    assert get_highest_set_bit_position(512) == 10

    with pytest.raises(TypeError, match="Input value must be an 'int' type"):
        get_highest_set_bit_position(-37)