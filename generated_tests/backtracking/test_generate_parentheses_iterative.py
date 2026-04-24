import pytest
from backtracking.generate_parentheses_iterative import generate_parentheses_iterative

@pytest.mark.parametrize("input, expected", [
    (0, [""]),
    (1, ["()"]),
    (2, ["(())", "()()"]),
    (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
    (4, ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()", "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"])
])
def test_generate_parentheses_iterative_regular_inputs(input, expected):
    assert generate_parentheses_iterative(input) == expected

@pytest.mark.parametrize("input", [-1, -5, -10])
def test_generate_parentheses_iterative_negative_inputs(input):
    with pytest.raises(ValueError):
        generate_parentheses_iterative(input)