#----constante----
Pregunta_peso = "¿Cuanto pesas en kg? : "
Pregunta_estatura = "¿Cuanto mides en m? : "
Mensaje_bienvenida = "Hola, voy a calcular su IMC"
Mensaje_despedida = "Tu IMC es :"

#--Entrada codgio--#

print(Mensaje_bienvenida)
peso = float(input(Pregunta_peso))
Estatura = float(input(Pregunta_estatura))
IMC = peso/(Estatura**2)
print (peso)
print(Estatura)
print(Mensaje_despedida, IMC)
Isobeso = IMC >= 30
print("El resultado de la prueba es: ", Isobeso)

#Tarea, pedir dos numeros al usuario y colocar si el numero a es mayor que b
#mostrar en pantalla suma, multiplicacion, division y exponente
