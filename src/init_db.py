import sqlite3

# Conecta a la base de datos (usa el mismo nombre de archivo que en app.py)
conn = sqlite3.connect('basededatos.db')  # asegúrate de que este sea el archivo correcto
c = conn.cursor()

# Crea la tabla clientes
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