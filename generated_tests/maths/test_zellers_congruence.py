import pytest
from maths.zellers_congruence import zeller

@pytest.mark.parametrize("input_date, expected_day", [
    ("01-01-2000", "Sunday"),
    ("12-25-2021", "Saturday"),
    ("07-04-1776", "Thursday"),
    ("02-29-2020", "Saturday"),
    ("03-01-1900", "Thursday"),
    ("03/01/1900", "Thursday")
])
def test_valid_dates(input_date, expected_day):
    result = zeller(input_date)
    assert result == f"Your date {input_date}, is a {expected_day}!"


@pytest.mark.parametrize("input_date, expected_error_message", [
    ("13-01-2000", "Month must be between 1 - 12"),
    ("02-30-2020", "Invalid date."),
    ("00-15-2020", "Month must be between 1 - 12"),
    ("01-01-0000", "Year out of range. There has to be some sort of limit...right?"),
    ("01/01/200", "Must be 10 characters long"),
    ("01@01>2000", "Date separator must be '-' or '/'"),
    ("aa-01-1900", "invalid literal for int() with base 10: 'aa'"),
    (None, "zeller() missing 1 required positional argument: 'date_input'")
])
def test_invalid_dates(input_date, expected_error_message):
    with pytest.raises(ValueError) as excinfo:
        zeller(input_date)
    assert str(excinfo.value) == expected_error_message