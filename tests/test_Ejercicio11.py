import builtins
from Ejercicio11_Validadorcc import main, validar_doc

def test_validar_doc():
    # Probando la función directamente
    assert validar_doc("1234") == True   # 1+2+3+4=10 → par
    assert validar_doc("111") == False   # 1+1+1=3 → impar
    assert validar_doc("abcd") == True   # sin dígitos → suma=0 → par

def test_main(monkeypatch, capfd):
    # Simular entradas: primero inválida, luego válida
    inputs = iter(["111", "1234"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    try:
        main()  # ejecutar el programa
    except SystemExit as e:
        assert str(e) == "Cédula válida"

    captured = capfd.readouterr()
    salida = captured.out
    # Verificar que el mensaje de error se mostró
    assert "Cédula inválida. Intente nuevamente." in salida
