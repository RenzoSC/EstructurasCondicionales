"""Realice un programa que pida un número del 1 al 12 y diga el nombre del mes correspondiente"""
mes = ["Enero" , "Febrero" , "Marzo", "Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Nombiembre","Diciembre"]
num = int(input("Ingrese un número del 1 al 12\n"))
if num >= 1 and num <= 12:
    print("El día de la semana que corresponde al número es " + mes[num-1])
else:
    print("Ingrese un valor válido")