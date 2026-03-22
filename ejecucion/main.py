from ejecucion.casos_uso import agregar_libro_biblio, eliminar_libro_biblio, mostrar_info_biblio, crear_libro_fisico, \
    crear_libro_digital, reportar_condicion_libro, buscar_titulo_libro, mostrar_info_libro, crear_empleado, \
    crear_usuario, gestionar_registro_empleado, buscar_empleado, buscar_usuario, prestar_libro_usuario, \
    devolver_libro_usuario, mostrar_info_persona
from ejecucion.objetos import bd_biblioteca

def main():
    biblioteca=bd_biblioteca()
    print('Bienvenido a la Biblioteca Central')
    print('1. Consultar la biblioteca')
    print('2. Consultar libros')
    print('3. Consultar personas')
    print('4. Consultar géneros')
    print('5. Consultar datos existentes')
    print('6. Salir')
    eleccion=0
    while eleccion not in [1,2,3,4,5]:
        eleccion=int(input('¿Qué deseas hacer hoy? (Introduce un número): '))
        if eleccion not in [1,2,3,4,5]:
            print('Error: opción inválida')

    if eleccion==1:
        print('Consultar la biblioteca')
        print('1. Agregar libros ya existentes a la biblioteca')
        print('2. Eliminar libros de la biblioteca')
        print('3. Mostrar información de la biblioteca')
        sub_eleccion=0
        while sub_eleccion not in [1,2,3]:
            sub_eleccion=int(input('¿Qué deseas hacer hoy? (Introduce un número): '))
            if sub_eleccion not in [1,2,3]:
                print('Error: opción inválida')

        if sub_eleccion==1:
            titulo=input('Introduce el libro que deseas agregar: ')
            libro,validez=buscar_titulo_libro(titulo)
            if validez:
                agregar_libro_biblio(biblioteca,libro)
                print('Libro agregado correctamente')
            else:
                print('Libro no existente')

        elif sub_eleccion==2:
            titulo=input('Introduce el libro que deseas eliminar: ')
            libro,validez=buscar_titulo_libro(titulo)
            if validez:
                eliminar_libro_biblio(biblioteca,libro)
                print('Libro eliminado correctamente')
            else:
                print('Libro no existente')

        else:
            mostrar_info_biblio(biblioteca)

    elif eleccion==2:
        print('Consultar libros')
        print('1. Crear un libro físico')
        print('2. Crear un libro digital')
        print('3. Reportar la condición de un libro físico')
        print('4. Mostrar información de un libro')
        sub_eleccion=0
        while sub_eleccion not in [1,2,3,4]:
            sub_eleccion=int(input('¿Qué deseas hacer hoy? (Introduce un número): '))
            if sub_eleccion not in [1,2,3,4]:
                print('Error: opción inválida')

        if sub_eleccion==1:
            titulo=input('Introduce el titulo: ')
            autor=input('Introduce el autor: ')
            anyo=int(input('Introduce el año: '))
            estanteria=input('Introduce la estanteria: ')
            crear_libro_fisico(titulo,autor,anyo,estanteria)
            print(f'Libro físico "{titulo}" creado correctamente')

        elif sub_eleccion==2:
            titulo=input('Introduce el titulo: ')
            autor=input('Introduce el autor: ')
            anyo=int(input('Introduce el año: '))
            formato=input('Introduce el formato: ')
            url=input('Introduce el url: ')
            crear_libro_digital(titulo,autor,anyo,formato,url)
            print(f'Libro digital "{titulo}" creado correctamente')

        elif sub_eleccion==3:
            titulo=input('Introduce el libro: ')
            condicion=input('Introduce la nueva condición: ')
            libro,validez=buscar_titulo_libro(titulo)
            if validez:
                reportar_condicion_libro(libro,condicion)
                print('Condición reportada correctamente')
            else:
                print('Libro no existente')

        else:
            titulo=input('Introduce el libro: ')
            libro,validez=buscar_titulo_libro(titulo)
            if validez:
                mostrar_info_libro(libro)
            else:
                print('Libro no existente')

    elif eleccion==3:
        print('Consultar personas')
        print('1. Crear un empleado')
        print('2. Crear un usuario')
        print('3. Gestionar registros (solo para empleados con roles correspondientes)')
        print('4. Prestar un libro')
        print('5. Devolver un libro')
        print('6. Mostrar información de una persona')
        sub_eleccion=0
        while sub_eleccion not in [1,2,3,4,5,6]:
            sub_eleccion=int(input('¿Qué deseas hacer hoy? (Introduce un número): '))
            if sub_eleccion not in [1,2,3,4,5,6]:
                print('Error: opción inválida')

        if sub_eleccion==1:
            dni=input('Introduce el DNI: ')
            nombre=input('Introduce el nombre: ')
            apellido=input('Introduce el apellido: ')
            edad=input('Introduce la edad: ')
            id_empleado=input('Introduce el id: ')
            puesto=input('Introduce el puesto: ')
            crear_empleado(dni,nombre,apellido,edad,id_empleado,puesto)
            print(f'Empleado {nombre} {apellido} creado correctamente')

        elif sub_eleccion==2:
            dni=input('Introduce el DNI: ')
            nombre=input('Introduce el nombre: ')
            apellido=input('Introduce el apellido: ')
            edad=input('Introduce la edad: ')
            crear_usuario(dni,nombre,apellido,edad)
            print(f'Usuario {nombre} {apellido} creado correctamente')

        elif sub_eleccion==3:
            titulo=input('Introduce el libro: ')
            empleado=input('Introduce el dni del empleado: ')
            libro,validez=buscar_titulo_libro(titulo)
            if validez:
                dni,validez=buscar_empleado(empleado)
                if validez:
                    gestionar_registro_empleado(dni,biblioteca,libro)
                else:
                    print('Empleado no existente')
            else:
                print('Libro no existente')

        elif sub_eleccion==4:
            titulo=input('Introduce el libro: ')
            usuario=input('Introduce el DNI del usuario: ')
            libro,validez=buscar_titulo_libro(titulo)
            if validez:
                dni,validez=buscar_usuario(usuario)
                if validez:
                    prestar_libro_usuario(dni,libro)
                else:
                    print('Usuario no existente')
            else:
                print('Libro no existente')

        elif sub_eleccion==5:
            titulo=input('Introduce el libro: ')
            usuario=input('Introduce el DNI del usuario: ')
            libro,validez=buscar_titulo_libro(titulo)
            if validez:
                dni,validez=buscar_usuario(usuario)
                if validez:
                    devolver_libro_usuario(dni,libro)
                else:
                    print('Usuario no existente')
            else:
                print('Libro no existente')

        elif sub_eleccion==6:
            persona=input('Introduce el dni de la persona: ')
            dni,validez=buscar_empleado(persona)
            if validez:
                mostrar_info_persona(dni)
            else:
                dni,validez=buscar_usuario(persona)
                if validez:
                    mostrar_info_persona(dni)
                else:
                    print('Persona no existente')











if __name__=='__main__':
    main()