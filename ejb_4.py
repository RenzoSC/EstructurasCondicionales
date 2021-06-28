"""Confeccione un programa que pida un número del 1 al 7 y diga el día de la semana correspondiente."""

dias = ["Lunes" , "Martes" , "Miercoles", "Jueves", "Viernes", "Sabado" , "Domingo"]
num = int(input("Ingrese un número del 1 al 7\n"))
if num >= 1 and num <= 7:
    print("El día de la semana que corresponde al número es " + dias[num-1])
else:
    print("Ingrese un valor válido")