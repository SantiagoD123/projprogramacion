import matplotlib.pyplot as plt
lissnack = []
lisprecio= []
for i in range(5):
    ingsnack = input("ingrese sus snack favoritos: ")
    ingprecio = float(input("ingrese el precio de esos snack: "))
    lissnack.append(ingsnack)
    lisprecio.append(ingprecio)
    print(ingsnack)
    print(ingprecio)
    print(lissnack)
    print(lisprecio)

plt.bar(lissnack, lisprecio, width= 0.6, color = 'b')
plt.title("Snack favoritos")
plt.xlabel("Snack")
plt.ylabel("Precio")
plt.savefig("Grafico de snack favoritos.png")
plt.show()


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


import pandas as pd
import matplotlib.pyplot as plt
print('''El ecg = Un electrocardiograma registra las señales eléctricas del corazón. 
Es una prueba común e indolora que se utiliza para detectar rápidamente los problemas cardíacos y 
controlar la salud del corazón.''')
ecg1Data = pd.read_csv('ecg1.csv',encoding='UTF-8',header=0,delimiter=';').to_dict()
muestras = list(ecg1Data['muestra'].values())
voltaje = list(ecg1Data['valor'].values())
plt.plot(muestras, voltaje)
plt.title("Electrocardiograma")
plt.xlabel("Tiempo (ms)")
plt.ylabel("Voltaje (mV)")
plt.savefig("Grafico de electrocardiograma1.png")
plt.show()

print ('''El ppg = La fotopletismografía o fotopletismograma es una técnica de pletismografía en la cual 
se utiliza un haz de luz para determinar el volumen de un órgano. ''')
ppg1Data = pd.read_csv('ppg1.csv',encoding='UTF-8',header=0,delimiter=';').to_dict()
muestras = list(ppg1Data['muestra'].values())
valores = list(ppg1Data['valor'].values())
plt.plot(muestras, valores)
plt.title("Fotopletismografia")
plt.xlabel('Tiempo(ms)')
plt.ylabel('Voltaje(mV)')
plt.savefig("Grafico de fotopletismografia1.png")
plt.show()