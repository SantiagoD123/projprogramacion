import pandas as pd
import matplotlib.pyplot as plt
ppgData = pd.read_csv('ppg.csv',encoding='UTF-8',header=0,delimiter=';').to_dict()
print(ppgData.keys())
muestras = list(ppgData['muestra'].values())
print(muestras)
valores = list(ppgData['valor'].values())
plt.plot(muestras, valores)
plt.title("Fotopletismografia")
plt.xlabel('Tiempo(ms)')
plt.ylabel('Voltaje(mV)')
plt.show()