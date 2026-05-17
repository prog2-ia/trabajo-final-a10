from clases.biblioteca.biblioteca import Biblioteca
from clases.valoracion.valoracion import Valoracion

#Listas que contienen datos iniciales (vacías al principio, pero después se rellenan en el main)
bd_libros: list = []
bd_empleados: list = []
bd_usuarios: list = []
bd_generos: list = []

#Datos: la Biblioteca Central
biblioteca_central: Biblioteca = Biblioteca('Biblioteca Central')

for ijk in bd_libros:
    biblioteca_central.agregar_libro(ijk)

#Datos: valoraciones
sistema_valoraciones: Valoracion = Valoracion()