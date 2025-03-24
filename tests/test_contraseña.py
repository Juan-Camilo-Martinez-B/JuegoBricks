import pytest
from src.contraseña import validar_contraseña

def test_validar_contraseña():
    assert validar_contraseña("Passw0rd") == True    # Válida
    assert validar_contraseña("pass") == False       # Corta
    assert validar_contraseña("Password") == False    # Sin números
    assert validar_contraseña("12345678") == False   # Sin mayúsculas