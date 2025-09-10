''' Crea una función que reciba una frase y una letra. La función debe
devolver una lista con todos los índices (posiciones) en los que aparece
esa letra en la frase.
•	Ejemplo: encontrar_indices("Hola SENA", "a") debería devolver [3, 8].
Conceptos aplicados: Funciones, enumerate(), bucle for, list.append().
'''
def Encontrar_indices(frase, letra):
    """
    Devuelve una lista con todos los índices donde aparece la letra en la frase.
    La comparación ignora mayúsculas/minúsculas.
    """
    indices = []  # debe estar dentro de la función para reiniciarse cada vez
    for i, caracter in enumerate(frase):
        if caracter.lower() == letra.lower():
            indices.append(i)
    return indices


def main():
    frase = input("Ingrese una frase\n")
    letra = input("Ingrese una letra\n")
    result = Encontrar_indices(frase, letra)
    print(result)


if __name__ == "__main__":
    main()
