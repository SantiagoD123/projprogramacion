#booleans son verdadero y falso
Pruebav = True
Pruebaf = False
print (Pruebav)
print (Pruebaf)
Pruebav = Pruebaf
print (Pruebav)
#Se colocaron diferentes variables para empezar el boolean
edad = 18
estatura = 1.86
peso = 62
nombre = "Santiago Díaz"
# utiliza los numerales para generar un marco en el print
# Comprueba mediante Boolean si ciertas razones son ciertas
print ("#"*15, "mayor edad", "#"*15)
ismayoredad = edad >= 18
print (ismayoredad)
#Aqui se puede ver una de estas "razones" si la estatura esta bajo el promedio
print ("#"*15, "bajo la estatura promedio", "#"*15)
ismayorestura = estatura < 1.70
print (ismayorestura)
#diferente de se escribe !=, como se comprueba aca, se utilizan dos int el del "peso" y otro al azar.
print ("#"*15, "Son diferentes pesos", "#"*15)
ispesodiferente = peso != 65 
print (ispesodiferente)