import matplotlib.pyplot as plt
lisciudad = []
lispoblacion= []
for i in range(5):
    ingciudad = input("ingrese su ciudad favorita: ")
    ingpoblacion = float(input("ingrese la poblacion de cada ciudad: "))
    lisciudad.append(ingciudad)
    lispoblacion.append(ingpoblacion)
    print(ingciudad)
    print(ingpoblacion)
    print(lisciudad)
    print(lispoblacion)
maximo = lispoblacion.index(max(lispoblacion))
pieExplode = [0, 0, 0, 0, 0]
pieExplode [maximo] = 0.2
pieLabels = lisciudad
sizes = lispoblacion
plt.pie(sizes, labels = pieLabels, explode=pieExplode)
plt.title("Ciudades favoritas")
plt.savefig("Grafico de ciudades favoritas.png")
plt.show()
