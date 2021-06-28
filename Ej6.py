"""Realice un programa donde el usuario ingrese su edad. Si es mayor de 16 años, muestre un mensaje
diciendo “puede votar”, sino “no vota”."""

"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no."""
while True:
    try:
        edad= int(input("Introduzca su edad\n"))
        if edad >= 18:
            print("Podes votar")
        elif edad < 0:
            print("THATS IMPOSSIBLE")
            raise (ValueError)
        else:
            print("Aun no podes votar")
        break
    except ValueError:
        print("Ingrese un valor válido por favor...")