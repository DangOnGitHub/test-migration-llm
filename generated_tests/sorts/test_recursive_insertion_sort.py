import pytest
from sorts.recursive_insertion_sort import rec_insertion_sort

def test_empty_array():
    array = []
    rec_insertion_sort(array, len(array))
    assert array == []

def test_single_value_array():
    array = [7]
    rec_insertion_sort(array, len(array))
    assert array == [7]

def test_integer_array():
    array = [49, 4, 36, 9, 144, 1]
    rec_insertion_sort(array, len(array))
    assert array == [1, 4, 9, 36, 49, 144]

def test_negative_values_array():
    array = [49, -36, -144, -49, 1, 9]
    rec_insertion_sort(array, len(array))
    assert array == [-144, -49, -36, 1, 9, 49]

def test_with_duplicates():
    array = [36, 1, 49, 1, 4, 9]
    rec_insertion_sort(array, len(array))
    assert array == [1, 1, 4, 9, 36, 49]

def test_with_string_array():
    array = ["c", "a", "e", "b", "d"]
    rec_insertion_sort(array, len(array))
    assert array == ["a", "b", "c", "d", "e"]

def test_sorted_array():
    array = [-12, -6, -3, 0, 2, 2, 13, 46]
    rec_insertion_sort(array, len(array))
    assert array == [-12, -6, -3, 0, 2, 2, 13, 46]

def test_reversed_sorted_array():
    array = [46, 13, 2, 2, 0, -3, -6, -12]
    rec_insertion_sort(array, len(array))
    assert array == [-12, -6, -3, 0, 2, 2, 13, 46]

def test_all_equal_array():
    array = [2, 2, 2, 2, 2]
    rec_insertion_sort(array, len(array))
    assert array == [2, 2, 2, 2, 2]

def test_mixed_case_strings():
    array = ["banana", "Apple", "apple", "Banana"]
    rec_insertion_sort(array, len(array))
    assert array == ["Apple", "Banana", "apple", "banana"]

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

def test_sort_custom_objects():
    array = [Person("Alice", 32), Person("Bob", 25), Person("Charlie", 28)]
    rec_insertion_sort(array, len(array))
    expected = [Person("Bob", 25), Person("Charlie", 28), Person("Alice", 32)]
    assert array == expected