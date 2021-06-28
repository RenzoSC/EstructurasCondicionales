"""Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo el cambio de dólares a pesos y
que sea el usuario quién decida qué tipo de cambio quiere, si de dólares a pesos o viceversa."""
#Valores de conversión 1 dólar = 95.35 pesos
parar = False
while not parar:
    decision = input("¿Quiere convertir dolares o pesos?(d/p)")
    if decision.lower() == "d":
        dolar = float(input("Ingrese su cantidad de dólares (solo números)\n"))
        pesos = 95.35 * dolar
        print("La cantidad de pesos en total es: " + str(round(pesos, 2)))
    elif decision.lower() == "p":
        pesos = float(input("Ingrese su cantidad de pesos (solo números)\n"))
        dolares = pesos / 95.35
        print("La cantidad de dólares en total es " + str(round(dolares, 2)))

    seguir = input("Para salir ingrese 'q'\nEn caso contrario aprete cualquier boton\n")
    if seguir == "q":
        parar = True
    else:
        parar = False
