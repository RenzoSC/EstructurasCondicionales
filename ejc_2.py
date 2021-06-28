"""Leer 10 números y obtener la cantidad de mayores y la cantidad de menores a 100, cuál es el número
máximo y cuál es el número mínimo."""
numeros = []
i = 1
while i <=10:
    num = int(input("Ingrese un número:\n"))
    numeros.append(num)
    i +=1
menores = []
for i in range(len(numeros)):
    if numeros[i] < 100:
        menores.append(numeros[i])

mayores = []
for i in range(len(numeros)):
    if numeros[i] >= 100:
        mayores.append(numeros[i])
print("Los números menores que 100 son:")
for i in range(len(menores)):
    print(menores[i])

print("Los números mayores que 100 son:")
for i in range(len(mayores)):
    print(mayores[i])

print("El número más grande es: " + str(max(mayores)))
print("El número más chico es: " + str(min(menores)))