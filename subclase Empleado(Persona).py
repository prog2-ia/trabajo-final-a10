class Empleado(Persona):
    def __init__(self, dni, nombre, apellido, edad, id_empleado, puesto):
        super().__init__(dni, nombre, apellido, edad)
        self.id_empleado = id_empleado
        self.puesto = puesto.lower()
        self.libros_gestionados = 0

    def gestionar_registro(self, biblioteca, libro):
        permisos_validos = ['bibliotecario', 'administrador']

        if self.puesto in permisos_validos:
            biblioteca.agregar_libro(libro)
            self.libros_gestionados += 1
            print(f"El empleado {self.nombre} (ID: {self.id_empleado}) ha registrado el libro '{libro.titulo}'.")
            print(f"Total gestionado por este empleado: {self.libros_gestionados}")
        else:
            print(f"ACCESO DENEGADO: El puesto de '{self.puesto}' no tiene permisos para modificar el inventario.")

    def mostrar_info(self):
        return (f"EMPLEADO #{self.id_empleado}\n"
                f"Nombre: {self.nombre} {self.apellido}\n"
                f"Cargo: {self.puesto}\n"
                f"{self.libros_gestionados} libros procesados.")