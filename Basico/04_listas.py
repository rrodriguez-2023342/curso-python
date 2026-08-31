### Listas ###

# Definición

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [35, 1.77, "Roberto", "Rodriguez"]

print(type(my_list))
print(type(my_other_list))

# Acceso a elementos y búsqueda

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(30))
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

print(my_other_list.index("Roberto")) # Devuelve el primer indice que tiene ese contenido

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

# Concatenación

print(my_list + my_other_list)
#print(my_list - my_other_list)

# Creación, inserción, actualización y eliminación

my_other_list.append("MoureDev") # Agrega el contenido en la ultima posicion de la lista
print(my_other_list)

my_other_list.insert(1, "Rojo") # Inserta el contenido en ese indice
print(my_other_list)

my_other_list[1] = "Azul" # Actualiza el contenido de ese indice
print(my_other_list)

my_other_list.remove("Azul") # Elimina el primer indice con este contenido
print(my_other_list)

my_list.remove(30)
print(my_list)

print(my_list.pop()) #Eliminar el ultimo indice de la lista
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

# Operaciones con listas

my_new_list = my_list.copy() # Hace una copia de la lista

my_list.clear() # Limpia toda la lista
print(my_list)
print(my_new_list)

my_new_list.reverse() # Le da la vuela a la lista
print(my_new_list)

my_new_list.sort() # Ordena la lista de forma ascendente
print(my_new_list)

# Sublistas

print(my_new_list[1:3])

# Cambio de tipo

my_list = "Hola Python"
print(my_list)
print(type(my_list))