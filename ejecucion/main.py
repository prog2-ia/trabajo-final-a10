from ejecucion.casos_uso import agregar_libro_biblio, eliminar_libro_biblio, mostrar_info_biblio, crear_libro_fisico, \
    crear_libro_digital, reportar_condicion_libro, buscar_titulo_libro, mostrar_info_libro, crear_empleado, \
    crear_usuario, gestionar_registro_empleado, buscar_empleado, buscar_usuario, prestar_libro_usuario, \
    devolver_libro_usuario, mostrar_info_persona, crear_genero, agregar_libro_genero, buscar_genero, mostrar_info_genero
from ejecucion.objetos import biblioteca_central, bd_libros, bd_empleados, bd_usuarios, bd_generos

def main():
    while True:
        print('Bienvenido a la Biblioteca Central')
        print('1. Consultar la biblioteca')
        print('2. Consultar libros')
        print('3. Consultar personas y préstamos')
        print('4. Consultar géneros')
        print('5. Consultar datos existentes')
        print('6. Salir')
        eleccion=0
        while eleccion not in [1,2,3,4,5,6]:
            eleccion=int(input('¿Qué deseas hacer hoy? (Introduce un número): '))
            if eleccion not in [1,2,3,4,5,6]:
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
                    agregar_libro_biblio(biblioteca_central,libro)
                    print('Libro agregado correctamente')
                else:
                    print('Libro no existente')

            elif sub_eleccion==2:
                titulo=input('Introduce el libro que deseas eliminar: ')
                libro,validez=buscar_titulo_libro(titulo)
                if validez:
                    eliminar_libro_biblio(biblioteca_central,libro)
                    print('Libro eliminado correctamente')
                else:
                    print('Libro no existente')

            else:
                mostrar_info_biblio(biblioteca_central)

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
                print(f'Empleado "{nombre} {apellido}" creado correctamente')

            elif sub_eleccion==2:
                dni=input('Introduce el DNI: ')
                nombre=input('Introduce el nombre: ')
                apellido=input('Introduce el apellido: ')
                edad=input('Introduce la edad: ')
                crear_usuario(dni,nombre,apellido,edad)
                print(f'Usuario "{nombre} {apellido}" creado correctamente')

            elif sub_eleccion==3:
                titulo=input('Introduce el libro: ')
                empleado=input('Introduce el dni del empleado: ')
                libro,validez=buscar_titulo_libro(titulo)
                if validez:
                    dni,validez=buscar_empleado(empleado)
                    if validez:
                        gestionar_registro_empleado(dni,biblioteca_central,libro)
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
                persona=input('Introduce el DNI de la persona: ')
                dni,validez=buscar_empleado(persona)
                if validez:
                    mostrar_info_persona(dni)
                else:
                    dni,validez=buscar_usuario(persona)
                    if validez:
                        mostrar_info_persona(dni)
                    else:
                        print('Persona no existente')

        elif eleccion==4:
            print('Consultar géneros')
            print('1. Crear un género')
            print('2. Agregar un género a un libro')
            print('3. Mostrar información de un género')
            sub_eleccion=0
            while sub_eleccion not in [1,2,3]:
                sub_eleccion=int(input('¿Qué deseas hacer hoy? (Introduce un número): '))
                if sub_eleccion not in [1,2,3]:
                    print('Error: opción inválida')

            if sub_eleccion==1:
                genero=input('Introduce el nombre del género: ')
                crear_genero(genero)
                print(f'Género "{genero}" creado correctamente')

            elif sub_eleccion==2:
                titulo=input('Introduce el libro: ')
                nombre_gen=input('Introduce el nombre del género: ')
                libro,validez=buscar_titulo_libro(titulo)
                if validez:
                    genero,validez=buscar_genero(nombre_gen)
                    if validez:
                        agregar_libro_genero(genero,libro,biblioteca_central)
                        print(f'Libro "{titulo}" agregado al género "{nombre_gen}" correctamente')
                    else:
                        print('Género no existente')
                else:
                    print('Libro no existente')

            else:
                nombre_gen=input('Introduce el nombre del género: ')
                genero,validez=buscar_genero(nombre_gen)
                if validez:
                    mostrar_info_genero(genero)
                else:
                    print('Género no existente')

        elif eleccion==5:
            print('Consultar datos existentes')
            print('1. Libros')
            print('2. Empleados')
            print('3. Usuarios')
            print('4. Géneros')
            sub_eleccion=0
            while sub_eleccion not in [1,2,3,4,5]:
                sub_eleccion=int(input('¿Qué deseas hacer hoy? (Introduce un número): '))
                if sub_eleccion not in [1,2,3,4,5]:
                    print('Error: opción inválida')

            if sub_eleccion==1:
                for i in bd_libros:
                    if i==bd_libros[-1]:
                        print(i.titulo)
                    else:
                        print(i.titulo,end=' | ')

            elif sub_eleccion==2:
                for i in bd_empleados:
                    if i==bd_empleados[-1]:
                        print(i.nombre,i.apellido)
                    else:
                        print(i.nombre,i.apellido,end=' | ')

            elif sub_eleccion==3:
                for i in bd_usuarios:
                    if i==bd_usuarios[-1]:
                        print(i.nombre,i.apellido)
                    else:
                        print(i.nombre,i.apellido,end=' | ')

            elif sub_eleccion==4:
                for i in bd_generos:
                    if i==bd_generos[-1]:
                        print(i.nombre)
                    else:
                        print(i.nombre,end=' | ')

        else:
            break

if __name__=='__main__':
    main()