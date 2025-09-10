'''Crea un programa que pida un número y, usando un operador ternario, asigne a una variable el texto "Par" o "Impar". Luego, imprime el resultado. Adicionalmente, si el número es múltiplo de 5, debe imprimir un mensaje extra.
Conceptos aplicados: Operador ternario, operador módulo (%), if.
'''
def par_impar(num: int) -> str:
    """
    Función que determina si un número es par o impar.
    Además, agrega un mensaje si es múltiplo de 5.

    Parámetros:
        num (int): número a evaluar.

    Retorna:
        str: mensaje indicando si es par/impar y si es múltiplo de 5.
    """
    mensaje = "El numero ingresado es par" if num % 2 == 0 else "El numero ingresado es impar"
    if num % 5 == 0:
        mensaje += " y además es múltiplo de 5"
    return mensaje


def main():
    entrada = (input("Ingrese un numero\n")).strip()
    if not entrada:
        print("No debe ingresar vacios")
        return

    num = int(entrada)
    print(par_impar(num))


if __name__ == '__main__':
    main()

