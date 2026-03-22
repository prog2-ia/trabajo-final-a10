from clases.biblioteca.biblioteca import Biblioteca
from clases.libro_local.fisico_libro import Fisico
from clases.libro_local.digital_libro import Digital
from clases.persona_local.empleado_persona import Empleado
from clases.persona_local.usuario_persona import Usuario
from clases.genero.genero import Genero



#Libros
libro_fis1=Fisico('Don Quijote de la Mancha','Miguel de Cervantes',1605,'A1')
libro_fis2=Fisico('1984','George Orwell',1949,'B2')
libro_dig1=Digital('Clean Code', 'Robert C. Martin', 2008, 'PDF', 'https://descarga.com/cleancode')
libro_dig2=Digital('Python Crash Course', 'Eric Matthes', 2019, 'EPUB', 'https://biblioteca.com/pythoncrashcourse')
bd_libros=[libro_fis1,libro_fis2,libro_dig1,libro_dig2]



#Empleados
empleado1=Empleado('11111111A','Ana','Garcia',35,'EMP001','bibliotecario')
empleado2=Empleado('44444444D','Carlos','Sanchez',31,'EMP004','asistente')
bd_empleados=[empleado1,empleado2]



#Usuarios
usuario1=Usuario('55555555E','Juan','Perez',21)
usuario2=Usuario('66666666F','Laura','Diaz',19)
bd_usuarios=[usuario1,usuario2]



#Géneros
genero1=Genero('Fantasía')
genero2=Genero('Ciencia ficción')
bd_generos=[genero1,genero2]



#Biblioteca
biblioteca_central=Biblioteca('Biblioteca Central')
for ijk in bd_libros:
    biblioteca_central.agregar_libro(ijk)