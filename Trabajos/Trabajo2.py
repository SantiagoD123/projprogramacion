#Tarea, pedir dos numeros al usuario y colocar si el numero a es mayor que b
#mostrar en pantalla suma, multiplicacion, division y exponente

#-------Entrada-------#
Mensaje_bienvenida = "Hola, Regalame dos numeros enteros"
Mensaje_n1 = "Tu primer numero es: " 
Mensaje_n2 = "Tu segundo numero es: "         
Mensaje_despedida = "Muchas gracias por su participación, vuelva pronto"
#---------codigo-------#

print (Mensaje_bienvenida)
N1 = int(input(Mensaje_n1))
N2 = int(input(Mensaje_n2))


print ("#"*15, "Numero 1 es mayor", "#"*15)
isbmayor = N1 > N2
print (isbmayor)
print ("#"*15, "Numero N2 es mayor", "#"*15)
isamayor = N1 < N2
print (isamayor)
print ("#"*15, "Ambos numeros son iguales", "#"*15)
isbmayor = N1 == N2
print (isbmayor)
print ("#"*15, "Son numeros diferentes", "#"*15)
isbmayor = N1 != N2
print (isbmayor)


sumar = N1 + N2
print ("el resultado de la suma es:", sumar)

restar = N1 - N2
print (f"la resta dio {restar} exitosamente")

multiplicar = N1 * N2
print ("el resultado de la multiplicacion es:", multiplicar)


dividir = N1 / N2
print (f"la division del numero 1 dio {dividir} exitosamente")

exponente = N1**N2
print ("el resultado del exponenciación del numero 1 es:", exponente)

exponente = N2**N1
print ("el resultado del exponenciación del numero 2 es:", exponente)

dividir = N2 / N1
print (f"la division del numero 2 dio {dividir} exitosamente")

print(Mensaje_despedida)