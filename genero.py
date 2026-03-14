#Clase padre genero
class Genero:
    def __init__(self,nombre):
        self.nombre=nombre
        self.libros=[]

    def agregar(self,libro,biblioteca):
        if libro not in biblioteca.libros:
            print('El libro no existe en la biblioteca')
            return
        for i in self.libros:
            if i.titulo==libro.titulo:
                print('El libro ya existe en este género')
                return
        self.libros.append(libro)
        libro.genero=self

    def listar(self):
        if not self.libros:
            print("El género está vacío")
        else:
            for libro in self.libros:
                print(libro)

    def mostrar_info_genero(self):
        print('Género: ',self.nombre)
        print('Número de libros: ',len(self.libros))