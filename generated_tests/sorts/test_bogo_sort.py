import pytest
from sorts.bogo_sort import bogo_sort

def test_bogo_sort_empty_array():
    input_array = []
    output_array = bogo_sort(input_array.copy())
    expected_output = []
    assert output_array == expected_output

def test_bogo_sort_single_integer_array():
    input_array = [4]
    output_array = bogo_sort(input_array.copy())
    expected_output = [4]
    assert output_array == expected_output

def test_bogo_sort_single_string_array():
    input_array = ["s"]
    output_array = bogo_sort(input_array.copy())
    expected_output = ["s"]
    assert output_array == expected_output

def test_bogo_sort_non_duplicate_integer_array():
    input_array = [6, -1, 99, 27, -15, 23, -36]
    output_array = bogo_sort(input_array.copy())
    expected_output = sorted(input_array)
    assert output_array == expected_output

def test_bogo_sort_duplicate_integer_array():
    input_array = [6, -1, 27, -15, 23, 27, -36, 23]
    output_array = bogo_sort(input_array.copy())
    expected_output = sorted(input_array)
    assert output_array == expected_output

def test_bogo_sort_non_duplicate_string_array():
    input_array = ["s", "b", "k", "a", "d", "c", "h"]
    output_array = bogo_sort(input_array.copy())
    expected_output = sorted(input_array)
    assert output_array == expected_output

def test_bogo_sort_duplicate_string_array():
    input_array = ["s", "b", "d", "a", "d", "c", "h", "b"]
    output_array = bogo_sort(input_array.copy())
    expected_output = sorted(input_array)
    assert output_array == expected_output

def test_bogo_sort_already_sorted_array():
    input_array = [-12, -6, -3, 0, 2, 2, 13, 46]
    output_array = bogo_sort(input_array.copy())
    expected_output = input_array.copy()
    assert output_array == expected_output

def test_bogo_sort_reversed_sorted_array():
    input_array = [46, 13, 2, 2, 0, -3, -6, -12]
    output_array = bogo_sort(input_array.copy())
    expected_output = sorted(input_array)
    assert output_array == expected_output

def test_bogo_sort_all_equal_array():
    input_array = [2, 2, 2, 2, 2]
    output_array = bogo_sort(input_array.copy())
    expected_output = [2, 2, 2, 2, 2]
    assert output_array == expected_output

def test_bogo_sort_mixed_case_strings():
    input_array = ["banana", "Apple", "apple", "Banana"]
    output_array = bogo_sort(input_array.copy())
    expected_output = sorted(input_array)
    assert output_array == expected_output

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

    def __lt__(self, other):
        return self.age < other.age

def test_bogo_sort_custom_objects():
    input_array = [Person("Alice", 32), Person("Bob", 25), Person("Charlie", 28)]
    output_array = bogo_sort(input_array.copy())
    expected_output = sorted(input_array)
    assert output_array == expected_output