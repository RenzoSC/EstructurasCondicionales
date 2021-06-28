"""Introducir los lados de un triángulo y visualizar por pantalla si dicho triángulo es equilátero, isósceles o
escaleno"""

lad1 = int(input("Ingrese el primer lado\n"))
lad2 = int(input("Ingrese el segundo lado\n"))
lad3 = int(input("Ingrese el tercer lado\n"))

if lad1 == lad2 and  lad1 == lad3:
    print("Es un triangulo Equilátero")
elif (lad1 == lad2 or lad1 == lad3) and (lad1 != lad3 or lad1 != lad2):
    print("Es un triangulo Isosceles")
else:
    print("Es un tiangulo Escaleno")