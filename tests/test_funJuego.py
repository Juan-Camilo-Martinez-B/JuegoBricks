import pytest
from src.funJuego import iniciar_juego, mover_personaje, finalizar_juego

def test_iniciar_juego(capsys):
    iniciar_juego()
    captured = capsys.readouterr()
    assert captured.out == "¡Iniciando juego!!!\n"

def test_mover_personaje(capsys):
    mover_personaje("derecha")
    captured = capsys.readouterr()
    assert captured.out == "Moviendo personaje hacia derecha\n"
    
    mover_personaje("arriba")  # Caso adicional
    captured = capsys.readouterr()
    assert captured.out == "Moviendo personaje hacia arriba\n"

def test_finalizar_juego(capsys):
    finalizar_juego()
    captured = capsys.readouterr()
    assert captured.out == "¡Fin del juego!!\n"