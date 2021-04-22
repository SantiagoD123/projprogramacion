class Torta():

    def __init__(self, formah, saborh, alturah):
        self.forma = formah
        self.sabor = saborh
        self.altura = alturah

    def mostrarAtr(self):
        print(f'''La torta tiene una forma {self.forma}, un sabor {self.sabor} 
        y una altura de {self.altura}''')


Tor = Torta("Redonda", "Chocolate", "2 metros")
Tor.mostrarAtr()

class Estudiante():
    def __init__(self, edadh, nombreh, idh, carrerah, semestreh):
        self.edad = edadh
        self.nombre = nombreh
        self.id = idh
        self.carrera = carrerah
        self.semestre = semestreh

    def mater(self, materia, tiempo):
        print(f'''Soy {self.nombre}, estoy estudiando la materia {materia} en un tiempo de {tiempo}''')
est = Estudiante(15, "Joselito", "4567892234", "Ingenieria Biomedica", "Tres")
est.mater("programación", "6 meses")

class Nutricionista():
    def __init__(self, edadh, idh, nombreh, uni):
        self.edad = edadh
        self.id = idh
        self.nombre = nombreh
        self.universidad = uni

    def imc(self):
        Peso = float(input("por favor diganos su peso en Kg: "))
        Estatura = float(input("por favor diganos su estatura en m: "))
        IMC = Peso/(Estatura**2)
        print("El Imc del paciente es de:", IMC)

nut = Nutricionista(15, 42135476432, "Pedro", "Universidad Ces")
nut.imc()

class Canguro():
    def __init__(self, edadh, idh, nombreh):
        self.edad = edadh
        self.id = idh
        self.nombre = nombreh

    def saltos(self, salto):
        for i in range (salto):
            print(f'El canguro {self.nombre} ha saltado {i+1} veces')

cag = Canguro(4, 4325, "Fabio")
cag.saltos(5)

class Guitarra():
    def __init__(self, tipoh, Numcuerdash):
        self.tipo = tipoh
        self.cuerdas = Numcuerdash
    
    def song(self, cancion, grupomusical):
        print(f'''La guitarra esta interpretando la cancion {cancion} hecha por el grupo {grupomusical}''')

gui = Guitarra("Guitarra acustica", "Tiene 6 cuerdas")
gui.song("Radioactive", "Imagine Dragons")