import tkinter as tk
from tkinter import ttk
from database.autor import Autor
import tkinter.font as tkFont

class AutoresTab:
    def __init__(self, notebook, db):
        self.db = db
        self.autor = Autor(db)
        self.frame = ttk.Frame(notebook)
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.frame, text="Nombre", anchor='w').grid(row=0, column=0, sticky='w')
        self.autor_nombre_entry = tk.Entry(self.frame, width=40)
        self.autor_nombre_entry.grid(row=0, column=1, sticky='w')

        tk.Label(self.frame, text="Apellido", anchor='w').grid(row=1, column=0, sticky='w')
        self.autor_apellido_entry = tk.Entry(self.frame, width=40)
        self.autor_apellido_entry.grid(row=1, column=1, sticky='w')

        tk.Label(self.frame, text="Nacionalidad", anchor='w').grid(row=2, column=0, sticky='w')
        self.autor_nacionalidad_entry = tk.Entry(self.frame, width=40)
        self.autor_nacionalidad_entry.grid(row=2, column=1, sticky='w')

        button_frame = tk.Frame(self.frame)
        button_frame.grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(button_frame, text="Agregar Autor", command=self.agregar_autor).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Eliminar Autor", command=self.eliminar_autor).pack(side=tk.LEFT, padx=5)

        # Lista de autores
        self.autores_tree = ttk.Treeview(self.frame, columns=("ID", "Nombre", "Apellido", "Nacionalidad"), show='headings')
        self.autores_tree.heading("ID", text="ID")
        self.autores_tree.heading("Nombre", text="Nombre")
        self.autores_tree.heading("Apellido", text="Apellido")
        self.autores_tree.heading("Nacionalidad", text="Nacionalidad")
        self.autores_tree.grid(row=4, column=0, columnspan=2, sticky='nsew')

        # Hacer que la tabla sea ajustable
        self.frame.grid_rowconfigure(4, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

        self.actualizar_lista_autores()

    def agregar_autor(self):
        nombre = self.autor_nombre_entry.get()
        apellido = self.autor_apellido_entry.get()
        nacionalidad = self.autor_nacionalidad_entry.get()
        self.autor.agregar(nombre, apellido, nacionalidad)
        self.actualizar_lista_autores()

    def eliminar_autor(self):
        selected = self.autores_tree.selection()
        if selected:
            autor_id = self.autores_tree.item(selected[0])['values'][0]
            self.autor.eliminar(autor_id)
            self.actualizar_lista_autores()

    def actualizar_lista_autores(self):
        for row in self.autores_tree.get_children():
            self.autores_tree.delete(row)
        autores = self.autor.ver_todos()
        for autor in autores:
            self.autores_tree.insert("", "end", values=autor)
        self.autoajustar_columnas(self.autores_tree)

    def autoajustar_columnas(self, treeview):
        for col in treeview["columns"]:
            max_width = max(tkFont.Font().measure(treeview.heading(col, 'text')),
                            max(tkFont.Font().measure(treeview.set(item, col)) for item in treeview.get_children()))
            treeview.column(col, width=max_width, stretch=True)