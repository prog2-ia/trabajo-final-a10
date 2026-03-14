#Clase padre biblioteca
class Biblioteca:
    def __init__(self,nombre): #Crear una biblioteca (de momento solo una)
        self.nombre=nombre
        self.libros=[]

    def agregar_libro(self,libro): #Agregar el libro_local
        self.libros.append(libro)
        print('Libro agregado correctamente.')

    def eliminar_libro(self,libro): #Eliminar el libro_local dependiendo de que si este se encuentra en la lista de libros
        if libro in self.libros:
            self.libros.remove(libro)
            print('Libro eliminado correctamente.')
        else:
            print('El libro_local no existe.')