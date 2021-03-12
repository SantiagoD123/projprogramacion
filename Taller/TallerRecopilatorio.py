#--Mensajes--#
#--Mensaje menu--#
preNumero = '''Ingrese una opción:
    1.Hacer conversión de dolares a pesos o Euros
    2.Lista de clasificación de ingresos
    3.Mostrar el ingreso más alto, más bajo y promedio
    4.Salir
'''
#--Mensaje primer punto--#
Mensaje_ingrese = '''C- Mostrar en pesos Colombianos
D- Mostrar en dolares
E- Mostrar en euros
'''



#--mensajes de despedida--#
Mensajedespedida = "Hasta luego, tenga un buen día"

#---Codigo---#
listaDolares = [20000,30000,4000,2500,1000,7600]
#--For pesos--#
listaPesos = []
for i in listaDolares:
    Pesos = i*3700
    listaPesos.append(Pesos)
#--For euros--#
listaEuros = []
for i in listaDolares:
    Euros = i*0.84
    listaEuros.append(Euros)
#--Ingresos mensuales--#
listaClasificacion = []
tipoClasificacion = ''
for i in listaDolares:
    if (i < 1000):
        tipoClasificación = 'Ingresos bajos'
    elif (i >= 1000 and i < 7000):
        tipoClasificación = 'Ingresos medios'
    elif (i >= 7000 and i < 20000):
        tipoClasificación = 'ingresos altos'
    else:
        tipoClasificación = 'Ingresos elevados'
    listaClasificacion.append(tipoClasificación)

#--menu--#
Opescogida = int(input(preNumero))

while (Opescogida !=4):
    if(Opescogida == 1):
        OpcionMoneda = input(Mensaje_ingrese)
        if (OpcionMoneda == 'C'):
            print("Lista en COP")
            print(listaPesos)
        elif (OpcionMoneda == 'D'):
            print("No es necesario una conversion porque ya esta en dolares")
            print (listaDolares)
        elif (OpcionMoneda == 'E'):
            print("Lista en Euros")
            print(listaEuros)
        else :
            print("opcion no valida, recuerde utilizar opciones validas")

#--opcion 2--#
    elif(Opescogida == 2):
        print(listaDolares, listaClasificacion)


#--Opcion 3--#
    elif(Opescogida == 3):
        print('El ingreso mayor es: ', max(listaDolares))
        print('El ingreso menor es: ', min(listaDolares))
        print('El promedio de ingresos es: ', sum(listaDolares)/len(listaDolares))

#--Entrada no valida--#
    else:
        print("Entrada no valida, recuerde utilizar entradas correctas : 1 - 2 - 3 - 4")

    Opescogida = int(input(preNumero))

print(Mensajedespedida)
