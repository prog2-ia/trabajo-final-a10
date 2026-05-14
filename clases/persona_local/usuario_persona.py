from clases.persona_local.persona_local import Persona
from clases.prestamo.prestamos import Prestamos

class Usuario(Persona):
    def __init__(self,dni,nombre,apellido,edad):
        super().__init__(dni,nombre,apellido,edad)
        # Atributo privado. Solo el usuario puede gestionar su lista
        self.__prestamos=[] # Lista de los libros que tiene el usuario en posesión porque la biblioteca se los ha prestado

    def prestar_libro(self,libro): # Método para solicitar un libro a la biblioteca
        if libro.disponible: # Verifica que el libro esté disponible (True)
            libro.prestar() # Se ejecuta el método de libro_local
            nuevo_prestamo=Prestamos(self,libro)
            self.__prestamos.append(nuevo_prestamo)
        else: # Si disponible = False no se puede solicitar
            print('No se puede prestar el libro.')

    def devolver_libro(self,libro): # Método para que el usuario devuelva un libro a la biblioteca
        for pres in self.__prestamos:
            if pres.libro==libro and pres.activo:
                libro.devolver()
                pres.finalizar_prestamo()
                return
        print('No se puede devolver el libro.')