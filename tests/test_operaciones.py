import pytest
from src.operaciones import factorial  # Importa el módulo desde el paquete src

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120

def test_factorial_negativo():
    with pytest.raises(ValueError) as excinfo:
        factorial(-1)
    assert str(excinfo.value) == "El factorial solo está definido para enteros no negativos"

def test_factorial_no_entero():
    with pytest.raises(ValueError) as excinfo:
        factorial(3.5)
    assert str(excinfo.value) == "El factorial solo está definido para enteros no negativos"