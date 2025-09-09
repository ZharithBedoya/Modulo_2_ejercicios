'''Ejercicio 1: Sistema de Precios de Entradas de Cine
Crea un programa que calcule el precio de una entrada de cine basándose en la edad del
cliente y si es estudiante:
Reglas (menores de 12 años): $10.000.
•	Jóvenes (12 a 17 años): $15.000.
•	Adultos (18 años en adelante): $20.000.
•	Si el cliente es estudiante (independientemente de la edad), tiene un 10% de descuento.
El programa debe pedir la edad y si es estudiante ('si' o 'no').'''

def validar_edad(edad):
    '''Esta funcion se encarga de validad
     la edad del usuario

     Parametros:
     edad(int): edad del usuario
     Return
     retorna la variable precio '''

    if edad <= 0 or edad > 80:
        return "Edad invalida"
    elif edad < 12:
        precio = 10000
    elif 12 <= edad <= 17:
        precio = 15000
    else:
        precio = 20000
    return precio  #retornar precio

def validar_estudiante(precio, estudiante):
    '''Esta funcion se encarga de validar
    si el usuario es estudiante

    Parametros:
    precio(double): precio de la entrada al cine
    estudiante(string): el usuario es estudiante

    Return
    retorna la variable precio '''


    if estudiante == 'si':
        precio *=  0.90
        return(f"El costo de su factura con descuento del 10% es de {precio}")
    elif estudiante == 'no':
        return(f"El costo de su entrada es {precio}")
    else:
        return("Entrada para estudiante inválida. Por favor, digite 'Si' o 'No'.")


def main():
    print("=== 😎 Costos De Entrada a Cine 😎 ===")
    edad = int(input("Ingrese la edad del Usuario \n"))
    precio = validar_edad(edad) #el valor de la funcion se guarda en la variable precio
    estudiante = input("¿El usuario es estudiante? Digite Si o No \n").strip().lower()
    validar_estudiante(precio, estudiante)


if __name__ == "__main__":
    main()
