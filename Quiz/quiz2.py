#---Mensajes---#
Mensaje_Bien = ('Buenas tardes, por favor ingrese la opción necesitada')
Mensaje_despe = ('Hasta luego, tenga un buen día')
preNumero = '''Ingrese una opción:
    1.Convertir la temperatura
    2.Estado del paciente segun su temperatura
    3.Mostrar la temperatura más alta, más baja y cada cuanto se tomo la muestra
    4.Salir
'''
#--Mensaje conversor--#
Mensaje_ingrese = '''F- Mostrar en Fahrenheit
K- Mostrar en Kelvin
C- Mostrar en Celsius
'''

#---codigo---#
#lista tempperatura corporal
Temperatura_Corporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]
#--For Kelvin--#
listaKelvin = []
for i in Temperatura_Corporal:
    Kelvin = i+273.15
    listaKelvin.append(Kelvin)
#--For fahrenheit--#
listaFar = []
for i in Temperatura_Corporal:
    Fahrenheit = (i*1.8)+32
    listaFar.append(Fahrenheit)

#--punto 2--#
listaCla = []
tipoCla = ''
for i in Temperatura_Corporal:
    if (i < 36):
        tipoCla = 'Hipotermia'
    elif (i >= 36 and i < 37.6):
        tipoCla = 'Estado normal'
    else:
        tipoCla = 'Fiebre'
    listaCla.append(tipoCla)

#--menu--#
print(Mensaje_Bien)
opcionescogida = int(input(preNumero))
while (opcionescogida != 4):
#--opcion 1--#
    if (opcionescogida == 1):
        Opciongrados = input(Mensaje_ingrese)
        if (Opciongrados == 'K'):
            print("Temperatura en Kelvin")
            print(listaKelvin)
        elif (Opciongrados == 'F'):
            print("Temperatura en Fahrenheit")
            print (listaFar)
        elif (Opciongrados == 'C'):
            print("Temperatura en Celsius")
            print(Temperatura_Corporal)
            print("No es necesario hacer una conversion")
        else :
            print("opcion no valida, recuerde utilizar opciones validas")
#--opcion 2--#
    elif (opcionescogida == 2):
        print(Temperatura_Corporal, listaCla)

#--opcion 3--#
    elif(opcionescogida == 3):
        print('La temperatura mas alta es: ', max(Temperatura_Corporal))
        print('La temperatura mas baja es: ', min(Temperatura_Corporal))
        print('Un dato se tomaba cada: ', 24/len(Temperatura_Corporal))
#--Mensaje invalido--#
    else:
        print("Entrada no valida, recuerde utilizar las opciones mostradas en pantalla")
    opcionescogida = int(input(preNumero))


print(Mensaje_despe)