import tkinter as tk
from tkinter import ttk, messagebox
from gui.libros_tab import LibrosTab
from gui.autores_tab import AutoresTab
from gui.categorias_tab import CategoriasTab

class App:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.root.title("Gestión de Biblioteca")
        self.root.geometry("800x600")  # Ajustar el tamaño de la ventana
        self.create_widgets()

    def create_widgets(self):
        # Crear la barra de menú
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        # Menú Archivo
        archivo_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Archivo", menu=archivo_menu)
        archivo_menu.add_command(label="Salir", command=self.root.quit)

        # Menú Ayuda
        ayuda_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=ayuda_menu)
        ayuda_menu.add_command(label="About", command=self.mostrar_about)

        notebook = ttk.Notebook(self.root)
        notebook.pack(expand=1, fill='both')

        # Pestaña para agregar libros
        self.tab_libros = LibrosTab(notebook, self.db)
        notebook.add(self.tab_libros.frame, text='Libros')

        # Pestaña para agregar autores
        self.tab_autores = AutoresTab(notebook, self.db)
        notebook.add(self.tab_autores.frame, text='Autores')

        # Pestaña para agregar categorías
        self.tab_categorias = CategoriasTab(notebook, self.db)
        notebook.add(self.tab_categorias.frame, text='Categorías')

    def mostrar_about(self):
        messagebox.showinfo("About", "Gestión de Biblioteca\nAutor: Sebastian Gil\nEmpresa: Tecno3F")