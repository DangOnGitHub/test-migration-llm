import pytest
from dynamic_programming.bitmask import AssignmentUsingBitmask

def test_count_no_of_ways():
    total_tasks = 5
    task_performed = [[1, 3, 4], [1, 2, 5], [3, 4]]
    assignment = AssignmentUsingBitmask(task_performed, total_tasks)
    ways = assignment.count_no_of_ways(task_performed)
    assert ways == 10

def test_no_possible_assignments():
    total_tasks = 3
    task_performed = [[2], [3]]
    assignment = AssignmentUsingBitmask(task_performed, total_tasks)
    ways = assignment.count_no_of_ways(task_performed)
    assert ways == 1

def test_single_person_multiple_tasks():
    total_tasks = 3
    task_performed = [[1, 2, 3]]
    assignment = AssignmentUsingBitmask(task_performed, total_tasks)
    ways = assignment.count_no_of_ways(task_performed)
    assert ways == 3

def test_multiple_people_single_task():
    total_tasks = 1
    task_performed = [[1], [1]]
    assignment = AssignmentUsingBitmask(task_performed, total_tasks)
    ways = assignment.count_no_of_ways(task_performed)
    assert ways == 0