from clases.libro_local.libro_local import Libro

class Fisico(Libro):
    def __init__(self, titulo: str, autor: str, anyo: int, estanteria: str, condicion: str = "Excelente") -> None:
        super().__init__(titulo, autor, anyo)
        self._estanteria: str = estanteria # Atributo protegido por seguridad
        self.condicion: str = condicion

    def mostrar_info(self) -> str: # Método para mostrar la info de un libro físico #
        info_fisico: str = super().mostrar_info() # Extendemos el método original
        return f"{info_fisico} | Ubicación: Estantería {self._estanteria} | Condición: {self.condicion}"

    def reportar_condicion(self, nueva_condicion: str) -> None: # Método para actualizar el estado de un libro físico
        self.condicion = nueva_condicion
        print(f"El estado de '{self.titulo}' ha sido actualizado a: {self.condicion}")