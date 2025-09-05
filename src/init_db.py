import sqlite3


conn = sqlite3.connect('basededatos.db')  
c = conn.cursor()


c.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        correo TEXT,
        telefono TEXT
    )
''')

conn.commit()
conn.close()

print("Tabla 'clientes' creada exitosamente.")