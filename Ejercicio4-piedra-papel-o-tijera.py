'''Implementa el clásico juego para jugar contra la computadora.
•	El usuario elige una opción y la computadora elige una al azar.
•	El programa determina el ganador basándose en las reglas (piedra vence a tijeras, tijeras a papel, papel a piedra).
•	Se debe llevar un conteo de las victorias del jugador y de la computadora. El juego termina cuando uno de los dos llegue a 3 victorias.
Conceptos aplicados: random.choice(), bucle while, if/elif/else, contadores, f-strings.'''

import random


def Iniciar_juego(juego):
    '''Esta funcion imprime el mensaje de iniciar el juego

    parametros:
    juego: string

    '''
    if ((juego == "piedra") or
            (juego == "papel") or
            (juego == "tijera")): #si se cumple alguna de las condiciones
        print("Iniciando el juego...")
    else:
        juego = str(input("Intente nuevamente ingrese piedra, papel o tijera para continuar \n")).lower()


def definir_ganador(juego, compu):
    '''Esta funcion se encarga de definir quien gana el juegpo, si el jugador o la computadora

    parametros:
    juego: string
    compu: string

    returns: Empate
             has ganado el juego
             ha ganado la computadora
    '''

    if juego == compu: #si el juego "piedra, papel o tijera es el mismo que elige la computadora "
        return "Empate"
    elif (juego == "piedra" and compu == "tijera") or \
            (juego == "tijera" and compu == "papel") or \
            (juego == "papel" and compu == "piedra"): #si se cumple cualquier condicion
        return "Ha ganado el jugador"
    else:
        return "Ha ganado la computadora"


print("==Bienvenido al juego de piedra, papel o tijera===✊✋✌️")
opciones = ["piedra", "papel", "tijera"]
victorias_jugador = 0
victorias_computadora = 0
while victorias_jugador < 3 and victorias_computadora < 3: #mientras vistorias jugador y victorias computadora sean menor a 3
    juego = input("Elige piedra, papel o tijera: \n ").lower().strip()

    if juego not in opciones: #si en la variable juegos  no hay ninguna palabra de la lista opciones
        print("Opción inválida, intenta de nuevo.")
        continue

    compu = random.choice(opciones) #elige al azar una de las opciones de la lista opciones
    print(f"La computadora eligió: {compu}")

    resultado = definir_ganador(juego, compu) #almacenar en la variable resultado la funcion definir ganador

    if resultado == "Empate":
        print("Empate, nadie gana esta ronda.")
    elif resultado == "Jugador":
        victorias_jugador += 1
        print("¡Has ganado esta ronda!")
    else:
        victorias_computadora += 1
        print("La computadora gana esta ronda.")

    print(f"Puntuación -> \nJugador: {victorias_jugador}\n| Computadora: {victorias_computadora}\n")

if victorias_jugador == 3:
    print("¡Felicidades! Ganaste el juego.")
else:
    print("La computadora ganó el juego. Mejor suerte la próxima vez.")
