import pytest
from conversions.decimal_to_any import decimal_to_any

@pytest.mark.parametrize("decimal, base, expected", [
    (0, 2, '0'),
    (0, 16, '0'),
    (0, 36, '0'),
    (10, 2, '1010'),
    (255, 16, 'FF'),
    (100, 8, '144'),
    (42, 2, '101010'),
    (1234, 16, '4D2'),
    (1234, 36, 'YA')
])
def test_convert_to_any_base(decimal, base, expected):
    assert decimal_to_any(decimal, base) == expected

def test_base_out_of_range():
    with pytest.raises(ValueError):
        decimal_to_any(10, 1)
    with pytest.raises(ValueError):
        decimal_to_any(10, 37)