import pytest
from conversions.time_conversions import convert_time

@pytest.mark.parametrize(
    "value, unit_from, unit_to, expected",
    [
        (60, "seconds", "minutes", 1),
        (120, "seconds", "minutes", 2),
        (2, "minutes", "seconds", 120),
        (2, "hours", "minutes", 120),
        (1, "days", "hours", 24),
        (1, "weeks", "days", 7),
        (1, "months", "days", 30.438),
        (1, "years", "days", 365.25),
        (3600, "seconds", "hours", 1),
        (86400, "seconds", "days", 1),
        (604800, "seconds", "weeks", 1),
        (31557600, "seconds", "years", 1),
    ],
)
def test_valid_conversions(value, unit_from, unit_to, expected):
    assert convert_time(value, unit_from, unit_to) == expected

def test_zero_value():
    assert convert_time(0, "seconds", "hours") == 0.0

def test_same_unit_conversion():
    assert convert_time(123.456, "minutes", "minutes") == 123.456

def test_negative_value():
    with pytest.raises(ValueError):
        convert_time(-5, "seconds", "minutes")

@pytest.mark.parametrize("unit_from, unit_to", [("lightyears", "seconds"), ("minutes", "centuries")])
def test_invalid_units(unit_from, unit_to):
    with pytest.raises(ValueError):
        convert_time(10, unit_from, unit_to)

def test_null_unit():
    with pytest.raises(ValueError):
        convert_time(10, None, "seconds")

    with pytest.raises(ValueError):
        convert_time(10, "minutes", None)

    with pytest.raises(ValueError):
        convert_time(10, None, None)

@pytest.mark.parametrize(
    "value, unit_from, unit_to",
    [
        (1.0, "hours", "minutes"),
        (2.5, "days", "hours"),
        (1000, "seconds", "minutes"),
    ],
)
def test_round_trip_conversion(value, unit_from, unit_to):
    converted = convert_time(value, unit_from, unit_to)
    round_trip = convert_time(converted, unit_to, unit_from)
    assert pytest.approx(round_trip, 0.05) == pytest.approx(value, 0.05)