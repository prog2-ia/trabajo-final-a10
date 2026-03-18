class Favoritos:
    def __init__(self):
        self.favoritos = [] # Lista vacía donde se almacenarán los libros marcados como favoritos

    def marcar_favorito(self, biblioteca, libro): # Método que recibe la biblioteca para marcar un libro como favorito de esta
        # Verifica que el libro exista en la biblioteca y que no haya sido añadido previamente a favoritos
        if libro in biblioteca.libros and libro not in self.favoritos:
            self.favoritos.append(libro)
            print(f"'{libro}' ha sido añadido a tus favoritos.")
        elif libro not in biblioteca.libros: # Si el libro no está en esa biblioteca...
            print(f"Error: El libro '{libro}' no existe en la biblioteca {biblioteca.nombre}.")
        else: # Si el libro ya estaba en la lista...
            print(f"El libro '{libro}' ya está en tu lista de favoritos.")

    def listar_favoritos(self): # Método que muestra la lista de favoritos
        if not self.favoritos: # Si la lista de favoritos está vacía...
            print("No tienes libros marcados como favoritos actualmente.")
        else: # Si hay elementos en la lista...
            print("Tu lista de libros favoritos:")
            contador = 1 # Contador para la enumeración visual
            for libro in self.favoritos:
                print(f"{contador}. {libro}")
                contador = contador + 1