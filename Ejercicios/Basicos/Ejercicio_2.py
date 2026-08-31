### Sistema básico de compra ###

'''
Crea un programa en Python que simule una compra sencilla en una tienda. El programa debe 
solicitar al usuario el nombre de un producto, su precio y la cantidad que desea comprar, 
almacenar cada dato en una variable y calcular el costo total de la compra multiplicando 
el precio por la cantidad. Además, debes crear una lista que contenga tres productos 
adicionales y una tupla que contenga los precios correspondientes a esos tres productos. 
Finalmente, muestra en pantalla un resumen ordenado de la compra, incluyendo el producto 
principal, su precio, la cantidad, el costo total, los tres productos adicionales y sus 
respectivos precios. Para resolver el ejercicio utiliza únicamente los conceptos que has 
aprendido hasta el momento: variables, operadores, strings, listas, tuplas, 
`input()`, `print()`, índices y conversión de tipos.
'''

nombre_producto = input("Ingrese el nombre del producto: ")
precio_producto = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad que desea comprar: "))

precio_final = precio_producto * cantidad

productos_adicionales = ["Mouse", "Teclado", "Audifonos"]
precios_adicionales = (100, 200, 300)

print("-------- COMPRA --------")
print(f"Producto principal: {nombre_producto}")
print(f"Precio: Q{precio_producto}")
print(f"Cantidad: {cantidad}")
print("")
print(f"Costo total: {precio_final}")
print("")
print("-------- PRODUCTOS ADICIONALES --------")
print(f"{productos_adicionales[0]} -> Q{precios_adicionales[0]}")
print(f"{productos_adicionales[1]} -> Q{precios_adicionales[1]}")
print(f"{productos_adicionales[2]} -> Q{precios_adicionales[2]}")
