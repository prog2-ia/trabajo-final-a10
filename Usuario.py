#Clase hija usuario
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