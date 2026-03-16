from clases.biblioteca.biblioteca import Biblioteca
from clases.libro_local.fisico_libro import Fisico
from clases.libro_local.digital_libro import Digital
from clases.persona_local.empleado_persona import Empleado
from clases.persona_local.usuario_persona import Usuario
from clases.genero.genero import Genero

biblioteca_central=Biblioteca('Biblioteca central')

libro1=Fisico('Don Quijote de la Mancha','Miguel de Cervantes',1605,'A1')
libro2=Fisico('1984','George Orwell',1949,'B2')
libro3=Fisico('La sombra del viento','Carlos Ruiz Zafón',2001,'C2')
libro4=Fisico('Los juegos del hambre','Suzanne Collins',2008,'D4')
libro5=Digital('Clean Code','Robert C. Martin',2008,'PDF','https://descarga.com/cleancode')
libro6=Digital('Python Crash Course','Eric Matthes',2019,'EPUB','https://biblioteca.com/pythoncrashcourse')

empleado1=Empleado('11111111A','Ana','Garcia',35,'EMP001','bibliotecario')
empleado2=Empleado('22222222B','Luis','Martinez',42,'EMP002','administrador')
empleado3=Empleado('33333333C','Marta','Lopez',29,'EMP003','bibliotecario')
empleado4=Empleado('44444444D','Carlos','Sanchez',31,'EMP004','asistente')

usuario1=Usuario('55555555E','Juan','Perez',21)
usuario2=Usuario('66666666F','Laura','Diaz',19)

genero1=Genero('Fantasía')
genero2=Genero('Ciencia ficción')