### Ejercicio con elif ###

'''
Crea un programa en Python que solicite al usuario su nombre y su edad. 
El programa debe utilizar condicionales para clasificar a la persona 
según su edad: si tiene entre 0 y 12 años debe clasificarse como niño, 
si tiene entre 13 y 17 años debe clasificarse como adolescente, si tiene 
entre 18 y 59 años debe clasificarse como adulto y si tiene 60 años o más 
debe clasificarse como adulto mayor. Guarda la clasificación obtenida en 
una variable y muestra un mensaje con el nombre, la edad y la clasificación 
de la persona.
'''

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

if edad < 0:
    print(f"{nombre}, no puedes ingresar una edad negativa!")
elif edad <= 12:
    clasificacion = "niño"
elif edad <= 17:
    clasificacion = "adolescente"
elif edad <= 59:
    clasificacion = "adulto"
else:
    clasificacion = "adulto mayor"

print("---- RESULTADO ----")
print(f"{nombre} tiene {edad} años, por lo tanto es un {clasificacion}")