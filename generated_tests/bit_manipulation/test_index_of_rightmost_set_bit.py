import pytest
from bit_manipulation.index_of_rightmost_set_bit import get_index_of_rightmost_set_bit

def test_get_index_of_rightmost_set_bit():
    assert get_index_of_rightmost_set_bit(40) == 3
    assert get_index_of_rightmost_set_bit(0) == -1
    with pytest.raises(ValueError):
        get_index_of_rightmost_set_bit(-40)