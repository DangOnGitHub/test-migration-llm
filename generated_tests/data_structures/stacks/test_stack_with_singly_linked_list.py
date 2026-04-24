import pytest
from data_structures.stacks.stack_with_singly_linked_list import LinkedStack


@pytest.fixture
def stack():
    return LinkedStack()


def test_push_and_peek(stack):
    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.peek() == 3
    assert len(stack) == 3


def test_pop(stack):
    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.is_empty()


def test_pop_empty_stack(stack):
    with pytest.raises(IndexError):
        stack.pop()


def test_peek_empty_stack(stack):
    with pytest.raises(IndexError):
        stack.peek()


def test_is_empty(stack):
    assert stack.is_empty()

    stack.push(1)
    assert not stack.is_empty()

    stack.pop()
    assert stack.is_empty()


def test_to_string(stack):
    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert str(stack) == "3->2->1"


def test_multiple_pushes_and_pops(stack):
    stack.push(5)
    stack.push(10)
    stack.push(15)

    assert stack.pop() == 15
    assert stack.peek() == 10
    assert stack.pop() == 10
    assert stack.pop() == 5
    assert stack.is_empty()


def test_get_size(stack):
    assert len(stack) == 0
    stack.push(1)
    stack.push(2)
    assert len(stack) == 2
    stack.pop()
    assert len(stack) == 1


def test_size_after_clearing_stack(stack):
    stack.push(1)
    stack.push(2)
    stack.push(3)

    # Manually clear the stack
    while not stack.is_empty():
        stack.pop()
    assert stack.is_empty()
    assert len(stack) == 0


def test_sequential_push_and_pop(stack):
    for i in range(1, 101):
        stack.push(i)
    assert len(stack) == 100

    for i in range(100, 0, -1):
        assert stack.pop() == i
    assert stack.is_empty()


def test_push_zero_and_negative_values(stack):
    stack.push(0)
    stack.push(-1)
    stack.push(-1)

    assert stack.pop() == -1
    assert stack.pop() == -1
    assert stack.pop() == 0


def test_push_duplicate_values(stack):
    stack.push(1)
    stack.push(1)
    stack.push(1)

    assert len(stack) == 3
    assert stack.pop() == 1
    assert stack.pop() == 1
    assert stack.pop() == 1


def test_push_after_emptying_stack(stack):
    stack.push(1)
    stack.push(2)
    stack.pop()
    stack.pop()

    assert stack.is_empty()

    stack.push(10)
    assert stack.peek() == 10
    assert len(stack) == 1


def test_peek_does_not_modify_stack(stack):
    stack.push(1)

    first_peek = stack.peek()
    second_peek = stack.peek()
    third_peek = stack.peek()

    assert first_peek == second_peek
    assert second_peek == third_peek
    assert len(stack) == 1
    assert stack.pop() == 1


def test_alternating_push_and_pop(stack):
    stack.push(1)
    assert stack.pop() == 1

    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3

    stack.push(4)
    assert stack.pop() == 4
    assert stack.pop() == 2

    assert stack.is_empty()


def test_to_string_with_single_element(stack):
    stack.push(42)
    assert str(stack) == "42"


def test_stack_integrity(stack):
    for i in range(10):
        stack.push(i)
        assert len(stack) == i + 1
        assert stack.peek() == i

    for i in reversed(range(10)):
        assert stack.peek() == i
        assert stack.pop() == i
        assert len(stack) == i