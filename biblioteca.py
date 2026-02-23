#Clase libro
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

    def dovolver(self): #Devolver el libro
        self.disponible=True
        print('Libro devuelto con éxito.')

    def mostrar_info(self): #Mostrar información del libro
        if self.disponible:
            estado='Disponible'
        else:
            estado='Prestado'
        return f'Título: {self.titulo} | Autor: {self.autor} | Año: {self.anyo} | Estado: {estado}'



#Clase usuario
class Usuario:
    def __init__(self,nombre,apellido): #Crear un usuario
        self.nombre=nombre
        self.apellido=apellido
        self.prestados=[]

    def prestar_libro(self,libro): #Prestar el libro dependiendo de que si este esté disponible
        if libro.disponible:
            libro.prestar()
            self.prestados.append(libro)
        else:
            print('No se puede prestar el libro.')

    def devolver_libro(self,libro): #Devolver el libro dependiendo de que si este se encuentra entre los prestados
        if libro in self.prestados:
            libro.devolver()
            self.prestados.remove(libro)
        else:
            print('Libro incorrecto.')