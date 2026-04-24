import pytest
from dynamic_programming.edit_distance import EditDistance

@pytest.fixture
def solver():
    return EditDistance()

@pytest.mark.parametrize("str1, str2, expected", [
    ("", "", 0),
    ("abc", "", 3),
    ("", "abcd", 4),
    ("same", "same", 0),
    ("a", "b", 1),
    ("abc", "abd", 1)
])
def test_min_distance_bottom_up(solver, str1, str2, expected):
    assert solver.min_dist_bottom_up(str1, str2) == expected

@pytest.mark.parametrize("str1, str2, expected", [
    ("", "", 0),
    ("abc", "", 3),
    ("", "abcd", 4),
    ("same", "same", 0),
    ("a", "b", 1),
    ("abc", "abd", 1)
])
def test_min_distance_top_down(solver, str1, str2, expected):
    assert solver.min_dist_top_down(str1, str2) == expected

def test_edit_distance_both_empty_strings(solver):
    assert solver.min_dist_top_down("", "") == 0
    assert solver.min_dist_bottom_up("", "") == 0

def test_edit_distance_one_empty_string(solver):
    assert solver.min_dist_top_down("", "hello") == 5
    assert solver.min_dist_top_down("worldly", "") == 7
    assert solver.min_dist_bottom_up("", "hello") == 5
    assert solver.min_dist_bottom_up("worldly", "") == 7

def test_edit_distance_equal_strings(solver):
    assert solver.min_dist_top_down("test", "test") == 0
    assert solver.min_dist_top_down("abc", "abc") == 0
    assert solver.min_dist_bottom_up("test", "test") == 0
    assert solver.min_dist_bottom_up("abc", "abc") == 0

def test_edit_distance_one_character_difference(solver):
    assert solver.min_dist_top_down("cat", "bat") == 1
    assert solver.min_dist_top_down("cat", "cats") == 1
    assert solver.min_dist_top_down("cats", "cat") == 1
    assert solver.min_dist_bottom_up("cat", "bat") == 1
    assert solver.min_dist_bottom_up("cat", "cats") == 1
    assert solver.min_dist_bottom_up("cats", "cat") == 1

def test_edit_distance_general_cases(solver):
    assert solver.min_dist_top_down("kitten", "sitting") == 3
    assert solver.min_dist_top_down("flaw", "lawn") == 2
    assert solver.min_dist_top_down("intention", "execution") == 5
    assert solver.min_dist_bottom_up("kitten", "sitting") == 3
    assert solver.min_dist_bottom_up("flaw", "lawn") == 2
    assert solver.min_dist_bottom_up("intention", "execution") == 5