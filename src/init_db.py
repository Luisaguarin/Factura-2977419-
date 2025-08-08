import sqlite3
import os

os.makedirs('database', exist_ok=True)

def crear_db_clientes():
    conn = sqlite3.connect(os.path.join('database', 'clientes.db'))
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT,
            telefono TEXT
        )
    ''')
    conn.commit()
    conn.close()

def crear_db_productos():
    conn = sqlite3.connect(os.path.join('database', 'productos.db'))
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            cantidad INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '_main_':
    crear_db_clientes()
    crear_db_productos()
    print("✅ Bases de datos inicializadas correctamente.")
    
# Asegurar que el directorio exista
os.makedirs('database', exist_ok=True)


# Crear la base de datos si no existe
db_path = os.path.join('database', 'clientes.db')
conn = sqlite3.connect(db_path)

# Crear tabla clientes
conn.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        correo TEXT,
        telefono TEXT
    )
''')

conn.commit()
conn.close()

print("Base de datos de clientes inicializada.")

# Crear la base de datos si no existe
db_path = os.path.join('database', 'productos.db')
conn = sqlite3.connect(db_path)

# Crear tabla productos
conn.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL,
        stock INTEGER
    )
''')

conn.commit()
conn.close()

print("Base de datos de productos inicializada.")