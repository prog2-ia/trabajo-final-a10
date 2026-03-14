from genero import Genero

class Favoritos(Genero):
    def __init__(self,nombre):
        super().__init__(nombre)
        self.favoritos=[]

    def marcar_favorito(self,libro):
        if libro in self.libros and libro not in self.favoritos:
            self.favoritos.append(libro)

    def listar_favoritos(self):
        if not self.favoritos:
            print("No hay libros favoritos en este género")
        else:
            print("Libros favoritos del género:", self.nombre)
            contador = 1
            for libro in self.favoritos:
                print(contador, libro)
                contador = contador + 1