### Sistema de descuentos ###

'''
Crea un programa en Python que solicite el nombre de un cliente y 
el total de su compra. El programa debe determinar el descuento según 
el monto de la compra: si la compra es menor a Q100, no recibe descuento; 
si está entre Q100 y Q499.99, recibe un 5% de descuento; si está entre 
Q500 y Q999.99, recibe un 10%; y si es de Q1000 o más, recibe un 15%. 
Guarda el porcentaje de descuento en una variable, calcula el monto del 
descuento y el total final a pagar. Finalmente, muestra el nombre del cliente, 
el total original, el porcentaje de descuento, el monto descontado y el total 
a pagar.
'''

nombre = input("Ingrese el nombre del cliente: ")
total_compra = float(input("Ingrese el total de la compra: "))

if total_compra < 100:
    descuento_porcentaje = 0
elif total_compra < 500:
    descuento_porcentaje = 0.05
elif total_compra < 1000:
    descuento_porcentaje = 0.10
else:
    descuento_porcentaje = 0.15

monto_descuento = total_compra * descuento_porcentaje
total_pagar = total_compra - monto_descuento

print("---- FACTURA ----")
print(f"Cliente: {nombre}")
print(f"Total original: Q{total_compra:.2f}")
print(f"Descuento: {descuento_porcentaje * 100:.0f}%")
print(f"Monto descontado: Q{monto_descuento:.2f}")
print(f"Total a pagar: Q{total_pagar:.2f}")