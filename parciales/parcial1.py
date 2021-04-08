#Crear una función que dado tres números
# muestre en pantalla la suma, la resta, la multiplicación, la
# división y la potencia entre ellos

def trenum (n1, n2, n3):
    print("La multiplicacion es: ", n1*n2*n3)
    print("La division es:", n1/n2/n3)
    print("La suma es:", n1+n2+n3)
    print("la resta es:", n1-n2-n3)
    print("la potencia es:",n1**n2**n3 )
n1 = int(input ("Ingrese el primer numero: "))
n2 = int(input ("Ingrese el segundo numero: "))
n3 = int(input ("Ingrese el tercer numero: "))
trenum(n1, n2, n3)

# Crear una función que dada tres listas del mismo
# tamaño las muestre en pantalla

def tlistas(lista1, lista2, lista3):
    if (len(lista1) == len(lista2) == len(lista3)):
        print(lista1, lista2, lista3)
    else:
        print("listas no tienen el mismo tamaño")
lis1 = [5, 10, 40, 20, 20, 30]
lis2 = [32, 20, 10, 9, 15, 29]
lis3 = [86, 289, 28, 37, 48 ,60]
tlistas(lis1, lis2, lis3)

# Valor 1.0 Crear una función que calcule y devuelva el área
# de un triangulo recuerde que la formula del mismo es
# (base*altura) /2. Pida las entradas que considere
# necesarias

def caltri (base, alt):
    area = (base*alt)/2
    print (area)
base = float(input("Por favor escriba la base: "))
alt = float(input("Escriba la altura: "))
area = caltri(base, alt)


# Valor 0.5 Crear una función que dada una lista de
# números enteros muestre el promedio, el máximo, el
# mínimo.

def numente(lista):
    maximo = max(lista)
    minimo = min(lista)
    sumanum = 0
    sumanum= sum(lista)
    totalnum = len(lista)
    promedio = sumanum/totalnum
    print('El mayor es:', maximo, 'Menor es:', minimo, 'promedio es:', promedio)
enteros = [50, 100, 28, 26, 68, 51, 5, 10, 3]
numente(enteros)

# Punto duro (Valor1.0) se sabe que la sucesión de
# Fibonacci sigue el siguiente patrón
# 0,1,1,2,3,5,8,13,21,34,55,89,144, …. Se le pide como
# ingeniero biomédico, que dado un número n de la
# sucesión muestre en pantalla su valor. Por ejemplo, si el
# usuario digita 3 se mostrará 1 y si el usuario digita 5
# mostrará 3 si ingresa 100 debe mostrar el número que le
# corresponda en la sucesión.

def patron (numpedido):
    num1 = 0
    num2 = 1
    for i in range (numpedido-1):
        a = num1 + num2
        num1, num2 = num2, a
    print(a)
n = int(input("Ingrese el numero del valor que desea ver: "))
numero = patron (n)
print (numero)