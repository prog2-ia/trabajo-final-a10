class Valoracion: #No utilizado de momento
    def __init__(self):
        # Atributo privado para evitar la manipulación
        self.__valoraciones = {} # Diccionario sobre las valoraciones de cada libro

    def valorar(self, biblioteca, libro, puntuacion): # Método que recibe la biblioteca para valorar un libro de esta
        if libro not in biblioteca.libros: # Comprueba que el libro exista dentro de la biblioteca proporcionada
            print(f"Error: El libro '{libro}' no pertenece a la biblioteca {biblioteca.nombre}")
            return # Sale si el libro no existe

        if puntuacion < 0 or puntuacion > 10: # Se asegura que la puntuación sea entre 0 y 10
            print("La puntuación debe ser entre 0 y 10")
            return # Sale si la nota no es válida

        self.__valoraciones[libro] = puntuacion # Si todo se cumple, agrega la valoración al diccionario
        print(f"Valoración de {puntuacion} añadida a '{libro}'")

    def mostrar_valoraciones(self): # Método para mostrar las valoraciones
        for libro in self.__valoraciones:
            print(libro, ":", self.__valoraciones[libro])