from genero import Genero

class Valoracion(Genero):
    def __init__(self,nombre):
        super().__init__(nombre)
        # Atributo privado para evitar la manipulación
        self.__valoraciones={} # Diccionario sobre las valoraciones de cada libro

    def valorar(self,libro,puntuacion): # Método para valorar un libro
        if libro not in self.libros: # Verifica que el libro existe y está en ese género
            print("El libro_local no está en este género")
            return
        if puntuacion<0 or puntuacion>10: # Asegura que la puntuación es entre 0 y 10
            print("La puntuación debe ser entre 0 y 10")
            return
        self.__valoraciones[libro]=puntuacion # Añade la valoración junto con su respectivo libro al diccionario

    def mostrar_valoraciones(self): # Método para mostrar las valoraciones
        for libro in self.__valoraciones:
            print(libro,":",self.__valoraciones[libro])