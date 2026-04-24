import pytest
from backtracking.match_word_pattern import match_word_pattern

def test_pattern_matching_success():
    assert match_word_pattern("aba", "GraphTreesGraph")
    assert match_word_pattern("xyx", "PythonRubyPython")

def test_pattern_matching_failure():
    assert not match_word_pattern("GG", "PythonJavaPython")

def test_empty_pattern_and_string():
    assert match_word_pattern("", "")

def test_empty_pattern():
    assert not match_word_pattern("", "nonempty")

def test_empty_string():
    assert not match_word_pattern("abc", "")

def test_longer_pattern_than_string():
    assert not match_word_pattern("abcd", "abc")
