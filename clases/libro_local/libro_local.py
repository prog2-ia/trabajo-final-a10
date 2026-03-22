from abc import ABC

class Libro(ABC):
    def __init__(self,titulo,autor,anyo):
        self.titulo=titulo
        self.autor=autor
        self.anyo=anyo
        self.disponible=True # Disponible por defecto para poder hacer prestaciones
        self.genero=None

    def prestar(self): # Método para prestar un libro
        if self.disponible: # Si está disponible se cambia a False para poner que ya ha sido prestado
            self.disponible=False
            print(f'Libro "{self.titulo}" prestado con éxito.')
        else: # Si ya no está disponible (False) es porque ya ha sido prestado
            print('El libro ya está prestado.')

    def devolver(self): # Método para devolver un libro
        if self.disponible:
            print('Libro disponible todavía.')
        else:
            self.disponible=True # Disponible vuelve a estar en True porque ha sido devuelto
            print(f'Libro "{self.titulo}" devuelto con éxito.')

    def mostrar_info(self): # Método para mostrar la info de un libro
        if self.disponible:
            estado='Disponible'
        else:
            estado='Prestado'
        if self.genero:
            genero=self.genero.nombre
        else:
            genero='Sin género'
        return f'Título: {self.titulo} | Autor: {self.autor} | Año: {self.anyo} | Género: {genero} | Estado: {estado}'