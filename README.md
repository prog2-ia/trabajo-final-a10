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
│   │   ├─ favoritos.py
│   │   └─ valoracion.py
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
    ├─ casos_uso.py
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

## 🛠️ Instalación y ejecución

Sigue estos pasos para configurar y ejecutar el proyecto en Linux:

### 1️⃣ Clonar el repositorio

```plaintext
git clone https://github.com/prog2-ia/trabajo-final-a10.git
cd trabajo-final-a10
```

### 2️⃣ Instalar Python (solo si no lo tienes, en este caso vamos a usar python 3)

```plaintext
sudo apt update
sudo apt install python3 python3-pip
```

### 3️⃣ Instalar dependencias (en este caso no es necesario, ya que el proyecto no requiere ninguna)

```plaintext
pip3 install -r requirements.txt
```

### 4️⃣ Ejecutar el programa

Desde la raíz del proyecto:

```plaintext
python3 -m ejecucion.main
```

---

## ▶️ Uso

Una vez ejecutado el programa:

```plaintext
python3 -m ejecucion.main
```

El sistema mostrará un menú con las distintas opciones disponibles como consultar libros, prestar un libro, etc.

---

## 📚 Ejemplos

### 📖 Añadir un libro

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

### 🔍 Buscar un libro

```plaintext
Consultar libros
1. Crear un libro físico
2. Crear un libro digital
3. Reportar la condición de un libro físico
4. Mostrar información de un libro
5. Volver
¿Qué deseas hacer hoy? (Introduce un número): 4
Introduce el libro: Don Quijote de la Mancha
Título: Don Quijote de la Mancha | Autor: Miguel de Cervantes | Año: 1605 | Género: Sin género | Estado: Disponible | Ubicación: Estantería A1 | Condición: Excelente
```

---

## 🛠️ Tecnologías utilizadas

* **Python 3**
* Programación Orientada a Objetos (POO)
* Organización modular de código

---

## 👨‍💻 Autor

Proyecto desarrollado por el grupo A10 para la asignatura de Programación II.

---

## 📄 Licencia

Este proyecto es de uso académico y educativo.