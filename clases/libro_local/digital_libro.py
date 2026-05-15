from clases.libro_local.libro_local import Libro

class Digital(Libro):
    def __init__(self, titulo: str, autor: str, anyo: int, formato: str, url: str) -> None:
        super().__init__(titulo, autor, anyo)
        self.formato: str = formato
        self.__url: str = url # Atributo privado para la seguridad del enlace

    def prestar(self) -> None: # Método para prestar un libro digital a otro usuario
        print(f"Enviando enlace de descarga ({self.formato}) al usuario: {self.__url}")
        # Sobreescribimos el método, ya que un libro digital siempre está disponible

    def mostrar_info(self) -> str: # Método para mostrar la info de un libro digital
        info_digital: str = super().mostrar_info() # Extendemos el método original
        return f"{info_digital} | Formato: {self.formato}"