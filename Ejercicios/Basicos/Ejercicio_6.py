### Sistema de calificaciones ###

'''
Crea un programa en Python que solicite al usuario el nombre de un
estudiante y su calificación final. El programa debe almacenar el 
nombre y la calificación en variables y utilizar condicionales para 
determinar si el estudiante aprobó o reprobó la materia. Si la 
calificación es mayor o igual a 60, debe mostrar un mensaje indicando 
que el estudiante aprobó; si la calificación es menor a 60, debe indicar 
que reprobó. Además, crea una lista con tres materias y una tupla con 
tres calificaciones correspondientes a esas materias. Finalmente, muestra 
el nombre del estudiante, su calificación final, el resultado obtenido y 
las tres materias con sus respectivas calificaciones. Utiliza únicamente 
los conceptos que has aprendido hasta el momento: variables, operadores, 
strings, listas, tuplas, índices, `input()`, `print()`, conversión de tipos 
y condicionales (`if`, `elif`, `else`).
'''

nombre_estudiante = input("Ingrese el nombre del estudiante: ")
calificacion = int(input("Ingrese la calificación del estudiante: "))

if calificacion >= 60:
    resultado =  "aprobó"
else:
    resultado = "reprobó"

materias = ["Matemáticas", "Ciencias", "Historia"]
calificaciones = (85, 54, 60)

print(f"--------- RESULTADO FINAL DEL ESTUDIANTE: {nombre_estudiante} ---------")
print(f"Calificación final: {calificacion}")
print(f"Resultado: {resultado}")
print("Materias y calificaciones:")
print(f"{materias[0]}: {calificaciones[0]}")
print(f"{materias[1]}: {calificaciones[1]}")
print(f"{materias[2]}: {calificaciones[2]}")