import matplotlib.pyplot as plt
pieLabels = ['bogota', 'Medellín', 'Calí', 'Barranquilla','Cartagena']
sizes = [10.4, 2.5, 2.4, 1.2, 1]
pieExplode = [0.1,0.0,0.0,0.0,0.0]


def etiquetarElementosPorcentuales(sizes, labels, indicador= ' ->'):
    acumulador = 0
    for elemento in sizes :
        acumulador += elemento

    for i in range (len(labels)):
        porcentaje = round(sizes[i]/acumulador*100)
        pieLabels[i] += indicador+str(porcentaje) + '%'

etiquetarElementosPorcentuales(sizes, pieLabels)
plt.pie(sizes, labels=pieLabels, explode=pieExplode)
plt.title('Ciudades mas grandes segun du poblacion')
plt.savefig('ciudades.png')
#####################
plt.show()