class Prestamos:
    def __init__(self,usuario,libro):
        self.usuario=usuario
        self.libro=libro
        self.activo=True

    def finalizar_prestamo(self):
        self.activo=False