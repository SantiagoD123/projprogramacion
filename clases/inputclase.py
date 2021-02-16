#input es pr hacerle preguntas al usurario

#-----constnte----#
PREGUNT_NOMBRE = "¿Como te llamas? : "
MENSJE_SALUDO = "Un gusto conocerte"
Pregunt_edad = "Cuantos años tienes? : "
pregunta_estatura = "¿Cuanto mides? : "

#----------Entrd codigo---------#
nombre = input(PREGUNT_NOMBRE)
edad = int(input(Pregunt_edad))
estatura = float(input(pregunta_estatura))
print(MENSJE_SALUDO, nombre)
print(edad+5)
print(estatura)