# Gestión de Biblioteca

Esta es una aplicación de gestión de biblioteca desarrollada en Python utilizando Tkinter para la interfaz gráfica y SQLite para la base de datos.

## Requisitos

- Python 3.x
- Tkinter (suele venir preinstalado con Python)

## Configuración del Entorno

### 1. Crear un Entorno Virtual

Abre una terminal y ejecuta los siguientes comandos:

```sh
python3 -m venv venv
```

### 2. Activar el Entorno Virtual

- En Windows:

```sh
venv\Scripts\activate
```

- En macOS/Linux:

```sh
source venv/bin/activate
```

## Crear la Base de Datos

### Crear la Base de Datos Vacía

Ejecuta el siguiente script para crear la base de datos y las tablas necesarias:

```sh
python3 crear_db.py
```

### Crear la Base de Datos con Datos de Ejemplo

Ejecuta el siguiente script para crear la base de datos con datos de ejemplo:

```sh
python3 crear_db_con_ejemplos.py
```

## Ejecutar la Aplicación

Ejecuta el siguiente comando para iniciar la aplicación:

```sh
python3 app.py
```

## Estructura del Proyecto

```sh
/
├── app.py
├── database/
│   ├── __init__.py
│   ├── database.py
│   ├── autor.py
│   ├── categoria.py
│   └── libro.py
├── gui/
│   ├── __init__.py
│   ├── app.py
│   ├── libros_tab.py
│   ├── autores_tab.py
│   └── categorias_tab.py
└── crear_db.py
└── crear_db_con_ejemplos.py
└── README.md
└── requeriments.txt
```

- **app.py**: Este archivo inicializa la base de datos, crea la ventana principal de Tkinter y lanza la aplicación.
- **database/database.py**: Define la clase `Database` que maneja la conexión a la base de datos SQLite y proporciona métodos para crear tablas, ejecutar consultas y obtener o crear autores y categorías.
- **database/autor.py**: Define la clase `Autor` que maneja las operaciones relacionadas con los autores en la base de datos.
- **database/categoria.py**: Define la clase `Categoria` que maneja las operaciones relacionadas con las categorías en la base de datos.
- **database/libro.py**: Define la clase `Libro` que maneja las operaciones relacionadas con los libros en la base de datos.
- **gui/app.py**: Define la clase `App` que maneja la ventana principal de la aplicación y configura las pestañas para libros, autores y categorías.
- **gui/libros_tab.py**: Funcionalidad de la pestaña de libros.
- **gui/autores_tab.py**: Funcionalidad de la pestaña de autores.
- **gui/categorias_tab.py**: Funcionalidad de la pestaña de categorías.
- **crear_db.py**: Script para crear la base de datos vacía.
- **crear_db_con_ejemplos.py**: Script para crear la base de datos con datos de ejemplo.
- **README.md**: Este archivo.
- **requeriments.txt**: Dependencias necesarias (Por ahora esta vacio).

## Funcionalidades

- **Agregar Libro**: Permite agregar un nuevo libro a la base de datos.
- **Eliminar Libro**: Permite eliminar un libro de la base de datos.
- **Ver Libros**: Muestra una lista de todos los libros en la base de datos.
- **Agregar Autor**: Permite agregar un nuevo autor a la base de datos.
- **Eliminar Autor**: Permite eliminar un autor de la base de datos.
- **Ver Autores**: Muestra una lista de todos los autores en la base de datos.
- **Agregar Categoría**: Permite agregar una nueva categoría a la base de datos.
- **Eliminar Categoría**: Permite eliminar una categoría de la base de datos.
- **Ver Categorías**: Muestra una lista de todas las categorías en la base de datos.

## Mejoras Futuras

- Añadir validaciones de datos.
- Mejorar la interfaz gráfica.
- Añadir funcionalidades de búsqueda y filtrado.
- Implementar la funcionalidad de actualización.

# Tecno 3F - Proyecto Final
## Python Intermedio
Este trabajo es parte del curso de Python intermedio de Tecno3F, dictado por **Gabriel Sebastian Roman**.
**Alumno:** Sebastian Gil
