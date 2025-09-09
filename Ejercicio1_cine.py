'''Ejercicio 1: Sistema de Precios de Entradas de Cine
Crea un programa que calcule el precio de una entrada de cine basándose en la edad del
cliente y si es estudiante:
Reglas (menores de 12 años): $10.000.
•	Jóvenes (12 a 17 años): $15.000.
•	Adultos (18 años en adelante): $20.000.
•	Si el cliente es estudiante (independientemente de la edad), tiene un 10% de descuento.
El programa debe pedir la edad y si es estudiante ('si' o 'no').'''

def validar_edad(edad):
    '''Esta función se encarga de validar
    la edad del usuario

    Parámetros:
    edad (int): edad del usuario

    Return:
    retorna la variable precio o mensaje de error
    '''
    if edad <= 0 or edad > 80:
        return "Edad inválida"
    elif edad < 12:
        precio = 10000
    elif 12 <= edad <= 17:
        precio = 15000
    else:
        precio = 20000
    return precio


def validar_estudiante(precio, estudiante):
    '''Esta función valida si el usuario es estudiante.

    Parámetros:
    precio (float): precio de la entrada
    estudiante (str): si el usuario es estudiante

    Retorna:
    Mensaje con el precio final
    '''
    if estudiante == 'si':
        precio *= 0.90
        return f"El costo de su factura con descuento del 10% es de {precio}"
    elif estudiante == 'no':
        return f"El costo de su entrada es {precio}"
    else:
        return "Entrada para estudiante inválida. Por favor, digite 'si' o 'no'."


def main():
    print("=== 😎 Costos De Entrada a Cine 😎 ===")

    # Validar edad
    entrada_edad = input("Ingrese la edad del usuario: ").strip()
    if entrada_edad == "":
        print("❌ La edad no puede estar vacía.")
        return  # termina el programa
    if not entrada_edad.isdigit():
        print("❌ La edad debe ser un número válido.")
        return
    edad = int(entrada_edad)
    precio = validar_edad(edad)


    # Validar si es estudiante
    estudiante = input("¿El usuario es estudiante? (Digite 'si' o 'no'): ").strip().lower()
    if estudiante == " ":
        print("Entrada para estudiante inválida. Por favor, digite 'si' o 'no'.")
        return

    resultado = validar_estudiante(precio, estudiante)
    print("✅", resultado)


if __name__ == "__main__":
    main()
