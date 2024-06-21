from tkinter import messagebox
from database.database import Database

class Libro:
    def __init__(self, db: Database):
        self.db = db

    def agregar(self, titulo, autor_id, categoria_id, fecha_publicacion):
        self.db.execute_query('''
            INSERT INTO libros (titulo, autor_id, categoria_id, fecha_publicacion)
            VALUES (?, ?, ?, ?)
        ''', (titulo, autor_id, categoria_id, fecha_publicacion))
        messagebox.showinfo("Éxito", "Libro agregado exitosamente")

    def ver_todos(self):
        return self.db.fetch_all('''
            SELECT libros.id, libros.titulo, 
                   CASE 
                       WHEN NULLIF(autores.nombre, '') IS NOT NULL AND NULLIF(autores.apellido, '') IS NOT NULL THEN autores.apellido || ', ' || autores.nombre
                       WHEN NULLIF(autores.nombre, '') IS NOT NULL THEN autores.nombre
                       WHEN NULLIF(autores.apellido, '') IS NOT NULL THEN autores.apellido
                       ELSE 'Dato Desconocido'
                   END AS autor, 
                   CASE 
                       WHEN NULLIF(categorias.nombre, '') IS NOT NULL THEN categorias.nombre
                       ELSE 'Dato Desconocido'
                   END AS categoria, 
                   CASE 
                       WHEN NULLIF(libros.fecha_publicacion, '') IS NOT NULL THEN libros.fecha_publicacion
                       ELSE 'Dato Desconocido'
                   END AS fecha_publicacion
            FROM libros
            JOIN autores ON libros.autor_id = autores.id
            JOIN categorias ON libros.categoria_id = categorias.id
        ''')

    def eliminar(self, id):
        self.db.execute_query('DELETE FROM libros WHERE id = ?', (id,))
        messagebox.showinfo("Éxito", "Libro eliminado exitosamente")
