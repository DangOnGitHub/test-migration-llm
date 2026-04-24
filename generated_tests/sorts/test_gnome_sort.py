import pytest
from sorts.gnome_sort import gnome_sort

def test_gnome_sort_empty_array():
    input_array = []
    output_array = gnome_sort(input_array)
    assert output_array == []

def test_single_integer_array():
    input_array = [4]
    expected_output = [4]
    output_array = gnome_sort(input_array)
    assert output_array == expected_output

def test_gnome_sort_non_duplicate_integer_array():
    input_array = [6, 3, 87, 99, 27, 4]
    expected_output = [3, 4, 6, 27, 87, 99]
    output_array = gnome_sort(input_array)
    assert output_array == expected_output

def test_gnome_sort_duplicate_integer_array():
    input_array = [6, 3, 87, 3, 99, 27, 4, 27]
    expected_output = [3, 3, 4, 6, 27, 27, 87, 99]
    output_array = gnome_sort(input_array)
    assert output_array == expected_output

def test_gnome_sort_negative_duplicate_integer_array():
    input_array = [6, 3, -87, 3, 99, -27, 4, -27]
    expected_output = [-87, -27, -27, 3, 3, 4, 6, 99]
    output_array = gnome_sort(input_array)
    assert output_array == expected_output

def test_single_string_array():
    input_array = ["b"]
    expected_output = ["b"]
    output_array = gnome_sort(input_array)
    assert output_array == expected_output

def test_gnome_sort_non_duplicate_string_array():
    input_array = ["He", "A", "bc", "lo", "n", "bcp", "mhp", "d"]
    expected_output = ["A", "He", "bc", "bcp", "d", "lo", "mhp", "n"]
    output_array = gnome_sort(input_array)
    assert output_array == expected_output

def test_gnome_sort_duplicate_string_array():
    input_array = ["He", "A", "bc", "lo", "n", "bcp", "mhp", "bcp"]
    expected_output = ["A", "He", "bc", "bcp", "bcp", "lo", "mhp", "n"]
    output_array = gnome_sort(input_array)
    assert output_array == expected_output

def test_sort_already_sorted_array():
    input_array = [-12, -6, -3, 0, 2, 2, 13, 46]
    expected_output = [-12, -6, -3, 0, 2, 2, 13, 46]
    output_array = gnome_sort(input_array)
    assert output_array == expected_output

def test_sort_reversed_sorted_array():
    input_array = [46, 13, 2, 2, 0, -3, -6, -12]
    expected_output = [-12, -6, -3, 0, 2, 2, 13, 46]
    output_array = gnome_sort(input_array)
    assert output_array == expected_output

def test_sort_all_equal_array():
    input_array = [2, 2, 2, 2, 2]
    expected_output = [2, 2, 2, 2, 2]
    output_array = gnome_sort(input_array)
    assert output_array == expected_output

def test_sort_mixed_case_strings():
    input_array = ["banana", "Apple", "apple", "Banana"]
    expected_output = ["Apple", "Banana", "apple", "banana"]
    output_array = gnome_sort(input_array)
    assert output_array == expected_output

# Custom Comparable class for testing in Python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

def test_sort_custom_objects():
    input_array = [
        Person("Alice", 32),
        Person("Bob", 25),
        Person("Charlie", 28),
    ]
    expected_output = [
        Person("Bob", 25),
        Person("Charlie", 28),
        Person("Alice", 32),
    ]
    output_array = gnome_sort(input_array)
    assert output_array == expected_output