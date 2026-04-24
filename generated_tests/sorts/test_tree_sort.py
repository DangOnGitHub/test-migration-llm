import pytest
from sorts.tree_sort import tree_sort

def test_tree_sort_empty_array():
    input_array = []
    expected_output = ()
    assert tree_sort(input_array) == expected_output

def test_tree_sort_single_string_element():
    input_array = ["Test"]
    expected_output = ("Test",)
    assert tree_sort(input_array) == expected_output

def test_tree_sort_string_array():
    input_array = ["F6w9", "l1qz", "dIxH", "larj", "kRzy", "vnNH", "3ftM", "hc4n", "C5Qi", "btGF"]
    expected_output = ("3ftM", "C5Qi", "F6w9", "btGF", "dIxH", "hc4n", "kRzy", "l1qz", "larj", "vnNH")
    assert tree_sort(input_array) == expected_output

def test_tree_sort_integer_array():
    input_array = [-97, -44, -4, -85, -92, 74, 79, -26, 76, -5]
    expected_output = (-97, -92, -85, -44, -26, -5, -4, 74, 76, 79)
    assert tree_sort(input_array) == expected_output

def test_tree_sort_double_array():
    input_array = [0.8047485045, 0.4493112337, 0.8298433723, 0.2691406748, 0.2482782839, 0.5976243420, 0.6746235284, 0.0552623569, 0.3515624123, 0.0536747336]
    expected_output = (0.0536747336, 0.0552623569, 0.2482782839, 0.2691406748, 0.3515624123, 0.4493112337, 0.5976243420, 0.6746235284, 0.8047485045, 0.8298433723)
    assert tree_sort(input_array) == expected_output