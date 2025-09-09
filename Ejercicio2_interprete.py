'''Ejercicio 2: Intérprete de Comandos Sencillo
Desarrolla un programa que simule un menú de consola usando la estructura match-case. El programa mostrará una lista de comandos disponibles ("guardar", "cargar", "salir") y el usuario ingresará uno
•	El programa debe ejecutar una acción simulada para cada comando (ej. imprimir "Guardando archivo...").
•	Si el comando no es válido, debe mostrar un mensaje de error.
•	El programa debe seguir pidiendo comandos hasta que el usuario escriba "salir".
•	Conceptos aplicados: Bucle while, match-case, input(), lower().'''


def comandos():
    '''se define la variable llamada comandos
    donde guardara los comandos (casos) disponibles.

 ciclo:
   while: permite que se repita el cliclo hasta que no se ingrese
   el numero 3: opcion salir

    Casos :
    - 'guardar':simula guardar un archivo
    - 'cargar':simula cargar un archivo
    - 'salir': Finaliza el programa.

Si el comando no se digita correctamente, debe mostrar un mensaje de error.'''
    while True:
        comando = input("Digite \n1.Para Guardar.\n2.Para Cargar.\n3.Para salir. \n").lower().strip()

        match comando:
            case "1":
                print("Guardando archivo...")

            case "2":
                print("Cargando archivo...")

            case "3":
                print("Saliendo del comando...")
                break
            case _:
                print("Comando invalido🙄")
                print("DIGITA UN COMANDO VALIDO!😒")

def main():
    comandos() #ejecutar la funcion comandos
if __name__ == "__main__":
        main()