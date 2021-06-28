"""Realice un programa que lea dos números y diga cuál es el mayor"""
num1 = int(input("Ingrese un número:\n"))
num2 = int(input("Ingrese otro número:\n"))
if num1 > num2:
    print(str(num1) + " Es el mayor")
elif num1 == num2:
    print("Los numeros son iguales")
else:
    print(str(num2) + " Es el mayor")