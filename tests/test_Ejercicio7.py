import builtins
from Ejercicio7_Combinador import main

def test_estudiantes(monkeypatch, capfd):
    # Simular entradas del usuario:
    # Cantidad: 2
    # Estudiante 1: Ana, Nota 90
    # Estudiante 2: Juan, Nota 85
    inputs = iter([
        "2",     # cantidad de estudiantes
        "Ana",   # nombre estudiante 1
        "90",    # nota estudiante 1
        "Juan",  # nombre estudiante 2
        "85"     # nota estudiante 2
    ])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    main()  # ejecutar programa

    captured = capfd.readouterr()
    salida = captured.out

    # Verificar que la salida contiene los mensajes correctos
    assert "El estudiante Ana tiene una nota de 90" in salida
    assert "El estudiante Juan tiene una nota de 85" in salida
