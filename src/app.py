from flask import Flask
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

if __name__ == '_main_':
    app.run()
    
    
@app.route('/')
def home():
    return render_template('layout.html')

@app.route("/clientes")
def clientes():
    return render_template('clientes.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')

@app.route('/formulario_producto')
def formulario_producto():
    return render_template('formulario_producto.html')

@app.route('/lista_productos')
def lista_productos():
    return render_template('lista_productos.html')

@app.route('/agregar_producto', methods=['POST'])
def agregar_producto():
    return redirect(url_for('productos'))

@app.route('/agregar_cliente', methods=['POST'])
def agregar_cliente():
    return redirect(url_for('clientes')) 

@app.route('/editar', methods=['POST'])
def editar():
    return render_template('editar.html')


@app.route('/submit', methods=['POST'])
def submit():
    nombre = request.form['nombre']
    email = request.form['email']
    telefono = request.form['telefono']
    mensaje = request.form['mensaje']
    # Aquí puedes procesar los datos, como guardarlos en una base de datos
    return f'Formulario enviado! Nombre: {nombre}, Email: {email}, Teléfono: {telefono}, Mensaje: {mensaje}'

if __name__ == '__main__':
    app.run(debug=True)
   
    