import pytest
from src.busqueda import buscar_elemento  # Importa el módulo desde el paquete src

def test_buscar_elemento():
    assert buscar_elemento([1, 2, 3, 4], 3) == True      # Presente
    assert buscar_elemento([1, 2, 3, 4], 5) == False      # Ausente
    assert buscar_elemento(["a", "b", "c"], "b") == True  # Strings
    assert buscar_elemento([], 1) == False               # Lista vacía