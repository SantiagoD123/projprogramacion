import matplotlib.pyplot as plt
mes = ["Enero", "Febrero", "Marzo", "Abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
paga = [915000, 968000, 1000000, 885000, 918756, 915846, 987455, 1100000, 879990, 915000, 1005400, 1205400]
plt.bar(mes, paga, width = 0.3, color = 'r')

plt.xlabel("Mes del año 2020")
plt.ylabel("ingresos")
plt.savefig("GraficoIngreso.png")


plt.show()