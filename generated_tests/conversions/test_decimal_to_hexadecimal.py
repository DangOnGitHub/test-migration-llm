import pytest
from conversions.decimal_to_hexadecimal import decimal_to_hexadecimal

@pytest.mark.parametrize("decimal, expected_hex", [
    (0, "0x0"),
    (1, "0x1"),
    (10, "0xa"),
    (15, "0xf"),
    (16, "0x10"),
    (255, "0xff"),
    (190, "0xbe"),
    (1800, "0x708")
])
def test_decimal_to_hexadecimal(decimal, expected_hex):
    assert decimal_to_hexadecimal(decimal) == expected_hex