from gui.app import App
from database.database import Database
import tkinter as tk

if __name__ == "__main__":
    db = Database('biblioteca.db')
    db.create_tables()
    root = tk.Tk()
    app = App(root, db)
    root.mainloop()
    db.close()