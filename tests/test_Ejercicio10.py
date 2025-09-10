from Ejercicio10_Transposición import transponer_bucles, transponer_listcomp

def test_transponer_bucles():
    matriz = [[1, 2, 3],
              [4, 5, 6]]
    resultado = transponer_bucles(matriz)
    esperado = [[1, 4],
                [2, 5],
                [3, 6]]
    assert resultado == esperado

def test_transponer_listcomp():
    matriz = [[1, 2, 3],
              [4, 5, 6]]
    resultado = transponer_listcomp(matriz)
    esperado = [[1, 4],
                [2, 5],
                [3, 6]]
    assert resultado == esperado
