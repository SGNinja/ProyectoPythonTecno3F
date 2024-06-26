import tkinter as tk
from tkinter import ttk, messagebox
from gui.libros_tab import LibrosTab
from gui.autores_tab import AutoresTab
from gui.categorias_tab import CategoriasTab
from utils.theme_manager import ThemeManager  # Importar ThemeManager

class App:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.theme_manager = ThemeManager(root)  # Crear una instancia de ThemeManager
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

        # Menú Tema
        tema_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Tema", menu=tema_menu)
        tema_menu.add_command(label="Claro", command=self.theme_manager.set_claro)
        tema_menu.add_command(label="Oscuro", command=self.theme_manager.set_oscuro)

        # Menú Ayuda
        ayuda_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Ayuda", menu=ayuda_menu)
        ayuda_menu.add_command(label="About", command=self.mostrar_about)

        notebook = ttk.Notebook(self.root)
        notebook.pack(expand=1, fill='both')

        # Manejo de errores en caso de DB vacia
        try:
            # Pestaña para agregar libros
            self.tab_libros = LibrosTab(notebook, self.db)
            notebook.add(self.tab_libros.frame, text='Libros')

            # Pestaña para agregar autores
            self.tab_autores = AutoresTab(notebook, self.db)
            notebook.add(self.tab_autores.frame, text='Autores')

            # Pestaña para agregar categorías
            self.tab_categorias = CategoriasTab(notebook, self.db)
            notebook.add(self.tab_categorias.frame, text='Categorías')
        except Exception as e:
            messagebox.showinfo("Base de datos vacía", "La base de datos se encuentra vacía. Por favor, agregue algunos registros.")
            label = tk.Label(self.root, text="La base de datos está vacía. Use las opciones de menú para agregar registros.")
            label.pack(pady=20)

    def mostrar_about(self):
        messagebox.showinfo("About", "Gestión de Biblioteca\nAutor: Sebastian Gil\nEmpresa: Tecno3F")