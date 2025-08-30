''' Crea una función que reciba una frase y una letra. La función debe
devolver una lista con todos los índices (posiciones) en los que aparece
esa letra en la frase.
•	Ejemplo: encontrar_indices("Hola SENA", "a") debería devolver [3, 8].
Conceptos aplicados: Funciones, enumerate(), bucle for, list.append().
'''

indices = []

def Encontrar_indices(frase, letra):
    ''' Esta funcion se encarga de sagregar a la lista la letra que digite el usuario

     parametros
     frase:str
     letra:str
     caracter:str
     indices:list

     return indices
    '''
    for i, caracter in enumerate(frase): #recorre y enumera cada caracter de la frase
        if caracter == letra: #si caracter es igual a letra
            indices.append(i) #agregar a indices
    return indices
def main():
    frase = (str(input("Ingrese una frase\n")))
    letra = (str(input("Ingrese una letra\n")))
    result = Encontrar_indices(frase, letra) #resultado almacena la funcion encontrar_indices
    print(result)
if __name__ == "__main__":
 main()