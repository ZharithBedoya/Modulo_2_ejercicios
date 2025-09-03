''' Dadas dos listas, una con nombres de estudiantes y otra con sus respectivas
notas finales, crea una función que las combine para generar un diccionario. Las claves
 serán los nombres y los valores las notas:
•	Luego, itera sobre el diccionario resultante para imprimir un reporte del tipo:
"El estudiante [Nombre] tiene una nota de [Nota]".
Conceptos aplicados: Funciones, zip(), dict(), bucle for sobre diccionarios.
'''


def main():
    nom_estu = []
    nota_estudiante = []
    print("🗒️==Notas de Estudiantes==🗒️")
    cant_st = input("Digite la cantidad de estudiantes que desea ingresar: ")

    if not cant_st.isdigit():
        print("Cantidad debe ser un número")
        exit()  # Finaliza el programa aquí
    else:
        cant = int(cant_st)

    for i in range(cant):  # en un rango definido por el que ingrese el usuario cant
        nombre = input(f"Ingrese el nombre de estudiante {i + 1}: ")
        while not nombre.isalpha():  # mientras que lka cant no sea numerica
            print("Nombre solo debe contenter letras")
            nombre = input("Ingrese nuevamente el nombre del estudiante: ")
        nota = input(f"Ingrese la nota del estudiante {nombre}: ")
        while not nota.isdigit():  # mientras que la nota no sea numerica
            print("La nota debe ser numeros")
            nota = input(f"Ingrese nuevamente la nota del estudiante {nombre}: ")

        nom_estu.append(nombre)  # agregar a num_estu el nombre
        nota_estudiante.append(nota)  # agregar a nota_estudiante la nota
        estudiante = dict(zip(nom_estu, nota_estudiante))  # unir las dos listas en un diccionario

        for estudiante, nota in estudiante.items():  # recorre las claves y los valores al mismo tiempo
            print(f"El estudiante {estudiante} tiene una nota de {nota}")

if __name__ == '__main__':
    main()
