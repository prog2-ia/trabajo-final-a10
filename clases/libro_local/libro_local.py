#Clase padre libro_local
from abc import ABC,abstractmethod

class Libro(ABC):
    def __init__(self,titulo,autor,anyo): #Crear un libro_local (inicialmente disponible para préstamos)
        self.titulo=titulo
        self.autor=autor
        self.anyo=anyo
        self.disponible=True
        self.genero=None

    def prestar(self): #Prestar el libro_local dependiendo de que si está disponible
        if self.disponible:
            self.disponible=False
            print('Libro prestado con éxito.')
        else:
            print('El libro_local ya está prestado.')

    def devolver(self): #Devolver el libro_local
        self.disponible=True
        print('Libro devuelto con éxito.')

    @abstractmethod
    def mostrar_info(self): #Mostrar información del libro_local
        if self.disponible:
            estado='Disponible'
        else:
            estado='Prestado'
        if self.genero:
            genero=self.genero.nombre
        else:
            genero='Sin género'
        return f'Título: {self.titulo} | Autor: {self.autor} | Año: {self.anyo} | Género: {genero} | Estado: {estado}'