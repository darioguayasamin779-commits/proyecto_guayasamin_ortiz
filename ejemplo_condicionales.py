# Ejemplo basico de condicionales con entrada por teclado

edad = int(input("Ingresa tu edad: "))

if edad < 0:
    print("La edad no puede ser negativa.")
elif edad < 18:
    print("Eres menor de edad.")
else:
    print("Eres mayor de edad.")
