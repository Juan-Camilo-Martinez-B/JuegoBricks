import pytest
from src.cadenas import convertir_mayusculas

def test_convertir_mayusculas_basico():
    assert convertir_mayusculas("hola") == "HOLA"

def test_convertir_mayusculas_con_espacios():
    assert convertir_mayusculas("hola mundo") == "HOLA MUNDO"

def test_convertir_mayusculas_con_caracteres_especiales():
    assert convertir_mayusculas("¡python!") == "¡PYTHON!"

def test_convertir_mayusculas_con_numeros():
    assert convertir_mayusculas("abc123") == "ABC123"

def test_convertir_mayusculas_vacio():
    assert convertir_mayusculas("") == ""

def test_convertir_mayusculas_ya_en_mayusculas():
    assert convertir_mayusculas("PYTHON") == "PYTHON"