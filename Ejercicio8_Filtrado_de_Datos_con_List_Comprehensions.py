'''Dada una lista de números [-5, 10, -15, 20, -25, 30], utiliza una list comprehension
   para crear tres nuevas listas:
•	Una lista con solo los números positivos.
•	Una lista con los cuadrados de todos los números.
•	Una lista de strings que diga "positivo" o "negativo" para cada número, usando un
     ternario dentro de la comprensión.
•	Conceptos aplicados: List comprehensions, operador ternario.
'''


def main():


    lista = [-5, 10, -15, 20, -25, 30]
    positivos = [num for num in lista if num > 0]
    cuadrados = [num ** 2 for num in lista]
    strings = ["positivo" if num > 0 else "negativo" for num in lista]

    print(f"la lista es: {lista}")
    print(f"La lista con numeros positivos es {positivos}")
    print(f"La lista con los cuadrados es {cuadrados}")
    print(f"La lista de strings es {strings}")

if __name__ == '__main__':
    main()
