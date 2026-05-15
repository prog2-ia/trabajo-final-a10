from clases.libro_local.fisico_libro import Fisico
from clases.libro_local.digital_libro import Digital
from clases.persona_local.empleado_persona import Empleado
from clases.persona_local.usuario_persona import Usuario
from clases.genero.genero import Genero
from ejecucion.objetos import bd_libros, bd_empleados, bd_usuarios, bd_generos

#Funciones: la Biblioteca
def agregar_libro_biblio(biblioteca, libro) -> None: #Agregar un libro a la Biblioteca
    biblioteca.agregar_libro(libro)

def eliminar_libro_biblio(biblioteca, libro) -> None: #Eliminar un libro de la Biblioteca
    biblioteca.eliminar_libro(libro)

def mostrar_info_biblio(biblioteca) -> None: #Mostrar información de la Biblioteca
    print(biblioteca.mostrar_info())

#Funciones: libros
def crear_libro_fisico(titulo: str, autor: str, anyo: int, estanteria: str) -> Fisico: #Crear un libro físico
    libro: Fisico = Fisico(titulo, autor, anyo, estanteria)
    bd_libros.append(libro)
    return libro

def reportar_condicion_libro(libro, condicion: str) -> None: #Reportar la condición de un libro físico
    libro.reportar_condicion(condicion)

def crear_libro_digital(titulo: str, autor: str, anyo: int, formato: str, url: str) -> Digital: #Crear un libro digital
    libro: Digital = Digital(titulo, autor, anyo, formato, url)
    bd_libros.append(libro)
    return libro

def mostrar_info_libro(libro) -> None: #Mostrar información de un libro
    print(libro.mostrar_info())

#Funciones: personas
def crear_empleado(dni: str, nombre: str, apellido: str, edad: int, id_empleado: str, puesto: str) -> Empleado: #Crear un empleado
    empleado: Empleado = Empleado(dni, nombre, apellido, edad, id_empleado, puesto)
    bd_empleados.append(empleado)
    return empleado

def gestionar_registro_empleado(empleado, biblioteca, libro) -> None: #Gestionar registro (solo algunos empleados)
    empleado.gestionar_registro(biblioteca, libro)

def crear_usuario(dni: str, nombre: str, apellido: str, edad: int) -> Usuario: #Crear un usuario
    usuario: Usuario = Usuario(dni, nombre, apellido, edad)
    bd_usuarios.append(usuario)
    return usuario

def prestar_libro_usuario(usuario, libro) -> None: #Prestar un libro
    usuario.prestar_libro(libro)

def devolver_libro_usuario(usuario, libro) -> None: #Devolver un libro
    usuario.devolver_libro(libro)

def mostrar_info_persona(persona) -> None: #Mostrar información de una persona
    print(persona.mostrar_info())

#Funciones: géneros
def crear_genero(nombre: str) -> Genero: #Crear un género
    genero: Genero = Genero(nombre)
    bd_generos.append(genero)
    return genero

def agregar_libro_genero(genero, libro) -> None: #Agregar un libro al género
    genero.agregar(libro)

def mostrar_info_genero(genero) -> None: #Mostrar información de un género
    print(genero.mostrar_info())

#Funciones de búsqueda: básicamente lo que hacen es devolver la información completa de algo dado solo su título, nombre, etc.
def buscar_libro(libro: str) -> tuple:
    libros: list = bd_libros
    validez: bool = False

    for i in libros:
        if i.titulo == libro:
            libro = i
            validez = True

    return libro, validez

def buscar_empleado(dni: str) -> tuple:
    empleados: list = bd_empleados
    validez: bool = False

    for i in empleados:
        if i.dni == dni:
            dni = i
            validez = True

    return dni, validez

def buscar_usuario(dni: str) -> tuple:
    usuarios: list = bd_usuarios
    validez: bool = False

    for i in usuarios:
        if i.dni == dni:
            dni = i
            validez = True

    return dni, validez

def buscar_genero(genero: str) -> tuple:
    generos: list = bd_generos
    validez: bool = False

    for i in generos:
        if i.nombre == genero:
            genero = i
            validez = True

    return genero, validez