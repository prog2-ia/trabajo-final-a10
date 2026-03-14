from libro import Libro

class Digital(Libro):
    def __init__(self, titulo, autor, anyo, formato, url):
        super().__init__(titulo, autor, anyo)
        self.formato = formato
        self.__url = url # Atributo privado para la seguridad del enlace

    def prestar(self):
        print(f"Enviando enlace de descarga ({self.formato}) al usuario: {self.__url}")
        # Sobreescribimos el método ya que un libro digital siempre está disponible

    def mostrar_info(self):
        info_digital = super().mostrar_info()
        return f"{info_digital} | Formato: {self.formato}"