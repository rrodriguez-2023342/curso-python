opcion = 0

while opcion != 3:
    print("----- MENÚ -----")
    print("1. Saludar")
    print("2. Mostrar mensaje")
    print("3. Salir")

    opcion = int(input("Selecciona una opcion: "))

    if opcion == 1:
        print("¡Hola! Bienvenido al programa.")
    elif opcion == 2:
        print("Estás aprendiendo Python.")
    elif opcion == 3:
        print("Programa finalizado.")
    else:
        print("Opción inválida.")