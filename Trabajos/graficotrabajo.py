import matplotlib.pyplot as plt
Atletas = ["Michael Phelps", "Larisa Latynina", "Paavo Nurmi", "Mark Spitz", "Carl Lewis"]
oro = [23, 9, 9, 9, 9]
plt.bar(Atletas, oro, width = 0.3, color = 'b')

plt.title("Atletas con más medallas de oro")

plt.xlabel("ATLETAS")
plt.ylabel("NUMERO DE MEDALLAS")
plt.savefig("Atletasgrafico.png")

plt.show()