class Persona():

    def __init__(self, idH, nombreH,edadH):
        self.edad = edadH
        self.nombre = nombreH
        self.id = idH

    def nombrepersona(self):
        print('Buenos días, mi nombre es', self.nombre)

    def edadpersona(self):
        print('Mi edad es', self.edad)
    
    def idpersona(self):
        print(f'Mi Id es {self.id}, mucho gusto ')
    
    def habla(self, mensaje):
        print(f'Yo {self.nombre} espero', mensaje)

    def caminar(self, distancia):
        for i in range (distancia):
            print(f'Yo {self.nombre} he caminado {i+1} pasos')



class Doctor(Persona):
    def __init__(self, idH, nombreH,edadH, profesionH, especializadoH):
        Persona.__init__(self, idH, nombreH,edadH)
        self.prof = profesionH
        self.especializado = especializadoH

class MedicoInterno(Doctor):
    def solucionProblem(self, problema):
        print(f'Hola soy un {self.prof}, especializado en {self.especializado} me llamo {self.nombre} y procedo a tratar su {problema}')

class Nutricionista(Persona):
    def __init__(self, idH, nombreH,edadH, profesionH, Uni):
        Persona.__init__(self, idH, nombreH,edadH)
        self.prof = profesionH
        self.universidad = Uni
    def Uni(self):
        print(f"Buenas tarde, yo soy {self.nombre} egresado de la universidad {self.universidad} y soy un {self.prof}")
        Peso = float(input("por favor diganos su peso en KG: "))
        Estatura = float(input("por favor diganos su estatura en m: "))
        IMC = Peso/(Estatura**2)
        print("Su Imc es de:", IMC)


class Abogado(Persona):
    def __init__(self, idH, nombreH,edadH, profesionH, especializaH, Uni):
        Persona.__init__(self, idH, nombreH,edadH)
        self.prof = profesionH
        self.universidad = Uni
        self.especializacion = especializaH
    def clien(self):
        print(f'''Buenas tarde, yo soy {self.nombre} egresada de la universidad {self.universidad} y 
        soy un {self.prof} especializado en {self.especializacion}''')
        nombC = input("Ingrese su nombre por favor: ")
        casoC = input("ingrese el caso el cual quiere ser representado: ")
        print(f"Yo {self.nombre} procedo a representar al cliente {nombC} en el caso {casoC}, Muchas gracias")


persona1=Persona(100200030, 'Manolo', 32)
persona1.nombrepersona()
persona1.edadpersona()
persona1.idpersona()
persona1.habla('le vaya bien en su trayecto, cuidese')
persona1.caminar(10)

doc = MedicoInterno(21427368, 'Raul', 38, 'Doctor', 'Medicina interna')
doc.solucionProblem('Dolor de cabeza')

nut = Nutricionista(1235662, "Pedro", 30, "Nutricionista", "CES")
nut.Uni()

abo = Abogado(23567543, "Teresa", 52, "Abogado", "area penal", "CES")
abo.clien()
