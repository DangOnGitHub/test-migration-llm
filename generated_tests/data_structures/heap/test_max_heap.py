import pytest
from data_structures.heap.max_heap import BinaryHeap

class TestBinaryHeap:

    @pytest.fixture(autouse=True)
    def setup_method(self):
        self.heap = BinaryHeap()
        self.heap.insert(5)
        self.heap.insert(2)
        self.heap.insert(8)
        self.heap.insert(1)
        self.heap.insert(9)

    def test_constructor_with_empty_heap(self):
        empty_heap = BinaryHeap()
        assert len(empty_heap) == 0

    def test_insert_element(self):
        self.heap.insert(10)
        assert self.heap.pop() == 10
        assert len(self.heap) == 6

    def test_get_element_at_index(self):
        max_value = self.heap.pop()
        assert max_value == 9

    def test_delete_element(self):
        self.heap.pop()
        assert self.heap.pop() == 8
        assert len(self.heap) == 3

    def test_delete_from_empty_heap(self):
        empty_heap = BinaryHeap()
        with pytest.raises(IndexError):
            empty_heap.pop()

    def test_extract_max(self):
        max_value = self.heap.pop()
        assert max_value == 9
        assert len(self.heap) == 4

        max_value = self.heap.pop()
        assert max_value == 8
        assert len(self.heap) == 3

    def test_extract_max_from_empty_heap(self):
        empty_heap = BinaryHeap()
        with pytest.raises(IndexError):
            empty_heap.pop()

    def test_heap_order(self):
        previous_value = self.heap.pop()
        while len(self.heap) > 0:
            current_value = self.heap.pop()
            assert previous_value >= current_value
            previous_value = current_value

    def test_size_and_empty(self):
        initial_size = len(self.heap)
        assert initial_size == 5
        assert self.heap.get_list != []

        while len(self.heap) > 0:
            self.heap.pop()

        assert len(self.heap) == 0
        assert self.heap.get_list == []