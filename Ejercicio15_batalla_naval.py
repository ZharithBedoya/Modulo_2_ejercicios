import random


def crear_tablero():
    ''' Crea un tablero 5x5 para el juego '''
    return [["_"] * 5 for _ in range(5)]


def mostrar_tablero(tablero):
    ''' Muestra el tablero en consola '''
    print("  A B C D E")
    for idx, fila in enumerate(tablero, start=1):
        print(f"{idx} " + " ".join(fila))


def posicion_valida(pos):
    ''' Valida que la coordenada ingresada sea correcta '''
    if len(pos) != 2:
        return False
    letra, num = pos[0].upper(), pos[1]
    if letra not in "ABCDE" or num not in "12345":
        return False
    return True


def convertir_coordenada(pos):
    ''' Convierte la coordenada (A1) a índices de lista '''
    letra, num = pos[0].upper(), pos[1]
    fila = int(num) - 1
    columna = ord(letra) - ord('A')
    return fila, columna


def colocar_barco():
    ''' Coloca un barco de 3 casillas al azar '''
    orientacion = random.choice(['horizontal', 'vertical'])
    if orientacion == 'horizontal':
        fila = random.randint(0, 4)
        columna = random.randint(0, 2)
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
        print(f"El barco estaba en las posiciones: "
              f"{[(chr(c + ord('A')) + str(r + 1)) for r, c in barco]}")
        mostrar_tablero(tablero)


if __name__ == "__main__":
    main()
