from clases.libro_local.fisico_libro import Fisico
from clases.libro_local.digital_libro import Digital

def crear_libro_fisico():
    titulo=input('Introduce el titulo: ')
    autor=input('Introduce el autor: ')
    anyo=int(input('Introduce el año: '))
    estanteria=input('Introduce la estanteria: ')
    libro=Fisico(titulo,autor,anyo,estanteria)
    return libro

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