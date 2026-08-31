### Salario mensual ###

'''
Crea un programa en Python que calcule el salario mensual de un empleado. 
El programa debe solicitar al usuario el nombre del empleado, el salario 
por hora y la cantidad de horas trabajadas durante el mes. Luego, debe 
calcular el salario bruto multiplicando el salario por hora por las horas 
trabajadas, calcular un descuento del 10% sobre el salario bruto y finalmente 
calcular el salario neto restando el descuento al salario bruto. Además, crea 
una lista que contenga tres beneficios que recibe el empleado y una tupla con 
tres números relacionados con su trabajo. Finalmente, muestra en pantalla un 
resumen con el nombre del empleado, salario por hora, horas trabajadas, salario 
bruto, descuento, salario neto, los tres beneficios y los tres números.
'''

nombre_empleado = input("Ingrese el nombre del empleado: ")
salario_x_hora = float(input("Ingrese el salario por hora: "))
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))

salario_bruto = salario_x_hora * horas_trabajadas
descuento = salario_bruto * 0.10
salario_neto = salario_bruto - descuento

beneficios = ["Parqueo gratis", "Descuentos en compras",  "Entradas de cine gratis"]
numeros = ("4913-8795", "4036-4916", "4549-5420")

print("-------- RESUMEN --------")
print(f"Nombre del empleado: {nombre_empleado}")
print(f"Salario por hora: Q{salario_x_hora}")
print(f"Horas trabajadas: {horas_trabajadas}")
print(f"Salario bruto: Q{salario_bruto}")
print(f"Descuento: Q{descuento}")
print(f"Salario neto: Q{salario_neto}")
print("")
print("-------- Beneficios --------")
print(f"Algunos beneficios del empleado son: \n 1. {beneficios[0]} \n 2. {beneficios[1]} \n 3. {beneficios[2]}")
print("")
print("-------- Números de la empresa --------")
print(f"Teléfono del jefe: {numeros[0]}")
print(f"Teléfono del secretario: {numeros[1]}")
print(f"Teléfono de recursos humanos: {numeros[2]}")