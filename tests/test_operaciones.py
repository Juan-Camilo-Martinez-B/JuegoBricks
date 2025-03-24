import pytest
from src.operaciones import factorial  # Importa el módulo desde el paquete src

def test_factorial():
    assert factorial(0) == 1           # Caso base
    assert factorial(5) == 120          # Caso general
    assert factorial(7) == 5040         # Otro caso

def test_factorial_negativo():
    with pytest.raises(ValueError):     # Verifica excepción
        factorial(-1)