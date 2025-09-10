import builtins
from Ejercicio5_clasificarnum import par_impar,main

def test_par(monkeypatch, capfd):
    # Simular que el usuario ingresa un número par (10)
    monkeypatch.setattr(builtins, "input", lambda _: "10")

    main()

    captured = capfd.readouterr()
    assert "El numero ingresado es par" in captured.out


def test_impar(monkeypatch, capfd):
    # Simular que el usuario ingresa un número impar (7)
    monkeypatch.setattr(builtins, "input", lambda _: "7")

    main()

    captured = capfd.readouterr()
    assert "El numero ingresado es impar" in captured.out


def test_vacio(monkeypatch, capfd):
    # Simular que el usuario no escribe nada
    monkeypatch.setattr(builtins, "input", lambda _: "")

    main()

    captured = capfd.readouterr()
    assert "No debe ingresar vacios" in captured.out
