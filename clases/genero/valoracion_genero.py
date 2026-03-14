from genero import Genero

class Valoracion(Genero):
    def __init__(self,nombre):
        super().__init__(nombre)
        self.__valoraciones={} # Atributo privado para evitar la manipulación

    def valorar(self,libro,puntuacion):
        if libro not in self.libros:
            print("El libro_local no está en este género")
            return
        if puntuacion<0 or puntuacion>10:
            print("La puntuación debe ser entre 0 y 10")
            return
        self.__valoraciones[libro]=puntuacion

    def mostrar_valoraciones(self):
        for libro in self.__valoraciones:
            print(libro,":",self.__valoraciones[libro])