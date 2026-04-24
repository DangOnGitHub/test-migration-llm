import random
import string

from sorts.bubble_sort import bubble_sort_iterative
from sorts.bubble_sort import bubble_sort_recursive


def test_bubble_sort_empty_array():
    assert bubble_sort_iterative([]) == []
    assert bubble_sort_recursive([]) == []


def test_bubble_sort_single_integer_element_array():
    assert bubble_sort_iterative([4]) == [4]
    assert bubble_sort_recursive([4]) == [4]


def test_bubble_sort_single_string_element_array():
    assert bubble_sort_iterative(["s"]) == ["s"]
    assert bubble_sort_recursive(["s"]) == ["s"]


def test_bubble_sort_integer_array():
    input_array = [4, 23, -6, 78, 1, 54, 23, -6, -231, 9, 12]
    expected_output = [-231, -6, -6, 1, 4, 9, 12, 23, 23, 54, 78]
    assert bubble_sort_iterative(input_array[:]) == expected_output
    assert bubble_sort_recursive(input_array[:]) == expected_output


def test_bubble_sort_string_array():
    input_array = ["cbf", "auk", "ó", "(b", "a", ")", "au", "á", "cba", "auk", "(a", "bhy", "cba"]
    expected_output = ["(a", "(b", ")", "a", "au", "auk", "auk", "bhy", "cba", "cba", "cbf", "á", "ó"]
    assert bubble_sort_iterative(input_array[:]) == expected_output
    assert bubble_sort_recursive(input_array[:]) == expected_output


def test_bubble_sort_already_sorted_array():
    input_array = [-12, -6, -3, 0, 2, 2, 13, 46]
    expected_output = [-12, -6, -3, 0, 2, 2, 13, 46]
    assert bubble_sort_iterative(input_array[:]) == expected_output
    assert bubble_sort_recursive(input_array[:]) == expected_output


def test_bubble_sort_reversed_sorted_array():
    input_array = [46, 13, 2, 2, 0, -3, -6, -12]
    expected_output = [-12, -6, -3, 0, 2, 2, 13, 46]
    assert bubble_sort_iterative(input_array[:]) == expected_output
    assert bubble_sort_recursive(input_array[:]) == expected_output


def test_bubble_sort_all_equal_array():
    input_array = [2, 2, 2, 2, 2]
    expected_output = [2, 2, 2, 2, 2]
    assert bubble_sort_iterative(input_array[:]) == expected_output
    assert bubble_sort_recursive(input_array[:]) == expected_output


def test_bubble_sort_mixed_case_strings():
    input_array = ["banana", "Apple", "apple", "Banana"]
    expected_output = ["Apple", "Banana", "apple", "banana"]
    assert bubble_sort_iterative(input_array[:]) == expected_output
    assert bubble_sort_recursive(input_array[:]) == expected_output


def test_bubble_sort_custom_objects():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __eq__(self, other):
            return self.age == other.age and self.name == other.name

        def __lt__(self, other):
            return self.age < other.age

    input_array = [Person("Alice", 32), Person("Bob", 25), Person("Charlie", 28)]
    expected_output = [Person("Bob", 25), Person("Charlie", 28), Person("Alice", 32)]
    assert bubble_sort_iterative(input_array[:]) == expected_output
    assert bubble_sort_recursive(input_array[:]) == expected_output