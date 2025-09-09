import builtins
import pytest
from Ejercicio3_validar_contrasena import cantidad_caracteres,mayusculas_pasword,validar_numeros,validar_vacios

def test_cantidad_caracteres(capsys):
    # Muy corta
    assert cantidad_caracteres("abc") is False
    captured = capsys.readouterr()
    assert "muy corta" in captured.out

    # Correcta
    assert cantidad_caracteres("abcdefgh") is True


def test_mayusculas_pasword(capsys):
    # Sin mayúsculas
    assert mayusculas_pasword("abcdefg1") is False
    captured = capsys.readouterr()
    assert "mayuscula" in captured.out

    # Con mayúscula
    assert mayusculas_pasword("Abcdefg1") is True


def test_validar_numeros(capsys):
    # Sin números
    assert validar_numeros("Abcdefgh") is False
    captured = capsys.readouterr()
    assert "al menos un numero" in captured.out

    # Con número
    assert validar_numeros("Abcdefg1") is True


def test_validar_vacios(capsys):
    # Solo espacios
    assert validar_vacios("   ") is None
    captured = capsys.readouterr()
    assert "no puede ser vacia" in captured.out

    # Contraseña normal
    assert validar_vacios("Abc12345") is None
    captured = capsys.readouterr()
    assert captured.out == ""
