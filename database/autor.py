from tkinter import messagebox
from database.database import Database

class Autor:
    def __init__(self, db: Database):
        self.db = db

    def agregar(self, nombre, apellido, nacionalidad):
        self.db.execute_query('''
            INSERT INTO autores (nombre, apellido, nacionalidad)
            VALUES (?, ?, ?)
        ''', (nombre, apellido, nacionalidad))
        messagebox.showinfo("Éxito", "Autor agregado exitosamente")

    def ver_todos(self):
        return self.db.fetch_all('SELECT * FROM autores')

    def eliminar(self, id):
        self.db.execute_query('DELETE FROM autores WHERE id = ?', (id,))
        messagebox.showinfo("Éxito", "Autor eliminado exitosamente")
