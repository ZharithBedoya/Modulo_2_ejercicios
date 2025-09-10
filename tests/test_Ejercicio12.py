import random

def main(lanzamientos=10000):
    frecuencias = {}

    for _ in range(lanzamientos):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2
        frecuencias[suma] = frecuencias.get(suma, 0) + 1

    print(f"Frecuencia de la suma de dos dados tras {lanzamientos} lanzamientos:")
    for suma in range(2, 13):
        print(f"Suma {suma}: {frecuencias.get(suma, 0)} veces")
