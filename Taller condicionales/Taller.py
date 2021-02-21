#----1.Dados dos numeros determine si son iguales o cual es mayor---#
#---entrada---#

Numero1 = "Primer numero: "
Numero2 = "Segundo numero: "
mayor1 = "El primer numero es mayor que el segundo numero"
mayor2 = "El segundo numero es mayor que el primer numero"
igual = "Los numeros son iguales"

#---codgio---#

N1 = int(input(Numero1))
N2 = int(input(Numero2))

if (N1>N2):
    print(mayor1)
elif (N2>N1):
    print(mayor2)
else:
    print(igual)







# 2. Pida la edad del usuario y muestre en pantalla la siguiente información:
#• Si tiene menos de 18 años diga que es menor de edad
#• Desde 18 hasta 25 Es Joven
#• Desde 26 hasta 60 Adulto
#• Mayor a 60 años es Adulto mayor

#---Entrada---#

edad = "Por favor regalanos la edad: "
edadmenor = "Es menor de edad"
edadjoven = "Es una persona joven"
edadadulto = "Es una persona adulta"
edadmayor = "Es un adulto mayor"

#---codigo---#

ed = int(input(edad))

if (ed<18):
    print(edadmenor)
elif (ed>=18 and ed<=25):
    print(edadjoven)
elif (ed>=26 and ed<=60):
    print(edadadulto)
else:
    print(edadmayor)






# 3.Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos
#   años han pasado desde ese año o cuántos años faltan para llegar a ese año.

#---entrada---#
Año_actual = "¿Cual es el año actual?: "
Año_cualquiera = "Ingrese año cualquiera: "

#--codigo--#

año1 = int(input(Año_actual))
año2 = int(input(Año_cualquiera))

if (año1>año2):
    resta = año1-año2
    print (f"han pasado {resta} años")
elif (año2>año1):
    resta2 = año2-año1
    print(f"Faltan {resta2} para llegar a este año")
else:
    print ("son el mismo año")







# 4. Escriba un programa que pida una distancia en centímetros y que escriba esa distancia en
#  kilómetros, metros y milimetros (escribiendo todas las unidades).

#---Entrada---#

distancia = ("Ingrese una distancia en centimetros: ")
unidad = ('''¿En que unidad las desea? : 
k-kilometros 
m-metros 
mm- milimetros: ''')
Mensaje_error = ("Unidades no validas")
#--codigo--#

dis = float(input(distancia))
uni = input(unidad)

K = dis/100000
M = dis/100
MM = dis*10

if (uni== 'k'):
    print("la distancia en kilometros es:", K)
elif (uni=='m'):
    print("La distancia en metros es:", M)
elif (uni=='mm'):
    print("la distancia en milimetros es:", MM)
else:
    print(Mensaje_error)
