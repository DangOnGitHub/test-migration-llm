import pytest
from bit_manipulation.excess_3_code import excess_3_code

def xs3_to_binary(xs3):
    binary = 0
    multiplier = 1
    while xs3 > 0:
        digit = (xs3 & 0xF) - 3
        binary += digit * multiplier
        multiplier *= 10
        xs3 >>= 4
    return binary

def binary_to_xs3(binary):
    xs3 = 0
    shift = 0
    while binary > 0:
        digit = (binary % 10) + 3
        xs3 |= (digit << (shift * 4))
        binary //= 10
        shift += 1
    return xs3

def test_xs3_to_binary():
    assert xs3_to_binary(0x4567) == 1234

def test_binary_to_xs3():
    assert binary_to_xs3(1234) == 0x4567

def test_xs3_to_binary_zero():
    assert xs3_to_binary(0x0) == 0

def test_binary_to_xs3_zero():
    assert binary_to_xs3(0) == 0x0

def test_xs3_to_binary_single_digit():
    assert xs3_to_binary(0x5) == 2

def test_binary_to_xs3_single_digit():
    assert binary_to_xs3(2) == 0x5