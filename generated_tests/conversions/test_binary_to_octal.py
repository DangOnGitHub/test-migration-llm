import pytest
from conversions.binary_to_octal import bin_to_octal

@pytest.mark.parametrize("binary, expected_octal", [
    ("0", "0"),
    ("1", "1"),
    ("10", "2"),
    ("111", "7"),
    ("1000", "10"),
    ("1111", "17"),
    ("110101", "65"),
    ("1010101", "125"),
    ("110110011", "663"),
    ("111111111", "777"),
    ("10010110", "226"),
    ("1011101", "135")
])
def test_bin_to_octal(binary, expected_octal):
    assert bin_to_octal(binary) == expected_octal

def test_incorrect_input():
    with pytest.raises(ValueError, match="Non-binary value was passed to the function"):
        bin_to_octal("1234")
    with pytest.raises(ValueError, match="Non-binary value was passed to the function"):
        bin_to_octal("102")
    with pytest.raises(ValueError, match="Non-binary value was passed to the function"):
        bin_to_octal("-1010")