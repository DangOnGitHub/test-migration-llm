import pytest
from maths.area import (
    surface_area_cube,
    surface_area_cuboid,
    surface_area_sphere,
    area_rectangle,
    surface_area_cylinder,
    area_square,
    area_triangle,
    area_parallelogram,
    area_trapezium,
    area_circle,
    surface_area_hemisphere,
    surface_area_cone,
)

def test_surface_area_cube():
    assert surface_area_cube(1) == 6.0

def test_surface_area_cuboid():
    assert surface_area_cuboid(5, 6, 7) == 214.0

def test_surface_area_sphere():
    assert surface_area_sphere(1) == pytest.approx(12.566370614359172)

def test_area_rectangle():
    assert area_rectangle(10, 20) == 200.0

def test_surface_area_cylinder():
    assert surface_area_cylinder(1, 2) == pytest.approx(18.84955592153876)

def test_area_square():
    assert area_square(10) == 100.0

def test_area_triangle():
    assert area_triangle(10, 10) == 50.0

def test_area_parallelogram():
    assert area_parallelogram(10, 20) == 200.0

def test_area_trapezium():
    assert area_trapezium(10, 20, 30) == 450.0

def test_area_circle():
    assert area_circle(20) == pytest.approx(1256.6370614359173)

def test_surface_area_hemisphere():
    assert surface_area_hemisphere(5) == pytest.approx(235.61944901923448)

def test_surface_area_cone():
    assert surface_area_cone(6, 8) == pytest.approx(301.59289474462014)

def test_all_illegal_input():
    with pytest.raises(ValueError):
        surface_area_cube(0)
    with pytest.raises(ValueError):
        surface_area_cuboid(0, 1, 2)
    with pytest.raises(ValueError):
        surface_area_cuboid(1, 0, 2)
    with pytest.raises(ValueError):
        surface_area_cuboid(1, 2, 0)
    with pytest.raises(ValueError):
        surface_area_sphere(0)
    with pytest.raises(ValueError):
        area_rectangle(0, 10)
    with pytest.raises(ValueError):
        area_rectangle(10, 0)
    with pytest.raises(ValueError):
        surface_area_cylinder(0, 1)
    with pytest.raises(ValueError):
        surface_area_cylinder(1, 0)
    with pytest.raises(ValueError):
        area_square(0)
    with pytest.raises(ValueError):
        area_triangle(0, 1)
    with pytest.raises(ValueError):
        area_triangle(1, 0)
    with pytest.raises(ValueError):
        area_parallelogram(0, 1)
    with pytest.raises(ValueError):
        area_parallelogram(1, 0)
    with pytest.raises(ValueError):
        area_trapezium(0, 1, 1)
    with pytest.raises(ValueError):
        area_trapezium(1, 0, 1)
    with pytest.raises(ValueError):
        area_trapezium(1, 1, 0)
    with pytest.raises(ValueError):
        area_circle(0)
    with pytest.raises(ValueError):
        surface_area_hemisphere(0)
    with pytest.raises(ValueError):
        surface_area_cone(1, 0)
    with pytest.raises(ValueError):
        surface_area_cone(0, 1)