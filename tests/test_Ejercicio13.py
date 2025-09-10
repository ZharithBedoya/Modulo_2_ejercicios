from Ejercicio13_Aventura import main  # Cambia al nombre real del archivo si es otro

def test_ruta_ganadora(monkeypatch, capfd):
    """
    Simula una ruta donde el jugador gana el juego:
    entrada -> norte -> este -> tomar el tesoro
    """
    # Secuencia de decisiones predefinidas
    decisiones = iter([
        "norte",   # de entrada a pasillo
        "este",    # de pasillo a sala_del_tesoro
        "tomar"    # tomar el tesoro y ganar
    ])

    # Reemplazamos input() para que devuelva las decisiones predefinidas
    monkeypatch.setattr("builtins.input", lambda _: next(decisiones))

    main()  # ejecuta el juego

    captured = capfd.readouterr()
    salida = captured.out

    # Verificar que la salida contenga ciertos mensajes
    assert "Bienvenido a la aventura en texto!" in salida
    assert "Estás en la entrada de una cueva oscura." in salida
    assert "Estás en un pasillo largo y estrecho." in salida
    assert "Has encontrado la sala del tesoro llena de oro." in salida
    assert "¡Felicidades! Has ganado el juego." in salida


def test_ruta_perdida_cofre(monkeypatch, capfd):
    """
    Simula una ruta donde el jugador pierde abriendo el cofre en la entrada.
    """
    decisiones = iter([
        "abrir cofre"  # pierde directamente
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(decisiones))

    main()

    captured = capfd.readouterr()
    salida = captured.out

    assert "El cofre estaba vacío. Pierdes." in salida


def test_decisiones_invalidas(monkeypatch, capfd):
    """
    Simula decisiones inválidas y luego una ruta válida hacia el tesoro.
    """
    decisiones = iter([
        "arriba",   # decisión inválida en entrada
        "norte",    # ir a pasillo
        "izquierda",# decisión inválida en pasillo
        "este",     # ir a sala del tesoro
        "tomar"     # ganar
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(decisiones))

    main()

    captured = capfd.readouterr()
    salida = captured.out

    # Verificar que se muestren mensajes de decisión no válida
    assert salida.count("Decisión no válida") == 2
    assert "¡Felicidades! Has ganado el juego." in salida
