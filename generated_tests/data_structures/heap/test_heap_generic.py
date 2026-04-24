import pytest
from data_structures.heap.heap_generic import Heap

@pytest.fixture
def heap():
    return Heap()

def test_insert_and_get_top(heap):
    heap.insert_item(10, 10)
    heap.insert_item(20, 20)
    heap.insert_item(5, 5)
    
    assert heap.get_top() == [20, 20]

def test_extract_top(heap):
    heap.insert_item(10, 10)
    heap.insert_item(20, 20)
    heap.insert_item(5, 5)
    
    assert heap.extract_top() == [20, 20]
    assert heap.get_top() == [10, 10]

def test_is_empty(heap):
    assert heap.get_top() is None
    heap.insert_item(1, 1)
    assert heap.get_top() is not None

def test_size(heap):
    assert heap.size == 0
    heap.insert_item(1, 1)
    heap.insert_item(2, 2)
    assert heap.size == 2

def test_update_item(heap):
    heap.insert_item(10, 10)
    heap.insert_item(20, 20)
    heap.insert_item(5, 5)

    heap.update_item(10, 10)
    assert heap.get_top() == [20, 20]

    heap.insert_item(30, 30)
    heap.update_item(20, 20)
    assert heap.get_top() == [30, 30]

def test_extract_from_empty_heap(heap):
    with pytest.raises(IndexError):
        heap.extract_top()

def test_get_from_empty_heap(heap):
    assert heap.get_top() is None

def test_update_nonexistent_item(heap):
    with pytest.raises(KeyError):
        heap.update_item(100, 100)