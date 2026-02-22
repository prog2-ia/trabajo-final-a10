#Clase libro
class Libro:
    def __init__(self,titulo,autor,anyo):
        self.titulo=titulo
        self.autor=autor
        self.anyo=anyo
        self.disponible=True

    def prestar(self):
        if self.disponible:
            self.disponible=False
            print('Libro prestado con éxito.')
        else:
            print('El libro ya está prestado.')

    def dovolver(self):
        self.disponible=True
        print('Libro devuelto con éxito.')

    def mostrar_info(self):
        if self.disponible:
            estado='Disponible'
        else:
            estado='Prestado'
        return f'Título: {self.titulo} | Autor: {self.autor} | Año: {self.anyo} | Estado: {estado}'

#Clase usuario
class Usuario:
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
        self.prestados=[]