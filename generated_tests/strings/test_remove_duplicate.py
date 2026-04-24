import pytest
from strings.remove_duplicate import remove_duplicates

def test_empty_string():
    assert remove_duplicates("") == ""

def test_null_string():
    assert remove_duplicates(None) is None  # Assuming we modify the function to handle None input

def test_single_character_string():
    assert remove_duplicates("a") == "a"

def test_string_with_no_duplicates():
    assert remove_duplicates("abc") == "abc"

def test_string_with_duplicates():
    assert remove_duplicates("aabbbccccddddd") == "abcd"

def test_string_with_all_same_characters():
    assert remove_duplicates("aaaaa") == "a"

def test_string_with_mixed_case():
    assert remove_duplicates("aabABAB") == "abAB"