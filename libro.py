#Clase padre libro
class Libro:
    def __init__(self,titulo,autor,anyo): #Crear un libro (inicialmente disponible para préstamos)
        self.titulo=titulo
        self.autor=autor
        self.anyo=anyo
        self.disponible=True

    def prestar(self): #Prestar el libro dependiendo de que si está disponible o no
        if self.disponible:
            self.disponible=False
            print('Libro prestado con éxito.')
        else:
            print('El libro ya está prestado.')

    def devolver(self): #Devolver el libro
        self.disponible=True
        print('Libro devuelto con éxito.')

    def mostrar_info(self): #Mostrar información del libro
        if self.disponible:
            estado='Disponible'
        else:
            estado='Prestado'
        return f'Título: {self.titulo} | Autor: {self.autor} | Año: {self.anyo} | Estado: {estado}'