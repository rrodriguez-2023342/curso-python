numero_secreto = 7
intentos = 0

while True:
    numero = int(input("Ingrese un numero entero: "))
    intentos += 1

    if numero < numero_secreto:
        print("El número secreto es mayor.")
    elif numero > numero_secreto:
        print("El número secreto es menor.")
    else:
        print("¡Correcto! Adivinaste el número.")
        break

print(f"Lo lograste en {intentos} intentos!")