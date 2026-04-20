from clases.libro_local.libro_local import Libro

class Biblioteca:
    def __init__(self,nombre:str)->None:
        self.nombre:str=nombre
        self.libros:list[str]=[] # Lista vacía de los libros que contendrá la biblioteca

    def agregar_libro(self,libro:Libro)->None: # Método para agregar un libro a la biblioteca
        self.libros.append(libro.titulo)

    def eliminar_libro(self,libro:Libro)->None: # Método para eliminar un libro de la biblioteca
        if libro.titulo in self.libros: # Verifica si el libro está en la biblioteca
            self.libros.remove(libro.titulo) # Si está lo elimina
        else: # Si no está mensaje de error
            print('El libro no existe.')

    def mostrar_info(self)->str:
        return f'Nombre: {self.nombre} | Libros: {self.libros}'