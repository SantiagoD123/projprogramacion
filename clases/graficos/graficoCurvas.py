import matplotlib.pyplot as plt

tiempo = [0,1,2,3,4,5]
sensor = [4,5,6,8,9,10]
plt.plot(tiempo,sensor,'--,c')
############
plt.title('Gráfico Sensor contra el tiempo')
plt.xlabel('Tiempo(s)')
plt.ylabel('Voltaje(mV)')
plt.savefig('sensor')
############
plt.show()

diccionario = {}
diccionario['NombresEstudiantes'] = ['Jacobo','Dani','Maria','Elena']
diccionario['EdadEstudiantes'] = [18,17,24,32]
diccionario['Peso'] = [84,56,64,57]
print(diccionario)

print(diccionario['NombresEstudiantes'][-1],diccionario['EdadEstudiantes'][-1],diccionario['Peso'][-1])

import pandas as pd
import matplotlib.pyplot as plt
ecgData = pd.read_csv('ecg.csv',encoding='UTF-8',header=0,delimiter=';').to_dict()
print(ecgData.keys())
muestras = list(ecgData['muestra'].values())
print(muestras)
voltaje = list(ecgData['valor'].values())
print(voltaje[-10:])
plt.plot(muestras, voltaje)
plt.show()