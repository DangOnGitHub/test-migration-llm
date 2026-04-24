import pytest
from strings.hamming_distance import hamming_distance


@pytest.mark.parametrize("s1, s2, expected", [
    ("", "", 0),
    ("java", "java", 0),
    ("karolin", "kathrin", 3),
    ("kathrin", "kerstin", 4),
    ("00000", "11111", 5),
    ("10101", "10100", 1),
])
def test_hamming_distance(s1, s2, expected):
    assert hamming_distance(s1, s2) == expected


@pytest.mark.parametrize("input1, input2", [
    (None, "abc"),
    ("abc", None),
    (None, None),
])
def test_hamming_distance_with_none_inputs(input1, input2):
    with pytest.raises(TypeError, match="object of type 'NoneType' has no len()"):
        hamming_distance(input1, input2)


def test_not_equal_string_lengths():
    with pytest.raises(ValueError, match="String lengths must match!"):
        hamming_distance("ab", "abc")