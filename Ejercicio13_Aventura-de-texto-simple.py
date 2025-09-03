'''
Diseña un pequeño juego de aventura basado en texto. El jugador comienza en una habitación
y puede tomar decisiones ('ir al norte', 'abrir cofre'):
•	El juego debe tener al menos 3 habitaciones y un estado final (ganar o perder).
•	Utiliza un bucle while para el bucle principal del juego y estructuras if/elif/else para
 manejar las decisiones del jugador y el estado del juego.
Conceptos integrados: Bucles, condicionales, manejo de estado con variables, input().
'''
def main():
    print("Bienvenido a la aventura en texto!")
    habitacion = "entrada"

    while True:
        if habitacion == "entrada":
            print("Estás en la entrada de una cueva oscura.")
            decision = input("¿Quieres ir al norte o abrir el cofre? ").lower()

            if decision == "ir al norte" or decision == "norte":
                habitacion = "pasillo"
            elif decision == "abrir cofre":
                print("El cofre estaba vacío. Pierdes.")
                break
            else:
                print("Decisión no válida. Intenta de nuevo.")

        elif habitacion == "pasillo":
            print("Estás en un pasillo largo y estrecho.")
            decision = input("¿Quieres ir al este o al sur? ").lower()

            if decision == "ir al este" or decision == "este":
                habitacion = "sala_del_tesoro"
            elif decision == "ir al sur" or decision == "sur":
                habitacion = "entrada"
            else:
                print("Decisión no válida. Intenta de nuevo.")

        elif habitacion == "sala_del_tesoro":
            print("Has encontrado la sala del tesoro llena de oro.")
            decision = input("¿Quieres tomar el tesoro o salir? ").lower()

            if decision == "tomar el tesoro" or decision == "tomar":
                print("¡Felicidades! Has ganado el juego.")
                break
            elif decision == "salir":
                habitacion = "pasillo"
            else:
                print("Decisión no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
