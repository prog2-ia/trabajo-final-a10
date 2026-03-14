from persona_local import Persona

class Usuario(Persona):
    def __init__(self,dni,nombre,apellido,edad): #Crear un usuario
        super().__init__(dni,nombre,apellido,edad)
        self.__prestados = []  # Atributo privado. Solo el usuario puede gestionar su lista

    def prestar_libro(self,libro): #Prestar el libro_local dependiendo de que si este esté disponible
        if libro.disponible:
            libro.prestar()
            self.__prestados.append(libro)
        else:
            print('No se puede prestar el libro_local.')

    def devolver_libro(self,libro): #Devolver el libro_local dependiendo de que si este se encuentra entre los prestados
        if libro in self.__prestados:
            libro.devolver()
            self.__prestados.remove(libro)
        else:
            print('Libro incorrecto.')