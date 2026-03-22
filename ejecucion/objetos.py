from clases.biblioteca.biblioteca import Biblioteca
from clases.libro_local.fisico_libro import Fisico
from clases.libro_local.digital_libro import Digital
from clases.persona_local.empleado_persona import Empleado
from clases.persona_local.usuario_persona import Usuario
from clases.genero.genero import Genero

def bd_biblioteca():
    biblioteca=Biblioteca('Biblioteca Central')
    for i in bd_libro():
        biblioteca.agregar_libro(i)
    return biblioteca

def bd_libro():
    libro_fis1=Fisico('Don Quijote de la Mancha','Miguel de Cervantes',1605,'A1')
    libro_fis2=Fisico('1984','George Orwell',1949,'B2')
    libro_dig1=Digital('Clean Code', 'Robert C. Martin', 2008, 'PDF', 'https://descarga.com/cleancode')
    libro_dig2=Digital('Python Crash Course', 'Eric Matthes', 2019, 'EPUB', 'https://biblioteca.com/pythoncrashcourse')
    return [libro_fis1,libro_fis2,libro_dig1,libro_dig2]

def bd_empleado():
    empleado1=Empleado('11111111A','Ana','Garcia',35,'EMP001','bibliotecario')
    empleado2=Empleado('44444444D','Carlos','Sanchez',31,'EMP004','asistente')
    return [empleado1,empleado2]

def bd_usuario():
    usuario1=Usuario('55555555E','Juan','Perez',21)
    usuario2=Usuario('66666666F','Laura','Diaz',19)
    return [usuario1,usuario2]

def bd_genero():
    genero1=Genero('Fantasía')
    genero2=Genero('Ciencia ficción')
    return [genero1,genero2]