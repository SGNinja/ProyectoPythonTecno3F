from tkinter import messagebox
from database.database import Database

class Categoria:
    def __init__(self, db: Database):
        self.db = db

    def agregar(self, nombre):
        self.db.execute_query('''
            INSERT INTO categorias (nombre)
            VALUES (?)
        ''', (nombre,))
        messagebox.showinfo("Éxito", "Categoría agregada exitosamente")

    def ver_todos(self):
        return self.db.fetch_all('SELECT * FROM categorias')

    def eliminar(self, id):
        self.db.execute_query('DELETE FROM categorias WHERE id = ?', (id,))
        messagebox.showinfo("Éxito", "Categoría eliminada exitosamente")