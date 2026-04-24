import pytest
from maths.perfect_cube import perfect_cube, perfect_cube_binary_search

def test_perfect_cube():
    assert perfect_cube(-27) == True
    assert perfect_cube_binary_search(-27) == True
    assert perfect_cube(-1) == True
    assert perfect_cube_binary_search(-1) == True
    assert perfect_cube(0) == True
    assert perfect_cube_binary_search(0) == True
    assert perfect_cube(1) == True
    assert perfect_cube_binary_search(1) == True
    assert perfect_cube(8) == True
    assert perfect_cube_binary_search(8) == True
    assert perfect_cube(27) == True
    assert perfect_cube_binary_search(27) == True

    assert perfect_cube(-9) == False
    assert perfect_cube_binary_search(-9) == False
    assert perfect_cube(2) == False
    assert perfect_cube_binary_search(2) == False
    assert perfect_cube(4) == False
    assert perfect_cube_binary_search(4) == False
    assert perfect_cube(30) == False
    assert perfect_cube_binary_search(30) == False