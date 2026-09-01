### Inventario de una tienda ###

'''
Crea un programa en Python que simule el inventario básico de una tienda. 
El programa debe solicitar al usuario el nombre de la tienda y crear una 
lista con cinco productos disponibles, junto con una tupla que contenga el 
precio correspondiente de cada producto. Luego, solicita al usuario la 
cantidad disponible de uno de los productos y calcula el valor total de 
ese producto en inventario multiplicando su precio por la cantidad 
disponible. Finalmente, muestra en pantalla el nombre de la tienda, los 
cinco productos con sus respectivos precios, la cantidad disponible del 
producto seleccionado y el valor total de ese producto en inventario. 
Utiliza únicamente los conceptos que has aprendido hasta el momento: 
variables, operadores, strings, listas, tuplas, índices, `input()`, 
`print()` y conversión de tipos.
'''

nombre_tienda = input("Ingrese el nombre de la tienda: ")

productos = ["Laptop", "Mouse", "Teclado", "Monitor", "Audifonos"]
precios = (1000, 150, 600, 300, 80)

print(f"\nBienvenido a {nombre_tienda}!")
print("Productos disponibles:")
print(f"1. {productos[0]} - Precio: Q{precios[0]}")
print(f"2. {productos[1]} - Precio: Q{precios[1]}")
print(f"3. {productos[2]} - Precio: Q{precios[2]}")
print(f"4. {productos[3]} - Precio: Q{precios[3]}")
print(f"5. {productos[4]} - Precio: Q{precios[4]}\n")

cantidad_1 = int(input(f"Ingrese la cantidad disponible de {productos[0]}: "))
cantidad_2 = int(input(f"Ingrese la cantidad disponible de {productos[1]}: "))
cantidad_3 = int(input(f"Ingrese la cantidad disponible de {productos[2]}: "))
cantidad_4 = int(input(f"Ingrese la cantidad disponible de {productos[3]}: "))
cantidad_5 = int(input(f"Ingrese la cantidad disponible de {productos[4]}: "))

valor_1 = precios[0] * cantidad_1
valor_2 = precios[1] * cantidad_2
valor_3 = precios[2] * cantidad_3
valor_4 = precios[3] * cantidad_4
valor_5 = precios[4] * cantidad_5

print(f"\nInventario de {nombre_tienda}:")
print(f"{productos[0]} - Cantidad: {cantidad_1} - Valor total: Q{valor_1}")
print(f"{productos[1]} - Cantidad: {cantidad_2} - Valor total: Q{valor_2}")
print(f"{productos[2]} - Cantidad: {cantidad_3} - Valor total: Q{valor_3}")
print(f"{productos[3]} - Cantidad: {cantidad_4} - Valor total: Q{valor_4}")
print(f"{productos[4]} - Cantidad: {cantidad_5} - Valor total: Q{valor_5}")