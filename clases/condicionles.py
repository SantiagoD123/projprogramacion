#--------constante------#
Mensaje_Bienvenida = "Hola, espero que estes bien"
Ingrese_numero_A = "Ingrese un numero A: "
Ingrese_numero_B = "Ingrese un numero B: "
Mensaje_Mayor = "El numero A es mayor que el numero B"
Mensaje_Menor = "El numero B es mayor que el numero A"
Mensaje_igual = "Son iguales"
#------Entrada codigo-----#
print(Mensaje_Bienvenida)

NA = int(input(Ingrese_numero_A))
NB = int(input(Ingrese_numero_B))
ismayor = NA>NB
ismenor = NA<NB
resultado = ""


if (ismayor):
    print(Mensaje_Mayor)
    resultado = Mensaje_Mayor
elif (ismenor):
    print(Mensaje_Menor)
    resultado = Mensaje_Menor
else:
    print(Mensaje_igual)
    resultado = Mensaje_igual

print(resultado)

