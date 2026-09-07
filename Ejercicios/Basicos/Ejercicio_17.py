contraseña_correcta = "python123"
intentos = 0

while True:
    contraseña = str(input("Ingrese la contraseña: "))
    intentos += 1

    if contraseña != contraseña_correcta:
        print("Contraseña incorrecta. Intenta nuevamente.")
    elif contraseña == contraseña_correcta:
        print("¡Acceso permitido!")
        break

print(f"Intentos realizados: {intentos}")