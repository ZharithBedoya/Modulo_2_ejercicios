
import builtins
from Ejercicio2_interprete import comandos

def test_guardar(monkeypatch, capfd):
    # Simular que el usuario digita "1" y luego "3" para salir
    inputs = iter(["1", "3"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    comandos()  # ejecutar

    captured = capfd.readouterr()
    assert "Guardando archivo..." in captured.out
    assert "Saliendo del comando..." in captured.out


def test_cargar(monkeypatch, capfd):
    inputs = iter(["2", "3"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    comandos()

    captured = capfd.readouterr()
    assert "Cargando archivo..." in captured.out
    assert "Saliendo del comando..." in captured.out


def test_invalido(monkeypatch, capfd):
    inputs = iter(["99", "3"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    comandos()

    captured = capfd.readouterr()
    assert "Comando invalido" in captured.out
    assert "Saliendo del comando..." in captured.out
