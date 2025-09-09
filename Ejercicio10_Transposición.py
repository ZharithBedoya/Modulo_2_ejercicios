'''Crea una función que reciba una matriz (lista de listas) y devuelva su transpuesta.
   La transpuesta se logra intercambiando filas por columnas.
•	Ejemplo: [[1, 2, 3], [4, 5, 6]] se convierte en [[1, 4], [2, 5], [3, 6]].
•	Resuelve este problema usando bucles for anidados y luego intenta resolverlo con
    una list comprehension anidada.
Conceptos aplicados: Listas anidadas (matrices), bucles anidados, list comprehensions anidadas.
'''

def transponer_bucles(matriz):
    '''Esta funcion se encarga de almacenar la trsnspuesta de la matriz
    matriz = [[1, 2, 3],
          [4, 5, 6]]
     parametros
     matriz:list de listas

     :return
     transpuesta '''
    filas = len(matriz) #1, 2, 3
                       # 4, 5, 6
    columnas = len(matriz[0]) #1,4,2,5,3,6
    transpuesta = []  #matriz para almacenar
    for i in range(columnas):
        fila_transpuesta = []
        for j in range(filas):
            fila_transpuesta.append(matriz[j][i]) #agregar a fila_transpuesta la matriz resultante de j*i
        transpuesta.append(fila_transpuesta)    #agrega a transpuesta el resultado de fila transpuesta
    return transpuesta


def transponer_listcomp(matriz):
    ''' Esta funcion se encarga de almacenar la trsnspuesta de la matriz
    matriz = [[1, 2, 3],
          [4, 5, 6]]
     parametros
     matriz:list de listas
     :return
     [[matriz[j][i] for j in range(len(matriz))]
     '''
    return [[matriz[j][i] for j in range(len(matriz))]
    for i in range(len(matriz[0]))] #list comprehension

# Ejemplo
matriz = [[1, 2, 3],
          [4, 5, 6]]

print("Transpuesta con bucles for:")
print(transponer_bucles(matriz))

print("\nTranspuesta con list comprehension:")
print(transponer_listcomp(matriz))

