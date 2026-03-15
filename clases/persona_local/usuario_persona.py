from persona_local import Persona

class Usuario(Persona):
    def __init__(self,dni,nombre,apellido,edad):
        super().__init__(dni,nombre,apellido,edad)
        # Atributo privado. Solo el usuario puede gestionar su lista
        self.__prestados = [] # Lista de los libros que tiene el usuario en posesión porque la biblioteca se los ha prestado

    def prestar_libro(self,libro): # Método para solicitar un libro a la biblioteca
        if libro.disponible: # Verifica que el libro esté disponible (True)
            libro.prestar() # Se ejecuta el método de libro_local
            self.__prestados.append(libro)
        else: # Si disponible = False no se puede solicitar
            print('No se puede prestar el libro.')

    def devolver_libro(self,libro): # Método para que el usuario devuelva un libro a la biblioteca
        if libro in self.__prestados: # Verifica que el libro lo tenga el usuario
            libro.devolver() # Se ejecuta el método de libro_local
            self.__prestados.remove(libro)
        else:
            print('Libro incorrecto.')