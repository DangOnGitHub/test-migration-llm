import pytest
from scheduling.highest_response_ratio_next import calculate_turn_around_time, calculate_waiting_time

def test_calculate_turn_around_time():
    process_names = ["A", "B", "C"]
    arrival_times = [0, 2, 4]
    burst_times = [3, 1, 2]
    no_of_processes = 3

    expected_turn_around_times = [3, 2, 2]
    actual_turn_around_times = calculate_turn_around_time(process_names, arrival_times, burst_times, no_of_processes)

    assert expected_turn_around_times == actual_turn_around_times, "Turn Around Times do not match"

def test_calculate_waiting_time():
    turn_around_times = [3, 1, 5]
    burst_times = [3, 1, 2]
    no_of_processes = 3

    expected_waiting_times = [0, 0, 3]
    actual_waiting_times = calculate_waiting_time([], turn_around_times, burst_times, no_of_processes)

    assert expected_waiting_times == actual_waiting_times, "Waiting Times do not match"

def test_complete_scheduling_scenario():
    process_names = ["A", "B", "C"]
    arrival_times = [0, 1, 2]
    burst_times = [5, 2, 1]
    no_of_processes = 3

    expected_turn_around_times = [5, 7, 4]
    turn_around_times = calculate_turn_around_time(process_names, arrival_times, burst_times, no_of_processes)
    assert expected_turn_around_times == turn_around_times, "Turn Around Times do not match"

    expected_waiting_times = [0, 5, 3]
    waiting_times = calculate_waiting_time(process_names, turn_around_times, burst_times, no_of_processes)
    assert expected_waiting_times == waiting_times, "Waiting Times do not match"

def test_zero_processes():
    process_names = []
    arrival_times = []
    burst_times = []
    no_of_processes = 0

    expected_turn_around_times = []
    actual_turn_around_times = calculate_turn_around_time(process_names, arrival_times, burst_times, no_of_processes)

    assert expected_turn_around_times == actual_turn_around_times, "Turn Around Times for zero processes should be an empty list"

def test_all_processes_arrive_at_same_time():
    process_names = ["A", "B", "C", "D"]
    arrival_times = [0, 0, 0, 0]
    burst_times = [4, 3, 1, 2]
    no_of_processes = 4

    expected_turn_around_times = [4, 10, 5, 7]
    actual_turn_around_times = calculate_turn_around_time(process_names, arrival_times, burst_times, no_of_processes)

    assert expected_turn_around_times == actual_turn_around_times, "Turn Around Times for processes arriving at the same time do not match"

def test_processes_with_zero_burst_time():
    process_names = ["A", "B", "C"]
    arrival_times = [0, 1, 2]
    burst_times = [3, 0, 2]
    no_of_processes = 3

    expected_turn_around_times = [3, 2, 3]
    actual_turn_around_times = calculate_turn_around_time(process_names, arrival_times, burst_times, no_of_processes)

    assert expected_turn_around_times == actual_turn_around_times, "Turn Around Times for processes with zero burst time do not match"

def test_processes_with_large_gaps_between_arrivals():
    process_names = ["A", "B", "C"]
    arrival_times = [0, 100, 200]
    burst_times = [10, 10, 10]
    no_of_processes = 3

    expected_turn_around_times = [10, 10, 10]
    actual_turn_around_times = calculate_turn_around_time(process_names, arrival_times, burst_times, no_of_processes)

    assert expected_turn_around_times == actual_turn_around_times, "Turn Around Times for processes with large gaps between arrivals do not match"

def test_processes_with_very_large_burst_times():
    process_names = ["A", "B"]
    arrival_times = [0, 1]
    burst_times = [int(2**31 / 2), int(2**31 / 2)]
    no_of_processes = 2

    expected_turn_around_times = [int(2**31 / 2), int(2**31) - 2]
    actual_turn_around_times = calculate_turn_around_time(process_names, arrival_times, burst_times, no_of_processes)

    assert expected_turn_around_times == actual_turn_around_times, "Turn Around Times for processes with very large burst times do not match"