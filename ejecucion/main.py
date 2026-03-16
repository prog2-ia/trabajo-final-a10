from objetos import (
    biblioteca_central,
    libro1,libro2,libro3,libro4,libro5,libro6,
    usuario1,
    empleado1,empleado4,
    genero1
)

def main():
    #Colores para diferenciar textos y códigos
    YELLOW = "\033[33m"
    GREEN = "\033[32m"
    RESET = "\033[0m"
    print()

    #Clase biblioteca
    print(GREEN,'CLASE BIBLIOTECA:',RESET)
    biblioteca_central.agregar_libro(libro1) #Agregar un libro a la biblioteca
    biblioteca_central.agregar_libro(libro2)
    biblioteca_central.agregar_libro(libro3)
    biblioteca_central.agregar_libro(libro4)
    biblioteca_central.agregar_libro(libro5)
    biblioteca_central.agregar_libro(libro6)
    print(YELLOW,'Biblioteca después de agregar libros:',RESET)
    print(biblioteca_central.mostrar_info()) #Comprobación
    biblioteca_central.eliminar_libro(libro6) #Eliminar un libro de la biblioteca
    print(YELLOW,'Biblioteca después de eliminar un libro:',RESET)
    print(biblioteca_central.mostrar_info()) #Comprobación
    print()

    #Clase libro y sus subclases
    print(GREEN,'CLASE LIBRO Y SUS SUBCLASES:',RESET)
    print(YELLOW,'Mostrar informaciones de libros:',RESET)
    print(libro1.mostrar_info()) #Mostrar información de un libro físico
    print(libro6.mostrar_info()) #Mostrar información de un libro digital
    print(YELLOW,'Actualizar la condición de un libro:',RESET)
    libro1.reportar_condicion('mala') #Repostar la condición de un libro
    print(libro1.mostrar_info()) #Comprobación
    print()

    #Clase persona y sus subclases
    print(GREEN,'CLASE PERSONA Y SUS SUBCLASES:',RESET)
    print(YELLOW,'Prestar un libro:',RESET)
    usuario1.prestar_libro(libro1) #Prestar un libro, cambiar su estado a "Prestado" y añadir este a la lista de libros prestados
    print(libro1.mostrar_info()) #Comprobación
    print(YELLOW,'Devolver un libro:',RESET)
    usuario1.devolver_libro(libro1) #Devolver un libro, cambiar su estado a "Disponible" y quitar este a la lista de libros prestados
    print(libro1.mostrar_info()) #Comprobación
    print(YELLOW,'Mostrar información de un empleado y gestionar un libro:',RESET)
    print(empleado1.mostrar_info()) #Mostrar información de un empleado
    empleado1.gestionar_registro(biblioteca_central,libro6) #Gestionar un libro para una biblioteca (añadirlo)
    print(YELLOW,'Mostrar información de un empleado y gestionar un libro, pero en este caso no se puede:',RESET)
    print(empleado1.mostrar_info())
    print(empleado4.mostrar_info()) #Mostrar información de un empleado
    empleado4.gestionar_registro(biblioteca_central,libro3) #En este caso no le deja, ya que tiene el puesto "asistente"
    print(YELLOW,'Comprobación de los libros de la biblioteca:',RESET)
    print(biblioteca_central.mostrar_info()) #Comprobación de los libros de la biblioteca
    print()

    #Clase género
    print(GREEN,'CLASE GÉNERO:',RESET)
    print(YELLOW,'Agregar libros en el género:',RESET)
    genero1.agregar(libro1,biblioteca_central) #Agregar un libro al género, ya que por defecto no tiene ningún género
    genero1.agregar(libro2,biblioteca_central)
    print(genero1.mostrar_info()) #Comprobación
    print(YELLOW,'Prueba de que los libros ya tienen género:',RESET)
    print(libro1.mostrar_info())
    print(libro2.mostrar_info())

if __name__ == '__main__':
    main()