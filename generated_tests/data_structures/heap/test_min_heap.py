import pytest
from data_structures.heap.min_heap import MinHeap, Node

@pytest.fixture
def setup_heap():
    elements = [Node("Five", 5.0), Node("Two", 2.0), Node("Eight", 8.0), Node("One", 1.0), Node("Nine", 9.0)]
    return MinHeap(elements)

def test_constructor_with_empty_list():
    empty_heap = MinHeap([])
    assert empty_heap.is_empty()

def test_constructor_with_initial_elements(setup_heap):
    heap = setup_heap
    assert heap is not None
    assert heap.size() == 5

def test_insert_element(setup_heap):
    heap = setup_heap
    node = Node("Half", 0.5)
    heap.insert(node)
    assert heap.peek().val == 0.5
    assert heap.size() == 6

def test_peek_element(setup_heap):
    heap = setup_heap
    element = heap.peek()
    assert element.name == "One"
    assert element.val == 1.0

def test_remove_element(setup_heap):
    heap = setup_heap
    min_element = heap.remove()
    assert min_element.name == "One"
    assert min_element.val == 1.0
    assert heap.size() == 4

def test_remove_element_from_empty_heap():
    empty_heap = MinHeap([])
    with pytest.raises(IndexError):
        empty_heap.remove()

def test_heap_order_property(setup_heap):
    heap = setup_heap
    parent_idx = 0
    size = len(heap.heap)
    while 2 * parent_idx + 1 < size:
        left_child = 2 * parent_idx + 1
        right_child = 2 * parent_idx + 2
        if left_child < size:
            assert heap.heap[parent_idx].val <= heap.heap[left_child].val
        if right_child < size:
            assert heap.heap[parent_idx].val <= heap.heap[right_child].val
        parent_idx += 1

def test_is_empty(setup_heap):
    heap = setup_heap
    assert not heap.is_empty()

    # Remove all elements
    while not heap.is_empty():
        heap.remove()

    assert heap.is_empty()

def test_decrease_key(setup_heap):
    heap = setup_heap
    node = Node("B", 6.0)
    heap.insert(node)
    heap.decrease_key(node, -17)
    assert heap[node.name] == -17