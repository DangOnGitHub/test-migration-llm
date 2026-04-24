import pytest
from conversions.temperature_conversions import (
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    fahrenheit_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_celsius,
    kelvin_to_fahrenheit
)

DELTA = 0.01

def assertAlmostEqual(actual, expected, delta):
    assert abs(actual - expected) <= delta

def test_celsius_to_fahrenheit():
    assertAlmostEqual(celsius_to_fahrenheit(0.0), 32.0, DELTA)
    assertAlmostEqual(celsius_to_fahrenheit(100.0), 212.0, DELTA)
    assertAlmostEqual(celsius_to_fahrenheit(-40.0), -40.0, DELTA)
    assertAlmostEqual(celsius_to_fahrenheit(37.0), 98.6, DELTA)

def test_celsius_to_kelvin():
    assertAlmostEqual(celsius_to_kelvin(0.0), 273.15, DELTA)
    assertAlmostEqual(celsius_to_kelvin(100.0), 373.15, DELTA)
    assertAlmostEqual(celsius_to_kelvin(-40.0), 233.15, DELTA)

def test_fahrenheit_to_celsius():
    assertAlmostEqual(fahrenheit_to_celsius(32.0), 0.0, DELTA)
    assertAlmostEqual(fahrenheit_to_celsius(212.0), 100.0, DELTA)
    assertAlmostEqual(fahrenheit_to_celsius(-40.0), -40.0, DELTA)
    assertAlmostEqual(fahrenheit_to_celsius(98.6), 37.0, DELTA)

def test_fahrenheit_to_kelvin():
    assertAlmostEqual(fahrenheit_to_kelvin(32.0), 273.15, DELTA)
    assertAlmostEqual(fahrenheit_to_kelvin(212.0), 373.15, DELTA)
    assertAlmostEqual(fahrenheit_to_kelvin(-40.0), 233.15, DELTA)

def test_kelvin_to_celsius():
    assertAlmostEqual(kelvin_to_celsius(273.15), 0.0, DELTA)
    assertAlmostEqual(kelvin_to_celsius(373.15), 100.0, DELTA)
    assertAlmostEqual(kelvin_to_celsius(0.0), -273.15, DELTA)

def test_kelvin_to_fahrenheit():
    assertAlmostEqual(kelvin_to_fahrenheit(273.15), 32.0, DELTA)
    assertAlmostEqual(kelvin_to_fahrenheit(373.15), 212.0, DELTA)
    assertAlmostEqual(kelvin_to_fahrenheit(233.15), -40.0, DELTA)