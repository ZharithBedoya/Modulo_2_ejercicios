from Ejercicio6_AnalizadorPosiciones import Encontrar_indices,main


from Ejercicio6_AnalizadorPosiciones import Encontrar_indices

def test_indices_en_frase():
    assert Encontrar_indices("Hola SENA", "a") == [3, 8]

def test_letra_no_encontrada():
    assert Encontrar_indices("Hola SENA", "z") == []

def test_varias_ocurrencias():
    assert Encontrar_indices("oooo", "o") == [0, 1, 2, 3]
