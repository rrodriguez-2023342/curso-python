'''
Crea un programa que solicite al usuario un número entero N
y utilice un ciclo for para contar cuántos números pares 
existen desde 1 hasta N.
'''

numero = int(input("Ingrese un numero entero: "))

contador_pares = 0

for i in range(1, numero + 1):
    if i % 2 == 0:
        contador_pares += 1

print(f"El numero de numeros pares del 1 al {numero} es: {contador_pares}")