import pytest
from backtracking.crossword_puzzle_solver import (
    is_valid,
    place_word,
    remove_word,
    solve_crossword,
)

def test_valid_placement():
    puzzle = [['', '', ''], ['', '', ''], ['', '', '']]
    assert is_valid(puzzle, "cat", 0, 0, True)
    assert is_valid(puzzle, "dog", 0, 0, False)
    assert not is_valid(puzzle, "cat", 1, 2, False)

def test_place_and_remove_word():
    puzzle = [['', '', ''], ['', '', ''], ['', '', '']]
    place_word(puzzle, "cat", 0, 0, True)
    assert puzzle[0][0] == 'c'
    assert puzzle[1][0] == 'a'
    assert puzzle[2][0] == 't'

    remove_word(puzzle, "cat", 0, 0, True)
    assert puzzle[0][0] == ''
    assert puzzle[1][0] == ''
    assert puzzle[2][0] == ''

def test_solve_crossword():
    puzzle = [['', '', ''], ['', '', ''], ['', '', '']]
    words = ["cat", "dog", "car"]
    assert solve_crossword(puzzle, words)

    # Solved crossword:
    # c d c
    # a o a
    # t g r

    assert puzzle[0][0] == 'c'
    assert puzzle[1][0] == 'a'
    assert puzzle[2][0] == 't'

    assert puzzle[0][1] == 'd'
    assert puzzle[1][1] == 'o'
    assert puzzle[2][1] == 'g'

    assert puzzle[0][2] == 'c'
    assert puzzle[1][2] == 'a'
    assert puzzle[2][2] == 'r'

def test_no_solution():
    puzzle = [['', '', ''], ['', '', ''], ['', '', '']]
    words = ["cat", "dog", "elephant"]
    assert not solve_crossword(puzzle, words)