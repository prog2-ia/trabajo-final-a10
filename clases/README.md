# Sistema de Gestión de Biblioteca 📚

Este proyecto es una simulación sencilla de un **sistema de gestión de biblioteca** desarrollado en Python utilizando **programación orientada a objetos (POO)**.
Permite modelar distintos elementos de una biblioteca como libros físicos y digitales, usuarios, empleados y géneros.

---

## 📂 Estructura del proyecto

El proyecto está organizado en módulos para separar las diferentes entidades del sistema.

```
proyecto/
│
├─ clases/
│   ├─ biblioteca/
│   │   └─ biblioteca.py
│   │
│   ├─ genero/
│   │   ├─ genero.py
│   │   ├─ favoritos_genero.py
│   │   └─ valoracion_genero.py
│   │
│   ├─ libro/
│   │   ├─ libro_local.py
│   │   ├─ fisico_libro.py
│   │   └─ digital_libro.py
│   │
│   └─ persona/
│       ├─ persona.py
│       ├─ empleado_persona.py
│       └─ usuario_persona.py
│
└─ ejecucion/
    ├─ main.py
    └─ objetos.py
```

---

## 🧩 Componentes principales

### Biblioteca

Representa la biblioteca principal donde se gestionan los diferentes elementos del sistema.

### Libros

Existen dos tipos de libros:

* **Libro físico** (`Fisico`)
  Contiene información sobre la ubicación en la biblioteca.

* **Libro digital** (`Digital`)
  Incluye el formato del archivo y el enlace de descarga.

Ambos heredan de la clase base `Libro`.

---

### Personas

El sistema distingue entre dos tipos de personas:

* **Empleado**

  * Tiene un ID de empleado
  * Tiene un rol dentro de la biblioteca

* **Usuario**

  * Puede interactuar con los recursos de la biblioteca

Ambos heredan de la clase base `Persona`.

---

### Géneros

Los libros pueden clasificarse por **género literario**, que se gestiona mediante las clases dentro del módulo `genero`.

---

## ▶️ Ejecución del programa

1. Descargar o clonar el proyecto completo.

2. Abrir una terminal en la carpeta raíz del proyecto.

3. Ejecutar el programa con:

```bash
python ejecucion/main.py
```

---

## 🛠️ Tecnologías utilizadas

* **Python 3**
* Programación Orientada a Objetos (POO)
* Organización modular de código

---

## 🎯 Objetivo del proyecto

El objetivo de este proyecto es practicar:

* Diseño de clases y herencia
* Organización de proyectos en Python
* Importación de módulos entre carpetas
* Modelado de sistemas mediante POO

---

## 👨‍💻 Autor

Proyecto desarrollado con fines educativos para practicar **estructura de proyectos en Python y programación orientada a objetos**.
