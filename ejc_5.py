"""  Leer 15 números negativos y convertirlos a positivos e imprimir dichos números. """
import time
x = 1
while  x <= 15:
    num = int(input("Ingrese un número negativo:\n"))
    if num <0:
        num = -num
        time.sleep(1.2)
        print(num)
        x += 1
    else:
        print("No ingresaste un número negativo....\n\n\n")