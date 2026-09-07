'''
Crea un programa en Python que solicite al usuario un número 
entero y muestre su tabla de multiplicar del 1 al 10 utilizando 
un ciclo for.
'''

numero = int(input("Ingrese un numero entero: "))

for i in range(1, 11):
    resultado =  numero * i
    print(f"{numero} x {i} = {resultado}")