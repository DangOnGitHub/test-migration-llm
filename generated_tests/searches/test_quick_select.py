import pytest
from searches.quick_select import quick_select
import random

def test_quick_select_minimum_of_one_element():
    elements = [42]
    minimum = quick_select(elements, 0)
    assert minimum == 42

def test_quick_select_minimum_of_two_elements():
    elements1 = [42, 90]
    elements2 = [90, 42]

    minimum1 = quick_select(elements1, 0)
    minimum2 = quick_select(elements2, 0)

    assert minimum1 == 42
    assert minimum2 == 42

def test_quick_select_minimum_of_three_elements():
    elements1 = [1, 2, 3]
    elements2 = [2, 1, 3]
    elements3 = [2, 3, 1]

    minimum1 = quick_select(elements1, 0)
    minimum2 = quick_select(elements2, 0)
    minimum3 = quick_select(elements3, 0)

    assert minimum1 == 1
    assert minimum2 == 1
    assert minimum3 == 1

def test_quick_select_minimum_of_many_elements():
    elements = generate_random_integers(NUM_RND_ELEMENTS)
    actual = quick_select(elements, 0)
    expected = min(elements)
    assert expected == actual

def test_quick_select_maximum_of_one_element():
    elements = [42]
    maximum = quick_select(elements, 0)
    assert maximum == 42

def test_quick_select_maximum_of_two_elements():
    elements1 = [42, 90]
    elements2 = [90, 42]

    maximum1 = quick_select(elements1, 1)
    maximum2 = quick_select(elements2, 1)

    assert maximum1 == 90
    assert maximum2 == 90

def test_quick_select_maximum_of_three_elements():
    elements1 = [1, 2, 3]
    elements2 = [2, 1, 3]
    elements3 = [2, 3, 1]

    maximum1 = quick_select(elements1, 2)
    maximum2 = quick_select(elements2, 2)
    maximum3 = quick_select(elements3, 2)

    assert maximum1 == 3
    assert maximum2 == 3
    assert maximum3 == 3

def test_quick_select_maximum_of_many_elements():
    elements = generate_random_integers(NUM_RND_ELEMENTS)
    actual = quick_select(elements, NUM_RND_ELEMENTS - 1)
    expected = max(elements)
    assert expected == actual

def test_quick_select_median_of_one_element():
    elements = [42]
    median = quick_select(elements, 0)
    assert median == 42

def test_quick_select_median_of_three_elements():
    elements1 = [1, 2, 3]
    elements2 = [2, 1, 3]
    elements3 = [2, 3, 1]

    median1 = quick_select(elements1, 1)
    median2 = quick_select(elements2, 1)
    median3 = quick_select(elements3, 1)

    assert median1 == 2
    assert median2 == 2
    assert median3 == 2

def test_quick_select_median_of_many_elements():
    median_index = NUM_RND_ELEMENTS // 2
    elements = generate_random_integers(NUM_RND_ELEMENTS)
    actual = quick_select(elements, median_index)

    elements_sorted = sorted(elements)
    assert elements_sorted[median_index] == actual

def test_quick_select_30th_percentile_of_10_elements():
    elements = generate_random_integers(10)
    actual = quick_select(elements, 2)

    elements_sorted = sorted(elements)
    assert elements_sorted[2] == actual

def test_quick_select_30th_percentile_of_many_elements():
    percentile30th = NUM_RND_ELEMENTS // 10 * 3
    elements = generate_random_integers(NUM_RND_ELEMENTS)
    actual = quick_select(elements, percentile30th)

    elements_sorted = sorted(elements)
    assert elements_sorted[percentile30th] == actual

def test_quick_select_70th_percentile_of_10_elements():
    elements = generate_random_integers(10)
    actual = quick_select(elements, 6)

    elements_sorted = sorted(elements)
    assert elements_sorted[6] == actual

def test_quick_select_70th_percentile_of_many_elements():
    percentile70th = NUM_RND_ELEMENTS // 10 * 7
    elements = generate_random_integers(NUM_RND_ELEMENTS)
    actual = quick_select(elements, percentile70th)

    elements_sorted = sorted(elements)
    assert elements_sorted[percentile70th] == actual

def test_quick_select_median_of_three_characters():
    elements = ['X', 'Z', 'Y']
    actual = quick_select(elements, 1)
    assert actual == 'Y'

def test_quick_select_median_of_many_characters():
    elements = generate_random_characters(NUM_RND_ELEMENTS)
    actual = quick_select(elements, NUM_RND_ELEMENTS // 30)

    elements_sorted = sorted(elements)
    assert elements_sorted[NUM_RND_ELEMENTS // 30] == actual

def test_quick_select_null_list():
    with pytest.raises(TypeError):
        quick_select(None, 0)

def test_quick_select_empty_list():
    objects = []
    result = quick_select(objects, 0)
    assert result is None

def test_quick_select_index_out_of_left_bound():
    with pytest.raises(TypeError):
        quick_select([1], -1)

def test_quick_select_index_out_of_right_bound():
    result = quick_select([1], 1)
    assert result is None

NUM_RND_ELEMENTS = 99
RANDOM = random.Random(42)

def generate_random_integers(n):
    return [RANDOM.randint(-1000, 1000) for _ in range(n)]

def generate_random_characters(n):
    return [chr(RANDOM.randint(0x41, 0x5A)) for _ in range(n)]