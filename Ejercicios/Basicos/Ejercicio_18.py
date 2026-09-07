saldo = 100
opcion = 0

while opcion != 4:
    print("--- CAJERO AUTOMATICO ---")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

    opcion = float(input("Seleccione una opcion: "))

    if opcion == 1:
        print("")
        print(f"El saldo actual es de {saldo}")
        print("")
    elif opcion == 2:
        print("")
        ingreso = float(input("Ingrese la cantidad de dinero que desea ingresa: "))
        saldo += ingreso
        print("")
    elif opcion == 3:
        print("")
        retiro = float(input("Ingrese la cantidad que desea retirar: "))

        if retiro > saldo:
            print("Saldo insuficiente.")
            print("")
        else: 
            saldo -= retiro
        print("")
    elif opcion == 4:
        print("")
        print("Gracias por utilizar el cajero.")
        print("")
    else:
        print("")
        print("Opcion invalida")
        print("")
