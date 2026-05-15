from abc import ABC

class Persona(ABC): # Clase que contiene únicamente los atributos de la persona
    def __init__(self, dni: str, nombre: str, apellido: str, edad: int) -> None:
        self.dni: str = dni
        self.nombre: str = nombre
        self.apellido: str = apellido
        self.edad: int = edad

    def mostrar_info(self) -> str:
        return f'DNI: {self.dni} | Nombre: {self.nombre} | Apellido: {self.apellido} | Edad: {self.edad}'