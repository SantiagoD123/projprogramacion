class Animal():
    def __init__(self, tipoAnimal, pesoAnimal ,peso2Animal, promvivir):
        self.peso = pesoAnimal
        self.raza = 'tigre albino'
        self.tipo = tipoAnimal
        self.vivir = promvivir
        self.peso2 = peso2Animal
    
    def tanimal(self):
        print('Hola el animal es', self.raza, 'y es un', self.tipo)

    def vive(self):
        print('El', self.raza, 'puede llegar a vivir hasta', self.vivir)

    def pesAnimal(self):
        escogido = input('''Por favor elige la opcion del genero sobre el cual deseas la informacion:
        M---> Macho
        H---> Hembra: 
        ''')
        if (escogido == 'M'):
            print("El", self.raza, " macho puede llegar a vivir entre 10-12 años")
            print("El peso del", self.raza, "puede ser maximo",self.peso)
        elif (escogido == "H"):
            print("El", self.raza, " hembra puede llegar a vivir hasta 16 años")
            print("El peso del", self.raza, "puede ser maximo ",self.peso2)
        else:
            ("No valido")
        return escogido


animal = Animal("Felino", 226, 181, 16)

animal.tanimal()
animal.vive()
animal.pesAnimal()
print(animal)

