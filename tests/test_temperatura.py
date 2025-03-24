import pytest
from src.temperatura import celsius_a_fahrenheit

def test_celsius_a_fahrenheit():
    assert celsius_a_fahrenheit(0) == 32          # Punto de congelación
    assert celsius_a_fahrenheit(100) == 212       # Punto de ebullición
    assert celsius_a_fahrenheit(-40) == -40       # Mismo valor
    assert celsius_a_fahrenheit(37) == pytest.approx(98.6, 0.1)  # Aproximado por decimales