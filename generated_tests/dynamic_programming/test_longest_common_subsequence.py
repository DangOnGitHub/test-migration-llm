import pytest
from dynamic_programming.longest_common_subsequence import longest_common_subsequence

def test_lcs_basic():
    str1 = "ABCBDAB"
    str2 = "BDCAB"
    expected_length = 4
    expected_seq = "BDAB"
    result_length, result_seq = longest_common_subsequence(str1, str2)
    assert (expected_length, expected_seq) == (result_length, result_seq)

def test_lcs_identical_strings():
    str1 = "AGGTAB"
    str2 = "AGGTAB"
    expected_length = 6
    expected_seq = "AGGTAB"
    result_length, result_seq = longest_common_subsequence(str1, str2)
    assert (expected_length, expected_seq) == (result_length, result_seq)

def test_lcs_no_common_characters():
    str1 = "ABC"
    str2 = "XYZ"
    expected_length = 0
    expected_seq = ""
    result_length, result_seq = longest_common_subsequence(str1, str2)
    assert (expected_length, expected_seq) == (result_length, result_seq)

def test_lcs_with_empty_string():
    str1 = ""
    str2 = "XYZ"
    expected_length = 0
    expected_seq = ""
    result_length, result_seq = longest_common_subsequence(str1, str2)
    assert (expected_length, expected_seq) == (result_length, result_seq)

def test_lcs_with_both_empty_strings():
    str1 = ""
    str2 = ""
    expected_length = 0
    expected_seq = ""
    result_length, result_seq = longest_common_subsequence(str1, str2)
    assert (expected_length, expected_seq) == (result_length, result_seq)

def test_lcs_with_null_first_string():
    str1 = None
    str2 = "XYZ"
    with pytest.raises(AssertionError):
        longest_common_subsequence(str1, str2)

def test_lcs_with_null_second_string():
    str1 = "ABC"
    str2 = None
    with pytest.raises(AssertionError):
        longest_common_subsequence(str1, str2)

def test_lcs_with_null_both_strings():
    str1 = None
    str2 = None
    with pytest.raises(AssertionError):
        longest_common_subsequence(str1, str2)

def test_lcs_with_longer_string_containing_common_subsequence():
    str1 = "ABCDEF"
    str2 = "AEBDF"
    expected_length = 4
    expected_seq = "ABDF"
    result_length, result_seq = longest_common_subsequence(str1, str2)
    assert (expected_length, expected_seq) == (result_length, result_seq)
