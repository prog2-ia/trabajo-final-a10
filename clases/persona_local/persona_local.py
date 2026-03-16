class Persona: # Clase que contiene únicamente los atributos de la persona
    def __init__(self,dni,nombre,apellido,edad):
        self.dni=dni
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad

    def mostrar_info(self):
        return f'DNI: {self.dni} | Nombre: {self.nombre} | Apellido: {self.apellido} | Edad: {self.edad}'