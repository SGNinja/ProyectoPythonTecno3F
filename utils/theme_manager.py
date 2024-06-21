import tkinter as tk
from tkinter import ttk

class ThemeManager:
    def __init__(self, root):
        self.root = root

    def set_claro(self):
        self.root.tk_setPalette(background='#f0f0f0', foreground='#000000', activeBackground='#e0e0e0', activeForeground='#000000')
        self.update_theme('default')

    def set_oscuro(self):
        self.root.tk_setPalette(background='#2e2e2e', foreground='#ffffff', activeBackground='#3e3e3e', activeForeground='#ffffff')
        self.update_theme('dark')

    def update_theme(self, theme):
        style = ttk.Style()
        if theme == 'dark':
            style.theme_use('clam')
            style.configure('TFrame', background='#2e2e2e')
            style.configure('TLabel', background='#2e2e2e', foreground='#ffffff')
            style.configure('TButton', background='#3e3e3e', foreground='#ffffff')
            style.configure('TNotebook', background='#2e2e2e', foreground='#ffffff')
            style.configure('TNotebook.Tab', background='#3e3e3e', foreground='#ffffff')
            style.configure('Treeview', background='#2e2e2e', foreground='#ffffff', fieldbackground='#2e2e2e')
            style.map('Treeview', background=[('selected', '#3e3e3e')], foreground=[('selected', '#ffffff')])
        else:
            style.theme_use('default')
            style.configure('TFrame', background='#f0f0f0')
            style.configure('TLabel', background='#f0f0f0', foreground='#000000')
            style.configure('TButton', background='#e0e0e0', foreground='#000000')
            style.configure('TNotebook', background='#f0f0f0', foreground='#000000')
            style.configure('TNotebook.Tab', background='#e0e0e0', foreground='#000000')
            style.configure('Treeview', background='#ffffff', foreground='#000000', fieldbackground='#ffffff')
            style.map('Treeview', background=[('selected', '#e0e0e0')], foreground=[('selected', '#000000')])
