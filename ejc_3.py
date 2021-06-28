"""Ingresar las edades y el sexo de 15 personas y determinar cuántas son mujeres, cuántos varones,
cuántos mayores de edad y cuántos menores de edad"""
x=1
varones = 0
mujeres = 0
mayores = 0
menores = 0
while x <=15:
    genero = input("Ingresa tu sexo(M/F):\n")
    edad = int(input("Ingresa tu edad:\n"))
    if genero.lower() == "m":
        varones+=1
    else:
        mujeres+=1
    if edad <18:
        menores+=1
    else:
        mayores+=1
    x+=1