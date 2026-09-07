'''
Crea un programa que solicite al usuario un número entero positivo N 
y utilice un ciclo while para sumar todos los números desde 1 hasta N.
'''

numero = int(input("Ingrese un numero entero positivo: "))

suma = 0
i = 1

while i <= numero:
    suma += i
    i +=1

print(f"La suma de los números del 1 al {numero} es: {suma}")