import pytest
from bit_manipulation.numbers_different_signs import different_signs

@pytest.mark.parametrize("num1, num2, expected", [
    # Different signs (positive and negative)
    (2, -1, True),
    (-3, 7, True),

    # Same signs (both positive)
    (10, 20, False),
    (0, 5, False),  # 0 is considered non-negative

    # Same signs (both negative)
    (-5, -8, False),

    # Edge case: Large positive and negative values
    (2**31-1, -2**31, True),

    # Edge case: Same number (positive and negative)
    (-42, -42, False),
    (42, 42, False)
])
def test_different_signs(num1, num2, expected):
    assert different_signs(num1, num2) == expected