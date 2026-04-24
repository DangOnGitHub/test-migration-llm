import pytest
from dynamic_programming.smith_waterman import smith_waterman, traceback, score_function

def test_identical_strings():
    score_matrix = smith_waterman("GATTACA", "GATTACA", match=2, mismatch=-1, gap=-2)
    max_score = max(max(row) for row in score_matrix)
    assert max_score == 14  # full match, 7*2

def test_partial_match():
    score_matrix = smith_waterman("GATTACA", "TTAC", match=2, mismatch=-1, gap=-2)
    max_score = max(max(row) for row in score_matrix)
    assert max_score == 8  # best local alignment "TTAC"

def test_no_match():
    score_matrix = smith_waterman("AAAA", "TTTT", match=1, mismatch=-1, gap=-2)
    max_score = max(max(row) for row in score_matrix)
    assert max_score == 0  # no alignment worth keeping

def test_insertion_deletion():
    score_matrix = smith_waterman("ACGT", "ACGGT", match=1, mismatch=-1, gap=-2)
    max_score = max(max(row) for row in score_matrix)
    assert max_score == 3  # local alignment "ACG"

def test_empty_strings():
    score_matrix = smith_waterman("", "", match=1, mismatch=-1, gap=-2)
    max_score = max(max(row) for row in score_matrix)
    assert max_score == 0

@pytest.mark.parametrize("s1, s2", [("null", "ABC"), ("ABC", "null"), ("null", "null")])
def test_null_inputs(s1, s2):
    first = None if s1 == "null" else s1
    second = None if s2 == "null" else s2
    with pytest.raises(TypeError):
        smith_waterman(first, second, match=1, mismatch=-1, gap=-2)