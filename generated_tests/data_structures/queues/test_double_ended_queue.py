import pytest
from data_structures.queues.double_ended_queue import Deque


def test_add_first():
    deque = Deque()
    deque.appendleft(10)
    assert deque.__repr__() == str([10])
    assert len(deque) == 1


def test_add_last():
    deque = Deque()
    deque.append(20)
    assert deque.__repr__() == str([20])
    assert len(deque) == 1


def test_poll_first():
    deque = Deque()
    deque.appendleft(10)
    deque.append(20)
    assert deque.popleft() == 10
    assert deque.__repr__() == str([20])
    assert len(deque) == 1


def test_poll_last():
    deque = Deque()
    deque.appendleft(10)
    deque.append(20)
    assert deque.pop() == 20
    assert deque.__repr__() == str([10])
    assert len(deque) == 1


def test_is_empty():
    deque = Deque()
    assert deque.is_empty()
    deque.appendleft(10)
    assert not deque.is_empty()


def test_peek_first_empty():
    deque = Deque()
    assert deque._front is None


def test_peek_last_empty():
    deque = Deque()
    assert deque._back is None


def test_poll_first_empty():
    deque = Deque()
    with pytest.raises(AssertionError):
        deque.popleft()


def test_poll_last_empty():
    deque = Deque()
    with pytest.raises(AssertionError):
        deque.pop()


def test_to_string():
    deque = Deque()
    deque.appendleft(10)
    deque.append(20)
    deque.appendleft(5)
    assert deque.__repr__() == str([5, 10, 20])


def test_alternating_add_remove():
    deque = Deque()
    deque.appendleft(1)
    deque.append(2)
    deque.appendleft(0)
    assert deque.popleft() == 0
    assert deque.pop() == 2
    assert deque.popleft() == 1
    assert deque.is_empty()


def test_size_after_operations():
    deque = Deque()
    assert len(deque) == 0
    deque.appendleft(1)
    deque.append(2)
    deque.appendleft(3)
    assert len(deque) == 3
    deque.popleft()
    deque.pop()
    assert len(deque) == 1


def test_null_values():
    deque = Deque()
    deque.appendleft(None)
    assert deque._front.val is None
    assert deque.popleft() is None
    assert deque.is_empty()


def test_multiple_add_first():
    deque = Deque()
    deque.appendleft(1)
    deque.appendleft(2)
    deque.appendleft(3)

    assert deque.__repr__() == str([3, 2, 1])
    assert len(deque) == 3


def test_multiple_add_last():
    deque = Deque()
    deque.append(1)
    deque.append(2)
    deque.append(3)

    assert deque.__repr__() == str([1, 2, 3])
    assert len(deque) == 3


def test_single_element_operations():
    deque = Deque()
    deque.appendleft(1)

    assert deque._front.val == 1
    assert deque._back.val == 1
    assert len(deque) == 1
    assert deque.popleft() == 1
    assert deque.is_empty()


def test_single_element_poll_last():
    deque = Deque()
    deque.append(1)

    assert deque.pop() == 1
    assert deque.is_empty()


def test_mixed_null_and_values():
    deque = Deque()
    deque.appendleft("first")
    deque.append(None)
    deque.appendleft(None)
    deque.append("last")

    assert len(deque) == 4
    assert deque.popleft() is None
    assert deque.popleft() == "first"
    assert deque.pop() == "last"


def test_symmetric_operations():
    deque = Deque()

    deque.appendleft(1)
    deque.append(2)

    assert deque.popleft() == 1
    assert deque.pop() == 2
    assert deque.is_empty()


if __name__ == "__main__":
    pytest.main()