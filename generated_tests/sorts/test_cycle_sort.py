from sorts.cycle_sort import cycle_sort

def test_cycle_sort():
    assert cycle_sort([4, 5, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert cycle_sort([0, 1, -10, 15, 2, -2]) == [-10, -2, 0, 1, 2, 15]