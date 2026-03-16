from clases.persona_local.persona_local import Persona

class Empleado(Persona):
    def __init__(self, dni, nombre, apellido, edad, id_empleado, puesto):
        super().__init__(dni, nombre, apellido, edad)
        self.__id_empleado = id_empleado # Atributo privado. Dato únicamente de la biblioteca
        self._puesto = puesto.lower() # Atributo protegido, ya que es información profesional
        self.libros_gestionados = 0 # Contador que almacena el número de libros gestionados por los empleados

    def gestionar_registro(self, biblioteca, libro): # Método para gestionar un libro
        # Solo los empleados con estos cargos pueden gestionar un libro
        permisos_validos = ['bibliotecario', 'administrador']

        if self._puesto in permisos_validos: # Verifica que el empleado sea un cargo válido
            biblioteca.agregar_libro(libro)
            self.libros_gestionados += 1
            print(f"El empleado {self.nombre} (ID: {self.__id_empleado}) ha registrado el libro '{libro.titulo}'.")
            print(f"Total gestionado por este empleado: {self.libros_gestionados}")
        else: # Si el empleado no tiene un cargo válido, no puede gestionar un libro
            print(f"ACCESO DENEGADO: El puesto de '{self._puesto}' no tiene permisos para modificar el inventario.")

    def mostrar_info(self): # Método para mostrar la info de un empleado
        return f'{super().mostrar_info()} | ID_empleado: {self.__id_empleado} | Puesto: {self._puesto}'