import pytest
from backtracking.word_search import word_exists

def test_word_search_1():
    board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    word = "ABCCED"
    assert word_exists(board, word)

def test_word_search_2():
    board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    word = "SEE"
    assert word_exists(board, word)

def test_word_search_3():
    board = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    word = "ABCB"
    assert not word_exists(board, word)