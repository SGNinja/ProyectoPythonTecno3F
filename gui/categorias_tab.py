import tkinter as tk
from tkinter import ttk
from database.categoria import Categoria
import tkinter.font as tkFont

class CategoriasTab:
    def __init__(self, notebook, db):
        self.db = db
        self.categoria = Categoria(db)
        self.frame = ttk.Frame(notebook)
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.frame, text="Nombre", anchor='w').grid(row=0, column=0, sticky='w')
        self.categoria_nombre_entry = tk.Entry(self.frame, width=40)
        self.categoria_nombre_entry.grid(row=0, column=1, sticky='w')

        button_frame = tk.Frame(self.frame)
        button_frame.grid(row=1, column=0, columnspan=2, pady=10)
        tk.Button(button_frame, text="Agregar Categoría", command=self.agregar_categoria).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Eliminar Categoría", command=self.eliminar_categoria).pack(side=tk.LEFT, padx=5)

        # Lista de categorías
        self.categorias_tree = ttk.Treeview(self.frame, columns=("ID", "Nombre"), show='headings')
        self.categorias_tree.heading("ID", text="ID")
        self.categorias_tree.heading("Nombre", text="Nombre")
        self.categorias_tree.grid(row=2, column=0, columnspan=2, sticky='nsew')

        # Hacer que la tabla sea ajustable
        self.frame.grid_rowconfigure(2, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

        # Etiqueta para mostrar el total de categorías
        self.total_categorias_label = tk.Label(self.frame, text="Total de Categorías Registradas: 0", anchor='e')
        self.total_categorias_label.grid(row=3, column=1, sticky='e', padx=10, pady=10)

        self.actualizar_lista_categorias()

    def agregar_categoria(self):
        nombre = self.categoria_nombre_entry.get()
        self.categoria.agregar(nombre)
        self.actualizar_lista_categorias()

    def eliminar_categoria(self):
        selected = self.categorias_tree.selection()
        if selected:
            categoria_id = self.categorias_tree.item(selected[0])['values'][0]
            self.categoria.eliminar(categoria_id)
            self.actualizar_lista_categorias()

    def actualizar_lista_categorias(self):
        for row in self.categorias_tree.get_children():
            self.categorias_tree.delete(row)
        categorias = self.categoria.ver_todos()
        for categoria in categorias:
            self.categorias_tree.insert("", "end", values=categoria)
        self.autoajustar_columnas(self.categorias_tree)
        self.actualizar_total_categorias()

    def actualizar_total_categorias(self):
        total_categorias = len(self.categorias_tree.get_children())
        self.total_categorias_label.config(text=f"Total de Categorías Registradas: {total_categorias}")

    def autoajustar_columnas(self, treeview):
        for col in treeview["columns"]:
            max_width = max(tkFont.Font().measure(treeview.heading(col, 'text')),
                            max(tkFont.Font().measure(treeview.set(item, col)) for item in treeview.get_children()))
            treeview.column(col, width=max_width, stretch=True)