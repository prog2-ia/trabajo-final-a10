class Valoracion(Genero):
    def __init__(self,nombre):
        super().__init__(nombre)
        self.valoraciones={}

    def valorar(self,libro,puntuacion):
        if libro not in self.libros:
            print("El libro no está en este género")
            return
        if puntuacion<0 or puntuacion>10:
            print("La puntuación debe ser entre 0 y 10")
            return
        self.valoraciones[libro]=puntuacion

    def mostrar_valoraciones(self):
        for libro in self.valoraciones:
            print(libro,":",self.valoraciones[libro])