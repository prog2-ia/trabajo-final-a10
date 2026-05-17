import pickle

from clases.libro_local.fisico_libro import Fisico
from clases.libro_local.digital_libro import Digital
from clases.persona_local.empleado_persona import Empleado
from clases.persona_local.usuario_persona import Usuario
from clases.genero.genero import Genero
from ejecucion.objetos import bd_libros, bd_empleados, bd_usuarios, bd_generos, sistema_valoraciones

#Funciones: la Biblioteca
def agregar_libro_biblio(biblioteca, libro) -> None: #Agregar un libro a la Biblioteca
    biblioteca.agregar_libro(libro)
    guardar_sistema()

def eliminar_libro_biblio(biblioteca, libro) -> None: #Eliminar un libro de la Biblioteca
    biblioteca.eliminar_libro(libro)
    guardar_sistema()

def mostrar_info_biblio(biblioteca) -> None: #Mostrar información de la Biblioteca
    print(biblioteca.mostrar_info())

#Funciones: libros
def crear_libro_fisico(titulo: str, autor: str, anyo: int, estanteria: str) -> Fisico: #Crear un libro físico
    libro: Fisico = Fisico(titulo, autor, anyo, estanteria)
    bd_libros.append(libro)
    guardar_sistema()
    return libro

def reportar_condicion_libro(libro, condicion: str) -> None: #Reportar la condición de un libro físico
    libro.reportar_condicion(condicion)
    guardar_sistema()

def crear_libro_digital(titulo: str, autor: str, anyo: int, formato: str, url: str) -> Digital: #Crear un libro digital
    libro: Digital = Digital(titulo, autor, anyo, formato, url)
    bd_libros.append(libro)
    guardar_sistema()
    return libro

def mostrar_info_libro(libro) -> None: #Mostrar información de un libro
    print(libro.mostrar_info())

#Funciones: personas
def crear_empleado(dni: str, nombre: str, apellido: str, edad: int, id_empleado: str, puesto: str) -> Empleado: #Crear un empleado
    empleado: Empleado = Empleado(dni, nombre, apellido, edad, id_empleado, puesto)
    bd_empleados.append(empleado)
    guardar_sistema()
    return empleado

def gestionar_registro_empleado(empleado, biblioteca, libro) -> None: #Gestionar registro (solo algunos empleados)
    empleado.gestionar_registro(biblioteca, libro)
    guardar_sistema()

def crear_usuario(dni: str, nombre: str, apellido: str, edad: int) -> Usuario: #Crear un usuario
    usuario: Usuario = Usuario(dni, nombre, apellido, edad)
    bd_usuarios.append(usuario)
    guardar_sistema()
    return usuario

def prestar_libro_usuario(usuario, libro) -> None: #Prestar un libro
    usuario.prestar_libro(libro)
    guardar_sistema()

def devolver_libro_usuario(usuario, libro) -> None: #Devolver un libro
    usuario.devolver_libro(libro)
    guardar_sistema()

def mostrar_info_persona(persona) -> None: #Mostrar información de una persona
    print(persona.mostrar_info())

#Funciones: géneros
def crear_genero(nombre: str) -> Genero: #Crear un género
    genero: Genero = Genero(nombre)
    bd_generos.append(genero)
    guardar_sistema()
    return genero

def agregar_libro_genero(genero, libro) -> None: #Agregar un libro al género
    genero.agregar(libro)
    guardar_sistema()

def mostrar_info_genero(genero) -> None: #Mostrar información de un género
    print(genero.mostrar_info())

#Funciones: valoraciones
def valorar_libro(libro,valoracion) -> None: #Valorar un libro
    sistema_valoraciones.valorar(libro,valoracion)
    guardar_sistema()

def mostrar_info_valoraciones() -> None:
    sistema_valoraciones.mostrar_valoraciones()

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

#Excepción personalizada para controlar que las entradas sean números
def pedir_entero(mensaje:str)->int:
    while True:
        try:
            return int(input(mensaje))

        except ValueError:
            print('Error: introduce un número válido')

#Ficheros binarios
def guardar_sistema()->None:
    datos={
        'libros': bd_libros,
        'usuarios': bd_usuarios,
        'empleados': bd_empleados,
        'generos': bd_generos
    }

    with open('biblioteca.dat','wb') as fichero:
        pickle.dump(datos, fichero)

def cargar_sistema()->dict:
    try:
        with open('biblioteca.dat','rb') as fichero:
            return pickle.load(fichero)

    except FileNotFoundError:
        #Primero creamos los objetos iniciales
        libro_fis1: Fisico = Fisico('Don Quijote de la Mancha', 'Miguel de Cervantes', 1605, 'A1')
        libro_fis2: Fisico = Fisico('1984', 'George Orwell', 1949, 'B2')
        libro_dig1: Digital = Digital('Clean Code', 'Robert C. Martin', 2008, 'PDF', 'https://descarga.com/cleancode')
        libro_dig2: Digital = Digital('Python Crash Course', 'Eric Matthes', 2019, 'EPUB','https://biblioteca.com/pythoncrashcourse')

        empleado1: Empleado = Empleado('11111111A', 'Ana', 'Garcia', 35, 'EMP001', 'bibliotecario')
        empleado2: Empleado = Empleado('44444444D', 'Carlos', 'Sanchez', 31, 'EMP004', 'asistente')

        usuario1: Usuario = Usuario('55555555E', 'Juan', 'Perez', 21)
        usuario2: Usuario = Usuario('66666666F', 'Laura', 'Diaz', 19)

        genero1: Genero = Genero('Fantasía')
        genero2: Genero = Genero('Ciencia ficción')

        datos={
            'libros':[libro_fis1,libro_fis2,libro_dig1,libro_dig2],
            'empleados': [empleado1, empleado2],
            'usuarios':[usuario1,usuario2],
            'generos':[genero1,genero2],
        }

        with open('biblioteca.dat','wb') as fichero:
            pickle.dump(datos,fichero)

        return datos

#Ficheros de texto
def exportar_informe_txt():
    with open('informe_biblioteca.txt', 'w', encoding='utf-8') as f:

        f.write("=== LIBROS ===\n")
        for libro in bd_libros:
            f.write(f"{libro.titulo} - {libro.autor}\n")

        f.write("\n=== USUARIOS ===\n")
        for u in bd_usuarios:
            f.write(f"{u.dni} - {u.nombre} {u.apellido}\n")

        f.write("\n=== EMPLEADOS ===\n")
        for e in bd_empleados:
            f.write(f"{e.dni} - {e.nombre}\n")