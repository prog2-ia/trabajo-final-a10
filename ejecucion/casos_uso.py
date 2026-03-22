from clases.libro_local.fisico_libro import Fisico
from clases.libro_local.digital_libro import Digital
from clases.persona_local.empleado_persona import Empleado
from clases.persona_local.usuario_persona import Usuario
from clases.genero.genero import Genero
from ejecucion.objetos import bd_libros, bd_empleados, bd_usuarios, bd_generos



#Biblioteca
def agregar_libro_biblio(biblioteca,libro):
    biblioteca.agregar_libro(libro)

def eliminar_libro_biblio(biblioteca,libro):
    biblioteca.eliminar_libro(libro)

def mostrar_info_biblio(biblioteca):
    print(biblioteca.mostrar_info())



#Libro
def crear_libro_fisico(titulo,autor,anyo,estanteria):
    libro=Fisico(titulo,autor,anyo,estanteria)
    bd_libros.append(libro)
    return libro

def reportar_condicion_libro(libro,condicion):
    libro.reportar_condicion(condicion)

def crear_libro_digital(titulo,autor,anyo,formato,url):
    libro=Digital(titulo,autor,anyo,formato,url)
    bd_libros.append(libro)
    return libro

def mostrar_info_libro(libro):
    print(libro.mostrar_info())



#Persona
def crear_empleado(dni,nombre,apellido,edad,id_empleado,puesto):
    empleado=Empleado(dni,nombre,apellido,edad,id_empleado,puesto)
    bd_empleados.append(empleado)
    return empleado

def gestionar_registro_empleado(empleado,biblioteca,libro):
    empleado.gestionar_registro(biblioteca,libro)

def crear_usuario(dni,nombre,apellido,edad):
    usuario=Usuario(dni,nombre,apellido,edad)
    bd_usuarios.append(usuario)
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
    bd_generos.append(genero)
    return genero

def agregar_libro_genero(genero,libro,biblioteca):
    genero.agregar(libro,biblioteca)

def mostrar_info_genero(genero):
    print(genero.mostrar_info())



#Funciones especiales
def buscar_titulo_libro(libro):
    libros=bd_libros
    validez=False
    for i in libros:
        if i.titulo==libro:
            libro=i
            validez=True
    return libro,validez

def buscar_empleado(dni):
    empleados=bd_empleados
    validez=False
    for i in empleados:
        if i.dni==dni:
            dni=i
            validez=True
    return dni,validez

def buscar_usuario(dni):
    usuarios=bd_usuarios
    validez=False
    for i in usuarios:
        if i.dni==dni:
            dni=i
            validez=True
    return dni,validez

def buscar_genero(genero):
    generos=bd_generos
    validez=False
    for i in generos:
        if i.nombre==genero:
            genero=i
            validez=True
    return genero,validez