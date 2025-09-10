import builtins
from Ejercicio15_batalla_naval import main

def test_hundir_barco(monkeypatch, capfd):
    """Simula hundir el barco correctamente"""
    barco_fijo = [(0, 0), (0, 1), (0, 2)]
    monkeypatch.setattr("Ejercicio15_batalla_naval.colocar_barco", lambda: barco_fijo)

    disparos = iter(["A1", "A2", "A3"])
    monkeypatch.setattr(builtins, "input", lambda _: next(disparos))

    main()

    captured = capfd.readouterr()
    salida = captured.out

    assert "¡Felicidades! Hundiste el barco." in salida
    assert "¡Bienvenido a Batalla Naval simplificada!" in salida


def test_disparo_incorrecto_y_valido(monkeypatch, capfd):
    """Simula un disparo incorrecto y luego aciertos"""
    barco_fijo = [(1, 1), (1, 2), (1, 3)]
    monkeypatch.setattr("Ejercicio15_batalla_naval.colocar_barco", lambda: barco_fijo)

    # Agregamos coordenadas adicionales para evitar StopIteration
    disparos = iter(["A1", "B2", "B3", "B4", "B1", "C1", "C2", "C3", "D1", "D2"])
    monkeypatch.setattr(builtins, "input", lambda _: next(disparos))

    main()

    captured = capfd.readouterr()
    salida = captured.out

    assert "Agua." in salida
    assert "¡Tocado!" in salida
