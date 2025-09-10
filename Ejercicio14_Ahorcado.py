import random

def elegir_palabra(palabras):
    """Escoge una palabra al azar de la lista"""
    return random.choice(palabras)

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    """Muestra el estado actual del tablero de letras adivinadas"""
    tablero = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    print("Palabra: ", tablero.strip())

def main():
    palabras = [
        "programacion", "ordenador", "teclado", "pantalla", "internet", "bandera",
        "montana", "elefante", "camarero", "libertad", "escritorio", "ventana",
        "telefono", "murcielago", "castillo", "bicicleta", "jirafa", "zapato",
        "cascada", "muralla"
    ]

    palabra_secreta = elegir_palabra(palabras)
    letras_adivinadas = []
    letras_intentadas = []
    vidas = 6

    print("¡Bienvenido al juego del Ahorcado!")

    while vidas > 0:
        mostrar_tablero(palabra_secreta, letras_adivinadas)
        print(f"Letras intentadas: {' '.join(letras_intentadas)}")
        print(f"Vidas restantes: {vidas}")

        letra = input("Ingresa una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor ingresa solo una letra válida.")
            continue

        if letra in letras_intentadas:
            print("Ya intentaste esa letra. Intenta con otra.")
            continue

        letras_intentadas.append(letra)

        if letra in palabra_secreta:
            letras_adivinadas.append(letra)
            print("¡Bien! Has encontrado una letra.")
        else:
            vidas -= 1
            print("La letra no está en la palabra.")

        if all(letra in letras_adivinadas for letra in palabra_secreta):
            print(f"¡Felicidades! Has adivinado la palabra: {palabra_secreta}")
            break

        if vidas == 0:
            exit(f"¡Has perdido! La palabra era: {palabra_secreta}")

if __name__ == '__main__':
    main()
