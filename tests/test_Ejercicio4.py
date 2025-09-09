import builtins
import random
import pytest
from Ejercicio4_juego import definir_ganador,Iniciar_juego


def test_empate():
    assert definir_ganador("piedra", "piedra") == "Empate"
    assert definir_ganador("papel", "papel") == "Empate"
    assert definir_ganador("tijera", "tijera") == "Empate"


def test_gana_jugador():
    assert definir_ganador("piedra", "tijera") == "Ha ganado el jugador"
    assert definir_ganador("tijera", "papel") == "Ha ganado el jugador"
    assert definir_ganador("papel", "piedra") == "Ha ganado el jugador"


def test_gana_computadora():
    assert definir_ganador("tijera", "piedra") == "Ha ganado la computadora"
    assert definir_ganador("papel", "tijera") == "Ha ganado la computadora"
    assert definir_ganador("piedra", "papel") == "Ha ganado la computadora"


def test_iniciar_juego_valido(capsys):
    Iniciar_juego("piedra")
    captured = capsys.readouterr()
    assert "Iniciando el juego..." in captured.out


def test_iniciar_juego_invalido(monkeypatch, capsys):
    # Simular que el usuario ingresa un valor incorrecto primero y luego "piedra"
    inputs = iter(["piedra"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    Iniciar_juego("invalido")
    captured = capsys.readouterr()
    # No imprime "Iniciando..." al inicio, pero al final ya pide bien
    assert "Iniciando el juego..." in captured.out
