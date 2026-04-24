import pytest
from dynamic_programming.rod_cutting import top_down_cut_rod, _enforce_args


def test_top_down_cut_rod_length_1():
    prices = [1]  # Price for piece of length 1
    length = 1
    expected_value = 1
    assert top_down_cut_rod(length, prices) == expected_value, \
        "The maximum obtainable value for a rod of length 1 should be 1."


def test_top_down_cut_rod_length_2():
    prices = [1, 5]  # Prices for lengths 1 and 2
    length = 2
    expected_value = 5  # Best value is to cut it into a single piece of length 2
    assert top_down_cut_rod(length, prices) == expected_value, \
        "The maximum obtainable value for a rod of length 2 should be 5."


def test_top_down_cut_rod_length_3():
    prices = [1, 5, 8]  # Prices for lengths 1, 2, and 3
    length = 3
    expected_value = 8  # Best value is to cut it into a single piece of length 3
    assert top_down_cut_rod(length, prices) == expected_value, \
        "The maximum obtainable value for a rod of length 3 should be 8."


def test_top_down_cut_rod_length_4():
    prices = [1, 5, 8, 9]  # Prices for lengths 1, 2, 3, and 4
    length = 4
    expected_value = 10  # Best value is to cut it into two pieces of length 2
    assert top_down_cut_rod(length, prices) == expected_value, \
        "The maximum obtainable value for a rod of length 4 should be 10."


def test_top_down_cut_rod_length_5():
    prices = [1, 5, 8, 9, 10]  # Prices for lengths 1, 2, 3, 4, and 5
    length = 5
    expected_value = 13  # Best value is to cut it into pieces of lengths 2 and 3
    assert top_down_cut_rod(length, prices) == expected_value, \
        "The maximum obtainable value for a rod of length 5 should be 13."


def test_top_down_cut_rod_length_0():
    prices = [1, 5, 8, 9, 10]  # Prices are irrelevant for length 0
    length = 0
    expected_value = 0  # No value obtainable from a rod of length 0
    assert top_down_cut_rod(length, prices) == expected_value, \
        "The maximum obtainable value for a rod of length 0 should be 0."


def test_top_down_cut_rod_empty_prices():
    prices = []
    length = 5
    with pytest.raises(ValueError):
        _enforce_args(length, prices)


def test_top_down_cut_rod_negative_length():
    prices = [1, 5, 8, 9, 10]  # Prices are irrelevant for negative length
    length = -1
    with pytest.raises(ValueError):
        _enforce_args(length, prices)