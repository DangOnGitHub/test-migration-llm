import pytest
from dynamic_programming.all_construct import all_construct

def test_all_construct_basic():
    expected = [["he", "l", "l", "o"]]
    result = all_construct("hello", ["he", "l", "o"])
    assert expected == result

def test_all_construct_multiple_ways():
    expected = [["purp", "le"], ["p", "ur", "p", "le"]]
    result = all_construct("purple", ["purp", "p", "ur", "le", "purpl"])
    assert expected == result

def test_all_construct_no_ways():
    expected = []
    result = all_construct("abcdef", ["gh", "ijk"])
    assert expected == result

def test_all_construct_empty_target():
    expected = [[]]
    result = all_construct("", ["a", "b", "c"])
    assert expected == result