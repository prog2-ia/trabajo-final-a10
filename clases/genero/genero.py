class Genero:
    def __init__(self,nombre):
        self.nombre=nombre
        self.libros=[] # Lista vacía para guardar libros de ese género

    def agregar(self,libro,biblioteca): # Método para agregar un libro de ese género
        if libro not in biblioteca.libros: # Verifica primero que el libro exista en la biblioteca
            print('El libro_local no existe en la biblioteca')
            return
        for i in self.libros: # Verifica si el libro ya está en la lista de su género
            if i.titulo==libro.titulo:
                print('El libro_local ya existe en este género')
                return
        self.libros.append(libro) # Si todo lo demás no se cumple, añade el libro a la lista
        libro.genero=self

    def listar(self): # Método para mostrar por pantalla los libros de la lista género
        if not self.libros: # Si no hay libros en la lista, mensaje de error
            print("El género está vacío")
        else: # Si hay libros...
            for libro in self.libros: # Recorre elemento a elemento de la lista y los va imprimiendo
                print(libro)

    def mostrar_info_genero(self): # Método para mostrar información sobre un género específico
        print('Género: ',self.nombre)
        print('Número de libros: ',len(self.libros))