from clases.libro_local.libro_local import Libro

class Fisico(Libro):
    def __init__(self, titulo, autor, anyo, estanteria, seccion, estado="Excelente"):
        super().__init__(titulo, autor, anyo)
        self._estanteria = estanteria # Atributo protegido por seguridad
        self._seccion = seccion # Atributo protegido por seguridad
        self.estado = estado

    def mostrar_info(self): # Método para mostrar la info de un libro físico #
        info_fisico = super().mostrar_info() # Extendemos el método original
        return f"{info_fisico} | Ubicación: Estantería {self._estanteria}, {self._seccion} | Estado: {self.estado}"

    def reportar_estado(self, nuevo_estado): # Método para actualizar el estado de un libro físico
        self.estado = nuevo_estado
        print(f"El estado de '{self.titulo}' ha sido actualizado a: {self.estado}")