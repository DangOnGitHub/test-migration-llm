import pytest
from backtracking.generate_parentheses import generate_parenthesis

def test_generate_parenthesis():
    assert generate_parenthesis(0) == [""]
    assert generate_parenthesis(1) == ["()"]
    assert sorted(generate_parenthesis(2)) == sorted(["(())", "()()"])
    assert sorted(generate_parenthesis(3)) == sorted(["((()))", "(()())", "(())()", "()(())", "()()()"])
    assert sorted(generate_parenthesis(4)) == sorted(["(((())))", "((()()))", "((())())", "((()))()", "(()(()))",
                                                    "(()()())", "(()())()", "(())(())", "(())()()", "()((()))",
                                                    "()(()())", "()(())()", "()()(())", "()()()()"])

@pytest.mark.parametrize("input_value", [-1, -5, -10])
def test_generate_parenthesis_negative(input_value):
    with pytest.raises(ValueError):
        generate_parenthesis(input_value)