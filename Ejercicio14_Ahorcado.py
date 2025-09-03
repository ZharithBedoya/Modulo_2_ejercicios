'''
Diseña una versión para consola del clásico juego del "Ahorcado". El programa debe ser capaz de gestionar toda la lógica del juego, desde la selección de la palabra hasta determinar si el jugador ha ganado o perdido.
Lógica del Juego:
•	El programa debe tener una lista predefinida de palabras secretas y seleccionar una al
    azar para cada partida.
•	Debe mostrar al jugador el "tablero", que consiste en guiones bajos representando las
   letras de la palabra secreta y una lista de las letras ya intentadas.
•	El jugador tiene un número limitado de intentos (ej. 6 vidas).
•	En cada turno, el jugador ingresa una letra. El programa debe validar si la entrada
    es una sola letra y si no ha sido intentada antes.
•	Si la letra está en la palabra secreta, se revelan todas sus apariciones
    (ej. _ _ _ _ _ -> _ a _ a _). Si no está, el jugador pierde una vida.
•	El juego termina cuando el jugador adivina todas las letras (gana) o se queda
    sin vidas (pierde).
'''
import random

def elegir_palabra(palabras):
    ''' Esta funcion se encarga de escoger una palabra de la lista
    palabras al azar

    :param palabras:
    :return: random.choice(palabras)
    '''
    return random.choice(palabras) #escoger una palabra al azar

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    ''' Esta funcion se encarga de validar si la letra esta en la palabra secreta

    :param palabra_secreta:
    :param letras_adivinadas:

    '''
    tablero = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra + " "  #agregar la letra al tablero
        else:
            tablero += "_ " #agregar una linea por cada letra de lsa lista palabras
    print("Palabra: ", tablero.strip()) #

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
        print(f"Letras intentadas: {' '.join(letras_intentadas)}") #unir los elementos en un solo string
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

        # Verificar si el jugador ganó
        if all(letra in letras_adivinadas for letra in palabra_secreta):
            print(f"¡Felicidades! Has adivinado la palabra: {palabra_secreta}")
            break

        if vidas == 0: #si ya no quedan vidsas se termina el juego
            exit(f"¡Has perdido! La palabra era: {palabra_secreta}")

if __name__ == '__main__':
    main()