from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clientes')
def clientes():
    return render_template('clientes.html')


if __name__ == '_main_':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Crear tabla si no existe
def init_db():
    conn = sqlite3.connect('base_datos.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    correo TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    precio REAL)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

# Clientes
@app.route('/clientes')
def clientes():
    conn = sqlite3.connect('base_datos.db')
    c = conn.cursor()
    c.execute("SELECT * FROM clientes")
    clientes = c.fetchall()
    conn.close()
    return render_template('clientes.html', clientes=clientes)

@app.route('/agregar_cliente', methods=['POST'])
def agregar_cliente():
    nombre = request.form['nombre']
    correo = request.form['correo']
    conn = sqlite3.connect('base_datos.db')
    c = conn.cursor()
    c.execute("INSERT INTO clientes (nombre, correo) VALUES (?, ?)", (nombre, correo))
    conn.commit()
    conn.close()
    return redirect(url_for('clientes'))

@app.route('/eliminar_cliente/<int:id>')
def eliminar_cliente(id):
    conn = sqlite3.connect('base_datos.db')
    c = conn.cursor()
    c.execute("DELETE FROM clientes WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('clientes'))

# Productos
@app.route('/productos')
def productos():
    conn = sqlite3.connect('base_datos.db')
    c = conn.cursor()
    c.execute("SELECT * FROM productos")
    productos = c.fetchall()
    conn.close()
    return render_template('productos.html', productos=productos)

@app.route('/agregar_producto', methods=['POST'])
def agregar_producto():
    nombre = request.form['nombre']
    precio = request.form['precio']
    conn = sqlite3.connect('base_datos.db')
    c = conn.cursor()
    c.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)", (nombre, precio))
    conn.commit()
    conn.close()
    return redirect(url_for('productos'))

@app.route('/eliminar_producto/<int:id>')
def eliminar_producto(id):
    conn = sqlite3.connect('base_datos.db')
    c = conn.cursor()
    c.execute("DELETE FROM productos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('productos'))

@app.route('/producto')
def productos():
    return render_template('producto.html')

# Facturación
@app.route('/factura', methods=['GET', 'POST'])
def factura():
    conn = sqlite3.connect('base_datos.db')
    c = conn.cursor()
    c.execute("SELECT * FROM clientes")
    clientes = c.fetchall()
    c.execute("SELECT * FROM productos")
    productos = c.fetchall()
    conn.close()

    if request.method == 'POST':
        cliente_id = request.form['cliente']
        producto_ids = request.form.getlist('producto')
        conn = sqlite3.connect('base_datos.db')
        c = conn.cursor()
        c.execute("SELECT nombre FROM clientes WHERE id = ?", (cliente_id,))
        cliente_nombre = c.fetchone()[0]
        productos_seleccionados = []
        total = 0
        for pid in producto_ids:
            c.execute("SELECT nombre, precio FROM productos WHERE id = ?", (pid,))
            nombre, precio = c.fetchone()
            productos_seleccionados.append((nombre, precio))
            total += precio
        conn.close()
        return render_template('factura.html', cliente=cliente_nombre, productos=productos_seleccionados, total=total)

    return render_template('factura.html', clientes=clientes, productos=productos)

if __name__ == '_main_':
    init_db()
    app.run(debug=True)


