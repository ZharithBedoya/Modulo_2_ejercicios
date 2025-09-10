from Ejercicio9_Transformación import main

def test_productos_iva(capfd):
    main()  # ejecuta la función principal

    captured = capfd.readouterr()
    salida = captured.out

    # Verificar que la salida contenga los resultados correctos
    assert "El costo de -> Camisa es de  $59500" in salida
    assert "El costo de -> Pantalón es de  $95200" in salida
