import pytest
from backtracking.combination_sum import combination_sum

def norm(result):
    answer = [sorted(comb) for comb in result]
    return sorted(answer, key=lambda x: (len(x), x))

def test_sample():
    candidates = [2, 3, 6, 7]
    target = 7
    expected = [[2, 2, 3], [7]]
    assert norm(expected) == norm(combination_sum(candidates, target))
