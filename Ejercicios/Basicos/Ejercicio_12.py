'''
Crea un programa que solicite al usuario un número entero positivo. 
El programa debe utilizar un ciclo while para contar desde 1 hasta 
ese número, mostrando cada número en pantalla.
'''

numero = int(input("Ingrese un numero entero positivo: "))

i = 1
while i <= numero:
    print(i)
    i += 1