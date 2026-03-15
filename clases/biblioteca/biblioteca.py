class Biblioteca:
    def __init__(self,nombre):
        self.nombre=nombre
        self.libros=[] # Lista vacía de los libros que contendrá la biblioteca

    def agregar_libro(self,libro): # Método para agregar un libro a la biblioteca
        self.libros.append(libro)
        print('Libro agregado correctamente.')

    def eliminar_libro(self,libro): # Método para eliminar un libro de la biblioteca
        if libro in self.libros: # Verifica si el libro está en la biblioteca
            self.libros.remove(libro) # Si está lo elimina
            print('Libro eliminado correctamente.')
        else: # Si no está mensaje de error
            print('El libro no existe.')