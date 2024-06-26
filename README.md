# Gestión de Biblioteca

Esta es una aplicación de gestión de biblioteca desarrollada en Python utilizando Tkinter para la interfaz gráfica y SQLite para la base de datos.

## Requisitos

- Python 3.x
- Tkinter (suele venir preinstalado con Python)

## Configuración del Entorno

### 1. Clonar el Repositorio

Abre una terminal y ejecuta el siguiente comando para clonar el repositorio:

```sh
git clone https://github.com/SGNinja/ProyectoPythonTecno3F.git
cd ProyectoPythonTecno3F
```

### 2. Crear un Entorno Virtual (*)

Abre una terminal y ejecuta los siguientes comandos:

```sh
python3 -m venv venv
```

### 3. Activar el Entorno Virtual (*)

- En Windows:

```sh
venv\Scripts\activate
```

- En macOS/Linux:

```sh
source venv/bin/activate
```
### 4. Instalar Dependencias (*)

Ejecuta el siguiente comando para instalar las dependencias requeridas:

```sh
pip install -r requirements.txt
```

#### (*) **NOTA**: Los pasos 2, 3 y 4 no son necesarios para esta versión de la aplicación, quizás en futuras versiones.

## Crear la Base de Datos

### Crear la Base de Datos Vacía

Ejecuta el siguiente script para crear la base de datos y las tablas necesarias:

```sh
python3 crear_db.py
```

### Crear la Base de Datos con Datos de Ejemplo (Opcional)

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
│   ├── database.py
│   ├── autor.py
│   ├── categoria.py
│   └── libro.py
├── gui/
│   ├── app.py
│   ├── libros_tab.py
│   ├── autores_tab.py
│   └── categorias_tab.py
├── utils/
│   └── theme_manager.py
├── crear_db.py
├── crear_db_con_ejemplos.py
├── requeriments.txt
└── README.md
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
- **utils/theme_manager.py**: Define una clase para manejar el cambio de temas (claro y oscuro).
- **crear_db.py**: Script para crear la base de datos vacía.
- **crear_db_con_ejemplos.py**: Script para crear la base de datos con datos de ejemplo.
- **requeriments.txt**: Dependencias necesarias (por ahora está vacío).
- **README.md**: Este archivo.

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
- **Cambiar Tema**: Permite cambiar entre un tema claro y un tema oscuro para la interfaz gráfica.

## Mejoras Futuras

- Añadir validaciones de datos.
- Mejorar la interfaz gráfica.
- Añadir funcionalidades de búsqueda y filtrado.
- Implementar la funcionalidad de actualización.

# Tecno 3F - Proyecto Final
## Python Intermedio
Este trabajo es parte del curso de Python intermedio de Tecno3F, dictado por **Gabriel Sebastian Roman**.
**Alumno:** Sebastian Gil
