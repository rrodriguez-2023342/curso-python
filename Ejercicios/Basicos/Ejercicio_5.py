### Factura de restaurante ###

'''
Crea un programa en Python que simule la cuenta de un restaurante. 
El programa debe solicitar al usuario su nombre y crear una lista con 
tres platos disponibles en el restaurante junto con una tupla que 
contenga el precio correspondiente de cada plato. Después, solicita al 
usuario la cantidad que consumió de cada uno de los tres platos y calcula 
el subtotal de cada plato multiplicando su precio por la cantidad consumida. 
Finalmente, calcula el total de la cuenta sumando los tres subtotales y muestra 
en pantalla un resumen que incluya el nombre del cliente, los tres platos, sus 
precios, las cantidades consumidas, los subtotales de cada plato y el total de 
la cuenta. Utiliza únicamente variables, operadores, strings, listas, tuplas, 
índices, `input()`, `print()` y conversión de tipos.
'''

nombre_cliente = input("Ingrese su nombre: ")

platos = ["Ensalada", "Sopa", "Pasta"]
precios = (15, 10, 20)

print(f"\nBienvenido al restaurante, {nombre_cliente}!\n")
cantidad_ensalada = int(input(f"Ingrese la cantidad de {platos[0]} consumida: "))
cantidad_sopa = int(input(f"Ingrese la cantidad de {platos[1]} consumida: "))
cantidad_pasta = int(input(f"Ingrese la cantidad de {platos[2]} consumida: "))

subtotal_ensalada = precios[0] * cantidad_ensalada
subtotal_sopa = precios[1] * cantidad_sopa
subtotal_pasta = precios[2] * cantidad_pasta

total_cuenta = subtotal_ensalada + subtotal_sopa + subtotal_pasta

print(f"\nResumen de la cuenta para {nombre_cliente}:")
print(f"{platos[0]} - Precio: Q{precios[0]} - Cantidad: {cantidad_ensalada} - Subtotal: Q{subtotal_ensalada}")
print(f"{platos[1]} - Precio: Q{precios[1]} - Cantidad: {cantidad_sopa} - Subtotal: Q{subtotal_sopa}")
print(f"{platos[2]} - Precio: Q{precios[2]} - Cantidad: {cantidad_pasta} - Subtotal: Q{subtotal_pasta}")
print(f"\nTotal de la cuenta: Q{total_cuenta}")