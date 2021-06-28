""" Leer 10 números y mostrar solamente los números positivos, y su sumatoria. """
x = 1
sumatoria = 0
while  x <= 10:
    num = int(input("Ingrese un número:\n"))
    if num >=0:
        sumatoria += num
    else:
        pass
    x += 1
print(sumatoria)