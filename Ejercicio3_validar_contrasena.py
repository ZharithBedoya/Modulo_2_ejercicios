'''Escribe un programa que pida al usuario crear una contraseña
y la valide usando un bucle while.
 El bucle solo terminará cuando la contraseña cumpla todos los criterios:
•	Mínimo 8 caracteres de longitud.
•	Contiene al menos una letra mayúscula.
•	Contiene al menos un número.
•	En cada intento fallido, el programa debe indicar qué regla no se cumplió.
Bucle while True, if/elif/else, len(), métodos de string
(isupper(), islower(), isdigit()), break.'''


def cantidad_caracteres(pasword):

    '''validar si la contrasela contiene mas de 8 caracteres

       Parametros:
       pasword

        return false
        return true
        '''
    if len(pasword) < 8: #len recorre la variable y verifica que no existan menos de 8 caracteres
       print("❌Contraseña ingresada es muy corta, debe contener por lo menos 8 caracteres")

       return False
    else:
       return True

def mayusculas_pasword(pasword):

    ''' funcion para validar si en la contraseña se ingresan por lo menos una mayusculas
    :parametros
    pasword

    return true
    :return false

    '''
    if any(c.isupper() for c in pasword): #se recorre pasword para verificar si tiene mayusculas
        return True
    else:
        print("La contraseña debe contener al menos un caracter en mayuscula")
        return False


def validar_numeros(pasword):
    ''' funcion para validar si en la contraseña se ingresan por lo menjos un numero
        :parametros
        pasword

        return true
        :return false

        '''
    if any(c.isdigit() for c in pasword): #recore la contraseña y verifica si hay numeros
        return True
    else:
        print("La contraseña debe contener al menos un numero")
        return False



def validar_vacios(pasword):
    ''' funcion para validar si en la contraseña se ingresan campos vacios
        :parametros
        pasword

        return true
        :return false

        '''
    if pasword.strip() == "": #se encarga de eliminar espaciosen blanco
        print("Una contraseña no puede ser vacia ")


def main():
    while True:
     pasword = str(input("Ingrese una contraseña para almacenarla en el programa debe contener 8 caracteres \n"))
     cantidad_caracteres(pasword)
     mayusculas_pasword(pasword)
     validar_numeros(pasword)
     validar_vacios(pasword)
     print("Ingresando.........")
     exit("✔️Contraseña almacenada corractamente😎")

if __name__ == '__main__':
    main()
