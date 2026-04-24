import pytest
from dynamic_programming.min_distance_up_bottom import min_distance_up_bottom

@pytest.mark.parametrize(
    "str1, str2, expected",
    [
        ("", "", 0),
        ("abc", "", 3),
        ("", "abcd", 4),
        ("same", "same", 0),
        ("a", "b", 1),
        ("abc", "abd", 1),
    ],
)
def test_min_distance_up_bottom(str1, str2, expected):
    assert min_distance_up_bottom(str1, str2) == expected

def test_edit_distance_both_empty_strings():
    assert min_distance_up_bottom("", "") == 0

def test_edit_distance_one_empty_string():
    assert min_distance_up_bottom("", "hello") == 5
    assert min_distance_up_bottom("worldly", "") == 7

def test_edit_distance_equal_strings():
    assert min_distance_up_bottom("test", "test") == 0
    assert min_distance_up_bottom("abc", "abc") == 0

def test_edit_distance_one_character_difference():
    assert min_distance_up_bottom("cat", "bat") == 1
    assert min_distance_up_bottom("cat", "cats") == 1
    assert min_distance_up_bottom("cats", "cat") == 1

def test_edit_distance_general_cases():
    assert min_distance_up_bottom("kitten", "sitting") == 3
    assert min_distance_up_bottom("flaw", "lawn") == 2
    assert min_distance_up_bottom("intention", "execution") == 5