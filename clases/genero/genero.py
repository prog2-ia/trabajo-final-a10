class Genero:
    def __init__(self, nombre: str) -> None:
        self.nombre: str = nombre
        self.libros: list[str] = [] # Lista vacía para guardar libros de ese género

    def agregar(self, libro: Libro) -> None: # Método para agregar un libro de ese género
        for i in self.libros: # Verifica si el libro ya está en la lista de su género
            if i == libro.titulo:
                print('El libro_local ya existe en este género')
                return

        self.libros.append(libro.titulo) # Si todo lo demás no se cumple, añade el libro a la lista
        libro.genero = self

    def mostrar_info(self) -> str: # Método para mostrar información sobre un género específico
        return f'Nombre: {self.nombre} | Libros: {self.libros}'