"""Realice un programa que lea tres números, muestre cuál es el mayor y determinar si es par o impar"""
def espar(num):
    if num %2 ==0:
        print("Es par")
    else:
        print("Es impar")

num1 = int(input("Ingrese un número:\n"))
num2 = int(input("Ingrese otro número:\n"))
num3 = int(input("Ingrese el último número:\n"))

if num1 > num2 and num1 > num3:
    print("El número más grande es " + str(num1))
    espar(num1)
elif num2 > num1 and num2 > num3:
    print("El número más grande es " + str(num2))
    espar(num2)
else:
    print("El número más grande es " + str(num3))
    espar(num3)