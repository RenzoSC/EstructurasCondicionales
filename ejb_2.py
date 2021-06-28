""" Realice un programa que le permita al usuario simular el pago ingresando el importe y la forma de pago:
• Contado (1): se aplica un descuento del 10% al importe
• Tarjeta (2): se aplica un interés de 10%
• Débito (3): se aplica un descuento del 5%"""

pago = int(input("Ingrese su monto a pagar\n"))
formaDePago = int(input("""Tiene varias pormas de pago!
                • Contado (1): se aplica un descuento del 10% al importe
                • Tarjeta (2): se aplica un interés de 10%
                • Débito (3): se aplica un descuento del 5%\nSeleccione un número\n"""))

if formaDePago == 1:
    total = pago - (pago * 0.1)
    print("El importe es: " + str(pago) + "\nEl descuento es: 10%\n" +"El pago total es: " + str(total))
elif formaDePago ==2:
    total = pago + (pago * 0.1)
    print("El importe es: " + str(pago) + "\nEl interés es: 10%\n" +"El pago total es: " + str(total))
else:
    total = pago - (pago * 0.05)
    print("El importe es: " + str(pago) + "\nEl descuento es: 5%\n" +"El pago total es: " + str(total))