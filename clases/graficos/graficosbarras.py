import matplotlib.pyplot as plt
lenguajes = ["java", "py", "dart", "ts", "elixir"]
encuesta = [30, 10, 20, 20, 20]
plt.bar(lenguajes, encuesta, width= 0.6, color = 'y')
#####Titulo####
plt.title("Lenguajes usados")
###Eje###
plt.xlabel("Lenguaje de programación")
plt.ylabel(" % de uso de lenguaje de programación")
plt.savefig("Grafico de lenguaje.png")
##########
plt.show()