import pytest
from collections.abc import Callable
from maths.euler_modified import euler_modified


@pytest.mark.parametrize(
    "ode_func, y0, x0, step_size, x_end, expected",
    [
        ((lambda x, y: x + y), 1.0, 0.0, 0.1, 0.1, 1.1),
    ],
)
def test_euler_modified_step(ode_func: Callable, y0: float, x0: float, step_size: float, x_end: float, expected: float) -> None:
    result = euler_modified(ode_func, y0, x0, step_size, x_end)
    assert pytest.approx(result[-1], 1e-9) == expected


@pytest.mark.parametrize(
    "ode_func, y0, x0, step_size, x_end, expected_exception",
    [
        ((lambda x, y: x + y), 1.0, 0.0, -0.1, 0.1, ValueError),
        ((lambda x, y: x + y), 1.0, 0.0, 0.0, 0.1, ValueError),
    ],
)
def test_euler_modified_invalid_step(ode_func: Callable, y0: float, x0: float, step_size: float, x_end: float, expected_exception: Exception) -> None:
    with pytest.raises(expected_exception):
        euler_modified(ode_func, y0, x0, step_size, x_end)


@pytest.mark.parametrize(
    "ode_func, y0, x0, step_size, x_end, expected_size, expected_first, expected_last",
    [
        ((lambda x, y: x), 0.0, 0.0, 0.5, 1.0, 3, 0.0, 0.25),
        ((lambda x, y: y), 1.0, 0.0, 0.1, 1.0, 11, 1.0, 2.8531167061100002),
        ((lambda x, y: x + y), 1.0, 0.0, 0.1, 0.1, 2, 1.0, 1.1)
    ],
)
def test_euler_modified_full(
    ode_func: Callable,
    y0: float,
    x0: float,
    step_size: float,
    x_end: float,
    expected_size: int,
    expected_first: float,
    expected_last: float,
) -> None:
    result = euler_modified(ode_func, y0, x0, step_size, x_end)
    assert len(result) == expected_size
    assert pytest.approx(result[0], 1e-9) == expected_first
    assert pytest.approx(result[-1], 1e-9) == expected_last


@pytest.mark.parametrize(
    "ode_func, y0, x0, step_size, x_end, expected_exception",
    [
        ((lambda x, y: x + y), 1.0, 1.0, 0.1, 0.0, ValueError),
        ((lambda x, y: x + y), 1.0, 0.0, 0.0, 1.0, ValueError),
        ((lambda x, y: x + y), 1.0, 0.0, -0.1, 1.0, ValueError),
    ],
)
def test_euler_modified_full_invalid_input(
    ode_func: Callable,
    y0: float,
    x0: float,
    step_size: float,
    x_end: float,
    expected_exception: Exception,
) -> None:
    with pytest.raises(expected_exception):
        euler_modified(ode_func, y0, x0, step_size, x_end)