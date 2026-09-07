'''
Crea un programa que solicite al usuario un número 
entero N y utilice un ciclo for para sumar todos los 
números desde 1 hasta N.
'''

numero = int(input("Ingrese un numero entero: "))

for i in range(1, numero + 1):
    suma = sum(range(1, numero +1))
print(f"La suma de los números del 1 al {numero} es: {suma}")