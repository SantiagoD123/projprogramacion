#-------------#

Mensaje_Bienvenida = "Bienvenido al codigo"
Mensaje_Mayor_Edad = "Eres mayor de edad puedes seguir"
Mensaje_Menor_Edad = "Eres menor de edad no puedes seguir"
Pregunta_edad = "¿Cual es tu edad?: "

#------------------#

print(Mensaje_Bienvenida)
edad = int(input(Pregunta_edad))
Ismayor = edad >=18
if (Ismayor):
    print(Mensaje_Mayor_Edad)
else:
    print(Mensaje_Menor_Edad)