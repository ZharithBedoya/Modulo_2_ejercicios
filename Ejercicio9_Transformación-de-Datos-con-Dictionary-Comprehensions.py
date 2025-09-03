'''Tienes una lista de productos, donde cada producto es un diccionario:
[{"nombre": "Camisa", "precio": 50000}, {"nombre": "Pantalón", "precio": 80000}]:
•	Usa una dictionary comprehension para crear un nuevo diccionario donde
los nombres de los productos sean las claves y los precios con un 19% de IVA incluido
sean los valores.
Conceptos aplicados: Dictionary comprehensions, acceso a valores de diccionario.
'''


def main():
    productos=[
    {"nombre": "Camisa", "precio": 50000},
    {"nombre": "Pantalón", "precio": 80000}
        ]
    productos_iva = { producto["nombre"]: #clave
     round(producto["precio"] * 1.19) #mulriplica el precio cxon el iva dejando 2 decimales
        for producto in productos
    }
    for nombre, precio in productos_iva.items(): #recorrer el nombre y el precio de productos_iva
        print(f" El costo de -> {nombre} es de  ${precio}")

if __name__ == '__main__':
    main()
