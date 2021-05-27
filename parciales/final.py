import matplotlib.pyplot as plt
lisalimentos = []
lisprecio= []
for i in range(8):
    ingalimentos = input("ingrese sus alimentos favoritos: ")
    ingprecio = float(input("ingrese el precio de esos alimentos: "))
    lisalimentos.append(ingalimentos)
    lisprecio.append(ingprecio)
    print(ingalimentos)
    print(ingprecio)
    print(lisalimentos)
    print(lisprecio)

plt.bar(lisalimentos, lisprecio, width= 0.6, color = 'g')
plt.title("Alimentos favoritos")
plt.xlabel("Alimentos")
plt.ylabel("Precio")
plt.savefig("Grafico de barras de alimentos favoritos.png")
plt.show()

# ---punto 2---#

class Humano():
    def __init__(self, nombreh, sexoh, edadh):
        self.nombre = nombreh
        self.sexo = sexoh
        self.edad = edadh

    def hablar(self, mensaje):
        print(f'Buenos días, mi nombre es {self.nombre} y quiero decir que', mensaje)

class Doctor(Humano):
    def Imc(self):
        print(f"Buenas tarde calculare su IMC")
        Peso = float(input("por favor diganos su peso en KG: "))
        Estatura = float(input("por favor diganos su estatura en m: "))
        IMC = Peso/(Estatura**2)
        print("Su Imc es de:", IMC)


hum = Humano("Santiago", "Masculino", 23)
hum.hablar('espero pases un excelente día')
doc = Doctor("Laura", "Femenino", 32)
doc.Imc()

# --punto 3--#

isCorrectData = False
while (isCorrectData == False):
    try:
        dolar = float(input("ingrese la cantidad de dinero en dolares: "))
        isCorrectData = True
    except ValueError:
        print('dato incorrecto, por favor ingrese nuevamente')


isCorrectData = False
while (isCorrectData == False):
    try:
        name = input("Ingrese su nombre por favor: ")
        assert(name.isalpha())
        isCorrectData = True
    except AssertionError:
        print('datos incorrectos ingrese nuevamente')


euros = dolar*0.82

print(f"{name} tiene {dolar} en dolares y {euros} en euros")


# --punto 4--#

import sys

nomArchivo = "pacientes.txt"
try:
    archivo = open(nomArchivo)
    print('Funciono')
except FileNotFoundError:
    archivo = open(nomArchivo, 'w', encoding='UTF-8')
    print("No se encontro el archivo entonces se guardo")
    sys.exit(1)

archivo = open(nomArchivo,'a')
nombre  = input('ingrese el nombre del paciente: ')
descripcion = input('ingrese una descripcion de la enfermedad: ')
precio = float (input('ingrese el precio de la consulta: '))
linea = "\nNombre:" + (nombre) + " \nDescripcion: "+ (descripcion) + " \nPrecio: "+ str(precio)
archivo.writelines(linea)
archivo.close()
