class Prestamos:
    def __init__(self, usuario, libro) -> None:
        self.usuario = usuario
        self.libro = libro
        self.activo: bool = True

    def finalizar_prestamo(self) -> None:
        self.activo = False