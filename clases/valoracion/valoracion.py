class Valoracion:
    def __init__(self) -> None:
        self.valoraciones: dict = {} # Diccionario sobre las valoraciones de cada libro

    def valorar(self, libro, puntuacion: int | float) -> None: # Método que recibe la biblioteca para valorar un libro de esta

        if puntuacion < 0 or puntuacion > 10: # Se asegura que la puntuación sea entre 0 y 10
            print("La puntuación debe ser entre 0 y 10")
            return # Sale si la nota no es válida

        self.valoraciones[libro.titulo] = puntuacion # Si todo se cumple, agrega la valoración al diccionario

    def mostrar_valoraciones(self) -> None: # Método para mostrar las valoraciones
        for libro, puntuacion in self.valoraciones.items():
            print(libro, ':', puntuacion)

    def __repr__(self) -> str:
        return f'Valoraciones: {self.valoraciones}'