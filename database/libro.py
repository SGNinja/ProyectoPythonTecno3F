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
            SELECT libros.id, libros.titulo, autores.apellido || ', ' || autores.nombre AS autor, categorias.nombre AS categoria, libros.fecha_publicacion
            FROM libros
            JOIN autores ON libros.autor_id = autores.id
            JOIN categorias ON libros.categoria_id = categorias.id
        ''')

    def eliminar(self, id):
        self.db.execute_query('DELETE FROM libros WHERE id = ?', (id,))
        messagebox.showinfo("Éxito", "Libro eliminado exitosamente")