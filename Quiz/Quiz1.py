#--Entrada--#

Mensaje_bienvenida = ("Buenas tardes, vamos a verificar el estado del paciente")
Trigliciredios = ("Ingrese el nivel de trigliceridos: ")
Homocisteina = ("Ingrese el nivel de homocisteina: ")
Mensaje_despedida = ("Tenga un buen día")

#--codigo--#

print(Mensaje_bienvenida)

tri = int(input(Trigliciredios))


if (tri<150):
    print("El paciente esta en estado optimo de trigliceridos")
elif (tri>=150 and tri<=199):
    print("El paciente sobrepasa el limite optimo de trigliceridos, por favor tenga cuidado")
elif (tri>=200 and tri<=499):
    print("El paciente esta en un nivel alto del optimo de trigliceridos, por favor tenga cuidado")
else:
    print("El paciente esta a un nivel muy alto del optimo de trigliceridos, por favor tengan cuidado")

hom = int(input(Homocisteina))

if(hom<2):
    print("Valores no predeterminados, por favor ingresar bien los valores de homocisteina. Gracias")
elif (hom>=2 and hom<15):
    print("El paciente esta en estado optimo de homocisteina")
elif (hom>=15 and hom<30):
    print("El paciente sobrepasa el limite optimo de homocisteina, por favor tenga cuidado")
elif (hom>=30 and hom<=100):
    print("El paciente esta en un nivel alto del optimo de homocisteina, por favor tenga cuidado")
else:
    print("El paciente esta a un nivel muy alto del optimo de homocisteina, por favor tengan cuidado")

print(Mensaje_despedida)