import builtins
from Ejercicio14_Ahorcado import main

def test_adivinar_palabra(monkeypatch, capfd):
    """Simula adivinar la palabra secreta letra por letra correctamente"""
    palabra_fija = "test"
    monkeypatch.setattr("Ejercicio14_Ahorcado.elegir_palabra", lambda palabras: palabra_fija)
    decisiones = iter(["t", "e", "s"])
    monkeypatch.setattr(builtins, "input", lambda _: next(decisiones))

    main()

    captured = capfd.readouterr()
    salida = captured.out

    assert "¡Felicidades! Has adivinado la palabra: test" in salida
    assert "¡Bienvenido al juego del Ahorcado!" in salida

def test_letra_incorrecta(monkeypatch, capfd):
    """Simula un intento con letra incorrecta"""
    palabra_fija = "abc"
    monkeypatch.setattr("Ejercicio14_Ahorcado.elegir_palabra", lambda palabras: palabra_fija)
    decisiones = iter(["x", "a", "b", "c"])
    monkeypatch.setattr(builtins, "input", lambda _: next(decisiones))

    main()

    captured = capfd.readouterr()
    salida = captured.out

    assert "La letra no está en la palabra." in salida
    assert "¡Felicidades! Has adivinado la palabra: abc" in salida

def test_letra_repetida(monkeypatch, capfd):
    """Simula ingresar una letra repetida"""
    palabra_fija = "hi"
    monkeypatch.setattr("Ejercicio14_Ahorcado.elegir_palabra", lambda palabras: palabra_fija)
    decisiones = iter(["h", "h", "i"])
    monkeypatch.setattr(builtins, "input", lambda _: next(decisiones))

    main()

    captured = capfd.readouterr()
    salida = captured.out

    assert "Ya intentaste esa letra. Intenta con otra." in salida
    assert "¡Felicidades! Has adivinado la palabra: hi" in salida
