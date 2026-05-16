from clases.biblioteca.biblioteca import Biblioteca
from clases.libro_local.fisico_libro import Fisico
from clases.libro_local.digital_libro import Digital
from clases.persona_local.empleado_persona import Empleado
from clases.persona_local.usuario_persona import Usuario
from clases.genero.genero import Genero

#Datos: libros
libro_fis1: Fisico = Fisico('Don Quijote de la Mancha', 'Miguel de Cervantes', 1605, 'A1')
libro_fis2: Fisico = Fisico('1984', 'George Orwell', 1949, 'B2')
libro_dig1: Digital = Digital('Clean Code', 'Robert C. Martin', 2008, 'PDF', 'https://descarga.com/cleancode')
libro_dig2: Digital = Digital('Python Crash Course', 'Eric Matthes', 2019, 'EPUB', 'https://biblioteca.com/pythoncrashcourse')

bd_libros: list = [libro_fis1, libro_fis2, libro_dig1, libro_dig2]

#Datos: empleados
empleado1: Empleado = Empleado('11111111A', 'Ana', 'Garcia', 35, 'EMP001', 'bibliotecario')
empleado2: Empleado = Empleado('44444444D', 'Carlos', 'Sanchez', 31, 'EMP004', 'asistente')

bd_empleados: list = [empleado1, empleado2]

#Datos: usuarios
usuario1: Usuario = Usuario('55555555E', 'Juan', 'Perez', 21)
usuario2: Usuario = Usuario('66666666F', 'Laura', 'Diaz', 19)

bd_usuarios: list = [usuario1, usuario2]

#Datos: géneros
genero1: Genero = Genero('Fantasía')
genero2: Genero = Genero('Ciencia ficción')

bd_generos: list = [genero1, genero2]

#Datos: la Biblioteca Central
biblioteca_central: Biblioteca = Biblioteca('Biblioteca Central')

for ijk in bd_libros:
    biblioteca_central.agregar_libro(ijk)