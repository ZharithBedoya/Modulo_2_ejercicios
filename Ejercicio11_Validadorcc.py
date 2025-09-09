''' Ejercicio 11: Validador de Cédula (Algoritmo Simple)
Escribe una función que valide un número de cédula (como string) basado en una regla simple:
la suma de sus dígitos debe ser un número par. La función debe devolver True si es válido y False si no:
•	Adicionalmente, el programa principal debe pedir al usuario su cédula hasta que ingrese una válida,
   usando un bucle.
Conceptos aplicados: Funciones, bucle while, conversión de tipos (str a int), bucle for sobre un string
'''

def validar_doc(documento):
    '''Esta funcion suma el documento ingresado si son digitos
    :parameter
    documento : strings

    :return
    True or false
    '''
    suma = sum(int(c) for c in documento if c.isdigit())  #sumar si documento son digitos
    return suma % 2 == 0

def main():
    while True: #mientras sea verdadero
        documento = input("Ingrese su número de cédula: ")
        if validar_doc(documento): #si se cumple validar documento
            exit("Cédula válida")
        else:
            print("Cédula inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
