"""Realice un programa que lea 4 números y diga cuantos son pares y cuantos impares y devuelva la
sumatoria de los pares."""
sum = 0

def espar(num):
    if num %2 ==0:
        return True
    else:
        return False

num1 = int(input("Dame un número:\n"))
num2 = int(input("Dame un número:\n"))
num3 = int(input("Dame un número:\n"))
num4 = int(input("Dame un número:\n"))

if espar(num1):
    sum += num1
if espar(num2):
    sum += num2
if espar(num3):
    sum += num3
if espar(num4):
    sum += num4

print("\n\nLa suma de todos los números pares es " + str(sum))
