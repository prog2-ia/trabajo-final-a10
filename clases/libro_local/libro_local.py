from abc import ABC

class Libro(ABC):
    def __init__(self, titulo: str, autor: str, anyo: int) -> None:
        self.titulo: str = titulo
        self.autor: str = autor
        self.anyo: int = anyo
        self.disponible: bool = True # Disponible por defecto para poder hacer prestaciones
        self.genero = None

    def prestar(self) -> None: # Método para prestar un libro
        if self.disponible: # Si está disponible se cambia a False para poner que ya ha sido prestado
            self.disponible = False
            print(f'Libro "{self.titulo}" prestado con éxito.')
        else: # Si ya no está disponible (False) es porque ya ha sido prestado
            print('El libro ya está prestado.')

    def devolver(self) -> None: # Método para devolver un libro
        if self.disponible:
            print('Libro disponible todavía.')
        else:
            self.disponible = True # Disponible vuelve a estar en True porque ha sido devuelto
            print(f'Libro "{self.titulo}" devuelto con éxito.')

    def mostrar_info(self) -> str: # Método para mostrar la info de un libro
        if self.disponible:
            estado: str = 'Disponible'
        else:
            estado: str = 'Prestado'

        if self.genero:
            genero: str = self.genero.nombre
        else:
            genero: str = 'Sin género'

        return f'Título: {self.titulo} | Autor: {self.autor} | Año: {self.anyo} | Género: {genero} | Estado: {estado}'