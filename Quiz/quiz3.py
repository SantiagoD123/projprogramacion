class Pagina():
    def __init__(self, tipodecontenidoh, formatoh, fechah):
        self.tipo = tipodecontenidoh
        self.formato = formatoh
        self.fecha = fechah

    def mostrarAtr(self):
        print(f'''En mi página hay contenido sobre {self.tipo}, en un formato {self.formato}
        y se público en el {self.fecha}''')

class Favoritos(Pagina):
    def __init__(self,tipodecontenidoh, formatoh, fechah,favcomui,fechaActualizacion):
        Pagina.__init__(self,tipodecontenidoh, formatoh, fechah)
        self.favoritocomunidad = favcomui
        self.fechaActualizacion = fechaActualizacion

    def agrgarSong (self, cancion, actualizacion):
        self.favoritocomunidad.append(cancion)
        self.fechaActualizacion = actualizacion

    def mostrarLista (self, cancionEliminida):
        print(self.favoritocomunidad)
        

lista = ["Hola", "pepito", "Camil"]
camil = Favoritos("camil", "mp3", 2020, "sorry", 2021) 
camil.mostrarLista(3)
print("========================================================================")
camil.agrgarSong("Canción agregada",2021)
print(camil.favoritocomunidad)







# pag = Pagina("Música", "PHP", 2012)

# pag.mostrarAtr()