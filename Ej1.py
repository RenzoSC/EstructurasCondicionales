"""1. Realice un programa que solicite dos letras ingresadas por el usuario y verifique si son iguales o no,
mostrando un mensaje."""
parar = False
while not parar:
        pal1 = input("Ingrese una letra:\n")
        pal2 = input("Ingrese una segunda letra:\n")
        if pal1.lower() == pal2.lower():
            print("Las letras son iguales")
        else:
            print("Las letras son distintas")
        parar=input("Para salir escriba 'q' sino cualquier otra tecla\n")
        if parar.lower() == "q":
            parar = True
        else:
            parar = False
        