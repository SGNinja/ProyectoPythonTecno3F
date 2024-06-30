import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS autores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                apellido TEXT,
                nacionalidad TEXT
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS categorias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT
            )
        ''')
        self.cursor.execute('''
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
        self.conn.commit()

    def execute_query(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()

    def fetch_all(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def fetch_one(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def close(self):
        self.conn.close()

    def get_or_create_autor(self, nombre, apellido, nacionalidad):
        autor = self.fetch_one('SELECT id FROM autores WHERE nombre = ? AND apellido = ?', (nombre, apellido))
        if autor:
            return autor[0]
        else:
            self.execute_query('INSERT INTO autores (nombre, apellido, nacionalidad) VALUES (?, ?, ?)', (nombre, apellido, nacionalidad))
            return self.cursor.lastrowid

    def get_or_create_categoria(self, nombre):
        categoria = self.fetch_one('SELECT id FROM categorias WHERE nombre = ?', (nombre,))
        if categoria:
            return categoria[0]
        else:
            self.execute_query('INSERT INTO categorias (nombre) VALUES (?)', (nombre,))
            return self.cursor.lastrowid
