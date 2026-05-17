# Sistema de Gestión de Biblioteca Inteligente 📚

Este proyecto es una simulación de un **sistema de gestión de biblioteca inteligente** desarrollado en **Python 3** utilizando **programación orientada a objetos (POO)** y una arquitectura modular.

El sistema permite gestionar:

- libros físicos y digitales,
- usuarios y empleados,
- préstamos,
- géneros literarios,
- persistencia de datos mediante ficheros binarios,
- y exportación de información en archivos de texto.

---

# 📂 Estructura del proyecto

```plaintext
trabajo-final-a10/
│
├─ clases/
│   │
│   ├─ biblioteca/
│   │   └─ biblioteca.py
│   │
│   ├─ genero/
│   │   └─ genero.py
│   │
│   ├─ libro_local/
│   │   ├─ libro_local.py
│   │   ├─ fisico_libro.py
│   │   └─ digital_libro.py
│   │
│   ├─ persona_local/
│   │   ├─ persona_local.py
│   │   ├─ empleado_persona.py
│   │   └─ usuario_persona.py
│   │
│   ├─ prestamo/
│   │   └─ prestamos.py
│   │
│   └─ valoracion/
│       └─ valoracion.py
│
├─ ejecucion/
│   ├─ biblioteca.dat
│   ├─ casos_uso.py
    ├─ main.py
│   └─ objetos.py
│
├─ README.md
└─ requirements.txt
```

---

# 🧩 Componentes principales

## 📚 Biblioteca

La clase `Biblioteca` representa la biblioteca principal del sistema y permite gestionar:

- libros disponibles,
- registros,
- consultas,
- y organización general de recursos.

---

# 📖 Libros

El sistema implementa una jerarquía de libros basada en herencia.

## Libro físico (`Fisico`)

Representa un libro físico almacenado en la biblioteca.

Incluye:

- ubicación en estantería,
- condición física,
- disponibilidad.

---

## Libro digital (`Digital`)

Representa un recurso digital.

Incluye:

- formato del archivo,
- enlace o URL,
- disponibilidad digital.

---

## Clase base `Libro`

Ambos tipos de libros heredan de una clase base común que contiene:

- título,
- autor,
- año,
- género,
- estado.

---

# 👥 Personas

El sistema distingue entre diferentes tipos de usuarios.

## Usuario

Puede:

- consultar libros,
- solicitar préstamos,
- devolver libros.

---

## Empleado

Además de las capacidades básicas, puede:

- gestionar registros,
- administrar recursos,
- controlar operaciones internas.

Cada empleado dispone de:

- ID de empleado,
- rol o puesto dentro de la biblioteca.

---

# 🏷️ Géneros

Los libros pueden clasificarse mediante géneros literarios.

Cada género permite:

- agrupar libros,
- organizar colecciones,
- consultar información asociada.

---

# 🔄 Persistencia de datos

El proyecto utiliza **ficheros binarios** mediante el módulo `pickle` para guardar automáticamente el estado del sistema.

Los datos persistentes incluyen:

- libros,
- usuarios,
- empleados,
- géneros.

La información se almacena en:

```plaintext
ejecucion/biblioteca.dat
```

---

# 📄 Exportación de datos

El sistema permite exportar información de la biblioteca mediante archivos de texto (`.txt`).

Ejemplos de información exportable:

- libros registrados,
- usuarios,
- empleados,
- géneros,
- informes generales del sistema.

---

# ⚠️ Manejo de excepciones

El proyecto implementa control de excepciones para:

- entradas inválidas,
- errores de conversión numérica,
- archivos inexistentes,
- carga de datos persistentes.

---

# 🛠️ Instalación y ejecución

## 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/prog2-ia/trabajo-final-a10.git
cd trabajo-final-a10
```

---

## 2️⃣ Instalar Python 3

### Linux

```bash
sudo apt update
sudo apt install python3 python3-pip
```

---

## 3️⃣ Instalar dependencias

El proyecto no requiere librerías externas.

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Ejecutar el sistema

Desde la raíz del proyecto:

```bash
python3 -m ejecucion.main
```

---

# ▶️ Uso del sistema

Al ejecutar el programa se mostrará un menú interactivo con opciones como:

- consultar libros,
- registrar usuarios,
- realizar préstamos,
- gestionar géneros,
- exportar información.

---

# 📚 Ejemplos de uso

## 📖 Crear un libro físico

```plaintext
Consultar libros
1. Crear un libro físico
2. Crear un libro digital
3. Reportar la condición de un libro físico
4. Mostrar información de un libro
5. Volver

¿Qué deseas hacer hoy? (Introduce un número): 1

Introduce el titulo: La Celestina
Introduce el autor: Fernando de Rojas
Introduce el año: 1500
Introduce la estanteria: A2

Libro físico "La Celestina" creado correctamente
```

---

## 🔍 Consultar un libro

```plaintext
Consultar libros
1. Crear un libro físico
2. Crear un libro digital
3. Reportar la condición de un libro físico
4. Mostrar información de un libro
5. Volver

¿Qué deseas hacer hoy? (Introduce un número): 4

Introduce el libro: Don Quijote de la Mancha

Título: Don Quijote de la Mancha
Autor: Miguel de Cervantes
Año: 1605
Estado: Disponible
Ubicación: Estantería A1
Condición: Excelente
```

---

## 📄 Exportar información

```plaintext
¿Qué deseas hacer hoy? (Introduce un número): 6

Datos exportados con éxito
```

---

# 🛠️ Tecnologías utilizadas

- Python 3
- Programación Orientada a Objetos (POO)
- Persistencia con `pickle`
- Ficheros de texto (`.txt`)
- Arquitectura modular

---

# 👨‍💻 Autoría

Proyecto desarrollado por el grupo **A10** para la asignatura de **Programación II**.

---

# 📄 Licencia

Proyecto desarrollado con fines académicos y educativos.