'''Ejercicio 15: Proyecto Final - Batalla Naval Simplificada
Crea una versión del juego "Batalla Naval" en una cuadrícula de 5x5:
•	El programa debe "esconder" un barco de 3 casillas en una fila o columna aleatoria.
•	El jugador tiene 10 turnos para adivinar las coordenadas (ej. "A3") y hundir el barco.
•	El programa debe gestionar el tablero (una lista de listas), validar la entrada del usuario, indicar si un disparo fue "Agua" o "Tocado", y llevar la cuenta de los turnos.

•	Al final, debe declarar si el jugador ganó o perdió.
Conceptos integrados: Lógica de juegos, listas anidadas, funciones, bucles while y for, condicionales, random, manipulación de strings.
'''

import random


def crear_tablero():
    ''' Esta funcion se encarga de crear el tablero para el juego
    '''
    # Crea tablero 5x5 con guiones bajos para representar casillas vacías
    return [["_"] * 5 for _ in range(5)]


def mostrar_tablero(tablero):
    ''' Esta funcion se encarga de mostrar el tablero
    :parameter tablero: lista de listas
    '''
    print("  A B C D E")
    for idx, fila in enumerate(tablero, start=1):
        print(f"{idx} " + " ".join(fila))


def posicion_valida(pos):
    # Validar formato correcto: letra A-E y número 1-5
    if len(pos) != 2:
        return False
    letra, num = pos[0].upper(), pos[1]
    if letra not in "ABCDE":
        return False
    if num not in "12345":
        return False
    return True


def convertir_coordenada(pos):
    # Convertir entrada ('A1') a índices (fila, columna) (0-based)
    letra, num = pos[0].upper(), pos[1]
    fila = int(num) - 1
    columna = ord(letra) - ord('A')
    return fila, columna


def colocar_barco():
    # Escoger aleatoriamente orientación y posición para un barco de 3 casillas
    orientacion = random.choice(['horizontal', 'vertical'])
    if orientacion == 'horizontal':
        fila = random.randint(0, 4)
        columna = random.randint(0, 2)  # Max columna para que quepa el barco
        posiciones = [(fila, columna + i) for i in range(3)]
    else:
        fila = random.randint(0, 2)
        columna = random.randint(0, 4)
        posiciones = [(fila + i, columna) for i in range(3)]
    return posiciones


def main():
    tablero = crear_tablero()
    barco = colocar_barco()
    intentos = 10
    aciertos = set()

    print("¡Bienvenido a Batalla Naval simplificada!")
    print("Tienes 10 turnos para hundir un barco de 3 casillas.")
    print("Introduce coordenadas como 'A1', 'B3', etc.")

    while intentos > 0:
        mostrar_tablero(tablero)
        print(f"Turnos restantes: {intentos}")
        disparo = input("Ingresa coordenada para disparar: ").strip()

        if not posicion_valida(disparo):
            print("Coordenada inválida. Usa formato de letra A-E y número 1-5.")
            continue

        fila, col = convertir_coordenada(disparo)

        if tablero[fila][col] != "_":
            print("Ya disparaste ahí. Intenta otra coordenada.")
            continue

        if (fila, col) in barco:
            print("¡Tocado!")
            tablero[fila][col] = "X"
            aciertos.add((fila, col))
            if len(aciertos) == 3:
                print("¡Felicidades! Hundiste el barco.")
                mostrar_tablero(tablero)
                break
        else:
            print("Agua.")
            tablero[fila][col] = "O"
            intentos -= 1

    else:
        print("Juego terminado. Te quedaste sin turnos.")
        print(f"El barco estaba en las posiciones: {[(chr(c + ord('A')) + str(r + 1)) for r, c in barco]}")
        mostrar_tablero(tablero)


if __name__ == "__main__":
    main()
