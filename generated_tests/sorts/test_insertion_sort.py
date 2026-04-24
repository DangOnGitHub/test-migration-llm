import random
import string
from sorts.insertion_sort import insertion_sort

def test_insertion_sort_empty_list():
    array = []
    sorted_array = insertion_sort(array)
    expected = []
    assert sorted_array == expected
    assert is_sorted(sorted_array)

def test_insertion_sort_single_value_list():
    array = [7]
    sorted_array = insertion_sort(array)
    expected = [7]
    assert sorted_array == expected
    assert is_sorted(sorted_array)

def test_insertion_sort_integer_list():
    array = [49, 4, 36, 9, 144, 1]
    sorted_array = insertion_sort(array)
    expected = [1, 4, 9, 36, 49, 144]
    assert sorted_array == expected
    assert is_sorted(sorted_array)

def test_insertion_sort_with_negative_values():
    array = [49, -36, -144, -49, 1, 9]
    sorted_array = insertion_sort(array)
    expected = [-144, -49, -36, 1, 9, 49]
    assert sorted_array == expected
    assert is_sorted(sorted_array)

def test_insertion_sort_with_duplicates():
    array = [36, 1, 49, 1, 4, 9]
    sorted_array = insertion_sort(array)
    expected = [1, 1, 4, 9, 36, 49]
    assert sorted_array == expected
    assert is_sorted(sorted_array)

def test_insertion_sort_with_string_list():
    array = ["c", "a", "e", "b", "d"]
    sorted_array = insertion_sort(array)
    expected = ["a", "b", "c", "d", "e"]
    assert sorted_array == expected
    assert is_sorted(sorted_array)

def test_insertion_sort_with_random_list():
    random_size = random.randint(1, 10_000)
    array = random.sample(range(-10_000, 10_000), random_size)
    sorted_array = insertion_sort(array)
    assert is_sorted(sorted_array)

def test_insertion_sort_already_sorted_list():
    input_array = [-12, -6, -3, 0, 2, 2, 13, 46]
    sorted_array = insertion_sort(input_array)
    expected_output = [-12, -6, -3, 0, 2, 2, 13, 46]
    assert sorted_array == expected_output

def test_insertion_sort_reversed_sorted_list():
    input_array = [46, 13, 2, 2, 0, -3, -6, -12]
    sorted_array = insertion_sort(input_array)
    expected_output = [-12, -6, -3, 0, 2, 2, 13, 46]
    assert sorted_array == expected_output

def test_insertion_sort_all_equal_list():
    input_array = [2, 2, 2, 2, 2]
    sorted_array = insertion_sort(input_array)
    expected_output = [2, 2, 2, 2, 2]
    assert sorted_array == expected_output

def test_insertion_sort_mixed_case_strings():
    input_array = ["banana", "Apple", "apple", "Banana"]
    expected_output = ["Apple", "Banana", "apple", "banana"]
    sorted_array = insertion_sort(input_array)
    assert sorted_array == expected_output

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

def test_insertion_sort_custom_objects():
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
    sorted_array = insertion_sort(input_array)
    assert sorted_array == expected_output

def is_sorted(collection):
    return all(collection[i] <= collection[i + 1] for i in range(len(collection) - 1))
