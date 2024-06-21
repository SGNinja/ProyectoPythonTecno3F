import sqlite3

def crear_db():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS autores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            apellido TEXT,
            nacionalidad TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            autor_id INTEGER,
            categoria_id INTEGER,
            fecha_publicacion DATE,
            FOREIGN KEY (autor_id) REFERENCES autores(id),
            FOREIGN KEY (categoria_id) REFERENCES categorias(id)
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    crear_db()