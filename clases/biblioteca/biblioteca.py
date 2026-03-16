class Biblioteca:
    def __init__(self,nombre):
        self.nombre=nombre
        self.libros=[] # Lista vacía de los libros que contendrá la biblioteca

    def agregar_libro(self,libro): # Método para agregar un libro a la biblioteca
        self.libros.append(libro.titulo)

    def eliminar_libro(self,libro): # Método para eliminar un libro de la biblioteca
        if libro.titulo in self.libros: # Verifica si el libro está en la biblioteca
            self.libros.remove(libro.titulo) # Si está lo elimina
        else: # Si no está mensaje de error
            print('El libro no existe.')

    def mostrar_info(self):
        return f'Nombre: {self.nombre} | Libros: {self.libros}'