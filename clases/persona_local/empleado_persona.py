from clases.persona_local.persona_local import Persona

class Empleado(Persona):
    def __init__(self, dni: str, nombre: str, apellido: str, edad: int, id_empleado: str, puesto: str) -> None:
        super().__init__(dni, nombre, apellido, edad)
        self.id_empleado: str = id_empleado # Atributo privado. Dato únicamente de la biblioteca
        self._puesto: str = puesto.lower() # Atributo protegido, ya que es información profesional
        self.libros_gestionados: int = 0 # Contador que almacena el número de libros gestionados por los empleados

    def gestionar_registro(self, biblioteca, libro) -> None: # Método para gestionar un libro
        # Solo los empleados con estos cargos pueden gestionar un libro
        permisos_validos: list[str] = ['bibliotecario', 'administrador']

        if self._puesto in permisos_validos: # Verifica que el empleado sea un cargo válido
            biblioteca.agregar_libro(libro)
            self.libros_gestionados += 1
            print(f"El empleado {self.nombre} (ID: {self.id_empleado}) ha registrado el libro '{libro.titulo}'.")
            print(f"Total gestionado por este empleado: {self.libros_gestionados}")
        else: # Si el empleado no tiene un cargo válido, no puede gestionar un libro
            print(f"ACCESO DENEGADO: El puesto de '{self._puesto}' no tiene permisos para modificar el inventario.")

    def mostrar_info(self) -> str: # Método para mostrar la info de un empleado
        return f'{super().mostrar_info()} | ID_empleado: {self.id_empleado} | Puesto: {self._puesto}'