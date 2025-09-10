from Ejercicio8_Filtrado import main

def test_listas(capfd):
    main()  # ejecutar la función principal

    captured = capfd.readouterr()
    salida = captured.out

    # Verificar que la salida contenga los mensajes correctos
    assert "la lista es: [-5, 10, -15, 20, -25, 30]" in salida
    assert "La lista con numeros positivos es [10, 20, 30]" in salida
    assert "La lista con los cuadrados es [25, 100, 225, 400, 625, 900]" in salida
    assert "La lista de strings es ['negativo', 'positivo', 'negativo', 'positivo', 'negativo', 'positivo']" in salida
