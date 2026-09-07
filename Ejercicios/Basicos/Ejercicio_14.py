'''
Crea un programa que solicite al usuario un número entero 
positivo N y utilice un ciclo while para recorrer los números 
desde 1 hasta N.
'''

numero = int(input("Ingrese un numero entero positivo: "))

i = 1
numeros_pares = 0

while i <= numero:
    if i % 2 == 0:
        print(i)
        numeros_pares += 1

    i += 1

print(f"La cantidad de numeros pares del 1 al {numero} es: {numeros_pares}")