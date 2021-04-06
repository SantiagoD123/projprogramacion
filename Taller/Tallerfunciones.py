#Dada una lista muéstrela en pantalla elemento a elemento

def elemlista(lista):
    for i in lista:
        print(i)

numeros = [24, 40, 80, 10, 20, 35, 77, 80, 105]
elemlista(numeros)

#Dada una lista de números enteros muestre en pantalla el número más grande, el más pequeño y el promedio 
#de la lista

def proLista(lista):
    menor = min(lista)
    mayor = max(lista)
    prom = 0
    prom =sum(lista)
    div = len(lista)
    promedio = prom/div
    print('El mayor es:', mayor, 'Menor es:', menor, 'promedio es:', promedio)
numeros = [24, 40, 80, 10, 20, 35, 77, 80, 105]
proLista(numeros)

#Saludar n veces

def saludo(n = 0):
    print("Buenas tardes " * n)
n = int(input ("¿Cuantas veces quieres saludar?: "))
saludo(n)

#Que devuelva todos los números pares de una lista de números enteros

def numpar(lista):
    par = []
    for i in lista:
        if i % 2 == 0:
            par.append(i)
    return par
numeros = [24, 40, 80, 10, 20, 35, 77, 80, 105]
print (numpar(numeros))

#Que devuelva únicamente los elementos mayores a 24

def nummay(lista):
    may = []
    for i in lista:
        if i > 24:
            may.append(i)
    return may
numeros = [24, 40, 80, 10, 20, 35, 77, 80, 105]
print (nummay(numeros))

#Se sabe que el IMC se calcula dividiendo el peso por la 
#altura al cuadrado, realice una función que lo calcule.

def imc(peso, alt):
    IMC = peso/(alt**2)
    print (IMC)
peso = float(input("Por favor escriba su peso: "))
alt = float(input("Escriba su estatura: "))
IMC = imc(peso, alt)

#Crea un función que sirva para despedirte del que esta ejecutando el código

def desp():
    print(Mensaje_despedida)
Mensaje_despedida = "Hasta luego, que tenga un buen dia"
desp()