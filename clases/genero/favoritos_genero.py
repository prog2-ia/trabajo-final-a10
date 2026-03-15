from genero import Genero

class Favoritos(Genero):
    def __init__(self,nombre):
        super().__init__(nombre)
        self.favoritos=[] # Lista vacía donde almacenaremos los géneros favoritos

    def marcar_favorito(self,libro): # Método para agregar un libro a favoritos
        # Verifica que el libro pertenezca al género y no esté ya en la lista de favoritos
        if libro in self.libros and libro not in self.favoritos:
            self.favoritos.append(libro)

    def listar_favoritos(self): # Método para mostrar los favoritos por consola
        if not self.favoritos: # Si la lista está vacía no hace nada
            print("No hay libros favoritos en este género")
        else:
            print("Libros favoritos del género:", self.nombre)
            contador = 1
            for libro in self.favoritos: # Va recorriendo la lista y los va imprimiendo enumeradamente
                print(contador, libro)
                contador = contador + 1