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

    # Insertar autores
    autores = [
        ('George', 'Orwell', 'Gran Bretaña'),
        ('J.K.', 'Rowling', 'Gran Bretaña'),
        ('J.R.R.', 'Tolkien', 'Gran Bretaña'),
        ('Gabriel', 'García Márquez', 'Colombia'),
        ('Jane', 'Austen', 'Gran Bretaña'),
        ('Mark', 'Twain', 'Estados Unidos'),
        ('F. Scott', 'Fitzgerald', 'Estados Unidos'),
        ('Ernest', 'Hemingway', 'Estados Unidos'),
        ('Leo', 'Tolstoy', 'Rusia'),
        ('Homer', '', 'Grecia')
    ]
    cursor.executemany('''
        INSERT INTO autores (nombre, apellido, nacionalidad)
        VALUES (?, ?, ?)
    ''', autores)
    conn.commit()

    # Insertar categorías
    categorias = [
        ('Ficción'),
        ('Fantasía'),
        ('Clásico'),
        ('Realismo Mágico'),
        ('Aventura'),
        ('Literatura'),
        ('Épico')
    ]
    cursor.executemany('''
        INSERT INTO categorias (nombre)
        VALUES (?)
    ''', [(categoria,) for categoria in categorias])
    conn.commit()

    # Obtener IDs de autores y categorías
    cursor.execute('SELECT id, nombre, apellido FROM autores')
    autores_dict = {f"{nombre} {apellido}".strip(): id for id, nombre, apellido in cursor.fetchall()}

    cursor.execute('SELECT id, nombre FROM categorias')
    categorias_dict = {nombre: id for id, nombre in cursor.fetchall()}

    # Insertar libros
    libros = [
        ('1984', autores_dict['George Orwell'], categorias_dict['Ficción'], '1949-06-08'),
        ('Harry Potter y la piedra filosofal', autores_dict['J.K. Rowling'], categorias_dict['Fantasía'], '1997-06-26'),
        ('El Señor de los Anillos', autores_dict['J.R.R. Tolkien'], categorias_dict['Fantasía'], '1954-07-29'),
        ('Cien años de soledad', autores_dict['Gabriel García Márquez'], categorias_dict['Realismo Mágico'], '1967-05-30'),
        ('Orgullo y prejuicio', autores_dict['Jane Austen'], categorias_dict['Clásico'], '1813-01-28'),
        ('Las aventuras de Tom Sawyer', autores_dict['Mark Twain'], categorias_dict['Aventura'], '1876-06-14'),
        ('El gran Gatsby', autores_dict['F. Scott Fitzgerald'], categorias_dict['Clásico'], '1925-04-10'),
        ('El viejo y el mar', autores_dict['Ernest Hemingway'], categorias_dict['Literatura'], '1952-09-01'),
        ('Guerra y paz', autores_dict['Leo Tolstoy'], categorias_dict['Clásico'], '1869-01-01'),
        ('La Ilíada', autores_dict['Homer'], categorias_dict['Épico'], '800-01-01')
    ]
    cursor.executemany('''
        INSERT INTO libros (titulo, autor_id, categoria_id, fecha_publicacion)
        VALUES (?, ?, ?, ?)
    ''', libros)
    conn.commit()

    conn.close()

if __name__ == "__main__":
    crear_db()