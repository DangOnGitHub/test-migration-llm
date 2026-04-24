import pytest
from sorts.slowsort import slowsort


def test_slow_sort_empty_list():
    seq = []
    slowsort(seq)
    assert seq == []


def test_slow_sort_single_integer_element_list():
    seq = [5]
    slowsort(seq)
    assert seq == [5]


def test_slow_sort_single_string_element_list():
    seq = ["k"]
    slowsort(seq)
    assert seq == ["k"]


def test_slow_sort_integer_list():
    seq = [8, 84, 53, -683, 953, 64, 2, 202, 98, -10]
    slowsort(seq)
    assert seq == [-683, -10, 2, 8, 53, 64, 84, 98, 202, 953]


def test_slow_sort_duplicate_integer_list():
    seq = [8, 84, 8, -2, 953, 64, 2, 953, 98]
    slowsort(seq)
    assert seq == [-2, 2, 8, 8, 64, 84, 98, 953, 953]


def test_slow_sort_string_list():
    seq = ["g", "d", "a", "b", "f", "c", "e"]
    slowsort(seq)
    assert seq == ["a", "b", "c", "d", "e", "f", "g"]


def test_slow_sort_duplicate_string_list():
    seq = ["g", "d", "a", "g", "b", "f", "d", "c", "e"]
    slowsort(seq)
    assert seq == ["a", "b", "c", "d", "d", "e", "f", "g", "g"]


def test_slow_sort_string_symbol_list():
    seq = ["cbf", "auk", "ó", "(b", "a", ")", "au", "á", "cba", "auk", "(a", "bhy", "cba"]
    slowsort(seq)
    assert seq == ["(a", "(b", ")", "a", "au", "auk", "auk", "bhy", "cba", "cba", "cbf", "á", "ó"]


def test_sort_already_sorted_list():
    seq = [-12, -6, -3, 0, 2, 2, 13, 46]
    slowsort(seq)
    assert seq == [-12, -6, -3, 0, 2, 2, 13, 46]


def test_sort_reversed_sorted_list():
    seq = [46, 13, 2, 2, 0, -3, -6, -12]
    slowsort(seq)
    assert seq == [-12, -6, -3, 0, 2, 2, 13, 46]


def test_sort_all_equal_list():
    seq = [2, 2, 2, 2, 2]
    slowsort(seq)
    assert seq == [2, 2, 2, 2, 2]


def test_sort_mixed_case_strings():
    seq = ["banana", "Apple", "apple", "Banana"]
    slowsort(seq)
    assert seq == ["Apple", "Banana", "apple", "banana"]


def test_slow_sort_custom_objects():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __lt__(self, other):
            return self.age < other.age

        def __eq__(self, other):
            return self.age == other.age and self.name == other.name

    seq = [Person("Alice", 32), Person("Bob", 25), Person("Charlie", 28)]
    expected = [Person("Bob", 25), Person("Charlie", 28), Person("Alice", 32)]
    slowsort(seq)
    assert seq == expected