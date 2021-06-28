"""Hacer un programa que permita decidir si dos palabras son iguales o diferentes. Mostrar mensaje por
pantalla."""

parar = False
while not parar:
        pal1 = input("Ingrese una palabra:\n")
        pal2 = input("Ingrese una segunda palabra:\n")
        if pal1.lower() == pal2.lower():
            print("Las palabras son iguales")
        else:
            print("Las palabras son distintas")
        parar=input("Para salir escriba 'q' sino cualquier otra tecla\n")
        if parar.lower() == "q":
            parar = True
        else:
            parar = False