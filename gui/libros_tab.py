import tkinter as tk
from tkinter import ttk
from database.libro import Libro
import tkinter.font as tkFont

class LibrosTab:
    def __init__(self, notebook, db):
        self.db = db
        self.libro = Libro(db)
        self.frame = ttk.Frame(notebook)
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.frame, text="Título", anchor='w').grid(row=0, column=0, sticky='w')
        self.titulo_entry = tk.Entry(self.frame, width=40)
        self.titulo_entry.grid(row=0, column=1, sticky='w')

        tk.Label(self.frame, text="Autor", anchor='w').grid(row=1, column=0, sticky='w')
        self.autor_combobox = ttk.Combobox(self.frame, width=38)
        self.autor_combobox.grid(row=1, column=1, sticky='w')
        self.actualizar_autores_combobox()

        tk.Label(self.frame, text="Categoría", anchor='w').grid(row=2, column=0, sticky='w')
        self.categoria_combobox = ttk.Combobox(self.frame, width=38)
        self.categoria_combobox.grid(row=2, column=1, sticky='w')
        self.actualizar_categorias_combobox()

        tk.Label(self.frame, text="Fecha de Publicación", anchor='w').grid(row=3, column=0, sticky='w')
        self.fecha_publicacion_entry = tk.Entry(self.frame, width=40)
        self.fecha_publicacion_entry.grid(row=3, column=1, sticky='w')

        button_frame = tk.Frame(self.frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(button_frame, text="Agregar Libro", command=self.agregar_libro).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Eliminar Libro", command=self.eliminar_libro).pack(side=tk.LEFT, padx=5)

        # Lista de libros
        self.libros_tree = ttk.Treeview(self.frame, columns=("ID", "Título", "Autor", "Categoría", "Fecha de Publicación"), show='headings')
        self.libros_tree.heading("ID", text="ID")
        self.libros_tree.heading("Título", text="Título")
        self.libros_tree.heading("Autor", text="Autor")
        self.libros_tree.heading("Categoría", text="Categoría")
        self.libros_tree.heading("Fecha de Publicación", text="Fecha de Publicación")
        self.libros_tree.grid(row=5, column=0, columnspan=2, sticky='nsew')

        # Hacer que la tabla sea ajustable
        self.frame.grid_rowconfigure(5, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

        self.actualizar_lista_libros()

    def agregar_libro(self):
        titulo = self.titulo_entry.get()
        autor_nombre_completo = self.autor_combobox.get()
        categoria_nombre = self.categoria_combobox.get()
        fecha_publicacion = self.fecha_publicacion_entry.get()

        # Separar el nombre completo en nombre y apellido
        autor_nombre, autor_apellido = autor_nombre_completo.split(' ', 1) if ' ' in autor_nombre_completo else (autor_nombre_completo, '')

        # Buscar el autor existente en la base de datos
        autor_id = self.db.fetch_one('SELECT id FROM autores WHERE nombre = ? AND apellido = ?', (autor_nombre, autor_apellido))
        if autor_id:
            autor_id = autor_id[0]
        else:
            autor_id = self.db.get_or_create_autor(autor_nombre, autor_apellido, "")

        categoria_id = self.db.get_or_create_categoria(categoria_nombre)

        self.libro.agregar(titulo, autor_id, categoria_id, fecha_publicacion)
        self.actualizar_lista_libros()

    def eliminar_libro(self):
        selected = self.libros_tree.selection()
        if selected:
            libro_id = self.libros_tree.item(selected[0])['values'][0]
            self.libro.eliminar(libro_id)
            self.actualizar_lista_libros()

    def actualizar_lista_libros(self):
        for row in self.libros_tree.get_children():
            self.libros_tree.delete(row)
        libros = self.libro.ver_todos()
        for libro in libros:
            self.libros_tree.insert("", "end", values=libro)
        self.autoajustar_columnas(self.libros_tree)

    def actualizar_autores_combobox(self):
        autores = self.db.fetch_all('SELECT * FROM autores')
        autor_nombres = [f"{autor[1]} {autor[2]}" for autor in autores]
        self.autor_combobox['values'] = autor_nombres

    def actualizar_categorias_combobox(self):
        categorias = self.db.fetch_all('SELECT * FROM categorias')
        categoria_nombres = [categoria[1] for categoria in categorias]
        self.categoria_combobox['values'] = categoria_nombres

    def autoajustar_columnas(self, treeview):
        for col in treeview["columns"]:
            max_width = max(tkFont.Font().measure(treeview.heading(col, 'text')),
                            max(tkFont.Font().measure(treeview.set(item, col)) for item in treeview.get_children()))
            treeview.column(col, width=max_width, stretch=True)