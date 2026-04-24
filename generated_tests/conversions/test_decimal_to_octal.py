import pytest
from conversions.decimal_to_octal import decimal_to_octal

def hex_to_decimal(hex_str):
    hex_digits = "0123456789ABCDEF"
    hex_str = hex_str.upper()
    decimal_value = 0

    for i in range(len(hex_str)):
        char = hex_str[i]
        digit_value = hex_digits.index(char)
        decimal_value = 16 * decimal_value + digit_value

    return decimal_value

def decimal_to_octal_format(decimal):
    octal_without_prefix = decimal_to_octal(decimal)[2:]
    return int(octal_without_prefix) if octal_without_prefix else 0

def hex_to_octal(hex_str):
    decimal_value = hex_to_decimal(hex_str)
    return decimal_to_octal_format(decimal_value)

def test_hex_to_decimal():
    assert hex_to_decimal("FF") == 255
    assert hex_to_decimal("10") == 16
    assert hex_to_decimal("0") == 0
    assert hex_to_decimal("FFF") == 4095

def test_decimal_to_octal():
    assert decimal_to_octal_format(hex_to_decimal("48")) == 110
    assert decimal_to_octal_format(hex_to_decimal("AD")) == 255
    assert decimal_to_octal_format(255) == 377
    assert decimal_to_octal_format(16) == 20
    assert decimal_to_octal_format(0) == 0
    assert decimal_to_octal_format(4095) == 7777

def test_hex_to_octal():
    assert hex_to_octal("FF") == 377
    assert hex_to_octal("10") == 20
    assert hex_to_octal("0") == 0
    assert hex_to_octal("FFF") == 7777