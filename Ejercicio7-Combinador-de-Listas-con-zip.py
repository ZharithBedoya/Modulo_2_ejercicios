''' Dadas dos listas, una con nombres de estudiantes y otra con sus respectivas
notas finales, crea una función que las combine para generar un diccionario. Las claves
 serán los nombres y los valores las notas:
•	Luego, itera sobre el diccionario resultante para imprimir un reporte del tipo:
"El estudiante [Nombre] tiene una nota de [Nota]".
Conceptos aplicados: Funciones, zip(), dict(), bucle for sobre diccionarios.
'''
nom_estu = []
nota_estudiante = []

print("🗒️==Notas de Estudiantes==🗒️")


def main():
    cant = int(input("Digite la cantidad de estudiantes que desea ingresar: "))

    for i in range(cant): #en un rango definido por el que ingrese el usuario cant
        nombre = input(f"Ingrese el nombre de estudiante {i + 1}: ")
        nota = input(f"Ingrese la nota de estudiante {i + 1}: ")
        nom_estu.append(nombre) #agregar a num_estu el nombre
        nota_estudiante.append(nota) #agregar a nota_estudiante la nota

        estudiante = dict(zip(nom_estu, nota_estudiante)) #unir las dos listas en un diccionario

    for estudiante, nota in estudiante.items(): #para estudiantes agregar la nota como un iten a la lista estudiante
        print(f"El estudiante {nom_estu} tiene una nota de {nota_estudiante}")


if __name__ == '__main__':
    main()