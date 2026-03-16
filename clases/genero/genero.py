class Genero:
    def __init__(self,nombre):
        self.nombre=nombre
        self.libros=[] # Lista vacía para guardar libros de ese género

    def agregar(self,libro,biblioteca): # Método para agregar un libro de ese género
        if libro.titulo not in biblioteca.libros: # Verifica primero que el libro exista en la biblioteca
            print('El libro_local no existe en la biblioteca')
            return
        for i in self.libros: # Verifica si el libro ya está en la lista de su género
            if i==libro.titulo:
                print('El libro_local ya existe en este género')
                return
        self.libros.append(libro.titulo) # Si todo lo demás no se cumple, añade el libro a la lista
        libro.genero=self

    def mostrar_info(self): # Método para mostrar información sobre un género específico
        return f'Nombre: {self.nombre} | Libros: {self.libros}'