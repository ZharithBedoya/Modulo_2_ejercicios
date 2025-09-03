'''
•	Crea un programa que simule el lanzamiento de dos dados 10,000 veces.
•	Usa un diccionario para contar la frecuencia de cada posible suma de los dados (de 2 a 12).
•	Al final, imprime un reporte con la frecuencia de cada suma.
Conceptos aplicados: random.randint(), bucles, diccionarios como contadores, método get().
'''

import random

def main():
    lanzamientos = 10000
    frecuencias = {}

    for _ in range(lanzamientos): #se repite 10.000 veces
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2 #suma los lanzamientos de los datos

        # Contar la frecuencia usando get() para inicializar en 0 si no existe
        frecuencias[suma] = frecuencias.get(suma, 0) + 1

    print("Frecuencia de la suma de dos dados tras 10,000 lanzamientos:")
    for suma in range(2, 13):
        print(f"Suma {suma}: {frecuencias.get(suma, 0)} veces")
if __name__ == "__main__":
    main()
