from clases.libro_local.libro_local import Libro

class Fisico(Libro):
    def __init__(self, titulo, autor, anyo, estanteria, seccion, estado="Excelente"):
        super().__init__(titulo, autor, anyo)
        self._estanteria = estanteria # Atributo protegido por seguridad
        self._seccion = seccion # Atributo protegido por seguridad
        self.estado = estado

    def mostrar_info(self):
        info_fisico = super().mostrar_info()
        return f"{info_fisico} | Ubicación: Estantería {self._estanteria}, {self._seccion} | Estado: {self.estado}"

    def reportar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        print(f"El estado de '{self.titulo}' ha sido actualizado a: {self.estado}")