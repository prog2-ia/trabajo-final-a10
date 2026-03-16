'''
from objetos import *

def main():
    #Colores para diferenciar textos y códigos
    violeta="\033[35m"
    yellow="\033[33m"
    reset="\033[0m"
    print()

    #Clase biblioteca
    print(violeta,'CLASE BIBLIOTECA:',reset)
    biblioteca_central.agregar_libro(libro1) #Agregar un libro a la biblioteca
    biblioteca_central.agregar_libro(libro2)
    biblioteca_central.agregar_libro(libro3)
    biblioteca_central.agregar_libro(libro4)
    biblioteca_central.agregar_libro(libro5)
    biblioteca_central.agregar_libro(libro6)
    print(yellow,'Biblioteca después de agregar libros:',reset)
    print(biblioteca_central.mostrar_info()) #Comprobación
    biblioteca_central.eliminar_libro(libro6) #Eliminar un libro de la biblioteca
    print(yellow,'Biblioteca después de eliminar un libro:',reset)
    print(biblioteca_central.mostrar_info()) #Comprobación
    print()

    #Clase libro y sus subclases
    print(violeta,'CLASE LIBRO Y SUS SUBCLASES:',reset)
    print(yellow,'Mostrar informaciones de libros:',reset)
    print(libro1.mostrar_info()) #Mostrar información de un libro físico
    print(libro6.mostrar_info()) #Mostrar información de un libro digital
    print(yellow,'Actualizar la condición de un libro:',reset)
    libro1.reportar_condicion('Mala') #Repostar la condición de un libro
    print(libro1.mostrar_info()) #Comprobación
    print()

    #Clase persona y sus subclases
    print(violeta,'CLASE PERSONA Y SUS SUBCLASES:',reset)
    print(yellow,'Prestar un libro:',reset)
    usuario1.prestar_libro(libro1) #Prestar un libro, cambiar su estado a "Prestado" y añadir este a la lista de libros prestados
    print(libro1.mostrar_info()) #Comprobación
    print(yellow,'Devolver un libro:',reset)
    usuario1.devolver_libro(libro1) #Devolver un libro, cambiar su estado a "Disponible" y quitar este a la lista de libros prestados
    print(libro1.mostrar_info()) #Comprobación
    print(yellow,'Mostrar información de un empleado y gestionar un libro:',reset)
    print(empleado1.mostrar_info()) #Mostrar información de un empleado
    empleado1.gestionar_registro(biblioteca_central,libro6) #Gestionar un libro para una biblioteca (añadirlo)
    print(yellow,'Mostrar información de un empleado y gestionar un libro, pero en este caso no se puede:',reset)
    print(empleado1.mostrar_info())
    print(empleado4.mostrar_info()) #Mostrar información de un empleado
    empleado4.gestionar_registro(biblioteca_central,libro3) #En este caso no le deja, ya que tiene el puesto "asistente"
    print(yellow,'Comprobación de los libros de la biblioteca:',reset)
    print(biblioteca_central.mostrar_info()) #Comprobación de los libros de la biblioteca
    print()

    #Clase género
    print(violeta,'CLASE GÉNERO:',reset)
    print(yellow,'Agregar libros en el género:',reset)
    genero1.agregar(libro1,biblioteca_central) #Agregar un libro al género, ya que por defecto no tiene ningún género
    genero1.agregar(libro2,biblioteca_central)
    print(genero1.mostrar_info()) #Comprobación
    print(yellow,'Prueba de que los libros ya tienen género:',reset)
    print(libro1.mostrar_info())
    print(libro2.mostrar_info())

if __name__ == '__main__':
    main()
'''