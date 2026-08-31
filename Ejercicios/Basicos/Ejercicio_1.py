### Información de una persona ###

'''
Crea un programa que almacene en variables la siguiente información de una persona:

Nombre
Edad
Ciudad
Una lista con 3 hobbies
Una tupla con 3 números favoritos 
'''

nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
ciudad = input("Ingresa tu ciudad: ")

hobbies = [
    input("Ingresa tu primer hobby: "),
    input("Ingresa tu segundo hobby: "),
    input("Ingresa tu tercer hobby: ")
]

numeros_fav = (1, 2, 3)


print("--------------------------------------------------------")
print(f"Mi nombre es {nombre}, tengo {edad} años y vivo en {ciudad}.")
print(f"Algunos de mis hobbies son: {hobbies[0]}, {hobbies[1]}, {hobbies[2]}.")
print(f"Mis numeros favoritos son: {numeros_fav[0]}, {numeros_fav[1]}, {numeros_fav[2]}")
print("--------------------------------------------------------")

nueva_edad = int(edad) + 5

print(f"En 5 años tendré {nueva_edad}")
print(f"Mi primer hobbie es: {hobbies[0]}")
print(f"Tu numero favorito mas grande es: {numeros_fav[2]}")