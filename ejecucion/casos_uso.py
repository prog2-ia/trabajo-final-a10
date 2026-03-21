from clases.biblioteca.biblioteca import Biblioteca
from clases.libro_local.fisico_libro import Fisico
from clases.libro_local.digital_libro import Digital
from clases.persona_local.empleado_persona import Empleado
from clases.persona_local.usuario_persona import Usuario
from clases.genero.genero import Genero

#Biblioteca
def crear_biblio():
    nombre=input('Introduce el nombre: ')
    biblioteca=Biblioteca(nombre)
    return biblioteca

def agregar_libro_biblio(biblioteca,libro):
    biblioteca.agregar_libro(libro)

def eliminar_libro_biblio(biblioteca,libro):
    biblioteca.eliminar_libro(libro)

def mostrar_info_biblio(biblioteca):
    print(biblioteca.mostrar_info())

#Libro
def crear_libro_fisico():
    titulo=input('Introduce el titulo: ')
    autor=input('Introduce el autor: ')
    anyo=int(input('Introduce el año: '))
    estanteria=input('Introduce la estanteria: ')
    libro=Fisico(titulo,autor,anyo,estanteria)
    return libro

def reportar_condicion_libro(libro,condicion):
    libro.reportar_condicion(condicion)

def crear_libro_digital():
    titulo=input('Introduce el titulo: ')
    autor=input('Introduce el autor: ')
    anyo=int(input('Introduce el año: '))
    formato=input('Introduce el formato: ')
    url=input('Introduce el url: ')
    libro=Digital(titulo,autor,anyo,formato,url)
    return libro

def mostrar_info_libro(libro):
    print(libro.mostrar_info())

#Persona
def crear_empleado(dni,nombre,apellido,edad,id_empleado,puesto):
    empleado=Empleado(dni,nombre,apellido,edad,id_empleado,puesto)
    return empleado

def gestionar_registro_empleado(empleado,biblioteca,libro):
    empleado.gestionar_registro(biblioteca,libro)

def crear_usuario(dni,nombre,apellido,edad):
    usuario=Usuario(dni,nombre,apellido,edad)
    return usuario

def prestar_libro_usuario(usuario,libro):
    usuario.prestar_libro(libro)

def devolver_libro_usuario(usuario,libro):
    usuario.devolver_libro(libro)

def mostrar_info_persona(persona):
    print(persona.mostrar_info())

#Género
def crear_genero(nombre):
    genero=Genero(nombre)
    return genero

def agregar_libro_genero(genero,libro,biblioteca):
    genero.agregar(libro,biblioteca)

def mostrar_info_genero(genero):
    print(genero.mostrar_info())