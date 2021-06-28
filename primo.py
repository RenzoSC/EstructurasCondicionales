def esprimo (num):
    contador = 0
    for i in range(1, num+1):
        if num % i == 0:
            contador +=1
        else:
            continue
    if contador == 2:
        return True
    else:
        return False

numero = int(input("Ingrese un número:\n"))

if esprimo(numero):
    print("Es primo")
else:
    print("No es primo")