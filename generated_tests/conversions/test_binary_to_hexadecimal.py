import pytest
from conversions.binary_to_hexadecimal import bin_to_hexadecimal

@pytest.mark.parametrize("binary_str, expected_hex", [
    ("0", "0x0"),
    ("1", "0x1"),
    ("10", "0x2"),
    ("1111", "0xf"),
    ("1101010", "0x6a"),
    ("1100", "0xc")
])
def test_bin_to_hexadecimal(binary_str, expected_hex):
    assert bin_to_hexadecimal(binary_str) == expected_hex

@pytest.mark.parametrize("binary_str", ["2", "1234", "11112"])
def test_invalid_binary_input(binary_str):
    with pytest.raises(ValueError):
        bin_to_hexadecimal(binary_str)