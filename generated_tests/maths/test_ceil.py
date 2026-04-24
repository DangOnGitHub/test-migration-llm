import pytest
import math
from maths.ceil import ceil

@pytest.mark.parametrize("input,expected", [
    (7.057, 8), 
    (7.004, 8), 
    (-13.004, -13), 
    (0.98, 1), 
    (-11.357, -11)
])
def test_ceil(input, expected):
    assert ceil(input) == expected

@pytest.mark.parametrize("data", [
    (float('inf'), float('inf')),
    (-float('inf'), -float('inf')),
    (float('nan'), float('nan')),
    (0.0, math.ceil(0.0)),
    (-0.0, math.ceil(-0.0)),
    (float('inf'), math.ceil(float('inf'))),
    (-float('inf'), math.ceil(-float('inf')))
])
def test_edge_cases(data):
    input, expected = data
    result = ceil(input)
    if math.isnan(input):
        assert math.isnan(result) 
    else:
        assert result == expected