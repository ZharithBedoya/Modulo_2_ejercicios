'''Crea un programa que pida un número y, usando un operador ternario, asigne a una variable el texto "Par" o "Impar". Luego, imprime el resultado. Adicionalmente, si el número es múltiplo de 5, debe imprimir un mensaje extra.
Conceptos aplicados: Operador ternario, operador módulo (%), if.
'''


def main():
    entrada = (input("Ingrese un numero\n")).strip()
    if not entrada:
        print("No debe ingresar vacios")
        return


    num = int(entrada)
    print("El numero ingresado es par" if num % 2 == 0
             else "El numero ingresado es impar")

if __name__ == '__main__':
    main()
