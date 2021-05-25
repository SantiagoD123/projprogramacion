# #----constante----
# Pregunta_peso = "¿Cuanto pesas en kg? : "
# Pregunta_estatura = "¿Cuanto mides en m? : "

# Mensaje_despedida = "Tu IMC es :"

# #--Entrada codgio--#

# isCorrectInfo = False
# while (isCorrectInfo == False):
#     try:
#         peso = float(input(Pregunta_peso))
#         Estatura = float(input(Pregunta_estatura))
#         IMC = peso/(Estatura**2)
#         isCorrectInfo = True
#     except ValueError:
#         print('ingresaste un dato no válido')

# print (peso)
# print (Estatura)
# print(Mensaje_despedida, IMC)

#-----Punto 2-----#

# parrafo = input("ingrese un parrafo por favor: ")

# print (parrafo)
# palabras = parrafo.split()
# print (len(palabras))

# indice = 0
# palabra = palabras [indice]
# longitud = len(palabra)
# for i in range (1, len[palabras]):
#     if len(palabras[i]) > longitud:
#         indice = 1
#         palabra = palabras[i]
#         longitud = len(palabra)
    
# print(palabra)
# print (indice)


#--------Tres------#

nombre  = input('ingrese  el nombre: ')
descripcion = input('ingrese una pequeña descripcion: ')
precio = float(input('ingrese el precio del mantenimiento: '))

nombreArchivo = "mantenimento.txt"
try:
    archivo = open(nombreArchivo)
    print('Funciono')
except FileNotFoundError:
    archivo = open(nombreArchivo, 'w', encoding='UTF-8')
    print("No funciono")

archivo = open(nombreArchivo,'a')
linea = "\nnombre:" + nombre + " \ndescripcion: "+ descripcion + " \nprecio: "+ str(precio)
archivo.writelines(linea)
archivo.close()
